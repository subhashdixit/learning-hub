# SQL practical questions: basics, windows and business cases

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Use the table creation and four-row dataset in the SQL theory guide. These answers run in SQLite; each has a specific expected result. Solve first, then open the answer.

## Easy 1. What is total revenue?

<details><summary>Answer</summary>

```sql
SELECT SUM(amount) AS revenue FROM orders;
```

Expected: 530.
</details>

## Easy 2. Which customers ordered more than once?

<details><summary>Answer</summary>

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders GROUP BY customer_id HAVING COUNT(*) > 1;
```

Expected: customer 101, 2 orders.
</details>

## Medium 3. Return the largest order in each region

<details><summary>Answer</summary>

```sql
WITH ranked AS (
 SELECT *, ROW_NUMBER() OVER (
  PARTITION BY region ORDER BY amount DESC, order_id
 ) AS rn FROM orders
)
SELECT order_id, region, amount FROM ranked WHERE rn = 1 ORDER BY region;
```

Expected: East order 2 (200), West order 3 (80). This selects one winner; `DENSE_RANK` on amount alone keeps all ties.
</details>

## Medium 4. Find each customer's previous order amount

<details><summary>Answer</summary>

```sql
SELECT order_id, customer_id, amount,
 LAG(amount) OVER (
  PARTITION BY customer_id ORDER BY order_date, order_id
 ) AS previous_amount
FROM orders ORDER BY order_id;
```

Expected: previous amounts NULL, 100, NULL, NULL. Do not replace the first missing predecessor with a fabricated order.
</details>

## Business case 5. Calculate East's revenue share

<details><summary>Answer</summary>

```sql
SELECT 1.0 * SUM(CASE WHEN region = 'East' THEN amount ELSE 0 END)
       / NULLIF(SUM(amount), 0) AS east_share
FROM orders;
```

Expected: 450/530 ≈ 0.849057. The denominator is all qualifying order revenue; change it if the business definition differs.
</details>

## Business case 6. Calculate monthly revenue growth

<details><summary>Answer</summary>

```sql
WITH monthly AS (
 SELECT substr(order_date, 1, 7) AS month, SUM(amount) AS revenue
 FROM orders GROUP BY substr(order_date, 1, 7)
), compared AS (
 SELECT month, revenue,
 LAG(revenue) OVER (ORDER BY month) AS previous_revenue FROM monthly
)
SELECT month, revenue,
 1.0 * (revenue - previous_revenue) / NULLIF(previous_revenue, 0) AS growth
FROM compared ORDER BY month;
```

Expected: January 380, growth NULL; February 150, growth about -0.605263. In a real dashboard, compare complete periods and use a calendar to represent absent months. A missing preceding month is not automatically a zero-sales month.
</details>

## Hard 7. Which rows are above their own regional average?

<details><summary>Answer</summary>

```sql
WITH scored AS (
 SELECT *, AVG(amount) OVER (PARTITION BY region) AS regional_average
 FROM orders
)
SELECT order_id FROM scored WHERE amount > regional_average ORDER BY order_id;
```

Expected: order 2 only. East's average is 150; a value equal to it is not above it.
</details>

## Hard 8. How would you test a join that doubles revenue?

<details><summary>Answer</summary>

Check uniqueness on both join keys and counts per order before joining. A one-to-many match can be valid but creates a new grain. Preaggregate each child table to order grain, join, then reconcile the total. `DISTINCT` is not a general repair: it can remove legitimate identical amounts.
</details>

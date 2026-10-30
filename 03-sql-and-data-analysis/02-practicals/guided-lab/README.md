# SQL —20 worked query problems

[Practicals](../README.md) · [Theory](../../01-theory/README.md)

Use SQLite 3.25+for window functions. The fixture is deliberately small so every output can be checked by hand. Other database dialects differ in dates, limits and some functions. Run `python3 lab.py` from this folder to execute all 20 checks.

## Sample data

```sql
CREATE TABLE customers(id INTEGER PRIMARY KEY,name TEXT NOT NULL);
CREATE TABLE orders(id INTEGER PRIMARY KEY,customer_id INTEGER,amount INTEGER,status TEXT,day TEXT);
INSERT INTO customers VALUES(1,'Asha'),(2,'Ben'),(3,'Chen'),(4,'Diya');
INSERT INTO orders VALUES(1,1,100,'paid','2026-01-01'),(2,1,50,'paid','2026-01-02'),(3,2,80,'refunded','2026-01-01'),(4,2,200,'paid','2026-01-03'),(5,3,NULL,'pending','2026-01-02'),(6,3,100,'paid','2026-01-04');
```

## 01. Paid orders — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id FROM orders WHERE status='paid' ORDER BY id;
```

Expected rows: `[(1,), (2,), (4,), (6,)]`.

Filter rows before aggregation.

</details>

## 02. Missing amount — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id FROM orders WHERE amount IS NULL;
```

Expected rows: `[(5,)]`.

Use IS NULL, not equality.

</details>

## 03. Count rows and known amounts — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT COUNT(*),COUNT(amount) FROM orders;
```

Expected rows: `[(6, 5)]`.

Missing and zero are different.

</details>

## 04. Paid total — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT SUM(amount) FROM orders WHERE status='paid';
```

Expected rows: `[(450,)]`.

The sum is at order grain.

</details>

## 05. Customers with multiple orders — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT customer_id FROM orders GROUP BY customer_id HAVING COUNT(*)>1 ORDER BY customer_id;
```

Expected rows: `[(1,), (2,), (3,)]`.

HAVING filters groups.

</details>

## 06. Amounts above 100 — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id FROM orders WHERE amount>100 ORDER BY id;
```

Expected rows: `[(4,)]`.

Strict greater-than excludes equal 100.

</details>

## 07. Conditional paid totals — Easy

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT customer_id,SUM(CASE WHEN status='paid' THEN amount ELSE 0 END) FROM orders GROUP BY customer_id ORDER BY customer_id;
```

Expected rows: `[(1, 150), (2, 200), (3, 100)]`.

The CASE defines eligible contribution.

</details>

## 08. Customers without any orders — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT c.id FROM customers c WHERE NOT EXISTS(SELECT 1 FROM orders o WHERE o.customer_id=c.id) ORDER BY c.id;
```

Expected rows: `[(4,)]`.

An anti-match does not require duplicated join rows.

</details>

## 09. Retain customers with zero paid orders — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT c.id,COUNT(o.id) FROM customers c LEFT JOIN orders o ON o.customer_id=c.id AND o.status='paid' GROUP BY c.id ORDER BY c.id;
```

Expected rows: `[(1, 2), (2, 1), (3, 1), (4, 0)]`.

The right-side filter belongs in ON to preserve unmatched customers.

</details>

## 10. Latest order per customer — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
WITH r AS(SELECT id,customer_id,ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY day DESC,id DESC) rn FROM orders) SELECT customer_id,id FROM r WHERE rn=1 ORDER BY customer_id;
```

Expected rows: `[(1, 2), (2, 4), (3, 6)]`.

Timestamp and ID define the winner.

</details>

## 11. Second distinct nonmissing amount — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT DISTINCT amount FROM orders WHERE amount IS NOT NULL ORDER BY amount DESC LIMIT 1 OFFSET 1;
```

Expected rows: `[(100,)]`.

DISTINCT makes the rank semantic explicit; absent second values return no row.

</details>

## 12. Running paid total — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id,SUM(amount) OVER(ORDER BY day,id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM orders WHERE status='paid' ORDER BY day,id;
```

Expected rows: `[(1, 100), (2, 150), (4, 350), (6, 450)]`.

Explicit frame and unique ordering define accumulation.

</details>

## 13. Previous paid amount — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id,LAG(amount) OVER(PARTITION BY customer_id ORDER BY day,id) FROM orders WHERE status='paid' ORDER BY customer_id,day,id;
```

Expected rows: `[(1, None), (2, 100), (4, None), (6, None)]`.

WHERE limits the window input to paid orders.

</details>

## 14. Customer paid-share of total — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
WITH a AS(SELECT customer_id,SUM(amount) total FROM orders WHERE status='paid' GROUP BY customer_id) SELECT customer_id,ROUND(1.0*total/SUM(total) OVER(),4) FROM a ORDER BY customer_id;
```

Expected rows: `[(1, 0.3333), (2, 0.4444), (3, 0.2222)]`.

Convert to noninteger arithmetic and state rounding.

</details>

## 15. Date totals — Medium

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT day,SUM(amount) FROM orders WHERE status='paid' GROUP BY day ORDER BY day;
```

Expected rows: `[('2026-01-01', 100), ('2026-01-02', 50), ('2026-01-03', 200), ('2026-01-04', 100)]`.

These ISO dates sort lexically here; production date types/dialects need explicit treatment.

</details>

## 16. Rank tied amounts — Hard

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id,RANK() OVER(ORDER BY amount DESC),DENSE_RANK() OVER(ORDER BY amount DESC) FROM orders WHERE amount IS NOT NULL ORDER BY amount DESC,id;
```

Expected rows: `[(4, 1, 1), (1, 2, 2), (6, 2, 2), (3, 4, 3), (2, 5, 4)]`.

RANK leaves a gap after the two 100 amounts.

</details>

## 17. Above customer average — Hard

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT o.id FROM orders o WHERE amount>(SELECT AVG(i.amount) FROM orders i WHERE i.customer_id=o.customer_id) ORDER BY o.id;
```

Expected rows: `[(1,), (4,)]`.

AVG ignores missing values; a customer with one known amount has no above-average order.

</details>

## 18. Distinct paying customers — Hard

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT COUNT(DISTINCT customer_id) FROM orders WHERE status='paid';
```

Expected rows: `[(3,)]`.

Four paid orders do not mean four paying customers.

</details>

## 19. Verify missing and zero separately — Hard

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT SUM(CASE WHEN amount IS NULL THEN 1 ELSE 0 END),SUM(CASE WHEN amount=0 THEN 1 ELSE 0 END) FROM orders;
```

Expected rows: `[(1, 0)]`.

Unknown amount is not known zero.

</details>

## 20. Paid amount with last-order annotation — Hard

Try it before expanding the solution.

<details>
<summary>Query, expected output and explanation</summary>

```sql
SELECT id,amount,MAX(day) OVER(PARTITION BY customer_id) FROM orders WHERE status='paid' ORDER BY id;
```

Expected rows: `[(1, 100, '2026-01-02'), (2, 50, '2026-01-02'), (4, 200, '2026-01-03'), (6, 100, '2026-01-04')]`.

The date annotation does not imply each row is the latest; use row filtering when that is the question.

</details>

## Extend the dataset

Add equal timestamps, duplicate business keys, zero amounts, customers without paid orders and an unmatched foreign key under a deliberately changed fixture. Predict which results should change. Use constraints when the contract should forbid a case; do not hide invalid data with DISTINCT.

## Recorded check

Executed on 2026-10-30 with Python 3.10. All embedded assertions passed. Small floating-point formatting differences are possible on other versions.

```text
Passed 20 SQL query checks on local SQLite 3.35.5
```

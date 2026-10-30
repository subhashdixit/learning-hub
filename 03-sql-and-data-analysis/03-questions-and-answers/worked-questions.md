# SQL and Data Analysis — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Tables, grain, keys, types and SELECT](#lesson-01)
- [02 — Filters, NULL, CASE, strings and dates](#lesson-02)
- [03 — GROUP BY, HAVING, conditional aggregation and weighted metrics](#lesson-03)
- [04 — Joins, EXISTS, subqueries, CTEs and set operations](#lesson-04)
- [05 — Windows, ranking, running totals and session patterns](#lesson-05)
- [06 — Data modelling, indexes, transactions and query plans](#lesson-06)
- [07 — EDA, missingness, duplicates and evidence quality](#lesson-07)
- [08 — Cohorts, funnels, experiments and analytical communication](#lesson-08)

<a id="lesson-01"></a>

## 01 — Tables, grain, keys, types and SELECT

[Read the lesson](../01-theory/lesson-01-relational-foundations.md)

### Q001. What is table grain?

<details>
<summary>Answer</summary>

The real-world unit represented by one row, such as an order or an order line.

</details>

### Q002. Why add a tie-breaker to ORDER BY?

<details>
<summary>Answer</summary>

To make equal-key output order deterministic where the task requires it.

</details>

### Q003. Does a foreign key automatically prevent every bad business record?

<details>
<summary>Answer</summary>

No. It checks a relationship, not all ranges, timing rules or business meaning.

</details>

<a id="lesson-02"></a>

## 02 — Filters, NULL, CASE, strings and dates

[Read the lesson](../01-theory/lesson-02-filters-and-null.md)

### Q004. Why is amount=NULL wrong?

<details>
<summary>Answer</summary>

Equality with unknown does not establish true; use IS NULL.

</details>

### Q005. COUNT(*) versus COUNT(amount)?

<details>
<summary>Answer</summary>

The first counts rows; the second only rows where amount is not NULL.

</details>

### Q006. Why can NOT IN fail with NULL?

<details>
<summary>Answer</summary>

The unknown comparison can prevent rows satisfying a simple true anti-match; NOT EXISTS often expresses the intention more safely.

</details>

<a id="lesson-03"></a>

## 03 — GROUP BY, HAVING, conditional aggregation and weighted metrics

[Read the lesson](../01-theory/lesson-03-aggregation-and-grain.md)

### Q007. WHERE versus HAVING?

<details>
<summary>Answer</summary>

WHERE filters input rows; HAVING filters aggregate groups.

</details>

### Q008. Why not average subgroup percentages blindly?

<details>
<summary>Answer</summary>

Their denominators can differ; an overall rate usually needs pooled numerators and denominators.

</details>

### Q009. How detect double-counted sums?

<details>
<summary>Answer</summary>

State grain, inspect key multiplicities before/after joins, and reconcile totals independently.

</details>

<a id="lesson-04"></a>

## 04 — Joins, EXISTS, subqueries, CTEs and set operations

[Read the lesson](../01-theory/lesson-04-joins-and-subqueries.md)

### Q010. Why COUNT(o.id) after a LEFT JOIN?

<details>
<summary>Answer</summary>

It counts matched non-NULL order keys, not the NULL-extended placeholder row.

</details>

### Q011. When use EXISTS?

<details>
<summary>Answer</summary>

When the question is whether any related match exists rather than how many matched combinations to return.

</details>

### Q012. Two duplicates on each side of a key: output count?

<details>
<summary>Answer</summary>

Four matching combinations, unless additional conditions change the relationship.

</details>

<a id="lesson-05"></a>

## 05 — Windows, ranking, running totals and session patterns

[Read the lesson](../01-theory/lesson-05-window-functions.md)

### Q013. Does a window reduce row count?

<details>
<summary>Answer</summary>

Not by itself. It computes values associated with each retained row.

</details>

### Q014. RANK versus DENSE_RANK?

<details>
<summary>Answer</summary>

Both give ties equal rank; RANK leaves gaps and DENSE_RANK does not.

</details>

### Q015. Why explicit frames?

<details>
<summary>Answer</summary>

They make row-based versus peer/time-based accumulation clear and reproducible.

</details>

<a id="lesson-06"></a>

## 06 — Data modelling, indexes, transactions and query plans

[Read the lesson](../01-theory/lesson-06-modeling-performance-transactions.md)

### Q016. Why fact grain before measures?

<details>
<summary>Answer</summary>

It determines which quantities can be summed and which joins preserve meaning.

</details>

### Q017. Does a CTE guarantee a faster query?

<details>
<summary>Answer</summary>

No. Execution depends on optimizer and engine semantics; inspect the actual plan and measurements.

</details>

### Q018. What does transaction atomicity mean?

<details>
<summary>Answer</summary>

The grouped database changes commit together or do not take effect as a committed partial operation.

</details>

<a id="lesson-07"></a>

## 07 — EDA, missingness, duplicates and evidence quality

[Read the lesson](../01-theory/lesson-07-eda-and-data-quality.md)

### Q019. Why define provenance?

<details>
<summary>Answer</summary>

It clarifies how selection, measurement and processing could bias the available evidence.

</details>

### Q020. Are repeated customer IDs duplicates?

<details>
<summary>Answer</summary>

Not in an order-grain table; uniqueness must be checked against the correct key.

</details>

### Q021. EDA versus confirmatory analysis?

<details>
<summary>Answer</summary>

EDA explores patterns and hypotheses; confirmation needs a specified design and valid inferential procedure.

</details>

<a id="lesson-08"></a>

## 08 — Cohorts, funnels, experiments and analytical communication

[Read the lesson](../01-theory/lesson-08-analysis-and-storytelling.md)

### Q022. Why fixed cohort denominators?

<details>
<summary>Answer</summary>

They preserve the original eligible group and prevent survivor-only retention inflation.

</details>

### Q023. Why distinguish absolute and relative effects?

<details>
<summary>Answer</summary>

A large relative change can correspond to a small absolute impact, depending on baseline.

</details>

### Q024. What makes an insight actionable?

<details>
<summary>Answer</summary>

It ties a measured comparison and its uncertainty to a concrete decision or justified next investigation.

</details>

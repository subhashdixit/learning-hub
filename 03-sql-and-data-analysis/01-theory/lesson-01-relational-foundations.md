# 01 — Tables, grain, keys, types and SELECT

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-01)

```mermaid
flowchart LR
 N0["Business unit per row"] --> N1["Keys and types"] --> N2["SELECT expressions"] --> N3["Ordered result"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A table is a ledger with a defined unit per row; SQL asks questions of that ledger.

Define grain before writing a query: one row per order differs from one row per order line. A primary key identifies a row; a foreign key links to another table under a declared relationship. Uniqueness, not-null and check constraints encode parts of the data contract. SQL tables do not have a guaranteed display order without ORDER BY.

SELECT chooses expressions, FROM supplies relations and WHERE filters rows. Use descriptive aliases and explicit selected columns for durable interfaces. Types matter: text dates can sort incorrectly if formats vary, and approximate floating-point amounts can be inappropriate for exact financial ledgers. Engine-specific numeric/date semantics need verification.

Relational thinking separates the question from the physical execution plan. A query's readable logical steps need not be the engine's execution order. The optimizer can reorder safe operations while preserving semantics. Before optimizing a query, check that it counts the intended unit and handles duplicate/missing keys.

## Work through it

All SQL snippets use the local sample database created in the practicals. It contains `customers(id,name)` and `orders(id,customer_id,amount,status,day)`.

```sql
SELECT id, amount, amount * 0.10 AS illustrative_tax
FROM orders
WHERE status = 'paid'
ORDER BY amount DESC, id;
```

The final id breaks equal-amount ties deterministically. The 10% rate is a teaching calculation, not a real tax rule.

## Common mistakes and practical limits

SELECT * hides schema assumptions. DISTINCT can conceal accidental duplicate joins rather than fixing them. Query results without ordering should be compared as relations, not assumed to arrive in insertion order.

---

[Subject home](../README.md) · [Filters, NULL, CASE, strings and dates →](lesson-02-filters-and-null.md)

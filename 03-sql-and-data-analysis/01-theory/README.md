# SQL and Data Analysis — theory in learning order

[Subject home](../README.md) · [Practicals](../02-practicals/README.md) · [Questions and answers](../03-questions-and-answers/README.md)

**[Algorithm story and family comparisons](ALGORITHM-STORY.md)** — understand the problem, mechanism, limitation and related alternatives.

Start with 01 and follow the numbered lessons. Each explains the idea in simple language, shows a worked example and identifies common mistakes. Run code examples and reproduce calculations before checking the answers.

**Sequence:** Grain → Query → Filter → Aggregate → Join → Windows → Data model → Analysis

1. [Tables, grain, keys, types and SELECT](lesson-01-relational-foundations.md)
2. [Filters, NULL, CASE, strings and dates](lesson-02-filters-and-null.md)
3. [GROUP BY, HAVING, conditional aggregation and weighted metrics](lesson-03-aggregation-and-grain.md)
4. [Joins, EXISTS, subqueries, CTEs and set operations](lesson-04-joins-and-subqueries.md)
5. [Windows, ranking, running totals and session patterns](lesson-05-window-functions.md)
6. [Data modelling, indexes, transactions and query plans](lesson-06-modeling-performance-transactions.md)
7. [EDA, missingness, duplicates and evidence quality](lesson-07-eda-and-data-quality.md)
8. [Cohorts, funnels, experiments and analytical communication](lesson-08-analysis-and-storytelling.md)

## Extended worked guides

These retained guides provide longer derivations and additional original-note examples. Use them when a lesson needs a deeper worked treatment; the numbered course above is the main reading route.

- [SQL: theory and code](01-sql.md)
- [Data analysis, EDA and feature engineering](02-eda.md)

## Primary references

These official texts/documentation support further detail and current API behaviour. The course examples are original teaching examples; check the installed version before using framework-specific APIs.

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [SQLite SQL reference](https://www.sqlite.org/lang.html)
- [pandas guide](https://pandas.pydata.org/docs/user_guide/index.html)

# 02 — Excel tables, formulas, lookups, pivots and reconciliation

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-02)

```mermaid
flowchart LR
 N0["Source table"] --> N1["Formulas or pivots"] --> N2["Key checks"] --> N3["Reconcile"] --> N4["Report"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A spreadsheet is executable analysis; formulas and manual cells need the same care as code.

Use structured tables, clear input/calculation/output separation and explicit units. Relative/absolute references change when formulas are copied. Lookup functions need a deliberate exact/approximate match policy and missing-key behaviour. Never assume a lookup key is unique without checking.

SUMIFS/COUNTIFS aggregate by criteria; pivot tables summarize a declared grain and filters. Weighted rates require summed numerators and denominators. Date parsing, text-formatted numbers and locale-specific separators can silently change results. Inspect formulas and sample rows, not only displayed totals.

Reconcile source row counts/totals, transformed totals and reported metrics. Protect against accidental edits where appropriate, document manual adjustments and keep a reproducible source version. Conditional formatting highlights values but is not a data validation or access-control mechanism.

## Work through it

For rows revenue[100,900],profit[50,90], total margin isSUM(profit)/SUM(revenue)=14%. An average of row margins gives 30% and overweights the small row.

If an absolute tax-rate cell is copied in formulas, locking its reference prevents it shifting to an unrelated cell; the specific spreadsheet syntax should match the chosen application.

## Common mistakes and practical limits

Do not hide errors with IFERROR(...,0) unless zero is genuinely the intended meaning. Hidden sheets can still expose sensitive data. A pivot needs a refresh/source-range policy.

---

[← Business questions, metric trees and KPI contracts](lesson-01-business-questions-and-kpis.md) · [BI semantic models, relationships, DAX and filter context →](lesson-03-bi-model-and-dax.md)

# Business Analytics and Coursework — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Business questions, metric trees and KPI contracts](#lesson-01)
- [02 — Excel tables, formulas, lookups, pivots and reconciliation](#lesson-02)
- [03 — BI semantic models, relationships, DAX and filter context](#lesson-03)
- [04 — Dashboard design, chart choice and accessible storytelling](#lesson-04)
- [05 — Customer, product, marketing and operations analytics](#lesson-05)
- [06 — Business cases, experiments, recommendations and capstone delivery](#lesson-06)

<a id="lesson-01"></a>

## 01 — Business questions, metric trees and KPI contracts

[Read the lesson](../01-theory/lesson-01-business-questions-and-kpis.md)

### Q001. Margin versus markup?

<details>
<summary>Answer</summary>

Margin divides profit by revenue; markup divides profit by cost.

</details>

### Q002. Why a KPI contract?

<details>
<summary>Answer</summary>

It fixes semantics so different queries/reports measure the same intended quantity.

</details>

### Q003. Does a metric tree prove causality?

<details>
<summary>Answer</summary>

No. It decomposes arithmetic relationships; causal levers need additional evidence.

</details>

<a id="lesson-02"></a>

## 02 — Excel tables, formulas, lookups, pivots and reconciliation

[Read the lesson](../01-theory/lesson-02-excel-and-analysis.md)

### Q004. Why exact-match lookups by default for IDs?

<details>
<summary>Answer</summary>

Approximate matching can return a different record when an exact ID is absent.

</details>

### Q005. Why reconcile totals?

<details>
<summary>Answer</summary>

It detects dropped/duplicated rows and transformation mistakes before presentation.

</details>

### Q006. Does hiding a sheet secure data?

<details>
<summary>Answer</summary>

No. It is a display choice, not a robust authorization boundary.

</details>

<a id="lesson-03"></a>

## 03 — BI semantic models, relationships, DAX and filter context

[Read the lesson](../01-theory/lesson-03-bi-model-and-dax.md)

### Q007. Measure versus calculated column?

<details>
<summary>Answer</summary>

A measure evaluates under current context; a calculated column stores row-level results produced during model processing.

</details>

### Q008. Why can total ratios differ from row averages?

<details>
<summary>Answer</summary>

The total recalculates pooled numerator/denominator in its own context.

</details>

### Q009. What should RLS testing include?

<details>
<summary>Answer</summary>

Representative identities and access paths, not only a developer’s unrestricted view.

</details>

<a id="lesson-04"></a>

## 04 — Dashboard design, chart choice and accessible storytelling

[Read the lesson](../01-theory/lesson-04-dashboards-and-communication.md)

### Q010. Which chart for a time trend?

<details>
<summary>Answer</summary>

Usually a line with a meaningful ordered time axis, with missing periods handled visibly.

</details>

### Q011. Why show source freshness?

<details>
<summary>Answer</summary>

A reader needs to know whether the comparison is based on complete current data.

</details>

### Q012. Observation versus recommendation?

<details>
<summary>Answer</summary>

An observed change is evidence; an intervention recommendation needs a justified causal/decision argument.

</details>

<a id="lesson-05"></a>

## 05 — Customer, product, marketing and operations analytics

[Read the lesson](../01-theory/lesson-05-customer-product-and-operations.md)

### Q013. Attribution versus incrementality?

<details>
<summary>Answer</summary>

Attribution assigns credit; incrementality estimates additional outcomes caused by an intervention.

</details>

### Q014. Why cohort alignment?

<details>
<summary>Answer</summary>

Different follow-up opportunities can create artificial retention differences.

</details>

### Q015. What does Little’s law connect?

<details>
<summary>Answer</summary>

Average work-in-system equals average throughput/arrival rate times average time under the stated stable-flow conditions.

</details>

<a id="lesson-06"></a>

## 06 — Business cases, experiments, recommendations and capstone delivery

[Read the lesson](../01-theory/lesson-06-cases-and-capstone.md)

### Q016. What makes a case reproducible?

<details>
<summary>Answer</summary>

Clear sources, versions, transformations, metric definitions and a path from inputs to reported results.

</details>

### Q017. Why sensitivity analysis?

<details>
<summary>Answer</summary>

It identifies which uncertain assumptions could change the recommendation.

</details>

### Q018. What belongs in a decision memo?

<details>
<summary>Answer</summary>

The decision, supporting result, limitations, trade-offs and a concrete measurable next step.

</details>

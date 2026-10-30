# Interview Preparation — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Clarify questions, reason aloud and check edge cases](#lesson-01)
- [02 — Coding and SQL interview patterns](#lesson-02)
- [03 — Statistics, ML and business-case interviews](#lesson-03)
- [04 — System design, project narratives and mock practice](#lesson-04)

<a id="lesson-01"></a>

## 01 — Clarify questions, reason aloud and check edge cases

[Read the lesson](../01-theory/lesson-01-structured-solving.md)

### Q001. What clarify for second largest?

<details>
<summary>Answer</summary>

Whether it means second distinct value, how to handle short input and what to return when absent.

</details>

### Q002. Why start with a small case?

<details>
<summary>Answer</summary>

It exposes semantics and boundary assumptions before implementation complexity grows.

</details>

### Q003. What belongs in an error log?

<details>
<summary>Answer</summary>

The mistaken reasoning, corrected principle and a concrete changed problem to retry.

</details>

<a id="lesson-02"></a>

## 02 — Coding and SQL interview patterns

[Read the lesson](../01-theory/lesson-02-coding-and-sql-rounds.md)

### Q004. Why check complement before inserting in two-sum?

<details>
<summary>Answer</summary>

It avoids reusing the same element and handles duplicates as separate occurrences.

</details>

### Q005. Why does latest need a tie policy?

<details>
<summary>Answer</summary>

Equal timestamps can otherwise produce nondeterministic or multiple records depending on the query.

</details>

### Q006. Why can sliding-window sum logic fail with negatives?

<details>
<summary>Answer</summary>

Extending/shrinking no longer changes the sum monotonically, breaking the usual invariant.

</details>

<a id="lesson-03"></a>

## 03 — Statistics, ML and business-case interviews

[Read the lesson](../01-theory/lesson-03-statistics-ml-cases.md)

### Q007. First check after a dashboard metric drops?

<details>
<summary>Answer</summary>

Definition, instrumentation, freshness, eligibility and composition before assuming a causal product change.

</details>

### Q008. Why serving constraints in an ML interview?

<details>
<summary>Answer</summary>

A high offline score can be unusable under latency, cost, data-availability or explainability requirements.

</details>

### Q009. What makes a proposed investigation strong?

<details>
<summary>Answer</summary>

It distinguishes plausible causes and states what result would support or weaken each one.

</details>

<a id="lesson-04"></a>

## 04 — System design, project narratives and mock practice

[Read the lesson](../01-theory/lesson-04-systems-and-project-stories.md)

### Q010. What if a project has no production metrics?

<details>
<summary>Answer</summary>

State its prototype/learning status and report the validation actually performed, without inventing business impact.

</details>

### Q011. Why quantify scale assumptions?

<details>
<summary>Answer</summary>

They determine storage, throughput, latency and reliability design choices.

</details>

### Q012. What should a mock score include besides correctness?

<details>
<summary>Answer</summary>

Communication, assumptions, edge-case verification and justified trade-offs.

</details>

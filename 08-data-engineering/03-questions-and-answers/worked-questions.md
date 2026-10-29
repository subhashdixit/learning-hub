# Questions and worked answers

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Try an answer aloud before opening the explanation. Use the theory chapter for the full derivation; the answers here focus on the reasoning.

## 1. Why can collect fail on a large DataFrame?

<details><summary>Answer</summary>

It moves results to the driver, whose memory may be much smaller than the distributed dataset.

</details>

## 2. What is a shuffle?

<details><summary>Answer</summary>

A redistribution of rows between partitions, often required for grouping, joining or sorting across keys.

</details>

## 3. What makes a load idempotent?

<details><summary>Answer</summary>

Rerunning the same logical input yields the same intended final result rather than duplicated rows or side effects.

</details>

## 4. Is a passing schema check enough?

<details><summary>Answer</summary>

No. Check keys, ranges, freshness, nulls and reconciliation. Valid types do not establish correct meaning.

</details>

## 5. Why keep raw inputs?

<details><summary>Answer</summary>

They allow reruns, audits and corrected transformations without relying on irreversible manual edits.

</details>

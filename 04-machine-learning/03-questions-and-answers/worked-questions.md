# Questions and worked answers

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Try an answer aloud before opening the explanation. Use the theory chapter for the full derivation; the answers here focus on the reasoning.

## 1. Training score is excellent; validation is poor. What next?

<details><summary>Answer</summary>

Check leakage and split design first, then distribution shift, complexity and regularization. Compare with a baseline; do not tune on the final test set.

</details>

## 2. Is R² = 0.9 equivalent to 90% accuracy?

<details><summary>Answer</summary>

No. It compares squared error with a mean baseline under its definition. It does not count correct predictions.

</details>

## 3. What does a regression tree maximize at a split?

<details><summary>Answer</summary>

The reduction in parent error after weighting child errors by sample size. Equivalently, it minimizes the resulting weighted child error.

</details>

## 4. How are bagging and boosting different?

<details><summary>Answer</summary>

Bagging aggregates models trained on resampled data. Boosting adds sequential corrections according to an objective or example-weighting rule.

</details>

## 5. What does a cluster ID of 2 mean?

<details><summary>Answer</summary>

Only an arbitrary assigned group label. Interpret its feature profile and stability; the ID itself has no numeric ordering.

</details>

## 6. Does large C in an SVM mean more errors are ignored?

<details><summary>Answer</summary>

No. It increases the penalty for violations relative to the norm term. Slack values measure violations, not a fixed count of ignored rows.

</details>

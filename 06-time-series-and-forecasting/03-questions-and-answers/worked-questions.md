# Questions and worked answers

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Try an answer aloud before opening the explanation. Use the theory chapter for the full derivation; the answers here focus on the reasoning.

## 1. Why not shuffle a forecasting dataset?

<details><summary>Answer</summary>

It can put future information into training and evaluate a different task from predicting later observations.

</details>

## 2. Is an MA model a rolling average?

<details><summary>Answer</summary>

No. A moving-average time-series model uses lagged innovations/errors. A rolling average is a smoothing calculation.

</details>

## 3. Can future exogenous variables be used?

<details><summary>Answer</summary>

Only if they are known at the forecast origin or separately forecast, with their uncertainty handled appropriately.

</details>

## 4. Why can MAPE be unsuitable for demand?

<details><summary>Answer</summary>

Actual values near zero create extreme ratios; zeros can make it undefined. Use a suitable metric and state the denominator policy.

</details>

## 5. Does an ADF rejection prove all stationarity conditions?

<details><summary>Answer</summary>

No. It gives evidence against a unit-root null under the test assumptions. Inspect the series, model and other assumptions.

</details>

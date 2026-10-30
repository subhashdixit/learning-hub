# 13 — Forecast combinations, hierarchies and probabilistic reconciliation

[Algorithm story](../ALGORITHM-STORY.md) · [Algorithm index](README.md) · [Practicals](../../02-practicals/README.md)

```mermaid
flowchart LR
 N0["Honest base forecasts"] --> N1["Combine or use hierarchy"] --> N2["Estimate weights or error covariance"] --> N3["Coherent point or sample forecasts"] --> N4["Evaluate every level"]
```

## On this page

- [1. Why this branch exists](#1-why-this-branch-exists)
- [2. How it works and learns](#2-how-it-works-and-learns)
- [3. Calculate a small example](#3-calculate-a-small-example)
- [4. Advantages, limitations and related alternatives](#4-advantages-limitations-and-related-alternatives)
- [5. How to choose and validate it](#5-how-to-choose-and-validate-it)

## 1. Why this branch exists

No one model is consistently best across every series/horizon, and independently predicted totals may not add up. Combination and reconciliation address robustness and consistency, which are separate from fitting another base algorithm.

## 2. How it works and learns

A fixed or learned weighted average combines base forecasts. Learn weights only using development forecasts that mimic serving; in-sample fitted predictions can make a poor model look exceptionally good. Stacking and error-based selection require an honest temporal protocol. Diverse errors can help; averaging the same shared error does not remove it.

For a hierarchy write coherent forecasts as $y=S b$, where b contains bottom-level values and S sums them into all levels. Bottom-up sums bottom forecasts; top-down allocates a total under proportions; reconciliation projects base forecasts into the coherent space under a specified criterion. MinT uses a forecast-error covariance estimate with appropriate regularization/assumptions. Probabilistic reconciliation must handle distributions/samples, not only independently adjusted point intervals.

## 3. Calculate a small example

Two regional forecasts 60 and 50 sum 110, but an independent national forecast 100 is inconsistent. A method must decide how to adjust them using its objective and evidence; there is no unique “correct” fix from these three numbers alone.

For two forecast errors with variance 1 and correlation.5, an equal average has variance.75 under this simplified equal-variance setup. It can reduce variance but cannot eliminate shared bias.

## 4. Advantages, limitations and related alternatives

Combination can improve stability at extra training/serving cost; learned weights can overfit. Reconciliation gives adding-up consistency but can distribute poor assumptions throughout a hierarchy. Coherence alone does not imply accuracy, calibration or an appropriate business decision.

## 5. How to choose and validate it

Compare unreconciled/reconciled and simple-average alternatives on matched origins. Check each hierarchy level, horizon, totals, interval/sample coherence and computational constraints. Keep the hierarchy and business aggregation definitions versioned.

---

[← ARCH, GARCH and conditional volatility](12-volatility.md)

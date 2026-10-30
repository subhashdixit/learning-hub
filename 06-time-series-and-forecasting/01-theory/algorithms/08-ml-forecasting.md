# 08 — Lagged regression, random forests, boosting and global forecasting

[Algorithm story](../ALGORITHM-STORY.md) · [Algorithm index](README.md) · [Practicals](../../02-practicals/README.md)

```mermaid
flowchart LR
 N0["Historical cutoff"] --> N1["Available lags and calendar"] --> N2["Fit supervised objective"] --> N3["Direct recursive or multioutput horizon"] --> N4["Backtest identical procedure"]
```

## On this page

- [1. Why this branch exists](#1-why-this-branch-exists)
- [2. How it works and learns](#2-how-it-works-and-learns)
- [3. Calculate a small example](#3-calculate-a-small-example)
- [4. Advantages, limitations and related alternatives](#4-advantages-limitations-and-related-alternatives)
- [5. How to choose and validate it](#5-how-to-choose-and-validate-it)

## 1. Why this branch exists

Linear dependence and fixed seasonal structure can miss nonlinear interactions among lags, calendar and known drivers. Converting history into supervised rows allows classical ML, while pooling rows across related series can share information.

## 2. How it works and learns

Create features from available lags, trailing summaries, calendar, static series attributes and known future covariates. Fit linear/regularized models, random forests or boosted trees using squared, absolute, quantile or other suitable losses. Fit preprocessing only within training windows. A rolling mean used for target t must not contain y_t or later values.

Recursive forecasting reuses earlier predictions; direct forecasting fits horizon-specific targets; multioutput models predict a vector. A global model shares parameters across series, while a local model fits each separately. Series identity, scaling, cold-start handling and relatedness determine whether pooling helps. Trees predict piecewise functions and do not automatically extrapolate a trend outside observed feature ranges.

## 3. Calculate a small example

For target day t, valid lag features could be $y_{t-1},y_{t-7}$ and the mean of $y_{t-7},\ldots,y_{t-1}$. A centered rolling mean includes future values and is invalid for this task.

At one fixed seven-day origin, tomorrow's actual will not be available when forecasting day+2. A recursive model must feed its day+1 prediction or use a different forecast strategy; silently using tomorrow's actual changes the evaluation task.

## 4. Advantages, limitations and related alternatives

Flexible interactions and scalable tabular training are strengths; feature leakage, recursive error accumulation, extrapolation and sparse histories are common weaknesses. Global fitting can transfer patterns but also mix incompatible series. Neural global models learn representations/end-to-end distributions; neither family is automatically best for every horizon or sample size.

## 5. How to choose and validate it

Tune lag window, features, pooling, forecast strategy and estimator complexity jointly using temporal validation. Evaluate per series/scale/horizon and compare seasonal naive, ETS and ARIMA. Include latency, cold start and coverage when using quantile outputs.

---

[← Croston, SBA, TSB and intermittent-demand forecasting](07-intermittent-demand.md) · [DeepAR, TCN, N-BEATS and N-HiTS →](09-neural-global-models.md)

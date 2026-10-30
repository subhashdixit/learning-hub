# 01 — Time indices, forecast horizons and naive baselines

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-01)

```mermaid
flowchart LR
 N0["Forecast origin"] --> N1["Available history"] --> N2["Baseline"] --> N3["Required horizon"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A forecast is a dated promise: what was known at the origin and when the answer is needed both matter.

Specify the target, frequency, forecast origin and horizon. Daily observations do not imply daily independent evidence. Resolve time zones, missing timestamps, duplicate timestamps and calendar effects before modelling. Missing demand is not necessarily zero demand; stockouts can censor observed sales.

A naive forecast repeats the last observation. A seasonal-naive forecast repeats the corresponding last-season value. Drift extrapolates average historical change. These cheap methods establish whether a complex model adds useful information. A horizon 1 task updated daily is different from predicting the whole next month at one fixed origin.

Plot level, seasonality, outliers, changes and business events. Known future covariates such as a planned holiday differ from future realized weather, which itself needs a forecast. Record data release timing and revisions so a backtest uses only what truly existed at each origin.

## Work through it

For weekly seasonality and observations $[10,12,11,13,20,25,18]$, tomorrow's seasonal-naive forecast can repeat 10 if the first value represents the matching weekday in the last full week. A last-value naive forecast repeats 18. Neither is universally correct: compare under repeated historical origins and the intended loss.

## Common mistakes and practical limits

Do not random-split a forecasting series. A revised economic number downloaded today may not have been available at the historical origin. Align target timestamps carefully when building lag features.

---

[Subject home](../README.md) · [Trend, seasonality, transformations, ACF and stationarity →](lesson-02-decomposition-and-stationarity.md)

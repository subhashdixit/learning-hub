# 06 — Lagged ML, intermittent demand, hierarchies and forecast operations

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-06)

```mermaid
flowchart LR
 N0["Features and release times"] --> N1["Forecast procedure"] --> N2["Reconcile hierarchy"] --> N3["Monitor issued forecasts"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A forecasting system is a chain of calendars, data releases, decisions and feedback—not only a model.

Tree/linear/neural forecasting models can use lags, trailing summaries and known calendar effects. Build every feature using values available at the forecast origin. Direct multistep models fit horizons separately; recursive models feed predictions forward; multioutput models learn several horizons jointly. Evaluate the exact serving procedure.

Intermittent demand has many zeros and irregular nonzero events. Croston-style methods separate arrival intervals and positive sizes under their assumptions; they are not universal solutions. Inventory needs lead-time demand and service/cost considerations, not merely the lowest point-error metric. Hierarchical forecasts must reconcile products, regions and totals so the outputs add up under a specified method.

Maintain versioned input snapshots, forecast origins, model/config versions and prediction intervals. Monitor revisions, missingness, bias, coverage and decision effects. Human overrides should be recorded with reasons and assessed against the unadjusted baseline; intuition is not automatically beneficial. Forecasting also includes scenario analysis when future drivers are uncertain.

## Work through it

If regional forecasts are 60 and 50 but an independently fitted national forecast is 100, the forecasts are incoherent. A reconciliation method adjusts them under a defined criterion and covariance assumptions rather than silently accepting 110=100.

For next 7 days at one origin, a feature“yesterday's actual”cannot use actuals from future forecast days. Either recurse predicted values, fit direct horizons or define a rolling one-step task.

## Common mistakes and practical limits

Forecast accuracy and inventory profit are different objectives. Do not overwrite old forecasts when updated actuals arrive; preserve what was issued when. A hierarchy needs valid aggregation relationships and consistent units.

---

[← Backtesting, metrics, residual diagnostics and intervals](lesson-05-forecast-evaluation.md) · [Continue with practicals](../02-practicals/README.md)

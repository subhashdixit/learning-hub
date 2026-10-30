# 03 — Exponential smoothing, Holt trends and seasonal ETS

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-03)

```mermaid
flowchart LR
 N0["Previous level"] --> N1["New observation"] --> N2["Weighted update"] --> N3["Next forecast"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** Smoothing is a weighted memory: recent observations can matter more without forgetting all history.

Simple exponential smoothing updates a level $\ell_t=\alpha y_t+(1-\alpha)\ell_{t-1}$. It suits data without a persistent trend/seasonality under the chosen model. Alpha controls responsiveness: large alpha follows new changes quickly but reacts more to noise.

Holt methods add a trend; damped trends limit indefinitely extrapolated growth. Seasonal methods include seasonal state. ETS state-space formulations make error, trend and seasonal assumptions explicit and support likelihood-based estimation and forecast distributions. Additive and multiplicative choices affect allowable values and how uncertainty scales.

Tune parameters and model form on realistic backtests or suitable information criteria, then assess the target horizon. A fitted line hugging history is not a forecast validation. Abrupt promotions, stockouts and regime changes may need exogenous information or explicit adjustment rather than ever faster smoothing.

## Work through it

Initial level 10, next observation 14 and alpha.25 give updated level $.25(14)+.75(10)=11$. A simple level-only next forecast is 11. With alpha 1 it becomes 14; with alpha 0 it remains 10. Those extremes illustrate responsiveness, not recommended universal settings.

## Common mistakes and practical limits

A level-only model does not extrapolate a real sustained trend. Multiplicative components need compatible positive data. Initialization and parameter estimation affect early states and should be part of the fitted procedure.

---

[← Trend, seasonality, transformations, ACF and stationarity](lesson-02-decomposition-and-stationarity.md) · [AR, MA, ARIMA, SARIMA and dynamic regression →](lesson-04-arima-and-dynamic-regression.md)

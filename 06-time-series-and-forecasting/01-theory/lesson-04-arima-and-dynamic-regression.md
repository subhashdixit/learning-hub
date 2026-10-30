# 04 — AR, MA, ARIMA, SARIMA and dynamic regression

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-04)

```mermaid
flowchart LR
 N0["Past values and innovations"] --> N1["ARIMA or regression"] --> N2["Future assumptions"] --> N3["Forecast"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** An AR model remembers past values; an MA model remembers past surprises.

An AR model relates current values to previous values, while an MA model relates them to current/past innovations. ARIMA combines autoregressive terms, differencing and moving-average errors. Its(p,d,q) orders describe those parts; seasonal(P,D,Q,m) terms add seasonal dependence. “Moving average”here is not the same as a rolling arithmetic mean.

Dynamic regression combines covariates with an explicit time-series error process. All required future covariates must be known, forecast or scenario-defined. Fit under the model's stationarity/invertibility and error assumptions as applicable; numerical convergence alone is not validation.

Compare candidate orders, residual autocorrelation and held-out forecast performance. Information criteria can help within a coherent fitting setup, but do not replace horizon-specific backtesting. Complex models can be weak on short samples and structural breaks. Neural or tree lag models are alternatives, not automatic upgrades.

## Work through it

An AR(1) model $y_t=c+\phi y_{t-1}+\epsilon_t$ with $c=2,\phi=.5$ and last value 10 predicts 7 next. The following expected value is $2+.5(7)=5.5$ when future innovations have mean 0. Under $|\phi|<1$, the stationary mean is $c/(1-\phi)=4$; forecasts move toward it.

## Common mistakes and practical limits

Do not confuse predicted residuals with known future innovations. A high AR coefficient does not automatically prove a causal persistence mechanism. Differentiate training fit residuals from genuine out-of-origin forecast errors.

---

[← Exponential smoothing, Holt trends and seasonal ETS](lesson-03-exponential-smoothing.md) · [Backtesting, metrics, residual diagnostics and intervals →](lesson-05-forecast-evaluation.md)

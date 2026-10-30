# Time Series and Forecasting — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Time indices, forecast horizons and naive baselines](#lesson-01)
- [02 — Trend, seasonality, transformations, ACF and stationarity](#lesson-02)
- [03 — Exponential smoothing, Holt trends and seasonal ETS](#lesson-03)
- [04 — AR, MA, ARIMA, SARIMA and dynamic regression](#lesson-04)
- [05 — Backtesting, metrics, residual diagnostics and intervals](#lesson-05)
- [06 — Lagged ML, intermittent demand, hierarchies and forecast operations](#lesson-06)

<a id="lesson-01"></a>

## 01 — Time indices, forecast horizons and naive baselines

[Read the lesson](../01-theory/lesson-01-time-index-and-baselines.md)

### Q001. Origin versus horizon?

<details>
<summary>Answer</summary>

Origin is the information cutoff; horizon is how far ahead the target lies.

</details>

### Q002. Why seasonal naive?

<details>
<summary>Answer</summary>

It preserves recurring seasonal position cheaply and is an essential comparison for seasonal data.

</details>

### Q003. Is future weather a known covariate?

<details>
<summary>Answer</summary>

Usually not as a realized value; use a forecast available at the origin or model uncertainty appropriately.

</details>

<a id="lesson-02"></a>

## 02 — Trend, seasonality, transformations, ACF and stationarity

[Read the lesson](../01-theory/lesson-02-decomposition-and-stationarity.md)

### Q004. Does differencing always help?

<details>
<summary>Answer</summary>

No. Unnecessary differencing can amplify noise and alter the dependence structure.

</details>

### Q005. ACF versus PACF?

<details>
<summary>Answer</summary>

ACF measures raw lag correlation; PACF removes specified intervening-lag linear effects.

</details>

### Q006. Why can exp(mean log y) misrepresent mean y?

<details>
<summary>Answer</summary>

Nonlinear expectation means exponentiating a mean on log scale is not generally the original-scale arithmetic mean.

</details>

<a id="lesson-03"></a>

## 03 — Exponential smoothing, Holt trends and seasonal ETS

[Read the lesson](../01-theory/lesson-03-exponential-smoothing.md)

### Q007. What does alpha control?

<details>
<summary>Answer</summary>

The relative weight of the newest observation in the level update.

</details>

### Q008. Why damp a trend?

<details>
<summary>Answer</summary>

To avoid projecting a short historical slope indefinitely into the future.

</details>

### Q009. Can good in-sample smoothing prove forecasting skill?

<details>
<summary>Answer</summary>

No. Evaluate predictions made using only data before each origin.

</details>

<a id="lesson-04"></a>

## 04 — AR, MA, ARIMA, SARIMA and dynamic regression

[Read the lesson](../01-theory/lesson-04-arima-and-dynamic-regression.md)

### Q010. MA model versus rolling mean?

<details>
<summary>Answer</summary>

An MA(q) model uses innovations; a rolling mean averages observed values in a window.

</details>

### Q011. What does d in ARIMA mean?

<details>
<summary>Answer</summary>

The order of nonseasonal differencing before the stationary ARMA component.

</details>

### Q012. Why future covariate availability?

<details>
<summary>Answer</summary>

A regression forecast cannot legitimately use a realized future input unavailable at its origin.

</details>

<a id="lesson-05"></a>

## 05 — Backtesting, metrics, residual diagnostics and intervals

[Read the lesson](../01-theory/lesson-05-forecast-evaluation.md)

### Q013. Why multiple origins?

<details>
<summary>Answer</summary>

One unusual holdout period may not describe typical forecast behaviour.

</details>

### Q014. Does 90% coverage mean each subgroup has 90% coverage?

<details>
<summary>Answer</summary>

No. Overall coverage can hide failures in specific horizons or segments.

</details>

### Q015. Why compare interval width too?

<details>
<summary>Answer</summary>

Coverage can be achieved trivially with intervals too wide to guide decisions.

</details>

<a id="lesson-06"></a>

## 06 — Lagged ML, intermittent demand, hierarchies and forecast operations

[Read the lesson](../01-theory/lesson-06-forecast-systems.md)

### Q016. Direct versus recursive forecast?

<details>
<summary>Answer</summary>

Direct models target each horizon; recursive prediction reuses predicted values for later steps.

</details>

### Q017. What is coherence?

<details>
<summary>Answer</summary>

Forecasts across an aggregation structure satisfy its adding-up relationships.

</details>

### Q018. Why log overrides?

<details>
<summary>Answer</summary>

To evaluate whether human changes improve decisions and reproduce what was actually issued.

</details>

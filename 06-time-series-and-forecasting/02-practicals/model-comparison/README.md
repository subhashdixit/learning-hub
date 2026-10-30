# Fit and compare ARIMA, SARIMA, SARIMAX, Holt–Winters and Prophet

[Practicals](../README.md) · [Forecasting algorithm story](../../01-theory/ALGORITHM-STORY.md)

This script trains the real library implementations on 252 daily synthetic observations and predicts the next 28 days from one fixed origin. A seasonal-naive baseline uses the same cutoff. Data contain a trend, weekly seasonality, a scheduled promotion and noise. No remote dataset or API key is needed.

## Run

Use a dedicated Python 3.10+ environment. Prophet includes a Stan-backed fitting dependency; follow the official installation guidance if your platform needs additional setup.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python compare_models.py
```

Run commands in this folder. [Read the full script](compare_models.py) and [recorded results](example-results.json). Parameters are fixed for teaching, not tuned against the reported holdout. Future promotion values are known by construction; no future target values are given to prediction.

## Recorded teaching run

| Model | MAE | RMSE |
|---|---:|---:|
| seasonal_naive | 1.3313 | 1.6395 |
| ARIMA | 1.9211 | 2.2158 |
| SARIMA | 1.3078 | 1.6229 |
| SARIMAX | 0.7137 | 0.9244 |
| ETS_Holt_Winters | 0.7103 | 0.8043 |
| Prophet | 0.3261 | 0.4484 |

The result is specific to this synthetic design, seed, versions and horizon. Prophet matches these component assumptions well here; this is not evidence it wins generally. The ordinary ARIMA is worse than seasonal naive in this example, showing why a more elaborate name is insufficient. A method-selection claim after viewing this comparison needs another untouched evaluation or an appropriate nested temporal protocol.

Statsmodels reported nonstationary/noninvertible *starting-parameter* adjustments and used its fallback starting values; the run completed and all forecasts were finite. Those initialization messages are not evidence that every fitted model is valid on another dataset. Inspect convergence and residual diagnostics when adapting the exercise.

## Extend it honestly

Introduce a regime break, remove the known promotion, change seasonality, shorten history or use intermittent counts. Compare several historical origins and horizons. Tune on development periods and keep a final test separate. Inspect bias and interval coverage; a point-error table is not a full evaluation of predictive distributions.

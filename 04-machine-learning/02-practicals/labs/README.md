# Runnable Machine Learning labs

[Practicals index](../README.md) · [Theory map](../../01-theory/README.md)

These small scripts use synthetic/local data and contain assertions for the worked calculations or basic invariants. They do not download datasets. The original notebooks and assignments are available from the practicals index.

## Run

Use a dedicated Python environment rather than changing an existing project. Python 3.10 or later is required for the pinned dependencies.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python 01-linear-algebra-and-gradients.py
```

Run commands from this folder. Run each other script the same way. Generated metrics are teaching results on synthetic data; they are not benchmark promises. Seeds make the examples repeatable, with small numerical differences possible across platforms.

| Order | Lab | What to inspect |
|---|---|---|
| 01 | [Regression calculations and gradient descent](01-linear-algebra-and-gradients.py) | Read comments, predict output, run and explain assertions |
| 02 | [Compare regression pipelines with an untouched test](02-leakage-safe-regression.py) | Read comments, predict output, run and explain assertions |
| 03 | [Select a classification threshold without test leakage](03-classification-costs.py) | Read comments, predict output, run and explain assertions |
| 04 | [Compare distinct supervised families on identical CV folds](04-algorithm-comparison.py) | Read comments, predict output, run and explain assertions |
| 05 | [Reproduce tree, AdaBoost and second-order leaf arithmetic](05-trees-and-boosting-math.py) | Read comments, predict output, run and explain assertions |
| 06 | [Compare clustering geometry and verify PCA reconstruction](06-clustering-and-pca.py) | Read comments, predict output, run and explain assertions |
| 07 | [Inspect anomaly ranking and calculate NDCG](07-anomaly-and-ranking.py) | Read comments, predict output, run and explain assertions |
| 08 | [Calibrate prediction intervals and evaluate finite-sample coverage](08-conformal-intervals.py) | Read comments, predict output, run and explain assertions |
| 09 | [Make lag features and compare a forecast with a naive baseline](09-time-safe-backtest.py) | Read comments, predict output, run and explain assertions |
| 10 | [Check Bellman updates and Bayesian/GP arithmetic](10-reinforcement-and-bayes.py) | Read comments, predict output, run and explain assertions |

## Extend each lab

Change one assumption at a time: introduce group duplication, alter prevalence, rescale a feature, change noise or choose a different forecast horizon. Explain why the metric changes. Keep the final test untouched while tuning. A passing arithmetic assertion verifies that example; it does not verify every estimator on your own datasets.

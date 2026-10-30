# Lab validation results

[Lab index](README.md)

Executed all ten scripts on 2026-10-30 with Python 3.10, NumPy 1.26.4, SciPy 1.13.1 and scikit-learn 1.6.1. All assertions passed. These are synthetic teaching checks, not an execution audit of every historical imported notebook.

## 01-linear-algebra-and-gradients.py

```text
Gradient fit: 5.099730637501128e-09 0.9999999977566197 ; least-squares: [-5.89116072e-16  1.00000000e+00]
```

## 02-leakage-safe-regression.py

```text
Chosen: {'ridge__alpha': 0.01} test RMSE: 14.161 baseline: 118.961
```

## 03-classification-costs.py

```text
Validation-chosen threshold: 0.19 ; test confusion matrix:
 [[542  20]
 [  5  33]]
Test average precision: 0.823 Brier: 0.023
```

## 04-algorithm-comparison.py

```text
logistic 0.852 +/- fold SD 0.022
knn 0.948 +/- fold SD 0.012
svm 0.948 +/- fold SD 0.004
forest 0.95 +/- fold SD 0.013
boosting 0.946 +/- fold SD 0.017
```

## 05-trees-and-boosting-math.py

```text
Tree gain: 121.0 AdaBoost weights: [0.08333333 0.08333333 0.08333333 0.08333333 0.08333333 0.08333333
 0.5       ] regularized leaf: 2.0
```

## 06-clustering-and-pca.py

```text
kmeans external ARI: 0.247 noise: 0
dbscan external ARI: 1.0 noise: 0
PCA retained fraction: 0.9000000000000001 reconstruction SSE: 2.0
```

## 07-anomaly-and-ranking.py

```text
Top anomaly indices: [302 300 301  69 146 252]
NDCG@3: 0.9197207891481876
```

## 08-conformal-intervals.py

```text
Calibration radius: 2.193 test coverage: 0.912 width: 4.386
```

## 09-time-safe-backtest.py

```text
Fold 1 model MAE 0.605 seasonal-naive 0.552
Fold 2 model MAE 0.52 seasonal-naive 0.703
Fold 3 model MAE 0.55 seasonal-naive 0.589
Fold 4 model MAE 0.712 seasonal-naive 0.819
```

## 10-reinforcement-and-bayes.py

```text
Q update: 2.26 Beta posterior mean: 0.6666666666666666 GP mean/variance: 0.8 0.19999999999999996
```

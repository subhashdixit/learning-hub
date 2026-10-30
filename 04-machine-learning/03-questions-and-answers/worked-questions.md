# Machine Learning — worked questions and answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

200 questions in course order. Try each before opening its answer. Questions progress from concepts to calculations and practical diagnosis within each lesson. Assignments and original exercise files live in Practicals.

- [01 — What machine learning learns](#lesson-01)
- [02 — Data preparation, feature engineering and leakage](#lesson-02)
- [03 — Generalization, bias, variance and learning curves](#lesson-03)
- [04 — Splits, cross-validation and hyperparameter search](#lesson-04)
- [05 — Loss functions and optimization](#lesson-05)
- [06 — Regression metrics and residual diagnostics](#lesson-06)
- [07 — Classification metrics, thresholds and calibration](#lesson-07)
- [08 — Linear regression: the full reasoning](#lesson-08)
- [09 — Ridge, lasso, elastic net and generalized regression](#lesson-09)
- [10 — Logistic regression and softmax classification](#lesson-10)
- [11 — Naive Bayes, LDA and QDA](#lesson-11)
- [12 — K-nearest neighbours and distance](#lesson-12)
- [13 — SVM, kernels and support vector regression](#lesson-13)
- [14 — Decision trees: entropy, Gini, regression and pruning](#lesson-14)
- [15 — Bagging, random forests and Extra Trees](#lesson-15)
- [16 — AdaBoost: learning from weighted mistakes](#lesson-16)
- [17 — Gradient boosting, XGBoost, LightGBM and CatBoost](#lesson-17)
- [18 — Voting, stacking and blending](#lesson-18)
- [19 — K-means, k-means++, mini-batch and k-medoids](#lesson-19)
- [20 — Hierarchical clustering and BIRCH](#lesson-20)
- [21 — DBSCAN, OPTICS and HDBSCAN](#lesson-21)
- [22 — Gaussian mixtures, EM and density estimation](#lesson-22)
- [23 — PCA, SVD, NMF, ICA and cross-decomposition](#lesson-23)
- [24 — Kernel PCA, manifolds, t-SNE, UMAP and spectral methods](#lesson-24)
- [25 — Anomaly, novelty and outlier detection](#lesson-25)
- [26 — Feature selection, imbalanced learning and label quality](#lesson-26)
- [27 — Bayesian learning and Gaussian processes](#lesson-27)
- [28 — Recommendation, matrix factorization and ranking](#lesson-28)
- [29 — Association rules, Apriori and FP-growth](#lesson-29)
- [30 — Semi-supervised, self-supervised, weak and active learning](#lesson-30)
- [31 — Online learning, drift and federated learning](#lesson-31)
- [32 — Reinforcement learning and contextual bandits](#lesson-32)
- [33 — Neural networks and representation learning](#lesson-33)
- [34 — Text, time series, survival and structured prediction](#lesson-34)
- [35 — Interpretability, permutation importance, SHAP and dependence plots](#lesson-35)
- [36 — Uncertainty, prediction intervals and conformal prediction](#lesson-36)
- [37 — Causality, fairness, robustness and responsible evaluation](#lesson-37)
- [38 — Deployment, reproducibility and monitoring](#lesson-38)
- [39 — Choose an algorithm and diagnose the result](#lesson-39)
- [40 — Advanced families, formula sheet and coverage map](#lesson-40)

<a id="lesson-01"></a>

## 01 — What machine learning learns

[Read the lesson](../01-theory/01-learning-map.md)

### Q001. Is ML the same as AI?

<details>
<summary>Answer</summary>

No. AI includes many ways to build intelligent behaviour; ML learns from data, and deep learning is one ML family.

</details>

### Q002. Is clustering classification without labels?

<details>
<summary>Answer</summary>

It finds a grouping under an objective or similarity rule. Its groups need not match a future labelled classification task.

</details>

### Q003. Parameter or hyperparameter: tree depth?

<details>
<summary>Answer</summary>

A configured maximum depth is a hyperparameter; the actual learned split thresholds are model parameters.

</details>

### Q004. Can a numeric target be a class?

<details>
<summary>Answer</summary>

Yes. Codes such as 0, 1, 2 may name categories; their numeric storage does not imply regression.

</details>

### Q005. Why define prediction time?

<details>
<summary>Answer</summary>

It determines which inputs genuinely exist and prevents using future information.

</details>

<a id="lesson-02"></a>

## 02 — Data preparation, feature engineering and leakage

[Read the lesson](../01-theory/02-data-and-features.md)

### Q006. Why not scale before splitting?

<details>
<summary>Answer</summary>

The validation distribution would influence learned preprocessing. Fit every learned step only on training data.

</details>

### Q007. Must trees be standardized?

<details>
<summary>Answer</summary>

Usually no: ordered threshold splits are mostly invariant to monotonic feature transformations. Other preprocessing may still be needed.

</details>

### Q008. Why is postcode not a continuous feature?

<details>
<summary>Answer</summary>

Numeric differences between arbitrary identifiers do not represent meaningful distance.

</details>

### Q009. What is target leakage?

<details>
<summary>Answer</summary>

A predictor contains outcome information unavailable at the time a real prediction would be made.

</details>

### Q010. Can we oversample before CV?

<details>
<summary>Answer</summary>

No. Duplicates or synthetic neighbours can connect training and validation folds. Resample within each training fold.

</details>

<a id="lesson-03"></a>

## 03 — Generalization, bias, variance and learning curves

[Read the lesson](../01-theory/03-generalization.md)

### Q011. Does low training loss prove learning?

<details>
<summary>Answer</summary>

It proves fitting to the training objective. Generalization needs evaluation on appropriate unseen examples.

</details>

### Q012. What is irreducible noise?

<details>
<summary>Answer</summary>

Variation not predictable from the available inputs under the modelled data-generating process.

</details>

### Q013. Does a train–validation gap always mean overfitting?

<details>
<summary>Answer</summary>

No. Shift, leakage, dependence and label differences can also create gaps.

</details>

### Q014. What is early stopping?

<details>
<summary>Answer</summary>

Stop iterative fitting when a separate validation criterion stops improving; the stopping decision is itself a tuned choice.

</details>

### Q015. Does no-free-lunch forbid model recommendations?

<details>
<summary>Answer</summary>

No. Recommendations use assumptions about the actual data and task, which is exactly what the theorem leaves out.

</details>

<a id="lesson-04"></a>

## 04 — Splits, cross-validation and hyperparameter search

[Read the lesson](../01-theory/04-validation.md)

### Q016. What does stratification protect?

<details>
<summary>Answer</summary>

Roughly similar class proportions across folds; it does not remove grouping, leakage or time dependence.

</details>

### Q017. Why nested CV?

<details>
<summary>Answer</summary>

Outer folds evaluate the full model-selection process while inner folds choose hyperparameters.

</details>

### Q018. Does random search mean random predictions?

<details>
<summary>Answer</summary>

No. It samples hyperparameter candidates; each candidate is trained and evaluated normally.

</details>

### Q019. Can test data choose a decision threshold?

<details>
<summary>Answer</summary>

No. Choose the threshold using development data; evaluate the frozen threshold once on test data.

</details>

### Q020. Why block bootstrap a time series?

<details>
<summary>Answer</summary>

Neighbouring observations are dependent. Blocks retain some dependence that independent row resampling would destroy.

</details>

<a id="lesson-05"></a>

## 05 — Loss functions and optimization

[Read the lesson](../01-theory/05-loss-and-optimization.md)

### Q021. Is RMSE the same objective value as MSE?

<details>
<summary>Answer</summary>

No. RMSE is its square root and has target units; on one fixed dataset minimizing either gives the same minimizer.

</details>

### Q022. Why use log loss instead of accuracy for training?

<details>
<summary>Answer</summary>

Log loss gives informative continuous probability errors; accuracy is flat over many small parameter changes.

</details>

### Q023. Are all algorithms trained by gradient descent?

<details>
<summary>Answer</summary>

No. Trees use split search, KNN stores examples, and some least-squares fits use direct linear algebra.

</details>

### Q024. Does convex mean a unique solution?

<details>
<summary>Answer</summary>

No. Rank-deficient least squares can have multiple minimizers; strict convexity gives uniqueness under suitable conditions.

</details>

### Q025. What does regularization strength control?

<details>
<summary>Answer</summary>

The trade-off between fitting training data and the chosen penalty, with scale depending on the objective convention.

</details>

<a id="lesson-06"></a>

## 06 — Regression metrics and residual diagnostics

[Read the lesson](../01-theory/06-regression-metrics.md)

### Q026. Can R² be negative?

<details>
<summary>Answer</summary>

Yes. The model can have larger squared error than predicting the evaluation-set target mean.

</details>

### Q027. Why is MAPE troublesome for sales?

<details>
<summary>Answer</summary>

Zero and near-zero actual sales make percentage errors undefined or unstable.

</details>

### Q028. Which loss targets a median?

<details>
<summary>Answer</summary>

Expected absolute error is minimized by a conditional median.

</details>

### Q029. What does a fan-shaped residual plot suggest?

<details>
<summary>Answer</summary>

Error variance changes with prediction level. Investigate variance modelling or suitable intervals.

</details>

### Q030. Can a good RMSE hide bias?

<details>
<summary>Answer</summary>

Yes. Particular groups, time periods or target ranges can systematically receive poor predictions.

</details>

<a id="lesson-07"></a>

## 07 — Classification metrics, thresholds and calibration

[Read the lesson](../01-theory/07-classification-metrics.md)

### Q031. Does 97% accuracy prove a useful fraud model?

<details>
<summary>Answer</summary>

No. Compare prevalence, a majority baseline, positive recall, false alerts and actual decision costs.

</details>

### Q032. Is ROC–AUC a probability calibration measure?

<details>
<summary>Answer</summary>

No. It measures ranking; monotonically changing scores can preserve AUC while changing calibration.

</details>

### Q033. When does a 0.5 threshold make sense?

<details>
<summary>Answer</summary>

Under calibrated probabilities and equal binary misclassification costs in the simple decision setting.

</details>

### Q034. Macro versus weighted F1?

<details>
<summary>Answer</summary>

Macro averages class scores equally; weighted averages by support and can hide a weak rare class.

</details>

### Q035. Why calibrate outside the test set?

<details>
<summary>Answer</summary>

Calibration fits a mapping using labels. Using final test labels would contaminate the reported estimate.

</details>

<a id="lesson-08"></a>

## 08 — Linear regression: the full reasoning

[Read the lesson](../01-theory/08-linear-regression.md)

### Q036. Is polynomial regression linear?

<details>
<summary>Answer</summary>

It is linear in coefficients even though its curve is nonlinear in the original input.

</details>

### Q037. Why avoid explicitly inverting XᵀX?

<details>
<summary>Answer</summary>

It worsens numerical conditioning; QR/SVD-based least-squares solvers are more stable.

</details>

### Q038. Must input features be normally distributed?

<details>
<summary>Answer</summary>

No. Normality assumptions belong to specific error-based inference results, not every input.

</details>

### Q039. Does a positive coefficient prove causality?

<details>
<summary>Answer</summary>

No. It is a conditional model association and can reflect confounding, selection or correlated features.

</details>

### Q040. Calculate MSE for y=[1,2,3], prediction=[.5,1,1.5].

<details>
<summary>Answer</summary>

Squared errors are.25,1,2.25, so MSE=3.5/3=1.1667.

</details>

<a id="lesson-09"></a>

## 09 — Ridge, lasso, elastic net and generalized regression

[Read the lesson](../01-theory/09-regularized-and-generalized-regression.md)

### Q041. Why standardize before lasso?

<details>
<summary>Answer</summary>

An equal numeric coefficient penalty should not favour a feature merely because its measurement units are large.

</details>

### Q042. Does ridge remove outliers?

<details>
<summary>Answer</summary>

No. Its coefficient penalty addresses fit complexity; squared residual loss remains sensitive to extreme residuals.

</details>

### Q043. When prefer elastic net to lasso?

<details>
<summary>Answer</summary>

When sparsity is useful but strongly correlated features make pure lasso unstable.

</details>

### Q044. What does τ=.9 predict?

<details>
<summary>Answer</summary>

A conditional 90th percentile under pinball loss, not the conditional mean.

</details>

### Q045. Can a Gamma model accept zero targets?

<details>
<summary>Answer</summary>

The usual Gamma response has strictly positive support; zero targets require a different model or justified treatment.

</details>

<a id="lesson-10"></a>

## 10 — Logistic regression and softmax classification

[Read the lesson](../01-theory/10-logistic-and-softmax.md)

### Q046. Why is logistic regression classification?

<details>
<summary>Answer</summary>

It models probabilities for categorical outcomes; the word regression refers to its regression on log odds.

</details>

### Q047. Does doubling odds double probability?

<details>
<summary>Answer</summary>

No. Odds 1 become 2, so probability moves from.5 to 2/3.

</details>

### Q048. What is the score gradient for binary cross-entropy?

<details>
<summary>Answer</summary>

With sigmoid output it is p−y; the weight gradient is (p−y)x.

</details>

### Q049. Softmax or independent sigmoid for multiple simultaneous tags?

<details>
<summary>Answer</summary>

Independent sigmoid outputs suit multilabel tags; softmax assumes mutually exclusive categories.

</details>

### Q050. What happens under complete separation without regularization?

<details>
<summary>Answer</summary>

Maximum likelihood can lack a finite coefficient optimum as magnitudes keep growing.

</details>

<a id="lesson-11"></a>

## 11 — Naive Bayes, LDA and QDA

[Read the lesson](../01-theory/11-bayes-and-discriminant-analysis.md)

### Q051. What is naive about Naive Bayes?

<details>
<summary>Answer</summary>

Conditional feature independence within each class, which simplifies the class likelihood into a product.

</details>

### Q052. Why use logarithms?

<details>
<summary>Answer</summary>

Products of many small probabilities can underflow; sums of logs preserve ordering more reliably.

</details>

### Q053. Does LDA require independent inputs?

<details>
<summary>Answer</summary>

No. Its shared covariance matrix can model feature correlations.

</details>

### Q054. Why can QDA overfit sooner?

<details>
<summary>Answer</summary>

A separate full covariance per class needs many more estimated parameters.

</details>

### Q055. How does Laplace smoothing handle an unseen category?

<details>
<summary>Answer</summary>

Add a pseudocount to every possible category and adjust the denominator consistently.

</details>

<a id="lesson-12"></a>

## 12 — K-nearest neighbours and distance

[Read the lesson](../01-theory/12-nearest-neighbours.md)

### Q056. Does KNN learn anything?

<details>
<summary>Answer</summary>

It is instance-based learning: the stored examples and neighbourhood rule form the predictive model even without a parametric training loop.

</details>

### Q057. Why scale?

<details>
<summary>Answer</summary>

A feature with large numeric units can dominate Euclidean distance without being more informative.

</details>

### Q058. Does larger k always improve accuracy?

<details>
<summary>Answer</summary>

No. It reduces local variability but can smooth away meaningful boundaries.

</details>

### Q059. Why is prediction potentially slow?

<details>
<summary>Answer</summary>

It may need distances to many stored training examples for every new query.

</details>

### Q060. Can ordinary KNN regression extrapolate a trend?

<details>
<summary>Answer</summary>

No. Positive-weight neighbour averages remain within the contributing target range.

</details>

<a id="lesson-13"></a>

## 13 — SVM, kernels and support vector regression

[Read the lesson](../01-theory/13-support-vector-machines.md)

### Q061. Can a correctly classified point incur hinge loss?

<details>
<summary>Answer</summary>

Yes. If its signed margin is between 0 and 1 it is correct but lies inside the desired margin.

</details>

### Q062. What does larger C do?

<details>
<summary>Answer</summary>

It increases the relative penalty for margin violations under the stated SVM objective.

</details>

### Q063. What does larger RBF gamma do?

<details>
<summary>Answer</summary>

It makes similarity decay faster with distance, allowing more local and potentially overfit boundaries.

</details>

### Q064. Are SVM scores probabilities?

<details>
<summary>Answer</summary>

No. Calibration or another probability estimation procedure is needed.

</details>

### Q065. Can SVR use kernels?

<details>
<summary>Answer</summary>

Yes. Kernelized support vector regression applies the same kernel idea with an epsilon-insensitive regression loss.

</details>

<a id="lesson-14"></a>

## 14 — Decision trees: entropy, Gini, regression and pruning

[Read the lesson](../01-theory/14-decision-trees.md)

### Q066. Does binary tree mean only two target classes?

<details>
<summary>Answer</summary>

No. CART uses two children per split and can predict many classes.

</details>

### Q067. How is information gain calculated?

<details>
<summary>Answer</summary>

Parent impurity minus the child impurities weighted by their sample proportions.

</details>

### Q068. What does a squared-error regression leaf predict?

<details>
<summary>Answer</summary>

The training target mean within that leaf, using sample weights if supplied.

</details>

### Q069. Why can a deep tree be unstable?

<details>
<summary>Answer</summary>

A small data change can alter an early greedy split and hence the entire downstream structure.

</details>

### Q070. What is the worked regression gain?

<details>
<summary>Answer</summary>

Parent MSE206 minus weighted child MSE85 equals 121 for the split at 162.5.

</details>

<a id="lesson-15"></a>

## 15 — Bagging, random forests and Extra Trees

[Read the lesson](../01-theory/15-bagging-and-forests.md)

### Q071. Bagging versus random forest?

<details>
<summary>Answer</summary>

A forest combines bootstrap-style tree averaging with random candidate feature subsets at splits.

</details>

### Q072. Why not average identical trees?

<details>
<summary>Answer</summary>

Perfectly correlated errors do not gain variance reduction from averaging.

</details>

### Q073. What fraction is OOB approximately?

<details>
<summary>Answer</summary>

For standard size-n bootstrap sampling, about e⁻¹≈36.8% of rows are omitted from any one sample.

</details>

### Q074. Can OOB replace a chronological split?

<details>
<summary>Answer</summary>

No. Its row-resampling assumptions do not recreate future forecasting.

</details>

### Q075. Do more trees always fix underfitting?

<details>
<summary>Answer</summary>

No. Averaging more weak or biased trees does not remove their shared systematic error.

</details>

<a id="lesson-16"></a>

## 16 — AdaBoost: learning from weighted mistakes

[Read the lesson](../01-theory/16-adaboost.md)

### Q076. Why are mistakes given more weight?

<details>
<summary>Answer</summary>

So subsequent learners focus on examples the current ensemble handles poorly.

</details>

### Q077. For error 1/7, what is alpha?

<details>
<summary>Answer</summary>

Half log 6≈.89588 in the stated binary formulation.

</details>

### Q078. What weight does the only mistake receive after normalization?

<details>
<summary>Answer</summary>

0.5; the other six examples receive 1/12 each.

</details>

### Q079. Why can label noise hurt AdaBoost?

<details>
<summary>Answer</summary>

The exponential loss may keep emphasizing examples that no sensible boundary should fit.

</details>

### Q080. Is the binary formula identical to multiclass SAMME?

<details>
<summary>Answer</summary>

No. Multiclass vote definitions differ; use the formulation implemented by the estimator.

</details>

<a id="lesson-17"></a>

## 17 — Gradient boosting, XGBoost, LightGBM and CatBoost

[Read the lesson](../01-theory/17-gradient-boosting.md)

### Q081. Are all boosting pseudo-residuals y−prediction?

<details>
<summary>Answer</summary>

No. That expression follows from squared error; other losses use their own negative derivative.

</details>

### Q082. Bagging versus boosting?

<details>
<summary>Answer</summary>

Bagging averages independently trained resampled learners; boosting sequentially adds corrections to an ensemble.

</details>

### Q083. Why tune learning rate and rounds together?

<details>
<summary>Answer</summary>

Smaller steps usually require more rounds; either setting alone gives an incomplete capacity choice.

</details>

### Q084. What is the leaf score for G=−6,H=2,lambda=1?

<details>
<summary>Answer</summary>

−G/(H+lambda)=6/3=2 under the stated second-order convention.

</details>

### Q085. Can early stopping use the final test set?

<details>
<summary>Answer</summary>

No. Choosing the stopping round uses labels and belongs to development validation.

</details>

<a id="lesson-18"></a>

## 18 — Voting, stacking and blending

[Read the lesson](../01-theory/18-voting-and-stacking.md)

### Q086. What is soft voting?

<details>
<summary>Answer</summary>

Average aligned class probabilities, then choose a class or apply a decision threshold.

</details>

### Q087. What makes stacking training honest?

<details>
<summary>Answer</summary>

Meta-features for each row come from base models that did not train on that row.

</details>

### Q088. Does OOF automatically handle time series?

<details>
<summary>Answer</summary>

No. The splitter used to generate OOF predictions must preserve the temporal prediction setting.

</details>

### Q089. Blending versus stacking?

<details>
<summary>Answer</summary>

Blending learns a combiner on a dedicated holdout; stacking commonly uses out-of-fold predictions.

</details>

### Q090. Why might a better ensemble still be rejected?

<details>
<summary>Answer</summary>

A small score gain may not justify latency, memory, cost and operational complexity.

</details>

<a id="lesson-19"></a>

## 19 — K-means, k-means++, mini-batch and k-medoids

[Read the lesson](../01-theory/19-centroid-clustering.md)

### Q091. Why does k-means use means?

<details>
<summary>Answer</summary>

The mean minimizes summed squared Euclidean distances within a fixed cluster.

</details>

### Q092. Does k-means find the global optimum?

<details>
<summary>Answer</summary>

Not generally. Initialization and local optima matter.

</details>

### Q093. What is WCSS for[1,2,8,9] at centres 1.5,8.5?

<details>
<summary>Answer</summary>

Four squared deviations of.25 sum to 1.

</details>

### Q094. Why not choose k only by minimum WCSS?

<details>
<summary>Answer</summary>

WCSS keeps improving as k grows; at one centre per point it is 0 but gives no useful grouping.

</details>

### Q095. What does silhouette.75 mean in the a=1,b=4 example?

<details>
<summary>Answer</summary>

The point is substantially closer on average to its own cluster than the nearest alternative cluster under that distance.

</details>

<a id="lesson-20"></a>

## 20 — Hierarchical clustering and BIRCH

[Read the lesson](../01-theory/20-hierarchical-clustering.md)

### Q096. What does dendrogram height mean?

<details>
<summary>Answer</summary>

The dissimilarity or merge criterion at which groups joined, with meaning depending on linkage.

</details>

### Q097. Why does single linkage chain?

<details>
<summary>Answer</summary>

Only one close pair is needed to join two groups, so bridges can link otherwise distant regions.

</details>

### Q098. Can Ward use any arbitrary distance?

<details>
<summary>Answer</summary>

Its variance-minimization interpretation relies on Euclidean geometry.

</details>

### Q099. Why can hierarchical clustering be expensive?

<details>
<summary>Answer</summary>

Pairwise distance storage and merge operations can scale poorly, often with quadratic memory.

</details>

### Q100. What does BIRCH compress?

<details>
<summary>Answer</summary>

It summarizes subclusters in a clustering-feature tree before optional global clustering.

</details>

<a id="lesson-21"></a>

## 21 — DBSCAN, OPTICS and HDBSCAN

[Read the lesson](../01-theory/21-density-clustering.md)

### Q101. Does DBSCAN need k?

<details>
<summary>Answer</summary>

It does not require a preset number of clusters; radius, density support and data determine the grouping.

</details>

### Q102. Is every noise point an anomaly in the business sense?

<details>
<summary>Answer</summary>

No. It is unassigned under a particular density rule, which may be poorly chosen.

</details>

### Q103. What makes a core point?

<details>
<summary>Answer</summary>

At least the required number of observations in its radius neighbourhood under the stated counting convention.

</details>

### Q104. Why can one radius fail?

<details>
<summary>Answer</summary>

Dense and sparse true groups may need very different neighbourhood scales.

</details>

### Q105. Can we report silhouette after removing noise without comment?

<details>
<summary>Answer</summary>

No. Report how much data was excluded and assess stability and usefulness too.

</details>

<a id="lesson-22"></a>

## 22 — Gaussian mixtures, EM and density estimation

[Read the lesson](../01-theory/22-mixtures-and-em.md)

### Q106. K-means or GMM: which has soft assignments?

<details>
<summary>Answer</summary>

A Gaussian mixture supplies posterior responsibilities; ordinary k-means uses hard assignments.

</details>

### Q107. Does EM guarantee the best global fit?

<details>
<summary>Answer</summary>

No. Exact steps improve or preserve likelihood but may reach a local optimum.

</details>

### Q108. Why regularize covariance?

<details>
<summary>Answer</summary>

To reduce ill-conditioning and discourage collapsed components with near-zero variance.

</details>

### Q109. What does BIC penalize?

<details>
<summary>Answer</summary>

Model parameter count relative to sample size, trading likelihood against complexity under its assumptions.

</details>

### Q110. What controls KDE smoothness?

<details>
<summary>Answer</summary>

Bandwidth: small values create spikes; large values wash out structure.

</details>

<a id="lesson-23"></a>

## 23 — PCA, SVD, NMF, ICA and cross-decomposition

[Read the lesson](../01-theory/23-linear-dimension-reduction.md)

### Q111. Does PCA use y?

<details>
<summary>Answer</summary>

Ordinary PCA does not; it maximizes input variance, which may not align with predictive signal.

</details>

### Q112. Why centre?

<details>
<summary>Answer</summary>

PCA directions should describe variation around the mean rather than the mean offset itself.

</details>

### Q113. How much variance does the example first component retain?

<details>
<summary>Answer</summary>

6 divided by 6+2/3 equals.9, or 90%.

</details>

### Q114. PCA versus truncated SVD on sparse text?

<details>
<summary>Answer</summary>

Truncated SVD often avoids centering and preserves sparse practicality; it is not the same centred problem.

</details>

### Q115. Why must PLS be inside CV?

<details>
<summary>Answer</summary>

Its representation uses target information and would leak labels if fitted before splitting.

</details>

<a id="lesson-24"></a>

## 24 — Kernel PCA, manifolds, t-SNE, UMAP and spectral methods

[Read the lesson](../01-theory/24-manifolds-and-spectral-methods.md)

### Q116. Do t-SNE islands prove distinct real clusters?

<details>
<summary>Answer</summary>

No. Local-neighbourhood preservation can produce visually separated islands without validated semantic groups.

</details>

### Q117. What does spectral clustering start from?

<details>
<summary>Answer</summary>

A similarity graph and its Laplacian; graph construction is central to the grouping.

</details>

### Q118. Why can Isomap fail?

<details>
<summary>Answer</summary>

A bad neighbourhood graph may disconnect regions or create shortcuts that corrupt estimated geodesic distances.

</details>

### Q119. Can every embedding transform new points?

<details>
<summary>Answer</summary>

No. Out-of-sample support varies and must be checked before using it in a predictive pipeline.

</details>

### Q120. Why repeat plots across seeds/settings?

<details>
<summary>Answer</summary>

To see whether apparent structure is stable rather than an initialization or hyperparameter artifact.

</details>

<a id="lesson-25"></a>

## 25 — Anomaly, novelty and outlier detection

[Read the lesson](../01-theory/25-anomaly-detection.md)

### Q121. Anomaly or fraud: same thing?

<details>
<summary>Answer</summary>

No. Statistical unusualness and business harm are different targets.

</details>

### Q122. What is novelty detection?

<details>
<summary>Answer</summary>

Fit a notion of normality on reference data and detect unusual new observations.

</details>

### Q123. Why can LOF treat a sparse group as normal?

<details>
<summary>Answer</summary>

It compares density locally with neighbouring points rather than only with a global average.

</details>

### Q124. Does contamination reveal the true anomaly rate?

<details>
<summary>Answer</summary>

No. It is a modelling/threshold assumption or configuration, not verified ground truth.

</details>

### Q125. How evaluate a 50-alert daily queue?

<details>
<summary>Answer</summary>

Use capacity-aware measures such as precision@50 plus reviewed outcomes and a strategy to estimate missed cases.

</details>

<a id="lesson-26"></a>

## 26 — Feature selection, imbalanced learning and label quality

[Read the lesson](../01-theory/26-feature-selection-and-imbalance.md)

### Q126. Feature selection versus extraction?

<details>
<summary>Answer</summary>

Selection keeps original columns; extraction creates new representations such as principal components.

</details>

### Q127. Why is global correlation filtering leakage?

<details>
<summary>Answer</summary>

It uses validation labels to choose predictors before evaluation.

</details>

### Q128. Does oversampling create independent information?

<details>
<summary>Answer</summary>

No. Repeating observations or interpolating neighbours does not create independent verified outcomes.

</details>

### Q129. Why keep test prevalence realistic?

<details>
<summary>Answer</summary>

Precision, probabilities and operational workload depend on the population being evaluated.

</details>

### Q130. What should come before SMOTE?

<details>
<summary>Answer</summary>

A correct target/split, suitable metrics, a baseline and threshold/cost analysis.

</details>

<a id="lesson-27"></a>

## 27 — Bayesian learning and Gaussian processes

[Read the lesson](../01-theory/27-bayesian-learning-and-gaussian-processes.md)

### Q131. Posterior versus likelihood?

<details>
<summary>Answer</summary>

The likelihood scores observations under parameters; the posterior combines likelihood with a prior and normalizes over parameters.

</details>

### Q132. What is Beta(1,1) updated by 7 successes 3 failures?

<details>
<summary>Answer</summary>

Beta(8,4), with posterior mean 8/12=2/3.

</details>

### Q133. Why does a GP need a kernel?

<details>
<summary>Answer</summary>

It specifies covariance between function values and thus the assumed notion of smoothness/similarity.

</details>

### Q134. Latent variance versus observation variance?

<details>
<summary>Answer</summary>

Observation prediction also includes measurement/noise variance, beyond uncertainty about the latent function.

</details>

### Q135. Why are exact GPs hard to scale?

<details>
<summary>Answer</summary>

Dense covariance factorization typically costs O (n³)time and O (n²)memory.

</details>

<a id="lesson-28"></a>

## 28 — Recommendation, matrix factorization and ranking

[Read the lesson](../01-theory/28-recommendation-and-ranking.md)

### Q136. Is no click always a negative preference?

<details>
<summary>Answer</summary>

No. Lack of exposure, position and opportunity can explain it.

</details>

### Q137. Why use matrix factorization?

<details>
<summary>Answer</summary>

It models a sparse interaction matrix with lower-dimensional user/item representations and regularization.

</details>

### Q138. What is cold start?

<details>
<summary>Answer</summary>

Prediction for new users/items lacking historical interactions; metadata or fallback strategies are needed.

</details>

### Q139. Why not evaluate ranking only with RMSE?

<details>
<summary>Answer</summary>

Small rating error does not ensure relevant items occupy the top positions.

</details>

### Q140. Why chronological evaluation?

<details>
<summary>Answer</summary>

It prevents future interactions from informing recommendations that are supposed to happen earlier.

</details>

<a id="lesson-29"></a>

## 29 — Association rules, Apriori and FP-growth

[Read the lesson](../01-theory/29-association-rules.md)

### Q141. Does bread⇒butter imply causation?

<details>
<summary>Answer</summary>

No. It describes co-occurrence; confounding and shared shopping context can explain it.

</details>

### Q142. Compute confidence for 20joint and 40bread baskets.

<details>
<summary>Answer</summary>

20/40=.5.

</details>

### Q143. Why can high confidence be misleading?

<details>
<summary>Answer</summary>

The consequent may already be extremely common; compare its base rate and lift.

</details>

### Q144. What property powers Apriori pruning?

<details>
<summary>Answer</summary>

Every subset of a frequent itemset must also be frequent under the same support threshold.

</details>

### Q145. How does FP-growth differ?

<details>
<summary>Answer</summary>

It mines compressed conditional pattern structures instead of explicitly enumerating all candidates level by level.

</details>

<a id="lesson-30"></a>

## 30 — Semi-supervised, self-supervised, weak and active learning

[Read the lesson](../01-theory/30-semi-self-and-weak-supervision.md)

### Q146. Semi-supervised versus self-supervised?

<details>
<summary>Answer</summary>

Semi-supervised uses some task labels plus unlabelled data; self-supervised creates a training signal from the data itself.

</details>

### Q147. What is pseudo-label confirmation bias?

<details>
<summary>Answer</summary>

The model reinforces its own wrong high-confidence predictions by treating them as labels.

</details>

### Q148. Does active learning simply choose random rows?

<details>
<summary>Answer</summary>

It selects rows by an information/cost strategy, though random exploration can improve coverage.

</details>

### Q149. Why can an augmentation be harmful?

<details>
<summary>Answer</summary>

It may change the true label, invalidating an assumed same-label or consistency relation.

</details>

### Q150. Can unlabelled test data be freely used?

<details>
<summary>Answer</summary>

Only under an explicitly defined transductive evaluation setting; ordinary inductive testing must keep its protocol uncontaminated.

</details>

<a id="lesson-31"></a>

## 31 — Online learning, drift and federated learning

[Read the lesson](../01-theory/31-online-and-federated-learning.md)

### Q151. What is prequential evaluation?

<details>
<summary>Answer</summary>

Predict on an incoming example, score when its label arrives, then update using that example.

</details>

### Q152. Can input drift monitoring detect all concept drift?

<details>
<summary>Answer</summary>

No. P (Y|X)can change while the input distribution stays similar.

</details>

### Q153. Does partial_fit exist for every model?

<details>
<summary>Answer</summary>

No. Incremental updates are estimator-specific and may have representation/class constraints.

</details>

### Q154. Does federated mean private?

<details>
<summary>Answer</summary>

No. Local data storage does not prevent information leakage through updates or outputs.

</details>

### Q155. What is a forgetting trade-off?

<details>
<summary>Answer</summary>

Faster adaptation may discard useful stable knowledge or overreact to transient noise.

</details>

<a id="lesson-32"></a>

## 32 — Reinforcement learning and contextual bandits

[Read the lesson](../01-theory/32-reinforcement-learning.md)

### Q156. Why is RL not ordinary supervised classification?

<details>
<summary>Answer</summary>

Actions affect future observations and rewards; there is not generally a fixed correct-action label for each state.

</details>

### Q157. SARSA versus Q-learning?

<details>
<summary>Answer</summary>

SARSA bootstraps the action taken by the behaviour policy; Q-learning uses the greedy next-action value.

</details>

### Q158. Compute the worked Q update.

<details>
<summary>Answer</summary>

Target=1+.9×4=4.6;2+.1×(4.6−2)=2.26.

</details>

### Q159. What is exploration?

<details>
<summary>Answer</summary>

Taking actions partly to gain information rather than only maximizing the current estimated reward.

</details>

### Q160. Does PPO clipping guarantee safe deployment?

<details>
<summary>Answer</summary>

No. It constrains a surrogate update mechanism and does not establish operational safety or correct reward design.

</details>

<a id="lesson-33"></a>

## 33 — Neural networks and representation learning

[Read the lesson](../01-theory/33-neural-networks.md)

### Q161. Why nonlinear activations?

<details>
<summary>Answer</summary>

Without them, a stack of linear layers is equivalent to a single linear map.

</details>

### Q162. Backpropagation versus Adam?

<details>
<summary>Answer</summary>

Backprop computes gradients; Adam uses gradients and running moments to choose parameter updates.

</details>

### Q163. Which head for multiple simultaneous labels?

<details>
<summary>Answer</summary>

Independent sigmoid outputs with a suitable multilabel loss, not an exclusive softmax.

</details>

### Q164. Does an autoencoder guarantee anomaly detection?

<details>
<summary>Answer</summary>

No. It can reconstruct unusual cases or learn irrelevant reconstruction structure.

</details>

### Q165. Why compare neural nets with trees on tabular data?

<details>
<summary>Answer</summary>

Inductive bias, sample size and compute differ; a simpler tabular model may generalize better with less tuning.

</details>

<a id="lesson-34"></a>

## 34 — Text, time series, survival and structured prediction

[Read the lesson](../01-theory/34-specialized-prediction.md)

### Q166. What is right censoring?

<details>
<summary>Answer</summary>

The event has not been observed by the last follow-up time; the true event time is later, not equal to that time.

</details>

### Q167. Why is a random forecasting split dangerous?

<details>
<summary>Answer</summary>

Future information can train a model evaluated on the past, unlike the real forecasting task.

</details>

### Q168. Hazard ratio 2 equals double event probability?

<details>
<summary>Answer</summary>

No. It multiplies the modelled instantaneous hazard under its assumptions, not every cumulative event probability.

</details>

### Q169. Why span metrics for entity recognition?

<details>
<summary>Answer</summary>

Correct complete entities matter; token accuracy can be inflated by many non-entity tokens.

</details>

### Q170. Binary relevance versus classifier chains?

<details>
<summary>Answer</summary>

Binary relevance fits labels separately; chains use preceding label predictions as inputs to model dependencies.

</details>

<a id="lesson-35"></a>

## 35 — Interpretability, permutation importance, SHAP and dependence plots

[Read the lesson](../01-theory/35-interpretability.md)

### Q171. Does feature importance imply causality?

<details>
<summary>Answer</summary>

No. It describes a fitted model under a measurement/perturbation procedure.

</details>

### Q172. Why can permutation understate a feature?

<details>
<summary>Answer</summary>

A correlated predictor can substitute for it after shuffling.

</details>

### Q173. PDP versus ICE?

<details>
<summary>Answer</summary>

PDP averages response curves; ICE retains per-example curves and can reveal heterogeneous behaviour.

</details>

### Q174. Why does a SHAP background matter?

<details>
<summary>Answer</summary>

It defines the reference and missing-feature comparison, changing the attribution game.

</details>

### Q175. Can a faithful explanation justify an unfair decision?

<details>
<summary>Answer</summary>

No. Faithfulness describes model behaviour; acceptability and policy require separate assessment.

</details>

<a id="lesson-36"></a>

## 36 — Uncertainty, prediction intervals and conformal prediction

[Read the lesson](../01-theory/36-uncertainty-and-conformal.md)

### Q176. Confidence versus prediction interval?

<details>
<summary>Answer</summary>

A confidence interval targets an estimated parameter/mean; a prediction interval targets a new outcome and includes outcome variability.

</details>

### Q177. For m=9,alpha=.2, what conformal rank?

<details>
<summary>Answer</summary>

Ceiling((9+1)×.8)=8.

</details>

### Q178. Does marginal coverage mean every subgroup has that coverage?

<details>
<summary>Answer</summary>

No. Marginal coverage averages over the joint population under the stated assumptions.

</details>

### Q179. Why not tune on calibration labels repeatedly?

<details>
<summary>Answer</summary>

Adaptive reuse can invalidate the protocol underlying the coverage guarantee.

</details>

### Q180. Can a perfect coverage score be useless?

<details>
<summary>Answer</summary>

Yes. An extremely wide interval may cover nearly everything without supporting a useful decision.

</details>

<a id="lesson-37"></a>

## 37 — Causality, fairness, robustness and responsible evaluation

[Read the lesson](../01-theory/37-causality-fairness-and-robustness.md)

### Q181. Does prediction imply intervention effect?

<details>
<summary>Answer</summary>

No. Association can arise from confounding or reverse causation.

</details>

### Q182. What is overlap in causal inference?

<details>
<summary>Answer</summary>

Relevant covariate groups must have a nonzero chance of receiving each compared treatment under the assumed design.

</details>

### Q183. Does dropping sensitive features ensure fairness?

<details>
<summary>Answer</summary>

No. Proxies, label bias and decision procedures can preserve disparities.

</details>

### Q184. Can all fairness criteria always hold together?

<details>
<summary>Answer</summary>

Generally no. Calibration and error-rate parity can conflict when base rates differ.

</details>

### Q185. Poisoning versus evasion?

<details>
<summary>Answer</summary>

Poisoning manipulates training data/process; evasion manipulates inputs at prediction time.

</details>

<a id="lesson-38"></a>

## 38 — Deployment, reproducibility and monitoring

[Read the lesson](../01-theory/38-deployment-and-monitoring.md)

### Q186. What belongs with the saved estimator?

<details>
<summary>Answer</summary>

Preprocessing, schema, feature definitions, label order, threshold, environment/version and validation evidence.

</details>

### Q187. What is training–serving skew?

<details>
<summary>Answer</summary>

Features or transformations differ between offline training and actual prediction.

</details>

### Q188. Does input drift always require retraining?

<details>
<summary>Answer</summary>

No. Investigate data bugs, harmless changes and actual performance before choosing a response.

</details>

### Q189. Why can observed live labels be biased?

<details>
<summary>Answer</summary>

Only selected cases may receive labels, and model actions can change which outcomes are observable.

</details>

### Q190. Why keep a rollback?

<details>
<summary>Answer</summary>

A statistically promising replacement can still fail operationally or under unexpected data.

</details>

<a id="lesson-39"></a>

## 39 — Choose an algorithm and diagnose the result

[Read the lesson](../01-theory/39-algorithm-selection.md)

### Q191. What should precede extensive tuning?

<details>
<summary>Answer</summary>

Verify target, prediction-time features, split and baseline, then inspect actual errors.

</details>

### Q192. Why compare models on the same folds?

<details>
<summary>Answer</summary>

It makes score differences less confounded by differing samples, while still respecting task structure.

</details>

### Q193. High AUC, poor precision: first action?

<details>
<summary>Answer</summary>

Check prevalence, threshold, PR behaviour and operational capacity rather than assuming the ranking model is useless.

</details>

### Q194. Why include serving cost?

<details>
<summary>Answer</summary>

An improvement may not be usable within latency, memory or maintenance constraints.

</details>

### Q195. Does this table replace evaluation?

<details>
<summary>Answer</summary>

No. It suggests candidates from assumptions; the actual valid comparison decides.

</details>

<a id="lesson-40"></a>

## 40 — Advanced families, formula sheet and coverage map

[Read the lesson](../01-theory/40-advanced-catalog-and-formula-sheet.md)

### Q196. What is a GAM?

<details>
<summary>Answer</summary>

A model summing learned feature functions, often with penalties; nonlinear effects can remain separately inspectable.

</details>

### Q197. What does a graphical model specify?

<details>
<summary>Answer</summary>

A factorization of a distribution and conditional-dependence assumptions, with a corresponding inference/learning problem.

</details>

### Q198. Why is an advanced catalogue useful?

<details>
<summary>Answer</summary>

It connects less common families to their objective, use and limits without confusing survey entries with full lessons.

</details>

### Q199. Does a Bayesian-network arrow automatically prove causality?

<details>
<summary>Answer</summary>

No. Causal interpretation needs explicit assumptions and evidence beyond a fitted dependency graph.

</details>

### Q200. What demonstrates course understanding?

<details>
<summary>Answer</summary>

A justified end-to-end modelling decision with correct data timing, objective, evaluation, error analysis and practical constraints.

</details>

# Mathematics and Statistics — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Algebra, functions, logarithms and mathematical notation](#lesson-01)
- [02 — Vectors, matrices, projections, eigenvectors and SVD](#lesson-02)
- [03 — Derivatives, partial derivatives, chain rule and integration](#lesson-03)
- [04 — Data types, summaries, spread and relationships](#lesson-04)
- [05 — Probability, conditioning, independence and Bayes](#lesson-05)
- [06 — Random variables, distributions, likelihood and the CLT](#lesson-06)
- [07 — Estimation, intervals, hypothesis tests and multiple comparisons](#lesson-07)
- [08 — t-tests, ANOVA, chi-square, nonparametric tests and experiments](#lesson-08)

<a id="lesson-01"></a>

## 01 — Algebra, functions, logarithms and mathematical notation

[Read the lesson](../01-theory/lesson-01-mathematical-language.md)

### Q001. Why use logs for likelihood products?

<details>
<summary>Answer</summary>

Products of small probabilities become sums of logs, improving numerical handling and simplifying optimization.

</details>

### Q002. Is log(a+b)=log(a)+log(b)?

<details>
<summary>Answer</summary>

No. The product rule applies to log(ab), not a sum.

</details>

### Q003. Why record units in a formula?

<details>
<summary>Answer</summary>

They identify invalid operations and make resulting coefficients/errors interpretable.

</details>

<a id="lesson-02"></a>

## 02 — Vectors, matrices, projections, eigenvectors and SVD

[Read the lesson](../01-theory/lesson-02-vectors-and-transformations.md)

### Q004. Can a rectangular matrix have an ordinary inverse?

<details>
<summary>Answer</summary>

No two-sided ordinary square inverse; pseudoinverses or least-squares methods solve appropriate related problems.

</details>

### Q005. What does rank deficiency mean for regression?

<details>
<summary>Answer</summary>

Some feature directions are redundant; coefficients may be nonunique or unstable.

</details>

### Q006. Why does PCA need centering?

<details>
<summary>Answer</summary>

To describe variation around the mean rather than the offset of the data cloud from zero.

</details>

<a id="lesson-03"></a>

## 03 — Derivatives, partial derivatives, chain rule and integration

[Read the lesson](../01-theory/lesson-03-calculus-and-optimization.md)

### Q007. Partial derivative versus total derivative?

<details>
<summary>Answer</summary>

A partial changes one independent coordinate; a total derivative accounts for dependencies along a specified change/path.

</details>

### Q008. Why chain rule for networks?

<details>
<summary>Answer</summary>

Outputs depend on parameters through nested intermediate functions.

</details>

### Q009. Does zero gradient prove the best solution?

<details>
<summary>Answer</summary>

No. It may be a maximum, saddle or only a local minimum.

</details>

<a id="lesson-04"></a>

## 04 — Data types, summaries, spread and relationships

[Read the lesson](../01-theory/lesson-04-descriptive-statistics.md)

### Q010. SD versus standard error?

<details>
<summary>Answer</summary>

SD measures observation spread; SE measures sampling variability of a statistic such as the mean.

</details>

### Q011. Is postcode quantitative?

<details>
<summary>Answer</summary>

Usually it is a categorical identifier despite numeric storage.

</details>

### Q012. Why plot before trusting a correlation?

<details>
<summary>Answer</summary>

Nonlinearity, groups and outliers can produce misleading single-number summaries.

</details>

<a id="lesson-05"></a>

## 05 — Probability, conditioning, independence and Bayes

[Read the lesson](../01-theory/lesson-05-probability-and-bayes.md)

### Q013. Mutually exclusive versus independent?

<details>
<summary>Answer</summary>

Exclusive events cannot occur together; independent events do not change each other’s probability.

</details>

### Q014. Why does low prevalence reduce positive predictive value?

<details>
<summary>Answer</summary>

Even a modest false-positive rate applies to a much larger nontarget population.

</details>

### Q015. Does expectation require independence to add?

<details>
<summary>Answer</summary>

No. E[X+Y]=E[X]+E[Y] whenever expectations exist.

</details>

<a id="lesson-06"></a>

## 06 — Random variables, distributions, likelihood and the CLT

[Read the lesson](../01-theory/lesson-06-random-variables-and-distributions.md)

### Q016. Can a continuous density exceed 1?

<details>
<summary>Answer</summary>

Yes. Only its integrated probability must respect probability bounds.

</details>

### Q017. What becomes approximately normal under a CLT?

<details>
<summary>Answer</summary>

A suitably standardized aggregate such as a mean, under specified conditions; not necessarily individual observations.

</details>

### Q018. How does SE change when n quadruples?

<details>
<summary>Answer</summary>

It halves for the usual independent mean with fixed variance.

</details>

<a id="lesson-07"></a>

## 07 — Estimation, intervals, hypothesis tests and multiple comparisons

[Read the lesson](../01-theory/lesson-07-estimation-and-inference.md)

### Q019. Does p=.03 mean a 97% chance the alternative is true?

<details>
<summary>Answer</summary>

No. It is a tail probability conditional on the null model, not a posterior hypothesis probability.

</details>

### Q020. Why report effect sizes?

<details>
<summary>Answer</summary>

A tiny effect can be significant in a huge sample yet be irrelevant to the decision.

</details>

### Q021. What does multiple-testing control address?

<details>
<summary>Answer</summary>

A specified error criterion across a family of analyses, rather than pretending every isolated threshold remains a global error rate.

</details>

<a id="lesson-08"></a>

## 08 — t-tests, ANOVA, chi-square, nonparametric tests and experiments

[Read the lesson](../01-theory/lesson-08-tests-and-experiment-design.md)

### Q022. What does significant ANOVA establish?

<details>
<summary>Answer</summary>

Evidence against equality of all group means under the model; it does not name all differing pairs.

</details>

### Q023. Why analyse paired differences?

<details>
<summary>Answer</summary>

The design links observations, and within-pair analysis accounts for that structure.

</details>

### Q024. Percentage points versus relative lift?

<details>
<summary>Answer</summary>

10% to 12% is 2 percentage points and 20% relative increase.

</details>

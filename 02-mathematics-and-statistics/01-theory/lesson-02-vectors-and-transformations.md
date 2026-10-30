# 02 — Vectors, matrices, projections, eigenvectors and SVD

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-02)

```mermaid
flowchart LR
 N0["Vector"] --> N1["Matrix transformation"] --> N2["Projection"] --> N3["Retained and discarded directions"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A matrix is a machine that transforms vectors; eigenvectors are directions it stretches without turning.

A vector represents coordinates or features. Its norm measures length, its dot product combines aligned components, and its direction matters separately from scale. A matrix product composes weighted combinations; order matters. A matrix of $n$ rows and $p$ features maps coefficient vectors of length $p$ to $n$ predictions.

Linear independence means no vector is a combination of the others. Rank counts independent directions. An inverse exists only for an appropriate nonsingular square matrix; least-squares solutions use projections and can be computed with QR/SVD without explicitly forming an inverse. Orthogonal projection finds the closest point in a subspace under squared Euclidean distance.

An eigenpair satisfies $Av=\lambda v$ for nonzero $v$. SVD writes $X=U\Sigma V^T$ and works for rectangular matrices. PCA centres observations and retains variance directions from covariance eigenvectors or SVD. High explained variance does not guarantee preserved predictive information. For the full geometric diagrams and calculations, continue with the retained linear-algebra visual guide linked in the course index.

## Work through it

For $A=\begin{bmatrix}2&0\\0&1\end{bmatrix}$, vector $(1,0)$ is stretched to $(2,0)$, so it is an eigenvector with eigenvalue 2. Vector $(1,1)$ becomes $(2,1)$ and changes direction, so it is not an eigenvector.

Project $(3,2)$ onto the horizontal axis to obtain $(3,0)$. Squared reconstruction error is 4. In PCA, that discarded perpendicular variation is the information a lower-rank representation loses.

## Common mistakes and practical limits

Matrix multiplication is not elementwise multiplication or generally commutative. A covariance eigenvector describes variation, not a causal mechanism. Avoid interpreting an arbitrary eigenvector sign flip as a different component.

---

[← Algebra, functions, logarithms and mathematical notation](lesson-01-mathematical-language.md) · [Derivatives, partial derivatives, chain rule and integration →](lesson-03-calculus-and-optimization.md)

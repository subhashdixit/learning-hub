# 01 — Algebra, functions, logarithms and mathematical notation

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-01)

```mermaid
flowchart LR
 N0["Quantity and units"] --> N1["Function"] --> N2["Allowed domain"] --> N3["Output interpretation"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** Algebra replaces an unknown quantity with a label so a relationship can be reasoned about.

A scalar is one number; a variable names a quantity; a function maps allowed inputs to outputs. Domain means allowed inputs, range means attained outputs. Solving an equation finds values satisfying equality; an inequality describes a region. Operations such as division require checking whether a denominator can be zero.

Powers and logarithms undo one another: if $b^a=x$, then $\log_b x=a$, for positive base other than 1 and positive input. Natural logarithms use base $e$. Log products become sums, which helps compute small likelihood products and interpret multiplicative change. A logarithm cannot accept zero or negative real inputs under the ordinary real-valued definition.

Summation notation $\sum_{i=1}^n x_i$ adds observations; an index labels a position, not a new measurement. Units matter: adding metres to seconds is invalid, and a ratio can have different meaning from a difference. In data science, a formula should specify shape, units and what is held fixed before it is translated into code.

## Work through it

If revenue $R=pq$ with price 20 and quantity 50, revenue is 1000. A10% quantity increase at fixed price produces 1100; simultaneous price changes require recomputing the product. For probabilities 0.01 repeated 3 times, the product is $10^{-6}$ and its natural log is $3\log0.01\approx-13.8155$.

For $2x+3=11$, subtract 3 then divide by 2 to obtain $x=4$. Squaring both sides in more complicated equations can introduce extraneous solutions, so substitute candidates back into the original relation.

## Common mistakes and practical limits

Do not cancel a quantity that might be zero. Correlation between two variables does not make their functional relation causal. Log rules do not permit log(a+b)=log(a)+log(b).

---

[Subject home](../README.md) · [Vectors, matrices, projections, eigenvectors and SVD →](lesson-02-vectors-and-transformations.md)

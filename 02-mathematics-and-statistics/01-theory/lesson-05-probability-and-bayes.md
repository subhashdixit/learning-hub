# 05 — Probability, conditioning, independence and Bayes

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-05)

```mermaid
flowchart LR
 N0["Prior rate"] --> N1["Likelihood"] --> N2["Conditional evidence"] --> N3["Posterior probability"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** Conditional probability changes the reference group: the denominator tells you whose outcomes you are counting.

Events are sets of possible outcomes. The complement rule gives $P(A^c)=1-P(A)$; the addition rule gives $P(A\cup B)=P(A)+P(B)-P(A\cap B)$. Conditional probability is $P(A|B)=P(A\cap B)/P(B)$ when $P(B)>0$. Independence means $P(A\cap B)=P(A)P(B)$; mutually exclusive nonzero-probability events are not independent.

Bayes' rule reverses a conditional using priors and likelihoods:$P(A|B)=P(B|A)P(A)/P(B)$. The base rate matters. A test with high sensitivity may still yield many false alerts when the target event is very rare. This is a general probability example, not an instruction about a real medical or financial test.

Expected value is a probability-weighted average; it need not be a possible single outcome. Linearity of expectation does not require independence, while simple variance addition does require zero covariance. Conditional independence is relative to what has been observed and differs from unconditional independence.

## Work through it

A synthetic screening system checks 10000 cases with 1% target prevalence:100 target and 9900 nontarget. At 90% sensitivity it flags 90 true cases; at 5% false-positive rate it flags 495 nontarget cases. Positive predictive value is $90/(90+495)=0.1538$, despite the high sensitivity.

For independent fair coin flips, the probability of two heads is $0.5\times0.5=0.25$. If the second outcome is deliberately copied from the first, that multiplication assumption fails.

## Common mistakes and practical limits

P(A|B) and  P(B|A) are usually different. A tiny p-value is not a posterior probability that a null is true. Verify the event universe and denominator before applying formulas.

---

[← Data types, summaries, spread and relationships](lesson-04-descriptive-statistics.md) · [Random variables, distributions, likelihood and the CLT →](lesson-06-random-variables-and-distributions.md)

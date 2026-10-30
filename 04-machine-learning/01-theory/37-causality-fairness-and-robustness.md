# 37 — Causality, fairness, robustness and responsible evaluation

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions and answers](../03-questions-and-answers/worked-questions.md#lesson-37)

```mermaid
flowchart LR
 Predictive_claim["Predictive claim"] --> Appropriate_evidence["Appropriate evidence"] --> Group_and_shift_checks["Group and shift checks"] --> Decision_review["Decision review"]
```

## On this page

- [Prediction and intervention ask different questions](#prediction-and-intervention-ask-different-questions)
- [Fairness is a decision problem with multiple definitions](#fairness-is-a-decision-problem-with-multiple-definitions)
- [Robustness and security](#robustness-and-security)

## Prediction and intervention ask different questions

A predictor estimates associations useful for $P(Y|X)$. A causal question asks what changes under an intervention, often written $P(Y|do(X=x))$. Umbrella purchases predict rain but do not cause it. A high model coefficient or SHAP value cannot by itself tell you which action will improve an outcome.

A confounder affects treatment and outcome. Randomized experiments break treatment–confounder association in expectation; observational methods require explicit identification assumptions. Propensity weighting, matching, outcome regression and doubly robust methods are tools, not substitutes for assumptions such as exchangeability/no unmeasured confounding, overlap and consistency.

```mermaid
flowchart LR
 C[Prior health] --> T[Treatment choice]
 C --> Y[Recovery]
 T --> Y
```

If healthier patients preferentially receive a treatment, comparing recovery rates mixes treatment and prior health. Conditioning on colliders or using post-treatment variables can introduce new bias. For individual treatment-effect prediction, validation is difficult because both potential outcomes are not observed for the same person. Uplift modelling aims at incremental response, not just likely response.

## Fairness is a decision problem with multiple definitions

| Check | Meaning | Why context matters |
|---|---|---|
| Demographic parity | Similar positive-decision rates across groups | Ignores differing outcomes and decision context |
| Equal opportunity | Similar true-positive rates | Requires credible outcomes and sufficient positives |
| Equalized odds | Similar TPR and FPR | May conflict with other requirements |
| Calibration within groups | Comparable probability meaning | Can conflict with error-rate parity when base rates differ |

These goals can be mutually incompatible in nontrivial settings. Removing a sensitive column does not remove correlated proxies or historical bias. Inspect group sample sizes and uncertainty; small groups can have unstable estimates. Engage domain and affected-user context when defining acceptable trade-offs rather than treating one fairness metric as universal approval.

## Robustness and security

Test ordinary distribution shifts: new locations, missing fields, unit changes, seasonal drift and corrupted inputs. Adversarial robustness concerns deliberate input perturbations under a threat model. Data poisoning changes training evidence; evasion changes prediction inputs; model extraction and membership inference target model information. A single random-noise test does not evaluate all these threats.

Use stress tests, schema validation, sensible constraints, redacted logs and an abstention/escalation plan matched to the application. Evaluate harms and false alerts, not just aggregate scores. Reproducibility requires versions, seeds, split definitions and data provenance; reproducible computation does not prove the data or objective was appropriate.

**Checkpoint:** state whether a claim is predictive, causal, fairness-related or security-related, and provide the corresponding evidence rather than using one accuracy number to answer all four.

---

[← 36: Uncertainty, prediction intervals and conformal prediction](36-uncertainty-and-conformal.md) · [38: Deployment, reproducibility and monitoring →](38-deployment-and-monitoring.md)

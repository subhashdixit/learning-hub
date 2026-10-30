# Chronological forecasting baselines and smoothing

[Practicals](../README.md) · [Theory](../../01-theory/README.md) · [Questions](../../03-questions-and-answers/worked-questions.md)

## Run and inspect

Run `python3 lab.py` from this folder with Python 3.10 or later. The lab uses the standard library and local/synthetic data; no account, API key or package installation is needed. It contains assertions for its worked arithmetic and failure cases.

1. Read the script and predict its results.
2. Run it and explain each assertion.
3. Change one assumption and predict what should change.
4. Reproduce the result from a clean process.

[Open the complete script](lab.py).

## Extend the exercise

Add a structural break and inspect performance over time instead of one total. Implement a fixed-origin 7-step evaluation and explain why it differs from the current daily-updated one-step procedure. Compare bias by weekday.

## What this check establishes

The script verifies this small example. It does not execute every imported notebook or prove production readiness. Historical exercises may need their own datasets/framework versions; use the collection indices for those materials.

## Recorded check

Executed on 2026-10-30 with Python 3.10. All embedded assertions passed. Small floating-point formatting differences are possible on other versions.

```text
One-step rolling-origin MAE: {'naive': 1.678, 'seasonal': 0.35} smoothed level: 11.0
```

# Python expense-ledger capstone

[Practicals](../README.md) · [Theory](../../01-theory/README.md) · [Questions](../../03-questions-and-answers/worked-questions.md)

## Run and inspect

Run `python3 lab.py` from this folder with Python 3.10 or later. The lab uses the standard library and local/synthetic data; no account, API key or package installation is needed. It contains assertions for its worked arithmetic and failure cases.

1. Read the script and predict its results.
2. Run it and explain each assertion.
3. Change one assumption and predict what should change.
4. Reproduce the result from a clean process.

[Open the complete script](lab.py).

## Extend the exercise

Add edit/delete operations while preserving unique IDs and integer monetary units. Add file persistence in a temporary test directory, then test invalid JSON and duplicate records. Explain ownership and failure semantics rather than suppressing errors.

## What this check establishes

The script verifies this small example. It does not execute every imported notebook or prove production readiness. Historical exercises may need their own datasets/framework versions; use the collection indices for those materials.

## Recorded check

Executed on 2026-10-30 with Python 3.10. All embedded assertions passed. Small floating-point formatting differences are possible on other versions.

```text
Category totals in paise: {'food': 1500, 'travel': 800} overall: 2300
```

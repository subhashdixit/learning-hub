# Questions and worked answers

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Try an answer aloud before opening the explanation. Use the theory chapter for the full derivation; the answers here focus on the reasoning.

## 1. What does RAG change?

<details><summary>Answer</summary>

It supplies retrieved evidence at inference; it does not itself retrain the underlying model.

</details>

## 2. How do you separate retrieval and answer failures?

<details><summary>Answer</summary>

First check whether relevant evidence was retrieved, then whether the answer uses it correctly. Measure both stages.

</details>

## 3. Why bound agent retries?

<details><summary>Answer</summary>

Unbounded loops waste resources and can repeat side effects. Retry transient problems with idempotency controls where needed.

</details>

## 4. Does valid JSON prove an answer correct?

<details><summary>Answer</summary>

No. Schema checks validate structure, not factual values or groundedness.

</details>

## 5. Workflow or agent?

<details><summary>Answer</summary>

Prefer a workflow for a known sequence; add dynamic decisions where they improve measured task completion.

</details>

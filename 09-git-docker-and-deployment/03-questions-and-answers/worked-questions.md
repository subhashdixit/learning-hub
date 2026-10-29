# Questions and worked answers

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Try an answer aloud before opening the explanation. Use the theory chapter for the full derivation; the answers here focus on the reasoning.

## 1. Image or container?

<details><summary>Answer</summary>

An image is the packaged source/environment/configuration; a container is a running instance.

</details>

## 2. Why inspect the staged diff?

<details><summary>Answer</summary>

It shows exactly what the next commit will record, which can differ from the working tree.

</details>

## 3. Does a successful container build prove a model endpoint works?

<details><summary>Answer</summary>

No. Exercise the running entry point with valid, invalid and representative requests.

</details>

## 4. What should be versioned with a model?

<details><summary>Answer</summary>

Code, configuration, preprocessing definition, dependency setup and the relevant data/model identifiers.

</details>

## 5. Why keep a rollback?

<details><summary>Answer</summary>

A new release may pass development checks yet fail under real traffic or data. Recovery should be deliberate and quick.

</details>

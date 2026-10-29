# Questions and worked answers

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Try an answer aloud before opening the explanation. Use the theory chapter for the full derivation; the answers here focus on the reasoning.

## 1. Does backpropagation update weights?

<details><summary>Answer</summary>

It calculates derivatives. The optimizer uses those derivatives to make an update.

</details>

## 2. Why are hidden activations needed?

<details><summary>Answer</summary>

Composed affine layers alone remain affine. Nonlinear activations allow a network to represent more complex relationships.

</details>

## 3. Does sparse cross-entropy keep only the argmax probability?

<details><summary>Answer</summary>

No. Sparse refers to integer target labels; the loss still uses the predicted probability assigned to the correct class.

</details>

## 4. How many updates are in one epoch with 1,000 rows and batch size 100?

<details><summary>Answer</summary>

Ten when the dataset is divided into ten full batches. Epoch and update are different units.

</details>

## 5. Which standard LSTM gates use sigmoid?

<details><summary>Answer</summary>

Forget, input and output gates. Tanh proposes candidate content and transforms cell content for the hidden state.

</details>

## 6. Does a 3×3 RGB filter have nine weights?

<details><summary>Answer</summary>

It has 27 weights because it spans three input channels, plus an optional bias for its output channel.

</details>

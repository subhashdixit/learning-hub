# Deep Learning and NLP — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Tensors, batches, layers and output contracts](#lesson-01)
- [02 — Backpropagation, initialization, optimizers and regularization](#lesson-02)
- [03 — Convolution, pooling, residual networks and transfer learning](#lesson-03)
- [04 — Text cleaning, tokenization, counts, TF–IDF and embeddings](#lesson-04)
- [05 — RNNs, LSTMs, GRUs and sequence learning](#lesson-05)
- [06 — Attention, positional information and transformers](#lesson-06)
- [07 — Autoencoders, VAEs, GANs, diffusion and language-model training](#lesson-07)

<a id="lesson-01"></a>

## 01 — Tensors, batches, layers and output contracts

[Read the lesson](../01-theory/lesson-01-tensors-and-shapes.md)

### Q001. Why record axis meanings?

<details>
<summary>Answer</summary>

Two arrays can have compatible sizes but represent different units, leading to silently wrong operations.

</details>

### Q002. Why nonlinear activations?

<details>
<summary>Answer</summary>

A chain of affine layers without nonlinearities is still one affine transformation.

</details>

### Q003. Multiclass versus multilabel output?

<details>
<summary>Answer</summary>

Exclusive classes commonly use one softmax distribution; simultaneous labels commonly use independent sigmoid outputs.

</details>

<a id="lesson-02"></a>

## 02 — Backpropagation, initialization, optimizers and regularization

[Read the lesson](../01-theory/lesson-02-backprop-and-training.md)

### Q004. Does backprop update parameters?

<details>
<summary>Answer</summary>

It computes gradients; an optimizer update changes parameters.

</details>

### Q005. Why reset gradients?

<details>
<summary>Answer</summary>

Frameworks often accumulate them, which is useful deliberately but wrong when unintended.

</details>

### Q006. Why evaluation mode?

<details>
<summary>Answer</summary>

Layers such as dropout and batch normalization need their defined inference behaviour.

</details>

<a id="lesson-03"></a>

## 03 — Convolution, pooling, residual networks and transfer learning

[Read the lesson](../01-theory/lesson-03-convolution-and-vision.md)

### Q007. Why weight sharing?

<details>
<summary>Answer</summary>

The same local pattern detector can be used across image locations with fewer parameters.

</details>

### Q008. What is a residual connection?

<details>
<summary>Answer</summary>

A shortcut adds an identity or projected input to a transformed path.

</details>

### Q009. Why audit augmentations?

<details>
<summary>Answer</summary>

An augmentation can change the true label or introduce unrealistic data.

</details>

<a id="lesson-04"></a>

## 04 — Text cleaning, tokenization, counts, TF–IDF and embeddings

[Read the lesson](../01-theory/lesson-04-text-representations.md)

### Q010. Why not always remove stop words?

<details>
<summary>Answer</summary>

Some words, including negation, carry task-critical meaning.

</details>

### Q011. Static versus contextual embeddings?

<details>
<summary>Answer</summary>

Static vectors are fixed per token; contextual representations depend on the input context.

</details>

### Q012. Does high semantic similarity prove a correct answer?

<details>
<summary>Answer</summary>

No. Similarity measures representation proximity, not truth or evidence support.

</details>

<a id="lesson-05"></a>

## 05 — RNNs, LSTMs, GRUs and sequence learning

[Read the lesson](../01-theory/lesson-05-recurrent-sequences.md)

### Q013. Why do gates help?

<details>
<summary>Answer</summary>

They learn controlled information retention/update paths rather than overwriting state indiscriminately.

</details>

### Q014. Can a bidirectional model forecast using future observations?

<details>
<summary>Answer</summary>

That would violate causal prediction-time availability unless those observations truly exist.

</details>

### Q015. What is teacher forcing?

<details>
<summary>Answer</summary>

Use known previous target tokens as training inputs, unlike generation using its own past predictions.

</details>

<a id="lesson-06"></a>

## 06 — Attention, positional information and transformers

[Read the lesson](../01-theory/lesson-06-attention-and-transformers.md)

### Q016. Why divide by sqrt(dk)?

<details>
<summary>Answer</summary>

To control dot-product scale as key dimensionality grows, improving softmax behaviour under the usual initialization reasoning.

</details>

### Q017. What does a causal mask prevent?

<details>
<summary>Answer</summary>

A prediction position attending to unavailable future positions.

</details>

### Q018. Do attention weights prove causal importance?

<details>
<summary>Answer</summary>

No. They are internal weights within a larger computation, not automatic intervention effects.

</details>

<a id="lesson-07"></a>

## 07 — Autoencoders, VAEs, GANs, diffusion and language-model training

[Read the lesson](../01-theory/lesson-07-generative-models-and-evaluation.md)

### Q019. VAE versus ordinary autoencoder?

<details>
<summary>Answer</summary>

A VAE models a probabilistic latent distribution with a prior-related regularization term rather than only deterministic reconstruction.

</details>

### Q020. What is GAN mode collapse?

<details>
<summary>Answer</summary>

The generator produces too little variety despite appearing plausible for a subset of outputs.

</details>

### Q021. Why task-specific evaluation?

<details>
<summary>Answer</summary>

Different generation systems can fail in ways a generic similarity or likelihood score does not measure.

</details>

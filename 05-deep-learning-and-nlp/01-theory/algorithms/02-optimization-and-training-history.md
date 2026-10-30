# 02 — SGD, momentum, adaptive optimizers, normalization and transfer

[Algorithm story](../ALGORITHM-STORY.md) · [Algorithm index](README.md) · [Practicals](../../02-practicals/README.md)

```mermaid
flowchart LR
 N0["Architecture and loss"] --> N1["Initialization and normalization"] --> N2["Gradient estimate"] --> N3["Optimizer and schedule"] --> N4["Validation checkpoint"]
```

## On this page

- [1. Why this branch exists](#1-why-this-branch-exists)
- [2. How it works and learns](#2-how-it-works-and-learns)
- [3. Calculate a small example](#3-calculate-a-small-example)
- [4. Advantages, limitations and related alternatives](#4-advantages-limitations-and-related-alternatives)
- [5. How to choose and validate it](#5-how-to-choose-and-validate-it)

## 1. Why this branch exists

A representable function can still be hard to train. Optimization, initialization and regularization methods target loss geometry/generalization, while transfer/adaptation changes how prior learned knowledge is reused.

## 2. How it works and learns

SGD uses sampled gradients. Momentum averages/update directions to reduce selected oscillations. AdaGrad accumulates squared gradients, useful in some sparse settings but can shrink steps too far; RMSProp uses a moving second-moment estimate; Adam combines first/second moment estimates with correction conventions. AdamW separates a weight-decay operation from the adaptive gradient update under its defined algorithm. No optimizer guarantees generalization or eliminates learning-rate selection.

Initialization such as Xavier/He-style scaling aims to preserve signal scales under assumptions about layers/activations. Batch normalization and layer normalization use different axes/statistics and training/inference behaviour. Dropout changes training activations; early stopping selects a development checkpoint; residual connections alter architecture/gradient paths. They address different problems and can interact.

Transfer can freeze a representation, fine-tune all weights or use parameter-efficient adapters. Distillation and quantization target other cost/deployment constraints. Catastrophic forgetting, domain mismatch and weak evaluation can turn seemingly successful adaptation into regression.

## 3. Calculate a small example

On $J(w)=(w-3)^2$, w=0 and step.1 give w=.6. On a differently scaled coordinate with curvature 100 times larger, the same step may diverge. An optimizer name does not replace scaling/rate/convergence checks.

A model with dropout accidentally left in training mode can produce inconsistent inference outputs. A batch-normalized model needs its correct evaluation behaviour and compatible learned statistics.

## 4. Advantages, limitations and related alternatives

New training recipes may improve speed/stability under a workload but can trade memory, numerical behaviour and sensitivity. A smaller validation loss during tuning is not independent test evidence. More epochs or a different optimizer cannot repair target leakage or invalid labels.

## 5. How to choose and validate it

Record loss convention, batch/update counts, schedule, precision, initialization, seeds and validation protocol. Compare actual compute and held-out performance. Monitor gradients and convergence warnings; do not blindly increase architecture size to solve a data-quality problem.

---

[← From a perceptron to multilayer networks](01-perceptron-to-mlp.md) · [LeNet, AlexNet, VGG and Inception: learning local visual structure →](03-cnn-family.md)

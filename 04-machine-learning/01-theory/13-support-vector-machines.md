# 13 — SVM, kernels and support vector regression

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions and answers](../03-questions-and-answers/worked-questions.md#lesson-13)

```mermaid
flowchart LR
 Scaled_inputs["Scaled inputs"] --> Kernel_similarity["Kernel similarity"] --> Margin_objective["Margin objective"] --> Support_vectors["Support vectors"] --> Score["Score"]
```

## On this page

- [Find a boundary with room around it](#find-a-boundary-with-room-around-it)
- [A kernel compares transformed features without writing them out](#a-kernel-compares-transformed-features-without-writing-them-out)
- [Regression version](#regression-version)

## Find a boundary with room around it

For labels $y_i\in\{-1,1\}$, a linear SVM chooses a large-margin separator. A common soft-margin objective is $\frac12\|w\|^2+C\sum_i\max(0,1-y_i(w^Tx_i+b))$. The geometric margin between the two supporting hyperplanes is $2/\|w\|$. The hinge loss is zero when an observation is on the correct side with sufficient margin. Support vectors are the examples that determine the solution through nonzero dual coefficients.

![Margin, support vectors and a nonlinear kernel boundary](assets/svm-margin.png)

If $w=(2,0),b=-4$, the boundary is $x_1=2$, the two margin lines are $x_1=1.5,2.5$, and their separation is 1. For a positive example $x_1=2.2$, score 0.4 gives hinge loss 0.6. It is correctly classified but still inside the desired margin. Larger $C$ penalizes violations more, permitting a tighter fit; it is not the same direction as a ridge penalty $\lambda$.

## A kernel compares transformed features without writing them out

A kernel represents $K(x,z)=\phi(x)^T\phi(z)$. Linear kernels are efficient for high-dimensional sparse problems. Polynomial kernels model feature interactions; RBF uses $\exp(-\gamma\|x-z\|^2)$ and creates flexible local similarity. Large $\gamma$ makes each example's influence more local and can overfit; small $\gamma$ gives smoother variation. Standardize inputs before tuning $C$ and $\gamma$ jointly.

The nonlinear prediction is $f(x)=\sum_i\alpha_i y_iK(x_i,x)+b$. This is not an explicit guarantee of calibrated probabilities. Probability estimates require a further fitting/calibration procedure and appropriate evaluation.

## Regression version

SVR uses an $\epsilon$-insensitive tube: errors inside the tube incur no residual penalty; outside, the loss is $\max(0,|y-f(x)|-\epsilon)$. It combines this with a coefficient norm penalty. For actual 10, prediction 10.3 and $\epsilon=0.5$, loss is 0; prediction 11 gives loss 0.5. Kernel methods apply to SVR too. Tune $C$, $\epsilon$, kernel and scale together; target units directly affect a sensible $\epsilon$.

| Prefer | Why | Watch out |
|---|---|---|
| Linear SVM for many sparse text features | Efficient margin-based baseline | Scores are not probabilities |
| RBF SVM on moderate-size scaled data | Flexible nonlinear boundaries | Kernel matrix and search can be expensive |
| SVR for nonlinear numeric prediction | Controlled tolerance tube | Scaling, target units and extrapolation |

Hard-margin SVM requires separability and is brittle to violations. Soft margins permit errors and are normally more practical. Large nonlinear SVM datasets can require substantial memory/time; kernel approximations or linear stochastic solvers may be better. Compare with logistic regression if calibrated probabilities are central, and with boosted trees for heterogeneous tabular interactions.

---

[← 12: K-nearest neighbours and distance](12-nearest-neighbours.md) · [14: Decision trees: entropy, Gini, regression and pruning →](14-decision-trees.md)

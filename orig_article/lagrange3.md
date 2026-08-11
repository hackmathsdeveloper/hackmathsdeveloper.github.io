L2 **weight decay** and ridge regression are the penalized form of a constrained optimization problem. The regularization coefficient is interpretable as a Lagrange multiplier: it sets the trade-off between fitting data and keeping the weight vector within an L2-norm budget. [cs.mcgill](https://www.cs.mcgill.ca/~dprecup/courses/ML/Lectures/ml-lecture03.pdf)

## Primal: ridge regression

For design matrix \(X\in\mathbb R^{n\times d}\), targets \(y\in\mathbb R^n\), and weights \(w\in\mathbb R^d\), ridge regression solves

\[
\min_w
\frac{1}{2}\|Xw-y\|_2^2
+
\frac{\lambda}{2}\|w\|_2^2,
\qquad \lambda>0.
\]

Setting its gradient to zero gives

\[
X^\top(Xw-y)+\lambda w=0,
\]

so

\[
\boxed{
w^\star=(X^\top X+\lambda I)^{-1}X^\top y
}.
\]

Unlike ordinary least squares, the \(\lambda I\) term makes the system better-conditioned when features are correlated or \(X^\top X\) is singular. Increasing \(\lambda\) shrinks weights toward zero; as \(\lambda\to\infty\), \(w^\star\to0\). [cs.mcgill](https://www.cs.mcgill.ca/~dprecup/courses/ML/Lectures/ml-lecture03.pdf)

## Where the multiplier comes from

Start with a hard capacity constraint instead:

\[
\min_w \frac{1}{2}\|Xw-y\|_2^2
\quad\text{subject to}\quad
\|w\|_2^2\le t.
\]

Its Lagrangian is

\[
\mathcal L(w,\lambda)
=
\frac{1}{2}\|Xw-y\|_2^2
+
\frac{\lambda}{2}(\|w\|_2^2-t),
\qquad \lambda\ge0.
\]

For a fixed \(\lambda\), the constant \(-\lambda t/2\) does not affect the minimizing \(w\). What remains is exactly ridge:

\[
\min_w
\frac{1}{2}\|Xw-y\|_2^2
+
\frac{\lambda}{2}\|w\|_2^2.
\]

Thus, under standard convexity/constraint-qualification conditions, each active norm budget \(t\) corresponds to a \(\lambda\), and both formulations produce the same solution. If the budget is loose, the constraint is inactive and KKT complementary slackness gives \(\lambda=0\): ordinary least squares is recovered. [cs.mcgill](https://www.cs.mcgill.ca/~dprecup/courses/ML/Lectures/ml-lecture03.pdf)

## Dual: sample-space formulation

To derive a convenient dual, introduce residuals \(r=Xw-y\):

\[
\min_{w,r}
\frac12\|r\|_2^2+\frac{\lambda}{2}\|w\|_2^2
\quad \text{s.t.}\quad
r=Xw-y.
\]

Attach dual variable \(\alpha\in\mathbb R^n\):

\[
\mathcal L(w,r,\alpha)
=
\frac12\|r\|_2^2
+\frac{\lambda}{2}\|w\|_2^2
+\alpha^\top(r-Xw+y).
\]

Stationarity gives

\[
r=-\alpha,
\qquad
\lambda w=X^\top\alpha,
\qquad
w=\frac1\lambda X^\top\alpha.
\]

Substitute those into \(\mathcal L\). The dual maximization is

\[
\boxed{
\max_\alpha
\left[
y^\top\alpha
-\frac12\|\alpha\|_2^2
-\frac{1}{2\lambda}\alpha^\top XX^\top\alpha
\right].
}
\]

Equivalently, letting \(K=XX^\top\),

\[
\boxed{
(K+\lambda I)\alpha=\lambda y,
\qquad
w^\star=X(K+\lambda I)^{-1}y.
}
\]

The dual works in \(n\)-dimensional **sample space** rather than \(d\)-dimensional feature/parameter space. It is especially useful when \(d\gg n\), and it exposes the kernelized solution: replace \(XX^\top\) by a valid kernel Gram matrix \(K_{ij}=k(x_i,x_j)\). [jack.valmadre](https://jack.valmadre.net/notes/2014/09/03/ridge-regression-dual/)

## Neural-network weight decay

For a neural network \(f_\theta\), L2-regularized training is

\[
\min_\theta
\mathcal L_{\text{data}}(\theta)
+
\frac{\lambda}{2}\|\theta\|_2^2.
\]

The gradient is

\[
\nabla_\theta \mathcal L_{\text{data}}(\theta)+\lambda\theta.
\]

With SGD learning rate \(\eta\),

\[
\theta_{t+1}
=
\theta_t-\eta\nabla_\theta\mathcal L_{\text{data}}(\theta_t)-\eta\lambda\theta_t
=
(1-\eta\lambda)\theta_t
-\eta\nabla_\theta\mathcal L_{\text{data}}(\theta_t).
\]

That multiplicative \(1-\eta\lambda\) shrinkage motivates the name **weight decay**. Penalizing squared parameter magnitudes is also used in neural networks, though the exact equivalence between “L2 regularization” and optimizer-level decoupled weight decay depends on the optimizer. [profs.sci.univr](http://profs.sci.univr.it/~castellini/docs/statsLearning19-20/SL2019-20_3_Shrinkage.pdf)

## Important distinction: duality vs weight decay

There are two related but distinct roles for the term “Lagrangian”:

| Concept | Role |
|---|---|
| **Lagrange multiplier \(\lambda\)** | Converts a hard norm budget, \(\|w\|^2\le t\), into a soft L2 penalty. It is a hyperparameter in ordinary ridge/weight-decay training, or an optimized dual variable if the norm constraint is enforced explicitly. |
| **Dual variables \(\alpha_i\)** | One variable per training residual/equality constraint in the ridge dual. They express the solution as a combination of training examples. |
| **Weight decay** | The resulting L2 penalty or, in SGD, the parameter-shrinking update rule. |
| **Kernel ridge regression** | Ridge solved in the dual, with \(XX^\top\) generalized to a kernel Gram matrix; it enables nonlinear functions without explicitly constructing the feature map.  [jack.valmadre](https://jack.valmadre.net/notes/2014/09/03/ridge-regression-dual/) |

A concise mental model: **the primal optimizes weights directly; the dual optimizes sample coefficients; the Lagrange multiplier prices the permitted model complexity.**


References:

1. https://www.cs.mcgill.ca/~dprecup/courses/ML/Lectures/ml-lecture03.pdf
2. http://profs.sci.univr.it/~castellini/docs/statsLearning19-20/SL2019-20_3_Shrinkage.pdf
3. https://stats.stackexchange.com/questions/92672/difference-between-primal-dual-and-kernel-ridge-regression
4. https://jack.valmadre.net/notes/2014/09/03/ridge-regression-dual/
5. https://www.kudosai.com/Blog/L2-Regularization-Ridge-Weight-Decay-A-Detailed-Gentle-Guide
6. https://teazrq.github.io/SMLR/kernel-ridge-regression.html
7. https://www.math.ntnu.no/emner/TMA4180/2023v/notes/Duality.pdf
8. https://blog.csdn.net/zhaijianfengrui/article/details/127965485
9. https://davidrosenberg.github.io/mlcourse/Archive/2017/Homework/hw4.pdf
10. https://www.slideshare.net/slideshow/machinelearningpresentation-70605402/70605402

---
title: "Sylvester's Law of Inertia: Why Every Quadratic Form Is Just Pluses, Minuses, and Zeros — And Nothing Else"
date: 2026-06-08
categories:
  - Algebra
  - Mathematics
tags:
  - sylvesters-law
  - inertia
  - quadratic-forms
  - eigenvalues
  - matrix-congruence
  - signature
  - diagonalization
share: true
read_time: true
excerpt: "Any real quadratic form can be diagonalized into a sum of squares with coefficients 1, -1, or 0. Sylvester's law of inertia says the counts of each — called the inertia triple — are invariant: no matter how you diagonalize, you get the same numbers. This is the fundamental classification theorem for real quadratic forms."
---

**Challenge to the reader:** Consider the quadratic form $Q(x,y) = 4x^2 + 4xy + y^2$. Write its symmetric matrix, find its eigenvalues, and determine the inertia triple $(p, q, r)$. Then find an explicit change of variables that diagonalizes it to $y_1^2$ (with no $y_2^2$ term).

---

## 1. Precise Statement of Sylvester's Law

Let $Q: \mathbb{R}^n \to \mathbb{R}$ be a real quadratic form, represented by a real symmetric matrix $A$ so that $Q(x) = x^{\mathsf{T}} A x$.

Then there exists an invertible real matrix $S$ such that, in new coordinates $y = Sx$, we have:

$$
Q(x) = Q(S^{-1}y) = \sum_{i=1}^n b_i y_i^2,
$$

where each $b_i \in \{1, -1, 0\}$.

Let:
- $p = \lvert\lbrace i : b_i = 1\rbrace\rvert$,
- $q = \lvert\lbrace i : b_i = -1\rbrace\rvert$,
- $r = \lvert\lbrace i : b_i = 0\rbrace\rvert$.

**Sylvester's law of inertia** says that the triple $(p, q, r)$ is uniquely determined by $Q$ and does not depend on which invertible change of variables $S$ you use.

Equivalently:
- $p$ = number of positive eigenvalues of $A$,
- $q$ = number of negative eigenvalues,
- $r$ = number of zero eigenvalues,

counted with multiplicity. The triple $(p,q,r)$ is called the **inertia** of $A$ or of $Q$.

---

## 2. Rank, Signature, and Invariants

From the inertia $(p, q, r)$ you get two classic invariants:

- **Rank:** $\operatorname{rank}(Q) = p + q$.
- **Signature:** $\operatorname{sig}(Q) = p - q$.

Sylvester's law can be restated as: for real quadratic forms, the rank and signature (equivalently the inertia triple) are invariant under real congruence $A \mapsto S^{\mathsf{T}} A S$ with $S$ invertible.

For a nondegenerate real quadratic form (i.e., $r = 0$), you can choose a basis such that $Q$ is a sum of $p$ positive and $q$ negative squares, with no zero coefficients; in this case the inertia is just $(p, q, 0)$.

---

## 3. Worked Example

Consider:

$$
Q(x,y) = 4x^2 + 4xy + y^2.
$$

The associated matrix is:

$$
A = \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}.
$$

This is symmetric and has eigenvalues $0$ and $5$, so its inertia is $(1, 0, 1)$: one positive eigenvalue, no negative eigenvalues, one zero eigenvalue.

Sylvester's law says that by a suitable invertible linear change of variables, you can rewrite $Q$ as:

$$
Q(x,y) = y_1^2 + 0 \cdot y_2^2
$$

(and every other diagonalization will have exactly one $+1$, no $-1$, and one $0$).

**Challenge to the reader:** Find an explicit invertible matrix $S$ such that the change of variables $(u, v)^{\mathsf{T}} = S (x, y)^{\mathsf{T}}$ transforms $4x^2 + 4xy + y^2$ into $u^2$. Verify that $\det S \neq 0$, so the transformation is genuinely invertible.

---

## 4. Why "Inertia"?

The name *inertia* comes from physics — just as mass resists change in velocity, the inertia triple resists change under coordinate transformations. No matter how you stretch, rotate, or shear the coordinate axes (invertibly), the numbers of positive, negative, and zero squares are fixed.

This is surprising because eigenvalues themselves are **not** invariant under congruence — only their signs are. For example:

$$
A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix}
$$

have different eigenvalues ($\{1,1\}$ vs $\{2, \frac{1}{2}\}$) but the same inertia $(2, 0, 0)$, and indeed they are congruent (take $S = \operatorname{diag}(\sqrt{2}, 1/\sqrt{2})$).

---

## 5. Consequences

Sylvester's law has far-reaching consequences:

1. **Critical point classification:** The Hessian of a function at a critical point is a quadratic form. Its inertia classifies minima ($p=n$), maxima ($q=n$), and various types of saddle points.

2. **Special relativity:** The Minkowski metric $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$ is a quadratic form of inertia $(3,1,0)$ (or $(1,3,0)$ depending on convention). No coordinate change can turn time into a spacelike dimension — the signature is invariant.

3. **Quadratic programming:** The inertia of the Hessian determines whether an optimization problem is convex (all positive), concave (all negative), or indefinite (mixed — and much harder).

---

## 6. Deeper Significance

Sylvester's law is a rigidity theorem: it tells you that while you have enormous freedom to change coordinates, some things are forced. The numbers of positive, negative, and zero directions are intrinsic to the quadratic form itself, independent of how you describe it.

This foreshadows deeper classification theorems: the classification of real inner product spaces by signature, the classification of symmetric bilinear forms over finite fields by dimension and discriminant, and ultimately the Hasse-Minkowski theorem, which completely classifies quadratic forms over number fields via local invariants at each prime.

**Final challenge:** Over a finite field $\mathbb{F}_p$ (with $p$ odd), two nondegenerate quadratic forms are equivalent if and only if they have the same dimension and discriminant (modulo squares). Prove that this means there are exactly two inequivalent nondegenerate quadratic forms of each dimension $n \ge 1$ over $\mathbb{F}_p$. How does this contrast with Sylvester's law over $\mathbb{R}$, where there are $n+1$ possibilities?

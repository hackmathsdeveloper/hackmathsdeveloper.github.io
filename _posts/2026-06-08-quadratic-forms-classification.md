---
title: "Every Quadratic Form Is Secretly Just Squares — The Classification That Unifies Them All"
date: 2026-06-08
categories:
  - Algebra
  - Mathematics
tags:
  - quadratic-forms
  - sylvester-inertia
  - matrix-representation
  - bilinear-forms
  - number-theory
  - linear-algebra
  - equivalence-classes
share: true
read_time: true
excerpt: "A quadratic form is any homogeneous degree-2 polynomial in n variables. Over ℝ, every single one diagonalizes to a sum of squares with +1, −1, or 0 coefficients — and the counts of each are invariant. Over ℚ or ℤ, the classification explodes into a rich arithmetic landscape."
---

**Challenge to the reader:** Write down a random symmetric $3 \times 3$ matrix with integer entries. Compute its eigenvalues. Based on the signs, determine the inertia triple $(p, q, r)$ — the numbers of positive, negative, and zero eigenvalues. This triple is the invariant that classifies your form up to real equivalence.

---

## 1. General Definition

A (real) quadratic form in $n$ variables is a map:

$$
Q: \mathbb{R}^n \to \mathbb{R}, \qquad Q(x) = \sum_{i,j} a_{ij} x_i x_j,
$$

with $a_{ij} = a_{ji}$. Equivalently, choose a symmetric matrix $A \in M_n(\mathbb{R})$ and write:

$$
Q(x) = x^{\mathsf{T}} A x.
$$

Over a given field, every choice of symmetric matrix $A$ gives a quadratic form, and different $A$ can give equivalent forms up to change of basis (congruence).

---

## 2. Canonical Small-Dimensional Examples

For 1–2 variables, you can see the variety of behavior explicitly:

- $Q(x) = ax^2$ in 1 variable (any $a \in \mathbb{R}$).
- $Q(x,y) = x^2 + y^2$ (positive definite).
- $Q(x,y) = -x^2 - y^2$ (negative definite).
- $Q(x,y) = x^2 - y^2$ (indefinite).
- $Q(x,y) = (x-y)^2$ (positive semidefinite).
- More generally $Q(x,y) = ax^2 + 2bxy + cy^2$ with arbitrary $a,b,c \in \mathbb{R}$.

Every 2-variable quadratic form over $\mathbb{R}$ is equivalent, via an invertible linear change of variables, to one of:

$$
\lambda_1 u^2 + \lambda_2 v^2, \qquad \text{with } \lambda_i \in \mathbb{R}.
$$

---

## 3. Matrix Representation and Higher Dimensions

In $n$ variables with symmetric $A$, diagonalization yields an orthogonal change of basis $x = P y$ such that:

$$
Q(x) = y^{\mathsf{T}} D y = \sum_{i=1}^n \lambda_i y_i^2,
$$

where $\lambda_i$ are eigenvalues of $A$. So, up to orthogonal equivalence, examples in $\mathbb{R}^n$ reduce to sums of squares with coefficients:

- **Positive definite:** all $\lambda_i \gt 0$, e.g. $x_1^2 + \cdots + x_n^2$.
- **Negative definite:** all $\lambda_i \lt 0$, e.g. $-x_1^2 - \cdots - x_n^2$.
- **Indefinite:** a mix of positive and negative coefficients, e.g. $x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2$.
- **Semidefinite:** some $\lambda_i = 0$, e.g. $x_1^2 + x_2^2$ in $\mathbb{R}^3$ ignoring $x_3$.

**Challenge to the reader:** Take the quadratic form $Q(x,y,z) = 2x^2 + 2y^2 + 2z^2 - 2xy - 2yz - 2zx$. Find an orthogonal change of variables that diagonalizes it, and determine its inertia triple.

---

## 4. Sylvester's Law of Inertia (Real Case)

Over $\mathbb{R}$, **Sylvester's law of inertia** says any real quadratic form is equivalent to:

$$
x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2
$$

with $p + q \le n$. The triple $(p, q, n-p-q)$ — the numbers of positive, negative, and zero directions — is an invariant. Thus, up to linear change of coordinates, **all real quadratic forms are exhausted by these normal forms**.

Equivalently:
- $p$ = number of positive eigenvalues of $A$,
- $q$ = number of negative eigenvalues,
- $r = n-p-q$ = number of zero eigenvalues,

counted with multiplicity. The triple $(p,q,r)$ is called the **inertia** of $A$ or of $Q$.

From the inertia you get two classic invariants:
- **Rank:** $\operatorname{rank}(Q) = p + q$.
- **Signature:** $\operatorname{sig}(Q) = p - q$.

---

## 5. Arithmetic Examples Over ℚ or ℤ

Over $\mathbb{Q}$ or $\mathbb{Z}$, the landscape is richer because integrality and local-global phenomena matter.

Typical examples:

- **Binary:** $ax^2 + bxy + cy^2$ with $a,b,c \in \mathbb{Z}$ (binary quadratic forms).
- **Ternary:** $x^2 + y^2 + z^2$, $x^2 + y^2 - z^2$, etc.
- **Classical forms used in number theory:**
  - Sum of two squares: $x^2 + y^2$.
  - Sum of three squares: $x^2 + y^2 + z^2$.
  - Sum of four squares: $x_1^2 + x_2^2 + x_3^2 + x_4^2$.

Classification involves equivalence under $\operatorname{GL}_n(\mathbb{Z})$, discriminants, genus, and spinor genus, and is highly nontrivial for $n \ge 3$.

---

## 6. Why You Cannot "List All" Examples

- Each symmetric $n \times n$ matrix over a field corresponds to a quadratic form, and there are infinitely many such matrices for any $n \ge 1$.
- Even up to linear equivalence (congruence), there are infinitely many inequivalent forms over $\mathbb{Q}$ or $\mathbb{Z}$. For instance, binary quadratic forms $ax^2 + bxy + cy^2$ with varying discriminant $b^2 - 4ac$ already give infinitely many classes.

So what one typically does is:

- Fix dimension and base field.
- Classify quadratic forms **up to equivalence** by invariants (signature over $\mathbb{R}$, discriminant and Hasse invariants over number fields, etc.).

---

## 7. Deeper Significance

Quadratic forms are the second-order Taylor expansion of any smooth function at a critical point — the Hessian is a quadratic form. Sylvester's law classifies critical points into minima ($p = n$), maxima ($q = n$), and saddles (mixed). In physics, quadratic forms encode kinetic energy ($\frac{1}{2}mv^2$), elastic potentials, and the metric structure of spacetime itself ($ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$, a quadratic form of inertia $(1,3,0)$ or $(3,1,0)$ depending on convention).

In number theory, the representation of integers by quadratic forms ($x^2 + y^2 = n$ has how many solutions?) leads to class numbers, modular forms, and the deepest theorems of algebraic number theory.

**Final challenge:** Prove that two binary quadratic forms $ax^2 + bxy + cy^2$ and $a'x^2 + b'xy + c'y^2$ over $\mathbb{Z}$ are equivalent if and only if they have the same discriminant $b^2 - 4ac = b'^2 - 4a'c'$. Does this simple invariant suffice? (Hint: it doesn't — find a counterexample, then research the notion of the *class group*.)

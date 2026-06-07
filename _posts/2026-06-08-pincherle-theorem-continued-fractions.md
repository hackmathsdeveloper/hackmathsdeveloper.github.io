---
title: "Pincherle's Theorem: The One Tool That Unlocks Every Polynomial Continued Fraction"
date: 2026-06-08
categories:
  - Number Theory
  - Mathematics
tags:
  - continued-fractions
  - pincherle-theorem
  - recurrences
  - polynomial-continued-fractions
  - convergence
  - complex-analysis
share: true
read_time: true
excerpt: "Pincherle's theorem turns the evaluation of an infinite continued fraction into a simple initial-value problem: find any sequence satisfying the recurrence, check a growth condition, and the limit is the ratio of two initial terms."
---

**Challenge to the reader:** For a continued fraction $K_{n=1}^{\infty} a_n/b_n$, guess a sequence $G_n$ that satisfies $G_n = a_n G_{n-2} + b_n G_{n-1}$. If you succeed, the limit is $-G_0/G_{-1}$ — provided a growth condition holds. Try this on the case $a_n = n+1$, $b_n = n$ with the guess $G_n = (-1)^{n+1}$.

---

## 1. Pincherle's Theorem Statement

For a continued fraction:

$$
K_{n=1}^{\infty}\frac{a_n}{b_n},
$$

suppose we can find sequences $a_n$, $b_n$, and an auxiliary sequence $G_n$ (defined for $n \ge -1$) satisfying the three-term recurrence:

$$
\boxed{G_n = a_n G_{n-2} + b_n G_{n-1} \qquad (n \ge 1)}.
$$

Let $B_n$ be the denominator convergents of the continued fraction (computed via the standard recurrence $B_n = b_n B_{n-1} + a_n B_{n-2}$ with $B_{-1}=0, B_0=1$). If the growth condition:

$$
\frac{G_n}{B_n} \to 0
$$

holds, then Pincherle's theorem gives the limit:

$$
\boxed{K_{n=1}^{\infty}\frac{a_n}{b_n} = -\frac{G_0}{G_{-1}}.}
$$

The theorem packages the entire convergence question into a single identifiable object: the auxiliary sequence $G_n$. Once you have it, the limit is determined by just two initial values.

## 2. Example 1: The Constant $(-1)^{n+1}$ and Limit 1

Consider the family:

$$
K_{n=1}^{\infty}\frac{n^\alpha+1}{n^\alpha},
\qquad \alpha>0.
$$

Set:

$$
a_n = n^\alpha+1,\qquad b_n = n^\alpha,\qquad G_n = (-1)^{n+1}.
$$

Verify the recurrence:

$$
\begin{aligned}
a_n G_{n-2} + b_n G_{n-1}
&= (n^\alpha+1)(-1)^{n-1} + n^\alpha(-1)^n \\[4pt]
&= (-1)^{n-1}\big((n^\alpha+1) - n^\alpha\big) \\[4pt]
&= (-1)^{n-1} = (-1)^{n+1} = G_n.
\end{aligned}
$$

The recurrence holds exactly. Now evaluate the initial values:

$$
G_{-1} = (-1)^0 = 1,\qquad G_0 = (-1)^1 = -1.
$$

Since $B_n \to \infty$ for $\alpha>0$, the growth condition $G_n/B_n \to 0$ is satisfied (the numerator is bounded, the denominator diverges). Pincherle gives:

$$
K_{n=1}^{\infty}\frac{n^\alpha+1}{n^\alpha} = -\frac{G_0}{G_{-1}} = -\frac{-1}{1} = 1.
$$

With a single alternating sequence, an entire infinite family is evaluated.

---

**Challenge:** Verify that $G_n = (-1)^{n+1}$ also works for the family $K_{n=1}^{\infty} \frac{n^\alpha + k}{n^\alpha}$ for any constant $k$. What is the limit?

---

## 3. Example 2: The Quadratic Seed $(n+2)^2$ and Limit 4

Now consider a more elaborate family:

$$
K_{n=1}^{\infty}\frac{(n+1)^2 f_n + 4n + 5}{n^2 f_n + 4n - 4} = 4,
$$

where $f_n \ge 1$ is an arbitrary polynomial. The witness sequence is:

$$
G_n = (n+2)^2.
$$

The core recurrence uses:

$$
a_n = 4n+5,\qquad b_n = -4n+4.
$$

Verify:

$$
\begin{aligned}
a_n G_{n-2} + b_n G_{n-1}
&= (4n+5)n^2 + (-4n+4)(n+1)^2 \\[4pt]
&= (4n^3+5n^2) + (-4n+4)(n^2+2n+1) \\[4pt]
&= 4n^3+5n^2 -4n^3 -4n^2 + 4n + 4 \\[4pt]
&= n^2 + 4n + 4 = (n+2)^2 = G_n.
\end{aligned}
$$

The initial values are:

$$
G_{-1} = (-1+2)^2 = 1,\qquad G_0 = (0+2)^2 = 4.
$$

Hence:

$$
K_{n=1}^{\infty}\frac{(n+1)^2 f_n + 4n + 5}{n^2 f_n + 4n - 4} = \frac{G_0}{G_{-1}} = 4.
$$

The polynomial $f_n$ is completely free — pick $f_n = n^{10}$ or $f_n = 1$, the limit is always $4$. This is the remarkable flexibility of the construction: the continued fraction family is infinite-dimensional, yet every member shares the same limit.

## 4. Example 3: Complex Product Seed and Limit m

For a complex-valued example, take:

$$
K_{n=1}^{\infty}\frac{(m+n)^2-1}{1}=m,
$$

valid for complex $m$ with $m \neq -k$ ($k \in \mathbb{N}$). The auxiliary sequence is:

$$
G_{-1}=1,\qquad G_n = (-1)^{n+1}\prod_{i=0}^{n}(m+i),
$$

with $a_n = (m+n-1)(m+n+1)$ and $b_n = 1$.

Verify the recurrence:

$$
\begin{aligned}
a_n G_{n-2} + b_n G_{n-1}
&= (m+n-1)(m+n+1)(-1)^{n-1}\prod_{i=0}^{n-2}(m+i) \;+\; (-1)^n\prod_{i=0}^{n-1}(m+i) \\[4pt]
&= (-1)^{n-1}\prod_{i=0}^{n-2}(m+i)\Big((m+n-1)(m+n+1) - (m+n-1)\Big) \\[4pt]
&= (-1)^{n-1}\prod_{i=0}^{n-2}(m+i)\cdot (m+n-1)(m+n) \\[4pt]
&= (-1)^{n-1}\prod_{i=0}^{n}(m+i) = (-1)^{n+1}\prod_{i=0}^{n}(m+i) = G_n.
\end{aligned}
$$

The initial values are:

$$
G_0 = -m,\qquad G_{-1} = 1.
$$

Pincherle yields:

$$
K_{n=1}^{\infty}\frac{(m+n)^2-1}{1} = -\frac{G_0}{G_{-1}} = -(-m) = m.
$$

Set $m=i$ and you obtain a polynomial continued fraction with complex coefficients converging to $i$.

---

| Example | $G_n$ | $a_n$, $b_n$ | Limit |
|---|---|---|---|
| 1 | $(-1)^{n+1}$ | $n^\alpha+1$, $n^\alpha$ | $1$ |
| 2 | $(n+2)^2$ | $4n+5$, $-4n+4$ | $4$ |
| 3 | $(-1)^{n+1}\prod(m+i)$ | $(m+n)^2-1$, $1$ | $m$ |

---

## 5. The Rule of Thumb

The nature of $G_n$ determines the nature of the limit:

- **Constant or low-degree polynomial $G_n$** → rational limits (Examples 1 and 2).
- **Product-form or hypergeometric $G_n$** → special-function limits (Bessel, hypergeometric) or complex values (Example 3).
- **Exponential or factorial $G_n$** → transcendental limits.

The growth condition $G_n/B_n \to 0$ is usually satisfied when $\deg(G_n) < \deg(B_n)$ or when $G_n$ is bounded and $B_n \to \infty$.

## 6. Deeper Significance

Pincherle's theorem is more than a computational shortcut — it reveals the algebraic heart of continued fractions. The recurrence $G_n = a_n G_{n-2} + b_n G_{n-1}$ is a second-order linear recurrence, and the continued fraction is essentially the **minimal solution** (the solution of slowest growth) of that recurrence.

This connects continued fractions to:

- **Orthogonal polynomials** — the denominator polynomials $B_n$ are orthogonal with respect to a moment functional determined by the continued fraction.
- **Padé approximation** — convergents of continued fractions correspond to diagonal Padé approximants.
- **Spectral theory** — the recurrence is a discrete Schrödinger equation; the continued fraction encodes the spectral measure.

## 7. Final Challenge

**Synthesis challenge:** Choose a new seed $G_n = mn + k$ (linear in $n$) with $m, k$ constants. Solve for the linear polynomials $a_n = An + B$, $b_n = Cn + D$ such that the recurrence $a_n G_{n-2} + b_n G_{n-1} = G_n$ holds for all $n$.

1. Write down the system of equations for $A, B, C, D$ in terms of $m$ and $k$.
2. Verify that one solution is $G_n = n+1$ → limit $2$.
3. Build the corresponding continued fraction using Proposition 1 (with a free polynomial $f_n$) and confirm the limit.

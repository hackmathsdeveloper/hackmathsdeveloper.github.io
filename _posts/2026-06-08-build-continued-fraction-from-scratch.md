---
title: "Build Your Own Continued Fraction From Scratch — And Watch It Converge Exactly Where You Want"
date: 2026-06-08
categories:
  - Number Theory
  - Mathematics
tags:
  - continued-fractions
  - constructive-methods
  - recurrences
  - polynomial-continued-fractions
  - pincherle-theorem
share: true
read_time: true
excerpt: "You don't need to stumble upon a continued fraction — you can build one from scratch. Choose a seed polynomial, solve a linear system for the partial numerators and denominators, and Proposition 1 turns your solution into an infinite family of continued fractions with a prescribed limit."
---

**Challenge to the reader:** Choose a seed $G_n = n+3$. Solve for linear $a_n, b_n$ such that $a_n G_{n-2} + b_n G_{n-1} = G_n$. Then build a continued fraction whose limit is exactly $G_0/G_{-1} = 3/2$.

---

## 1. The Constructive Plan

In the previous post we saw Pincherle's theorem: if you *find* a sequence $G_n$ satisfying $G_n = a_n G_{n-2} + b_n G_{n-1}$, the continued fraction $K a_n/b_n$ evaluates to $-G_0/G_{-1}$. The constructive direction reverses the logic:

1. **Choose** an easy polynomial $G_n$.
2. **Solve** for simple polynomials $a_n, b_n$ that satisfy the recurrence.
3. **Apply** Proposition 1 to build an infinite family of continued fractions, all sharing the same limit $G_0/G_{-1}$, parameterized by a free polynomial $f_n$.

The result: you design continued fractions to converge to whatever limit you want.

## 2. Step 1: Choose a Seed

Pick the quadratic:

$$
G_n = (n+2)^2.
$$

Then:

$$
G_{n-2} = n^2,\qquad G_{n-1} = (n+1)^2,\qquad G_n = (n+2)^2.
$$

We seek linear polynomials:

$$
a_n = An + B,\qquad b_n = Cn + D
$$

such that the recurrence holds identically for all $n$:

$$
(An+B)\,G_{n-2} + (Cn+D)\,G_{n-1} = G_n.
$$

## 3. Step 2: Solve the Coefficient Matching

Substitute $G_{n-2} = n^2$ and $G_{n-1} = (n+1)^2$:

$$
(An+B)n^2 + (Cn+D)(n+1)^2 = (n+2)^2.
$$

Expand each term:

$$
\begin{aligned}
(An+B)n^2 &= An^3 + Bn^2, \\[4pt]
(Cn+D)(n+1)^2 &= (Cn+D)(n^2+2n+1) \\
&= Cn^3 + (2C+D)n^2 + (C+2D)n + D.
\end{aligned}
$$

Summing:

$$
(A+C)n^3 + (B+2C+D)n^2 + (C+2D)n + D = n^2 + 4n + 4.
$$

Match coefficients of $n^3, n^2, n, n^0$:

$$
\begin{aligned}
A + C &= 0 \\
B + 2C + D &= 1 \\
C + 2D &= 4 \\
D &= 4
\end{aligned}
$$

Solve from the bottom up: $D=4$ → $C = -4$ → $A = 4$ → $B + 2(-4) + 4 = 1$ → $B = 5$.

We have found:

$$
\boxed{a_n = 4n+5,\qquad b_n = -4n+4.}
$$

---

**Challenge:** Verify by direct substitution that $(4n+5)n^2 + (-4n+4)(n+1)^2$ simplifies to $(n+2)^2$ for all $n$.

---

## 4. Step 3: Build the Infinite Family

Proposition 1 says: given the core solution $(a_n, b_n, G_n)$, pick any polynomial $f_n \ge 1$ and define:

$$
s_n = f_n G_{n-1} + a_n,\qquad t_n = f_n G_{n-2} - b_n.
$$

Then:

$$
K_{n=1}^{\infty}\frac{s_n}{t_n} = \frac{G_0}{G_{-1}}.
$$

With $G_{n-1} = (n+1)^2$, $G_{n-2} = n^2$, and our $a_n, b_n$:

$$
s_n = (n+1)^2 f_n + 4n + 5,
$$
$$
t_n = n^2 f_n + 4n - 4.
$$

Therefore, **for any polynomial $f_n \ge 1$**:

$$
\boxed{K_{n=1}^{\infty}\frac{(n+1)^2 f_n + 4n + 5}{n^2 f_n + 4n - 4} = 4.}
$$

The limit is fixed at $4$ because:

$$
\frac{G_0}{G_{-1}} = \frac{(0+2)^2}{(-1+2)^2} = \frac{4}{1} = 4.
$$

## 5. A Concrete Instance

Choose $f_n = n^{10}$. Then:

$$
\begin{aligned}
s_n &= n^{10}(n+1)^2 + 4n + 5 = n^{12} + 2n^{11} + n^{10} + 4n + 5, \\[4pt]
t_n &= n^{12} + 4n - 4.
\end{aligned}
$$

The continued fraction:

$$
K_{n=1}^{\infty}\frac{n^{12} + 2n^{11} + n^{10} + 4n + 5}{n^{12} + 4n - 4} = 4.
$$

The first few partial quotients:

- $n=1$: $13/1$
- $n=2$: $9225/4104$
- $n=3$: $248066/531453$

Despite the messy-looking terms, the recurrence certificate $G_n = (n+2)^2$ guarantees the infinite limit is exactly $4$. That is the power of the constructive method — you know the answer *before* computing a single convergent.

---

| Step | Action | Example |
|---|---|---|
| 1 | Choose seed $G_n$ | $(n+2)^2$ |
| 2 | Solve for $a_n, b_n$ | $a_n = 4n+5$, $b_n = -4n+4$ |
| 3 | Pick free $f_n$ | $f_n = n^{10}$ |
| 4 | Build $s_n = f_n G_{n-1} + a_n$ | $n^{12} + 2n^{11} + n^{10} + 4n + 5$ |
| 5 | Build $t_n = f_n G_{n-2} - b_n$ | $n^{12} + 4n - 4$ |
| 6 | Limit | $\frac{G_0}{G_{-1}} = 4$ |

---

## 6. The Pattern to Reuse

This derivation is a template you can reuse with different seeds:

- **Linear seed** $G_n = mn + k$ → solve for constant $a_n, b_n$ → limit $k/(k-m)$.
- **Pure power** $G_n = n^k$ → polynomial $a_n, b_n$ of degree $k-2$ → limit determined by $0^k$ and $(-1)^k$.
- **Product seed** $G_n = \prod_{i=0}^{n}(m+i)$ → $a_n, b_n$ of controlled degree → limit $m$ (complex allowed).
- **Hypergeometric seed** → continued fractions encoding Bessel, $q$-series, and modular forms.

In every case, the work reduces to solving a linear system for the coefficients of $a_n$ and $b_n$, followed by a mechanical application of Proposition 1.

## 7. Deeper Significance

The constructive approach reveals something profound: **the set of polynomial continued fractions with a given limit is infinite-dimensional**. The free polynomial $f_n$ can be chosen arbitrarily — raising the degree, changing the coefficients, introducing oscillations — and the limit is unaffected. This is the algebraic analogue of the fact that many different series can sum to the same value.

From a research perspective, this means polynomial continued fractions are not scarce objects to be discovered; they are abundant objects to be *designed*. The design space is parameterized by the seed $G_n$ and the free polynomial $f_n$.

## 8. Final Challenge

**Synthesis challenge:** Start with a linear seed $G_n = n+3$.

1. Solve for constant $a_n$ and $b_n$ (degree 0 polynomials) such that $a_n G_{n-2} + b_n G_{n-1} = G_n$.
2. Compute $G_0/G_{-1}$ to find the limit.
3. Choose $f_n = n^2$ and write out the first three partial quotients of the resulting continued fraction.
4. Compute the first three convergents numerically and confirm they approach the predicted limit.

---
title: "How Euler Turned the Gregory-Leibniz Series Into a Continued Fraction — And Why Squares Appear"
date: 2026-06-08
categories:
  - Analysis
  - Mathematics
tags:
  - euler-transformation
  - gregory-leibniz-series
  - pi
  - continued-fractions
  - hypergeometric-functions
  - arctan
  - forward-differences
share: true
read_time: true
excerpt: "The Gregory-Leibniz series for π/4 has simple rational terms 1/(2n+1). Apply Euler's transformation, and these linear denominators reorganize into a continued fraction whose numerators are perfect squares — a surprising structural metamorphosis driven by forward differences."
---

**Challenge to the reader:** Write down the Gregory-Leibniz series for $\pi/4$ and compute the first three forward differences $\Delta a_0, \Delta^2 a_0, \Delta^3 a_0$ where $a_n = 1/(2n+1)$. Observe the pattern that emerges.

---

## 1. The Gregory-Leibniz Series

The classic alternating series for $\pi$ is deceptively simple:

$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots = \sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
$$

Each term is a rational function of $n$ with a linear denominator $2n+1$. This series converges — but painfully slowly. To get $\pi$ to 6 decimal places requires about a million terms.

Euler's transformation changes everything: it rewrites the series into a form that converges far faster, and — in a surprising structural twist — produces a continued fraction whose partial numerators are perfect squares $1^2, 2^2, 3^2, \dots$.

## 2. Euler's Transformation of Alternating Series

For an alternating series:

$$
S = \sum_{n=0}^{\infty} (-1)^n a_n,
$$

Euler's transformation states:

$$
S = \sum_{n=0}^{\infty} \frac{\Delta^n a_0}{2^{n+1}},
$$

where $\Delta$ is the forward difference operator:

$$
\Delta a_n = a_n - a_{n+1},
$$

and $\Delta^n$ denotes $n$-fold iteration.

For $a_n = \frac{1}{2n+1}$, we compute the successive differences at $n=0$.

## 3. Computing the Forward Differences

**First difference:**

$$
\begin{aligned}
\Delta a_n &= \frac{1}{2n+1} - \frac{1}{2n+3} = \frac{2}{(2n+1)(2n+3)}.
\end{aligned}
$$

At $n=0$:

$$
\Delta a_0 = \frac{2}{3}.
$$

**Second difference:**

$$
\Delta^2 a_n = \Delta(\Delta a_n) = \frac{8}{(2n+1)(2n+3)(2n+5)}.
$$

At $n=0$:

$$
\Delta^2 a_0 = \frac{8}{15}.
$$

**Third difference:**

$$
\Delta^3 a_n = \frac{48}{(2n+1)(2n+3)(2n+5)(2n+7)}.
$$

At $n=0$:

$$
\Delta^3 a_0 = \frac{48}{105}.
$$

---

**Challenge:** Compute $\Delta^4 a_0$ and confirm that the general formula is:

$$
\Delta^k a_0 = \frac{2^k k!}{1 \cdot 3 \cdot 5 \cdots (2k+1)}.
$$

---

## 4. The General Pattern

The pattern is clear: each difference introduces two more linear factors in the denominator and a factor of $2k$ in the numerator. In general:

$$
\Delta^k a_0 = \frac{2^k k!}{(2k+1)!!},
$$

where $(2k+1)!! = 1 \cdot 3 \cdot 5 \cdots (2k+1)$ is the double factorial.

Applying Euler's transformation, the alternating series becomes:

$$
\frac{\pi}{4} = \frac{1}{2} + \frac{1}{6} + \frac{1}{30} + \frac{1}{70} + \frac{1}{126} + \cdots.
$$

This is markedly faster than Gregory-Leibniz: the terms decay like $1/k!$ rather than $1/k$.

## 5. The Hypergeometric Connection

Observe that:

$$
\frac{1}{2k+1} = \int_0^1 x^{2k}\,dx.
$$

Summing under the integral:

$$
\frac{\pi}{4} = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1} = \sum_{k=0}^{\infty} \frac{(k!)^2}{(2k+1)!}.
$$

This is a hypergeometric series:

$$
\frac{\pi}{4} = {}_2F_1\!\left(1, \tfrac{1}{2}; \tfrac{3}{2}; -1\right).
$$

The hypergeometric form is the bridge to continued fractions. Euler (and later Gauss and Stieltjes) developed systematic transformations from hypergeometric series to continued fractions — the Euler continued fraction algorithm.

## 6. Euler's Continued Fraction for Arctangent

Applying Euler's continued-fraction algorithm to:

$$
\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots,
$$

yields the celebrated continued fraction:

$$
\arctan x = \cfrac{x}
{1+\cfrac{1^2 x^2}
{3+\cfrac{2^2 x^2}
{5+\cfrac{3^2 x^2}
{7+\cdots}}}}.
$$

This is the Euler–Lambert continued fraction for the inverse tangent.

## 7. Specializing to $x=1$

Since $\arctan(1) = \frac{\pi}{4}$, set $x=1$:

$$
\boxed{
\frac{\pi}{4}
=
\cfrac{1}
{1+\cfrac{1^2}
{3+\cfrac{2^2}
{5+\cfrac{3^2}
{7+\cfrac{4^2}
{9+\cdots}}}}}
}.
$$

The numerators are $1^2, 2^2, 3^2, 4^2, \dots = n^2$ (polynomial of degree $2$) and the denominators are $1, 3, 5, 7, 9, \dots = 2n+1$ (polynomial of degree $1$).

## 8. Why Squares Appear

The structural metamorphosis — linear denominators $1/(2n+1)$ in the original series becoming quadratic numerators $n^2$ in the continued fraction — is a direct consequence of the Euler transformation's algebra:

1. The original series has terms of the form $(-1)^n / (2n+1)$, which is a rational function with linear denominator.
2. Euler's transformation involves forward differences $\Delta^n$, each of which introduces two additional linear factors in the denominator and a factor of $2$ in the numerator.
3. After $n$ iterations, the numerator accumulates $2^n n!$ while the denominator accumulates the double factorial $(2n+1)!!$.
4. When Euler's continued-fraction algorithm processes these ratios, the algebraic simplification produces $(n+1)^2/((2n+1)(2n+3))$, which the algorithm converts to partial numerators $n^2$ and partial denominators $2n+1$.

The **degree-doubling phenomenon**: a series with denominator degree $d$ transforms into a continued fraction whose numerator degree is $2d$. Here $d=1$, so numerators have degree $2$ (the squares).

---

| Object | Terms | Degree |
|---|---|---|
| Gregory-Leibniz series | $\frac{(-1)^n}{2n+1}$ | Denominator degree 1 |
| Euler transformed series | $\frac{2^n n!}{2^{n+1} (2n+1)!!}$ | Denominator degree $n+1$ |
| Euler CF numerators | $1^2, 2^2, 3^2, \dots$ | Degree 2 |
| Euler CF denominators | $1, 3, 5, 7, \dots$ | Degree 1 |

---

## 9. Deeper Significance

This transformation is not a one-off trick. The same mechanism applies to:

- **Catalan's constant** — a series with degree $2$ denominators transforms into a continued fraction with degree $4$ numerators.
- **$\zeta(3)$ (Apéry)** — Apéry's famous proof of irrationality uses a continued fraction derived via a related transformation.
- **General hypergeometric ${}_pF_q$** — Euler's continued fraction algorithm systematically converts hypergeometric series to continued fractions.

The Gregory-Leibniz → $\pi$ continued fraction is the entry point to this entire landscape.

## 10. Final Challenge

**Synthesis challenge:** Consider Catalan's constant:

$$
G = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2}.
$$

1. Compute the first three forward differences $\Delta^k a_0$ for $a_n = 1/(2n+1)^2$.
2. The known continued fraction for $G$ has numerators $1^4, 2^4, 3^4, \dots$ (degree 4). Explain why the degree-doubling phenomenon predicts this.
3. Compute the first three convergents of this continued fraction and compare them to the true value $G \approx 0.915965594$.

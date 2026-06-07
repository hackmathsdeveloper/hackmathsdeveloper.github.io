---
title: "From Gregory-Leibniz to Brouncker: The Euler Transformation That Gave π Its Most Elegant Fraction"
date: 2026-06-08
categories:
  - Analysis
  - Mathematics
tags:
  - continued-fractions
  - pi
  - brouncker
  - euler-transformation
  - gregory-leibniz-series
  - degree-analysis
  - catalan-constant
share: true
read_time: true
excerpt: "The Euler transformation converts rational-function series into polynomial continued fractions with a precise degree-doubling law: a series with denominator degree d becomes a continued fraction whose numerators have degree 2d. Lord Brouncker's 1655 continued fraction for 4/π is the canonical example."
---

**Challenge to the reader:** The Gregory-Leibniz series has denominator degree 1. The resulting continued fraction has numerator degree 2 (squares). For Catalan's constant $G = \sum (-1)^n/(2n+1)^2$, the denominator degree is 2. Predict the degree of the numerators in the corresponding continued fraction.

---

## 1. Two Continued Fractions for $\pi$

The literature contains two celebrated continued fractions for $\pi$, related by inversion:

**Euler's continued fraction for $\pi/4$:**

$$
\frac{\pi}{4}
=
\cfrac{1}
{1+\cfrac{1^2}
{3+\cfrac{2^2}
{5+\cfrac{3^2}
{7+\cdots}}}}.
$$

**Brouncker's continued fraction for $4/\pi$ (1655):**

$$
\frac{4}{\pi}
=
1 + \cfrac{1^2}
{2+\cfrac{3^2}
{2+\cfrac{5^2}
{2+\cfrac{7^2}
{2+\cdots}}}}
=
1 + \mathop{\mathbf{K}}\limits_{n=1}^{\infty}\frac{(2n-1)^2}{2}.
$$

Brouncker's version is the reciprocal of Euler's, rearranged. Each reveals a different structural aspect of the same underlying transformation.

## 2. The Euler Transformation: A General Phenomenon

The Euler transformation is the engine behind both. For an infinite series:

$$
\sum_{n \ge 0} a_n,
$$

the transformation equates it to a continued fraction of the form:

$$
\sum_{n \ge 0} a_n =
a_0 +
\cfrac{a_1}
{1+\cfrac{-a_2/a_1}
{1+a_2/a_1+\cfrac{-a_1 a_3/(a_2(a_2+a_3))}
{1+a_3/a_2+\cdots}}}.
$$

The crucial structural observation: **if the terms $a_n$ of the original series are rational functions of $n$ with a fixed denominator degree $d$, then the resulting continued fraction has partial numerators whose degree is at least $2d$.**

This degree-doubling is not an accident — it is a direct algebraic consequence of how forward differences interact with rational functions under the Euler transformation.

## 3. Case Study: Gregory-Leibniz → Brouncker

The Gregory-Leibniz series:

$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}.
$$

Here $a_n = 1/(2n+1)$ has denominator degree $d=1$. Applying Euler's transformation:

1. The forward differences $\Delta^k a_0 = 2^k k! / (2k+1)!!$ accumulate polynomial degree in both numerator and denominator.
2. When the continued-fraction algorithm processes these, the algebraic simplification reorganizes the structure.
3. The result is Brouncker's fraction:

$$
\frac{4}{\pi} = 1 + \frac{1^2}{2 + \frac{3^2}{2 + \frac{5^2}{2 + \cdots}}}.
$$

The partial numerators are $(2n-1)^2$, a polynomial of **degree 2** (matching the $2d$ prediction), while the partial denominators are the constant $2$, a polynomial of **degree 0**.

## 4. The Degree-Doubling Law in Generality

The sources identify this as a systematic phenomenon:

| Series | Denominator degree $d$ | CF numerator degree | Example numerators |
|---|---|---|---|
| Gregory-Leibniz | 1 | 2 ($= 2d$) | $1^2, 3^2, 5^2, \dots$ |
| Catalan's constant | 2 | 4 ($= 2d$) | $1^4, 2^4, 3^4, \dots$ |
| General alternating | $d$ | $2d$ | Polynomial of degree $2d$ |

For Catalan's constant:

$$
G = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2},
$$

the denominator has degree $2$, so the continued fraction numerator degree is $4$. Indeed, the known continued fraction for Catalan's constant involves fourth powers as partial numerators.

---

**Challenge:** For the series $\sum_{n=0}^{\infty} (-1)^n / (n+1)^3$, predict the continued fraction numerator degree. Then find the first three convergents using the Euler transformation.

---

## 5. Why the Phenomenon Occurs

The degree doubling is rooted in the forward difference operation. Each application of $\Delta$ to a rational function $a_n = P(n)/Q(n)$ produces:

$$
\Delta a_n = \frac{P(n)}{Q(n)} - \frac{P(n+1)}{Q(n+1)} = \frac{P(n)Q(n+1) - P(n+1)Q(n)}{Q(n)Q(n+1)}.
$$

The denominator degree doubles (from $\deg Q$ to $2\deg Q$), and the numerator degree increases correspondingly. After $k$ iterations, the denominator accumulates $k$ additional factors, each of degree $\deg Q$, producing total denominator degree $k \cdot \deg Q$.

When Euler's continued-fraction algorithm processes the ratios $\Delta^n a_0 / \Delta^{n-1} a_0$, the algebraic cancellation leaves numerator degree $2d$ and denominator degree $d$ (or lower), which become the partial numerators and denominators of the resulting continued fraction.

## 6. The Simplification Step

The transformation from the Gregory-Leibniz series to Brouncker's fraction involves a crucial algebraic simplification. The alternating rational terms $(-1)^n/(2n+1)$, when processed through the Euler machinery, generate expressions involving products of consecutive odd integers. These products simplify to ratios like:

$$
\frac{(2n+1)^2}{(2n-1)(2n+3)},
$$

which the continued fraction algorithm then renders as partial numerator $(2n-1)^2$ and partial denominator $2$.

The squared odd integers emerge not from any squaring operation in the original series, but from the algebraic interplay of consecutive terms under the Euler transformation.

## 7. Connection to Modern Research

The degree-doubling phenomenon connects classical 18th-century analysis to modern research on polynomial continued fractions:

- **Bowman and McLaughlin's polynomial continued fractions** systematically classify continued fractions by the degrees of $a_n$ and $b_n$, with the equal-degree case being particularly rich.
- **The Euler transformation** provides one of the oldest and most important bridges between series and continued fractions, predating Pincherle's theorem by over a century.
- **Apéry's proof of $\zeta(3)$'s irrationality** uses a continued fraction derived via a related transformation — the degree analysis is essential to establishing the growth conditions needed for the irrationality argument.

## 8. Final Challenge

**Synthesis challenge:** The general Euler transformation for an alternating series can be written:

$$
\sum_{n=0}^{\infty} (-1)^n a_n = \cfrac{a_0}{1 + \cfrac{a_1/a_0}{1 - a_1/a_0 + \cfrac{a_2/a_1}{1 + a_2/a_1 - \cdots}}}.
$$

1. Take $a_n = 1/(2n+1)^3$ (denominator degree $d=3$). According to the degree-doubling law, what degree should the continued fraction numerators have?
2. Compute the first two partial numerators of the resulting continued fraction.
3. Compute the first three convergents and compare them to the true sum $\approx 0.968946$.

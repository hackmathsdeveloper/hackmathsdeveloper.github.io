---
title: "The Infinite Product for tan(x) That Hides in Sine and Cosine — And Why arctan(x) Has None"
date: 2026-06-08
categories:
  - Analysis
  - Mathematics
tags:
  - infinite-product
  - tangent
  - arctangent
  - sine
  - cosine
  - complex-analysis
  - weierstrass-factorization
share: true
read_time: true
excerpt: "Dividing Euler's sine product by the cosine product yields a clean infinite product for tan(x) — one factor for each zero and pole. But ask the same question for arctan(x), and the answer flips: no such product exists. This is the story of why some functions factor and others refuse."
---

**Challenge to the reader:** Compute the first three factors of the $\tan x$ product for $n = 1, 2, 3$ and evaluate the truncated product at $x = \pi/4$. Compare the result to the exact value $\tan(\pi/4) = 1$. How quickly does the product converge?

---

## 1. What We Already Know

Recall Euler's sine product from the companion derivation:

$$
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

There is a corresponding product for $\cos(\pi z)$ whose zeros are at the half-integers $z = \pm\frac{1}{2}, \pm\frac{3}{2}, \pm\frac{5}{2}, \dots$:

$$
\cos(\pi z) = \prod_{n=1}^{\infty}\left(1 - \frac{4z^{2}}{(2n-1)^{2}}\right).
$$

This comes from the same logic: entire function, zeros at $z = \frac{2n-1}{2}$, simple, order 1. Fix the multiplicative constant by evaluating at $z = 0$, where $\cos(0) = 1$.

---

## 2. Dividing Sine by Cosine Gives Tangent

Define:

$$
\tan(\pi z) = \frac{\sin(\pi z)}{\cos(\pi z)}.
$$

Using the two products above:

$$
\tan(\pi z)
= \frac{\pi z\prod_{n=1}^{\infty}\left(1 - \dfrac{z^{2}}{n^{2}}\right)}
       {\prod_{n=1}^{\infty}\left(1 - \dfrac{4z^{2}}{(2n-1)^{2}}\right)}.
$$

Thus:

$$
\boxed{
\tan(\pi z)
= \pi z\prod_{n=1}^{\infty}
\frac{1 - \dfrac{z^{2}}{n^{2}}}{1 - \dfrac{4z^{2}}{(2n-1)^{2}}}
}.
$$

In the usual variable $x$, putting $z = x/\pi$:

$$
\boxed{
\tan x = x\prod_{n=1}^{\infty}
\frac{1 - \dfrac{x^{2}}{\pi^{2}n^{2}}}{1 - \dfrac{4x^{2}}{\pi^{2}(2n-1)^{2}}}
}.
$$

This is the natural "Euler-type" infinite product for $\tan x$, expressed purely in terms of its zeros $x = k\pi$ (in the numerator) and poles $x = \frac{\pi}{2} + k\pi$ (in the denominator).

**Challenge to the reader:** Derive the cosine product from scratch: start with an entire function whose zeros are the half-integers, write the Weierstrass product, group terms symmetrically, and fix the constant using $z = 0$.

---

## 3. The Structural Beauty of the tan Product

What makes this product satisfying is its **symmetry**. Each factor is a ratio:

$$
\frac{1 - \dfrac{x^{2}}{\pi^{2}n^{2}}}{1 - \dfrac{4x^{2}}{\pi^{2}(2n-1)^{2}}}.
$$

The numerator vanishes at the zeros of $\tan x$ ($x = \pm \pi n$), and the denominator vanishes at the poles ($x = \pm\frac{\pi}{2}(2n-1)$). The product weaves together the full meromorphic structure of tangent into a single expression.

If you want a "from scratch" derivation similar in spirit to the cotangent-Mittag-Leffler argument, you can also start from the partial fraction expansion:

$$
\pi \cot(\pi z) = \frac{1}{z} + \sum_{n=1}^{\infty}\frac{2z}{z^{2}-n^{2}}, \qquad
\pi \tan(\pi z) = \sum_{n=-\infty}^{\infty}\frac{1}{z - (n+\tfrac{1}{2})},
$$

then integrate to get a logarithm of a product, and finally exponentiate. The result matches the product above up to a constant factor, which you fix by local expansion near $0$.

---

## 4. Why arctan Has No Analogous Infinite Product

A Weierstrass-style "infinite product representation" is fundamentally a representation of **entire** functions in terms of their zeros:

$$
f(z) = e^{g(z)}\prod_{n} E_p\!\left(\frac{z}{z_n}\right),
$$

where $z_n$ are the zeros of $f$.

$\arctan z$ is not a suitable candidate for such a product:

- **$\arctan z$ is not entire.** It is only analytic on $\mathbb{C} \setminus \lbrace i, -i\rbrace$ because it satisfies $\tan(\arctan z) = z$ and $\tan w$ has poles at $\frac{\pi}{2} + k\pi$, which translate into logarithmic branch points for $\arctan$ in its complex definition.

- **$\arctan z$ has no nontrivial zeros.** Over $\mathbb{C}$, the standard branch of $\arctan z$ has no zeros other than $z = 0$, so there is no nontrivial infinite set of zeros to encode in a product. A product with only one factor is just a linear function — not an infinite product at all.

Instead, $\arctan x$ is naturally represented by **series** or integrals:

$$
\arctan x = \int_{0}^{x}\frac{1}{1+t^{2}}\,dt
= x - \frac{x^{3}}{3} + \frac{x^{5}}{5} - \cdots, \qquad |x| \le 1.
$$

---

## 5. What You Can Do Instead

You can of course produce **products whose values are arctan constants**, for example by integrating products involving $\cos x$ or $\sin x$ and comparing to $\arctan$ limits. Machin-type formulas express constants like $\pi$ as finite linear combinations of $\arctan(1/n)$:

$$
\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}.
$$

But these are finite combinations, not infinite products for the function $\arctan x$ itself. There is no standard closed-form infinite product "for $\arctan x$" analogous to Euler's sine product or the $\tan x$ product above.

## 6. Deeper Significance

The contrast between $\tan x$ (has an infinite product) and $\arctan x$ (does not) teaches an important lesson about complex analysis: **infinite product representations belong to entire functions**, and more generally to meromorphic functions that can be expressed as ratios of entire functions. The inverse trigonometric functions are not entire — they have branch cuts — and so they live in a different universe of representations (integrals, series, differential equations).

This also explains why $\sin$, $\cos$, and their ratio $\tan$ admit such beautiful factorizations: they are the "building blocks" of the theory, while their inverses are constructed objects that inherit their complexity from the branch structure of the logarithm.

**Final challenge:** Consider the function $\operatorname{sinc}(z) = \frac{\sin(\pi z)}{\pi z}$. Write its infinite product, then take the logarithmic derivative. Show that you recover the partial fraction expansion of $\pi\cot(\pi z) - 1/z$. This connects the product representation back to Mittag-Leffler theory — a two-way bridge between zeros and poles.

---
title: "Why Sine's Zeros Hold a Secret Infinite Product — And How Euler Cracked It Open"
date: 2026-06-08
categories:
  - Analysis
  - Mathematics
tags:
  - infinite-product
  - sine
  - euler
  - weierstrass-factorization
  - basel-problem
  - complex-analysis
  - mittag-leffler
share: true
read_time: true
excerpt: "Every sine wave crosses zero at predictable integer multiples of π. Euler discovered that these zeros encode the entire function — sin(x) equals an infinite product of factors (1 − x²/π²n²), one for each root. This is not just elegant; it solves the Basel problem as a corollary."
---

**Challenge to the reader:** Write down the first three factors of Euler's product for $\sin x$ at $n = 1, 2, 3$. Multiply them out to order $x^3$ and verify that the coefficient matches the Taylor series of $\sin x$ up to $x^3$.

---

## 1. Statement of the Target Formula

We want to show:

$$
\sin(\pi z) = \pi z \prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right), \qquad z \in \mathbb{C},
$$

which is equivalent, after substituting $z = x/\pi$, to:

$$
\sin x = x \prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right).
$$

This identity encodes **all** the zeros of the sine function into a single infinite product. Each factor $(1 - x^2 / \pi^2 n^2)$ vanishes exactly when $x = \pm \pi n$, matching where $\sin x = 0$.

Why does this matter? Because it transforms an oscillatory trigonometric function into an algebraic-looking factorization — and as a free bonus, comparing the $x^3$ coefficient with the Taylor series of $\sin x$ immediately yields $\sum_{n=1}^{\infty} 1/n^2 = \pi^2/6$, solving the famous Basel problem.

---

## 2. Using Zeros to Guess a Product

Key observations:

- $\sin(\pi z)$ is an entire function of order 1 with simple zeros at all integers $z = n \in \mathbb{Z}$.
- A natural "Weierstrass-style" product with exactly these zeros is:

$$
f(z) := z \prod_{n=1}^{\infty}\left(1 - \frac{z}{n}\right)\left(1 + \frac{z}{n}\right)
     = z \prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

Provided the product converges (which it does, by standard infinite product theory for entire functions of small order), $f$ is entire and has simple zeros exactly at $z \in \mathbb{Z}$. Thus $\sin(\pi z)$ and $f(z)$ are both entire with the same zero set and multiplicities.

By the identity theorem for holomorphic functions, their ratio has no zeros or poles, hence is an entire function with no zeros. Therefore:

$$
\frac{\sin(\pi z)}{f(z)} = e^{g(z)}
$$

for some entire function $g(z)$.

---

## 3. Showing the Ratio is Actually Constant

Define:

$$
h(z) := \frac{\sin(\pi z)}{z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)}.
$$

From above, $h(z) = e^{g(z)}$ is entire and never zero.

To see that $g$ is constant, we use the logarithmic derivative:

**Step 1.** Start from the known partial fraction expansion of $\pi \cot(\pi z)$:

$$
\pi \cot(\pi z) = \frac{1}{z} + \sum_{n=1}^{\infty} \frac{2z}{z^{2} - n^{2}}, \qquad z \notin \mathbb{Z}.
$$

This can be obtained by residue calculus or Mittag-Leffler theory.

**Step 2.** Note that:

$$
\frac{d}{dz}\log\sin(\pi z)
= \frac{\sin'(\pi z)}{\sin(\pi z)}\cdot\pi
= \pi\cot(\pi z).
$$

**Step 3.** Compute the logarithmic derivative of the candidate product:

$$
\log\!\left(\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})\right)
= \log(\pi z) + \sum_{n=1}^{\infty}\log\!\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

Differentiating termwise (justified by uniform convergence on compact sets away from the zeros):

$$
\frac{d}{dz}\log\!\left(\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})\right)
= \frac{1}{z} + \sum_{n=1}^{\infty}\frac{-2z/n^{2}}{1 - z^{2}/n^{2}}
= \frac{1}{z} + \sum_{n=1}^{\infty}\frac{2z}{z^{2} - n^{2}}.
$$

**Step 4.** Compare with the expansion from Step 1:

$$
\frac{d}{dz}\log\sin(\pi z) = \frac{d}{dz}\log\!\left(\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})\right).
$$

Hence:

$$
\frac{d}{dz}\log\frac{\sin(\pi z)}{\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})} = 0,
$$

so the logarithm of the ratio is constant; i.e., $g(z)$ is constant and:

$$
\sin(\pi z) = C\,\pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
$$

for some constant $C \in \mathbb{C}$.

**Challenge to the reader:** Take the logarithmic derivative of $\cos(\pi z)$ written as a product over half-integer zeros and verify you recover $-\pi\tan(\pi z)$. This is the direct analog of what we just did for sine.

---

## 4. Determining the Constant via Taylor Expansion

Finally, expand near $z = 0$.

The Maclaurin series for $\sin(\pi z)$ is:

$$
\sin(\pi z) = \pi z - \frac{\pi^{3}}{6}z^{3} + O(z^{5}).
$$

For the product side, note that:

$$
\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
= 1 - \left(\sum_{n=1}^{\infty}\frac{1}{n^{2}}\right)z^{2} + O(z^{4}),
$$

because the linear term vanishes and the quadratic term is minus the sum of $1/n^{2}$.

So:

$$
\pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
= \pi z - \pi z\left(\sum_{n=1}^{\infty}\frac{1}{n^{2}}\right)z^{2} + O(z^{5})
= \pi z - \pi\left(\sum_{n=1}^{\infty}\frac{1}{n^{2}}\right)z^{3} + O(z^{5}).
$$

Comparing coefficients of $z$ shows immediately that $C = 1$. (The comparison at $z^{3}$ then retrieves the Basel sum $\sum_{n=1}^{\infty}1/n^{2} = \pi^{2}/6$, but you do not need that to fix $C$ — simply look at the leading term.)

Thus:

$$
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right),
$$

and in the original variable $x$:

$$
\boxed{\sin x = x\prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right)}.
$$

---

## 5. Alternative Weierstrass Viewpoint

There is a closely related derivation using general Weierstrass factorization: for an entire function of order 1 whose zeros are the integers, Weierstrass theory gives a product of the form:

$$
\sin(\pi z) = e^{az+b}z\prod_{n\neq 0}\left(1 - \frac{z}{n}\right)e^{z/n},
$$

and additional symmetry (oddness and boundedness on vertical strips) forces $a = 0$, while scaling at $0$ fixes $b = 0$, leading again to Euler's product.

## 6. Deeper Significance

Euler's sine product is more than a curiosity. It reveals a profound principle: **an entire function is essentially determined by its zeros**, up to an exponential factor. This is the content of the Weierstrass factorization theorem, and the sine product is its most famous and accessible example.

Moreover, the product provides a bridge between trigonometry and number theory. The coefficient comparison that yields $\zeta(2) = \pi^2/6$ is the first step into the deep relationship between the Riemann zeta function and the distribution of primes — a thread that runs through all of analytic number theory.

**Final challenge:** Use Euler's sine product to derive the value of $\sum_{n=1}^{\infty} 1/n^4 = \pi^4/90$. Hint: expand the product to order $z^5$ and match coefficients with the Taylor series of $\sin(\pi z)$. This requires identifying the pattern of elementary symmetric sums of $1/n^2$, $1/n^4$, and their relationship.

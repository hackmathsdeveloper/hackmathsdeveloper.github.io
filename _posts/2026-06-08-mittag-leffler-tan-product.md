---
title: "How to Build tan(x) From Its Poles Alone — The Mittag-Leffler Route to an Infinite Product"
date: 2026-06-08
categories:
  - Analysis
  - Mathematics
tags:
  - mittag-leffler
  - tangent
  - infinite-product
  - partial-fractions
  - complex-analysis
  - meromorphic-functions
  - cosine-product
share: true
read_time: true
excerpt: "Instead of dividing sine by cosine, you can construct the infinite product for tan(x) directly from its poles and residues using Mittag-Leffler's theorem. Write the partial fraction sum, recognize it as a logarithmic derivative, integrate — and the product emerges."
---

**Challenge to the reader:** Write down the first five poles of $\tan(\pi z)$ (positive and negative), compute their residues, and verify that pairing the $+k$ and $-k-1$ terms produces the symmetric form $2z/(z^2 - (n+1/2)^2)$.

---

## 1. Setting Up the Meromorphic Data for tan(πz)

Consider $f(z) = \tan(\pi z)$. It is meromorphic on $\mathbb{C}$ with:

- Poles at $z_k = k + \tfrac{1}{2}$, for $k \in \mathbb{Z}$.
- All poles are simple, and the residue at each pole is $-1/\pi$ (because $\tan w$ has residue $1$ at its poles $w = \tfrac{\pi}{2} + k\pi$, and the factor $\pi$ in $\tan(\pi z)$ contributes a Jacobian $\pi$).

Mittag-Leffler's theorem tells us that we can expand a meromorphic function as a sum of its principal parts, possibly plus an entire function. For $\pi\tan(\pi z)$ the theorem gives the explicit partial fraction expansion:

$$
\pi \tan(\pi z)
= \lim_{N\to\infty}\sum_{k=-N}^{N}\frac{-1}{z - (k+\tfrac{1}{2})}
= 2z\sum_{n=0}^{\infty}\frac{-1}{z^{2} - (n+\tfrac{1}{2})^{2}},
$$

where the second equality is obtained by pairing terms $k$ and $-k-1$ and simplifying.

Equivalently:

$$
\tan(\pi z)
= -\frac{2z}{\pi}\sum_{n=0}^{\infty}\frac{1}{z^{2} - (n+\tfrac{1}{2})^{2}}.
$$

This is the starting point: **the poles of tangent completely determine its partial fraction structure**.

---

## 2. Relating tan(πz) to the Logarithmic Derivative of cos(πz)

We now look at the logarithmic derivative of $\cos(\pi z)$. Define:

$$
g(z) := \cos(\pi z).
$$

Then:

$$
\frac{g'(z)}{g(z)} = \frac{d}{dz}\log g(z)
= -\pi\tan(\pi z).
$$

On the other hand, $\cos(\pi z)$ is an entire function whose zeros are exactly the half-integers $z_k = k+\tfrac{1}{2}$, all simple. For such a function, the logarithmic derivative can be written using the zeros:

$$
\frac{g'(z)}{g(z)}
= \sum_{k\in\mathbb{Z}}\frac{1}{z - z_k} + \text{(entire correction)}.
$$

But by the Mittag-Leffler expansion above, we already know that:

$$
\pi\tan(\pi z) = \sum_{k\in\mathbb{Z}} \frac{-1}{z - (k+\tfrac{1}{2})},
$$

hence:

$$
-\pi\tan(\pi z)
= \sum_{k\in\mathbb{Z}} \frac{1}{z - (k+\tfrac{1}{2})}.
$$

So we have:

$$
\frac{g'(z)}{g(z)} = -\pi\tan(\pi z)
= \sum_{k\in\mathbb{Z}} \frac{1}{z - (k+\tfrac{1}{2})}.
$$

The right-hand side is already a convergent Mittag-Leffler expansion (principal parts only), so the "entire correction" term is actually **zero**. In other words, the logarithmic derivative is fully determined by the poles — no extra entire function is needed.

**Challenge to the reader:** Prove that if two meromorphic functions have the same principal parts at all poles and both vanish at a common point, they must be identical. Apply this to justify why the entire correction term vanishes.

---

## 3. Integrating the Logarithmic Derivative

Integrate $g'(z)/g(z)$ with respect to $z$. Formally:

$$
\log g(z) = \int \frac{g'(z)}{g(z)}\,dz
= \int \sum_{k\in\mathbb{Z}}\frac{1}{z - (k+\tfrac{1}{2})}\,dz.
$$

Integrating term by term (justified by uniform convergence on compact subsets away from the zeros/poles):

$$
\log g(z) = \sum_{k\in\mathbb{Z}}\log\!\left(z - (k+\tfrac{1}{2})\right) + C,
$$

and exponentiating:

$$
g(z) = C\prod_{k\in\mathbb{Z}}\left(z - (k+\tfrac{1}{2})\right).
$$

To normalize and get something symmetric (and absolutely convergent as a product), group terms $k$ and $-k-1$. This gives factors of the form:

$$
\left(z - (k+\tfrac{1}{2})\right)\!\left(z - (-k-\tfrac{1}{2})\right)
= z^{2} - \left(k+\tfrac{1}{2}\right)^{2},
$$

so we can write:

$$
\cos(\pi z)
= C\prod_{n=0}^{\infty}\left(1 - \frac{z^{2}}{(n+\tfrac{1}{2})^{2}}\right).
$$

Choosing $z = 0$ gives:

$$
1 = \cos(0) = C\prod_{n=0}^{\infty}\left(1 - 0\right) = C,
$$

hence $C = 1$. Furthermore, recognizing that $(n+\tfrac{1}{2}) = \tfrac{2n+1}{2}$ and reindexing:

$$
\cos(\pi z) = \prod_{n=1}^{\infty}\left(1 - \frac{4z^{2}}{(2n-1)^{2}}\right).
$$

This is the infinite product for cosine, derived **purely from its zeros via Mittag-Leffler integration** — no prior knowledge of sine required.

---

## 4. Assembling the tan Product

From the earlier sine product:

$$
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

Combine this with the cosine product we just derived:

$$
\cos(\pi z)
= \prod_{n=1}^{\infty}\left(1 - \frac{4z^{2}}{(2n-1)^{2}}\right).
$$

Then:

$$
\tan(\pi z)
= \frac{\sin(\pi z)}{\cos(\pi z)}
= \frac{\pi z\prod_{n=1}^{\infty}\left(1 - \dfrac{z^{2}}{n^{2}}\right)}
       {\prod_{n=1}^{\infty}\left(1 - \dfrac{4z^{2}}{(2n-1)^{2}}\right)}.
$$

Thus the Mittag-Leffler route gives, up to the normalization we fixed via $\cos(0) = 1$:

$$
\boxed{
\tan(\pi z)
= \pi z\prod_{n=1}^{\infty}
\frac{1 - \dfrac{z^{2}}{n^{2}}}{1 - \dfrac{4z^{2}}{(2n-1)^{2}}}
}.
$$

In the usual variable $x = \pi z$:

$$
\boxed{
\tan x
= x\prod_{n=1}^{\infty}
\frac{1 - \dfrac{x^{2}}{\pi^{2}n^{2}}}{1 - \dfrac{4x^{2}}{\pi^{2}(2n-1)^{2}}}
}.
$$

---

## 5. Deeper Significance

This derivation illustrates a powerful **two-step recipe** that generalizes far beyond tangent:

1. **Mittag-Leffler step:** Expand a meromorphic function as a sum over its principal parts (poles and residues).
2. **Integration step:** Recognize the sum as a logarithmic derivative, integrate termwise, and exponentiate to recover a product over zeros.

This recipe works for any meromorphic function that is the logarithmic derivative of an entire function — which includes $\cot$, $\tan$, the Weierstrass $\wp$-function, and many others. It inverts the usual direction (product → logarithmic derivative → partial fractions) and shows that the two representations are mathematically equivalent.

**Final challenge:** Apply the same two-step recipe to $\pi\cot(\pi z)$. Start from its Mittag-Leffler expansion $\pi\cot(\pi z) = 1/z + \sum_{n=1}^{\infty} 2z/(z^2 - n^2)$, recognize it as the logarithmic derivative of $\sin(\pi z)$, integrate, and recover Euler's sine product. This is the "dual" derivation — you'll see how the two products are two sides of the same coin.

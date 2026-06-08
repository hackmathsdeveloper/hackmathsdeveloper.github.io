---
title: "The Cotangent Trick: How Mittag-Leffler Reveals Euler's Sine Product Without Guessing"
date: 2026-06-08
categories:
  - Analysis
  - Mathematics
tags:
  - mittag-leffler
  - cotangent
  - sine-product
  - euler
  - partial-fractions
  - complex-analysis
  - infinite-product
share: true
read_time: true
excerpt: "Start with the partial fraction expansion of πcot(πz) — every integer is a simple pole with residue 1. Recognize it as the logarithmic derivative of sin(πz), integrate term by term, and Euler's infinite product drops out. No guessing, no Weierstrass theory needed: just poles, residues, and integration."
---

**Challenge to the reader:** Verify that the residue of $\pi\cot(\pi z)$ at $z = n$ (for any integer $n$) is exactly $1$. Compute it directly using the definition $\cot w = \cos w / \sin w$ and the fact that $\sin(\pi z)$ has a simple zero at each integer.

---

## 1. Meromorphic Data for πcot(πz)

Consider $F(z) = \pi\cot(\pi z)$. It is meromorphic on $\mathbb{C}$ with:

- Poles at all integers $n \in \mathbb{Z}$.
- All poles simple, with residue $1$ at each integer (since $\cot w$ has residue $1$ at $w = k\pi$, and the factor $\pi$ from $w = \pi z$ cancels with the Jacobian $dw = \pi\,dz$).

Mittag-Leffler's theorem gives an expansion of a meromorphic function as a sum of its principal parts plus (at most) an entire function. For $F(z)$, these principal parts are:

$$
\frac{1}{z-n}, \qquad n \in \mathbb{Z}.
$$

A standard symmetric choice of expansion is:

$$
\pi\cot(\pi z)
= \frac{1}{z} + \sum_{n\neq 0}\left(\frac{1}{z-n} + \frac{1}{n}\right),
$$

where the $\tfrac{1}{n}$ terms are inserted to make the resulting series converge normally; they contribute an entire function which is absorbed globally.

Grouping $n$ and $-n$ yields the more familiar form:

$$
\pi\cot(\pi z)
= \frac{1}{z} + \sum_{n=1}^{\infty}\left(\frac{1}{z-n} + \frac{1}{z+n}\right).
$$

Compute the combined fraction:

$$
\frac{1}{z-n} + \frac{1}{z+n}
= \frac{(z+n) + (z-n)}{z^{2} - n^{2}}
= \frac{2z}{z^{2} - n^{2}},
$$

so:

$$
\boxed{
\pi\cot(\pi z)
= \frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2}-n^{2}}, \qquad z \notin \mathbb{Z}.
}
$$

This is the Mittag-Leffler partial fraction expansion for $\pi\cot(\pi z)$.

---

## 2. Recognizing πcot(πz) as a Logarithmic Derivative

Let $f(z) = \sin(\pi z)$. Then:

$$
\frac{d}{dz}\log f(z)
= \frac{f'(z)}{f(z)}
= \frac{\pi\cos(\pi z)}{\sin(\pi z)}
= \pi\cot(\pi z), \qquad z \notin \mathbb{Z}.
$$

So we have:

$$
\frac{d}{dz}\log\sin(\pi z)
= \frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2} - n^{2}}.
$$

The right-hand side is already a convergent sum of rational functions on any compact set avoiding the integers, so we can integrate termwise there.

**Challenge to the reader:** Show that the series $\sum_{n=1}^{\infty} \frac{2z}{z^2 - n^2}$ converges uniformly on any compact subset of $\mathbb{C} \setminus \mathbb{Z}$. This justifies the termwise integration in the next step.

---

## 3. Integrating the Partial Fraction Expansion

Integrate both sides with respect to $z$:

$$
\log\sin(\pi z)
= \int\left(\frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2}-n^{2}}\right)\,dz.
$$

Compute the integrals:

- $\displaystyle \int \frac{1}{z}\,dz = \log z$ (up to additive constant).
- For each $n \ge 1$:
  $$
  \int \frac{z}{z^{2}-n^{2}}\,dz
  = \frac{1}{2}\log(z^{2}-n^{2}) + \text{const},
  $$
  since the derivative of $z^{2} - n^{2}$ is $2z$.

Thus:

$$
\log\sin(\pi z)
= \log z + \sum_{n=1}^{\infty}\log(z^{2}-n^{2}) + C,
$$

where $C$ is a constant of integration.

Rewrite $\log(z^{2}-n^{2})$ as $\log n^{2} + \log(1 - z^{2}/n^{2})$:

$$
\log(z^{2}-n^{2}) = \log n^{2} + \log\!\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

Substitute:

$$
\log\sin(\pi z)
= \log z + \sum_{n=1}^{\infty}\left[\log n^{2} + \log\!\left(1 - \frac{z^{2}}{n^{2}}\right)\right] + C.
$$

The $\sum_{n=1}^{\infty}\log n^{2}$ piece depends only on $n$, not on $z$; it can be absorbed into the constant. Denote by $C'$ the new constant:

$$
\log\sin(\pi z)
= C' + \log z + \sum_{n=1}^{\infty}\log\!\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

---

## 4. Exponentiate and Fix the Constant

Exponentiate:

$$
\sin(\pi z)
= e^{C'}\,z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).
$$

So we have:

$$
\boxed{
\sin(\pi z)
= C\,z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right),
}
$$

for some constant $C = e^{C'}$.

To determine $C$, compare behavior near $z = 0$.

Using the usual Taylor series:

$$
\sin(\pi z) = \pi z - \frac{\pi^{3}}{6}z^{3} + O(z^{5}), \qquad z \to 0.
$$

On the other hand, expand the product:

$$
z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
= z\left(1 + O(z^{2})\right),
$$

so the leading term is just $z$.

Thus near zero:

$$
\sin(\pi z) \sim \pi z, \qquad
C\,z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right) \sim C z.
$$

Therefore $C = \pi$, and we obtain Euler's product:

$$
\boxed{
\sin(\pi z)
= \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right), \qquad z \in \mathbb{C}.
}
$$

Returning to $x = \pi z$, this is:

$$
\sin x = x\prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right).
$$

---

## 5. Deeper Significance

This derivation reveals something subtle about the relationship between **poles** and **zeros** in complex analysis. The Mittag-Leffler expansion of $\pi\cot(\pi z)$ encodes the poles of cotangent — but $\cot$ is the **logarithmic derivative** of $\sin$. So the poles of $\cot$ are exactly the zeros of $\sin$ (plus the origin). By integrating the pole expansion, we reconstruct the zero-based product.

This is a manifestation of a deeper principle: **the logarithmic derivative converts products (over zeros) into sums (over poles)**. The entire machinery of Weierstrass products and Mittag-Leffler partial fractions are two sides of this single transformation — differentiate a product to get a sum, integrate a sum to get a product.

The same technique works for any meromorphic function that can be expressed as a logarithmic derivative: the Gamma function, elliptic functions, and beyond.

**Final challenge:** Apply this technique to the Gamma function. Start from the known Mittag-Leffler expansion of the digamma function $\psi(z) = \Gamma'(z)/\Gamma(z)$, integrate termwise, and derive the Weierstrass product for $1/\Gamma(z)$. This connects the sine product to the broader theory of special functions — and reveals why $\Gamma(z)$ has no zeros at all.

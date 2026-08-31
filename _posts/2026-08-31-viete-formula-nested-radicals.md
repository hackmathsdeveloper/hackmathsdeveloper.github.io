---
title: "Why π Lives Inside an Infinite Tower of Square Roots — Viète's Secret Product"
date: 2026-08-31
categories:
  - Analysis
  - Mathematics
tags:
  - vietes-formula
  - pi
  - half-angle-identities
  - nested-radicals
  - infinite-products
  - archimedean-bounds
share: true
read_time: true
excerpt: "One half-angle identity, applied again and again to a polygon inscribed in the unit circle, produces Viète's 1593 product: 2/π as an infinite tower of nested square roots. Here is the full derivation, one doubling of sides at a time."
---

**Challenge to the reader:** Starting from $\cos(\pi/2)=0$ and using only the half-angle formula $\cos(\theta/2)=\sqrt{(1+\cos\theta)/2}$, write $\cos(\pi/4)$, $\cos(\pi/8)$, $\cos(\pi/16)$ as nested radicals, then multiply the first three factors of Viète's product and compare the result with $2/\pi\approx 0.63662$. (All three factors are computed in §2.)

*Part of the Viète series: [Ludolph van Ceulen and the 35 Digits]({% post_url 2026-08-31-van-ceulen-35-digits-pi %}) · [Twenty Pattern Variations on Viète's Product]({% post_url 2026-08-31-viete-formula-twenty-variations %}).*

## The core theorem

**Viète's formula (1593).**

$$
\frac{2}{\pi} = \frac{\sqrt{2}}{2}
\cdot
\frac{\sqrt{2+\sqrt{2}}}{2}
\cdot
\frac{\sqrt{2+\sqrt{2+\sqrt{2}}}}{2}
\cdots
$$

Each new factor nests one more $2$ inside the radical. This was the first infinite product for $\pi$ in the history of mathematics — and the first formula for $\pi$ built from nothing but the number $2$ and square roots.

**Why it matters.** The formula converts a geometric limit — regular polygons whose side counts double forever — into a purely algebraic recipe. It also shows why a transcendental number can be approximated by numbers that are as constructible as it gets: every finite partial product is a ruler-and-compass length.

---

## 1. The half-angle engine

The entire derivation runs on one identity — the cosine half-angle formula:

$$
\cos\left(\frac{\theta}{2}\right)=\sqrt{\frac{1+\cos\theta}{2}},\qquad 0 \le \theta \le \pi.
$$

One application halves the angle at the cost of exactly one new square root. The sine companion

$$
\sin\left(\frac{\theta}{2}\right)=\sqrt{\frac{1-\cos\theta}{2}}
$$

drives the side lengths of the polygons instead. Using the Pythagorean identity $\cos\theta=\sqrt{1-\sin^2\theta}$, it can be written entirely in terms of sine:

$$
\sin\left(\frac{\theta}{2}\right)=\frac{\sqrt{2-\sqrt{4-4\sin^2\theta}}}{2}=\frac{\sqrt{2-\sqrt{2^2-(2\sin\theta)^2}}}{2}.
$$

---

## 2. Doubling the polygon: square to circle

Viète inscribes a regular polygon in the unit circle (radius $R=1$) and repeatedly doubles the number of sides: square ($n=4$), octagon ($n=8$), 16-gon ($n=16$), and so on. Each doubling bisects the central angle, and each successive factor of the product is the cosine of the halved angle.

1. **First factor ($n=4$, square):** starting from $\cos(\pi/2)=0$,

$$
\cos\left(\frac{\pi}{4}\right)=\frac{\sqrt{2}}{2}.
$$

2. **Second factor ($n=8$, octagon):**

$$
\cos\left(\frac{\pi}{8}\right)=\frac{\sqrt{2+\sqrt{2}}}{2}.
$$

3. **Third factor ($n=16$):**

$$
\cos\left(\frac{\pi}{16}\right)=\frac{\sqrt{2+\sqrt{2+\sqrt{2}}}}{2}.
$$

The side lengths of the same polygons are governed by the sine twin: the inscribed square has side $\sqrt{2}$ (so $\sin(\pi/4)=\sqrt{2}/2$), the octagon has side $2\sin(\pi/8)=\sqrt{2-\sqrt{2}}$, and so on.

**Challenge:** Compute the fourth factor $\cos(\pi/32)$ as a nested radical and multiply the first four factors — the product should round to $0.6376$, just above the limit $2/\pi\approx 0.63662$. (The partial products approach the limit from above, since every factor is below $1$.)

---

## 3. The infinite product

Repeat the double-angle identity

$$
\sin x = 2\sin\left(\frac{x}{2}\right)\cos\left(\frac{x}{2}\right)
$$

$k$ times:

$$
\sin x = 2^k \sin\left(\frac{x}{2^k}\right) \prod_{j=1}^{k} \cos\left(\frac{x}{2^j}\right).
$$

Set $x=\pi/2$ and use $\sin(\pi/2)=1$:

$$
1 = 2^k \sin\left(\frac{\pi}{2^{k+1}}\right) \prod_{j=1}^{k} \cos\left(\frac{\pi}{2^{j+1}}\right),
$$

so

$$
\prod_{j=1}^{k} \cos\left(\frac{\pi}{2^{j+1}}\right) = \frac{1}{2^k \sin\left(\pi/2^{k+1}\right)}.
$$

As $k\to\infty$ the denominator tends to $\pi/2$, because $2^k\sin(\pi/2^{k+1})\to\pi/2$ — this is the sinc limit $\sin u/u\to 1$ in disguise. Hence

$$
\frac{2}{\pi} = \prod_{j=1}^{\infty} \cos\left(\frac{\pi}{2^{j+1}}\right) =
\frac{\sqrt{2}}{2}
\cdot
\frac{\sqrt{2+\sqrt{2}}}{2}
\cdot
\frac{\sqrt{2+\sqrt{2+\sqrt{2}}}}{2}
\cdots
$$

This is Viète's formula in cosine form — an infinite product of nested radicals.

**Challenge:** Verify the telescoping identity numerically: for $k=1,2,3$, check that $\prod_{j=1}^{k}\cos(\pi/2^{j+1})$ equals $1/(2^k\sin(\pi/2^{k+1}))$ to five decimals.

---

## 4. The limit formulation: Archimedes' insight

Archimedes bounded the circle between inscribed and circumscribed polygons; Viète's product is the inscribed half of that story, written multiplicatively. The perimeter of the inscribed regular $2^k$-gon in the unit circle is

$$
P_{2^k} = 2^{k+1}\sin\left(\frac{\pi}{2^k}\right),
$$

and the geometric limit is simply

$$
\lim_{k\to\infty} 2^{k+1}\sin\left(\frac{\pi}{2^k}\right) = 2\pi.
$$

Expanding $\sin(\pi/2^k)$ through repeated half-angle steps reproduces the product exactly. Polygon perimeters and nested radicals encode the same limit — one view geometric, one algebraic.

---

## 5. Deeper significance

Viète's product opened a lineage that runs through Wallis and Euler:

- It was the **first infinite product for π**, proving that π admits infinite expressions, not just finite approximations.
- Every partial product is a **constructible number** — angle bisection is a legal ruler-and-compass operation — a foretaste of Gauss's work on constructible polygons.
- Convergence is geometric with ratio $1/4$ per factor (see the series' third post), so each new factor buys about $0.6$ decimal digits — slow by modern standards, but each step costs only one square root.

**Connection table.** Viète's formula sits at the head of a family of early π formulas:

| Formula | Year | Structure | Convergence |
|---|---|---|---|
| Viète's product | 1593 | Infinite product of nested radicals | Geometric, ratio $1/4$ per factor ($\approx 0.6$ digits) |
| Wallis's product | 1656 | Infinite product of rationals | Error $O(1/n)$, very slow |
| Leibniz's series | 1674 | Alternating series | Error $O(1/n)$, very slow |
| Machin's formula | 1706 | Arctangent identity | Geometric, $\approx 1.4$ digits per term |

**Final challenge:** Iterate $\sin x = 2\sin(x/2)\cos(x/2)$ to prove the general product $\frac{\sin x}{x}=\prod_{k=1}^{\infty}\cos(x/2^k)$, then evaluate it at $x=\pi/6$. You should obtain an infinite product for $3/\pi$ — write down its first three factors.

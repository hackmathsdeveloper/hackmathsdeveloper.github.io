---
title: "The 4.6-Quintillion-Sided Polygon That Trapped π — Van Ceulen's 35-Digit Secret"
date: 2026-08-31
categories:
  - History of Mathematics
  - Mathematics
tags:
  - pi
  - van-ceulen
  - polygon-approximation
  - archimedean-bounds
  - ludolphine-number
  - numerical-history
share: true
read_time: true
excerpt: "Ludolph van Ceulen squeezed π between inscribed and circumscribed polygons all the way to a 2^62-gon — about 4.6 quintillion sides — and certified 35 decimal digits by hand. Here is the recurrence he ran, a modern reconstruction, and why 35 digits follow from an interval of width 10^-37."
---

**Challenge to the reader:** Verify the first squeeze by hand: the inscribed square in the unit circle gives $2\sqrt{2}\lt\pi$, the circumscribed square gives $\pi\lt 4$. Then compute the octagon bounds $a_8=8\sin(\pi/8)$ and $b_8=8\tan(\pi/8)$ and confirm the interval width is below $0.26$. (Both bounds are derived in §3.)

*Part of the Viète series: [Why π Lives Inside an Infinite Tower of Square Roots]({% post_url 2026-08-31-viete-formula-nested-radicals %}) · [Twenty Pattern Variations on Viète's Product]({% post_url 2026-08-31-viete-formula-twenty-variations %}).*

## The core theorem

**Van Ceulen's sandwich.** For every $n\ge 3$,

$$
n\sin\left(\frac{\pi}{n}\right) \lt \pi \lt n\tan\left(\frac{\pi}{n}\right),
$$

where the two bounds are the half-perimeters of regular $n$-gons inscribed in and circumscribed about the unit circle. At $n=2^{62}\approx 4.61\times10^{18}$ the interval between the bounds is narrower than $10^{-35}$ — which is how one man, working by hand, certified 35 digits of π.

**Why it matters.** No calculus, no machine, no convergence theorem — just bisected angles and square roots, each step turning a lower-and-upper bound into a tighter one. It is the purest demonstration that a rigorous decimal expansion of π needs only elementary geometry and enormous persistence. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Van_Ceulen/)

---

## 1. The geometric setup

Choose a circle of radius $r=1$; its circumference is $2\pi$. For a regular $n$-gon:

- The inscribed polygon lies inside the circle, so its perimeter $p_n$ is too small:

$$
p_n \lt 2\pi.
$$

- The circumscribed polygon lies outside the circle, so its perimeter $P_n$ is too large:

$$
2\pi \lt P_n.
$$

Thus

$$
p_n \lt 2\pi \lt P_n.
$$

Dividing by $2$ gives direct lower and upper bounds for $\pi$:

$$
n\sin\left(\frac{\pi}{n}\right) \lt \pi \lt n\tan\left(\frac{\pi}{n}\right).
$$

The formulae come from one of the $n$ congruent central triangles:

$$
p_n = 2n\sin\left(\frac{\pi}{n}\right), \qquad P_n = 2n\tan\left(\frac{\pi}{n}\right).
$$

Van Ceulen did not possess modern trigonometric notation in this form, but his chord and tangent calculations implement exactly these quantities.

---

## 2. Why doubling sides worked

The key operation was

$$
n \longrightarrow 2n.
$$

Instead of computing a new polygon from scratch, he bisected each central angle. If a side of the inscribed $n$-gon is a chord, then the side of the inscribed $2n$-gon is the chord of half the angle.

Modernly, if

$$
s_n = 2\sin\left(\frac{\pi}{n}\right)
$$

is the side length of the inscribed $n$-gon in a unit circle, then the side length after doubling is

$$
s_{2n} = \sqrt{2-\sqrt{4-s_n^2}}.
$$

This is the cosine half-angle formula in geometric disguise. To see it, write

$$
s_n = 2\sin\theta, \qquad \theta = \frac{\pi}{n}.
$$

Then

$$
s_{2n} = 2\sin\left(\frac{\theta}{2}\right) = \sqrt{2-2\cos\theta},
$$

and since

$$
\cos\theta = \sqrt{1-\sin^2\theta} = \sqrt{1-\frac{s_n^2}{4}},
$$

we get

$$
s_{2n} = \sqrt{2-\sqrt{4-s_n^2}}.
$$

So one square root operation turns the side length for an $n$-gon into that for a $2n$-gon.

For circumscribed polygons, the corresponding tangent-side recurrence is

$$
t_{2n} = \frac{2t_n}{\sqrt{4+t_n^2}+2},
$$

where

$$
t_n = 2\tan\left(\frac{\pi}{n}\right)
$$

is the side length of the circumscribed $n$-gon around a unit circle. In practical historical computation, variants based on semiperimeters, chords, and "sagittae" were often more convenient because they reduced the arithmetic burden.

**Challenge:** Starting from $s_4=\sqrt{2}$ and the recurrence, compute $s_8$ and $s_{16}$, and confirm they equal $2\sin(\pi/8)$ and $2\sin(\pi/16)$. Then apply the tangent recurrence to $t_4=2$ and check that $t_8=2(\sqrt{2}-1)$.

---

## 3. A modern reconstruction

One clean way to reproduce the method uses polygon half-perimeters directly. Let

$$
a_n = n\sin\left(\frac{\pi}{n}\right), \qquad b_n = n\tan\left(\frac{\pi}{n}\right).
$$

Then

$$
a_n \lt \pi \lt b_n.
$$

Start with an inscribed square and a circumscribed square:

$$
a_4 = 4\sin\left(\frac{\pi}{4}\right) = 2\sqrt{2} \approx 2.8284271247,
$$

$$
b_4 = 4\tan\left(\frac{\pi}{4}\right) = 4.
$$

Therefore,

$$
2.8284271247 \lt \pi \lt 4.
$$

After doubling to an octagon,

$$
a_8 = 8\sin\left(\frac{\pi}{8}\right) = 4\sqrt{2-\sqrt{2}} \approx 3.0614674589,
$$

$$
b_8 = 8\tan\left(\frac{\pi}{8}\right) = 8(\sqrt{2}-1) \approx 3.3137084990.
$$

Hence,

$$
3.0614674589 \lt \pi \lt 3.3137084990.
$$

**Challenge:** Compute $a_{16}=16\sin(\pi/16)$ and $b_{16}=16\tan(\pi/16)$ to four decimals and confirm that $\pi$ lies between them, with the interval width now below $0.08$.

---

## 4. How fast the bounds tighten

The interval narrows every time the number of sides doubles:

$$
4,\ 8,\ 16,\ 32,\ldots,\ 2^{62}.
$$

At a very large $n$, both expressions are extremely close to $\pi$:

$$
n\sin\left(\frac{\pi}{n}\right) \approx \pi - \frac{\pi^3}{6n^2},
$$

$$
n\tan\left(\frac{\pi}{n}\right) \approx \pi + \frac{\pi^3}{3n^2}.
$$

So the total width of the enclosure is approximately

$$
b_n - a_n \approx \frac{\pi^3}{2n^2}.
$$

For $n=2^{62}$, this is of order

$$
\frac{\pi^3}{2(2^{62})^2} \approx 7.3\times 10^{-37},
$$

which is comfortably narrower than $10^{-35}$. That is why a $2^{62}$-gon can certify about 35 decimal digits.

---

## 5. Relation to Viète's formula

Viète's formula results from tracking the same halving process multiplicatively. Starting with

$$
\sin x = 2\sin\left(\frac{x}{2}\right)\cos\left(\frac{x}{2}\right),
$$

and repeating the identity gives

$$
\sin x = 2^m \sin\left(\frac{x}{2^m}\right) \prod_{k=1}^{m} \cos\left(\frac{x}{2^k}\right).
$$

With $x=\pi/2$,

$$
1 = 2^m \sin\left(\frac{\pi}{2^{m+1}}\right) \prod_{k=1}^{m} \cos\left(\frac{\pi}{2^{k+1}}\right).
$$

As $m\to\infty$,

$$
2^m \sin\left(\frac{\pi}{2^{m+1}}\right) \longrightarrow \frac{\pi}{2},
$$

giving

$$
\frac{2}{\pi} = \prod_{k=1}^{\infty} \cos\left(\frac{\pi}{2^{k+1}}\right).
$$

Van Ceulen's polygon sequence and Viète's nested radicals therefore encode the same geometry:

| Aspect | Viète | Van Ceulen |
|---|---|---|
| Core operation | Halve a central angle | Double the number of polygon sides |
| Algebraic result | Product of half-angle cosines | Recursive chord/tangent computations |
| Geometric object | Inscribed polygon areas or perimeters | Explicit inner and outer polygon bounds |
| Output | An infinite product for $2/\pi$ | A certified decimal interval containing $\pi$ |
| Certainty | Convergence in the limit | A rigorous lower and upper bound at each finite stage |

---

## 6. The 35-digit result

The celebrated value is

$$
\pi \approx 3.14159265358979323846264338327950288.
$$

It became known in parts of Europe as the **Ludolphine number**. The digits were famously associated with van Ceulen's tombstone in Leiden; the original stone was lost, and a replacement was installed in 2000. [en.wikipedia](https://en.wikipedia.org/wiki/Ludolph_van_Ceulen)

Viète had published a 20-decimal value in *Van den Circkel* in 1596, using polygonal computation; van Ceulen's later work extended the result. The 35-digit result was completed before van Ceulen's death in 1610, but the full value appeared posthumously in Willebrord Snellius's *Cyclometricus* in 1621; a 1615 posthumous publication reported 33 digits. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Van_Ceulen/)

---

## 7. Why it still matters

What made this extraordinary was not a new shortcut, but the scale and reliability of the hand computation. Each doubling required high-precision square-root extraction, multiplication, division, and careful control of lower and upper bounds. Doing that repeatedly — without electronic calculation, modern decimal arithmetic, or symbolic trigonometric notation — over decades was an immense computational achievement.

It also fixed the meaning of "a decimal expansion of π": not a claim about a limiting object, but a certified interval, valid at every finite stage. Every modern rigorous computation of π inherits that discipline, even if its engines are Ramanujan-type series instead of polygons.

**Final challenge:** From the width estimate $\pi^3/(2n^2)$, solve for the side count $n$ needed to certify $d$ decimal digits, and show that $d=35$ requires $n\gt\sqrt{\pi^3/2}\cdot 10^{17.5}\approx 1.2\times10^{18}$ — the scale of van Ceulen's $2^{62}\approx 4.6\times10^{18}$-gon. Sanity check: does your formula reproduce the octagon stage, where $n=8$ certifies only one digit?

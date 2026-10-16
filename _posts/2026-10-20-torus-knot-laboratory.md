---
title: "The Torus Knot Laboratory: An Interactive Playground"
date: 2026-10-20
categories:
  - Knot Theory
  - Mathematics
tags:
  - torus-knots
  - interactive
  - javascript
  - visualization
  - crossing-number
  - knot-genus
share: true
read_time: true
excerpt: "The final part of the series is a self-contained interactive laboratory: nine torus knots as shaded 3D tubes, rotatable and zoomable, with live winding numbers, component counts, crossing numbers, and genera — all computed from the one equation of Part 4."
---

**Challenge to the reader:** In the laboratory below, set $p=8$, $q=6$ and confirm the component count from Part 4. Then compare $T(5,2)$ with $T(2,5)$ — the same knot in two embeddings. Why does swapping $p$ and $q$ keep the knot type fixed?

*Part 5 of five in the series **From Weaving Mathematics to Torus Knots**: [Part 1 — The Mathematics Hidden in a Weave]({% post_url 2026-10-16-weaving-mathematics %}) · [Part 2 — From Fabric to Knot Theory: A Weave Is a Link on a Torus]({% post_url 2026-10-17-weaving-and-knots %}) · [Part 3 — Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement]({% post_url 2026-10-18-torus-knots-versus-weaving-knots %}) · [Part 4 — Constructing the Torus Knot: Two Circular Motions, One Equation]({% post_url 2026-10-19-torus-knot-construction %}) · Part 5 — The Torus Knot Laboratory: An Interactive Playground (this page).*

The laboratory below is the finished instrument for the equation of Part 4:

$$
\boxed{
\begin{aligned}
x(t)&=\bigl(R+r\cos(pt)\bigr)\cos(qt),\\
y(t)&=\bigl(R+r\cos(pt)\bigr)\sin(qt),\\
z(t)&=r\sin(pt),
\end{aligned}
\qquad 0\le t\le 2\pi
}
$$

Every visual in it is computed from this formula — the tubes are triangle meshes swept around the centerline, sorted by depth and shaded, with no external libraries. It is self-contained: open it in any modern browser without installing anything.

<div style="border:1px solid #2b3857;border-radius:14px;overflow:hidden;margin:18px 0">
<iframe src="/torus-knot-laboratory.html" title="Torus Knot Laboratory" style="width:100%;height:1250px;border:0;display:block" loading="lazy"></iframe>
</div>

The page is embedded above; it is also available as a standalone page: [torus-knot-laboratory.html](/torus-knot-laboratory.html) (open in a new tab for a larger view).

## What the laboratory includes

- All nine preset knots from Part 4's table: $(3,2)$, $(4,3)$, $(5,2)$, $(5,3)$, $(5,4)$, $(7,2)$, $(7,4)$, $(8,5)$, and $(8,7)$.
- Shaded 3D tubes with drag-to-rotate, scroll/pinch-to-zoom, and automatic rotation.
- Adjustable winding numbers $p$, $q$, torus radii $R$, $r$, and strand thickness.
- A translucent supporting torus, a mirror toggle, and PNG export.
- Computed component counts, minimal crossing numbers, and knot genus.
- An embedded explanation of the equations.

## Experiments to try

1. **Coprimality.** Keep $p=3$, $q=2$ (one component); then try $p=4$, $q=2$ — the lab generates all $\gcd(p,q)=2$ components explicitly, instead of retracing one curve twice.
2. **$T(p,q)$ versus $T(q,p)$.** Compare $T(5,2)$ and $T(2,5)$: different silhouettes, the same knot type (Part 4, Section 3).
3. **Geometry versus topology.** Drag $R$ and $r$ around: the knot changes shape but never type, as long as $R>r>0$.
4. **Mirror.** Toggle the mirror and compare the two chiral versions.
5. **Degenerate cases.** Set $p=1$ or $q=1$: the curve is an unknot.
6. **The camera does not count crossings.** Compare the *minimal* crossing number in the stats panel with the overlaps visible from your current viewpoint.

## The arc of the series

Each part contributed one equation to the same object:

| Part | Equation | What it did |
|---|---|---|
| 1 | $A_{ij}=(j-si)\bmod n\in S$, $r=n/\gcd(n,s)$ | Encoded a weave as a binary matrix; modular arithmetic set the repeat length |
| 2 | $A_{ij}\mapsto \rho=r+\varepsilon\sigma(i,j)$ on $T^2\times[0,1]$ | Turned the matrix into over–under geometry: a link on a torus |
| 3 | $T(p,q)=\overline{(\sigma_1\cdots\sigma_{p-1})^q}$, $W(p,q)=\overline{(\sigma_1\sigma_2^{-1}\cdots)^q}$ | Same shadow, different signs: two different knots |
| 4 | $(R+r\cos pt)(\cos qt,\sin qt)$, $z=r\sin pt$ | Built $T(p,q)$ from two synchronized circular motions |
| 5 | the same equation, rendered | Made it something you can hold and turn |

A cloth, a link diagram, and a torus knot are the same object at three different zoom levels: a matrix of crossings, its closure on a torus, and a curve wound around that torus.

---

**Final challenge:** With the lab's PNG export, produce side-by-side images of $T(8,7)$ and $T(7,8)$, then verify from the images alone that both have genus $21$ and minimal crossing number $48$ — and explain why the pictures cannot prove it.

*End of the series **From Weaving Mathematics to Torus Knots**. Return to [Part 1 — The Mathematics Hidden in a Weave]({% post_url 2026-10-16-weaving-mathematics %}) to review the whole arc.*

*References for the curious reader: the [torus knot](https://en.wikipedia.org/wiki/Torus_knot) article on Wikipedia; [Wolfram MathWorld](https://mathworld.wolfram.com/TorusKnot.html); the weaving-knot papers from Part 3 ([arXiv:1506.04139](https://arxiv.org/abs/1506.04139), [arXiv:1704.03982](https://arxiv.org/abs/1704.03982)).*

---
title: "Four Octagons, One Vertex, 540° — The Tiling That Broke Flat Space"
date: 2026-10-23
categories:
  - Tiling Theory
  - Mathematics
tags:
  - regular-tessellations
  - schlafli-symbol
  - hyperbolic-geometry
  - angle-defect
  - gauss-bonnet
  - poincare-disk
  - curvature
share: true
read_time: true
excerpt: "Four regular octagons meeting at a vertex demand 540° on flat paper, so the {8,4} tiling is impossible in the Euclidean plane. In hyperbolic space each octagon can be right-angled, and Gauss–Bonnet fixes its area at exactly 2π. This is the curvature trichotomy behind every regular tessellation."
---

**Challenge to the reader:** Place four regular octagons around one shared vertex and add up their interior angles. Before reading Section 2, decide whether the $\lbrace 8,4\rbrace$ tiling can live on a flat sheet, a sphere, or a saddle — then check your verdict against the sign of $1/p+1/q-1/2$.

*Part 1 of four in the series **The Shape of the Possible: Tilings, Curvature, and Construction**: Part 1 — Four Octagons, One Vertex, 540° (this page) · [Part 2 — The 81 Ways to Tile a Plane]({% post_url 2026-10-23-two-orbit-tilings-81-isohedral-types %}) · [Part 3 — The Sevenfold Tiling Flat Paper Forbids]({% post_url 2026-10-23-sevenfold-hyperbolic-tiling %}) · [Part 4 — Why 60° Refuses to Be Cut in Three]({% post_url 2026-10-23-why-60-degrees-cannot-be-trisected %}).*

A regular tessellation is a tiling by congruent regular polygons with the same number of tiles meeting at every vertex. It is encoded by the Schläfli symbol $\lbrace p,q\rbrace$: $p$ is the number of sides of each tile, and $q$ is the number of tiles around each vertex.

The entire classification rests on one comparison. With $p$-gons meeting $q$ at a time, the tiling exists precisely when

$$
\boxed{
\frac{1}{p}+\frac{1}{q}
\begin{cases}
  \gt \frac{1}{2}, & \text{spherical geometry},\\
  = \frac{1}{2}, & \text{Euclidean geometry},\\
  \lt \frac{1}{2}, & \text{hyperbolic geometry}.
\end{cases}}
$$

**Why it matters.** This inequality is the complete answer to "which regular tessellations exist?" It explains why the same combinatorial symbol can be impossible on paper, possible on a sphere, and unavoidable on a saddle. It also turns curvature into an angle budget that you can compute by hand.

---

## 1. The vertex budget

Start with a regular $p$-gon. Its interior angles sum to $(p-2)\pi$, so each angle is

$$
A_p=\frac{(p-2)\pi}{p}=\pi\left(1-\frac{2}{p}\right).
$$

If $q$ such polygons meet at a vertex, the total angle there is

$$
S=qA_p=q\pi\left(1-\frac{2}{p}\right).
$$

For the tiling to close without overlap or gap in the Euclidean plane, the budget must balance exactly:

$$
S=2\pi.
$$

Substitute and simplify:

$$
q\pi\left(1-\frac{2}{p}\right)=2\pi
\quad\Longrightarrow\quad
q(p-2)=2p
\quad\Longrightarrow\quad
(p-2)(q-2)=4.
$$

The positive integer factorisations of $4$ give the three Euclidean solutions:

| $(p-2)(q-2)$ | $p$ | $q$ | Tiling |
|---|---|---|---|
| $1\cdot 4$ | $3$ | $6$ | triangular |
| $2\cdot 2$ | $4$ | $4$ | square |
| $4\cdot 1$ | $6$ | $3$ | hexagonal |

**Challenge.** List every integer pair $p,q\ge 3$ with $1/p+1/q \gt 1/2$. How many spherical regular tessellations does your list produce?

---

## 2. The 540° verdict

For $\lbrace 8,4\rbrace$, the Euclidean interior angle is

$$
A_8=\frac{(8-2)\pi}{8}=\frac{3\pi}{4}=135^\circ.
$$

Four of them contribute

$$
S=4\cdot 135^\circ=540^\circ.
$$

That is $180^\circ$ too much. The four octagons overlap; no flat arrangement can avoid it. In fact three octagons already contribute $405^\circ$, so even $\lbrace 8,3\rbrace$ fails in the Euclidean plane.

There is no escape by choosing a different $q$: the Euclidean condition $1/8+1/q=1/2$ gives $q=8/3$, not an integer. **No regular octagon tiles the Euclidean plane at all.**

The subtlety is *regularity*, not the number eight. Irregular octagons tile the plane easily. A regular octagon is rigid: once its side length is fixed, every interior angle is forced to $135^\circ$. Curvature is what relaxes that rigidity.

---

## 3. Curvature changes the angle budget

On a sphere, a polygon's angles sum to more than the Euclidean value; in the hyperbolic plane, they sum to less. A regular $p$-gon in the hyperbolic plane can therefore be made *thin*: as its vertices move outward toward the ideal boundary, its interior angle decreases continuously from the Euclidean value $\pi(1-2/p)$ toward $0$.

This gives an existence proof. To build $\lbrace p,q\rbrace$ in the hyperbolic plane, we need each tile to have angle exactly

$$
A=\frac{2\pi}{q}.
$$

A regular hyperbolic $p$-gon realizes every angle between $0$ and $\pi(1-2/p)$. So the required angle is available precisely when

$$
\frac{2\pi}{q} \lt \pi\left(1-\frac{2}{p}\right),
$$

which rearranges to

$$
\frac{1}{p}+\frac{1}{q} \lt \frac{1}{2}.
$$

For $\lbrace 8,4\rbrace$, the required angle is $2\pi/4=\pi/2=90^\circ$, comfortably below the Euclidean $135^\circ$. The hyperbolic octagon can be right-angled, and four right angles fit around a vertex exactly.

**Challenge.** Compare $\lbrace 5,4\rbrace$ (pentagons, four per vertex) with $\lbrace 5,3\rbrace$ (pentagons, three per vertex). Which required angle is smaller than the Euclidean pentagon angle, and which is larger? Which tiling is hyperbolic and which is spherical?

---

## 4. Gauss–Bonnet fixes the area

The angle deficit of one tile is the difference between its Euclidean angle sum and its actual angle sum:

$$
\Delta_p = (p-2)\pi - p\cdot\frac{2\pi}{q}.
$$

Gauss–Bonnet says this deficit *is* the hyperbolic area of the tile (for curvature $-1$):

$$
\operatorname{Area}(\lbrace p,q\rbrace)
  = \pi p\left(1-\frac{2}{p}-\frac{2}{q}\right).
$$

For the right-angled octagon:

$$
\operatorname{Area}(\lbrace 8,4\rbrace)
  = 8\pi\left(1-\frac{1}{4}-\frac{1}{2}\right)
  = 2\pi.
$$

For the heptagonal tiling of Part 3:

$$
\operatorname{Area}(\lbrace 7,3\rbrace)
  = 7\pi\left(1-\frac{2}{7}-\frac{2}{3}\right)
  = \frac{\pi}{3}.
$$

The formula is positive exactly when $1/p+1/q \lt 1/2$. In the Euclidean case the deficit is zero; in the spherical case it is negative, and the same computation becomes the spherical angle excess. The sign of the defect is the sign of the curvature.

**Challenge.** Compute the area of a $\lbrace 5,4\rbrace$ pentagon and a $\lbrace 4,5\rbrace$ square. Which is larger? Check both against the sign of $1/p+1/q-1/2$.

---

## 5. Why the Poincaré disk looks warped

The hyperbolic plane cannot be drawn on a flat screen without distortion. The Poincaré disk model puts the entire plane inside the unit disk and represents geodesics as diameters and circular arcs orthogonal to the boundary. Its metric is

$$
ds^2=\frac{4\,(dx^2+dy^2)}{(1-x^2-y^2)^2}.
$$

The metric is a positive scalar multiple of the Euclidean metric at every point. That is what *conformal* means: angles are preserved, even though lengths and areas are not. Near the boundary the scale factor blows up, so the tiles appear to shrink; the tiling continues forever inside a finite circle.

At every vertex of the $\lbrace 8,4\rbrace$ tiling, the four drawn angles really are $90^\circ$. The warping is a distortion of the *drawing*, not of the hyperbolic tiling.

The Klein model makes the opposite trade. Geodesics become straight Euclidean chords, which is convenient for drawing, but the model is not conformal: the angles you see are not the hyperbolic angles. A regular hyperbolic octagon drawn in the Klein model has straight sides, yet its apparent corner angles are distorted. Conformality is a property of the projection, not a property of the space. What makes the tiling possible is curvature; what makes it look a certain way is the map.

---

## 6. The full trichotomy

The table compares the required angle $2\pi/q$ with the Euclidean angle $\pi(1-2/p)$. If the required angle is larger, the tile must be spherical; if equal, Euclidean; if smaller, hyperbolic.

| Symbol | Tile | $q$ | Required $2\pi/q$ | Euclidean angle | Geometry |
|---|---|---|---|---|---|
| $\lbrace 3,3\rbrace$ | triangle | 3 | $120^\circ$ | $60^\circ$ | spherical |
| $\lbrace 3,4\rbrace$ | triangle | 4 | $90^\circ$ | $60^\circ$ | spherical |
| $\lbrace 3,5\rbrace$ | triangle | 5 | $72^\circ$ | $60^\circ$ | spherical |
| $\lbrace 4,3\rbrace$ | square | 3 | $120^\circ$ | $90^\circ$ | spherical |
| $\lbrace 5,3\rbrace$ | pentagon | 3 | $120^\circ$ | $108^\circ$ | spherical |
| $\lbrace 3,6\rbrace$ | triangle | 6 | $60^\circ$ | $60^\circ$ | Euclidean |
| $\lbrace 4,4\rbrace$ | square | 4 | $90^\circ$ | $90^\circ$ | Euclidean |
| $\lbrace 6,3\rbrace$ | hexagon | 3 | $120^\circ$ | $120^\circ$ | Euclidean |
| $\lbrace 7,3\rbrace$ | heptagon | 3 | $120^\circ$ | $128.571^\circ$ | hyperbolic |
| $\lbrace 8,4\rbrace$ | octagon | 4 | $90^\circ$ | $135^\circ$ | hyperbolic |
| $\lbrace 5,4\rbrace$ | pentagon | 4 | $90^\circ$ | $108^\circ$ | hyperbolic |
| $\lbrace 4,5\rbrace$ | square | 5 | $72^\circ$ | $90^\circ$ | hyperbolic |
| $\lbrace 3,7\rbrace$ | triangle | 7 | $51.429^\circ$ | $60^\circ$ | hyperbolic |

The five spherical rows are the Platonic solids: tetrahedron, octahedron, icosahedron, cube, and dodecahedron. The three Euclidean rows are the only regular tilings of the flat plane. The hyperbolic rows continue forever: every pair with $1/p+1/q \lt 1/2$ gives one.

---

## 7. Deeper significance

The trichotomy is not a curiosity about polygons. It is the two-dimensional case of a general principle: curvature is an angle budget, and the sign of the budget decides which regular structures fit.

Three consequences are worth carrying forward.

- **Regular polygons that tile flatly are rare.** Only triangles, squares, and hexagons tile the Euclidean plane regularly. The hyperbolic plane admits infinitely many regular tilings, one for every pair with $1/p+1/q \lt 1/2$.
- **The Euclidean census is not the whole census.** Part 2 counts the 81 isohedral symmetry types of the Euclidean plane. Hyperbolic space has infinitely many regular examples before any classification begins.
- **Construction is a separate question.** A regular heptagon cannot be built with compass and straightedge, yet the $\lbrace 7,3\rbrace$ hyperbolic tiling exists. Part 4 explains why the operation set, not the angle, is the real obstruction.

The same angle-defect idea scales upward: in three dimensions, the Schläfli symbol $\lbrace p,q,r\rbrace$ and the sign of a curvature sum classify regular honeycombs. The bookkeeping gets heavier; the principle does not.

---

## Final challenge

Find every regular tiling $\lbrace p,q\rbrace$ whose tiles have hyperbolic area exactly $\pi/2$. Start from

$$
\pi p\left(1-\frac{2}{p}-\frac{2}{q}\right)=\frac{\pi}{2},
$$

solve for $q$ in terms of $p$, and use $q\ge 3$ to bound $p$. There are exactly two solutions; one uses triangles and one uses pentagons.

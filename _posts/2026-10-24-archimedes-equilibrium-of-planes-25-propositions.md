---
title: "The Lever Law That Became a Geometry Machine — 25 Propositions That Find Every Centre of Gravity"
date: 2026-10-24 06:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - on-the-equilibrium-of-planes
  - law-of-the-lever
  - centre-of-gravity
  - centroid
  - archimedes
  - mechanics
  - ancient-geometry
share: true
read_time: true
excerpt: "On the Equilibrium of Planes contains 25 propositions: the law of the lever, the centroids of triangles, parallelograms and trapeziums, and the parabolic centroids of Book II. This is the complete proposition-by-proposition guide."
---

**Challenge to the reader:** Two weights, $6$ and $4$, balance on a beam. If the heavier weight is $2$ units from the fulcrum, where is the lighter weight? Then explain why the answer does not depend on the units, only on the inverse ratio.

*Part 6 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · **Part 6 — Equilibrium I** (this page) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

*On the Equilibrium of Planes*, also known as *On the Centres of Gravity of Planes*, contains 25 propositions in two books: 15 in Book I and 10 in Book II. Book I develops the law of the lever and the centres of gravity of rectilinear figures. Book II determines the centres of gravity of parabolic segments and portions cut off between parallel chords.

The central relation is the law of the lever:

$$
\boxed{W_1d_1=W_2d_2.}
$$

**Why it matters.** This is not only a statement about physical balance. It is a machine for computing areas and centroids. Archimedes uses it to turn geometric figures into weights, to combine and subtract them, and eventually to find the centre of gravity of a curved parabolic region. The same law powers the mechanical proof of the quadrature of the parabola in Part 2.

---

## 1. The postulates

Book I begins with seven postulates. They are not additional proved propositions; they define the framework.

1. Equal weights balance at equal distances; at unequal distances, the farther equal weight prevails.
2. Adding weight to one side of an equilibrium makes that side prevail.
3. Removing weight from one side makes the other side prevail.
4. Congruent plane figures have coincident centres of gravity when superposed.
5. Similar figures have similarly situated centres of gravity.
6. Equal magnitudes can replace balancing magnitudes at the same distances without disturbing equilibrium.
7. The centre of gravity of a convex figure lies inside it.

The fifth postulate is the one that lets Archimedes transfer a centroid result from one triangle to another similar triangle. The sixth lets him replace a figure by an equal-area figure at the same position. Both are used repeatedly.

---

## 2. The law of the lever: Propositions 1–7

### Propositions 1–3: the basic balance relations

- **I.1.** If two weights balance at equal distances, the weights are equal.
- **I.2.** At equal distances, unequal weights do not balance; the heavier prevails.
- **I.3.** If unequal weights balance, the heavier is nearer the fulcrum.

These establish the direction of the relationship before its exact ratio is proved.

### Propositions 4–5: combining equal magnitudes

- **I.4.** The centre of gravity of two equal magnitudes lies at the midpoint of the segment joining their individual centres.
- **I.5.** If three equal magnitudes have collinear, equally spaced centres, their combined centre is the centre of the middle magnitude.

I.5 has two explicit generalizations:

- **Odd number:** if the centres are equally spaced and magnitudes equally far from the middle are equal, the combined centre is the middle centre.
- **Even number:** under the corresponding paired-equality and equal-spacing conditions, the combined centre is the midpoint between the two middle centres.

### Propositions 6–7: the lever law

For commensurable magnitudes,

$$
\boxed{
\frac{d_1}{d_2}=\frac{W_2}{W_1},
\qquad\text{or}\qquad
W_1d_1=W_2d_2.
}
$$

Proposition 7 extends the same inverse-proportion rule to incommensurable magnitudes. The extension is not automatic: it requires an exhaustion argument comparing the incommensurable ratio with rational approximations.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p6-lever.svg' | relative_url }}" alt="A balance beam with a weight of 2 at distance 3 on the left and a weight of 3 at distance 2 on the right, illustrating W1 d1 equals W2 d2.">
<figcaption>The law of the lever. The heavier weight sits at the shorter distance; the products $W_1d_1$ and $W_2d_2$ are equal.</figcaption>
</figure>

**Mid-post challenge.** Two weights, $6$ and $4$, balance. If the heavier is $2$ units from the fulcrum, find the distance of the lighter. Then reverse the question: if the lighter is $3$ units from the fulcrum, where is the heavier?

---

## 3. Combining and subtracting: Proposition 8

Proposition 8 is the subtraction principle. If a part is removed from a magnitude and its centre differs from that of the whole, the centre of the remainder lies on the line joining those two centres, extended beyond the centre of the whole, away from the removed part.

If the whole has weight $W$ and centre $G$, and the removed part has weight $w$ and centre $P$, then the remainder's centre $R$ satisfies

$$
\boxed{
\frac{GR}{GP}=\frac{w}{W-w}.
}
$$

In modern vector notation,

$$
\boxed{
\mathbf r_R
=
\frac{W\mathbf r_G-w\mathbf r_P}{W-w}.
}
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p6-subtraction.svg' | relative_url }}" alt="An L-shaped remainder of a 6 by 4 rectangle after removing a 2 by 2 square, with the whole centroid G, the removed part centroid P, and the remainder centroid R on the line through them.">
<figcaption>Proposition I.8. A $2\times2$ square is removed from the corner of a $6\times4$ rectangle. The whole centroid is $G$, the removed part's centroid is $P$, and the remainder's centroid $R$ lies on the line $PG$ extended, with $GR/GP=w/(W-w)$.</figcaption>
</figure>

This subtraction principle is central to the later centroid constructions. It lets Archimedes build a complicated figure from simpler ones, or remove a piece and track the centre of what remains.

**Mid-post challenge.** For the L-shape in the figure, the whole rectangle has area $24$ and centroid $G=(3,2)$; the removed $2\times2$ square has area $4$ and centroid $P=(5,1)$. Use the vector formula to find $R$, and verify that $GR/GP=1/5$.

---

## 4. Centroids of rectilinear figures: Propositions 9–15

### Propositions 9 and 10: the parallelogram

The centre of gravity of a parallelogram lies on the line joining the midpoints of either pair of opposite sides (I.9). It is the intersection of the diagonals (I.10).

### Propositions 11 and 12: similar triangles

If two triangles are similar and two points occupy corresponding positions, then if one point is the centre of gravity of its triangle, the other is the centre of gravity of the other triangle (I.11). If the centre of one triangle lies on a median, the centre of the similar triangle lies on the corresponding median (I.12).

These are preparatory. They let Archimedes prove the median property for a general triangle by reducing it to a convenient similar triangle.

### Propositions 13 and 14: the triangle

In any triangle, the centre of gravity lies on the line joining a vertex to the midpoint of the opposite side (I.13). The centre is the common intersection of the three medians (I.14), and it divides each median in the ratio

$$
\boxed{VG:GM=2:1,}
$$

where $V$ is the vertex and $M$ the midpoint of the opposite side.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p6-triangle.svg' | relative_url }}" alt="A triangle with all three medians drawn, their intersection G, and labels showing CG to GM equals 2 to 1.">
<figcaption>Propositions I.13–I.14. The three medians meet at $G$, and $G$ divides each median in the ratio $2:1$ from the vertex.</figcaption>
</figure>

**Mid-post challenge.** For the triangle with vertices $(0,0)$, $(6,0)$, and $(2,5)$, compute the centroid directly as the average of the vertices. Then find the midpoint $M$ of the side opposite $C=(2,5)$ and verify that $CG:GM=2:1$.

### Proposition 15: the trapezium

For a quadrilateral with two parallel sides, the centre lies on the segment joining the midpoints of those sides. Let the parallel sides have lengths $B>b$, with midpoints $M_B,M_b$. Then

$$
\boxed{
\frac{M_bG}{GM_B}
=
\frac{2B+b}{B+2b}.
}
$$

Equivalently, if their perpendicular separation is $h$, the centroid's perpendicular distance from the larger base is

$$
\boxed{
\bar y=\frac{h(B+2b)}{3(B+b)}.
}
$$

The centroid lies closer to the larger parallel side.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p6-trapezoid.svg' | relative_url }}" alt="A trapezium with parallel sides 6 and 3 and height 4, its midline, and the centroid dividing the midline in the ratio 5 to 4.">
<figcaption>Proposition I.15. The centroid lies on the midline. For $B=6$, $b=3$, $h=4$, the distance from the larger base is $16/9$, and $M_bG:GM_B=5:4$.</figcaption>
</figure>

**Mid-post challenge.** A trapezium has parallel sides $B=6$ and $b=3$ and height $h=4$. Compute $\bar y$ from the larger base and the ratio $M_bG:GM_B$. Check that your two answers are consistent.

---

## 5. Book II: the parabolic centroids

Book II contains ten propositions devoted to parabolic segments. The central result is Proposition II.8:

$$
\boxed{VG:GM=3:2,}
$$

where $V$ is the segment's vertex and $M$ is the midpoint of its chord. In modern terms, the centroid of the parabolic segment lies three fifths of the way from the vertex to the base, or two fifths of the height above the base.

Proposition II.10 extends the result to the portion of a parabola between two parallel chords. If the smaller and larger chord lengths are $s$ and $L$, and $H$ is the distance between their midpoints, then the centroid lies inside the middle fifth of the diameter and satisfies

$$
\boxed{
\frac{PG}{GQ}
=
\frac{L^2(2s+L)}{s^2(2L+s)}.
}
$$

Part 7 reconstructs all ten propositions, including the polygonal approximation that proves them. Here it is enough to note the pattern: Book I supplies the lever and the centroids of rectilinear figures; Book II applies them, through exhaustion, to a curved region.

---

## 6. Why the work matters

*On the Equilibrium of Planes* is the first systematic theory of centres of gravity. It introduces the idea that a extended body can be replaced by a point mass at its centroid for the purpose of balance. It proves the lever law for commensurable and incommensurable magnitudes. It finds the centroids of the parallelogram, the triangle, and the trapezium. And it sets up the machinery that Book II uses to find the centroid of a parabolic segment.

The work is also a bridge between physics and mathematics. The lever is a physical principle; the centroid is a geometric point. Archimedes uses the physical principle to prove geometric theorems, and the geometric theorems to compute physical centres. The two subjects are not separate.

---

## Final challenge

Use Proposition I.8 to find the centroid of the L-shape obtained by removing a $2\times2$ square from the corner of a $6\times4$ rectangle. Then verify your answer with the vector formula

$$
\mathbf r_R=\frac{W\mathbf r_G-w\mathbf r_P}{W-w}.
$$

Finally, explain why the subtraction principle is necessary for the parabolic centroid in Book II. What figure is being removed, and what remains?

*Next in the series: [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) gives the ten propositions of Book II the detailed treatment they deserve, including the odd-number ratios, the polygon centroids, and the middle-fifth theorem.*

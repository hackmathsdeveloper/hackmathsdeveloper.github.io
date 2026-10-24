---
title: "The Centre of Gravity Hiding in a Parabola — Archimedes' Ten-Proposition Finale"
date: 2026-10-24 05:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - on-the-equilibrium-of-planes
  - book-ii
  - parabolic-segment
  - centroid
  - method-of-exhaustion
  - archimedes
  - mechanics
share: true
read_time: true
excerpt: "Book II of On the Equilibrium of Planes contains ten propositions on the centres of gravity of parabolic segments. This is the detailed reconstruction, from the odd-number polygon ratios to the middle-fifth theorem for a portion between parallel chords."
---

**Challenge to the reader:** For the parabolic segment bounded by $y=1-x^2$ and $y=0$, compute the centroid directly by integration. You should find $\bar y=2/5$. Then verify that the segment's vertex $V=(0,1)$ and the chord midpoint $M=(0,0)$ satisfy $VG:GM=3:2$.

*Part 7 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · **Part 7 — Equilibrium II** (this page) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

Book II of *On the Equilibrium of Planes* contains ten propositions. All of them are about one subject: the centre of gravity of a parabolic segment, and of the portion of a parabolic segment cut off between two parallel chords.

The culminating result is Proposition II.8:

$$
\boxed{VG:GM=3:2,}
$$

where $V$ is the vertex of the segment and $M$ is the midpoint of its chord. Equivalently,

$$
VG=\frac35\,VM,
\qquad
MG=\frac25\,VM.
$$

The centroid lies three fifths of the way from the vertex to the base.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p6-parabola-centroid.svg' | relative_url }}" alt="The parabolic segment bounded by y equals one minus x squared and the x-axis, its diameter VM, and the centroid G dividing the diameter in the ratio 3 to 2.">
<figcaption>Proposition II.8. The centroid $G$ lies on the diameter $VM$, with $VG=3/5\,VM$ and $GM=2/5\,VM$.</figcaption>
</figure>

**Why it matters.** Book I found the centroids of triangles, parallelograms, and trapeziums by finite decomposition. Book II does the same for a curved region. The method is exhaustion: approximate the parabolic segment by inscribed polygons whose centroids can be computed, prove that those centroids approach a unique point, and show that the point is the segment's centre of gravity.

---

## 1. A note on the text

Some popular summaries describe Book II as a sequence of problems about a parabolic segment suspended from a point on its axis, base, or curve. That is not the content of the Greek Book II. The ten propositions of Book II concern the centres of gravity of parabolic regions and of portions between parallel chords. The suspension problems belong to a different tradition of paraphrase.

This post follows the Greek text. The distinction matters because the actual Book II is a rigorous exercise in the exhaustion method, not a collection of statics exercises.

---

## 2. The equal-area replacement: Proposition II.1

Book II begins with a result about combining two parabolic segments. For two segments whose areas can be applied to a given straight line, the centre of gravity of their combination lies on the segment joining their individual centres, dividing it inversely as their areas.

For areas $A_1,A_2$, with centres $G_1,G_2$, the combined centre $G$ satisfies

$$
\boxed{
\frac{G_1G}{GG_2}=\frac{A_2}{A_1}.
}
$$

The proof replaces each parabolic segment by a rectangle of equal area. This is the technique that makes the whole book possible: a curved region is replaced by a rectilinear region whose centroid is already known, and the balance law does the rest.

The replacement preserves area, not shape. That is enough for the balance argument, because the moment of a uniform lamina depends on its area and its centroid, not on its outline.

---

## 3. The inscribed polygon: Proposition II.2

Archimedes uses a particular sequence of inscribed polygons. Begin with the triangle having the segment's base and height. Then add analogous triangles in each remaining parabolic segment, and repeat.

The key result is that the centre of gravity of every polygon inscribed by this construction lies on the **diameter** of the parabolic segment — the line from the chord midpoint to the segment vertex.

The introductory observations also establish two geometric facts:

- the chords joining paired polygon vertices are parallel to the original base and are bisected by the diameter;
- at successive construction levels, the subdivisions of the diameter follow odd-number ratios, such as $1:3:5:7$.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p7-polygon.svg' | relative_url }}" alt="A parabolic segment with an inscribed polygon whose vertices lie on the parabola, horizontal chords, and diameter intervals labelled in the ratios 7 to 5 to 3 to 1 from the base to the vertex.">
<figcaption>Proposition II.2. The inscribed polygon's vertices lie on the parabola; the horizontal chords are bisected by the diameter; the successive diameter intervals are in odd-number ratios. For this third-generation polygon, the intervals from base to vertex are $7:5:3:1$.</figcaption>
</figure>

**Mid-post challenge.** For the polygon with vertices at

$$
x=0,\ \pm\frac14,\ \pm\frac12,\ \pm\frac34,\ \pm1
$$

on $y=1-x^2$, compute the heights of the horizontal chords and show that the diameter intervals are in the ratio $1:3:5:7$ (from the vertex down, or $7:5:3:1$ from the base up).

---

## 4. Similar segments and the diameter: Propositions II.3–II.4

### Proposition II.3

For two similar parabolic segments, construct the prescribed inscribed polygons with the same number of sides. Their centres of gravity divide the respective diameters in the same ratio.

This is the parabolic analogue of Book I's similarity postulate. Similar figures have similarly situated centroids.

### Proposition II.4

The centre of gravity of every parabolic segment lies on its diameter. The result extends the polygon result to the entire curved region.

The proof is an exhaustion argument. Every inscribed polygon has its centroid on the diameter. The segment's centroid must lie on the same line, because the polygons can be made arbitrarily close to the segment.

---

## 5. The polygon centroids approach the segment centroid: Propositions II.5–II.6

### Proposition II.5

The centre of gravity of the complete parabolic segment lies **nearer its vertex** than the centre of gravity of any polygon inscribed by the prescribed construction.

This is the monotonicity step. Each inscribed polygon leaves out the curved slivers near the vertex; its centroid is therefore pulled toward the base. The segment's centroid is higher.

### Proposition II.6

Given any positive length, however small, one can construct an inscribed polygon whose centre of gravity is closer than that length to the centre of gravity of the parabolic segment:

$$
\boxed{
\text{for every }\varepsilon>0,\quad
\text{an inscribed polygon exists with }
\lvert G_{\mathrm{polygon}}G\rvert<\varepsilon.
}
$$

This is a rigorous approximation result for centres of gravity, not merely for areas. It is the step that lets Archimedes pass from the polygon centroids to the segment centroid.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p7-centroid-limit.svg' | relative_url }}" alt="A parabolic segment with three generations of inscribed polygons and their centroids G0, G1, G2 on the diameter, approaching the segment centroid G at two fifths of the height.">
<figcaption>Propositions II.5–II.6. The polygon centroids $G_0,G_1,G_2$ lie on the diameter and climb toward the segment centroid $G$. The segment's centroid is nearer the vertex than any of them.</figcaption>
</figure>

**Mid-post challenge.** The triangle $APB$ has its centroid at one third of the height above the base. The parabolic segment's centroid is at two fifths of the height. Which is closer to the vertex? Does this agree with Proposition II.5?

---

## 6. The exact centroid: Propositions II.7–II.8

### Proposition II.7

The centres of gravity of similar parabolic segments divide their diameters in the same ratio. The proof uses the corresponding polygonal approximations and the arbitrarily close approximation of II.6.

### Proposition II.8

Let $V$ be the segment's vertex, $M$ its chord's midpoint, and $G$ its centre of gravity. Then

$$
\boxed{VG:GM=3:2.}
$$

Equivalently,

$$
VG=\frac35VM,
\qquad
MG=\frac25VM.
$$

The centroid lies three fifths of the way from the vertex to the base.

**Mid-post challenge.** Verify II.8 directly for $y=1-x^2$ by integration. The area is $4/3$, and the first moment about the base is

$$
\int_{-1}^{1}\int_{0}^{1-x^2}y\,dy\,dx.
$$

Show that the quotient is $2/5$, then check $VG:GM=(1-2/5):(2/5)=3:2$.

---

## 7. The proportionality lemma: Proposition II.9

Proposition II.9 is not a separate centroid theorem. It is an algebraic-geometrical lemma used in the proof of II.10.

Let four decreasing positive lengths be in continued proportion:

$$
a:b=b:c=c:d.
$$

Define lengths $x,y$ by

$$
\frac{x}{\frac35(a-c)}=\frac{d}{a-d}
$$

and

$$
\frac{y}{a-c}
=
\frac{2a+4b+6c+3d}
{5a+10b+10c+5d}.
$$

Then

$$
\boxed{x+y=\frac25a.}
$$

This modern symbolic statement reproduces the proportionality result used in II.10. It is not Archimedes' notation; it is a compact algebraic rendering of the geometric lemma.

The lemma is the technical heart of the final proposition. It tells Archimedes exactly where the centroid sits inside the middle fifth of the diameter.

---

## 8. The portion between parallel chords: Proposition II.10

Consider the region bounded by two parallel chords and the two intervening arcs of the parabola. Its centre of gravity lies on the diameter joining the chords' midpoints.

Let:

- $M_s$ be the midpoint of the smaller chord;
- $M_L$ be the midpoint of the larger chord;
- $H=M_sM_L$;
- $s,L$ be the smaller and larger chord lengths;
- $P,Q$ be points on the diameter with

$$
M_sP=\frac25H,
\qquad
M_sQ=\frac35H.
$$

Then the centre $G$ lies within the middle fifth $PQ$ and satisfies

$$
\boxed{
\frac{PG}{GQ}
=
\frac{L^2(2s+L)}{s^2(2L+s)}.
}
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p7-portion.svg' | relative_url }}" alt="A parabolic region cut between the chords y equals 1 and y equals 4, with the diameter, the middle fifth between P and Q, and the centroid G dividing it in the ratio 16 to 5.">
<figcaption>Proposition II.10. The centroid lies inside the middle fifth of the diameter, between $P$ and $Q$. For $s=2$, $L=4$, the ratio is $PG:GQ=16:5$.</figcaption>
</figure>

Archimedes states this ratio using volumes of solids with square bases and specified heights. The expression above is its algebraic equivalent. Using half-chord lengths instead of full chord lengths gives the same ratio.

### The limiting cases

- If $s=L$, the two chords are equal, the ratio is $1$, and $G$ is the midpoint of $PQ$.
- If $s\to0$, the smaller chord shrinks to the vertex, and the ratio tends to infinity, so $G$ approaches $Q$ — the $3/5$ point. This is exactly the segment centroid of II.8.

**Mid-post challenge.** Derive the II.10 ratio by computing the first moments of the region between the two chords. Then check the two limiting cases above.

---

## 9. Why Book II is a masterpiece of exhaustion

Book II takes the most elementary tool in the treatise — the lever — and uses it to find a property of a curved region that cannot be found by finite decomposition alone. The strategy has four steps:

1. Replace each parabolic segment by an equal-area rectangle (II.1).
2. Inscribe polygons whose centroids lie on the diameter (II.2–II.4).
3. Prove that the polygon centroids approach the segment centroid (II.5–II.6).
4. Use similarity and a proportionality lemma to pin down the exact position (II.7–II.10).

The result is not an approximation. It is an exact point, proved by exhaustion. The centroid of a parabolic segment is as precisely determined as the centroid of a triangle.

---

## Final challenge

Derive Proposition II.10's ratio

$$
\frac{PG}{GQ}
=
\frac{L^2(2s+L)}{s^2(2L+s)}
$$

for the portion between two parallel chords. Then check the limiting cases:

1. $s=L$: show that $G$ is the midpoint of $PQ$.
2. $s\to0$: show that $G\to Q$, recovering the $3:2$ ratio of II.8.

Explain why the middle fifth $PQ$ is the natural interval for the centroid: what happens at $P$ and at $Q$ in the two limits?

*Next in the series: [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}) takes the same exhaustion method into three dimensions and measures the volumes of paraboloid, hyperboloid, and spheroid segments.*

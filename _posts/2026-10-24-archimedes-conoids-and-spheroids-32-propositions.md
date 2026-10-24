---
title: "The Volumes Archimedes Measured Before Calculus Existed — 32 Propositions, Three Curved Worlds"
date: 2026-10-24 04:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - on-conoids-and-spheroids
  - paraboloid
  - hyperboloid
  - spheroid
  - method-of-exhaustion
  - archimedes
  - solid-geometry
share: true
read_time: true
excerpt: "On Conoids and Spheroids contains 32 propositions on the volumes of paraboloid, hyperboloid and spheroid segments. This is the complete guide to the formulas, the exhaustion method, and the oblique-cut cases."
---

**Challenge to the reader:** A paraboloid segment has base area $B$ and perpendicular height $H$. Show that its volume is $BH/2$. Then compare it with the cone of the same base and height: what is the ratio, and why is it larger than $1$?

*Part 8 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · **Part 8 — Conoids and Spheroids** (this page).*

Archimedes' *On Conoids and Spheroids* contains 32 propositions, preceded by definitions and two preliminary lemmas. Its results concern ellipses, the geometry of sections of solids of revolution, and — above all — the volumes of segments of paraboloids, hyperboloids, and spheroids.

The treatise is the three-dimensional companion to the *Quadrature of the Parabola*. The same exhaustion method that measured a parabolic area now measures the volume of a paraboloid, a hyperboloid, and a spheroid. The cross-sections are conics; the sums are controlled by finite approximations; the answers are exact rational multiples.

---

## 1. The objects studied

Archimedes' terminology translates as follows:

| Archimedes' term | Modern object |
|---|---|
| Right-angled conoid | Paraboloid of revolution |
| Obtuse-angled conoid | One sheet of a two-sheeted hyperboloid of revolution |
| Oblong spheroid | Prolate spheroid: an ellipse revolved about its major axis |
| Flat spheroid | Oblate spheroid: an ellipse revolved about its minor axis |

A **segment** is a finite solid bounded by part of one of these surfaces and a cutting plane. Archimedes treats both perpendicular and oblique cuts.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p8-ellipse.svg' | relative_url }}" alt="An ellipse with semimajor axis a and semiminor axis b inside its auxiliary circle of radius a, with the area ratio b over a and the formula area equals pi a b.">
<figcaption>The ellipse result of Proposition 4. The ellipse is to its auxiliary circle as the minor axis is to the major axis, so $A=\pi ab$. This area comparison is one of the preliminaries for the solid volumes.</figcaption>
</figure>

---

## 2. Preliminaries and auxiliary results

### Propositions 1–2: ratios and finite sums

Proposition 1 includes a rule for combining corresponding ratios of finite collections of magnitudes. Its role is to pass from relations between individual slices to relations between sums of slices.

Proposition 2 supplies a finite-sum relation used in the hyperboloid calculation, involving terms of the form

$$
ah+h^2,\quad a(2h)+(2h)^2,\quad \ldots,\quad a(nh)+(nh)^2.
$$

Here $a$ and $h$ are fixed lengths. These are the quadratic expressions that arise from hyperboloid cross-sectional areas.

### Propositions 4–6: the area of an ellipse

Proposition 4 states:

> The area of an ellipse is to the area of its auxiliary circle as the minor axis is to the major axis.

Writing $a,b$ for the semimajor and semiminor axes,

$$
\frac{A_{\mathrm{ellipse}}}{\pi a^2}=\frac ba,
\qquad\text{hence}\qquad
\boxed{A_{\mathrm{ellipse}}=\pi ab.}
$$

Propositions 5 and 6 give related area comparisons rather than new, independent area formulas.

### Propositions 7–9: realizing an ellipse as a section

These are construction results. Propositions 7 and 8 concern constructing cones of which a given ellipse is a plane section. Proposition 9 gives the analogous construction for a cylinder. The constructions supply comparison solids for the oblique segments.

### Propositions 11–18: sections and geometry

These establish properties of the solids and their plane sections, derived from the properties of the generating conic sections. They provide the geometric framework for the volume arguments.

### Proposition 19: arbitrarily close inner and outer approximations

For the segments under consideration, Archimedes constructs inscribed and circumscribed collections of cylinders or obliquely truncated cylinders whose volumes differ by less than any prescribed positive magnitude:

$$
V_{\mathrm{in}}\leq V\leq V_{\mathrm{out}},
\qquad
V_{\mathrm{out}}-V_{\mathrm{in}}<\varepsilon.
$$

This is the approximation result that makes the later exhaustion proofs possible.

### Proposition 20: a central plane bisects a spheroid

Any plane through the centre of a spheroid divides both:

1. the solid into two equal volumes;
2. its surface into two equal areas.

The statement applies to a general plane through the centre, not just an equatorial plane.

---

## 3. The paraboloid: Propositions 21–24

### Propositions 21–22: the volume of a paraboloid segment

A segment of a paraboloid of revolution is one and a half times the cone — or the appropriate segment of a cone — with the same base and axis. Archimedes treats perpendicular and oblique cuts.

In modern notation, if $B$ is the area of the planar base and $H$ is the perpendicular height,

$$
\boxed{
V_{\mathrm{paraboloid\ segment}}
=\frac32\,V_{\mathrm{cone}}
=\frac12 BH.
}
$$

For a perpendicular cut with circular base radius $r$,

$$
V=\frac12\pi r^2H.
$$

The segment occupies half the volume of a cylinder with the same base and perpendicular height.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p8-paraboloid.svg' | relative_url }}" alt="The cross-section z equals r squared cut at height H, with the comparison cone drawn dashed and the paraboloid segment shaded, illustrating volume equals half base times height.">
<figcaption>Propositions 21–22. The paraboloid $z=r^2$ cut at height $H$ has volume $BH/2$, which is $\tfrac32$ times the cone on the same base and axis. Here $B$ is the area of the circular base, not the base radius.</figcaption>
</figure>

**Mid-post challenge.** A paraboloid segment has base area $B=\pi R^2$ and height $H$. Show that its volume is $\pi R^2H/2$. Then compute the volume of the cone with the same base and height and verify the ratio $3/2$.

### Propositions 23–24: comparing two paraboloid segments

These compare the volumes of two segments of the same paraboloid in terms of their axes; Proposition 24 supplies the squared-axis comparison used elsewhere by Archimedes.

For perpendicular cuts, writing $h_1,h_2$ for the distances from the vertex to the cutting planes,

$$
\boxed{
\frac{V_1}{V_2}
=
\left(\frac{h_1}{h_2}\right)^2.
}
$$

Equivalently, the volume of a right segment of a fixed paraboloid is proportional to the square of its height.

The square law is not an accident. The cross-section radius grows like the square root of the height, so the area grows linearly in the height; integrating that area gives a quadratic in the height. Archimedes proves the same relation geometrically.

---

## 4. The hyperboloid: Propositions 25–26

### The setup

Let:

- $A$ be the vertex;
- $C$ be the centre of the hyperboloid;
- $CA=a$ be its axial semidiameter;
- $AD=h$ be the axis of the segment.

Then

$$
\boxed{
\frac{V_{\mathrm{segment}}}
     {V_{\mathrm{cone\ with\ same\ base\ and\ axis}}}
=
\frac{h+3a}{h+2a}.
}
$$

The propositions cover perpendicular and oblique sections.

For a perpendicular cut, with base area $B$ and height $h$,

$$
\boxed{
V=\frac{Bh}{3}\frac{h+3a}{h+2a}.
}
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p8-hyperboloid.svg' | relative_url }}" alt="The cross-section of a hyperboloid of revolution from vertex A to cutting plane D, with centre C, axial semidiameter a, height h, asymptotes dashed, and the comparison cone in orange.">
<figcaption>Propositions 25–26. The hyperboloid segment from vertex $A$ to cutting plane $D$. The comparison cone has the same base and axis; the volume ratio is $(h+3a)/(h+2a)$.</figcaption>
</figure>

Unlike the paraboloid result, this is not a constant multiple of the comparison cone. The ratio depends on the segment's size relative to the hyperboloid's axial semidiameter.

**Mid-post challenge.** For $a=1$ and $h=2$, compute the ratio $(h+3a)/(h+2a)$. Then take the limit $h\to\infty$ and explain why the segment becomes cone-like.

---

## 5. The spheroid: Propositions 27–32

### Propositions 27–30: the volume of a spheroidal segment

Let $C$ be the centre, $A,A'$ the two corresponding vertices, and let the cutting plane determine segment axes $AD=h$ and $A'D=2a-h$, where $CA=a$. For the segment not greater than half the spheroid,

$$
\boxed{
\frac{V_{\mathrm{segment}}}
     {V_{\mathrm{comparison\ cone}}}
=
\frac{CA+A'D}{A'D}
=
\frac{3a-h}{2a-h}.
}
$$

For a perpendicular cap with base area $B$,

$$
\boxed{
V=\frac{Bh}{3}\frac{3a-h}{2a-h},
\qquad 0<h\leq a.
}
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p8-spheroid.svg' | relative_url }}" alt="Left: an ellipse with a cap of height h shaded and its base chord. Right: half an ellipse compared with a cone from the centre to the equator.">
<figcaption>Propositions 27–30. A spheroidal cap of height $h$ has volume $\frac{Bh}{3}\cdot\frac{3a-h}{2a-h}$. At the central cut $h=a$, the half-spheroid is exactly twice its comparison cone.</figcaption>
</figure>

**Mid-post challenge.** A spheroid has $a=2$, $b=1.5$. Cut a cap of height $h=1.2$ from the pole. Compute the base area $B$, the cap volume, and the ratio to the comparison cone. You should find a ratio of $12/7$.

### The central-cut special case

When the cutting plane passes through the centre, $h=a$, and the ratio becomes

$$
\frac{3a-a}{2a-a}=2.
$$

Thus a half-spheroid has twice the volume of the cone with the same base and axis.

For an equatorial cut, if $a$ is the axial semiaxis and $b$ the equatorial radius, this yields the familiar whole-spheroid formula

$$
\boxed{
V_{\mathrm{spheroid}}=\frac43\pi ab^2.
}
$$

This formula is a direct modern consequence of the central-cut result, not a separate additional proposition.

### Propositions 31–32: the two complementary segments

The final two propositions determine the ratio of the volumes of the two unequal segments into which a plane divides a spheroid.

For a perpendicular cut, write the complementary cap heights as $h$ and $k$, where $h+k=2a$. Then

$$
\boxed{
\frac{V_h}{V_k}
=
\frac{h^2(3a-h)}
     {k^2(3a-k)}
=
\frac{h^2(h+3k)}
     {k^2(k+3h)}.
}
$$

This is a modern restatement of the complementary-segment comparison; Archimedes states such results as geometric proportions.

---

## 6. The main volume formulas together

For perpendicular cuts, the principal cubature results can be summarized as follows. Here $B$ denotes base area, $h$ the cap height, and $a$ the relevant axial semiaxis or semidiameter.

| Solid or segment | Modern volume formula | Propositions |
|---|---|---|
| Paraboloid segment | $V=\frac12Bh$ | 21–22 |
| Hyperboloid segment | $V=\frac{Bh}{3}\frac{h+3a}{h+2a}$ | 25–26 |
| Spheroidal cap, no larger than half | $V=\frac{Bh}{3}\frac{3a-h}{2a-h}$ | 27–30 |
| Half-spheroid | $V=2V_{\mathrm{comparison\ cone}}$ | Special case of 27–30 |
| Whole spheroid | $V=\frac43\pi ab^2$ | Consequence of the central cut |

The distinguishing achievement is that Archimedes establishes these volume relations — including the oblique-cut versions — using finite geometric approximations and exhaustion, rather than integral calculus.

---

## 7. Why the method handles three different solids

The three solids have different cross-sections:

- the paraboloid has circular cross-sections whose areas grow linearly with height;
- the hyperboloid has cross-sections whose areas grow quadratically with height, with a constant offset;
- the spheroid has elliptical cross-sections whose areas grow quadratically and then shrink.

But the method is the same in each case:

1. Slice the solid by parallel planes.
2. Inscribe and circumscribe cylinders or truncated cylinders.
3. Prove that the difference between the inner and outer sums can be made smaller than any prescribed volume.
4. Use a finite summation identity to identify the exact limit.
5. Rule out every other value by contradiction.

The cross-section is where the conic geometry enters. The exhaustion is where the rigor enters. The finite sums are where the arithmetic enters. Archimedes needs all three.

---

## Final challenge

Derive the spheroidal cap volume formula

$$
V=\frac{Bh}{3}\frac{3a-h}{2a-h}
$$

from the integral of the spheroid's cross-section. Then verify the half-spheroid case $h=a$ and the whole-spheroid case. Finally, explain why the hyperboloid ratio depends on $a$ and $h$ while the paraboloid ratio does not.

*This completes the eight treatise posts. Return to the [series guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) for the map that connects them, the three tools they share, and a reading order.*

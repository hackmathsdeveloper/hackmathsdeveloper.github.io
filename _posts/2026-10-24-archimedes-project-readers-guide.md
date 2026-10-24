---
title: "The Archimedes Project: Every Result, Reconstructed — the Map That Connects Eight Treatises"
date: 2026-10-24 12:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - archimedes
  - history-of-mathematics
  - method-of-exhaustion
  - ancient-geometry
  - series-guide
  - proof
  - mathematical-method
share: true
read_time: true
excerpt: "Eight treatises, more than 150 propositions, one method. This guide maps the whole Archimedes series: what each treatise proves, how the arguments depend on one another, and the three tools — geometry, mechanics, and exhaustion — that hold the project together."
---

**Challenge to the reader:** Before reading the map, write down which treatise you think proves the area of a parabolic segment, which proves the surface area of a sphere, and which finds the centre of gravity of a parabolic segment. Then check your answers against the dependency map in Section 1. The connections are not the ones a modern syllabus would suggest.

*You are reading the **Guide** to the nine-part series **The Archimedes Project: Every Result, Reconstructed**: **Guide** (this page) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

Archimedes left a body of work that measures curved areas, curved surfaces, and curved solids with no calculus. The formulas look modern:

$$
S_{\text{parabola}}=\frac43T,
\qquad
A_{\text{sphere}}=4\pi R^2,
\qquad
V_{\text{sphere}}=\frac43\pi R^3,
\qquad
V_{\text{paraboloid}}=\frac12BH.
$$

But the notation is ours, not his. Archimedes wrote in geometric proportions, not algebraic equations. He had no coordinate system, no limit symbol, and no integral. What he had was a method: reduce a curved object to a sequence of rectilinear objects, prove that the sequence can be made arbitrarily close, and use a contradiction to exclude every value except one.

This series reconstructs the results treatise by treatise. This guide connects them.

---

## 1. The dependency map

The map is not a chronology. It is a graph of the arguments: which treatise supplies a result that another treatise uses.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p9-dependency-map.svg' | relative_url }}" alt="A dependency graph connecting Equilibrium of Planes I, Quadrature of the Parabola, Equilibrium of Planes II, On Spirals, Measurement of a Circle, On the Sphere and Cylinder, and On Conoids and Spheroids, with labelled arrows.">
<figcaption>How the works feed one another. Solid boxes are treatises with their own post in this series; the dashed green box is a related work used by the argument. Arrows are conceptual dependencies reconstructed from the proofs, not dates of composition.</figcaption>
</figure>

Read the arrows:

- **Equilibrium I → Quadrature.** The lever law and the centroids of triangles and trapezoids supply the mechanical proof of the parabolic area.
- **Quadrature → Equilibrium II.** The area of a parabolic segment lets Book II replace a curved region by an equal-area rectangle, which is the first step in finding its centroid.
- **Quadrature → Sphere and Cylinder.** The exhaustion template — finite bounds, arbitrarily small remainder, contradiction — becomes the model for the sphere's surface and volume.
- **Sphere and Cylinder → Conoids and Spheroids.** The cylinder-and-frustum approximation is extended from spheres to paraboloids, hyperboloids, and spheroids.
- **On Spirals → Quadrature.** The spiral's area arguments use the same finite-sum and exhaustion technique as the parabola.
- **On Spirals → Measurement of a Circle.** The tangent construction turns a circumference into a straight segment, enabling the circle quadrature.
- **Measurement of a Circle → Sphere and Cylinder.** The circle-area theorem is part of the geometric toolkit for the sphere.

The most surprising arrow is the first one. Mechanics is not a side topic in Archimedes. It is a proof engine for geometry.

---

## 2. The three tools

Every result in the series is built from three kinds of reasoning.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p9-three-tools.svg' | relative_url }}" alt="A triangle connecting geometry, mechanics, and exhaustion, each pointing to a central exact result.">
<figcaption>The three tools. Geometry supplies exact ratios; mechanics supplies moments and centroids; exhaustion converts finite approximations into an exact equality.</figcaption>
</figure>

### Geometry: conic sections and exact ratios

The parabola, ellipse, hyperbola, circle, and spiral supply exact relations between chords, tangents, ordinates, and areas. These relations are the input to every proof. Without the square law of the parabola, there is no $1/8$ child triangle. Without the ellipse's area ratio, there is no spheroid volume. Without the spiral's radius-angle proportionality, there is no trisection.

### Mechanics: levers and centres of gravity

The lever law $W_1d_1=W_2d_2$ turns areas into weights. The centroid turns an extended figure into a point. Together they let Archimedes compare a curved region with a triangle, or a parabolic segment with a rectangle, without ever writing an integral.

### Exhaustion: finite bounds and contradiction

Exhaustion is the logical glue. It has three parts:

1. a finite construction that approximates the curved object from inside and outside;
2. a proof that the gap between the two approximations can be made smaller than any prescribed positive magnitude;
3. a contradiction argument that excludes every value except the claimed one.

The finite identity is often explicit — for example, $S_n+\frac13\frac{T}{4^n}=\frac43T$ in the parabola. The contradiction is often a double *reductio*: assume the area is too large, derive an inscribed polygon larger than the region; assume it is too small, derive a circumscribed polygon smaller than the region.

---

## 3. The eight treatises at a glance

| Part | Treatise | Central result | Method |
|---|---|---|---|
| [1]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) | *Quadrature of the Parabola* | $S=\frac43T=\frac23bh$ | 24 propositions; two proofs |
| [2]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) | *Quadrature of the Parabola* | The mechanical and geometric proofs side by side | Balances; inscribed triangles; finite sums |
| [3]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) | *Sphere and Cylinder* | $A_{\text{sphere}}=4\pi R^2$ | Polygonal solids; frustum lemma; double contradiction |
| [4]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) | *Sphere and Cylinder* | Sphere is $\frac23$ of its cylinder | 44 propositions of Book I; cubic of Book II |
| [5]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) | *On Spirals* | $A_1=\frac13\pi d^2$; $OT=2\pi d$ | 28 propositions; sector approximations; tangents |
| [6]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) | *Equilibrium of Planes* I | $W_1d_1=W_2d_2$; centroids of polygons | 15 propositions; lever law; subtraction |
| [7]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) | *Equilibrium of Planes* II | $VG:GM=3:2$ for a parabolic segment | 10 propositions; inscribed polygons; middle fifth |
| [8]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}) | *Conoids and Spheroids* | $V_{\text{paraboloid}}=\frac12BH$; hyperboloid and spheroid ratios | 32 propositions; cylinder approximations; exhaustion |

The two *Quadrature* posts are deliberately different. Part 1 is the proposition-by-proposition tour of all 24 results. Part 2 is the side-by-side reconstruction of the two proofs, with the exact finite-sum squeeze. Read Part 1 for completeness; read Part 2 for the logic.

---

## 4. The connective tissue

Four ideas recur across the series.

### 4.1 The parabola is the bridge between area and centroid

The *Quadrature* gives the area of a parabolic segment. Book II of *Equilibrium* uses that area to replace the segment by an equal-area rectangle, and then finds the segment's centroid. The two treatises are not independent: the centroid theory depends on the area theorem, and the area theorem's mechanical proof depends on the lever.

This is the tightest loop in the series:

$$
\text{lever law}
\;\longrightarrow\;
\text{parabolic area}
\;\longrightarrow\;
\text{parabolic centroid}.
$$

### 4.2 The sphere and the conoids share a method

The sphere's surface is trapped between polygonal surfaces; the paraboloid's volume is trapped between cylindrical shells. The objects differ, but the sandwich is the same:

$$
V_{\text{in}}\leq V\leq V_{\text{out}},
\qquad
V_{\text{out}}-V_{\text{in}}<\varepsilon.
$$

Once you understand the sphere proof, the conoid proofs are variations on a theme. The cross-sections change from circles to ellipses, parabolas, and hyperbolas; the exhaustion logic does not.

### 4.3 The spiral is the bridge to the impossible constructions

The spiral's tangent gives a straight segment equal to a circumference. Combined with the circle-area theorem, that squares the circle. The spiral's radius-angle proportionality trisects an angle. Neither construction is possible with straightedge and compass alone; both become possible when the spiral is added to the tool set.

This is the series' clearest example of a curve that earns its place by doing something no conic can do.

### 4.4 The finite identity is the proof, not the infinite series

Modern readers see

$$
S=T\left(1+\frac14+\frac1{16}+\cdots\right)=\frac43T
$$

and think the proof is the infinite series. It is not. The proof is the finite identity

$$
S_n+\frac13\frac{T}{4^n}=\frac43T
$$

plus the fact that the remainder can be made arbitrarily small. The infinite series is a summary of the finite identity, not a substitute for it.

The same pattern appears in the spiral, the sphere, and the conoids: a finite sum with an exact remainder, plus an exhaustion argument.

**Mid-post challenge.** Pick one arrow in the dependency map and rewrite the corresponding argument in your own words. Name the exact proposition that supplies the input and the exact proposition that uses it. Then explain what would fail if the arrow were reversed.

---

## 5. The result ledger

| Result | Formula | Where |
|---|---|---|
| Parabolic segment | $S=\frac43T=\frac23bh$ | Quadrature |
| Sphere surface | $A=4\pi R^2$ | Sphere and Cylinder I.33 |
| Sphere volume | $V=\frac43\pi R^3$ | Sphere and Cylinder I.34 |
| Sphere-to-cylinder | $V$ and $A$ both $\frac23$ | Sphere and Cylinder I.44 |
| Spherical cap area | $A=2\pi Rh$ | Sphere and Cylinder I.35–37 |
| Spherical cap volume | $V=\pi h^2(R-h/3)$ | Sphere and Cylinder II.2 |
| Spherical sector | $V=\frac23\pi R^2h$ | Sphere and Cylinder I.42–43 |
| Spiral first turn | $A_1=\frac13\pi d^2$ | On Spirals 24 |
| Spiral tangent | $OT=2\pi d$ | On Spirals 18 |
| Spiral portion | $A=\frac{\Delta\theta}{6}(r_1^2+r_1r_2+r_2^2)$ | On Spirals 26 |
| Lever law | $W_1d_1=W_2d_2$ | Equilibrium I.6–7 |
| Triangle centroid | $VG:GM=2:1$ | Equilibrium I.14 |
| Trapezium centroid | $\frac{M_bG}{GM_B}=\frac{2B+b}{B+2b}$ | Equilibrium I.15 |
| Parabolic centroid | $VG:GM=3:2$ | Equilibrium II.8 |
| Parabolic portion | $\frac{PG}{GQ}=\frac{L^2(2s+L)}{s^2(2L+s)}$ | Equilibrium II.10 |
| Paraboloid segment | $V=\frac12BH$ | Conoids 21–22 |
| Hyperboloid segment | $V=\frac{Bh}{3}\frac{h+3a}{h+2a}$ | Conoids 25–26 |
| Spheroidal cap | $V=\frac{Bh}{3}\frac{3a-h}{2a-h}$ | Conoids 27–30 |
| Whole spheroid | $V=\frac43\pi ab^2$ | Conoids 27–30, central cut |

The ledger is a reading list in disguise. Every row is a post; every post is a proof.

**Mid-post challenge.** Pick three rows of the ledger and identify which of the three tools is doing the main work in each. Then find one row where all three tools are indispensable, and explain why removing any one of them breaks the proof.

---

## 6. Four reading orders

The series can be read in several ways.

**The method first.** Parts [1]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) → [2]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) → [3]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) → [8]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}). This is the clearest path through exhaustion: area, then surface, then volume.

**The mechanics first.** Parts [6]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) → [2]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) → [7]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}). Start with the lever and the centroid; then see the mechanical proof of the parabola; then see how Book II uses the area result.

**The famous constructions first.** Parts [3]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) → [4]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) → [5]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}). The sphere, the tombstone ratio, and the spiral that squares the circle.

**The full sweep.** [1]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) → [2]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) → [3]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) → [4]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) → [5]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) → [6]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) → [7]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) → [8]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}) → this guide.

---

## 7. What Archimedes did not have

It is tempting to read the formulas as if Archimedes had modern algebra and calculus. He did not.

- **No algebraic notation.** He wrote proportions, not equations. The equation $S=4T/3$ is a translation.
- **No coordinate geometry.** He used chords, tangents, diameters, and ordinates, not $x$ and $y$.
- **No limit concept.** He used finite inequalities and the fact that a remainder can be made smaller than any prescribed magnitude.
- **No integral.** He summed finite collections of triangles, trapezoids, cylinders, and frustums.

What he did have was a standard of rigor that survives translation. The modern formulas are not improvements on his arguments; they are different notations for the same conclusions.

---

## 8. About the figures

Every figure in this series is an SVG generated from the equations, not a hand-drawn sketch. Curves are sampled from their defining formulas; tangent lines, chords, centroids, and area ratios are computed exactly. The generator is in the repository at `_tools/archimedes_figures.py`, and the output is in `assets/archimedes/`.

The parabolas are plotted from $y=x^2$ or $y=1-x^2$. The spiral is plotted from $r=a\theta$. The sphere, hyperboloid, and spheroid figures use exact cross-sections and exact ratios. Where a figure shows a numerical example, the numbers are rational and checked: $7/3$, $21/25$, $16/5$, $5/4$, $12/7$, and so on.

This matters for the same reason the proofs do. A diagram can illustrate a false claim as easily as a true one. These diagrams are constructed so that the geometry they display is the geometry the text proves.

---

## Final challenge

The series rests on three tools: geometry, mechanics, and exhaustion. Choose one result from each of three different treatises — for example, the parabolic area, the sphere's surface, and the parabolic centroid — and for each one identify:

1. the finite geometric construction;
2. the exact finite identity or bound;
3. the contradiction or limiting step that converts the finite result into an exact equality.

Then explain which of the three tools is doing the work at each step. If you can do this for three different treatises, you have understood the method that unifies the entire Archimedes Project.

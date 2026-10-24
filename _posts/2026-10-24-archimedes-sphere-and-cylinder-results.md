---
title: "The 2:3 Ratio Archimedes Wanted on His Tombstone — and the 44 Propositions of Book I"
date: 2026-10-24 08:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - on-the-sphere-and-cylinder
  - sphere-volume
  - spherical-cap
  - spherical-sector
  - archimedes
  - ancient-geometry
  - cubic-equation
share: true
read_time: true
excerpt: "On the Sphere and Cylinder proves that a sphere has two thirds the volume and two thirds the total surface area of its circumscribing cylinder. This is the complete result catalogue, from the 44 propositions of Book I to the cubic equation of Book II."
---

**Challenge to the reader:** A cylinder circumscribes a sphere of radius $r$, so the cylinder has radius $r$ and height $2r$. Compute both volumes and both total surface areas. Confirm that the sphere is exactly two thirds of the cylinder in both measurements. Then check that the sphere's surface area equals the cylinder's *lateral* area, not its total area.

*Part 4 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · **Part 4 — Sphere and Cylinder** (this page) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

*On the Sphere and Cylinder* (*Περὶ σφαίρας καὶ κυλίνδρου*) was written around 225 BC in two books. Book I establishes the surface areas and volumes of spheres, spherical caps, cones, and cylinders through the method of exhaustion. Book II applies those results to planes cutting spheres.

The result Archimedes was proudest of is the ratio:

$$
\boxed{
\frac{V_{\text{sphere}}}{V_{\text{cylinder}}}
=
\frac{A_{\text{sphere}}}{A_{\text{cylinder}}}
=
\frac23.
}
$$

He asked for a sphere inscribed in a cylinder to be carved on his tombstone. The ratio is not a numerical coincidence; it follows from the same exhaustion machinery that proves $A_{\text{sphere}}=4\pi r^2$.

---

## 1. The setup

Let $r$ be the radius of the sphere, so its diameter is $d=2r$. Circumscribe a right circular cylinder: its height is $2r$ and its base radius is $r$.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p4-sphere-cylinder.svg' | relative_url }}" alt="A sphere of radius r inside a cylinder of radius r and height 2r, with the volume and surface area ratios 2 to 3.">
<figcaption>The sphere and its circumscribing cylinder. The cylinder's total surface is $6\pi r^2$; the sphere's is $4\pi r^2$; the cylinder's volume is $2\pi r^3$; the sphere's is $\tfrac43\pi r^3$.</figcaption>
</figure>

The three quantities that matter are:

$$
A_{\text{sphere}}=4\pi r^2,
\qquad
V_{\text{sphere}}=\frac43\pi r^3,
\qquad
A_{\text{cylinder}}=6\pi r^2.
$$

The cylinder's lateral area is

$$
2\pi r\cdot 2r=4\pi r^2,
$$

which is exactly the sphere's surface area. The cylinder's two circular caps add $2\pi r^2$, bringing its total to $6\pi r^2$.

### Why the ratios are both $2/3$

$$
\frac{V_{\text{sphere}}}{V_{\text{cylinder}}}
=
\frac{\tfrac43\pi r^3}{2\pi r^3}
=
\frac23,
$$

and

$$
\frac{A_{\text{sphere}}}{A_{\text{cylinder}}}
=
\frac{4\pi r^2}{6\pi r^2}
=
\frac23.
$$

The equality of the two ratios is the tombstone fact.

---

## 2. Book I: the surface-area theorems

Book I begins with axioms about convex surfaces and curves, then develops the surface results.

### Propositions 13 and 14: the cylinder's lateral area

The lateral surface area of a right circular cylinder equals the area of a circle whose radius is the mean proportional between the height of the cylinder and the diameter of its base:

$$
A_{\text{cylinder, lateral}}=2\pi r h.
$$

For the circumscribing cylinder, $h=2r$, so the lateral area is $4\pi r^2$.

### Proposition 33: the sphere's surface area

The surface area of any sphere is four times the area of its greatest circle:

$$
\boxed{A_{\text{sphere}}=4\pi r^2.}
$$

Part 3 reconstructs the exhaustion proof. The key idea is that the sphere's surface is trapped between the surfaces of inscribed and circumscribed polygonal solids, both of which converge to $4\pi r^2$.

### Propositions 35–37: the spherical cap

The surface area of a spherical cap equals the area of a circle whose radius is the straight line from the vertex of the cap to a point on the base perimeter:

$$
\boxed{A_{\text{cap}}=2\pi r h,}
$$

where $h$ is the height of the cap.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p4-cap.svg' | relative_url }}" alt="A sphere with a cap of height h shaded above a horizontal chord, showing the base radius and the formulas for the cap area and volume.">
<figcaption>A spherical cap of height $h$. Its area is $2\pi rh$; its volume is $\pi h^2(r-h/3)$. A hemisphere is the case $h=r$.</figcaption>
</figure>

The cap formula is remarkable because it depends only on the height, not on where the cap is cut from the sphere. A shallow cap near the pole and a deeper cap near the equator have the same area if their heights agree.

### The hemisphere check

Set $h=r$. Then

$$
A_{\text{cap}}=2\pi r^2,
$$

which is half the sphere's surface. The cap is a hemisphere.

**Mid-post challenge.** A spherical cap has height $h=r$. What fraction of the sphere's surface and volume does it contain? Check your answer against $A=2\pi rh$ and $V=\pi h^2(r-h/3)$.

---

## 3. Book I: the volume theorems

### Proposition 34: the sphere's volume

Any sphere is equal in volume to four times the cone whose base is the greatest circle of the sphere and whose height is the radius:

$$
\boxed{
V_{\text{sphere}}
=4\left(\frac13\pi r^2\cdot r\right)
=\frac43\pi r^3.
}
$$

### Propositions 42 and 43: the spherical sector

A spherical sector is the solid generated by rotating a circular sector of the sphere about its axis. It is a cone from the centre of the sphere plus the spherical cap. Its volume is

$$
\boxed{
V_{\text{sector}}
=\frac13(2\pi r h)r
=\frac23\pi r^2h,
}
$$

where $h$ is the height of the cap.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p4-sector.svg' | relative_url }}" alt="A sphere with a circular sector shaded about the vertical axis, its cap, and the sector volume formula two thirds pi r squared h.">
<figcaption>A spherical sector. The solid is a cone with apex at the sphere's centre plus the cap. Its volume is $\tfrac23\pi r^2h$, where $h$ is the cap height.</figcaption>
</figure>

The formula is a direct consequence of the cap area: the sector is the cone over the cap, and its volume is one third of the cap's area times the radius.

### Proposition 44: the grand ratio

A sphere has two thirds the volume and two thirds the total surface area of its circumscribing cylinder:

$$
\boxed{
\frac{V_{\text{sphere}}}{V_{\text{cylinder}}}
=
\frac{\tfrac43\pi r^3}{2\pi r^3}
=
\frac23,
\qquad
\frac{A_{\text{sphere}}}{A_{\text{cylinder}}}
=
\frac{4\pi r^2}{6\pi r^2}
=
\frac23.
}
$$

This is the result Archimedes asked to have carved on his tomb.

---

## 4. Book II: cutting and segmenting spheres

Book II contains nine propositions applying Book I to planes intersecting spheres.

### Proposition 2: the volume of a spherical segment

The volume of a spherical segment of height $h$ cut from a sphere of radius $r$ is

$$
\boxed{
V_{\text{segment}}
=\pi h^2\left(r-\frac h3\right).
}
$$

Equivalently,

$$
V_{\text{segment}}
=\frac{\pi h^2(3r-h)}{3}.
$$

The formula reduces to the hemisphere at $h=r$:

$$
V=\pi r^2\left(r-\frac r3\right)
=\frac23\pi r^3,
$$

which is half of $\tfrac43\pi r^3$.

### Propositions 3 and 4: cutting a sphere in a given ratio

Given a sphere, cut it by a plane so that:

1. the surface areas of the two resulting spherical segments have a given ratio;
2. the volumes of the two resulting spherical segments have a given ratio.

The surface case is comparatively straightforward because cap areas are linear in height. The volume case is not. It requires solving a cubic equation of the form

$$
\boxed{x^3-ax^2+b=0,}
$$

and Archimedes solves it geometrically by intersecting conic sections.

**Mid-post challenge.** For a sphere of radius $r$, let the smaller cap have height $h$ and the larger cap height $2r-h$. Show that the condition

$$
\frac{V_{\text{small}}}{V_{\text{large}}}=k
$$

leads to the cubic

$$
h^3-3rh^2+\frac{4k}{1+k}r^3=0.
$$

Identify $a$ and $b$ in the form $x^3-ax^2+b=0$.

### Why a cubic, and why conic sections

The volume of a cap is cubic in its height:

$$
V(h)=\pi h^2\left(r-\frac h3\right).
$$

Setting a ratio of two such volumes produces a cubic equation. Greek geometry had no general cubic formula. Archimedes' solution is a **neusis**-style construction: intersect a parabola and a hyperbola (or another pair of conics) so that the intersection point has the required coordinate. The construction is not a ruler-and-compass construction; it enlarges the permitted tools in the same way the spiral does for angle trisection.

This is one of the places where Archimedes' geometry goes beyond what straightedge and compass can do.

### Propositions 8 and 9: similar spherical segments

Similar spherical segments — segments subtending equal angles at the centre — have surface areas proportional to the squares of their heights or base radii, and volumes proportional to the cubes:

$$
\boxed{
\frac{A_1}{A_2}
=
\left(\frac{h_1}{h_2}\right)^2,
\qquad
\frac{V_1}{V_2}
=
\left(\frac{h_1}{h_2}\right)^3.
}
$$

The square and cube laws are the signature of similarity in two and three dimensions. They also explain why the cubic in Proposition 4 is unavoidable: the volume ratio is a ratio of cubes.

---

## 5. The result catalogue

| Result | Statement | Location |
|---|---|---|
| Cylinder lateral area | $A=2\pi rh$ | I.13–14 |
| Sphere surface area | $A=4\pi r^2$ | I.33 |
| Spherical cap area | $A=2\pi rh$ | I.35–37 |
| Sphere volume | $V=\tfrac43\pi r^3$ | I.34 |
| Spherical sector volume | $V=\tfrac23\pi r^2h$ | I.42–43 |
| Sphere-to-cylinder ratio | $V$ and $A$ both $\tfrac23$ | I.44 |
| Spherical segment volume | $V=\pi h^2(r-h/3)$ | II.2 |
| Cut by surface ratio | Solvable by a proportion | II.3 |
| Cut by volume ratio | Solves a cubic by conics | II.4 |
| Similar segment areas | $A_1/A_2=(h_1/h_2)^2$ | II.8 |
| Similar segment volumes | $V_1/V_2=(h_1/h_2)^3$ | II.9 |

The catalogue is compact, but each line is the endpoint of a finite exhaustion argument. The formulas are not guesses fitted to measurements; they are forced by polygonal approximations and contradiction.

---

## 6. Why the tombstone ratio matters

The 2:3 ratio is elegant, but its real significance is methodological. It shows that a curved solid and a rectilinear solid can stand in an exact rational ratio. The sphere is not approximately two thirds of the cylinder; it is exactly two thirds.

That exactness is the point. The ratio survives because both quantities are pinned down by the same finite inequalities. The sphere's volume is not defined by a limit that might depend on the approximation; it is defined by the requirement that every inscribed polygonal solid have smaller volume and every circumscribed one larger volume.

The tombstone is a statement about proof, not just about numbers.

---

## Final challenge

Archimedes' Proposition II.4 asks for a plane cutting a sphere so that the two volumes have a given ratio. Reduce the problem to a cubic, explain why the cubic cannot be solved by straightedge and compass in general, and describe how intersecting two conic sections produces the required point. Then verify that your construction gives the correct answer in the special case where the two volumes are equal.

*Next in the series: [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) turns to a curve that is not a conic, and uses it to square the circle and trisect an angle.*

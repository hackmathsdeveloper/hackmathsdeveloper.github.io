---
title: "The Sphere's Surface Area Is 4πR² — and Archimedes Proved It Without a Single Integral"
date: 2026-10-24 09:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - sphere-surface-area
  - method-of-exhaustion
  - proof-by-contradiction
  - archimedes
  - ancient-geometry
  - frustum
  - zone-theorem
share: true
read_time: true
excerpt: "Archimedes trapped the sphere's surface between inscribed and circumscribed polygonal solids and squeezed both to 4πR². The proof is a double reductio ad absurdum built on one frustum lemma — and it still reads like a modern rigorous argument."
---

**Challenge to the reader:** Inscribe a square in a circle of radius $R$ and rotate the upper half of the square about a diameter. Compute the surface area of the resulting solid. Show that it is $2\sqrt2\,\pi R^2$, which is strictly less than $4\pi R^2$. Then explain why rotating more sides should push the answer upward toward $4\pi R^2$.

*Part 3 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · **Part 3 — The Sphere's Surface** (this page) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

Archimedes' proof that the surface area of a sphere of radius $R$ is four times the area of its great circle,

$$
\boxed{A=4\pi R^2,}
$$

is one of the crowning achievements of ancient geometry. There is no calculus in it. There is no limit notation. There is a regular polygon, a rotation, a frustum lemma, and a double *reductio ad absurdum*.

**Why it matters.** The argument does not merely compute the number. It shows why the number is forced. The sphere's surface is caught between two polygonal surfaces that can be made arbitrarily close to it, and both bounds converge to the same value. That is the exhaustion method at its purest.

---

## 1. The strategy: two polygons around one circle

Start with a great circle of radius $R$. Inscribe a regular polygon with $2n$ sides and circumscribe another regular polygon with $2n$ sides. The inscribed polygon lies inside the circle; the circumscribed polygon lies outside and touches the circle at the midpoints of its sides.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p3-polygons.svg' | relative_url }}" alt="A circle of radius R with an inscribed regular hexagon, a circumscribed regular hexagon, the radius R, and the apothem a_n.">
<figcaption>The two polygons around the circle. The inscribed polygon lies inside; the circumscribed polygon lies outside and touches the circle at the midpoints of its sides. The figure shows six sides; the proof takes $2n$ sides and lets $n$ grow.</figcaption>
</figure>

The plan has three steps:

1. Rotate the upper chain of each polygon about a diameter. This produces a solid made of cones and frustums.
2. Compute the surface area of each solid using one lemma about frustums.
3. Show that both surface areas approach $4\pi R^2$, then use a double contradiction to prove that the sphere's surface area cannot be anything else.

The phrase "upper chain" matters. If you rotate the entire closed polygon, the upper and lower chains generate the same surface twice. Archimedes rotates one chain, from one endpoint of the axis to the other, so each zone of the surface is counted once.

---

## 2. Revolution: cones, frustums, and the two solids

Rotate the upper chain of the inscribed polygon about the diameter. Each side generates a frustum of a cone; the sides adjacent to the axis generate cones, which are frustums with one radius equal to zero. The resulting solid lies entirely inside the sphere.

Rotate the upper chain of the circumscribed polygon. The resulting solid contains the sphere entirely.

Because the inscribed solid is inside the sphere and the circumscribed solid contains it, their surface areas satisfy

$$
S_{\text{inscribed}}<A_{\text{sphere}}<S_{\text{circumscribed}}.
$$

This is the geometric sandwich. The rest of the proof is a calculation of the two outer surfaces and a squeeze.

---

## 3. The frustum lemma and the exact surface sums

### The lemma

The lateral surface area of a frustum of a cone with slant height $s$ and base radii $r_1$ and $r_2$ is

$$
\boxed{\text{Area}=2\pi\,r_{\text{mid}}\,s,}
$$

where

$$
r_{\text{mid}}=\frac{r_1+r_2}{2}
$$

is the average radius, equivalently the distance from the midpoint of the slant side to the axis of rotation.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p3-frustum.svg' | relative_url }}" alt="An axial cross-section of a conical frustum with radii r1 and r2, slant height s, and midpoint radius r_mid, illustrating the formula lateral area equals 2 pi r_mid s.">
<figcaption>The frustum lemma. The lateral area is the circumference at the midpoint radius times the slant height: $2\pi r_{\text{mid}}s$. A cone is the case $r_1=0$.</figcaption>
</figure>

**Mid-post challenge.** Check the lemma for a cone by setting $r_1=0$. You should recover the familiar lateral area $\pi r_2 s$.

### The inscribed sum

For a regular $2n$-gon inscribed in a circle of radius $R$, let

$$
a_n=R\cos\frac{\pi}{2n}
$$

be the apothem, the perpendicular distance from the centre to a side. Each side has the same slant length, and the midpoint radii of the frustums sum in such a way that the total surface area of the inscribed solid collapses to

$$
S_{\text{inscribed}}=2\pi\,(2R)\,a_n
=4\pi R^2\cos\frac{\pi}{2n}.
$$

As $n$ grows, $\cos(\pi/(2n))\to1$, so

$$
S_{\text{inscribed}}\to4\pi R^2.
$$

The inscribed areas approach the sphere's surface from below.

### The circumscribed sum

For the circumscribed $2n$-gon, write $\delta=\pi/(2n)$. The vertices lie at radius $R\sec\delta$, and a direct application of the frustum lemma to the upper chain gives the modern exact expression

$$
S_{\text{circumscribed}}
=4\pi R^2\sec^2\delta\,\sin\bigl((n-1)\delta\bigr).
$$

As $n$ grows, $\sec^2\delta\to1$ and $\sin((n-1)\delta)=\cos\delta\to1$, so

$$
S_{\text{circumscribed}}\to4\pi R^2.
$$

The circumscribed areas approach the sphere's surface from above.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p3-squeeze.svg' | relative_url }}" alt="A plot of the inscribed and circumscribed polygonal surface areas divided by 4 pi R squared against the number of polygon sides; both curves converge to the value 1, with the region between them shaded.">
<figcaption>The squeeze. Plotted vertically is the surface area divided by $4\pi R^2$; horizontally is the number of polygon sides. The inscribed curve rises to $1$; the circumscribed curve falls to $1$. The gap can be made smaller than any prescribed positive area.</figcaption>
</figure>

**Mid-post challenge.** For $n=2$ (a square), verify that the inscribed formula gives $2\sqrt2\,\pi R^2$ and the circumscribed formula gives $4\sqrt2\,\pi R^2$. Which one matches your rotation of the upper half of the square?

---

## 4. The double proof by contradiction

Let

$$
C=4\pi R^2
$$

be four times the area of the great circle. Archimedes proves $A_{\text{sphere}}=C$ by excluding both strict inequalities.

### Part A: assume $A_{\text{sphere}}>C$

If $A_{\text{sphere}}>C$, then, because the circumscribed areas decrease to $C$, we can choose $n$ large enough that

$$
S_{\text{circumscribed}}<A_{\text{sphere}}.
$$

But the circumscribed solid completely encloses the sphere, so its surface area must be strictly greater than the sphere's:

$$
S_{\text{circumscribed}}>A_{\text{sphere}}.
$$

Contradiction. Therefore $A_{\text{sphere}}$ cannot be strictly greater than $C$.

### Part B: assume $A_{\text{sphere}}<C$

If $A_{\text{sphere}}<C$, then, because the inscribed areas increase to $C$, we can choose $n$ large enough that

$$
S_{\text{inscribed}}>A_{\text{sphere}}.
$$

But the inscribed solid lies entirely inside the sphere, so its surface area must be strictly less than the sphere's:

$$
S_{\text{inscribed}}<A_{\text{sphere}}.
$$

Contradiction. Therefore $A_{\text{sphere}}$ cannot be strictly less than $C$.

### Conclusion

Since $A_{\text{sphere}}$ is neither greater than nor less than $C$,

$$
\boxed{A_{\text{sphere}}=C=4\pi R^2.}
$$

**Mid-post challenge.** Write the two contradiction arguments as formal inequality chains. In each part, identify the two inequalities that cannot both hold, and state exactly which construction produces the contradicting one.

---

## 5. The zone theorem: why height, not latitude, controls area

The proof above is often remembered for its double contradiction. But the frustum lemma hides a beautiful corollary: the area of a band of a sphere depends only on its height, not on where the band sits.

For a sphere of radius $R$, slice it by two horizontal planes at heights $z_1$ and $z_2$. The band between them has area

$$
\boxed{A_{\text{band}}=2\pi R\,(z_2-z_1).}
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p3-zones.svg' | relative_url }}" alt="A sphere cut by equally spaced horizontal planes, with alternating shaded bands. The band height is delta z and the area of each band is 2 pi R delta z.">
<figcaption>The zone theorem. Equally spaced horizontal slices cut the sphere into bands of equal area. A band near the pole and a band near the equator have the same area if their heights are equal.</figcaption>
</figure>

A modern derivation is one line:

$$
A_{\text{band}}
=\int_{z_1}^{z_2}2\pi R\,dz
=2\pi R(z_2-z_1).
$$

The factor $2\pi R$ is constant. The latitude does not appear. That is why equal-height bands have equal area, even though bands near the equator look wider.

Archimedes proves the same statement geometrically. The frustum lemma is the engine: as the slices become thin, the frustum area approaches the zone area, and the midpoint radius tends to $R$.

This is the result that later becomes the **hat-box theorem**: the surface area of a sphere equals the area of the rectangle you would get by unwrapping it into a cylinder of the same radius and height.

---

## 6. Why the argument is airtight

The proof rests on three facts:

1. **The inscribed solid is inside the sphere.** Its surface area is therefore smaller.
2. **The circumscribed solid contains the sphere.** Its surface area is therefore larger.
3. **Both polygonal surface areas converge to $C$.** The gap can be made smaller than any prescribed positive area.

Given those facts, neither $A>C$ nor $A<C$ can survive. The exact equality is forced.

This is the same logical pattern as the quadrature of the parabola: a finite construction, an arbitrarily tight inequality, and a contradiction that excludes every value except one. The objects change; the method does not.

---

## Final challenge

Prove the zone theorem directly from the frustum lemma without using an integral. Take a sphere of radius $R$, cut it by two horizontal planes at heights $z_1$ and $z_2$, and approximate the band by frustums generated by chords of the great circle. Show that the sum of the frustum areas tends to $2\pi R(z_2-z_1)$ as the chords become small. Then explain why equal-height bands of the sphere have equal area.

*Next in the series: [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) collects all the results of the treatise that contains this proof, including the 2:3 ratio Archimedes asked to have carved on his tomb.*

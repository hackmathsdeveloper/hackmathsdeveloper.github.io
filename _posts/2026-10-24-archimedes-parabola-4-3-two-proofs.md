---
title: "Two Proofs, One Answer: How Archimedes Caught the Parabola Between a Lever and Infinity"
date: 2026-10-24 10:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - quadrature-of-the-parabola
  - law-of-the-lever
  - method-of-exhaustion
  - geometric-series
  - archimedes
  - proof-by-contradiction
share: true
read_time: true
excerpt: "Archimedes proved that a parabolic segment is four thirds of its inscribed triangle twice: once with balances, once with inscribed triangles and exhaustion. This is the side-by-side reconstruction of both proofs and the exact squeeze that makes them work."
---

**Challenge to the reader:** Show that the inscribed vertex triangle occupies exactly three quarters of the parabolic segment, so the two curved slivers have total area $T/3$. Then explain why an argument that only shows the slivers shrink cannot, by itself, prove that their total is exactly $T/3$.

*Part 2 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · [Part 1 — The Parabola's 24 Propositions]({% post_url 2026-10-24-archimedes-parabola-24-propositions %}) · **Part 2 — Two Proofs of 4/3** (this page) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

Archimedes' *The Quadrature of the Parabola* proves one central result:

$$
\boxed{
\operatorname{Area}(\text{parabolic segment})
=\frac43\,\operatorname{Area}(\triangle APB).
}
$$

Equivalently, if the segment has base $b$ and perpendicular height $h$,

$$
\boxed{S=\frac23bh.}
$$

What makes the treatise extraordinary is not the formula but the two independent routes to it. One route runs through the law of the lever and the centres of gravity of triangles and trapezoids. The other runs through a recursive construction of inscribed triangles and a finite geometric-sum identity. Both end at the same number.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p2-two-proofs.svg' | relative_url }}" alt="Two schematic panels: a mechanical proof with a balance and weights, and a geometric proof with nested triangles in a parabolic segment, both pointing to the formula S equals four thirds T.">
<figcaption>Two arguments, one result. The mechanical route uses finite balance lemmas; the geometric route uses inscribed triangles and exhaustion. Neither is an informal summing of infinitely many pieces.</figcaption>
</figure>

---

## 1. What is being measured?

A parabolic segment is the region enclosed by an arc of a parabola and a chord joining two points $A$ and $B$ on the parabola. The chord need not be perpendicular to the axis.

Let $P$ be the point on the arc where the tangent is parallel to $AB$. Archimedes calls $P$ the **vertex of the segment**; it need not be the vertex of the whole parabola. The triangle $APB$ has the same base and the same perpendicular height as the segment.

The theorem says

$$
\operatorname{Area}(\text{segment})
=\frac43\operatorname{Area}(\triangle APB).
$$

Since the triangle's area is $\tfrac12bh$, the segment's area is $\tfrac23bh$. The triangle therefore occupies three quarters of the segment, and the curved regions outside it occupy the remaining quarter.

### What "quadrature" means

The goal is to express the curved region's area through a rectilinear figure whose area is already understood. Archimedes achieves an exact ratio to a triangle, not a numerical approximation. In his introductory letter he describes the problem as squaring the segment bounded by a straight line and a parabola.

---

## 2. The logical structure

| Propositions | Purpose |
|---|---|
| 1–5 | Establish or recall the parabola properties needed later |
| 6–13 | Develop balance results for triangles and trapezoids |
| 14–15 | Apply those results to polygonal approximations |
| 16–17 | Complete the first quadrature |
| 18–21 | Develop the inscribed-triangle construction |
| 22–23 | Establish the finite approximation and summation results |
| 24 | Complete the purely geometric quadrature |

The first proof is not the informal argument of *The Method*, where collections of line-sections are balanced. Here the mechanical proof proceeds through finite triangles, finite trapezoids, strict bounds, and a final contradiction.

---

## 3. Propositions 1–5: the shared geometry

The first five propositions supply the ratios both proofs need. Part 1 treats them in detail; here is the working summary.

### Proposition 1: midpoint and parallel tangent

If the axis-parallel line through the midpoint $M$ of chord $AB$ meets the parabola at $P$, then the tangent at $P$ is parallel to $AB$. Conversely, a tangent parallel to $AB$ meets the axis-parallel through the chord midpoint.

### Proposition 2: the tangent intercept is bisected

The tangent at $B$ meets the diameter $PM$ at $E$, and

$$
PM=PE.
$$

This connects the enclosing triangle with the inscribed triangle.

### Proposition 3: the square law

Transverse distances squared are proportional to corresponding distances along a diameter. In coordinates this is $y=kx^2$, or

$$
\frac{y_1}{y_2}=\frac{x_1^2}{x_2^2}.
$$

The square law is the source of the $1/8$ child ratio and the $1/4$ generation ratio.

### Proposition 4: chord-relative proportionality

A proportion relating the chord, a side of the inscribed triangle, an axis-parallel line, and the parabola itself. Its role is to adapt the square law to an arbitrary chord, including an oblique one.

### Proposition 5: the section ratio

Draw through one endpoint of the chord a line parallel to the axis, and draw the tangent at the other endpoint. These lines and the chord form an enclosing triangle. A line through this triangle parallel to the axis is divided by the parabola in a ratio determined by the corresponding division of the chord. This is the geometric bridge to the balance argument.

---

## 4. The mechanical quadrature: Propositions 6–17

### The underlying idea

Imagine plane figures as uniform thin plates. Their weights are proportional to their areas, and a balance relates a weight to its distance from the fulcrum. Archimedes uses this to obtain area comparisons, but the proof proceeds through finite geometric figures and inequalities.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p2-lever.svg' | relative_url }}" alt="A balance beam with a triangle whose centroid is one third of the arm length from the fulcrum, balanced by a counterweight of one third the triangle's area at the full arm length.">
<figcaption>The balance lemma behind Proposition 6. A triangle whose centroid lies at $L/3$ from the fulcrum is balanced at distance $L$ by one third of its area: $Z\cdot L=T\cdot L/3$.</figcaption>
</figure>

### Propositions 6–13: the balance lemmas

| Proposition | Result and purpose |
|---|---|
| 6 | In the prescribed right-triangle configuration, the balancing area equals one third of the triangle's area |
| 7 | Extends the one-third result to a scalene triangle |
| 8 | Bounds the balancing area of a displaced right triangle between two comparison areas |
| 9 | Gives the analogous bounds for a scalene triangle |
| 10 | Upper bound for a right-angled trapezoid |
| 11 | Corresponding trapezoid bound in a more general configuration |
| 12 | Both lower and upper bounds for another trapezoid configuration |
| 13 | Extends the two-sided bounds to the general trapezoid |

These are configuration-dependent statements. Proposition 6 does not say that every triangle balances one third of its area at arbitrary distances. The prescribed positions and lever lengths are essential.

### Propositions 14–15: polygonal bounds

Archimedes divides the chord into equal parts and constructs triangles and trapezoids associated with the parabola. Proposition 14 treats a chord perpendicular to the axis; Proposition 15 treats the oblique-chord case. The balance lemmas yield an inner polygonal area $L$ and an outer polygonal area $U$ such that, for the enclosing triangle of area $C$,

$$
3L<C<3U.
$$

Equivalently,

$$
L<\frac C3<U.
$$

The parabolic segment is also trapped between the polygonal approximations.

### Proposition 16: the segment is one third of the enclosing triangle

Refining the construction makes the difference between the bounding areas sufficiently small to rule out either inequality

$$
A_{\text{segment}}>\frac C3
\qquad\text{or}\qquad
A_{\text{segment}}<\frac C3.
$$

Therefore

$$
\boxed{A_{\text{segment}}=\frac C3.}
$$

The enclosing triangle is formed by the chord, the axis-parallel line through one endpoint, and the tangent at the other endpoint.

### Proposition 17: the first proof of the $4/3$ theorem

The enclosing triangle has four times the area of the inscribed vertex triangle $T$. Hence

$$
A_{\text{segment}}
=\frac13(4T)
=\frac43T.
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p2-auxiliary.svg' | relative_url }}" alt="The large auxiliary triangle ADB formed by the chord AB, the axis-parallel through A, and the tangent at B, containing the smaller inscribed triangle APB; the large triangle has area 4T and the small one T.">
<figcaption>The auxiliary triangle $ADB$ has area $4T$, while the inscribed triangle $APB$ has area $T$. The segment is one third of $ADB$, hence four thirds of $T$.</figcaption>
</figure>

**Mid-post challenge.** Explain why the polygonal bounds $3L<C<3U$ can exclude both $S>C/3$ and $S<C/3$. Your argument should say exactly how refining the division makes the gap between $L$ and $U$ smaller than any prescribed positive area.

---

## 5. The geometric quadrature: Propositions 18–24

The second proof replaces balances with a recursive construction of inscribed triangles.

### Proposition 18: locating the vertex

The axis-parallel line through the midpoint of the chord meets the parabola at the segment's vertex. This gives the construction required not only for the original triangle but for every smaller triangle added later.

### Proposition 19: the three-quarter height relation

Draw axis-parallel distances from the chord to the curve, one at the chord's midpoint and one at the midpoint of either half. The central distance is $4/3$ of the quarter-position distance:

$$
h_{\text{quarter}}=\frac34h_{\text{middle}}.
$$

In the normalized model $y=1-x^2$ on $[-1,1]$,

$$
y(0)=1,\qquad y\!\left(\frac12\right)=\frac34.
$$

### Proposition 20: the inscribed triangle exceeds half the segment

If $T$ is the area of the inscribed vertex triangle and $A$ the area of the segment, then

$$
T>\frac12A.
$$

After removing that triangle, less than half the segment remains. Repeat in each residual segment. At every round, more than half of each residual segment is removed. The total remainder can therefore be made smaller than any assigned positive area.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p2-parallelogram.svg' | relative_url }}" alt="The parabolic segment inside a rectangle of area twice the inscribed triangle, showing S less than 2T and therefore T greater than S over 2.">
<figcaption>Why the first triangle removes more than half. The segment lies strictly inside the enclosing rectangle of area $2T$, so $S<2T$ and therefore $T>S/2$.</figcaption>
</figure>

### Proposition 21: each child triangle has one eighth of its parent's area

The first triangle leaves two smaller parabolic segments. Inscribe a vertex triangle in each. Archimedes proves that each new triangle has area

$$
\frac18T.
$$

Together they have area

$$
2\cdot\frac18T=\frac14T.
$$

| Generation | Number of triangles | Area of each | Total area added |
|---|---:|---:|---:|
| 0 | $1$ | $T$ | $T$ |
| 1 | $2$ | $T/8$ | $T/4$ |
| 2 | $4$ | $T/64$ | $T/16$ |
| 3 | $8$ | $T/512$ | $T/64$ |
| $n$ | $2^n$ | $T/8^n$ | $T/4^n$ |

Individual triangles shrink by a factor of eight; the total area of each generation shrinks by a factor of four.

### Proposition 22: every finite sum remains inside the segment

For any finite stage,

$$
S_n=T+\frac T4+\frac{T}{4^2}+\cdots+\frac{T}{4^n}
$$

is the area of an inscribed polygon. Therefore

$$
S_n<A.
$$

The finite sums are genuine lower approximations to the segment's area.

### Proposition 23: the exact finite summation identity

For successively quartered magnitudes, Archimedes proves the identity that, in modern notation, reads

$$
\boxed{
S_n+\frac13\frac{T}{4^n}=\frac43T.
}
$$

Equivalently,

$$
S_n=\frac43T-\frac{T}{3\cdot4^n}.
$$

This is a finite theorem. No infinite series needs to be assumed. It gives the exact difference between the polygonal area and the proposed answer.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p2-intervals.svg' | relative_url }}" alt="Six horizontal bars, one for each n from zero to five, each running from the inscribed sum Sn to K equals four thirds, with the exact gaps one third, one twelfth, one forty-eighth, and so on.">
<figcaption>The squeeze from below. Each row shows the interval from $S_n$ to $K=4T/3$; the gap is exactly $T/(3\cdot4^n)$. The intervals nest and shrink by a factor of four each time.</figcaption>
</figure>

### Proposition 24: the final geometric theorem

Let

$$
K=\frac43T.
$$

Archimedes rules out both alternatives:

- If $A<K$, Proposition 23 allows a finite inscribed polygon with area greater than $A$, which is impossible because every inscribed polygon lies inside the segment.
- If $A>K$, Proposition 20 allows the remaining uncovered area to become smaller than $A-K$. The polygon would then have area greater than $K$, contradicting Proposition 23.

Hence

$$
\boxed{A=K=\frac43T.}
$$

**Mid-post challenge.** Write out the two contradiction arguments in full, using explicit inequalities. In the case $A>K$, explain why Proposition 20 lets you choose a polygon whose omitted area is smaller than $A-K$, and why that forces the polygon's area to exceed $K$.

---

## 6. Why the factor $1/8$ appears

Take the segment bounded by

$$
y=1-x^2
\quad\text{and}\quad y=0,
\qquad -1\le x\le1.
$$

The first inscribed triangle has vertices

$$
A=(-1,0),\qquad P=(0,1),\qquad B=(1,0).
$$

Its area is

$$
T=\frac12(2)(1)=1.
$$

For the left residual segment, the chord $AP$ is

$$
y=x+1.
$$

Its midpoint has $x=-\tfrac12$, so the smaller segment's vertex is

$$
Q=\left(-\frac12,\frac34\right).
$$

At that $x$-coordinate, the chord has height $\tfrac12$, leaving a vertical separation of

$$
\frac34-\frac12=\frac14.
$$

Using vectors from $A$,

$$
P-A=(1,1),\qquad
Q-A=\left(\frac12,\frac34\right),
$$

the child triangle's area is

$$
\frac12
\left\lvert
1\cdot\frac34-1\cdot\frac12
\right\rvert
=\frac18.
$$

The other child has the same area. Their combined area is $1/4$ of the parent triangle's area.

In modern infinite-series language, the complete area is therefore

$$
A=1+\frac14+\frac1{16}+\cdots=\frac43.
$$

Archimedes obtains this conclusion through finite identities and exhaustion rather than modern limit notation.

---

## 7. Useful modern consequences

These formulas are modern restatements or deductions, not additional numbered propositions in the treatise.

### Area from base and height

For every parabolic segment,

$$
\boxed{A=\frac23bh.}
$$

For example, if $b=12$ and $h=5$,

$$
A=\frac23(12)(5)=40.
$$

### Area between a quadratic and a chord

For

$$
f(x)=ax^2+bx+c,\qquad a\ne0,
$$

take the chord joining the curve at $x=u$ and $x=v$, with $u<v$. Let its line be $\ell(x)$. Algebra gives

$$
\ell(x)-f(x)=a(x-u)(v-x).
$$

At the midpoint $x=(u+v)/2$, the magnitude of the vertical gap is

$$
\frac{\lvert a\rvert(v-u)^2}{4}.
$$

The inscribed triangle consequently has area

$$
T=\frac12(v-u)\frac{\lvert a\rvert(v-u)^2}{4}.
$$

Applying Archimedes' theorem gives

$$
\boxed{
A=\frac{\lvert a\rvert}{6}(v-u)^3.
}
$$

Although the chord may be sloped, the triangle-area calculation remains valid: its determinant equals the horizontal span times the corresponding vertical gap, divided by two.

### Exact error after a finite number of generations

If generations $0$ through $n$ have been added, then

$$
A-S_n=\frac{T}{3\cdot4^n}.
$$

Since $A=\tfrac43T$, the relative error is

$$
\boxed{\frac{A-S_n}{A}=\frac1{4^{n+1}}.}
$$

| Generations included | Fraction of the segment covered |
|---|---:|
| Initial triangle only | $75\%$ |
| Through generation 1 | $93.75\%$ |
| Through generation 2 | $98.4375\%$ |
| Through generation 3 | $99.609375\%$ |

These exact approximation rates follow from Propositions 23–24.

---

## 8. What makes the work important

The treatise connects three ideas that are often taught separately:

1. **Geometry** supplies the square law of the parabola and the exact ratios between successive triangles.
2. **Mechanics** supplies an independent route through balances and area comparisons.
3. **Exhaustion** turns arbitrarily accurate finite approximations into an exact equality.

The deepest point is that drawing more and more triangles is not, by itself, a proof. Archimedes separately establishes that the uncovered region can be made arbitrarily small and that the finite polygonal areas approach one specific candidate value. That combination — not merely recognizing the series $1+\tfrac14+\tfrac1{16}+\cdots$ — is the rigorous core of his quadrature.

---

## Final challenge

Archimedes never writes an infinite sum. Reconstruct his proof that $S=4T/3$ using only these three ingredients:

1. every finite inscribed sum satisfies $S_n<S$;
2. the exact finite identity $S_n+\frac13\frac{T}{4^n}=\frac43T$;
3. the inscribed polygons exhaust the segment, so the uncovered area can be made smaller than any prescribed positive area.

Identify exactly where each ingredient is used, and explain why the argument fails if any one of them is removed.

*Next in the series: [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) turns the same exhaustion strategy on a curved surface and proves $A=4\pi R^2$ by a double contradiction.*

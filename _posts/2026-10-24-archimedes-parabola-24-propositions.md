---
title: "The Parabola That Refused to Be Squared — Until Archimedes Found 4/3 Hiding Inside It"
date: 2026-10-24 11:00:00
categories:
  - Archimedes
  - Mathematics
tags:
  - quadrature-of-the-parabola
  - method-of-exhaustion
  - parabolic-segment
  - geometric-series
  - archimedes
  - ancient-geometry
  - proof-by-contradiction
share: true
read_time: true
excerpt: "Archimedes' Quadrature of the Parabola proves that every parabolic segment is exactly four thirds of its inscribed vertex triangle. This is the proposition-by-proposition tour of all 24 results, with exact SVG reconstructions."
---

**Challenge to the reader:** Take the parabola $y=x^2$ with $A=(-1,1)$ and $B=(1,1)$. Compute the area of $\triangle APB$ and the area of the parabolic segment directly. Then verify that the tangent at $B$ meets the vertical line through $A$ at height $-3$, so that the auxiliary triangle $ADB$ has exactly four times the area of $\triangle APB$.

*Part 1 of nine in the series **The Archimedes Project: Every Result, Reconstructed**: [Guide]({% post_url 2026-10-24-archimedes-project-readers-guide %}) · **Part 1 — The Parabola's 24 Propositions** (this page) · [Part 2 — Two Proofs of 4/3]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) · [Part 3 — The Sphere's Surface]({% post_url 2026-10-24-archimedes-sphere-surface-area-exhaustion %}) · [Part 4 — Sphere and Cylinder]({% post_url 2026-10-24-archimedes-sphere-and-cylinder-results %}) · [Part 5 — On Spirals]({% post_url 2026-10-24-archimedes-on-spirals-28-propositions %}) · [Part 6 — Equilibrium I]({% post_url 2026-10-24-archimedes-equilibrium-of-planes-25-propositions %}) · [Part 7 — Equilibrium II]({% post_url 2026-10-24-archimedes-equilibrium-book-ii-centroids %}) · [Part 8 — Conoids and Spheroids]({% post_url 2026-10-24-archimedes-conoids-and-spheroids-32-propositions %}).*

Archimedes' *The Quadrature of the Parabola* establishes a result short enough to write in one line:

$$
\boxed{
\operatorname{Area}(\text{parabolic segment})
=\frac43\,\operatorname{Area}(\triangle APB).
}
$$

The treatise proves it twice — once with a mechanical argument about balances, once with a purely geometric argument about inscribed triangles and exhaustion — across 24 propositions. The formula is famous. What is less famous is how much precise geometry is packed into the proof.

**Why it matters.** The parabola is the first curved region in Western mathematics whose area is proved to be an exact rational multiple of a rectilinear figure. Not approximated. Not bounded between two close numbers. Exactly four thirds. That standard of proof — a finite construction, an inequality that can be made arbitrarily tight, and a contradiction that excludes every other value — is the ancestor of the rigorous integral.

---

## 1. What exactly is being measured?

Let $A$ and $B$ lie on a parabola. The chord $AB$ and the intervening arc enclose a **parabolic segment**. Let $P$ be the point on that arc where the tangent is parallel to $AB$. Archimedes calls $P$ the **vertex of the segment**. It need not be the vertex of the whole parabola, and the chord need not be perpendicular to the axis.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p1-segment.svg' | relative_url }}" alt="A parabola with an oblique chord AB, the point P where the tangent is parallel to the chord, the inscribed triangle APB, and the shaded parabolic segment.">
<figcaption>The segment is the region between the chord and the arc. The point $P$ is fixed by the condition that the tangent at $P$ is parallel to $AB$; the triangle $APB$ has the same base and the same perpendicular height as the segment.</figcaption>
</figure>

The theorem can be stated in three equivalent ways:

$$
\boxed{
S=\frac43\,T,
\qquad
S=\frac23\,bh,
\qquad
T=\frac34\,S,
}
$$

where $S$ is the segment's area, $T$ is the area of $\triangle APB$, $b$ is the chord length, and $h$ is the perpendicular distance from $P$ to the chord. The triangle occupies exactly three quarters of the segment; the two curved slivers outside it occupy the remaining quarter.

### What "quadrature" means

To **square** a region is to construct a square of equal area. Archimedes reduces the curved region to a rational multiple of a triangle, and a triangle to a square. In his introductory letter to Dositheus he explains that he first investigated the result mechanically and then demonstrated it geometrically. That order matters: the balance gave him the answer; the geometry gave him the proof.

---

## 2. The architecture of the treatise

The 24 propositions are not a single argument. They are two proofs with a shared geometric toolkit.

| Propositions | Subject | Role |
|---|---|---|
| 1–5 | Properties of parabolas | Supply the ratios used later |
| 6–13 | Balances, triangles, trapezoids | Build the mechanical area comparisons |
| 14–15 | Polygonal approximations | Trap the segment between finite sums |
| 16–17 | First quadrature | Prove the area theorem mechanically |
| 18–21 | Inscribed-triangle geometry | Establish the $1/8$ child ratio |
| 22–23 | Finite sums | Control the successive approximations |
| 24 | Second quadrature | Complete the geometric exhaustion proof |

The distinction between this treatise and *The Method* is worth keeping in view. The mechanical proof here is not an informal balancing of infinitely many line-sections. It uses finite triangles, finite trapezoids, finite bounds, and a final contradiction.

---

## 3. Propositions 1–5: the geometry of the parabola

The first five propositions are the grammar of the whole treatise. Archimedes treats the first three as known conic results rather than proving them from scratch.

### Proposition 1: the chord midpoint fixes the vertex

Let $M$ be the midpoint of chord $AB$. Draw through $M$ a line parallel to the parabola's axis, meeting the parabola at $P$. Then the tangent at $P$ is parallel to $AB$. Conversely, if the tangent at $P$ is parallel to $AB$, the axis-parallel line through $P$ bisects $AB$.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p1-prop1.svg' | relative_url }}" alt="The parabola y equals x squared, the chord from A at minus one comma one to B at one comma one, its midpoint M, the vertical diameter through M meeting the parabola at P, and the horizontal tangent at P parallel to the chord.">
<figcaption>Proposition 1: bisect the chord, drop the axis-parallel through the midpoint, and the point where it meets the parabola is the vertex $P$. The tangent there is parallel to the chord.</figcaption>
</figure>

For a modern check, take

$$
y=x^2,\qquad A=(a,a^2),\qquad B=(b,b^2).
$$

The chord slope is

$$
\frac{b^2-a^2}{b-a}=a+b.
$$

The midpoint has $x$-coordinate $(a+b)/2$, and the tangent slope at that coordinate is

$$
2\left(\frac{a+b}{2}\right)=a+b.
$$

So the tangent at $P$ is indeed parallel to $AB$.

### Proposition 2: the tangent intercept is bisected

With $P,M,A,B$ as above, let the tangent at $B$ meet the line $PM$ at $E$. Then

$$
\boxed{PM=PE.}
$$

In the symmetric model $y=x^2$, $A=(-a,a^2)$, $B=(a,a^2)$, we have $P=(0,0)$ and $M=(0,a^2)$. The tangent at $B$ is

$$
y=2ax-a^2,
$$

so its intersection with the diameter is $E=(0,-a^2)$. Hence $PM=a^2=PE$.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p1-prop2.svg' | relative_url }}" alt="The parabola y equals x squared with A at minus one comma one and B at one comma one, the tangents at A and B meeting at E below the vertex P, and the vertical diameter through P and the chord midpoint M.">
<figcaption>Proposition 2: the tangents at $A$ and $B$ meet at $E$ on the diameter, and $P$ bisects $EM$. The relation links the enclosing triangle to the inscribed triangle.</figcaption>
</figure>

### Proposition 3: the quadratic law of ordinates

Measured from $P$, distances along a diameter are proportional to the squares of corresponding transverse distances:

$$
\frac{PM}{PN}=\frac{AM^2}{RN^2},
$$

where $RN$ is parallel to $AM$ and $R$ lies on the parabola. This is the geometric content of $y=kx^2$. It is the square law that eventually produces the factor $1/8$ for an individual child triangle and $1/4$ for a whole generation.

### Proposition 4: a chord-relative proportionality

Let $M$ be the midpoint of $AB$ and $P$ the segment vertex. Through another point $R$ on the parabola, draw a line parallel to the axis, meeting $AB$ at $O$ and $AP$ at $F$. The proposition gives

$$
AM:MO=OF:FR
$$

with the appropriate arrangement of the points. Its role is to convert the square law into a relation between straight-line intercepts adapted to an arbitrary chord, including an oblique one.

### Proposition 5: the ratio that powers the mechanical proof

Through $A$, draw a line parallel to the axis. Let it meet the tangent at $B$ at $D$. Through a point $K$ on $AB$, draw an axis-parallel line meeting the parabola at $Q$ and $DB$ at $L$. Then

$$
\boxed{
\frac{QK}{LQ}=\frac{AK}{KB}.
}
$$

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p1-prop5.svg' | relative_url }}" alt="The enclosing triangle ADB with A at minus one comma one, D at minus one comma minus three, B at one comma one, a point K on the chord, the vertical through K meeting the parabola at Q and the tangent DB at L, and the ratio labels.">
<figcaption>Proposition 5: the parabola cuts the axis-parallel section $QL$ in the same ratio in which $K$ cuts the chord. The figure uses $K=(2/5,1)$; then $AK/KB=QK/LQ=7/3$.</figcaption>
</figure>

**Mid-post challenge.** Verify Proposition 5 for $K=(2/5,1)$ on the chord $y=1$. You should find $Q=(2/5,4/25)$ and $L=(2/5,-1/5)$, so that $QK=21/25$, $LQ=9/25$, and both ratios equal $7/3$.

This is the bridge to mechanics. Positions along the chord have become ratios between portions of parallel sections.

---

## 4. Propositions 6–13: the balance lemmas

The mechanical proof treats plane figures as uniform thin plates. Their weights are proportional to their areas, and the balance relation is

$$
W_1d_1=W_2d_2.
$$

But Archimedes needs more than two point weights. He needs to balance extended triangles and trapezoids.

### Propositions 6 and 7: balancing a triangle

In Proposition 6, a right triangle occupies one side of a balance with its height along an arm of length $L$. A counterweight at distance $L$ on the opposite side balances it when its area is one third of the triangle's area. Proposition 7 extends the result to a scalene triangle.

The modern explanation is the centroid. The triangular lamina has its centre of gravity at distance $L/3$ from the fulcrum. If $T$ is its area and $Z$ the balancing area, then

$$
ZL=T\frac L3,
\qquad\text{so}\qquad
Z=\frac T3.
$$

### Propositions 8 and 9: bounds for displaced triangles

These propositions bound the balancing area of a triangle that occupies a more restricted part of the arm. The balancing area lies between two comparison areas determined by the triangle's position and the lever-arm ratios.

### Propositions 10–13: one-sided and two-sided trapezoid bounds

Propositions 10 and 11 give one-sided bounds for trapezoids. Propositions 12 and 13 give both lower and upper bounds for a trapezoid positioned between two points of the arm. The conceptual pattern is simple: if an area $W$ lies entirely between distances $r$ and $s$ from the fulcrum, its moment is bounded by

$$
rW\leq \text{moment}\leq sW.
$$

The actual propositions use specific configurations and strict inequalities. Their purpose is to turn the curved-area problem into controlled finite comparisons.

---

## 5. Propositions 14–17: the first quadrature

### Propositions 14 and 15: trapping the segment

Construct the triangle $ADB$:

- $AD$ is parallel to the axis;
- $DB$ is tangent at $B$;
- $AB$ is the chord.

Divide $AB$ into equal parts and draw the corresponding parallel lines. This produces triangular and trapezoidal approximations. Archimedes proves that the area of $ADB$ lies between three times two suitable approximating sums:

$$
3L_n<[ADB]<3U_n.
$$

Proposition 14 handles a chord perpendicular to the axis; Proposition 15 handles the oblique chord. Refining the division squeezes the segment's area.

### Proposition 16: one third of the auxiliary triangle

The exhaustion argument establishes

$$
\boxed{S=\frac13[ADB],}
$$

where $S$ is the segment's area. The logic is a contradiction:

1. Suppose $S$ differs from $[ADB]/3$.
2. The difference is a positive area.
3. Refine the construction until the approximation error is smaller than that difference.
4. The established bounds become impossible.

### Proposition 17: the theorem in its usual form

The auxiliary triangle has four times the area of the inscribed triangle:

$$
[ADB]=4[APB].
$$

Therefore

$$
\boxed{
S=\frac13[ADB]=\frac43[APB].
}
$$

For $y=x^2$ with endpoints $(-a,a^2)$ and $(a,a^2)$, the inscribed triangle has area $a^3$. The tangent at $B$ meets the vertical line through $A$ at height $-3a^2$, so

$$
[ADB]=\frac12(4a^2)(2a)=4a^3.
$$

The ratio $4:1$ becomes transparent.

---

## 6. Propositions 18–24: the purely geometric proof

The second proof replaces balances with a recursive construction of inscribed triangles.

### Proposition 18: locating the vertex

The axis-parallel line through the midpoint of the chord meets the parabola at the vertex of the segment — the point of greatest perpendicular distance from the chord. This explains why $\triangle APB$ has the same base and height as the segment, and it supplies the construction for every smaller triangle added later.

### Proposition 19: the three-quarter height relation

The axis-parallel distance from the chord to the parabola at the midpoint is four thirds of the corresponding distance at a quarter-point:

$$
h_{\mathrm{mid}}=\frac43\,h_{\mathrm{quarter}}.
$$

In the symmetric model, the gap between the chord $y=a^2$ and the parabola is

$$
g(x)=a^2-x^2.
$$

Hence

$$
g(0)=a^2,\qquad
g(a/2)=\frac34a^2.
$$

This local $4:3$ relation is an ingredient in the child-triangle area calculation.

### Proposition 20: the first triangle exceeds half the segment

Archimedes proves, without assuming the final area formula,

$$
[APB]>\frac12S.
$$

A modern way to see the bound is to enclose the segment in the parallelogram formed by the chord, the parallel tangent at $P$, and the axis-parallel lines through the endpoints. Its area is twice the area of $\triangle APB$, and the segment lies strictly inside it. Therefore $S<2T$, so $T>S/2$.

The corollary is crucial. Repeated insertion of these triangles removes more than half of each remaining segment. The total remaining area can therefore be made smaller than any prescribed positive area.

### Proposition 21: each child triangle has one eighth of its parent's area

After inserting $\triangle APB$, two smaller parabolic segments remain. Inscribe the corresponding triangle in each. If the original triangle has area $T$, each new triangle has area

$$
\boxed{\frac T8}.
$$

Together they contribute

$$
\frac T8+\frac T8=\frac T4.
$$

Each triangle is one eighth; the whole next generation is one quarter.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p1-children.svg' | relative_url }}" alt="A parabolic segment with the first inscribed triangle, the two child triangles, and four grandchild triangles, colored by generation, with a legend giving areas T, T over 4, and T over 16.">
<figcaption>The recursive construction. Generation 0 contributes $T$; generation 1 contributes $2\cdot T/8=T/4$; generation 2 contributes $4\cdot T/64=T/16$. The individual triangles shrink by a factor of eight; each generation's total shrinks by a factor of four.</figcaption>
</figure>

### Proposition 22: every finite sum stays inside the segment

The successive total areas added are

$$
T,\quad \frac T4,\quad \frac{T}{4^2},\quad \ldots.
$$

Every finite sum is less than the segment's area:

$$
\boxed{
T+\frac T4+\cdots+\frac{T}{4^n}<S.
}
$$

These are actual inscribed polygons, not numerical approximations.

### Proposition 23: the exact finite identity

For a finite sequence in which each term is one quarter of the preceding term,

$$
\boxed{
T+\frac T4+\cdots+\frac{T}{4^n}
+\frac13\frac{T}{4^n}
=\frac43T.
}
$$

In words: add one third of the last term to the finite sum, and the result is four thirds of the first term. Writing

$$
S_n=T+\frac T4+\cdots+\frac{T}{4^n},
$$

the identity becomes

$$
\boxed{
\frac43T-S_n=\frac{T}{3\cdot4^n}.
}
$$

This is more faithful to Archimedes than simply asserting an infinite-series formula. It is a finite theorem with an exact remainder.

<figure class="arch-fig">
<img src="{{ '/assets/archimedes/p1-series.svg' | relative_url }}" alt="A true-scale bar of total length four thirds of T divided into T, T over 4, T over 16, and smaller pieces, with the tail magnified sixteen times to show the exact remainder T over 768.">
<figcaption>The finite identity as a bar. The main bar is drawn to scale; the inset magnifies the tail from $1.25T$ to $4T/3$ by a factor of sixteen so that $T/16$, $T/64$, $T/256$, and the exact remainder $T/768$ become visible.</figcaption>
</figure>

### Proposition 24: the final exhaustion argument

Let

$$
K=\frac43T.
$$

Archimedes excludes both possible inequalities:

- If $S<K$, Proposition 23 allows an inscribed sum $S_n$ close enough to $K$ that $S_n>S$, contradicting Proposition 22.
- If $S>K$, Proposition 20's exhaustion corollary allows an inscribed polygon whose omitted area is smaller than $S-K$. That polygon must have area greater than $K$, contradicting Proposition 23.

Therefore

$$
\boxed{S=K=\frac43T.}
$$

**Mid-post challenge.** Prove Proposition 23 by induction on $n$. Start from $S_0=T$, and show that adding $T/4^{n+1}$ to $S_n$ while adjusting the remainder gives the same identity at $n+1$.

---

## 7. Why the factor $1/8$ appears: a worked derivation

Here is the coordinate reconstruction of Proposition 21.

Take

$$
y=x^2,
$$

with

$$
A=(-1,1),\qquad P=(0,0),\qquad B=(1,1).
$$

The first triangle has area

$$
T=\frac12(2)(1)=1.
$$

For the smaller segment between $A$ and $P$, the chord has slope $-1$. The tangent to $y=x^2$ has slope $2x$, so the next segment vertex is

$$
Q=\left(-\frac12,\frac14\right).
$$

The triangle $AQP$ has area

$$
[AQP]
=
\frac12\left\lvert
\det
\begin{pmatrix}
-1&1\\
-\frac12&\frac14
\end{pmatrix}
\right\rvert
=
\frac12\left(-\frac14+\frac12\right)
=
\frac18.
$$

By symmetry, the triangle on the other side also has area $1/8$. The next generation contributes $1/4$, as Proposition 21 states.

The scaling explanation is especially useful:

- each child's horizontal scale is $1/2$;
- its deviation from its own chord scales by $1/4$, because the curve is quadratic;
- area therefore scales by

$$
\frac12\cdot\frac14=\frac18.
$$

| Generation $n$ | Number of new triangles | Area of each | Total new area |
|---|---:|---:|---:|
| 0 | $1$ | $T$ | $T$ |
| 1 | $2$ | $T/8$ | $T/4$ |
| 2 | $4$ | $T/64$ | $T/16$ |
| 3 | $8$ | $T/512$ | $T/64$ |
| $n$ | $2^n$ | $T/8^n$ | $T/4^n$ |

---

## 8. Modern formulas that follow from the theorem

These are coordinate consequences of Archimedes' result, not additional propositions in his text.

### A parabolic cap of base $b$ and height $h$

A convenient equation is

$$
y=h\left(1-\frac{4x^2}{b^2}\right),
\qquad -\frac b2\leq x\leq \frac b2.
$$

Its area above the chord $y=0$ is

$$
\boxed{S=\frac23bh.}
$$

The segment occupies two thirds of its enclosing rectangle, and the principal inscribed triangle occupies three quarters of the segment. These are equivalent forms of the $4/3$ theorem.

### An arbitrary quadratic and an arbitrary chord

Let

$$
f(x)=\alpha x^2+\beta x+\gamma,
\qquad u<v,
$$

and let $\ell(x)$ be the line joining $(u,f(u))$ and $(v,f(v))$. Direct algebra gives

$$
\ell(x)-f(x)=\alpha(x-u)(v-x).
$$

The maximum vertical gap is therefore

$$
h_v=\frac{\lvert\alpha\rvert}{4}(v-u)^2.
$$

The inscribed triangle has area

$$
T=\frac12(v-u)h_v
=\frac{\lvert\alpha\rvert}{8}(v-u)^3.
$$

Applying Archimedes' theorem gives

$$
\boxed{
S=\frac{\lvert\alpha\rvert}{6}(v-u)^3.
}
$$

Notice that $\beta$ and $\gamma$ disappear. They alter the position and tilt, but not the chord-relative area over a fixed horizontal interval. The use of horizontal width and vertical gap here is a determinant-based area calculation; it does not identify the vertical gap with perpendicular height.

### Exact error after finitely many generations

Proposition 23 gives the exact omitted area:

$$
\boxed{
S-S_n=\frac{T}{3\cdot4^n}.
}
$$

Since $S=4T/3$, the relative error is

$$
\boxed{
\frac{S-S_n}{S}=\frac1{4^{n+1}}.
}
$$

The initial triangle leaves $25\%$ of the segment uncovered; including the next generation leaves $6.25\%$; including one more leaves $1.5625\%$.

**Mid-post challenge.** Show that the relative error after $n$ generations is exactly $1/4^{n+1}$ by substituting $S=4T/3$ into the remainder formula. Then compute the first $n$ for which the error is below $10^{-6}$.

---

## 9. What makes the treatise remarkable

The achievement is not only the value $4/3$, but the way Archimedes connects three kinds of reasoning:

1. **Conic geometry** supplies exact relations between chords, tangents, and ordinates.
2. **Mechanical comparison** turns those relations into area bounds.
3. **Exhaustion** converts arbitrarily close finite approximations into an exact equality.

In modern language, the geometric proof reads

$$
S=T\sum_{n=0}^{\infty}\frac1{4^n}
=\frac43T.
$$

But Archimedes' logical foundation is not an unexplained act of "adding infinitely many triangles." It is the combination of a finite identity, a proof that the remainder can be made arbitrarily small, and a contradiction argument excluding every other area.

That distinction is the central mathematical lesson of *The Quadrature of the Parabola*. The infinite series is the modern summary; the finite identity plus exhaustion is the proof.

---

## Final challenge

For an arbitrary quadratic $f(x)=\alpha x^2+\beta x+\gamma$ and chord endpoints $u<v$, prove that

$$
\ell(x)-f(x)=\alpha(x-u)(v-x),
$$

then derive

$$
S=\frac{\lvert\alpha\rvert}{6}(v-u)^3.
$$

Finally, explain why $\beta$ and $\gamma$ disappear, and why the result still holds when the chord is oblique.

*Next in the series: [Part 2 — Two Proofs, One Answer]({% post_url 2026-10-24-archimedes-parabola-4-3-two-proofs %}) reconstructs the mechanical and geometric proofs side by side, with the exact finite-sum squeeze that closes the argument.*


Archimedes’ *On Spirals* contains **28 propositions**. They fall into two main strands: properties of tangents to the spiral, and areas bounded by the spiral. Below is a catalogue covering the whole treatise, with closely related preliminary propositions grouped together. The formulas are modern restatements, not Archimedes’ original notation. [dokumen](https://dokumen.pub/the-works-of-archimedes-translation-and-commentary-2-9781139019279.html)

## Notation and definition

Archimedes defines the spiral by combining two uniform motions: a ray rotates about a fixed origin while a point moves outward along the ray at constant speed. In modern polar coordinates,

\[
r=a\theta,\qquad a>0,\quad \theta\geq0.
\]

Let \(d=2\pi a\) be the radial distance gained in one complete revolution. The “first circle” has radius \(d\), the second circle radius \(2d\), and the \(n\)-th circle radius \(nd\). [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

## 1. Preliminary results: Propositions 1–11

These are supporting lemmas rather than the principal results about spirals.

| Propositions | Content and purpose |
|---|---|
| 1–2 | Proportionality results for uniform motion: relating distances travelled and elapsed times. These underpin the relation between the rotation angle and the point’s distance from the origin. |
| 3–4 | Geometrical comparison and approximation lemmas used later in the tangent proofs. |
| 5–9 | Auxiliary circle-and-line constructions and inequalities, including *neusis*-type constructions—placing a straight line subject to prescribed intersection or length conditions—used in establishing the tangent results. |
| 10 | A sum-of-squares identity for lengths in arithmetic progression whose common difference equals the smallest term. |
| 11 | A related result for a more general arithmetic progression, supplying the square-sum comparisons needed in determining spiral areas. |

The first eleven propositions establish the machinery used in the two later strands; Propositions 10–11 belong especially to the area arguments. This table summarizes their roles rather than reproducing each preliminary enunciation in full. [dokumen](https://dokumen.pub/the-works-of-archimedes-translation-and-commentary-2-9781139019279.html)

For Proposition 10, if \(u_k=kh\), its identity can be written

\[
3\sum_{k=1}^{n}u_k^2
=(n+1)u_n^2+h\sum_{k=1}^{n}u_k.
\]

It is equivalent to the familiar formula

\[
\sum_{k=1}^{n}k^2=\frac{n(n+1)(2n+1)}6.
\]

This is the arithmetic behind summing the circular-sector approximations used later. [people.math.osu](https://people.math.osu.edu/sinnott.1/ReadingClassics/On%20Archimedian%20Spirals.pdf)

## 2. Basic properties of the spiral: Propositions 12–15

### Proposition 12 — Equally spaced angles give an arithmetic progression of radii

If successive rays from the origin meet the spiral at equal angular intervals, their lengths form an arithmetic progression:

\[
r_k=a(\theta_0+k\Delta\theta)
=r_0+ka\Delta\theta.
\]

Thus equal increments of angle produce equal increments of radius. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Proposition 13 — A line cannot touch the spiral at two distinct points

A straight line tangent to the spiral touches it at only one point.

Here “touch” concerns tangency: the statement should not be read as saying that a tangent line cannot intersect another portion of the spiral. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Proposition 14 — Radii on the first turn are proportional to the corresponding circular arcs

For two points on the first turn, their distances from the origin have the same ratio as the arcs swept out on the first circle:

\[
\frac{r_1}{r_2}=\frac{\theta_1}{\theta_2}.
\]

This expresses the defining proportionality geometrically, using circular arcs rather than numerical angles. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Proposition 15 — The same proportionality extends to later turns

For points on the second turn, one adds a complete circumference to the corresponding first-circle arcs. The corollary extends the rule to the \(n\)-th turn.

Writing \(\theta=2\pi(n-1)+\phi\), the modern statement is

\[
r=a\bigl(2\pi(n-1)+\phi\bigr).
\]

The completed revolutions must therefore be counted; the direction of a ray alone does not determine the spiral radius. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

## 3. Tangent results: Propositions 16–20

### Propositions 16–17 — Position of the tangent relative to the radius

These establish the acute/obtuse angle relations between the tangent and the radius at the point of contact: the appropriate angle on the forward side of the radius is obtuse, and the corresponding backward-side angle is acute. Together they handle the relevant turns of the spiral and establish the geometry needed for the subsequent tangent-length results. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Proposition 18 — The tangent at the end of the first turn determines a circle’s circumference

Let \(P\) be the endpoint of the first complete turn, so \(OP=d\). Draw the tangent at \(P\), and let it meet at \(T\) the line through \(O\) perpendicular to \(OP\). Then

\[
OT=2\pi d.
\]

Thus \(OT\) equals the circumference of the first circle. This converts a circular circumference into a straight segment, provided the spiral and its tangent are available. [dokumen](https://dokumen.pub/the-works-of-archimedes-translation-and-commentary-2-9781139019279.html)

### Proposition 19 — The corresponding result at the end of any complete turn

At the endpoint of the \(n\)-th turn, \(OP=nd\). With the same perpendicular-and-tangent construction,

\[
OT=n\bigl(2\pi OP\bigr)=2\pi n^2d.
\]

In words: the intercepted perpendicular segment equals \(n\) times the circumference of the \(n\)-th circle. [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

### Proposition 20 — The corresponding result at an arbitrary point

At any point \(P\), construct \(T\) by intersecting the tangent at \(P\) with the line through the origin perpendicular to \(OP\). The intercepted segment equals the circular arc swept through the full accumulated rotation, measured on the circle of radius \(OP\). In modern notation,

\[
OT=r\theta=\frac{r^2}{a}.
\]

For a point beyond the first turn, the arc measurement includes the appropriate number of complete circumferences. Propositions 18–19 are the complete-turn cases of this relation. [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

## 4. Area approximation: Propositions 21–23

These establish the exhaustion arguments required to calculate areas.

| Proposition | Result |
|---|---|
| 21 | The region bounded by the first complete turn and the initial line can be enclosed between inscribed and circumscribed figures made of circular sectors, with their area difference smaller than any prescribed positive area. |
| 22 | The analogous approximation is established for the second complete turn. |
| 23 | The construction extends to a general spiral portion, providing the approximation needed for the general area theorem. |

Their essential content is that the sector approximations can be made arbitrarily close—not merely that one can draw a rough inner and outer approximation. [dokumen](https://dokumen.pub/the-works-of-archimedes-translation-and-commentary-2-9781139019279.html)

## 5. Exact areas: Propositions 24–28

### Proposition 24 — The first-turn area is one-third of the first circle

The area enclosed by the first complete turn and the initial line is

\[
A_1=\frac13\pi d^2.
\]

The proposition also treats a portion of the first turn: its area is one-third of the corresponding circular sector whose radius is the final spiral radius. For an accumulated angle \(\beta\leq2\pi\), this becomes

\[
A(0,\beta)=\frac{a^2\beta^3}{6}
=\frac13\left(\frac12\beta(a\beta)^2\right).
\]

 [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Proposition 25 — The second-turn region is \(7/12\) of the second circle

The region bounded by the second turn and the segment of the initial line joining its endpoints has area

\[
A_2=\frac{7}{12}\pi(2d)^2
=\frac73\pi d^2.
\]

This is the region swept out during the second revolution, not just the shell lying between the first and second turns. [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

### Proposition 26 — General area of a spiral portion

Consider a forward spiral portion spanning at most one complete revolution. Let its endpoint radii be \(r_1,r_2\), with angular span \(\Delta\theta\). Its area, bounded by the spiral and the two endpoint radii, is

\[
A=\frac{\Delta\theta}{6}
\left(r_1^2+r_1r_2+r_2^2\right).
\]

Equivalently, relative to the circular sector of radius \(r_2\) and angle \(\Delta\theta\),

\[
\frac{A}{\tfrac12r_2^2\Delta\theta}
=
\frac{r_1^2+r_1r_2+r_2^2}{3r_2^2}.
\]

This is a modern algebraic rendering of Archimedes’ geometrical area ratio. [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

### Proposition 27 — Successive full-turn shells have areas in arithmetic progression

Let \(R_1\) be the first-turn area, and let \(R_n\), for \(n\geq2\), be the shell added between the \((n-1)\)-st and \(n\)-th turns. Then

\[
R_2=6R_1,
\]

and

\[
R_3=2R_2,\quad
R_4=3R_2,\quad \ldots,\quad
R_n=(n-1)R_2.
\]

Consequently,

\[
R_1:R_2:R_3:R_4:\cdots
=1:6:12:18:\cdots.
\]

The arithmetic progression applies to the added shells beginning with \(R_2\), not to all first-turn and shell areas starting with \(R_1\). [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

### Proposition 28 — Area ratio for the two parts of a partial shell

Take a spiral portion with endpoint radii \(r_1<r_2\). Draw circles centred at the origin with these radii. Inside the corresponding annular sector, the spiral divides the region into two pieces:

- \(L\): between the inner circle and the spiral;
- \(U\): between the spiral and the outer circle.

Archimedes gives their ratio, which can be written

\[
\frac{U}{L}
=
\frac{r_1+2r_2}{2r_1+r_2}.
\]

Equivalently, putting \(h=r_2-r_1\),

\[
\frac{U}{L}
=
\frac{r_1+\tfrac23h}{r_1+\tfrac13h}.
\]

This is the partial-shell counterpart of the full-shell comparisons in Proposition 27. [dokumen](https://dokumen.pub/the-works-of-archimedes-translation-and-commentary-2-9781139019279.html)

## What the famous constructions amount to

Two consequences are often mentioned alongside the treatise:

- Circle quadrature: Proposition 18 supplies a straight segment equal to a circle’s circumference. Together with the circle-area theorem from *Measurement of a Circle*, it enables construction of an equal-area triangle and hence an equal-area square, once the spiral tangent is available. [en.wikipedia](https://en.wikipedia.org/wiki/On_Spirals)
- Angle trisection—and more generally division into equal parts—follows from the proportionality of radius and accumulated angle. Dividing an appropriate radius in three and locating the corresponding point on the spiral divides the angle in three. This is a consequence of the spiral’s defining property, not an additional numbered proposition beyond the 28. [en.wikipedia](https://en.wikipedia.org/wiki/On_Spirals)

Neither is a construction using an unmarked straightedge and compass alone: access to the spiral, and for the circumference construction its tangent, enlarges the permitted tools. [en.wikipedia](https://en.wikipedia.org/wiki/Archimedean_spiral)

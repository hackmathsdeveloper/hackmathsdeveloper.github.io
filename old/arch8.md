
Archimedes’ *The Quadrature of the Parabola* establishes one central result:

\[
\boxed{\text{Area of a parabolic segment}
=\frac43\,\text{area of its inscribed vertex triangle}.}
\]

Equivalently, if the segment has base \(b\) and perpendicular height \(h\), its area is

\[
\boxed{A=\frac23bh.}
\]

The remarkable achievement is not merely the formula: Archimedes gives two different demonstrations, one using mechanics and one using geometry and **exhaustion**. The treatise contains 24 propositions that develop these arguments. Below, “all the results” refers to the results in this particular treatise, rather than all of Archimedes’ mathematical works. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/)

## 1. What exactly is being measured?

A parabolic segment is the region enclosed by:

- an arc of a parabola;
- a straight chord joining two points \(A\) and \(B\) on the parabola.

The chord need not be perpendicular to the parabola’s axis.

Let \(P\) be the point on the arc where the tangent is parallel to \(AB\). Archimedes calls this the vertex of the segment. It need not be the vertex of the entire parabola.

The triangle \(APB\) has the same base and height as the segment. Archimedes proves

\[
\operatorname{Area}(\text{segment})
=\frac43\operatorname{Area}(\triangle APB).
\]

Since the triangle’s area is \(\tfrac12bh\), the segment’s area is \(\tfrac23bh\). Thus the triangle occupies three quarters of the segment, and the curved regions outside it occupy the remaining quarter. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### What “quadrature” means

The objective is to determine the curved region’s area in terms of a rectilinear figure whose area is already understood. Archimedes achieves this by proving an exact ratio to a triangle, rather than merely finding a numerical approximation. In his letter introducing the work, he describes the problem as squaring the segment bounded by a straight line and a parabola. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/)

## 2. How the treatise is organized

The logical structure is:

| Propositions | Purpose |
|---|---|
| 1–5 | Establish or recall properties of parabolas needed later |
| 6–13 | Develop balance results for triangles and trapezoids |
| 14–15 | Apply those results to polygonal approximations of parabolic segments |
| 16–17 | Complete the first quadrature |
| 18–21 | Develop the inscribed-triangle construction |
| 22–23 | Establish finite approximation and summation results |
| 24 | Complete the purely geometric quadrature |

An important historical distinction: the mechanical argument in this treatise is not simply the later argument in *The Method* in which one informally balances collections of line-sections. Here, the first proof works through finite triangles, trapezoids, bounds, and a final contradiction argument. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 3. Propositions 1–5: the geometry of the parabola

Archimedes begins with properties that make the later area arguments possible. The following are explanatory paraphrases, with modern notation where useful. The first three properties are cited as results already known from earlier conic geometry, rather than proved afresh in this treatise. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 1: chord midpoint and parallel tangent

Let a line through \(P\), parallel to the parabola’s axis, meet a chord \(AB\) at \(M\).

Then:

\[
AM=MB
\quad\Longleftrightarrow\quad
\text{the tangent at }P\text{ is parallel to }AB.
\]

This gives a construction for the segment’s vertex:

1. Bisect the chord.
2. Draw through its midpoint a line parallel to the parabola’s axis.
3. Take its intersection with the parabolic arc.

The resulting point is \(P\). [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 2: the tangent intercept is bisected

With \(P,M,A,B\) as above, let the tangent at \(B\) meet the line \(PM\) at \(E\). Then

\[
PM=PE.
\]

Thus \(P\) bisects the relevant intercept between the chord and the endpoint tangent. This relation later connects an enclosing triangle with the inscribed triangle. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 3: distances along a diameter vary as squares of ordinates

The parabola has a square-law property: transverse distances squared are proportional to corresponding distances measured along a diameter.

In suitable coordinates this becomes

\[
y=kx^2,
\]

or, for two points,

\[
\frac{y_1}{y_2}=\frac{x_1^2}{x_2^2}.
\]

Archimedes states this geometrically, not through coordinate equations. The square law is what ultimately produces the ratios \(1/8\) for individual child triangles and \(1/4\) for successive generations of triangles. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 4: a chord-relative proportionality

Archimedes next derives a proportion relating intersections of:

- the chord;
- a side of the inscribed triangle;
- a line parallel to the parabola’s axis;
- the parabola itself.

Its role is to translate the preceding square-law property into a form adapted to an arbitrary chord, including an oblique one. In Heath’s commentary, this can be understood as changing from tangent-and-diameter coordinates to coordinates based on the chord and a parallel diameter. [piratesandrevolutionaries.blogspot](https://piratesandrevolutionaries.blogspot.com/2014/04/archimedes-quadrature-of-parabola-prop4.html)

### Proposition 5: the section ratio inside an enclosing triangle

Draw through one endpoint of the chord a line parallel to the axis, and draw the tangent at the other endpoint. These lines and the chord form an enclosing triangle.

A line through this triangle parallel to the axis is divided by the parabola in a ratio determined by the corresponding division of the chord.

This is the geometric bridge to the mechanical argument: positions along the chord become ratios between portions of parallel sections. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 4. Propositions 6–17: the mechanical quadrature

### The underlying idea

Imagine plane figures as uniform thin plates. Their weights are proportional to their areas.

A balance relates a weight to its distance from the fulcrum. Archimedes uses this to obtain area comparisons, but the proof proceeds through finite geometric figures and inequalities—not through modern integrals. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Propositions 6–13: balance lemmas

These eight propositions establish the mechanical tools.

| Proposition | Result and purpose |
|---|---|
| 6 | In a specified right-triangle balance configuration, the area balancing the triangle at the prescribed opposite point equals one third of the triangle’s area. |
| 7 | Extends the corresponding one-third result to a scalene triangle in the prescribed configuration. |
| 8 | Bounds the balancing area of a displaced right triangle between two comparison areas. |
| 9 | Gives the analogous bounds for a scalene triangle. |
| 10 | Establishes an upper bound for the balancing area of a right-angled trapezoid whose nonparallel sides converge toward a specified point. |
| 11 | Gives a corresponding trapezoid bound in a more general configuration. |
| 12 | Establishes both lower and upper comparison bounds for another trapezoid configuration. |
| 13 | Extends these two-sided bounds to the corresponding general trapezoid. |

These are configuration-dependent statements. Proposition 6, for example, does not say that every triangle balances one third of its area at arbitrary distances. The prescribed positions and lever lengths are essential. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Propositions 14–15: polygonal bounds for the segment

Archimedes divides the chord into equal parts and constructs triangles and trapezoids associated with the parabola.

- Proposition 14 treats a chord perpendicular to the axis.
- Proposition 15 treats the oblique-chord case.

The balance lemmas yield an inner polygonal area \(L\) and an outer polygonal area \(U\) such that, for the enclosing triangle of area \(C\),

\[
3L<C<3U.
\]

Equivalently,

\[
L<\frac C3<U.
\]

The parabolic segment is also trapped between the polygonal approximations. This prepares an exhaustion argument comparing its area with \(C/3\). [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 16: the segment is one third of the enclosing triangle

Refining the construction makes the difference between the bounding areas sufficiently small to rule out either inequality

\[
A_{\text{segment}}>\frac C3
\qquad\text{or}\qquad
A_{\text{segment}}<\frac C3.
\]

Therefore,

\[
\boxed{A_{\text{segment}}=\frac C3.}
\]

Here the enclosing triangle is the one formed by the chord, the axis-parallel line through one endpoint, and the tangent at the other. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 17: the first proof of the \(4/3\) theorem

The enclosing triangle has four times the area of the inscribed vertex triangle \(T\). Hence

\[
A_{\text{segment}}
=\frac13(4T)
=\frac43T.
\]

This completes the first quadrature. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 5. Propositions 18–24: the purely geometric quadrature

The second proof replaces balances with a recursive construction of inscribed triangles.

### Proposition 18: locating the segment’s vertex

The axis-parallel line through the midpoint of the chord meets the parabola at the vertex of the segment.

This gives the construction required not only for the original triangle but also for every smaller triangle added later. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 19: the three-quarter height relation

Draw axis-parallel distances from the chord to the curve:

- one at the chord’s midpoint;
- another at the midpoint of either half of the chord.

The central distance is \(4/3\) of the quarter-position distance. Equivalently,

\[
h_{\text{quarter}}=\frac34h_{\text{middle}}.
\]

In the normalized modern model

\[
y=1-x^2,\qquad -1\le x\le1,
\]

this appears as

\[
y(0)=1,\qquad y\!\left(\frac12\right)=\frac34.
\]

This height relation is an ingredient in the child-triangle area calculation. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 20: the inscribed triangle exceeds half the segment

If \(T\) is the area of the inscribed vertex triangle and \(A\) the area of the segment, then

\[
T>\frac12A.
\]

The immediate consequence is crucial: after removing that triangle, less than half the segment remains.

Repeat the construction in each remaining segment. At every round, more than half of each residual segment is removed. Consequently, the total remainder can be made smaller than any assigned positive area. This is the geometric justification that the construction exhausts the segment. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 21: each child triangle has one eighth of its parent’s area

The first triangle leaves two smaller parabolic segments.

Inscribe a vertex triangle in each. Archimedes proves that each new triangle has area

\[
\frac18T.
\]

Together, therefore, they have area

\[
2\cdot\frac18T=\frac14T.
\]

Repeating this construction gives:

| Generation | Number of triangles | Area of each | Total area added |
|---|---:|---:|---:|
| 0 | \(1\) | \(T\) | \(T\) |
| 1 | \(2\) | \(T/8\) | \(T/4\) |
| 2 | \(4\) | \(T/64\) | \(T/16\) |
| 3 | \(8\) | \(T/512\) | \(T/64\) |
| \(n\) | \(2^n\) | \(T/8^n\) | \(T/4^n\) |

The distinction matters: individual triangles shrink by a factor of eight, while the total area of each generation shrinks by a factor of four. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 22: every finite sum remains inside the segment

For any finite stage,

\[
S_n=T+\frac T4+\frac{T}{4^2}+\cdots+\frac{T}{4^n}
\]

is the area of an inscribed polygon. Therefore,

\[
S_n<A.
\]

This establishes that the finite sums are genuine lower approximations to the segment’s area. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 23: the exact finite summation identity

For successively quartered magnitudes, Archimedes proves the identity that, in modern notation, reads

\[
\boxed{
S_n+\frac13\frac{T}{4^n}=\frac43T.
}
\]

Equivalently,

\[
S_n=\frac43T-\frac{T}{3\cdot4^n}.
\]

This is a finite theorem: no infinite series needs to be assumed. It gives the exact difference between the polygonal area and the proposed answer. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 24: the final geometric theorem

Let

\[
K=\frac43T.
\]

Archimedes rules out both alternatives:

- If \(A<K\), Proposition 23 allows a finite inscribed polygon with area greater than \(A\), which is impossible.
- If \(A>K\), Proposition 20 allows the remaining uncovered area to become smaller than \(A-K\). The polygon would then have area greater than \(K\), contradicting Proposition 23.

Hence

\[
\boxed{A=K=\frac43T.}
\]

This completes the second proof. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 6. Why the factor \(1/8\) appears: a modern worked reconstruction

The following coordinate calculation explains Proposition 21; it is not Archimedes’ original notation.

Take the segment bounded by

\[
y=1-x^2
\quad\text{and}\quad y=0,
\qquad -1\le x\le1.
\]

The first inscribed triangle has vertices

\[
A=(-1,0),\qquad P=(0,1),\qquad B=(1,0).
\]

Its area is

\[
T=\frac12(2)(1)=1.
\]

For the left residual segment, the chord \(AP\) is

\[
y=x+1.
\]

Its midpoint has \(x=-\tfrac12\), so the smaller segment’s vertex is

\[
Q=\left(-\frac12,\frac34\right).
\]

At that \(x\)-coordinate, the chord has height \(\tfrac12\), leaving a vertical separation of

\[
\frac34-\frac12=\frac14.
\]

Using vectors from \(A\),

\[
P-A=(1,1),\qquad
Q-A=\left(\frac12,\frac34\right),
\]

the child triangle’s area is

\[
\frac12
\left|
1\cdot\frac34-1\cdot\frac12
\right|
=\frac18.
\]

The other child has the same area. Thus their combined area is \(1/4\) of the parent triangle’s area, exactly as Proposition 21 states. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

In modern infinite-series language, the complete area is therefore

\[
A=1+\frac14+\frac1{16}+\cdots=\frac43.
\]

Archimedes obtains this conclusion through finite identities and exhaustion rather than modern limit notation. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 7. Useful modern consequences of his theorem

These formulas are modern restatements or deductions, not additional numbered propositions in the treatise.

### Area from base and height

For every parabolic segment,

\[
\boxed{A=\frac23bh.}
\]

For example, if \(b=12\) and \(h=5\),

\[
A=\frac23(12)(5)=40.
\]

This follows immediately from Archimedes’ triangle ratio. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/)

### Area between a quadratic and a chord

For

\[
f(x)=ax^2+bx+c,\qquad a\ne0,
\]

take the chord joining the curve at \(x=u\) and \(x=v\), with \(u<v\). Let its line be \(\ell(x)\). Algebra gives

\[
\ell(x)-f(x)=a(x-u)(v-x).
\]

At the midpoint \(x=(u+v)/2\), the magnitude of the vertical gap is

\[
\frac{|a|(v-u)^2}{4}.
\]

The inscribed triangle consequently has area

\[
T=\frac12(v-u)\frac{|a|(v-u)^2}{4}.
\]

Applying Archimedes’ theorem gives

\[
\boxed{
A=\frac{|a|}{6}(v-u)^3.
}
\]

Although the chord may be sloped, the triangle-area calculation remains valid: its determinant equals the horizontal span times the corresponding vertical gap, divided by two. This is a modern coordinate consequence of the arbitrary-chord theorem. [proofwiki](https://proofwiki.org/wiki/Quadrature_of_Parabola)

### Exact error after a finite number of generations

If generations \(0\) through \(n\) have been added, then

\[
A-S_n=\frac{T}{3\cdot4^n}.
\]

Since \(A=\tfrac43T\), the relative error is

\[
\boxed{\frac{A-S_n}{A}=\frac1{4^{n+1}}.}
\]

Thus:

| Generations included | Fraction of the segment covered |
|---|---:|
| Initial triangle only | \(75\%\) |
| Through generation 1 | \(93.75\%\) |
| Through generation 2 | \(98.4375\%\) |
| Through generation 3 | \(99.609375\%\) |

These exact approximation rates follow from Propositions 23–24. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 8. What makes the work important

The treatise connects three ideas that are often taught separately:

1. Geometry supplies the square law of the parabola and the exact ratios between successive triangles.
2. Mechanics supplies an independent route through balances and area comparisons.
3. Exhaustion turns arbitrarily accurate finite approximations into an exact equality. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

The deepest point is that drawing more and more triangles is not, by itself, a proof. Archimedes separately establishes that the uncovered region can be made arbitrarily small and that the finite polygonal areas approach one specific candidate value. That combination—not merely recognizing the series \(1+\tfrac14+\tfrac1{16}+\cdots\)—is the rigorous core of his quadrature. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

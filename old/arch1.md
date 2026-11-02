
Archimedes’ *The Quadrature of the Parabola* establishes that the area of a region bounded by a parabola and a straight chord is **four-thirds** the area of a particular inscribed triangle. It develops this result through 24 propositions and gives two proofs: one using the geometry of balances, and another using inscribed triangles and the method of exhaustion. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/)

I will interpret “all the results” as the results in this treatise, rather than Archimedes’ entire mathematical output. Below is a proposition-by-proposition account, followed by a detailed reconstruction of the main geometric proof. Modern coordinates will make the relationships explicit; they are explanatory additions, not Archimedes’ original notation.

## 1. Precisely what does Archimedes prove?

Let \(A\) and \(B\) lie on a parabola. The chord \(AB\) and the intervening parabolic arc enclose a parabolic segment.

Choose the point \(P\) on that arc where the tangent is parallel to \(AB\). Then

\[
\boxed{
\operatorname{Area}(\text{parabolic segment})
=\frac43\,\operatorname{Area}(\triangle APB).
}
\]

Equivalently, if the chord has length \(b\), and the perpendicular distance from \(P\) to the chord is \(h\),

\[
\boxed{
\operatorname{Area}(\text{parabolic segment})=\frac23bh.
}
\]

This is valid for oblique chords as well as chords perpendicular to the parabola’s axis. The “vertex of the segment” \(P\) need not be the vertex of the whole parabola. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

“Quadrature” means finding a square equal in area to a given region. Reducing the curved region to a rational multiple of a triangle therefore solves its quadrature. Archimedes states this result in his introductory letter to Dositheus, explaining that he first investigated it mechanically and then demonstrated it geometrically. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/)

## 2. The organization of the treatise

| Propositions | Subject | Role |
|---|---|---|
| 1–5 | Properties of parabolas | Supply the geometric ratios needed later |
| 6–13 | Balances, triangles, and trapezoids | Establish mechanical area comparisons |
| 14–15 | Approximations of parabolic segments | Apply those comparisons to the curved region |
| 16–17 | First quadrature | Prove the area theorem through mechanical comparisons and exhaustion |
| 18–21 | Inscribed-triangle geometry | Establish convergence and the \(1/8\) triangle ratio |
| 22–23 | Finite sums of areas | Control the successive approximations |
| 24 | Second quadrature | Complete a purely geometric exhaustion proof |

This division is important: propositions 6–17 are not merely an informal argument involving infinitely thin slices. The treatise uses finite constructions and inequalities to make the first proof rigorous. Its approach differs from the more familiar mechanical argument in Archimedes’ separate work *The Method*. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 3. Propositions 1–5: the underlying geometry of a parabola

### Proposition 1: a chord-midpoint and tangent relation

Let \(M\) be the midpoint of chord \(AB\). Draw through \(M\) a line parallel to the parabola’s axis, meeting the parabola at \(P\).

Then the tangent at \(P\) is parallel to \(AB\). Conversely, if the tangent at \(P\) is parallel to \(AB\), the axis-parallel line through \(P\) bisects \(AB\). [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

For a modern verification, take

\[
y=x^2,\qquad A=(a,a^2),\qquad B=(b,b^2).
\]

The chord slope is

\[
\frac{b^2-a^2}{b-a}=a+b.
\]

The midpoint has \(x\)-coordinate \((a+b)/2\), and the tangent slope at that coordinate is

\[
2\left(\frac{a+b}{2}\right)=a+b.
\]

This identifies the correct third vertex of the inscribed triangle.

### Proposition 2: equal intercepts on the segment’s diameter

Let the tangent at \(B\) intersect the line \(PM\) at \(E\). Then

\[
PE=PM.
\]

Thus the tangent intersection and the chord midpoint lie equally far from \(P\), on opposite sides. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

In the symmetric model

\[
y=x^2,\quad A=(-a,a^2),\quad B=(a,a^2),
\]

we have

\[
P=(0,0),\qquad M=(0,a^2).
\]

The tangent at \(B\) is

\[
y=2ax-a^2,
\]

so its intersection with \(x=0\) is \(E=(0,-a^2)\). The equality follows immediately.

### Proposition 3: the quadratic law of ordinates

Measured from \(P\), distances along a diameter are proportional to the squares of corresponding transverse distances:

\[
\frac{PM}{PN}
=
\frac{AM^2}{RN^2},
\]

where \(RN\) is parallel to \(AM\), and \(R\) lies on the parabola. This is the geometric content of a quadratic equation such as

\[
y=kx^2.
\]

Archimedes explicitly treats the first three propositions as established conic results, rather than giving proofs of them in this treatise. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 4: a chord-intersection ratio

Let \(M\) be the midpoint of \(AB\), and let \(P\) be the segment vertex. Through another point \(R\) on the parabola, draw a line parallel to the axis, meeting \(AB\) at \(O\) and the line \(AP\) at \(F\).

The proposition gives the ratio

\[
AM:MO=OF:FR,
\]

with the appropriate geometric arrangement of the points. It converts the quadratic relation of proposition 3 into a relation between straight-line intercepts. [piratesandrevolutionaries.blogspot](https://piratesandrevolutionaries.blogspot.com/2014/04/archimedes-quadrature-of-parabola-prop4.html)

Its significance is practical: ratios involving the curved boundary can now be compared with ratios in triangles.

### Proposition 5: the ratio used in the mechanical proof

Through \(A\), draw a line parallel to the axis. Let it meet the tangent at \(B\) at \(D\). Through a point \(K\) on \(AB\), draw an axis-parallel line meeting the parabola at \(Q\) and \(DB\) at \(L\).

Then

\[
\boxed{
\frac{QK}{LQ}=\frac{AK}{KB}.
}
\]

This relates the two pieces of a transverse line cut by the parabola to the two pieces of the original chord. It supplies the link between parabolic geometry and the lever comparisons that follow. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 4. Propositions 6–13: results about balances

These propositions use uniform plane figures as weights. With uniform density, their weights are proportional to their areas. The underlying balance relation is

\[
W_1d_1=W_2d_2.
\]

But Archimedes needs more than the balance of two point weights: he needs comparisons for extended triangles and trapezoids. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Propositions 6 and 7: balancing a triangle

In proposition 6, a right triangle occupies one side of a balance, with its height along an arm of length \(L\). A counterweight at distance \(L\) on the opposite side balances it when its area is one-third of the triangle’s area.

Proposition 7 establishes the corresponding result for a scalene triangle. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

The modern explanation uses the centroid: the relevant triangular lamina has its centre of gravity at distance \(L/3\) from the fulcrum. Thus, if \(T\) is its area and \(Z\) is the balancing area,

\[
ZL=T\frac L3,
\qquad\text{so}\qquad
Z=\frac T3.
\]

### Propositions 8 and 9: bounds for triangular weights

These consider triangles occupying a more restricted part of a balance arm.

- Proposition 8 treats a right triangle.
- Proposition 9 treats the corresponding scalene triangle.

They bound the balancing area between comparison areas determined by the triangle’s position and the lever-arm ratios. In the constructions of the text, the balancing area is smaller than the triangle itself but larger than a specified comparison area. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Propositions 10 and 11: one-sided bounds for trapezoids

These replace triangles with trapezoids.

- Proposition 10 treats the right-angled configuration.
- Proposition 11 gives the corresponding oblique configuration.

They show that the balancing area is smaller than a specified comparison area obtained from the trapezoid’s area and a lever-arm ratio. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Propositions 12 and 13: two-sided bounds for trapezoids

These establish both a lower and an upper bound on the balancing area of a trapezoid positioned between two points of the balance arm.

- Proposition 12 handles the right-angled arrangement.
- Proposition 13 handles the oblique analogue. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

The conceptual pattern is simple. If an area \(W\) lies entirely between distances \(r\) and \(s\) from a fulcrum, its moment is bounded by

\[
rW\leq \text{moment}\leq sW.
\]

Archimedes’ actual propositions use more specific configurations and strict inequalities. Their purpose is to turn the curved-area problem into controlled finite comparisons.

## 5. Propositions 14–17: the first quadrature

### Propositions 14 and 15: trapping the parabolic area

Construct the triangle \(ADB\) from proposition 5:

- \(AD\) is parallel to the parabola’s axis;
- \(DB\) is tangent at \(B\);
- \(AB\) is the segment’s chord.

Divide \(AB\) into equal parts and construct parallel lines, producing triangular and trapezoidal approximations associated with the segment.

Archimedes proves that the area of \(ADB\) lies between three times two suitable approximating sums:

\[
3L_n<[ADB]<3U_n.
\]

Proposition 14 handles a chord perpendicular to the axis; proposition 15 handles an oblique chord. The approximations are then used to squeeze the segment’s area. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 16: one-third of the auxiliary triangle

The exhaustion argument establishes

\[
\boxed{
S=\frac13[ADB],
}
\]

where \(S\) is the parabolic segment’s area. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

The logical mechanism is contradiction:

1. Suppose \(S\) differs from \([ADB]/3\).
2. The difference is a positive area.
3. Refine the construction until the approximation error is smaller than that difference.
4. The established bounds become impossible.

### Proposition 17: the main theorem in its usual form

The auxiliary triangle has four times the area of the inscribed triangle:

\[
[ADB]=4[APB].
\]

Therefore

\[
\boxed{
S=\frac13[ADB]=\frac43[APB].
}
\]

This completes the first proof. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

For example, for \(y=x^2\) with endpoints \((-a,a^2)\) and \((a,a^2)\),

\[
[APB]=a^3.
\]

The tangent at \(B\) meets the vertical line through \(A\) at height \(-3a^2\), so

\[
[ADB]=\frac12(4a^2)(2a)=4a^3.
\]

The ratio \(4:1\) becomes transparent.

## 6. Propositions 18–24: the purely geometric proof

### Proposition 18: locating the segment vertex

The axis-parallel line through the midpoint of the chord meets the parabola at the segment’s vertex: the point of greatest perpendicular distance from the chord. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

This explains why triangle \(APB\) has the same base and height as the segment.

### Proposition 19: midpoint and quarter-point heights

The axis-parallel distance from the chord to the parabola at the midpoint is four-thirds of the corresponding distance at a quarter-point:

\[
h_{\mathrm{mid}}=\frac43h_{\mathrm{quarter}}.
\]

 [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

For the symmetric model, the gap between the chord \(y=a^2\) and the parabola is

\[
g(x)=a^2-x^2.
\]

Hence

\[
g(0)=a^2,\qquad
g(a/2)=\frac34a^2.
\]

This local \(4:3\) relation helps establish the area ratios of the next triangles.

### Proposition 20: the first triangle occupies more than half the segment

Archimedes proves, without assuming the final area formula,

\[
[APB]>\frac12S.
\]

 [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

A modern way to see the bound is to enclose the segment in the parallelogram formed by:

- the chord;
- the parallel tangent at \(P\);
- the axis-parallel lines through the endpoints.

Its area is twice the area of \(APB\), and the segment lies strictly inside it.

The important corollary is that repeated insertion of these triangles makes the total remaining area smaller than any prescribed positive area. Each round removes more than half of what remains. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 21: each child triangle has one-eighth the parent’s area

After inserting \(APB\), two smaller parabolic segments remain. Inscribe the corresponding triangle in each.

If the original triangle has area \(T\), each new triangle has area

\[
\boxed{\frac T8}.
\]

Together, they contribute

\[
\frac T8+\frac T8=\frac T4.
\]

The distinction matters: each triangle is one-eighth, while the whole next generation is one-quarter. [en.wikipedia](https://en.wikipedia.org/wiki/Quadrature_of_the_Parabola)

### Proposition 22: every finite triangle sum remains below the segment

The successive total areas added are

\[
T,\quad \frac T4,\quad \frac{T}{4^2},\quad \ldots.
\]

Every finite sum is less than the segment’s area:

\[
\boxed{
T+\frac T4+\cdots+\frac{T}{4^n}<S.
}
\]

These are actual inscribed polygons, not merely numerical approximations. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

### Proposition 23: an exact finite geometric-sum identity

For a finite sequence in which each term is one-quarter of the preceding term,

\[
\boxed{
T+\frac T4+\cdots+\frac{T}{4^n}
+\frac13\frac{T}{4^n}
=\frac43T.
}
\]

In words: add one-third of the last term to the finite sum, and the result is four-thirds of the first term. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

Writing

\[
S_n=T+\frac T4+\cdots+\frac{T}{4^n},
\]

the identity becomes

\[
\boxed{
\frac43T-S_n=\frac{T}{3\cdot4^n}.
}
\]

This is more faithful to Archimedes’ proof than simply asserting an infinite-series formula.

### Proposition 24: the final exhaustion argument

Let

\[
K=\frac43T.
\]

Archimedes excludes both possible inequalities:

- If \(S<K\), proposition 23 allows an inscribed sum \(S_n\) close enough to \(K\) that \(S_n>S\), contradicting proposition 22.
- If \(S>K\), proposition 20’s exhaustion corollary allows an inscribed polygon whose omitted area is smaller than \(S-K\). That polygon must have area greater than \(K\), contradicting proposition 23.

Therefore

\[
\boxed{S=K=\frac43T.}
\]

This completes the second proof using finite constructions and contradiction. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 7. Why the one-eighth ratio holds: a worked derivation

Here is a modern coordinate reconstruction of proposition 21.

Take

\[
y=x^2,
\]

with

\[
A=(-1,1),\qquad P=(0,0),\qquad B=(1,1).
\]

The first triangle has area

\[
T=\frac12(2)(1)=1.
\]

For the smaller segment between \(A\) and \(P\), the chord has slope \(-1\). The tangent to \(y=x^2\) has slope \(2x\), so the next segment vertex is

\[
Q=\left(-\frac12,\frac14\right).
\]

The triangle \(AQP\) has area

\[
[AQP]
=
\frac12\left|
\det
\begin{pmatrix}
-1&1\\
-\frac12&\frac14
\end{pmatrix}
\right|
=
\frac12\left(-\frac14+\frac12\right)
=
\frac18.
\]

By symmetry, the triangle on the other side also has area \(1/8\). Thus the next generation contributes \(1/4\), as proposition 21 states. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

The scaling explanation is especially useful:

- each child’s horizontal scale is \(1/2\);
- its deviation from its own chord scales by \(1/4\), because the curve is quadratic;
- area therefore scales by

\[
\frac12\cdot\frac14=\frac18.
\]

Repeating the construction yields:

| Generation \(n\) | Number of new triangles | Area of each | Total new area |
|---|---:|---:|---:|
| 0 | \(1\) | \(T\) | \(T\) |
| 1 | \(2\) | \(T/8\) | \(T/4\) |
| 2 | \(4\) | \(T/64\) | \(T/16\) |
| 3 | \(8\) | \(T/512\) | \(T/64\) |
| \(n\) | \(2^n\) | \(T/8^n\) | \(T/4^n\) |

This is the geometric origin of the series used to describe the proof in modern notation. [en.wikipedia](https://en.wikipedia.org/wiki/Quadrature_of_the_Parabola)

## 8. Modern formulas that follow from the theorem

The following are coordinate consequences of Archimedes’ result, rather than additional propositions in his text.

### A parabolic cap of base \(b\) and height \(h\)

A convenient equation is

\[
y=h\left(1-\frac{4x^2}{b^2}\right),
\qquad -\frac b2\leq x\leq \frac b2.
\]

Its area above the chord \(y=0\) is

\[
\boxed{S=\frac23bh.}
\]

Thus the segment occupies two-thirds of its enclosing rectangle, or three-quarters of its own area is occupied by the principal inscribed triangle. These are equivalent forms of the \(4/3\) theorem. [britannica](https://www.britannica.com/topic/Quadrature-of-the-Parabola)

### An arbitrary quadratic and an arbitrary chord

Let

\[
f(x)=\alpha x^2+\beta x+\gamma,
\qquad u<v,
\]

and let \(\ell(x)\) be the line joining \((u,f(u))\) and \((v,f(v))\). Direct algebra gives

\[
\ell(x)-f(x)=\alpha(x-u)(v-x).
\]

The maximum vertical gap is therefore

\[
h_v=\frac{|\alpha|}{4}(v-u)^2.
\]

The inscribed triangle has area

\[
T=\frac12(v-u)h_v
=\frac{|\alpha|}{8}(v-u)^3.
\]

Applying Archimedes’ theorem gives

\[
\boxed{
S=\frac{|\alpha|}{6}(v-u)^3.
}
\]

Notice that \(\beta\) and \(\gamma\) disappear: they alter the position and tilt, but not this chord-relative area for a fixed horizontal interval. The use of horizontal width and vertical gap here is a determinant-based area calculation; it does not identify vertical gap with perpendicular height.

### Exact error after finitely many generations

Once the area theorem is established, proposition 23 gives the exact omitted area:

\[
\boxed{
S-S_n=\frac{T}{3\cdot4^n}.
}
\]

Since \(S=4T/3\), the relative error is

\[
\boxed{
\frac{S-S_n}{S}=\frac1{4^{n+1}}.
}
\]

For example, the initial triangle leaves \(25\%\) of the segment uncovered; including the next generation leaves \(6.25\%\); including one more leaves \(1.5625\%\). This exact error formula is the modern numerical reading of Archimedes’ finite-sum identity. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

## 9. What makes the treatise remarkable?

The achievement is not only the value \(4/3\), but the way Archimedes connects three kinds of reasoning:

1. Conic geometry supplies exact relations between chords, tangents, and ordinates.
2. Mechanical comparisons turn those relations into area bounds.
3. Exhaustion converts arbitrarily close finite approximations into an exact equality. [web.calstatela](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/QuadraturaParabolae/QP.contents.html)

In modern language, the geometric proof reads

\[
S=T\sum_{n=0}^{\infty}\frac1{4^n}
=\frac43T.
\]

But Archimedes’ logical foundation is not an unexplained act of “adding infinitely many triangles.” It is the combination of a finite identity, a proof that the remainder can be made arbitrarily small, and a contradiction argument excluding every other area. That distinction is the central mathematical lesson of *The Quadrature of the Parabola*. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/)

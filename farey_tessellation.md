
The figure is the **Farey tessellation** of the hyperbolic plane \(\mathbb H^2\), shown in the Poincaré disk model. Its vertices are all rational boundary points together with \(\infty\); its edges are hyperbolic geodesics connecting *Farey neighbours*. [warwick.ac](https://warwick.ac.uk/fac/sci/maths/people/staff/caroline_series/hypgeomandcntdfractions.pdf)

## Upper-half-plane construction

It is easiest to construct it first in the upper-half-plane model

\[
\mathbb H=\{z=x+iy:y>0\}.
\]

Here hyperbolic geodesics are:

- vertical lines \(x=c\), with endpoints \(c\) and \(\infty\);
- Euclidean semicircles orthogonal to the real axis.

Represent each ideal boundary point by a reduced fraction \(p/q\), with \(\infty=1/0\).

Two reduced fractions \(p/q\) and \(r/s\) are joined by an edge exactly when

\[
|ps-qr|=1.
\]

Such a pair is called a pair of Farey neighbours. Draw the semicircle with endpoints \(p/q\) and \(r/s\), or a vertical line if one endpoint is \(\infty\). Drawing every such edge yields the tessellation. [warwick.ac](https://warwick.ac.uk/fac/sci/maths/people/staff/caroline_series/hypgeomandcntdfractions.pdf)

## Recursive mediant algorithm

You can generate it without checking every determinant.

1. Start with the ideal triangle having vertices
   \[
   0/1,\qquad 1/1,\qquad 1/0=\infty.
   \]

2. Whenever an edge has Farey-neighbour endpoints
   \[
   \frac pq<\frac rs,
   \]
   insert their mediant
   \[
   \frac pq\oplus\frac rs
   =
   \frac{p+r}{q+s}.
   \]

3. Add the two geodesics
   \[
   \frac pq \longleftrightarrow \frac{p+r}{q+s},
   \qquad
   \frac{p+r}{q+s} \longleftrightarrow \frac rs.
   \]

4. Repeat independently for every newly created interval.

For example, the first subdivision of the base edge \(0/1\)--\(1/1\) inserts

\[
\frac01\oplus\frac11=\frac12.
\]

The next round gives

\[
\frac01\oplus\frac12=\frac13,
\qquad
\frac12\oplus\frac11=\frac23,
\]

then \(1/4,2/5,3/5,3/4,\ldots\). Every reduced rational appears after finitely many iterations, while irrational boundary points are limiting accumulation points of the construction. [warwick.ac](https://warwick.ac.uk/fac/sci/maths/people/staff/caroline_series/hypgeomandcntdfractions.pdf)

## Why the cells are ideal triangles

If \(p/q\) and \(r/s\) are neighbours, then the mediant makes two new neighbour pairs because

\[
\left|p(q+s)-q(p+r)\right|=|ps-qr|=1,
\]

and similarly for \((p+r)/(q+s)\) and \(r/s\). Thus subdivision preserves the admissible-edge condition.

The corresponding geodesics do not cross in the interior of \(\mathbb H\); they only share endpoints. The complementary components are therefore triangles whose vertices lie on \(\partial\mathbb H=\mathbb R\cup\{\infty\}\). These are *ideal triangles*, and their interiors cover \(\mathbb H\) disjointly. [warwick.ac](https://warwick.ac.uk/fac/sci/maths/people/staff/caroline_series/hypgeomandcntdfractions.pdf)

## Transfer to the disk

Your picture uses the disk model. Apply the Cayley transform, for example

\[
w=\frac{z-i}{z+i},
\]

which maps \(\mathbb H\) to the unit disk \(\mathbb D\). Under this map:

- \(\mathbb R\cup\{\infty\}\) maps to the unit circle;
- upper-half-plane geodesics map to circle arcs meeting the unit circle at right angles;
- the Farey ideal triangles map exactly to the curvilinear ideal triangles in the image.

Thus the apparent dense pattern near the circumference is not an additional rule: it is the image of rational endpoints with arbitrarily large denominators, which become increasingly fine near every point of the ideal boundary.

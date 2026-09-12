
https://tthtlc.github.io/rotating_cardiod_line4.html
https://tthtlc.github.io/cardiod_line3.html

The linked page appears to explore a **cardioid produced by perpendicular projections onto the tangent line of a circle**: a point \(B\) travels around a fixed circle, its tangent is drawn, and the perpendicular foot \(D\) of a fixed point \(C\) onto that tangent traces a cardioid when \(C\) lies on the circle. This is a rich construction because it connects Euclidean geometry, envelopes, parametrizations, loci, and numerical experimentation. [geogebra](https://www.geogebra.org/m/dkh6g2wn)

## Start with the core model

A convenient normalized setup is:

\[
A=(0,0), \qquad B(t)=(\cos t,\sin t), \qquad C=(a,0).
\]

The tangent at \(B(t)\) to the unit circle is

\[
x\cos t+y\sin t=1.
\]

The perpendicular projection \(D(t)\) of \(C\) onto this tangent is

\[
D(t)=C+\bigl(1-C\cdot B(t)\bigr)B(t),
\]

so explicitly,

\[
\begin{aligned}
x(t)&=a+\bigl(1-a\cos t\bigr)\cos t,\\
y(t)&=\bigl(1-a\cos t\bigr)\sin t.
\end{aligned}
\]

The cardioid case is \(a=1\), meaning \(C\) is on the circle. The general \(a\)-family is especially worth studying: it reveals exactly why the cardioid is a threshold case rather than an isolated curiosity.

## 30 explorations and variations

| # | Exploration | A concrete mathematical question |
|---:|---|---|
| 1 | Derive the locus analytically | Starting from the projection formula, derive \(x(t)\) and \(y(t)\) from first principles using dot products or normal vectors. |
| 2 | Obtain a polar equation | With origin at \(A\), find \(r(t)\) and \(\theta(t)\); determine whether the locus can be written in a simple polar form. |
| 3 | Eliminate the parameter | Eliminate \(t\) from the parametric equations to obtain an implicit Cartesian equation \(F(x,y)=0\). |
| 4 | Prove the cardioid condition | Prove rigorously that \(a=1\), and only \(a=1\), gives a cusp at the fixed point \(C\). |
| 5 | Classify all \(a\)-values | Study the locus for \(0<a<1\), \(a=1\), \(1<a<2\), \(a=2\), and \(a>2\). Identify smooth, cusped, self-intersecting, and looped regimes. |
| 6 | Locate singularities | Solve \(x'(t)=y'(t)=0\). Find when cusps or stationary points occur and relate them to the geometry. |
| 7 | Detect self-intersections | For which values of \(a\) do distinct parameters \(t_1\neq t_2\) yield the same point \(D\)? |
| 8 | Measure the inner loop | When \(a>1\), compute the area enclosed by the inner loop and investigate how it changes as \(a\) increases. |
| 9 | Compute enclosed area | Use Green’s theorem or a parametric area integral to calculate the area enclosed by the cardioid case. |
| 10 | Compute arc length | Set up the arc-length integral \(\int_0^{2\pi}\sqrt{x'(t)^2+y'(t)^2}\,dt\), simplify it, and compare with the known cardioid length. |
| 11 | Study curvature | Compute \(\kappa(t)\), identify maximum and minimum curvature, and see what happens near the cardioid cusp. |
| 12 | Find osculating circles | Construct or calculate the osculating circle at selected values of \(t\). How does its radius behave approaching the cusp? |
| 13 | Tangent-angle evolution | Find the slope or angle of the tangent to the locus as \(t\) varies. Compare it with the angle \(t\) of \(B\) on the original circle. |
| 14 | Normal-line geometry | Determine whether normals to the locus have an interesting envelope or pass through a recognizable auxiliary curve. |
| 15 | Evolute of the cardioid | Compute or plot the locus of centers of curvature. Investigate its cusps and symmetries. |
| 16 | Involute experiment | Starting from the cardioid, construct an involute by unwinding a taut string numerically or geometrically. |
| 17 | Vary the reference circle radius | Replace the unit circle by radius \(R\). Determine which features merely scale and which depend on \(a/R\). |
| 18 | Move \(C\) off the horizontal axis | Take \(C=(a\cos\phi,a\sin\phi)\). Prove that this is simply a rotation of the original family, and identify the rotation. |
| 19 | Put \(C\) inside the circle | Choose \(\lVert C\rVert<R\). Analyze the resulting curve: Does it remain convex? Does it have a cusp or loop? |
| 20 | Put \(C\) outside the circle | Choose \(\lVert C\rVert>R\). Determine precisely when loops form and how their size depends on distance from the center. |
| 21 | Use an arbitrary fixed point | Let \(C\) be any point in the plane, not necessarily constrained relative to the circle. Classify the locus entirely in terms of \(d=\lVert AC\rVert\). |
| 22 | Replace perpendicular projection by oblique projection | From \(C\), draw a line at a fixed angle \(\alpha\) to the tangent rather than a perpendicular. What locus results? Which \(\alpha\) produce cusps? |
| 23 | Project onto the normal instead | Project \(C\) onto the radial normal line through \(B\). Compare the locus with the tangent-projection construction. |
| 24 | Use a secant instead of a tangent | Let a line through \(B\) meet the circle again at \(E\); project \(C\) onto \(BE\). Let the secant direction vary according to a chosen rule. |
| 25 | Replace the circle by an ellipse | Let \(B\) move on \(x^2/p^2+y^2/q^2=1\), project \(C\) onto the tangent, and numerically investigate the new locus. |
| 26 | Replace the circle by a parabola | Let \(B\) move along \(y=x^2\); project a fixed point onto the tangent. Determine whether the locus is algebraic and calculate its degree. |
| 27 | Replace the circle by a general conic | Develop a computational framework for tangent projection from a fixed point to ellipses, hyperbolas, and parabolas. Compare singularities. |
| 28 | Interpret through pedal curves | Investigate whether the curve is a pedal curve, an inverse pedal curve, or closely related to one. Formulate the construction in the language of classical differential geometry. |
| 29 | Compare with rolling-circle cardioids | Compare this locus with the standard cardioid traced by a point on a circle rolling externally around an equal circle. Seek a direct transformation or shared parametrization. A cardioid also arises from that rolling construction.  [exo](http://www.exo.net/~pauld/activities/Cardiod_polar_plot.html) |
| 30 | Build an interactive research tool | Make a GeoGebra, Desmos, SVG/JavaScript, or Python tool with sliders for \(R\), \(a\), \(\phi\), and oblique angle \(\alpha\); automatically detect cusps, loops, curvature extrema, and enclosed area. |

## Stronger research directions

### 1. A bifurcation study

This is perhaps the best single investigation. Normalize the circle to radius 1 and let the fixed point be \(C=(a,0)\). Then classify the family

\[
D_a(t)=\left(a+(1-a\cos t)\cos t,\ (1-a\cos t)\sin t\right).
\]

A compelling project question is:

> How does the topology and differential geometry of the tangent-projection locus change as the normalized distance \(a=\lVert AC\rVert/R\) crosses critical values?

You can organize it around:

- \(0\le a<1\): fixed point inside the circle.
- \(a=1\): cusp/cardioid transition.
- \(a>1\): appearance of an inner loop or other self-intersection behavior.
- Scaling invariance: only the ratio \(a/R\) matters.

This becomes a clean example of a one-parameter geometric bifurcation.

### 2. A projective and differential-geometry study

The tangent to a conic is naturally expressed through the conic’s dual curve. For a general parametrized curve \(\gamma(t)\), define the tangent line and project a fixed point \(C\) onto it. Then explore:

\[
D(t)=\operatorname{proj}_{T_{\gamma(t)}}(C).
\]

Questions include:

- What properties of \(\gamma\) determine cusp formation in \(D\)?
- Does \(D\) preserve or reflect symmetries of \(\gamma\)?
- What is the algebraic degree of the locus when \(\gamma\) is a conic?
- Which source curves yield rational projection loci?

This generalizes the cardioid page into a reusable theory of **fixed-point projections onto moving tangents**.

### 3. A complex-number formulation

Write the moving point on the unit circle as \(z=e^{it}\). Then the tangent condition can be written using \(z\), \(\bar z\), or real parts, and the projection mapping can be studied algebraically. This has several advantages:

- Rotations become multiplication by \(e^{i\phi}\).
- The off-axis location of \(C\) is handled naturally.
- Symmetry becomes transparent.
- Elimination may be easier with the substitution \(u=e^{it}\), where \(\bar u=1/u\).

A particularly satisfying objective is to derive the entire family of loci via a rational map of the unit circle and identify the algebraic curve that results.

## Suggested progression

For a rigorous and visually satisfying sequence:

1. Reproduce the original cardioid construction dynamically.
2. Derive the parametric equations for \(D(t)\).
3. Introduce the distance parameter \(a=\lVert AC\rVert/R\).
4. Plot several cases, such as \(a=0\), \(a=0.5\), \(a=1\), \(a=1.2\), and \(a=2\).
5. Prove the cusp criterion by solving \(D_a'(t)=0\).
6. Compute one global invariant—preferably area or winding number.
7. Generalize to an ellipse and compare the singularity behavior.

The most promising outcome is not merely “another cardioid construction,” but a complete study of a **family of pedal-like loci arising from tangent-line projection**.

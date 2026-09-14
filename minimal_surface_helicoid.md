
https://www.perplexity.ai/search/c47dfc9c-9a3b-4347-9001-b64dfae2cf4f

A soap film spanning a **helical boundary** is obtained by minimizing surface area with that wire held fixed. For the canonical “helical wire plus its axis” frame, the resulting minimal surface is a **helicoid**—a ruled, screw-symmetric surface with zero mean curvature. Soap films at equilibrium satisfy \(H=0\), the Euler–Lagrange condition for the area functional. [princeton](https://www.princeton.edu/~stonelab/Teaching/FredBraszFinalPaper.pdf)

## 1. Specify the boundary

A single open helix is not, by itself, the boundary of an ordinary compact spanning surface: a surface boundary must be a closed curve (or a collection of curves). The standard physical setup is:

- a helical wire
  \[
  \mathbf c_1(v)=\bigl(a\cos v,\;a\sin v,\;bv\bigr),
  \qquad 0\le v\le V,
  \]
- the straight wire segment along the \(z\)-axis joining its endpoints,
  \[
  \mathbf c_0(v)=\bigl(0,\;0,\;bv\bigr),
  \qquad 0\le v\le V,
  \]
- plus short end connectors, if needed, to make the frame closed.

Here:

- \(a\) is the helix radius;
- \(b\) is the vertical rise per radian;
- the pitch per full turn is \(2\pi b\);
- \(V\) controls how many turns appear: \(N=V/(2\pi)\).

Dipping this “slinky plus central straw” type frame into soap solution produces a portion of a helicoid. [jimrolf](http://www.jimrolf.com/explorationsInComplexVariables/bookChapters/Ch2.pdf)

## 2. Use screw symmetry

The natural ansatz respects the symmetry of the boundary: as the surface rotates through angle \(v\), it also translates vertically by \(bv\). Parameterize it by

\[
\boxed{
\mathbf X(u,v)
=
\bigl(u\cos v,\;u\sin v,\;bv\bigr)
}
\]

with

\[
0\le u\le a,
\qquad
0\le v\le V.
\]

This surface has the desired boundary:

\[
\mathbf X(0,v)=(0,0,bv)=\mathbf c_0(v),
\]

and

\[
\mathbf X(a,v)=(a\cos v,a\sin v,bv)=\mathbf c_1(v).
\]

Geometrically, for each fixed \(v\), the parameter \(u\) traces a straight radial line from the axis to the helix. As \(v\) evolves, these lines rotate and rise, sweeping out the helicoid.

## 3. Derive the area functional

Differentiate:

\[
\mathbf X_u=(\cos v,\sin v,0),
\]

\[
\mathbf X_v=(-u\sin v,u\cos v,b).
\]

The area element is

\[
dA=\left\lVert \mathbf X_u\times\mathbf X_v\right\rVert\,du\,dv.
\]

The cross product is

\[
\mathbf X_u\times\mathbf X_v
=
\bigl(b\sin v,\;-b\cos v,\;u\bigr),
\]

so

\[
\left\lVert \mathbf X_u\times\mathbf X_v\right\rVert
=
\sqrt{u^2+b^2}.
\]

Therefore the area is

\[
A
=
\int_0^V\int_0^a \sqrt{u^2+b^2}\,du\,dv.
\]

Carrying out the \(u\)-integral,

\[
\boxed{
A
=
\frac{V}{2}
\left[
a\sqrt{a^2+b^2}
+
b^2\ln\!\left(
\frac{a+\sqrt{a^2+b^2}}{|b|}
\right)
\right].
}
\]

This calculates the area of the helicoidal patch. But to show that it is stationary under all boundary-preserving variations—not merely a plausible surface—you verify that it has zero mean curvature.

## 4. Verify minimal-surface equation

The first fundamental form coefficients are

\[
E=\mathbf X_u\cdot\mathbf X_u=1,
\]

\[
F=\mathbf X_u\cdot\mathbf X_v=0,
\]

\[
G=\mathbf X_v\cdot\mathbf X_v=u^2+b^2.
\]

A unit normal is

\[
\mathbf n
=
\frac{\mathbf X_u\times\mathbf X_v}
{\left\lVert\mathbf X_u\times\mathbf X_v\right\rVert}
=
\frac{(b\sin v,-b\cos v,u)}
{\sqrt{u^2+b^2}}.
\]

The second derivatives are

\[
\mathbf X_{uu}=0,
\]

\[
\mathbf X_{uv}=(-\sin v,\cos v,0),
\]

\[
\mathbf X_{vv}=(-u\cos v,-u\sin v,0).
\]

Hence the second fundamental form coefficients are

\[
e=\mathbf n\cdot\mathbf X_{uu}=0,
\]

\[
f=\mathbf n\cdot\mathbf X_{uv}
=
-\frac{b}{\sqrt{u^2+b^2}},
\]

\[
g=\mathbf n\cdot\mathbf X_{vv}=0.
\]

The mean curvature is

\[
H=\frac{eG-2fF+gE}{2(EG-F^2)}.
\]

Since \(e=g=F=0\),

\[
\boxed{H=0.}
\]

Thus the helicoid is a minimal surface. Equivalently, the first variation of the area vanishes for every sufficiently small deformation that leaves the wire boundary fixed. The general variational statement is that equilibrium soap films have vanishing mean curvature; in graph coordinates this arises as the Euler–Lagrange equation for the area functional. [princeton](https://www.princeton.edu/~stonelab/Teaching/FredBraszFinalPaper.pdf)

## 5. Generalization: two helical boundary wires

If the frame consists of two coaxial helices with the same pitch but radii \(r_1\) and \(r_2\),

\[
\mathbf c_i(v)
=
\bigl(r_i\cos v,\;r_i\sin v,\;bv\bigr),
\qquad i=1,2,
\]

then the helicoid strip

\[
\boxed{
\mathbf X(u,v)
=
(u\cos v,\;u\sin v,\;bv),
\qquad
r_1\le u\le r_2,\quad 0\le v\le V
}
\]

spans them. Its area is

\[
A
=
V\int_{r_1}^{r_2}\sqrt{u^2+b^2}\,du,
\]

or explicitly,

\[
A
=
\frac{V}{2}
\left[
u\sqrt{u^2+b^2}
+
b^2\ln\!\left(u+\sqrt{u^2+b^2}\right)
\right]_{r_1}^{r_2}.
\]

## Important qualification

“Minimal” has two related meanings:

- \(H=0\): the surface is an **area-stationary** minimal surface.
- Least area among all surfaces with the same boundary: the surface is a **global area minimizer**.

The helicoid always satisfies \(H=0\), so it is the correct local equilibrium equation for the soap film. But for a sufficiently long, wide, or complicated finite wire frame, global stability can be subtler: soap films can undergo instability, change topology, or select another spanning configuration. This is the distinction between solving the minimal-surface equation and solving the full Plateau problem for a particular closed wire frame. The general Plateau problem concerns least-area surfaces bounded by prescribed curves. [pi.math.cornell](https://pi.math.cornell.edu/~meadows/create/)

In short, for the standard helical frame the derivation is:

\[
\boxed{
\text{fixed helical boundary}
\;\Longrightarrow\;
\delta A=0
\;\Longrightarrow\;
H=0
\;\Longrightarrow\;
\mathbf X(u,v)=(u\cos v,u\sin v,bv),
}
\]

which is the helicoid.


The **Enneper surface** is one of the simplest complete nonplanar minimal surfaces in \(\mathbb R^3\). It has zero mean curvature everywhere, is conformally parameterized by the whole complex plane, and—unlike the helicoid, catenoid, or classical Scherk examples—is **self-intersecting**, so it is best regarded as a minimal immersion rather than an embedded soap-film surface. [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

## Standard parametrization

A common scaling of the classical Enneper surface is

\[
\boxed{
\mathbf X(u,v)=
\left(
u-\frac{u^3}{3}+uv^2,\;
v-\frac{v^3}{3}+u^2v,\;
u^2-v^2
\right),
\qquad (u,v)\in\mathbb R^2.
}
\]

Different references sometimes insert factors of \(1/2\), \(1/3\), or rescale the vertical coordinate. Those choices change the scale but not the geometry: all describe the same surface up to rigid motion and homothety. [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

In complex notation, set

\[
z=u+iv.
\]

Then one convenient expression is

\[
\boxed{
\mathbf X(z)
=
\operatorname{Re}
\left(
z-\frac{z^3}{3},\;
-i\left(z+\frac{z^3}{3}\right),\;
z^2
\right).
}
\]

Expanding its real part yields the real parametrization above, up to a harmless reflection or sign convention in the \(y\)-coordinate.

## Derivation from Weierstrass data

The Enneper surface is the canonical first example of the Weierstrass–Enneper representation. In one convention, a conformal minimal immersion is reconstructed from a meromorphic Gauss map \(g\) and a holomorphic differential \(dh\) by

\[
\mathbf X(z)
=
\operatorname{Re}
\int^z
\left(
\frac12\left(\frac1g-g\right),
\frac{i}{2}\left(\frac1g+g\right),
1
\right)dh.
\]

Choose the particularly simple data

\[
\boxed{
g(z)=z,
\qquad
dh=z\,dz.
}
\]

Then

\[
\frac12\left(\frac1g-g\right)dh
=
\frac12(1-z^2)\,dz,
\]

\[
\frac{i}{2}\left(\frac1g+g\right)dh
=
\frac{i}{2}(1+z^2)\,dz,
\]

\[
dh=z\,dz.
\]

After integration,

\[
\mathbf X(z)
=
\operatorname{Re}
\left(
\frac12\left(z-\frac{z^3}{3}\right),\;
\frac{i}{2}\left(z+\frac{z^3}{3}\right),\;
\frac{z^2}{2}
\right).
\]

Multiplying by \(2\) gives the standard scaled parametrization:

\[
\mathbf X(z)
=
\operatorname{Re}
\left(
z-\frac{z^3}{3},\;
i\left(z+\frac{z^3}{3}\right),\;
z^2
\right).
\]

Thus, Enneper’s surface is not found by guessing a graph \(z=u(x,y)\), as Scherk’s surface is. Instead, it is naturally constructed from holomorphic data. The Weierstrass representation guarantees conformality and \(H=0\) wherever the induced metric is nondegenerate. The classical choice \(g(z)=z\), \(dh=z\,dz\) is the standard Enneper datum. [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

## Direct verification of minimality

Write

\[
\mathbf X(u,v)
=
\left(
u-\frac{u^3}{3}+uv^2,\;
v-\frac{v^3}{3}+u^2v,\;
u^2-v^2
\right).
\]

Its first derivatives are

\[
\mathbf X_u
=
\left(
1-u^2+v^2,\;
2uv,\;
2u
\right),
\]

\[
\mathbf X_v
=
\left(
2uv,\;
1-v^2+u^2,\;
-2v
\right).
\]

They satisfy

\[
\mathbf X_u\cdot\mathbf X_v=0,
\]

and

\[
\lVert\mathbf X_u\rVert^2
=
\lVert\mathbf X_v\rVert^2
=
(1+u^2+v^2)^2.
\]

Therefore the induced first fundamental form is

\[
\boxed{
ds^2=(1+u^2+v^2)^2(du^2+dv^2).
}
\]

The parameters are **isothermal** or conformal: infinitesimal angles in the \((u,v)\)-plane are preserved by the map.

Each coordinate function is harmonic:

\[
\Delta x=0,\qquad \Delta y=0,\qquad \Delta z=0.
\]

For a conformal immersion, harmonicity of the coordinate functions is equivalent to vanishing mean-curvature vector. Hence

\[
\boxed{H=0.}
\]

This is the efficient direct route to minimality: rather than compute the full second fundamental form and then average the principal curvatures, use the conformal-harmonic characterization of minimal immersions.

## Curvature and completeness

For the normalization above, the Gaussian curvature is

\[
\boxed{
K(u,v)
=
-\frac{4}{(1+u^2+v^2)^4}.
}
\]

So:

- \(K<0\) everywhere;
- there are no flat points;
- the surface is locally saddle-shaped at every point;
- its curvature approaches \(0\) as \(u^2+v^2\to\infty\).

Because the conformal metric is

\[
ds^2=(1+r^2)^2(du^2+dv^2),
\qquad r^2=u^2+v^2,
\]

a radial path to \(r=\infty\) has intrinsic length

\[
\int_0^\infty (1+r^2)\,dr=\infty.
\]

Thus, the surface is **complete**: an observer constrained to move along it cannot reach its ideal end in finite intrinsic distance, even though the surface has only one topological end.

Its total Gaussian curvature is

\[
\boxed{
\int_{\text{Enneper}}K\,dA=-4\pi.
}
\]

This places it in the smallest nonzero finite-total-curvature class. A classical classification result states that the complete minimal surfaces in \(\mathbb R^3\) with total curvature \(-4\pi\) are, up to the relevant equivalences, the catenoid and the Enneper surface. [en.wikipedia](https://en.wikipedia.org/wiki/Enneper_surface)

## Polar form and symmetry

Let

\[
u=r\cos\theta,
\qquad
v=r\sin\theta.
\]

Then

\[
z=u^2-v^2=r^2\cos(2\theta).
\]

The horizontal complex coordinate \(x+iy\), up to a choice of orientation, can be arranged as

\[
x+iy
=
re^{i\theta}
-
\frac{r^3}{3}e^{-3i\theta}.
\]

This form displays the surface’s symmetry:

- the \(z\)-coordinate involves \(\cos(2\theta)\);
- the cubic term changes phase three times as \(\theta\) makes one revolution;
- the complete surface has threefold rotational symmetry about the \(z\)-axis, combined with reflection symmetries.

At the origin,

\[
\mathbf X(0,0)=(0,0,0),
\]

and the tangent plane is horizontal. The local Taylor expansion is

\[
x\approx u,\qquad y\approx v,\qquad z\approx u^2-v^2.
\]

Thus near the origin, Enneper’s surface resembles

\[
z=x^2-y^2,
\]

the familiar saddle. Far from the origin, the cubic horizontal terms dominate, the sheet folds over, and different parameter values map to the same point in \(\mathbb R^3\).

## Self-intersection and “end”

A crucial distinction is:

\[
\boxed{
\text{Enneper is complete and regular, but not embedded.}
}
\]

“Regular” means the differential has rank two at every point:

\[
\mathbf X_u\times\mathbf X_v\ne 0.
\]

Indeed, because

\[
\lVert\mathbf X_u\times\mathbf X_v\rVert
=
(1+u^2+v^2)^2>0,
\]

there are no branch points or singular points in the parametrization.

But global injectivity fails: distinct pairs \((u,v)\) can represent the same spatial point. Consequently, the outer portions of the surface pass through each other. The resulting self-intersection is not a singularity of the abstract minimal surface; it is a failure of the immersion to be one-to-one as a map into \(\mathbb R^3\). The classical Enneper surface is therefore a self-intersecting minimal immersion of \(\mathbb C\) into \(\mathbb R^3\). [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

The one end of the surface has multiplicity three. Informally, as \(r\to\infty\), the dominant term in the horizontal position is cubic in \(r\), and the normal direction covers the sphere once under the Gauss map \(g(z)=z\), while the surface develops its characteristic three-lobed, self-overlapping geometry.

## Relation to a physical soap film

Enneper’s surface is mathematically a minimal surface, but it is generally **not** the equilibrium film spanning an ordinary wire frame in the same direct way as a catenoid patch, helicoid patch, or finite Scherk patch.

There are two reasons:

- A real soap film is typically modeled as an embedded surface, possibly with singular junctions under the full physical Plateau laws; Enneper’s smooth immersion intersects itself transversely.
- The complete Enneper surface has no finite boundary. It is defined over the whole plane, so it is not directly a finite-boundary Plateau solution.

Nevertheless, a compact parameter-domain patch,

\[
D_R=\{(u,v):u^2+v^2\le R^2\},
\]

has boundary curve

\[
\Gamma_R(\theta)=\mathbf X(R\cos\theta,R\sin\theta).
\]

That patch is a stationary minimal surface bounded by \(\Gamma_R\). Whether it is the actual least-area soap film for that wire depends on the radius \(R\), allowed competitors, and stability. As \(R\) becomes large, self-overlap and instability make the physical interpretation increasingly delicate.

## Comparison with the other examples

| Surface | Standard representation | Global structure | Symmetry | Embedded? | Natural soap-film picture |
|---|---|---|---|---|---|
| Helicoid | \((u\cos v,u\sin v,bv)\) | Complete, one-ended | Screw symmetry | Yes | Helical wire with axis or matching helical boundaries |
| Scherk | \(z=\log(\cos y/\cos x)\) | Complete after periodic extension, multiple planar ends | Translational and reflection symmetry | Yes | Alternating vertical-wall or periodic frame |
| Enneper | \(\left(u-\frac{u^3}{3}+uv^2,\;v-\frac{v^3}{3}+u^2v,\;u^2-v^2\right)\) | Complete, one end, total curvature \(-4\pi\) | Threefold rotational and reflection symmetry | No; self-intersecting | Mainly an analytic and geometric model, rather than a generic stable film |

Enneper’s surface is especially important because it demonstrates that \(H=0\) is a local differential condition, not a guarantee that a surface is globally area-minimizing, physically stable, or embedded. It is one of the cleanest examples where complex analysis, conformal geometry, and the calculus of variations converge.

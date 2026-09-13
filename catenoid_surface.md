
The **catenoid** is the canonical minimal surface of revolution: rotate a catenary \(r=a\cosh(z/a)\) about its axis and you obtain a surface with zero mean curvature. Physically, it is the familiar hourglass-shaped soap film that can span two coaxial circular wire rings. [jfuchs.hotell.kau](https://jfuchs.hotell.kau.se/kurs/amek/prst/15_sofi.pdf)

## Geometry and parametrizations

Let the axis of rotation be the \(z\)-axis. A catenoid with neck radius \(a>0\), centered at \(z=z_0\), has generating curve

\[
\boxed{
r(z)=a\cosh\left(\frac{z-z_0}{a}\right).
}
\]

Rotating that curve gives the parametrization

\[
\boxed{
\mathbf X(v,\theta)
=
\left(
a\cosh v\cos\theta,\;
a\cosh v\sin\theta,\;
av+z_0
\right),
}
\]

where

\[
v\in\mathbb R,\qquad 0\le\theta<2\pi.
\]

Equivalently, with \(z=av+z_0\),

\[
\mathbf X(z,\theta)
=
\left(
a\cosh\left(\frac{z-z_0}{a}\right)\cos\theta,\;
a\cosh\left(\frac{z-z_0}{a}\right)\sin\theta,\;
z
\right).
\]

The narrowest horizontal circle occurs at \(z=z_0\):

\[
r(z_0)=a.
\]

This is the **neck**. The catenoid is symmetric under reflection through the plane \(z=z_0\), and its two ends expand exponentially:

\[
r(z)\sim \frac a2e^{|z-z_0|/a}
\qquad\text{as}\qquad |z|\to\infty.
\]

An implicit equation follows immediately:

\[
\boxed{
x^2+y^2
=
a^2\cosh^2\left(\frac{z-z_0}{a}\right).
}
\]

## Derivation by minimizing area

Consider a surface of revolution described by radius \(r(z)>0\) on \(z\in[z_1,z_2]\):

\[
\mathbf X(z,\theta)
=
\bigl(r(z)\cos\theta,\;r(z)\sin\theta,\;z\bigr).
\]

The two tangent vectors are

\[
\mathbf X_z
=
\bigl(r'(z)\cos\theta,\;r'(z)\sin\theta,\;1\bigr),
\]

\[
\mathbf X_\theta
=
\bigl(-r(z)\sin\theta,\;r(z)\cos\theta,\;0\bigr).
\]

Their cross product has magnitude

\[
\left\lVert\mathbf X_z\times\mathbf X_\theta\right\rVert
=
r(z)\sqrt{1+r'(z)^2}.
\]

Hence the surface area is

\[
\boxed{
A[r]
=
2\pi\int_{z_1}^{z_2}
r(z)\sqrt{1+r'(z)^2}\,dz.
}
\]

The Lagrangian is

\[
L(r,r')=r\sqrt{1+r'^2}.
\]

Because \(L\) does not explicitly depend on \(z\), the Beltrami identity gives a first integral:

\[
L-r'\frac{\partial L}{\partial r'}
=
\text{constant}.
\]

Now

\[
\frac{\partial L}{\partial r'}
=
\frac{rr'}{\sqrt{1+r'^2}},
\]

so

\[
r\sqrt{1+r'^2}
-
r'\frac{rr'}{\sqrt{1+r'^2}}
=
\frac{r}{\sqrt{1+r'^2}}
=
a,
\]

where the constant is denoted \(a>0\). Therefore

\[
\frac{r}{\sqrt{1+r'^2}}=a,
\]

or

\[
r'^2=\frac{r^2}{a^2}-1.
\]

Separating variables,

\[
\frac{dr}{\sqrt{r^2-a^2}}
=
\frac{dz}{a}.
\]

Integrating,

\[
\operatorname{arcosh}\left(\frac ra\right)
=
\pm\frac{z-z_0}{a}.
\]

Thus

\[
\boxed{
r(z)=a\cosh\left(\frac{z-z_0}{a}\right).
}
\]

This is the catenary; its surface of revolution is the catenoid. It is the only nonplanar minimal surface of revolution. [ugr](https://www.ugr.es/~jperez/papers/bamsJan11.pdf)

## Direct zero-curvature check

Use the conformal parametrization

\[
\mathbf X(v,\theta)
=
\left(
a\cosh v\cos\theta,\;
a\cosh v\sin\theta,\;
av
\right).
\]

The first derivatives are

\[
\mathbf X_v
=
\left(
a\sinh v\cos\theta,\;
a\sinh v\sin\theta,\;
a
\right),
\]

\[
\mathbf X_\theta
=
\left(
-a\cosh v\sin\theta,\;
a\cosh v\cos\theta,\;
0
\right).
\]

The first fundamental form coefficients are

\[
E=\mathbf X_v\cdot\mathbf X_v=a^2\cosh^2 v,
\]

\[
F=\mathbf X_v\cdot\mathbf X_\theta=0,
\]

\[
G=\mathbf X_\theta\cdot\mathbf X_\theta=a^2\cosh^2v.
\]

Therefore,

\[
\boxed{
ds^2=a^2\cosh^2v\,(dv^2+d\theta^2).
}
\]

So \((v,\theta)\) are conformal coordinates.

A compatible unit normal is

\[
\mathbf N
=
\left(
-\frac{\cos\theta}{\cosh v},\;
-\frac{\sin\theta}{\cosh v},\;
\tanh v
\right).
\]

The second fundamental coefficients are, up to the chosen orientation,

\[
e=a,\qquad f=0,\qquad g=-a.
\]

Thus the principal curvatures are

\[
\boxed{
k_1=\frac{1}{a\cosh^2v},
\qquad
k_2=-\frac{1}{a\cosh^2v}.
}
\]

They are equal in magnitude and opposite in sign, hence

\[
\boxed{
H=\frac{k_1+k_2}{2}=0.
}
\]

The Gaussian curvature is negative:

\[
\boxed{
K=k_1k_2
=
-\frac{1}{a^2\cosh^4v}.
}
\]

At the neck, \(v=0\),

\[
K(0)=-\frac1{a^2},
\]

so the saddle curvature is strongest there. Toward either end, \(\cosh v\to\infty\), and \(K\to0^-\).

## Two-ring soap film

Take two equal coaxial circular rings, each of radius \(R\), in the planes

\[
z=\pm h.
\]

A centered catenoid spanning them must satisfy

\[
\boxed{
R=a\cosh\left(\frac ha\right).
}
\]

Let

\[
t=\frac ha.
\]

Then

\[
a=\frac ht,
\qquad
R=\frac ht\cosh t,
\]

and hence

\[
\boxed{
\frac hR=\frac{t}{\cosh t}.
}
\]

This single dimensionless equation determines the possible catenoids.

The function

\[
f(t)=\frac{t}{\cosh t}
\]

has a maximum where

\[
f'(t)=0
\quad\Longleftrightarrow\quad
\cosh t-t\sinh t=0
\quad\Longleftrightarrow\quad
\boxed{t\tanh t=1.}
\]

Numerically,

\[
t\approx1.19968,
\]

so

\[
\boxed{
\left(\frac hR\right)_{\max}\approx0.66274.
}
\]

Since the full ring-to-ring separation is \(d=2h\),

\[
\boxed{
\frac dR\approx1.32549.
}
\]

Thus:

- if \(d/R>1.3255\), no catenoidal stationary soap-film solution exists;
- if \(d/R=1.3255\), the two catenoid branches merge at a limiting neck;
- if \(d/R<1.3255\), there are generally two catenoids: a thick-neck and a thin-neck branch.

Experimental and theoretical discussions often summarize this as the maximum separation being approximately \(1.33R\), with \(R\) the common ring radius. [astro.princeton](https://www.astro.princeton.edu/~burrows/classes/542/papers/soap.catenoid.0711.3256.pdf)

## Stability versus area competition

Solving \(H=0\) does **not** automatically mean the surface is a stable or globally area-minimizing film.

For equal rings separated by \(d=2h\):

| Regime | What happens |
|---|---|
| \(d/R>1.3255\) | No catenoid solution exists; the connected film must collapse or break |
| \(1.05\lesssim d/R<1.3255\) | A thick and a thin catenoid exist; the thick one is locally stable, but two flat disks have less total area |
| \(d/R\lesssim1.05\) | The thick-neck catenoid has less area than two disks and is the globally favorable idealized configuration |
| Thin-neck branch | It is an unstable stationary point: a perturbation tends to make the neck pinch or expand |

The comparison configuration consists of two planar disks, whose combined area is

\[
A_{\text{disks}}=2\pi R^2.
\]

For the catenoid, substitution of \(z=av\) into the area integral gives

\[
A_{\text{cat}}
=
2\pi a^2
\int_{-t}^{t}\cosh^2v\,dv
=
2\pi a^2\left(t+\sinh t\cosh t\right).
\]

Using \(R=a\cosh t\),

\[
\boxed{
\frac{A_{\text{cat}}}{2\pi R^2}
=
\frac{t+\sinh t\cosh t}{\cosh^2t}.
}
\]

The equality \(A_{\text{cat}}=2\pi R^2\) occurs at approximately

\[
\boxed{
\frac dR\approx1.055.
}
\]

So a catenoid can remain locally stable over a range in which two separate disks have lower total area. In a physical experiment, whether the film stays connected then depends on how it was formed, perturbations, air flow, liquid drainage, and whether the film has a pathway to break and reconfigure. The cited analysis gives approximately \(d/R\simeq1.33\) as the existence limit and \(d/R\simeq1.05\) as the area crossover with two disks. [astro.princeton](https://www.astro.princeton.edu/~burrows/classes/542/papers/soap.catenoid.0711.3256.pdf)

## Complex-analytic construction

The catenoid also emerges elegantly from Weierstrass data. Take the punctured complex plane

\[
M=\mathbb C\setminus\{0\},
\]

with

\[
\boxed{
g(w)=w,
\qquad
dh=\frac{dw}{w}.
}
\]

In the Weierstrass representation,

\[
\mathbf X(w)
=
\operatorname{Re}
\int
\left(
\frac12\left(g^{-1}-g\right),\;
\frac{i}{2}\left(g^{-1}+g\right),\;
1
\right)dh.
\]

If \(w=e^{v+i\theta}\), the real part of the integrated expression produces, up to rotation, translation, and scale,

\[
\mathbf X(v,\theta)
=
\left(
a\cosh v\cos\theta,\;
a\cosh v\sin\theta,\;
av
\right).
\]

The topology \(M=\mathbb C^\ast\) corresponds to a cylinder, which matches the catenoid’s topology:

\[
\boxed{
\text{genus}=0,\qquad
\text{two ends},\qquad
\text{one annular neck.}
\]

The catenoid has total Gaussian curvature

\[
\boxed{
\int_{\text{catenoid}}K\,dA=-4\pi.
}
\]

It is the unique complete embedded minimal annulus with finite total curvature, and the only nonplanar minimal surface of revolution. [ugr](https://www.ugr.es/~jperez/papers/bamsJan11.pdf)

## Catenoid–helicoid connection

The catenoid and helicoid are **conjugate minimal surfaces**: they arise from the same underlying Weierstrass data, with a phase rotation in the complex differential. Locally, they are isometric.

Their conformal metrics may be written in the same form:

\[
ds^2
=
a^2\cosh^2v\,(du^2+dv^2),
\]

after using suitable conformal coordinates for each. Yet their global embeddings differ dramatically:

- the catenoid is rotationally symmetric, embedded, and has two ends;
- the helicoid is screw-symmetric, embedded, and has one end;
- bending a local catenoid patch through the associated-family deformation can transform it continuously into a helicoid patch while preserving the intrinsic metric and minimality.

This association illustrates an important principle: a minimal surface’s intrinsic geometry need not uniquely determine how it sits in \(\mathbb R^3\).

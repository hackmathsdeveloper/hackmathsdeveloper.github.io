
The **Scherk surface** is a classical minimal surface that models a soap film separating space into alternating regions—rather like an infinite checkerboard of vertical walls joined by smooth saddle-shaped sheets. Unlike the helicoid, whose natural symmetry is screw motion, the standard Scherk surface has translational periodicity and four asymptotic vertical planar ends. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Scherk_surface)

## The standard equation

The most familiar form, often called the **doubly periodic Scherk surface** or Scherk’s first surface, is the graph

\[
\boxed{
z(x,y)=\log\!\left(\frac{\cos y}{\cos x}\right)
=
\log(\cos y)-\log(\cos x).
}
\]

It is defined wherever the logarithm is real:

\[
-\frac{\pi}{2}<x<\frac{\pi}{2},
\qquad
-\frac{\pi}{2}<y<\frac{\pi}{2}.
\]

Equivalently,

\[
\boxed{
e^z\cos x=\cos y.
}
\]

This implicit form is especially useful because it makes the symmetries and vertical asymptotes transparent. The equation is a standard representation of Scherk’s surface, and it is the unique minimal surface expressible as a translation graph \(z=f(x)+g(y)\), apart from the trivial affine-plane cases. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Scherk_surface)

## Derivation from the minimal-surface equation

For a graph \(z=u(x,y)\), the area of a patch over a planar domain \(D\) is

\[
A[u]
=
\iint_D
\sqrt{1+u_x^2+u_y^2}\,dx\,dy.
\]

Stationarity under variations \(u\mapsto u+\varepsilon\eta\), with \(\eta=0\) on the fixed boundary, yields the minimal-surface equation

\[
\boxed{
(1+u_y^2)u_{xx}
-2u_xu_yu_{xy}
+
(1+u_x^2)u_{yy}=0.
}
\]

This is equivalent to zero mean curvature, \(H=0\). [ias.ac](https://www.ias.ac.in/public/Volumes/pmsc/126/03/0421-0431.pdf)

Now impose the **translation-surface ansatz**

\[
u(x,y)=f(x)+g(y).
\]

Then

\[
u_x=f'(x),\qquad u_y=g'(y),
\]

\[
u_{xx}=f''(x),\qquad u_{yy}=g''(y),\qquad u_{xy}=0.
\]

The PDE reduces to

\[
\boxed{
\bigl(1+g'^2\bigr)f''
+
\bigl(1+f'^2\bigr)g''
=0.
}
\]

Divide by \((1+f'^2)(1+g'^2)\):

\[
\frac{f''}{1+f'^2}
+
\frac{g''}{1+g'^2}
=0.
\]

The first term depends only on \(x\), while the second depends only on \(y\). Therefore each must be constant:

\[
\frac{f''}{1+f'^2}=c,
\qquad
\frac{g''}{1+g'^2}=-c.
\]

Since

\[
\frac{d}{dx}\arctan f'= \frac{f''}{1+f'^2},
\]

integrating gives

\[
\arctan f'(x)=cx+\alpha,
\qquad
\arctan g'(y)=-cy+\beta.
\]

Thus

\[
f'(x)=\tan(cx+\alpha),
\qquad
g'(y)=\tan(-cy+\beta).
\]

After integrating one more time,

\[
f(x)=-\frac1c\log\cos(cx+\alpha)+C_1,
\]

\[
g(y)=\frac1c\log\cos(\beta-cy)+C_2.
\]

So the general nonplanar translation-type minimal graph is

\[
\boxed{
u(x,y)
=
\frac{1}{c}
\log
\left[
\frac{\cos(\beta-cy)}
{\cos(\alpha+cx)}
\right]
+C.
}
\]

Choosing \(c=1\), \(\alpha=\beta=C=0\) gives exactly

\[
u(x,y)=\log\left(\frac{\cos y}{\cos x}\right).
\]

That separation derivation explains why Scherk’s graph is exceptional: the minimal-surface PDE is nonlinear, but the additive form \(f(x)+g(y)\) reduces it to two solvable ordinary differential equations. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Scherk_surface)

## Geometry and asymptotic planes

The surface is saddle-like at the origin. Indeed,

\[
u(0,0)=0,
\qquad
u_x(0,0)=u_y(0,0)=0.
\]

Near \((0,0)\),

\[
\log\cos t
=
-\frac{t^2}{2}+O(t^4),
\]

so

\[
u(x,y)
=
\frac{x^2-y^2}{2}+O\!\left(x^4+y^4\right).
\]

Thus locally it resembles the hyperbolic paraboloid

\[
z\approx \frac{x^2-y^2}{2},
\]

with principal curvatures of opposite sign. As expected for a minimal surface, their average—mean curvature—is zero.

At the edges of the fundamental square:

\[
x\to\pm\frac{\pi}{2}
\quad\Longrightarrow\quad
\cos x\to0^+,
\quad\Longrightarrow\quad
z\to+\infty,
\]

while

\[
y\to\pm\frac{\pi}{2}
\quad\Longrightarrow\quad
\cos y\to0^+,
\quad\Longrightarrow\quad
z\to-\infty.
\]

So one fundamental patch has four vertical planar ends asymptotic to

\[
x=\pm\frac{\pi}{2},
\qquad
y=\pm\frac{\pi}{2}.
\]

This is why the surface looks like a smooth transition between four alternating vertical half-planes. In the quotient by its horizontal translations, the complete surface is typically described as doubly periodic and properly embedded, with parallel planar ends. [math.uci](https://www.math.uci.edu/~vmm/Surface/Minimal_Surfaces_2011_Matthias_Weber.pdf)

## Periodicity and reflection

The graph expression itself is not simply periodic in \(x\) or \(y\) alone, because changing \(x\) by \(\pi\) reverses the sign of \(\cos x\). But its **implicit equation**

\[
e^z\cos x=\cos y
\]

reveals useful rigid motions that preserve the complete surface.

For example,

\[
(x,y,z)\mapsto(x+\pi,y,-z)
\]

preserves the equation because

\[
e^{-z}\cos(x+\pi)
=
-e^{-z}\cos x,
\]

and, after rearrangement using \(e^z\cos x=\cos y\), this maps the surface onto itself when the appropriate reflected sheet is included. Similarly, reflections in the coordinate planes generate adjacent fundamental patches.

A convenient statement is:

- the basic graph lies over one square,
  \[
  \left(-\frac\pi2,\frac\pi2\right)^2;
  \]
- reflections across the vertical asymptotic planes extend it;
- the full extension forms an infinite periodic minimal surface.

In physical terms, the single graph patch is not usually the whole soap film. It is one chamber of an infinite periodic film whose adjacent chambers are obtained by symmetry.

## Relation to soap-film frames

A finite Scherk-type soap film can be approximated by a wire frame whose boundary lies in four nearly vertical planes and alternates between “upward” and “downward” sides. The prescribed boundary behavior is roughly

\[
u\to+\infty
\quad\text{on two opposite sides,}
\]

\[
u\to-\infty
\quad\text{on the other two sides.}
\]

This is the idealized infinite-boundary version. A physical finite frame replaces the infinite vertical asymptotes with tall finite wire edges, so the realized film is only approximately Scherk-like away from its boundary.

A useful comparison with the helicoid is:

| Feature | Helicoid | Scherk surface |
|---|---|---|
| Canonical equation | \(\mathbf X(u,v)=(u\cos v,u\sin v,bv)\) | \(z=\log(\cos y/\cos x)\) |
| Symmetry | Screw rotation plus translation | Reflections and horizontal periodic extension |
| Local shape | Twisted ruled saddle | Alternating saddle sheet |
| Natural idealized boundary | Helix and axis, or two helices | Four alternating vertical planar ends |
| Mean curvature | \(H=0\) | \(H=0\) |
| Gaussian curvature | Negative except on limiting behavior | Negative in the interior |
| Soap-film intuition | Spiral ramp or twisted sheet | A smooth separator of alternating vertical regions |

## Two classical meanings

The terminology can be confusing because “Scherk surface” is used for more than one closely related classical family.

### Doubly periodic Scherk surface

The graph

\[
z=\log\frac{\cos y}{\cos x}
\]

is the standard doubly periodic example. It has four families of planar ends in a fundamental cell and extends periodically through space. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Scherk_surface)

### Singly periodic Scherk surface

A different Scherk family is singly periodic and is often written, after scaling and rotation, in a form such as

\[
\boxed{
\sin z=\sinh x\,\sinh y.
}
\]

It repeats in one spatial direction and has four Scherk-type ends in a quotient by that period. More generally, the angle between its asymptotic half-planes can vary; this parameter controls the geometry of the four ends. The singly periodic family is naturally described via Weierstrass data on a four-punctured sphere. [math.uci](https://www.math.uci.edu/~vmm/Surface/Minimal_Surfaces_2011_Matthias_Weber.pdf)

These two families should not be confused:

- the graph \(z=\log(\cos y/\cos x)\) is the canonical doubly periodic form;
- the singly periodic family is a different complete embedding with one translational period and adjustable end angle.

## Complex-analytic viewpoint

Like the helicoid and catenoid, Scherk surfaces admit a Weierstrass–Enneper representation. Given a Riemann surface \(M\), meromorphic Gauss map \(g\), and height differential \(dh\), a conformal minimal immersion can be reconstructed as

\[
\mathbf X(p)
=
\operatorname{Re}
\int^p
\left(
\frac12(g^{-1}-g),
\frac{i}{2}(g^{-1}+g),
1
\right)dh.
\]

For the singly periodic Scherk surface, one standard choice is based on the four-punctured Riemann sphere, with punctures corresponding to the four Scherk ends; one cited formulation uses

\[
G(w)=w,
\qquad
dh=\frac{i\,w}{w^4-1}\,dw.
\]

The poles at the fourth roots of unity encode the asymptotic ends, while the period conditions determine whether the integral closes up to a spatial translation. [math.uci](https://www.math.uci.edu/~vmm/Surface/Minimal_Surfaces_2011_Matthias_Weber.pdf)

The complex representation is useful because it makes several structural properties nearly automatic:

- conformality of the parameterization;
- harmonic coordinate functions;
- zero mean curvature;
- asymptotic ends represented by punctures or poles;
- translational symmetries represented by nonzero periods of the Weierstrass integrals.

The Scherk surface therefore sits at an important junction: it is both an explicit PDE solution and a central example in the complex-analytic theory of complete embedded minimal surfaces.

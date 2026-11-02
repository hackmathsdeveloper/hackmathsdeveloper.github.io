
The fundamental forms describe two complementary aspects of a surface: its intrinsic geometry—lengths, angles, and area—and how it bends in the surrounding space. A surface is **minimal** when its mean curvature vanishes everywhere. The key connection is that mean curvature is one-half the trace of the second fundamental form measured using the first fundamental form. This condition is also exactly the equation for a surface to be stationary under area variations. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

Below, we work with smooth, regular surfaces in Euclidean space \(\mathbb R^3\).

## 1. Setting up the geometry

Let a surface be parametrized by
\[
X(u,v)=(x(u,v),y(u,v),z(u,v)),
\qquad X_u\times X_v\neq 0.
\]

Its tangent plane is spanned by \(X_u,X_v\), and a choice of unit normal is
\[
n=\frac{X_u\times X_v}{\lVert X_u\times X_v\rVert}.
\]

The fundamental forms encode the geometry associated with these tangent vectors and with the changing normal. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

## 2. The first fundamental form: measurement within the surface

The first fundamental form is the metric induced by the Euclidean dot product:
\[
I=E\,du^2+2F\,du\,dv+G\,dv^2,
\]
where
\[
E=\langle X_u,X_u\rangle,\qquad
F=\langle X_u,X_v\rangle,\qquad
G=\langle X_v,X_v\rangle.
\]

Equivalently, its matrix is
\[
g=
\begin{pmatrix}
E&F\\
F&G
\end{pmatrix}.
\]

This form determines lengths, angles, and areas on the surface. For example, a curve \(\gamma(t)=X(u(t),v(t))\) has length
\[
L(\gamma)
=
\int
\sqrt{E\dot u^2+2F\dot u\dot v+G\dot v^2}\,dt,
\]
and the area element is
\[
dA=\sqrt{EG-F^2}\,du\,dv.
\]
Thus, the first fundamental form tells a hypothetical inhabitant of the surface how to make measurements without referring to the surrounding space. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

### Intrinsic geometry versus bending

Two surfaces can have the same local metric but sit differently in space. Rolling a planar sheet into a cylinder preserves its local lengths and angles while changing its bending. The first fundamental form therefore does not, by itself, specify the complete extrinsic geometry. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

## 3. The second fundamental form: bending in space

Choose the convention
\[
II=e\,du^2+2f\,du\,dv+g\,dv^2,
\]
with
\[
e=\langle X_{uu},n\rangle,\qquad
f=\langle X_{uv},n\rangle,\qquad
g=\langle X_{vv},n\rangle.
\]

Here the scalar coefficient \(g\) is distinct from the metric matrix above; when necessary, denote the second-form matrix by
\[
b=
\begin{pmatrix}
e&f\\
f&g
\end{pmatrix}.
\]

For a nonzero tangent vector \(w=aX_u+bX_v\), the normal curvature in that direction is
\[
k_n(w)=\frac{II(w,w)}{I(w,w)}
=
\frac{ea^2+2fab+gb^2}{Ea^2+2Fab+Gb^2}.
\]

The denominator normalizes the tangent vector’s length; the numerator measures the normal component of bending. Consequently, the second fundamental form must be interpreted relative to the first. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

### The shape operator

With the convention
\[
S=-dn,
\]
the two forms satisfy
\[
II(w,z)=I(Sw,z).
\]

In coordinates,
\[
[S]=g^{-1}b.
\]

The eigenvalues of \(S\) are the principal curvatures \(k_1,k_2\): the extreme values of normal curvature among unit tangent directions. In an orthonormal principal basis,
\[
I=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\qquad
II=
\begin{pmatrix}
k_1&0\\
0&k_2
\end{pmatrix}.
\]

This is the simplest way to see what the two forms do: the first measures tangent vectors, while the second assigns bending to their directions. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

## 4. Mean curvature, Gaussian curvature, and minimality

For surfaces in \(\mathbb R^3\), define
\[
H=\frac{k_1+k_2}{2},
\qquad
K=k_1k_2.
\]

Using the fundamental-form coefficients,
\[
H=
\frac{eG-2fF+gE}{2(EG-F^2)},
\]
and
\[
K=\frac{eg-f^2}{EG-F^2}.
\]

Mean curvature measures the average signed bending, whereas Gaussian curvature measures the product of the principal curvatures. Gaussian curvature is intrinsic, even though this formula computes it using extrinsic data. [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

A surface is minimal precisely when
\[
H=0.
\]
Therefore its fundamental forms satisfy
\[
\boxed{eG-2fF+gE=0.}
\]

Equivalently,
\[
\operatorname{tr}(g^{-1}b)=0,
\qquad\text{or}\qquad
k_2=-k_1.
\]

Minimality is thus a balance of bending, not an absence of bending. The surface bends equally in opposite senses along its principal directions. Reversing the unit normal changes the signs of \(II\), \(k_1,k_2\), and \(H\), but does not change minimality or \(K\). Some references define mean curvature as \(k_1+k_2\), without the factor \(1/2\); the zero-curvature condition is unchanged. [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

### Immediate geometric consequences

On a minimal surface,
\[
K=-k_1^2\leq 0.
\]

Consequently:

- Wherever the second fundamental form is nonzero, the surface is saddle-shaped.
- If \(K=0\) at a point, both principal curvatures vanish there.
- If \(K\equiv0\) on a connected minimal surface, the surface lies in a plane.
- An umbilic point, where \(k_1=k_2\), must have \(k_1=k_2=0\). [math.mcgill](https://www.math.mcgill.ca/gantumur/math580f12/minimal_surfaces.pdf)

A flat point does not imply that a whole neighborhood is planar: vanishing at one point is much weaker than vanishing everywhere.

## 5. Why zero mean curvature comes from area

Consider a normal variation of a surface:
\[
X_t=X+t\phi n,
\]
where \(\phi\) is smooth and supported away from the boundary.

With the conventions above, the first variation of area is
\[
\left.\frac{d}{dt}A(X_t)\right|_{t=0}
=
-2\int_\Sigma H\phi\,dA.
\]

Therefore,
\[
\delta A=0\text{ for every }\phi
\quad\Longleftrightarrow\quad
H=0.
\]

This establishes the variational meaning of minimality: a minimal surface is a critical point of the area functional under boundary-fixing variations. [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

### Stationary does not necessarily mean minimizing

The word “minimal” can be misleading. The condition \(H=0\) guarantees that the first derivative of area vanishes, not that every deformation increases area.

For a two-sided minimal surface in \(\mathbb R^3\), the second variation is
\[
\delta^2A(\phi)
=
\int_\Sigma
\left(
|\nabla_\Sigma\phi|^2-|S|^2\phi^2
\right)dA,
\]
where
\[
|S|^2=k_1^2+k_2^2=-2K.
\]

Thus,
\[
\delta^2A(\phi)
=
\int_\Sigma
\left(
|\nabla_\Sigma\phi|^2+2K\phi^2
\right)dA.
\]

A minimal surface is stable if this expression is nonnegative for every admissible \(\phi\). Area-minimizing surfaces are stable, but stability alone does not guarantee area minimization. The distinction is analogous to the difference between a critical point, a nonnegative second derivative, and an actual minimum in calculus. [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

## 6. Minimal surfaces written as graphs

Suppose
\[
X(x,y)=(x,y,u(x,y)).
\]

Then
\[
E=1+u_x^2,\qquad F=u_xu_y,\qquad G=1+u_y^2,
\]
and, with the upward normal,
\[
e=\frac{u_{xx}}{W},\qquad
f=\frac{u_{xy}}{W},\qquad
g=\frac{u_{yy}}{W},
\qquad
W=\sqrt{1+u_x^2+u_y^2}.
\]

Substituting into \(eG-2fF+gE=0\) yields the minimal-surface equation:
\[
\boxed{
(1+u_y^2)u_{xx}
-2u_xu_yu_{xy}
+(1+u_x^2)u_{yy}=0.
}
\]

Its divergence form is
\[
\operatorname{div}
\left(
\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}
\right)=0.
\]

These equations express the stationarity of the graph-area functional
\[
A[u]=\int_\Omega\sqrt{1+|\nabla u|^2}\,dx\,dy.
\]
 [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

When the slope is small, the nonlinear equation approximately becomes
\[
u_{xx}+u_{yy}=0.
\]
This explains why harmonic functions provide a linear approximation to minimal graphs—but a harmonic height function is not generally an exact minimal graph.

## 7. Worked example: the catenoid

Consider
\[
X(u,v)=
\bigl(
a\cosh v\cos u,\;
a\cosh v\sin u,\;
av
\bigr),
\qquad a>0.
\]

The fundamental-form formulas above give
\[
E=G=a^2\cosh^2v,\qquad F=0.
\]

For the normal determined by \(X_u\times X_v\),
\[
n=
\left(
\frac{\cos u}{\cosh v},
\frac{\sin u}{\cosh v},
-\tanh v
\right),
\]
and direct differentiation gives
\[
e=-a,\qquad f=0,\qquad g=a.
\]

Hence
\[
I=a^2\cosh^2v\,(du^2+dv^2),
\]
\[
II=-a\,du^2+a\,dv^2.
\]

The shape operator is diagonal:
\[
[S]=
\begin{pmatrix}
-\dfrac{1}{a\cosh^2v}&0\\[4pt]
0&\dfrac{1}{a\cosh^2v}
\end{pmatrix}.
\]

Therefore
\[
H=0,
\qquad
K=-\frac{1}{a^2\cosh^4v}.
\]

This explicit calculation illustrates the defining balance: the catenoid bends in opposite senses with equal principal-curvature magnitude. Its Gaussian curvature is most negative at the waist \(v=0\) and approaches zero along its ends. These conclusions follow directly from the fundamental-form and curvature formulas.  [scholarworks.lib.csusb](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=4191&context=etd-project)

## 8. Conformal coordinates reveal a connection to harmonic functions

In conformal coordinates, the first fundamental form has the special form
\[
I=\lambda^2(du^2+dv^2).
\]

Thus \(E=G=\lambda^2\) and \(F=0\), so minimality reduces to
\[
e+g=0.
\]

More powerfully, the vector-valued position function satisfies
\[
\Delta_\Sigma X=2Hn.
\]

Since the surface Laplacian in these coordinates is
\[
\Delta_\Sigma
=
\frac{1}{\lambda^2}
(\partial_{uu}+\partial_{vv}),
\]
we obtain
\[
H=0
\quad\Longleftrightarrow\quad
X_{uu}+X_{vv}=0.
\]

Thus a conformally parametrized immersion is minimal exactly when all three coordinate functions are harmonic. Conformality remains essential: arbitrary harmonic coordinate functions need not define a minimal immersion. This connection underlies the use of complex analysis and the Weierstrass representation in minimal-surface theory.  [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

## 9. The third fundamental form

The third fundamental form measures how the normal changes:
\[
III(w,z)=\langle dn(w),dn(z)\rangle
=I(Sw,Sz).
\]

Since a \(2\times2\) shape operator satisfies
\[
S^2-2HS+K\,\mathrm{Id}=0,
\]
the three fundamental forms obey
\[
III-2H\,II+K\,I=0.
\]

For a minimal surface this simplifies to
\[
\boxed{III=-K\,I.}
\]

Where \(K<0\), the Gauss map \(n:\Sigma\to S^2\) therefore scales all tangent lengths by the same factor \(\sqrt{-K}\), preserving angles up to orientation. This is the differential-geometric reason that the Gauss map of a minimal surface is conformal away from its flat points.  [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

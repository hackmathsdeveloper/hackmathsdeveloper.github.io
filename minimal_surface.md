
A **minimal surface** is a smooth surface whose mean curvature is zero at every point. Equivalently, it is stationary for the area functional under every compactly supported deformation; this is why soap films spanning wire frames are the canonical physical model. “Minimal” means *locally area-minimizing or at least area-stationary*—not necessarily globally the smallest possible surface for a boundary. [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

## The main ways to explore them

Minimal-surface theory sits at the intersection of calculus of variations, PDE, differential geometry, complex analysis, topology, and geometric measure theory. Useful directions include:

| Direction | Core question | Main tools |
|---|---|---|
| Variational theory | Which surfaces make area stationary or minimizing? | First/second variation, Plateau problem, stability |
| PDE theory | Which functions solve the minimal-surface equation? | Quasilinear elliptic PDE, maximum principles, regularity |
| Differential geometry | What does \(H=0\) imply for curvature and coordinates? | Fundamental forms, shape operator, Gauss map |
| Complex analysis | How can holomorphic data generate minimal surfaces? | Conformal parameters, harmonic maps, Weierstrass representation |
| Global geometry/topology | Which complete, embedded, finite-topology surfaces exist? | Completeness, ends, total curvature, classification |
| Singularities and higher dimensions | When do area minimizers develop singularities? | Geometric measure theory, minimal hypersurfaces |
| Numerical/physical models | How do you compute or simulate soap-film-like surfaces? | Finite elements, discrete differential geometry, Surface Evolver-type methods |

A strong learning sequence is:

1. Derive the graph equation from area minimization.
2. Study classical examples: plane, catenoid, helicoid, Scherk surface, Enneper surface.
3. Move to parametrized surfaces and prove that minimality is \(H=0\).
4. Use conformal coordinates to turn the nonlinear geometric condition into the linear harmonic equation.
5. Learn the Weierstrass–Enneper representation, which constructs surfaces from complex-analytic data.
6. Study stability, curvature, completeness, topology, and global classification.

## Equivalent definitions

Let \(X:\Sigma\to\mathbb R^3\) be a smooth immersed surface, where \(\Sigma\) is a two-dimensional parameter domain.

The following are closely related—and, under the usual smoothness hypotheses, equivalent—ways to define a minimal surface.

### 1. Zero mean curvature

At a point, let \(k_1,k_2\) be the principal curvatures. Define mean curvature by

\[
H=\frac{k_1+k_2}{2}.
\]

A surface is minimal exactly when

\[
\boxed{H=0.}
\]

Therefore,

\[
k_1=-k_2.
\]

So, except at flat points, a minimal surface bends upward in one principal direction and downward by an equal amount in the other. It is intrinsically saddle-shaped.

### 2. Stationary area

For a parametrized surface \(X(u,v)\), its area is

\[
A[X]=\int_\Omega \lVert X_u\times X_v\rVert\,du\,dv.
\]

Consider a variation

\[
X_t=X+tV,
\]

where \(V\) is a smooth vector field that vanishes at the boundary. The first-variation formula has the form

\[
\left.\frac{d}{dt}A[X_t]\right|_{t=0}
=
-2\int_\Sigma H\,\langle V,N\rangle\,dA,
\]

up to the convention used for mean curvature. Since the normal component \(\langle V,N\rangle\) can be chosen arbitrarily, stationarity for all such variations is equivalent to

\[
H\equiv 0.
\]

This is the geometric origin of the definition. [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

### 3. Local least-area property

A stronger condition says that every sufficiently small patch minimizes area among competing surfaces with the same boundary curve. This implies \(H=0\).

The reverse must be stated carefully: \(H=0\) always means area-*stationary*, but not every minimal surface is stable or globally area-minimizing. The catenoid, for example, is minimal, but sufficiently large portions can be unstable under certain variations.

### 4. Harmonic conformal parametrization

Choose **conformal coordinates** \((u,v)\), meaning

\[
\langle X_u,X_v\rangle=0,
\qquad
\lVert X_u\rVert=\lVert X_v\rVert.
\]

Then the induced metric is

\[
ds^2=\lambda^2(du^2+dv^2).
\]

In such coordinates, minimality becomes

\[
\boxed{\Delta X=X_{uu}+X_{vv}=0.}
\]

Thus each Cartesian coordinate function \(x(u,v)\), \(y(u,v)\), and \(z(u,v)\) is harmonic:

\[
\Delta x=\Delta y=\Delta z=0.
\]

This is one of the deepest simplifications in the subject: a nonlinear area problem becomes harmonic-function theory after choosing the right coordinates. [carmancater.github](https://carmancater.github.io/assets/pdf/Cater_M585_S22_MinSurf.pdf)

## Deriving the minimal-surface equation

The most direct derivation treats the surface as a graph over the \(xy\)-plane:

\[
X(x,y)=(x,y,u(x,y)).
\]

The function \(u(x,y)\) is the height of the surface.

### Area of a graph

Compute the tangent vectors:

\[
X_x=(1,0,u_x),
\qquad
X_y=(0,1,u_y).
\]

Their cross product is

\[
X_x\times X_y=(-u_x,-u_y,1),
\]

so

\[
\lVert X_x\times X_y\rVert
=
\sqrt{1+u_x^2+u_y^2}.
\]

Therefore the area functional is

\[
\boxed{
A[u]=\int_\Omega \sqrt{1+u_x^2+u_y^2}\,dx\,dy.
}
\]

### First variation

Perturb \(u\) while holding its boundary values fixed:

\[
u_t=u+t\phi,
\qquad
\phi|_{\partial\Omega}=0.
\]

Then

\[
A[u_t]
=
\int_\Omega
\sqrt{1+(u_x+t\phi_x)^2+(u_y+t\phi_y)^2}\,dx\,dy.
\]

Differentiating at \(t=0\) gives

\[
\left.\frac{d}{dt}A[u_t]\right|_{t=0}
=
\int_\Omega
\frac{u_x\phi_x+u_y\phi_y}
{\sqrt{1+u_x^2+u_y^2}}
\,dx\,dy.
\]

Integrate by parts. The boundary term disappears because \(\phi=0\) on \(\partial\Omega\):

\[
\left.\frac{d}{dt}A[u_t]\right|_{t=0}
=
-\int_\Omega
\phi\,
\operatorname{div}
\left(
\frac{\nabla u}{\sqrt{1+\lVert\nabla u\rVert^2}}
\right)
dx\,dy.
\]

For this derivative to vanish for *every* allowable \(\phi\), the coefficient of \(\phi\) must vanish:

\[
\boxed{
\operatorname{div}
\left(
\frac{\nabla u}{\sqrt{1+\lVert\nabla u\rVert^2}}
\right)=0.
}
\]

This is the **minimal-surface equation** in divergence form. [math.uchicago](https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf)

Expanding it yields

\[
\boxed{
(1+u_y^2)u_{xx}
-2u_xu_yu_{xy}
+(1+u_x^2)u_{yy}=0.
}
\]

This is a nonlinear, second-order, elliptic PDE. [en.wikipedia](https://en.wikipedia.org/wiki/Minimal_surface)

## Geometric properties

For a smooth minimal surface in \(\mathbb R^3\), the following properties are especially important.

- **Opposite principal curvatures:** \(k_1+k_2=0\), hence \(k_2=-k_1\).

- **Nonpositive Gaussian curvature:** Since
  \[
  K=k_1k_2=-k_1^2\le 0,
  \]
  a nonflat minimal surface has negative Gaussian curvature wherever its second fundamental form is nonzero.

- **No compact boundaryless examples in Euclidean \(\mathbb R^3\):** Each coordinate function is harmonic. A compact surface without boundary would force these functions to be constant by the maximum principle, so the immersion would be trivial.

- **Coordinate functions are harmonic in conformal coordinates:** This connects minimal surfaces to potential theory and complex analysis.

- **The Gauss map is conformal/meromorphic in the conformal setting:** The normal-direction map carries strong complex-analytic structure. This underlies representation formulas and classification results. [en.wikipedia](https://en.wikipedia.org/wiki/Minimal_surface)

- **Maximum principles apply:** Two distinct minimal graphs generally cannot touch tangentially at an interior point with one entirely on one side of the other, unless they locally coincide. This is a geometric manifestation of elliptic PDE maximum principles.

- **Scale and rigid-motion invariance:** Translations, rotations, reflections, and uniform scalings preserve minimality.

- **Second variation distinguishes stable from unstable surfaces:** Solving \(H=0\) only establishes a critical point of area. The second variation determines whether nearby variations increase area, decrease it, or do both.

## Classical examples and formulas

### Plane

\[
X(u,v)=(u,v,0).
\]

Here \(k_1=k_2=0\), so \(H=0\). A plane is the simplest complete, stable minimal surface.

### Catenoid

A catenoid can be parametrized by

\[
X(u,v)=
\left(
a\cosh\frac{v}{a}\cos u,\;
a\cosh\frac{v}{a}\sin u,\;
v
\right),
\]

where \(a>0\).

It is the surface of revolution obtained by rotating a catenary about an axis. It is minimal but demonstrates the important point that “minimal” does not automatically mean globally area-minimizing for arbitrary boundary data.

### Helicoid

\[
X(u,v)=
\left(
u\cos v,\;
u\sin v,\;
av
\right),
\]

with pitch parameter \(a\neq0\).

The helicoid resembles a spiral ramp. It is a complete, embedded minimal surface. Remarkably, the catenoid and helicoid are locally isometric and belong to an associated family of minimal surfaces.

### Scherk’s graph

One classical graph is

\[
u(x,y)=\log\left(\frac{\cos y}{\cos x}\right),
\]

on a domain where the expression is defined. It solves the nonlinear minimal-surface equation and provides a useful example with periodic, saddle-like structure.

### Enneper surface

The Enneper surface is a complete minimal surface with self-intersections. It is especially useful for seeing how complex analytic data can create a minimal immersion.

## The Weierstrass representation

For local or simply connected constructions, complex analysis provides a systematic “formula generator.”

Let \(g(z)\) be meromorphic and let \(dh\) be a holomorphic 1-form. Then, subject to the required regularity and period conditions, define

\[
X(z)
=
\operatorname{Re}
\int^z
\left(
\frac{1}{2}\left(\frac{1}{g}-g\right),
\frac{i}{2}\left(\frac{1}{g}+g\right),
1
\right)dh.
\]

The resulting map parametrizes a minimal surface.

Here:

- \(g\) represents the stereographically projected Gauss map.
- \(dh\) controls the vertical differential and metric scaling.
- The condition that the real parts of periods vanish ensures the integral defines a single-valued immersion on a non-simply-connected domain.

This representation explains why minimal surfaces have such strong ties to meromorphic functions, Riemann surfaces, residues, periods, and algebraic geometry. [en.wikipedia](https://en.wikipedia.org/wiki/Minimal_surface)

## A practical derivation roadmap

If your goal is to derive formulas rather than only recognize them, use this framework:

1. **Specify the model.**  
   Use a graph \(z=u(x,y)\) for a PDE problem, or an immersion \(X(u,v)\) for an intrinsic geometric problem.

2. **Compute the first fundamental form.**  
   For \(X(u,v)\), set
   \[
   E=\langle X_u,X_u\rangle,\quad
   F=\langle X_u,X_v\rangle,\quad
   G=\langle X_v,X_v\rangle.
   \]

3. **Compute the unit normal.**  
   \[
   N=\frac{X_u\times X_v}{\lVert X_u\times X_v\rVert}.
   \]

4. **Compute the second fundamental form.**  
   \[
   e=\langle X_{uu},N\rangle,\quad
   f=\langle X_{uv},N\rangle,\quad
   g=\langle X_{vv},N\rangle.
   \]

5. **Evaluate mean curvature.**  
   \[
   H=
   \frac{eG-2fF+gE}{2(EG-F^2)}.
   \]

6. **Set \(H=0\).**  
   This produces the minimal-surface condition for your parametrization:
   \[
   eG-2fF+gE=0.
   \]

7. **If possible, choose conformal coordinates.**  
   With \(E=G\) and \(F=0\), the condition reduces to
   \[
   X_{uu}+X_{vv}=0,
   \]
   so the coordinate functions are harmonic. [carmancater.github](https://carmancater.github.io/assets/pdf/Cater_M585_S22_MinSurf.pdf)

The central unifying chain is:

\[
\text{area stationarity}
\quad\Longleftrightarrow\quad
H=0
\quad\Longleftrightarrow\quad
\text{minimal-surface PDE}
\quad\Longleftrightarrow\quad
\Delta X=0
\text{ in conformal coordinates}.
\]

That chain is the foundation from which most of the theory—classical examples, complex representations, stability theory, and modern minimal-hypersurface research—develops.

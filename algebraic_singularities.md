
For algebraic polynomial equations, a **singularity** is a point on the solution set where the equations fail to define a locally smooth object of the expected dimension. The universal test is rank loss of the Jacobian; after locating those points, the possible local behaviors range from simple crossings and cusps to nonreduced components, non-isolated singular loci, and singularities at infinity. [indico.ictp](https://indico.ictp.it/event/a05209/session/6/contribution/4/material/0/2.pdf)

## General setup

Let an affine algebraic set be

\[
X = V(f_1,\dots,f_m)\subseteq k^n,
\]

where \(k\) is usually \(\mathbb C\) or \(\mathbb R\), and \(f_i\in k[x_1,\dots,x_n]\).

Its Jacobian matrix is

\[
J_f(p)=
\begin{pmatrix}
\frac{\partial f_1}{\partial x_1}(p) & \cdots & \frac{\partial f_1}{\partial x_n}(p)\\
\vdots & & \vdots\\
\frac{\partial f_m}{\partial x_1}(p) & \cdots & \frac{\partial f_m}{\partial x_n}(p)
\end{pmatrix}.
\]

If \(X\) has local dimension \(d\) near \(p\), then the expected Jacobian rank is \(n-d\). Thus:

\[
p\in \operatorname{Sing}(X)
\quad\Longleftrightarrow\quad
\operatorname{rank} J_f(p)<n-d.
\]

Equivalently, the Zariski tangent space

\[
T_pX=\ker J_f(p)
\]

has dimension **larger** than the local dimension of \(X\).

For a hypersurface \(X=V(f)\subseteq k^n\), the condition simplifies to

\[
f(p)=0,\qquad
\frac{\partial f}{\partial x_1}(p)=\cdots=
\frac{\partial f}{\partial x_n}(p)=0.
\]

So the singular locus is defined algebraically by the ideal

\[
I_{\mathrm{sing}}=(f,f_{x_1},\dots,f_{x_n}).
\]

For a plane curve \(f(x,y)=0\), this becomes the familiar system

\[
f=f_x=f_y=0.
\]

This is the standard Jacobian criterion for hypersurfaces. [indico.ictp](https://indico.ictp.it/event/a05209/session/6/contribution/4/material/0/2.pdf)

## Main singularity scenarios

The following table gives the principal possibilities you encounter for polynomial equations.

| Scenario | Local algebraic form or test | Geometric behavior | Example |
|---|---|---|---|
| Smooth point | Jacobian has expected rank | Locally a manifold/regular variety | \(y-x^2=0\) everywhere |
| Multiple root in one variable | \(f(a)=f'(a)=0\) | Root collision; as a zero-dimensional scheme, it is nonreduced | \((x-1)^2=0\) |
| Ordinary double point / node | Lowest nonzero term has two distinct tangent factors | Two smooth branches cross transversely | \(y^2-x^2=0=(y-x)(y+x)\) |
| Tangential double point / tacnode | Two branches share a tangent line | Branches touch rather than cross | \(y^2-x^4=0=(y-x^2)(y+x^2)\) |
| Cusp | One branch, singular parametrization; tangent cone is repeated | Sharp pointed branch | \(y^2-x^3=0\) |
| Higher cusp | Higher-order unibranch singularity | More degenerate cusp | \(y^2-x^5=0\) |
| Triple or higher multiple point | Multiplicity \(m\ge3\) | Three or more tangent directions, or repeated tangencies | \(y^3-x^3=0\) |
| Reducible-component intersection | Several irreducible factors vanish at once | Components meet; may be transverse or tangent | \(xy=0\) |
| Nonreduced hypersurface | \(f=g^r\), \(r>1\) | Underlying geometric set may be smooth, but scheme has nilpotents; every point is singular under the reduced-equation warning | \(y^2=0\) |
| Positive-dimensional singular locus | Jacobian rank drops along a curve/surface/etc. | Not isolated; often caused by product structure or a cone | \(x^2-y^2z=0\) has singular line \(x=y=0\) |
| Cone vertex | Homogeneous equation with all first derivatives zero at origin | Vertex is singular; tangent cone equals the cone itself | \(x^2+y^2-z^2=0\) at \(0\) |
| Rank-defect complete intersection | All defining equations vanish but Jacobian rank is too low | Constraints fail to cut dimension transversely | \(V(xz,yz)\subset \mathbb A^3\) |
| Singularities at infinity | Singular point in projective closure on \(Z=0\) | Affine chart can look smooth while projective compactification is singular | Analyze homogenized \(F(X,Y,Z)\) |
| Real isolated point | Real locus may have a point but no real branches | Complex geometry may contain branches invisible over \(\mathbb R\) | \(x^2+y^2=0\) in \(\mathbb R^2\) |
| Complex-only singularity | Singular over \(\mathbb C\), no real singular point | Essential when classifying real curves via complexification | \(x^2+y^2=0\) has complex lines \(y=\pm ix\) |
| Family/parameter degeneration | Discriminant vanishes | Smooth fibers acquire singular points when parameters collide | \(y^2=x^3+ax+b\), with \(4a^3+27b^2=0\) |

The cusp \(y^2=x^3\) is a canonical example: solving \(f=f_x=f_y=0\) gives only \((0,0)\), and its tangent space there is two-dimensional even though the curve itself has dimension one. [personalpages.manchester.ac](https://personalpages.manchester.ac.uk/staff/gabor.megyesi/teaching/math32062/singularities.pdf)

## Plane curves: classify using multiplicity and tangent cone

Let \(f(x,y)=0\), and translate a singular point to the origin. Write

\[
f(x,y)=f_m(x,y)+f_{m+1}(x,y)+\cdots,
\]

where \(f_j\) is homogeneous of degree \(j\), and \(f_m\neq0\). The number \(m\) is the **multiplicity** of the singularity.

The polynomial \(f_m\) is the **tangent cone**. Factoring it over \(\mathbb C\) reveals the first-order branch geometry.

### Multiplicity one: smooth

If the lowest-degree part is linear,

\[
f_1(x,y)=ax+by,
\]

then \(\nabla f(0,0)\neq 0\), so the point is smooth.

Example:

\[
f=y-x^2,
\qquad f_1=y.
\]

The tangent is \(y=0\).

### Multiplicity two: the decisive first branch

Suppose

\[
f_2(x,y)=ax^2+bxy+cy^2.
\]

The discriminant

\[
\Delta=b^2-4ac
\]

gives the first classification over \(\mathbb R\):

| Quadratic tangent cone | Real interpretation | Typical outcome |
|---|---|---|
| \(\Delta>0\) | Two distinct real tangent lines | Node or two real branches crossing |
| \(\Delta=0\) | Repeated tangent line | Cusp, tacnode, or higher-contact singularity |
| \(\Delta<0\) | No real tangent lines | May be an isolated real point, though complex branches exist |

Examples:

\[
y^2-x^2=0
\]

has tangent cone \((y-x)(y+x)\): a node with two distinct tangent lines.

\[
y^2-x^3=0
\]

has tangent cone \(y^2\): a repeated tangent line \(y=0\), but the next term \(-x^3\) distinguishes it as a cusp.

\[
y^2-x^4=0
\]

also has tangent cone \(y^2\), yet it factors into two smooth branches,

\[
y=x^2,\qquad y=-x^2,
\]

which are tangent at the origin. This is a tacnode-type configuration.

Thus, multiplicity and tangent cone are necessary but not always sufficient: when the tangent cone has repeated factors, one must inspect higher-order terms, factor locally, or resolve the singularity.

## Isolated versus non-isolated singularities

A singular point is **isolated** if it is the only singular point in some neighborhood. It is **non-isolated** if the singular locus itself has positive dimension.

### Isolated example

For

\[
f(x,y)=y^2-x^3,
\]

\[
f_x=-3x^2,\qquad f_y=2y.
\]

The only solution to \(f=f_x=f_y=0\) is \((0,0)\). Hence the cusp is isolated.

### Non-isolated example

Consider the Whitney umbrella surface

\[
f(x,y,z)=x^2-y^2z.
\]

Then

\[
f_x=2x,\qquad f_y=-2yz,\qquad f_z=-y^2.
\]

All derivatives vanish precisely when

\[
x=0,\qquad y=0,
\]

with \(z\) arbitrary. Therefore,

\[
\operatorname{Sing}(X)=\{(0,0,z):z\in k\},
\]

a whole line of singular points. This example is commonly used to illustrate that polynomial varieties can have singular sets rather than merely singular points. [people.kth](https://people.kth.se/~mattiasj/research/ag1.pdf)

Non-isolated singularities often indicate one of these structural phenomena:

- A product with a singular factor, such as \(C\times \mathbb A^r\).
- Intersecting components that continue to meet along a locus.
- A nonreduced factor.
- A failure of an intended complete intersection.
- A cone or determinantal variety with a high-dimensional vertex or rank-drop locus.

## Systems of polynomial equations

For a system

\[
f_1=\cdots=f_m=0
\]

the hypersurface rule “all partial derivatives vanish” is not correct by itself. Instead, inspect the rank of \(J_f\).

Suppose \(X\subseteq \mathbb A^n\) is expected to have codimension \(c\). Then \(p\in X\) is singular when

\[
\operatorname{rank}J_f(p)<c.
\]

Equivalently, form the ideal generated by:

- the equations \(f_1,\dots,f_m\), and
- all \(c\times c\) minors of \(J_f\).

Its zero set is the singular locus, assuming the expected codimension \(c\) is the correct one locally.

### Important caution: redundant equations

The same geometric set can be described by different systems. For example, the line \(y=0\) can be given by

\[
(y)=0
\]

or by the redundant system

\[
(y,y^2)=0.
\]

The second Jacobian has artificially dependent rows. Geometry should be determined from the **reduced ideal** and local codimension, not blindly from an arbitrary presentation.

This is why the coordinate ring and ideal-theoretic formulation matter:

\[
X=\operatorname{Spec}\bigl(k[x_1,\ldots,x_n]/I\bigr).
\]

A point can be geometrically smooth on the reduced set while still carrying nonreduced scheme structure in the original ideal.

## Singularities from repeated factors

If

\[
f=g^r h,\qquad r\ge2,
\]

then the factor \(g=0\) occurs with multiplicity. Since

\[
\nabla(g^r h)
=
r g^{r-1}h\nabla g+g^r\nabla h,
\]

the gradient vanishes along \(g=0\) wherever the repeated factor dominates. Thus a repeated component generally creates a large singular locus for the polynomial hypersurface.

Example:

\[
f(x,y)=y^2.
\]

The underlying set is simply the smooth line \(y=0\), but

\[
f_x=0,\qquad f_y=2y,
\]

so every point of \(y=0\) satisfies \(f=f_x=f_y=0\). Scheme-theoretically it is a **double line**, not a smooth reduced curve.

A practical first step in singularity analysis is therefore square-free decomposition:

\[
f_{\mathrm{red}}=\frac{f}{\gcd(f,f_x,f_y,\dots)}.
\]

For a hypersurface over characteristic zero, analyze \(f_{\mathrm{red}}\) if the goal is the geometry of the underlying set, and retain multiplicities if the goal is scheme structure or intersection theory.

## Singularities at infinity

Affine analysis can miss singular behavior at infinity. For a polynomial

\[
f(x,y)
\]

of total degree \(d\), form its homogenization

\[
F(X,Y,Z)=Z^d f(X/Z,Y/Z).
\]

The projective closure is

\[
\overline X=V(F)\subseteq \mathbb P^2.
\]

Points at infinity satisfy \(Z=0\). To find all projective singularities, solve

\[
F=F_X=F_Y=F_Z=0
\]

in projective space.

Example:

\[
f(x,y)=y^2-x^3.
\]

The homogenization is

\[
F(X,Y,Z)=Y^2Z-X^3.
\]

The affine cusp occurs at \([0:0:1]\). The point at infinity is \([0:1:0]\); evaluating derivatives shows that it is nonsingular. But other affine curves acquire singularities only after this projective closure step, so a global classification should always include it.

## Parameter-dependent singularities and discriminants

For a family

\[
f(x;\lambda)=0,
\]

a singular fiber occurs when there exists an \(x\) such that

\[
f(x;\lambda)=0,\qquad
\frac{\partial f}{\partial x}(x;\lambda)=0.
\]

Eliminating \(x\) yields the **discriminant locus** in parameter space.

For a univariate polynomial \(p(x)\), this is exactly the repeated-root criterion:

\[
\operatorname{Disc}(p)=0
\quad\Longleftrightarrow\quad
\gcd(p,p')\neq1.
\]

For the elliptic-curve family

\[
E_{a,b}:\quad y^2=x^3+ax+b,
\]

the curve is singular exactly when

\[
4a^3+27b^2=0.
\]

- If the cubic has one double root and one simple root, the singular fiber is nodal.
- If the cubic has a triple root, the singular fiber is cuspidal.

This is a particularly important bridge between elementary polynomial singularities, discriminants/resultants, elliptic curves, and degeneration in algebraic geometry.

## A practical workflow

To explore all singularity scenarios for a concrete polynomial or system:

1. **Specify the ground field.** Work over \(\mathbb C\) for geometric classification; then separately determine what is visible over \(\mathbb R\). Real and complex singular behavior can differ substantially.

2. **Reduce the defining equations.** Factor polynomials and identify repeated factors. Decide whether you care about the reduced variety or the full scheme.

3. **Determine local dimension or expected codimension.** For a hypersurface, codimension is one unless the polynomial is zero or highly degenerate; for systems, use dimension computations or ideal theory.

4. **Compute the singular ideal.**
   - Hypersurface:
     \[
     (f,f_{x_1},\dots,f_{x_n}).
     \]
   - Codimension-\(c\) system:
     \[
     (f_1,\dots,f_m,\text{ all }c\times c\text{ minors of }J_f).
     \]

5. **Solve or decompose the singular locus.** Gröbner bases, elimination, primary decomposition, and saturation are standard symbolic tools.

6. **For each singular point, translate it to the origin.** Write the local Taylor expansion and find the lowest-degree nonzero homogeneous term.

7. **Factor the tangent cone.** Distinct linear factors indicate distinct tangential branches; repeated factors require higher-order analysis.

8. **Distinguish branches.** Use local factorization, Puiseux expansions for plane curves, normalization, or blow-ups.

9. **Compute local invariants if needed.**
   - Multiplicity \(m_p\).
   - Number of local branches.
   - Delta invariant \(\delta_p\).
   - Milnor number
     \[
     \mu_p=\dim_k k[[x,y]]/(f_x,f_y)
     \]
     for an isolated plane-curve singularity in characteristic zero.
   - Tjurina number
     \[
     \tau_p=\dim_k k[[x,y]]/(f,f_x,f_y).
     \]

10. **Projectivize.** Homogenize and inspect the hyperplane at infinity.

The Jacobian-rank viewpoint is the common foundation: for a hypersurface, singular points are exactly where the defining polynomial and every first derivative vanish; for general systems, singularity is failure of the Jacobian to have the rank required by the local codimension. [indico.ictp](https://indico.ictp.it/event/a05209/session/6/contribution/4/material/0/2.pdf)

## Compact example

Take

\[
f(x,y)=y^2-x^2(x+1).
\]

Then

\[
f_x=-3x^2-2x=-x(3x+2),\qquad f_y=2y.
\]

A singular point must satisfy \(y=0\), \(x=0\) or \(x=-2/3\), and \(f(x,0)=0\).

- At \(x=0\), \(f(0,0)=0\), so \((0,0)\) is singular.
- At \(x=-2/3\), \(f(-2/3,0)\neq0\), so it is not on the curve.

Now expand near the origin:

\[
f=y^2-x^2-x^3.
\]

Its lowest-degree part is

\[
f_2=y^2-x^2=(y-x)(y+x).
\]

Hence the tangent cone has two distinct lines, \(y=x\) and \(y=-x\). Therefore the origin is an ordinary nodal double point, not a cusp. This same computation—solve the Jacobian equations, then analyze the lowest nonzero homogeneous term—is the fastest first-pass method for most explicit plane-polynomial problems.

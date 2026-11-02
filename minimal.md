
# The First and Second Fundamental Forms in Differential Geometry

## 1. Overview and Conceptual Distinction

The **first** and **second fundamental forms** are the two foundational quadratic forms that encode the intrinsic and extrinsic geometry of a surface $S \subset \mathbb{R}^3$, respectively. Given a smooth parametrized surface $\mathbf{r}(u, v)$, they answer fundamentally different questions:

| | First Fundamental Form ($I$) | Second Fundamental Form ($II$) |
|---|---|---|
| **What it measures** | Intrinsic metric properties | Extrinsic bending/curvature |
| **Depends on** | Tangent vectors only | Normal vector and its variation |
| **Invariant under** | Isometries (bending without stretching) | Rigid motions of $\mathbb{R}^3$ |

---

## 2. The First Fundamental Form — Intrinsic Geometry

### Definition

The first fundamental form is the restriction of the Euclidean inner product to the tangent plane $T_pS$. It is written as:

$$I = E\,du^2 + 2F\,du\,dv + G\,dv^2$$

where the coefficients are:
$$E = \mathbf{r}_u \cdot \mathbf{r}_u, \quad F = \mathbf{r}_u \cdot \mathbf{r}_v, \quad G = \mathbf{r}_v \cdot \mathbf{r}_v$$

Equivalently, for a tangent vector $d\mathbf{r} = \mathbf{r}_u\,du + \mathbf{r}_v\,dv$:
$$I(d\mathbf{r}, d\mathbf{r}) = |d\mathbf{r}|^2$$

The matrix representation is the **metric tensor**:
$$[I] = \begin{pmatrix} E & F \\ F & G \end{pmatrix}$$

### 2.1 Arc Length

The first fundamental form directly defines the **infinitesimal arc length** $ds$ along a curve $\gamma(t) = \mathbf{r}(u(t), v(t))$ on the surface:

$$ds^2 = E\,du^2 + 2F\,du\,dv + G\,dv^2$$

The total length of a curve $\gamma: [a, b] \to S$ is:

$$L(\gamma) = \int_a^b \sqrt{E\left(\frac{du}{dt}\right)^2 + 2F\frac{du}{dt}\frac{dv}{dt} + G\left(\frac{dv}{dt}\right)^2}\,dt$$

> **Key insight:** $ds^2$ is the squared length of the differential displacement vector projected onto the surface. On a flat plane with Cartesian coordinates, $E=G=1, F=0$, recovering $ds^2 = du^2 + dv^2$.

### 2.2 Angles

Given two tangent vectors at a point $p$, say $\mathbf{w}_1 = a_1\mathbf{r}_u + b_1\mathbf{r}_v$ and $\mathbf{w}_2 = a_2\mathbf{r}_u + b_2\mathbf{r}_v$, the angle $\theta$ between them is determined entirely by $I$:

$$\cos\theta = \frac{I(\mathbf{w}_1, \mathbf{w}_2)}{\sqrt{I(\mathbf{w}_1, \mathbf{w}_1)}\sqrt{I(\mathbf{w}_2, \mathbf{w}_2)}} = \frac{Ea_1a_2 + F(a_1b_2 + a_2b_1) + Gb_1b_2}{\sqrt{Ea_1^2 + 2Fa_1b_1 + Gb_1^2}\sqrt{Ea_2^2 + 2Fa_2b_2 + Gb_2^2}}$$

Two curves intersecting on $S$ have the same angle as their tangent vectors in $T_pS$, measured via $I$.

> **Conformal maps** preserve angles, meaning they preserve the *ratio* of the first fundamental form to a flat metric, i.e., $I = \lambda(u,v)(du^2 + dv^2)$ for some positive function $\lambda$.

### 2.3 Surface Area

The area element $dA$ on the surface is derived from the cross product of the tangent vectors:

$$dA = |\mathbf{r}_u \times \mathbf{r}_v|\,du\,dv$$

Using the Lagrange identity $|\mathbf{r}_u \times \mathbf{r}_v|^2 = |\mathbf{r}_u|^2|\mathbf{r}_v|^2 - (\mathbf{r}_u \cdot \mathbf{r}_v)^2 = EG - F^2$, we get:

$$dA = \sqrt{EG - F^2}\,du\,dv$$

The total area of a region $R \subset S$ is:

$$\text{Area}(R) = \iint_R \sqrt{EG - F^2}\,du\,dv$$

Note that $\sqrt{EG - F^2} = \sqrt{\det[I]}$, so the area element is the square root of the determinant of the metric tensor — exactly analogous to the Riemannian volume form $\sqrt{\det g}\,dx^1 \wedge dx^2$.

---

## 3. The Second Fundamental Form — Extrinsic Geometry

### Definition

While $I$ measures lengths and angles *within* the surface, $II$ measures how the surface **bends in the ambient space** $\mathbb{R}^3$. It captures the rate of change of the unit normal $\mathbf{n}$.

$$II = e\,du^2 + 2f\,du\,dv + g\,dv^2$$

where (using the standard notation $L, M, N$ or $e, f, g$):

$$e = \mathbf{r}_{uu} \cdot \mathbf{n}, \quad f = \mathbf{r}_{uv} \cdot \mathbf{n}, \quad g = \mathbf{r}_{vv} \cdot \mathbf{n}$$

with $\mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{|\mathbf{r}_u \times \mathbf{r}_v|}$.

Geometrically, $II(d\mathbf{r}, d\mathbf{r})$ measures the **normal component of the acceleration** of a curve on the surface — how much the curve is forced to bend away from the tangent plane.

The matrix form is:
$$[II] = \begin{pmatrix} e & f \\ f & g \end{pmatrix}$$

---

### 3.1 The Shape Operator (Weingarten Map)

The **shape operator** $S_p: T_pS \to T_pS$ is the linear map defined by the negative derivative of the Gauss map:

$$S_p(\mathbf{v}) = -d\mathbf{n}_p(\mathbf{v})$$

It is related to the two fundamental forms by:

$$II(\mathbf{v}, \mathbf{w}) = I(S_p(\mathbf{v}), \mathbf{w})$$

In matrix form, using the bases $\{\mathbf{r}_u, \mathbf{r}_v\}$:

$$[S] = [I]^{-1}[II] = \frac{1}{EG - F^2}\begin{pmatrix} G & -F \\ -F & E \end{pmatrix}\begin{pmatrix} e & f \\ f & g \end{pmatrix}$$

The shape operator is **self-adjoint** with respect to $I$, meaning $I(S(\mathbf{v}), \mathbf{w}) = I(\mathbf{v}, S(\mathbf{w}))$, which guarantees real eigenvalues.

### 3.2 Normal Curvature

For a unit tangent vector $\mathbf{v} \in T_pS$ (unit with respect to $I$), the **normal curvature** in the direction $\mathbf{v}$ is:

$$\kappa_n(\mathbf{v}) = II(\mathbf{v}, \mathbf{v}) = I(S(\mathbf{v}), \mathbf{v})$$

This is the curvature of the normal section — the curve obtained by intersecting $S$ with the plane spanned by $\mathbf{v}$ and $\mathbf{n}$.

### 3.3 Principal Curvatures

Since $S$ is self-adjoint, the **Spectral Theorem** guarantees two real eigenvalues $\kappa_1, \kappa_2$ (the **principal curvatures**) with orthogonal eigenvectors $\mathbf{v}_1, \mathbf{v}_2$ (the **principal directions**).

They are found by solving:
$$\det([II] - \kappa[I]) = 0$$
$$(e - \kappa E)(g - \kappa G) - (f - \kappa F)^2 = 0$$

Expanding:
$$(EG - F^2)\kappa^2 - (Eg + Ge - 2Ff)\kappa + (eg - f^2) = 0$$

The principal curvatures are the roots:
$$\kappa_{1,2} = \frac{(Eg + Ge - 2Ff) \pm \sqrt{(Eg + Ge - 2Ff)^2 - 4(EG - F^2)(eg - f^2)}}{2(EG - F^2)}$$

**Euler's Theorem** states that the normal curvature in any direction making angle $\theta$ with the first principal direction is:
$$\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta$$

### 3.4 Gaussian Curvature

The **Gaussian curvature** $K$ is the determinant of the shape operator:

$$K = \det(S) = \kappa_1 \kappa_2 = \frac{\det[II]}{\det[I]} = \frac{eg - f^2}{EG - F^2}$$

**Gauss's Theorema Egregium** (1827) states that $K$ depends *only* on $I$ — it is an **intrinsic invariant**. This means you can compute $K$ from $E, F, G$ and their derivatives alone (via the Brioschi formula), without ever referencing the normal or the embedding. This is a profound result: a 2D being living on the surface can measure curvature without knowing about 3D space.

Classification by sign of $K$:
- $K > 0$: **elliptic** point (e.g., sphere)
- $K < 0$: **hyperbolic** point (e.g., saddle)
- $K = 0$: **parabolic** or **flat** point (e.g., cylinder, plane)

### 3.5 Mean Curvature and Minimal Surfaces

The **mean curvature** $H$ is half the trace of the shape operator:

$$H = \frac{1}{2}\text{tr}(S) = \frac{\kappa_1 + \kappa_2}{2} = \frac{Eg - 2Ff + Ge}{2(EG - F^2)}$$

Unlike $K$, the mean curvature is an **extrinsic** quantity — it depends on how the surface is embedded.

#### The Minimal Surface Condition

A surface is a **minimal surface** if and only if:

$$\boxed{H = 0 \quad \text{everywhere}}$$

This is equivalent to $\kappa_1 = -\kappa_2$ at every point: the principal curvatures are equal in magnitude and opposite in sign.

**Why $H = 0$?** Minimal surfaces arise as critical points of the area functional. Consider a variation of the surface $\mathbf{r} \to \mathbf{r} + t\,\phi\,\mathbf{n}$ for a smooth function $\phi$. The first variation of area is:

$$\left.\frac{d}{dt}\text{Area}(\mathbf{r} + t\phi\mathbf{n})\right|_{t=0} = -2\iint \phi\,H\,\sqrt{EG - F^2}\,du\,dv$$

For this to vanish for *all* compactly supported variations $\phi$, we need $H \equiv 0$. Thus:

> **Minimal surfaces are precisely the surfaces that are critical points of area under all compactly supported normal variations.**

Classic examples of minimal surfaces:
- **Catenoid**: surface of revolution of a catenary; $H = 0$
- **Helicoid**: ruled surface generated by a rotating line; $H = 0$
- **Enneper's surface**, **Scherk's surface**, **Costa's surface**

The catenoid and helicoid are famously **associate minimal surfaces** — they share the same Gauss map and $II$ up to a rotation in the tangent plane, illustrating the deep connection between $I$, $II$, and the complex-analytic structure of minimal surfaces (via the Weierstrass–Enneper representation).

---

## 4. Summary Comparison

| Property | First Fundamental Form $I$ | Second Fundamental Form $II$ |
|---|---|---|
| **Coefficients** | $E, F, G$ | $e, f, g$ |
| **Geometric meaning** | Intrinsic metric (distances, angles, areas) | Extrinsic bending (how surface curves in $\mathbb{R}^3$) |
| **Arc length** | $ds^2 = E\,du^2 + 2F\,du\,dv + G\,dv^2$ | Not directly defined |
| **Angles** | $\cos\theta = \frac{I(\mathbf{w}_1, \mathbf{w}_2)}{\|w_1\|\|w_2\|}$ | Not directly defined |
| **Area** | $\iint \sqrt{EG - F^2}\,du\,dv$ | Not directly defined |
| **Shape operator** | $[I]$ is the metric used to raise/lower indices | $[S] = [I]^{-1}[II]$ |
| **Principal curvatures** | Not defined | Eigenvalues of $S$: $\kappa_1, \kappa_2$ |
| **Gaussian curvature** | $K = \frac{eg - f^2}{EG - F^2}$ (intrinsic!) | $K = \det(S) = \kappa_1\kappa_2$ |
| **Mean curvature** | Not defined | $H = \frac{Eg - 2Ff + Ge}{2(EG - F^2)}$ |
| **Minimal surface** | Not directly relevant | $H = 0 \iff \kappa_1 = -\kappa_2$ |

### The Deep Connection

The two forms are not independent. The **Gauss–Codazzi–Mainardi equations** are the compatibility conditions that $I$ and $II$ must satisfy to define a valid surface in $\mathbb{R}^3$:

- **Gauss equation**: relates derivatives of $I$ to $K$ (and hence $II$) — this is the PDE expression of *Theorema Egregium*.
- **Codazzi–Mainardi equations**: relate derivatives of $II$ to derivatives of $I$.

By **Bonnet's theorem**, if $I$ and $II$ satisfy these equations, they uniquely determine a surface in $\mathbb{R}^3$ up to rigid motions. Together, $I$ and $II$ provide a complete description of surface geometry — the first telling you how to measure *on* the surface, the second telling you how the surface *curves through space*.

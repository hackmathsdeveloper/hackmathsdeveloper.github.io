
# Bifurcations of Maps: Local Stability Loss Across the Unit Circle

## 1. Setting: Discrete-Time Dynamical Systems

A discrete-time dynamical system (a *map*) is given by

\[
x_{n+1} = f(x_n, \mu), \qquad x_n \in \mathbb{R}^m,\ \mu \in \mathbb{R}^k,
\]

where \(f\) is smooth and \(\mu\) is a parameter vector. Unlike flows (ODEs), where stability is governed by eigenvalues of the Jacobian having negative real part, here the Jacobian

\[
A = D_x f(x^*, \mu)
\]

governs local stability of a fixed point \(x^*\) (satisfying \(f(x^*,\mu)=x^*\)). The fixed point is **linearly stable** iff all eigenvalues \(\lambda_i\) of \(A\) satisfy

\[
|\lambda_i| < 1,
\]

i.e., they lie strictly inside the **unit circle** in the complex plane. The moment one or more eigenvalues cross the unit circle as \(\mu\) varies, the fixed point loses hyperbolicity and a **local bifurcation** occurs.

The unit circle has three "danger zones," each giving a qualitatively different bifurcation:

| Eigenvalue crossing | Name | Normal form |
|---|---|---|
| \(\lambda = +1\) | Saddle-node / transcritical / pitchfork | \(x \mapsto x \pm x^2\) (etc.) |
| \(\lambda = -1\) | Period-doubling (flip) | \(x \mapsto -x - x^3\) |
| \(\lambda = e^{\pm i\theta}\), \(\theta \neq 0,\pi\) | Neimark–Sacker | \(z \mapsto e^{i\theta} z (1 + \dots)\) |

The bifurcation is **local** because it depends only on the behavior near \(x^*\) (center manifold reduction reduces \(m\) to 1 or 2 dimensions). This is the discrete analogue of the Andronov–Poincaré–Hopf classification for flows, but with the imaginary axis replaced by the unit circle.

---

## 2. The Three Codimension-One Crossings

### 2.1 Crossing at \(+1\): Saddle-Node and Its Relatives

When a simple real eigenvalue \(\lambda = +1\) crosses, the map locally behaves like its 1-D normal form. The generic cases are:

- **Saddle-node (tangent) bifurcation**: normal form \(x \mapsto \mu + x \pm x^2\). For \(\mu < 0\) (say) no fixed points; at \(\mu = 0\) one semi-stable point; for \(\mu > 0\) a stable and an unstable fixed point appear. This is the birth/death of fixed points.
- **Transcritical bifurcation**: \(x \mapsto \mu x - x^2\). Two fixed points exchange stability as they pass through each other at \(\mu = 0\).
- **Pitchfork bifurcation**: \(x \mapsto \mu x - x^3\) (supercritical) or \(\mu x + x^3\) (subcritical). A symmetric fixed point loses stability and a symmetric pair of stable fixed points is born (or the reverse).

**Non-degeneracy conditions** (for the saddle-node in 1-D):
\[
f(0,0) = 0, \quad \partial_x f(0,0) = 1, \quad \partial_\mu f(0,0) \neq 0, \quad \partial_{xx} f(0,0) \neq 0.
\]

In higher dimensions, when \(\lambda = +1\) is simple, a center manifold reduction brings the system to this 1-D form. If \(\lambda = +1\) has algebraic multiplicity \(> 1\) or the crossing is non-transversal, one gets degenerate or higher-codimension bifurcations.

**Dynamical meaning**: no new *period* is created — the period remains 1. Only the number/stability of fixed points changes.

---

### 2.2 Crossing at \(-1\): Period-Doubling (Flip) Bifurcation

When a simple real eigenvalue \(\lambda = -1\) crosses, the fixed point loses stability and a **period-2 orbit** is born. This is the *flip* bifurcation, and it is the discrete-time signature of the route to chaos (Feigenbaum cascade).

**Normal form** (1-D):
\[
x \mapsto -(1+\mu) x + x^3
\]
(or \(x \mapsto -x - \mu x + x^3\)). At \(\mu = 0\), \(\lambda = -1\). For \(\mu > 0\) (supercritical case) the fixed point is unstable and a stable 2-cycle appears:
\[
x_{\pm} = \pm\sqrt{\mu} + O(\mu).
\]

**Key feature**: the *second iterate* \(f^2\) undergoes a pitchfork bifurcation at \(\mu = 0\). Indeed, the 2-cycle of \(f\) corresponds to fixed points of \(f^2\), and the stability of the 2-cycle is governed by
\[
(f^2)'(x_\pm) = f'(x_+) f'(x_-) = \lambda^2 \approx 1 - 2\mu + \dots
\]
which is \(<1\) in the supercritical case.

**Non-degeneracy conditions**:
\[
f(0,0)=0, \quad \partial_x f(0,0) = -1, \quad \text{and a nonzero cubic coefficient in the normal form.}
\]

**Higher dimensions**: if \(\lambda = -1\) is simple, center manifold reduction to 1-D applies. The bifurcation creates a period-2 orbit; if the map is invertible, the 2-cycle inherits the stability type (node/saddle/focus) from the reduced map.

**Consequence**: repeated period-doubling as \(\mu\) increases produces the Feigenbaum cascade \(2^n\)-cycles accumulating at \(\mu_\infty\), with universal ratio \(\delta \approx 4.6692\). This is the most famous route to chaos in maps like the logistic map \(x \mapsto \mu x(1-x)\).

---

### 2.3 Crossing at \(e^{\pm i\theta}\): Neimark–Sacker Bifurcation

When a complex-conjugate pair of eigenvalues crosses the unit circle at
\[
\lambda_{1,2} = e^{\pm i\theta}, \qquad 0 < \theta < \pi, \quad \theta \neq \pi/2 \text{ generically},
\]
the fixed point loses stability and an **invariant closed curve** (a topological circle) is born. This is the discrete analogue of the Hopf bifurcation and is called the **Neimark–Sacker** (or secondary Hopf, or Andronov–Hopf) bifurcation.

**Normal form** (in complex coordinates \(z \in \mathbb{C}\)):
\[
z \mapsto e^{i\theta} z (1 + \mu + c |z|^2) + O(|z|^4),
\]
where \(c = c_R + i c_I\) is the first Lyapunov coefficient. The bifurcation is:

- **Supercritical** if \(c_R < 0\): a stable invariant circle is born for \(\mu > 0\) (or \(\mu < 0\), depending on sign convention), surrounding the now-unstable fixed point.
- **Subcritical** if \(c_R > 0\): an unstable invariant circle exists for \(\mu < 0\) and collapses onto the fixed point at \(\mu = 0\), which becomes unstable; there is a hysteresis and possible jump to a distant attractor.

**Non-degeneracy conditions**:
1. \(\lambda = e^{i\theta}\) with \(\theta \neq 0, \pi\) (no strong resonance).
2. The first Lyapunov coefficient \(c_R \neq 0\).
3. Transversality: \(\frac{d|\lambda(\mu)|}{d\mu}\big|_{\mu=0} \neq 0\).

**Dynamics on the circle**: The restriction of the map to the invariant circle is a circle diffeomorphism with rotation number \(\rho\). If \(\rho\) is rational \(p/q\), the circle contains a \(q\)-periodic orbit (phase-locked); if irrational, the dynamics is quasiperiodic. As parameters vary, the rotation number winds through rationals, producing **Arnold tongues** (see §3).

**Difference from Hopf in flows**: In ODEs, the Hopf bifurcation produces a limit cycle whose amplitude grows like \(\sqrt{\mu}\). Here the invariant circle is a *discrete* set of points under iteration, but its closure is a circle; the "amplitude" still grows like \(\sqrt{\mu}\) for the supercritical case.

**Strong resonances**: When \(\theta = 2\pi p/q\) with \(q = 1,2,3,4\), the bifurcation is degenerate or requires higher-order terms. \(\theta = 0\) is the \(+1\) case; \(\theta = \pi\) is the \(-1\) (flip) case; \(\theta = \pm 2\pi/3\) and \(\pm \pi/2\) give **strong 1:3 and 1:4 resonances**, where the normal form has additional terms and the bifurcation picture is more complex (e.g., 3 or 4 invariant circles may appear, or a saddle-node of periodic orbits on the circle).

---

## 3. Resonance Tongues (Arnold Tongues)

### 3.1 Setup

Consider a two-parameter family where a Neimark–Sacker bifurcation occurs. After reduction to the center manifold and transformation to polar coordinates, the dynamics near the bifurcation is approximated by

\[
\begin{aligned}
r_{n+1} &= r_n \big(1 + \mu + a r_n^2 + \dots\big), \\
\theta_{n+1} &= \theta_n + \omega + b r_n^2 + \dots
\end{aligned}
\]

where \(\omega = \theta\) (the rotation angle at the bifurcation) and \(a, b\) depend on the nonlinear terms. The angular map is a **circle map** with rotation number \(\rho(\mu, \omega)\) depending on parameters.

### 3.2 Phase Locking and Tongues

For a circle map, the rotation number \(\rho\) is a continuous function of parameters. **Mode locking** occurs when \(\rho = p/q\) (rational); this corresponds to a \(q\)-periodic orbit on the invariant circle. The set of parameters \((\mu, \omega)\) for which \(\rho = p/q\) forms a **resonance tongue** (Arnold tongue) emanating from the point \(\mu = 0\), \(\omega = 2\pi p/q\).

- **Inside the tongue**: the dynamics is periodic (phase-locked) — a stable \(q\)-cycle exists.
- **Outside the tongue**: the dynamics is quasiperiodic — the invariant circle persists and the rotation number is irrational.
- **At the tongue boundary**: a **saddle-node bifurcation of periodic orbits** occurs on the invariant circle: a stable and an unstable \(q\)-cycle collide and annihilate.

The width of the \(p/q\) tongue near \(\mu = 0\) scales as
\[
\Delta \omega \sim C \mu^{q/2}
\]
(for the supercritical case), so tongues with small denominators \(q\) are much wider than those with large \(q\). The tongue structure is **Farey-ordered**: between tongues \(p_1/q_1\) and \(p_2/q_2\) lies the tongue \((p_1+p_2)/(q_1+q_2)\).

### 3.3 Devil's Staircase and Fractal Structure

For fixed \(\mu > 0\), the rotation number as a function of \(\omega\) is a **Devil's staircase**: a continuous, non-decreasing function that is constant on intervals (the tongues) and increases on a Cantor-like set of positive measure (the quasiperiodic parameters). The complement of the tongues has fractal dimension \(< 1\). As \(\mu \to 0^+\), the measure of the quasiperiodic set tends to full measure (tongues shrink), while for large \(\mu\) the tongues overlap and the circle map becomes chaotic (the transition to chaos via **overlapping resonances**, as in the standard circle map).

### 3.4 Strong Resonances

The tongues with \(q = 1, 2, 3, 4\) (i.e., \(\omega = 0, \pi, 2\pi/3, \pi/2\)) are special:

- \(q=1\): \(\omega = 0\) — this is the \(+1\) eigenvalue case (saddle-node), not a genuine Neimark–Sacker.
- \(q=2\): \(\omega = \pi\) — this is the flip bifurcation.
- \(q=3\): \(\omega = 2\pi/3\) — strong 1:3 resonance; the normal form has a cubic term that cannot be removed, and the bifurcation may produce three invariant circles or a saddle-node of 3-cycles.
- \(q=4\): \(\omega = \pi/2\) — strong 1:4 resonance; the normal form has a quartic term, producing up to four invariant circles.

These strong resonances require separate analysis because the "resonance tongue" has a different shape near the origin (it opens with a different power law, or the tongue boundary is not smooth).

---

## 4. Summary Table

| Crossing | Eigenvalue | Bifurcation | New object | Normal form | Codim |
|---|---|---|---|---|---|
| \(+1\) | \(\lambda = 1\) | Saddle-node | Fixed points | \(x \mapsto \mu + x \pm x^2\) | 1 |
| \(+1\) | \(\lambda = 1\) | Transcritical | Exchange of stability | \(x \mapsto \mu x - x^2\) | 1 |
| \(+1\) | \(\lambda = 1\) | Pitchfork | Symmetric pair | \(x \mapsto \mu x - x^3\) | 1 |
| \(-1\) | \(\lambda = -1\) | Period-doubling (flip) | 2-cycle | \(x \mapsto -(1+\mu)x + x^3\) | 1 |
| \(e^{\pm i\theta}\) | \(\lambda = e^{\pm i\theta}\) | Neimark–Sacker | Invariant circle | \(z \mapsto e^{i\theta} z (1+\mu + c|z|^2)\) | 1 |
| \(e^{\pm i\theta}\), \(\theta = 2\pi p/q\) | strong resonance | Degenerate NS | \(q\)-cycles / circles | Higher-order terms | 2+ |

---

## 5. Further Topics and Connections

- **Center manifold reduction**: Justifies reducing \(m\)-dimensional maps to 1-D (for \(\pm 1\)) or 2-D (for NS) near the bifurcation, provided the critical eigenvalues are simple (or semi-simple).
- **Normal form theory**: Uses near-identity coordinate changes to eliminate non-resonant terms, yielding the polynomial normal forms above.
- **Codimension-two bifurcations**: When two conditions are met simultaneously (e.g., \(\lambda = 1\) and \(\lambda = -1\), or NS with \(c_R = 0\)), richer phenomena occur (e.g., Bogdanov–Takens, cusp, degenerate Hopf).
- **Global bifurcations**: Homoclinic/heteroclinic tangles, crises, and boundary crises in maps are global analogues.
- **Applications**: Population dynamics (logistic, Ricker maps), economics (cobweb models), control theory (sampled-data systems), and numerical continuation (AUTO, MATCONT) for maps.
- **Quasiperiodicity and chaos**: The NS bifurcation is a primary route to quasiperiodicity and, via resonance overlap, to chaos (Ruelle–Takens scenario).

---

## 6. Key References

- Kuznetsov, Y. A. *Elements of Applied Bifurcation Theory* — the standard reference for maps and flows.
- Guckenheimer, J. & Holmes, P. *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* — classic, includes maps.
- Arnold, V. I. *Geometrical Methods in the Theory of Ordinary Differential Equations* — resonance tongues and circle maps.
- Wiggins, S. *Introduction to Applied Nonlinear Dynamical Systems and Chaos* — accessible treatment.
- Shilnikov, L. P. et al. *Methods of Qualitative Theory in Nonlinear Dynamics* — rigorous treatment of homoclinic and local bifurcations.

This framework — local stability loss across the unit circle, the three codimension-one crossings, and the resonance tongue structure — forms the backbone of discrete-time bifurcation theory, paralleling but distinct from the continuous-time theory of Andronov–Hopf, saddle-node, and pitchfork bifurcations.

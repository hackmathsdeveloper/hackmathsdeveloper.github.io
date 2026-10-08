
In discrete-time dynamical systems governed by smooth iterated maps $x_{n+1} = f(x_n, \mu)$, the stability of a fixed point $x^*$ is dictated by the eigenvalues (multipliers) $\lambda_i$ of the Jacobian matrix $J = Df(x^*)$.

Unlike continuous-time ODEs—where stability is lost when real parts of eigenvalues cross zero ($\text{Re}(\lambda) = 0$)—discrete-time systems lose local topological stability when one or more multipliers **cross the unit circle** in the complex plane ($\vert{}\lambda\vert{} = 1$).

---

## 1. Local Stability Criteria & The Unit Circle

For a discrete map, $x^*$ is locally asymptotically stable if all multipliers lie strictly inside the unit circle ($\mathbb{S}^1$):


$$\vert{}\lambda_i\vert{} < 1 \quad \forall i$$

As a parameter $\mu$ is continuously varied, local stability is lost at the boundary $\vert{}\lambda\vert{} = 1$. The geometry of where and how these eigenvalues exit the unit disk determines the bifurcation class:

```
                  Complex Plane (Eigenvalues)
                             Im(λ)
                               ^
                          , - -|- - .
                        '      |      '  <-- Neimark–Sacker (λ = e^{±iθ})
                      /        |        \
                     |    *    |    *    |
                     |  (Inside: Stable) |
     λ = -1  <-------|----+----+----+----|------->  λ = +1
 Period-Doubling     |         |         |        Fold / Transcritical / Pitchfork
  (Flip / 2-Cycle)    \        |        /
                        .      |      .
                          ` - -|- - '
                               v

```

There are three generic codimension-1 scenarios on the unit circle:

1. **$\lambda = +1$ crossing**: Real eigenvalue exits through $+1$.
2. **$\lambda = -1$ crossing**: Real eigenvalue exits through $-1$.
3. **$\lambda_{1,2} = e^{\pm i \theta_0}$ crossing ($\theta_0 \neq 0, \pi$)**: Complex-conjugate pair exits simultaneously.

---

## 2. Real Eigenvalue Crossing at $+1$ (Fold, Transcritical, Pitchfork)

When a single real eigenvalue exits through $+1$, the map loses stability without introducing new natural frequencies or periods at the linear level.

### Local Normal Forms ($1\text{D}$)

Depending on the spatial symmetries of $f(x, \mu)$:

* **Fold / Saddle-Node:** $x_{n+1} = \mu + x_n \pm x_n^2$
* Two fixed points collide and annihilate as $\mu$ passes through $0$.


* **Transcritical:** $x_{n+1} = (1 + \mu)x_n \pm x_n^2$
* Fixed points exchange stability at $\mu = 0$.


* **Pitchfork (Symmetric):** $x_{n+1} = (1 + \mu)x_n \pm x_n^3$
* Supercritical ($-\text{sign}$) yields two stable fixed points flanking an unstable one; subcritical ($+\text{sign}$) yields the reverse.



---

## 3. Real Eigenvalue Crossing at $-1$ (Period-Doubling / Flip Bifurcation)

When a real multiplier exits the unit circle at $\lambda = -1$, local orientation-reversing dynamics near the fixed point cause $x_n$ to alternate sides on each step ($f'(x^*) < 0$).

### Mechanism and $1\text{D}$ Normal Form

Near $\mu = 0$, the $1\text{D}$ normal form is:


$$x_{n+1} = -(1 + \mu)x_n + c x_n^3 + \mathcal{O}(x_n^4)$$

1. At $\mu = 0$, $\lambda = -1$.
2. Examining the **second-iterate map** $f^2(x) = f(f(x))$:

$$f^2(x) = (1 + 2\mu)x - 2c x^3 + \mathcal{O}(x^4)$$



Notice that for $f^2$, the multiplier is $\lambda_{f^2} = (-1)^2 = +1$. The flip bifurcation of $f$ corresponds to a **pitchfork bifurcation** of $f^2$.
3. For $\mu > 0$, $f^2(x)$ creates two new fixed points $x_{(1)}$ and $x_{(2)}$ satisfying $f(x_{(1)}) = x_{(2)}$ and $f(x_{(2)}) = x_{(1)}$. This forms a **stable period-2 orbit** (a 2-cycle).

```
   Supercritical Flip Bifurcation:
   
           x ^               
             |      \     /   <-- Stable 2-cycle
             |       \   /
             |........\./........  Fixed point x* becomes unstable
             |         *
             |        / \
             +-------+---+-----> μ
                    μ = 0

```

### Classification

* **Supercritical ($c < 0$):** A stable 2-cycle branches off continuously as the fixed point destabilizes.
* **Subcritical ($c > 0$):** An unstable 2-cycle collapses onto the fixed point, destroying its basin of attraction.

---

## 4. Complex Eigenvalue Crossing (Neimark–Sacker / Torus Bifurcation)

When a complex-conjugate pair of multipliers crosses the unit circle at $\lambda_{1,2} = e^{\pm i \theta_0}$ (with $0 < \theta_0 < \pi$), stability is lost in a $2\text{D}$ plane. This is the discrete-time analogue of the continuous **Hopf bifurcation**.

### $2\text{D}$ Normal Form (Polar Coordinates)

In complex coordinates $z_n \in \mathbb{C}$, the local dynamics can be transformed to:


$$z_{n+1} = e^{i\theta_0} z_n (1 + d\mu) + a z_n \vert{}z_n\vert{}^2 + \mathcal{O}(\vert{}z_n\vert{}^4)$$

Converting to polar coordinates $(r_n, \phi_n)$ where $z_n = r_n e^{i\phi_n}$:


$$\begin{aligned} r_{n+1} &= (1 + d\mu)r_n + d_1 r_n^3 + \mathcal{O}(r_n^5) \\ \phi_{n+1} &= \phi_n + \theta_0 + c_1 r_n^2 + \mathcal{O}(r_n^4) \end{aligned}$$

where $d_1 = \text{Re}(e^{-i\theta_0} a)$ is the first Lyapunov coefficient for maps.

```
                   Neimark-Sacker Bifurcation
  
          Unstable x*                      Invariance:
           (Center)                      Closed Loop S^1
            .  /  |                         . - - - .
           /  *   .                       '   -->     '
          |  / \  |                      |  /  *  \  |
           .  |  /                        .   <--   .
          μ < 0 (Stable Point)               ` - - - '
                                          μ > 0 (Invariant Circle)

```

### Dynamical Consequences

* **Supercritical ($d_1 < 0$):** As $\mu$ increases through $0$, the fixed point loses stability, and a smooth, **invariant closed curve** $\mathbb{S}^1$ is born surrounding $x^*$.
* If the rotation number $\omega = \frac{\theta_0}{2\pi}$ is **irrational**, trajectories densely cover the invariant circle (dense quasiperiodic motion).
* If $\omega$ is **rational**, the dynamics lock into periodic orbits on the invariant circle.

---

## 5. Resonance Tongues (Arnold Tongues)

The dynamics on or near a Neimark–Sacker invariant circle depend critically on the rotation number $\omega(\mu) \approx \frac{\theta_0}{2\pi}$.

### Strong vs. Weak Resonances

When computing the normal form, terms of the form $z^p \bar{z}^q$ can only be removed via coordinate transformations if $e^{i(p - q - 1)\theta_0} \neq 1$. Resonances occur when:


$$k \theta_0 \equiv 0 \pmod{2\pi} \implies \theta_0 = 2\pi \frac{p}{k}, \quad p, k \in \mathbb{Z}^+$$

1. **Strong Resonances ($k = 1, 2, 3, 4$):**
* Normal form transformations break down at low orders.
* **$k=1$ ($\lambda = 1$):** Fold / Transcritical.
* **$k=2$ ($\lambda = -1$):** Period-doubling.
* **$k=3$ ($\theta_0 = 2\pi/3$):** Period-3 subharmonic resonance (creates a $3$-cycle directly; no standard invariant circle).
* **$k=4$ ($\theta_0 = \pi/2$):** Period-4 subharmonic resonance (complex interaction yielding up to four invariant closed curves or rapid onset of chaos).


2. **Weak Resonances ($k \ge 5$):**
* The Neimark–Sacker reduction holds to low order, but secondary **frequency-locking** occurs as the non-linear coupling strength increases.



### Arnold Resonance Tongues in $2\text{D}$ Parameter Space

If we consider a 2-parameter family of maps (e.g., controlling rotation frequency $\Omega$ and coupling parameter $K$, as in the **Arnold Circle Map** $x_{n+1} = x_n + \Omega - \frac{K}{2\pi}\sin(2\pi x_n)$):

```
     K ^
       |                V-shaped Resonance Tongues
       |          p/q = 1/3       1/2       2/3
       |           \   /         |   |         \   /
       |            \ /          |   |          \ /
       |             \           |   |           /
       |              \          |   |          /
       +---------------+---------+---+---------+-------> Ω
                       1/3       1/2       2/3

```

* **Tongue Boundaries:** Each rational ratio $\frac{p}{k}$ grounds a wedge-shaped region in parameter space touch $K=0$ at a single point $(\Omega = p/k, K = 0)$.
* **Inside a Tongue:** The motion is **mode-locked** (frequency-locked). The invariant circle breaks up into a pair of $k$-cycles: one **stable** (node or focus) and one **unstable** (saddle). The boundary of the tongue corresponds to a **saddle-node bifurcation of periodic orbits**.
* **Outside the Tongues:** The rotation number is irrational, yielding quasiperiodic motion. As $K$ increases, the tongues widen and eventually overlap, signaling the destruction of the smooth invariant curve and the transition to **chaos**.

---

## 6. Summary Comparison

| Bifurcation | Multipliers ($\lambda_i$) | Phase Space Effect | Physical Analogy |
| --- | --- | --- | --- |
| **Fold / SN** | $\lambda = +1$ | Fixed point creation/annihilation | Turning point / hysteresis |
| **Flip / PD** | $\lambda = -1$ | Fixed point $\to$ period-2 cycle | Subharmonic resonance ($f/2$) |
| **Neimark–Sacker** | $\lambda_{1,2} = e^{\pm i \theta_0}$ | Fixed point $\to$ invariant circle $\mathbb{S}^1$ | Onset of quasiperiodicity / discrete flutter |
| **Resonance Tongue** | Phase lock on $\mathbb{S}^1$ | Pair of $k$-cycles (stable/saddle) born | Frequency entrainment / mode locking |

---

[Normal Forms for Maps: Fixed Points & the Neimark-Sacker Bifurcation](https://www.youtube.com/watch?v=Gpbo88G5sgU)
This video provides a detailed mathematical derivation of normal forms for discrete maps, illustrating how eigenvalues crossing the unit circle lead to the Neimark-Sacker bifurcation and resonance conditions.

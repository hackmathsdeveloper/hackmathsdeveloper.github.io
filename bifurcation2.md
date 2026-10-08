
A fixed point of a smooth map \(x_{n+1}=f(x_n,\alpha)\) is locally stable when every multiplier (eigenvalue of the Jacobian) lies strictly inside the unit circle. Generically, stability is lost in one of three ways as a parameter varies: a real multiplier crosses at +1, a real multiplier crosses at −1, or a complex-conjugate pair \(e^{\pm i\theta_0}\) crosses together. These cases give the fold/transcritical/pitchfork family, the period-doubling (flip) bifurcation, and the Neimark–Sacker bifurcation. Two-parameter families of Neimark–Sacker points then produce resonance (Arnold) tongues.

## Unit circle and stability

For a flow \(\dot x=F(x)\), the stability boundary is the imaginary axis. For a map, it is the unit circle \(|\lambda|=1\), because a perturbation evolves as \(\delta_{n}\approx \lambda^n\delta_0\). When no multiplier lies on the circle (a hyperbolic fixed point), the Hartman–Grobman theorem says the map is locally conjugate to its linearization, so nothing can bifurcate there. The same theory covers a period-\(k\) orbit: treat it as a fixed point of \(f^k\), whose multipliers are the eigenvalues of the product of Jacobians along the orbit.

At a non-hyperbolic point you reduce to the center manifold, which is tangent to the critical eigenvectors. There are three generic codimension-one cases:

| Critical multipliers | Center manifold dim | Generic bifurcation | What appears |
|---|---|---|---|
| \(\lambda=+1\) | 1 | Fold (saddle-node) | Two fixed points collide and vanish |
| \(\lambda=-1\) | 1 | Flip (period-doubling) | A period-2 orbit |
| \(\lambda=e^{\pm i\theta_0}\), \(0<\theta_0<\pi\) | 2 | Neimark–Sacker | A closed invariant curve |

Poincaré maps link these to flows. A flip of the return map means a periodic orbit doubles its period. A Neimark–Sacker bifurcation of the return map means an invariant 2-torus is born (a torus bifurcation).

## Crossing at +1

On the 1D center manifold, write \(f(x,\alpha)=x+\dots\) The generic case is the fold, with normal form
\[
x\mapsto x+\beta\pm x^2 .
\]
It requires \(f_{xx}\neq0\) (nondegeneracy) and \(f_\alpha\neq0\) (transversality). For \(\pm\beta<0\) there are two fixed points \(x=\pm\sqrt{\mp\beta}\), one stable and one unstable. They merge at \(\beta=0\) and disappear afterwards. Unlike the other two cases, the fold doesn't hand stability to a new object. The orbit simply jumps elsewhere, which leads to hysteresis and to intermittency near the "ghost" of the lost fixed point.

If structure forces a fixed point to persist (for example \(f(0,\alpha)=0\)), the +1 crossing becomes transcritical: \(x\mapsto(1+\beta)x\pm x^2\), where two branches exchange stability. If a \(\mathbb Z_2\) symmetry \(f(-x)=-f(x)\) holds, it becomes a pitchfork: \(x\mapsto(1+\beta)x\pm x^3\). These are non-generic without such constraints. Recent work strengthens the standard theorems for all four elementary map bifurcations (saddle-node, transcritical, pitchfork, period-doubling) to differentiable conjugacy with their normal forms  [epubs.siam](https://epubs.siam.org/doi/abs/10.1137/22M1503701).

## Period-doubling at −1

When \(\lambda=-1\), orbits near the fixed point flip sides on every iterate. The generic 1D normal form is \(f_\mu(x)=-\mu x\pm x^3+\text{h.o.t.}\)  [scholarpedia](http://www.scholarpedia.org/article/Period_doubling). The restricted map is decreasing, so its only periodic orbits have period 1 or 2  [arxiv](https://arxiv.org/html/2206.04840v1). This is why the new object has to be a 2-cycle.

### Criticality via the second iterate

Write \(f(x)=-x+ax^2+bx^3+O(x^4)\) at criticality. Composing gives
\[
f^2(x)=x-2(a^2+b)\,x^3+O(x^4),
\]
so the second iterate looks like a pitchfork. The sign of \(a^2+b\) decides the outcome:

- **Supercritical** (\(a^2+b>0\)): once the fixed point goes unstable, a stable 2-cycle of amplitude \(O(\sqrt{|\beta|})\) appears.
- **Subcritical** (\(a^2+b<0\)): an unstable 2-cycle shrinks onto the fixed point and destroys its stability. The normal form \(y_{t+1}=-(1+\mu)y_t-y_t^3\) is a standard model  [sciencedirect](https://www.sciencedirect.com/topics/engineering/doubling-bifurcation).

### Worked example: the logistic map

For \(f(x)=rx(1-x)\), the fixed point \(x^*=1-1/r\) has multiplier \(2-r\), which reaches −1 at \(r=3\). A stable 2-cycle exists for \(3<r<1+\sqrt6\approx3.449\). Then the 2-cycle's own multiplier reaches −1 and it flips to a 4-cycle, and so on. The cascade accumulates near \(r\approx3.5699\), with ratios of successive intervals converging to Feigenbaum's \(\delta\approx4.669\).

## Neimark–Sacker invariant circles

Suppose a pair \(\mu_{1,2}=r(\alpha)e^{\pm i\theta(\alpha)}\) crosses with \(r(0)=1\). Define \(\beta=r(\alpha)-1\). In complex coordinates the truncated normal form is
\[
z\mapsto e^{i\theta(\beta)}(1+\beta)\,z+c(\beta)\,z|z|^2 .
\]
The theorem needs three conditions:

1. Transversality: \(r'(0)\neq0\).
2. Non-resonance: \(e^{ik\theta_0}\neq1\) for \(k=1,2,3,4\).
3. Nondegeneracy: the first Lyapunov coefficient \(d(0)=\mathrm{Re}[e^{-i\theta_0}c(0)]\neq0\).

If \(d(0)<0\), the bifurcation is supercritical. A unique stable closed invariant curve of radius \(O(\sqrt\beta)\) exists for \(\beta>0\). If \(d(0)>0\), it is subcritical: an unstable curve of radius \(O(\sqrt{-\beta})\) exists for \(\beta<0\)  [scholarpedia](http://www.scholarpedia.org/article/Neimark-Sacker_bifurcation).

### Computing the Lyapunov coefficient

Start from the original map, written with Taylor coefficients \(g_{jk}\) of \(z^j\bar z^k\). Kuznetsov's formula is
\[
d=\mathrm{Re}\!\left(\tfrac{e^{-i\theta_0}g_{21}}{2}\right)
-\mathrm{Re}\!\left(\tfrac{(1-2e^{i\theta_0})e^{-2i\theta_0}}{2(1-e^{i\theta_0})}g_{20}g_{11}\right)
-\tfrac12|g_{11}|^2-\tfrac14|g_{02}|^2 .
\]
Kuznetsov's lecture notes give a fully worked example where this comes out negative, \(-\frac{2+a^2}{2a(1+a^2)}\)  [staff.science.uu](https://www.staff.science.uu.nl/~kouzn101/NLDV/Lect10_11.pdf). Other references derive it for numerical schemes  [royalsocietypublishing](https://royalsocietypublishing.org/rspa/article/462/2074/3167/82012/Neimark-Sacker-bifurcations-in-a-non-standard), and BifurcationKit computes it automatically for Poincaré maps of periodic orbits  [docs.sciml](https://docs.sciml.ai/BifurcationKit/dev/ns/).

### Example: delayed logistic map

Take \((x,y)\mapsto(rx(1-y),\,x)\). At the fixed point \(x=y=1-1/r\), the Jacobian is \(\begin{pmatrix}1&-(r-1)\\1&0\end{pmatrix}\). Its trace is 1 and its determinant is \(r-1\). The pair reaches the unit circle at \(r=2\), with \(2\cos\theta_0=1\), so \(\theta_0=\pi/3\). The bifurcation is supercritical, and an attracting invariant loop grows as \(r\) increases past 2.

### How it differs from Hopf

A Hopf bifurcation produces a periodic orbit. A Neimark–Sacker bifurcation instead produces a whole circle, and the dynamics on that circle is a new problem: it's a circle map with rotation number near \(\theta_0/2\pi\). The truncated normal form rotates rigidly. The higher-order terms that were dropped decide whether orbits on the circle are quasi-periodic or phase-locked  [arxiv](https://arxiv.org/html/0711.1505v1).

## Resonance tongues

Now unfold in two parameters. The Neimark–Sacker points form a curve, and \(\theta_0\) varies along it. Wedge-shaped Arnold tongues grow out of every point where \(\theta_0/2\pi=p/q\)  [maia.ub](https://www.maia.ub.es/dsg/wsims08/slides/Osinga.pdf):

- Inside a tongue, the invariant circle carries a pair of period-\(q\) orbits with rotation number \(p/q\), usually a node and a saddle. The circle is the unstable manifold of the saddle, joined at the node. The dynamics is phase-locked.
- The tongue boundaries are fold (saddle-node) bifurcations of these \(q\)-cycles. Crossing a boundary destroys the locked pair  [maia.ub](https://www.maia.ub.es/dsg/wsims08/slides/Osinga.pdf).
- Between tongues, rotation numbers are irrational and the motion is quasi-periodic.
- Tongues for \(q\ge5\) are extremely thin at the tip. Near the NS curve their width scales roughly like \(\beta^{(q-2)/2}\). Low-\(q\) tongues dominate in practice.

### Strong resonances

The values \(q\le4\) (\(\theta_0=0,\pi,2\pi/3,\pi/2\)) are excluded from the theorem. These are the strong resonances. Here the theorem does not guarantee an invariant torus  [maia.ub](https://www.maia.ub.es/dsg/wsims08/slides/Osinga.pdf). Each is its own codimension-two point (1:1 Bogdanov–Takens type, 1:2, 1:3, 1:4). At these points the resonant terms \(\bar z^{q-1}\) enter the normal form at or before cubic order and change the local picture. For example, at 1:3 no invariant circle bifurcates locally. Instead a saddle 3-cycle passes through the fixed point.

### The Arnold circle map as a model

Arnold's original family is
\[
\theta_{i+1}=\theta_i+\Omega+\tfrac{K}{2\pi}\sin(2\pi\theta_i),
\]
and each V-shaped region touches down at a rational \(\Omega=p/q\) as \(K\to0\)  [en.wikipedia](https://en.wikipedia.org/wiki/Arnold_tongue). Its behaviour depends on \(K\):

- At \(K=0\) the tongues form a set of measure zero.
- At \(K=1\) they fill the line except for a Cantor set of dimension about 0.87  [mathworld.wolfram](https://mathworld.wolfram.com/ArnoldTongue.html). Plotting rotation number against \(\Omega\) gives the "devil's staircase."
- For \(K>1\) the map stops being invertible. Tongues overlap and chaos is possible  [chaosdiscovery](https://www.chaosdiscovery.com/module1c-circledeep.html).

The \(K=0\) axis is not itself a Neimark–Sacker curve. Still, it is a good model of the dynamics on an invariant circle near one  [maia.ub](https://www.maia.ub.es/dsg/wsims08/slides/Osinga.pdf). Further from the NS curve, inside tongues, the invariant circle can lose smoothness and break up, for example through homoclinic tangles of the saddle cycle or through a period-doubling of the node. This is one route from quasi-periodicity to chaos. Variants show other tongue shapes: piecewise-linear circle maps give "sausage" tongues that pinch to zero width  [iopscience.iop](https://iopscience.iop.org/article/10.1088/0253-6102/8/1/1), and area-preserving maps have their own tongue phenomena  [arxiv](https://arxiv.org/abs/2206.10040).

### Minimal code to map tongues

```python
import numpy as np
def rot_num(Om, K, N=2000, burn=500):
    th = 0.0
    for _ in range(burn): th = th + Om + K/(2*np.pi)*np.sin(2*np.pi*th)
    th0 = th
    for _ in range(N):    th = th + Om + K/(2*np.pi)*np.sin(2*np.pi*th)
    return (th - th0)/N   # lift, no mod 1
```
Scan a grid of \((\Omega,K)\) and colour each point by `rot_num`. Plateaus at rationals \(p/q\) (detect them with a tolerance such as \(10^{-4}\)) trace out the tongues.


Holomorphic functions originate from asking for a complex analogue of “differentiable function” and discovering that complex differentiability is so rigid it forces power‑series behavior, which Cauchy and others realized in the 19th century. [en.wikipedia](https://en.wikipedia.org/wiki/Holomorphic_function)

***

## 1. Basic notion: complex differentiability

Start with a function \(f:\mathbb{C}\to\mathbb{C}\).  

- We mimic the real derivative and define
  \[
  f'(z_0)=\lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}
  \]
  if that limit exists. [jaikrishnanj.github](https://jaikrishnanj.github.io/CA18/Holomorphic%20functions.pdf)
- The crucial difference: in \(\mathbb{C}\) you can approach \(z_0\) from infinitely many directions, not just from left/right as in \(\mathbb{R}\). [brilliant](https://brilliant.org/wiki/holomorphic-function/)

If **that** limit exists in a neighborhood of each point in a domain \(D\subset\mathbb{C}\), we call \(f\) **holomorphic on \(D\)**. [en.wikipedia](https://en.wikipedia.org/wiki/Holomorphic_function)

So conceptually, holomorphic = complex‑differentiable in an open region (not just at one point).

***

## 2. Why this is special in complex dimension 1

Historically, the surprise was that this simple definition is much stronger in complex analysis than in real analysis.

- For real functions, “differentiable once” does not imply analytic or even twice differentiable.  
- For complex functions, Cauchy showed that if \(f\) is complex differentiable on a region, then:
  - It has derivatives of all orders.  
  - It is equal locally to a convergent power series (analytic).  
  - It satisfies Cauchy’s integral formula and all the machinery that follows. [staff.fnwi.uva](https://staff.fnwi.uva.nl/j.j.o.o.wiegerinck/edu/scv/scv.pdf)

This discovery (1830s–1840s, Cauchy) effectively **created** the modern theory of holomorphic functions: the right notion of “nice function” in the complex setting is “once complex‑differentiable on a domain.” [staff.fnwi.uva](https://staff.fnwi.uva.nl/j.j.o.o.wiegerinck/edu/scv/scv.pdf)

So the origin is: take the most naive generalization of the derivative to \(\mathbb{C}\), and discover that it has unexpectedly powerful consequences.

***

## 3. Geometric and linguistic origin

Geometrically:

- A holomorphic function between domains in \(\mathbb{C}\) preserves the complex structure; it is exactly a map that in local complex coordinates looks like a convergent power series. [ihes](https://www.ihes.fr/~dustin/files/RiemannSurfaces/RS1.pdf)
- On a Riemann surface, “holomorphic function” means a map locally modeled on open subsets of \(\mathbb{C}\) with holomorphic transition maps; this is the natural notion of a structure‑preserving map. [ihes](https://www.ihes.fr/~dustin/files/RiemannSurfaces/RS1.pdf)

Linguistically:

- “Holomorphic” comes from Greek *holos* (whole) and *morphe* (form), roughly “having a globally coherent form.” [mathworld.wolfram](https://mathworld.wolfram.com/HolomorphicFunction.html)
- It is essentially synonymous with “analytic function,” but many authors prefer “holomorphic” to emphasize the geometric/structural aspect rather than just power‑series behavior. [mathworld.wolfram](https://mathworld.wolfram.com/HolomorphicFunction.html)

***

## 4. Cauchy–Riemann viewpoint

Another way to see the origin: write \(z=x+iy\) and \(f(z)=u(x,y)+iv(x,y)\).

Requiring complex differentiability at a point leads to the **Cauchy–Riemann equations**
\[
u_x = v_y,\quad u_y = -v_x
\]
plus mild regularity conditions. [jaikrishnanj.github](https://jaikrishnanj.github.io/CA18/Holomorphic%20functions.pdf)

So from PDE viewpoint:

- Holomorphic functions are exactly those real 2D vector fields \((u,v)\) that satisfy Cauchy–Riemann, hence are harmonic conjugates etc. [en.wikipedia](https://en.wikipedia.org/wiki/Holomorphic_function)
- This ties holomorphic functions tightly to potential theory and harmonic functions, which is why they show up in physics (electrostatics, incompressible flow).

Thus, holomorphic functions originate simultaneously from:

- Extending the derivative to complex variables.  
- Recognizing the strong consequences (Cauchy’s theorems).  
- Characterizing them by Cauchy–Riemann and harmonicity.

***

## 5. Functions of several complex variables

The same idea generalizes:

- A function \(f:\mathbb{C}^n\to\mathbb{C}\) is **holomorphic** if it is complex‑differentiable in each variable and satisfies the appropriate multidimensional analogue of Cauchy–Riemann. [staff.fnwi.uva](https://staff.fnwi.uva.nl/j.j.o.o.wiegerinck/edu/scv/scv.pdf)
- Again, holomorphy implies local power‑series expansion in several variables: the analytic and geometric content gets even richer. [staff.fnwi.uva](https://staff.fnwi.uva.nl/j.j.o.o.wiegerinck/edu/scv/scv.pdf)

So “holomorphic” is the natural origin point for all of complex analytic geometry: it is the right generalization of “smooth and compatible with the complex structure.”

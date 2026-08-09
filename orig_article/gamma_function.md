
The **Gamma function** is one of the most important objects in mathematics.

It generalizes the factorial:

[
n! = 1\cdot2\cdot3\cdots n
]

to:

* non-integer values
* complex numbers
* analytic continuation over the complex plane

The core identity is:

[
\Gamma(n+1)=n!
]

for integers (n\ge0).

Visualization of the defining recurrence:

\Gamma(z+1)=z\Gamma(z)

---

# 1. Motivation: extending factorials

Factorials are defined only for integers:

[
1!,2!,3!,\dots
]

Question:

Can we define:

[
\left(\frac12\right)!
]

or:

[
\pi!
]

or even:

[
(2+3i)!
]

Euler solved this by constructing the Gamma function.

---

# 2. Euler integral definition

The Gamma function is defined by:

[
\Gamma(z)
=========

\int_0^\infty
t^{z-1}e^{-t},dt
]

valid for:

[
\Re(z)>0
]

Visualization of Euler’s integral:

\Gamma(z)=\int_0^{\infty} t^{z-1}e^{-t},dt

---

# 3. Why this definition works

The key property comes from integration by parts.

Take:

[
\Gamma(z+1)
===========

\int_0^\infty t^z e^{-t}dt
]

Use:

* (u=t^z)
* (dv=e^{-t}dt)

Then:

* (du=zt^{z-1}dt)
* (v=-e^{-t})

Integration by parts gives:

[
\Gamma(z+1)
===========

\left[-t^z e^{-t}\right]_0^\infty
+
z\int_0^\infty t^{z-1}e^{-t}dt
]

Boundary term vanishes:

[
\Gamma(z+1)
===========

z\Gamma(z)
]

This is the fundamental recursion.

---

# 4. Recovering factorials

Now compute:

[
\Gamma(1)
=========

# \int_0^\infty e^{-t}dt

1
]

Then:

[
\Gamma(2)=1\Gamma(1)=1
]

[
\Gamma(3)=2\Gamma(2)=2
]

[
\Gamma(4)=3\Gamma(3)=6
]

Thus:

[
\Gamma(n+1)=n!
]

exactly.

---

# 5. Half-integer values

One of the most famous results:

[
\Gamma\left(\frac12\right)=\sqrt{\pi}
]

This is astonishing because:

* factorials suddenly connect to (\pi)
* Gaussian integrals appear
* probability theory emerges

Visualization:

\Gamma\left(\frac12\right)=\sqrt{\pi}

---

# 6. Derivation of (\Gamma(1/2))

Start with:

[
\Gamma\left(\frac12\right)
==========================

\int_0^\infty t^{-1/2}e^{-t}dt
]

Substitute:

[
t=x^2
]

Then:

[
dt=2x,dx
]

and:

[
t^{-1/2}=\frac1x
]

So:

[
\Gamma\left(\frac12\right)
==========================

2\int_0^\infty e^{-x^2}dx
]

Now use the Gaussian integral:

[
\int_{-\infty}^\infty e^{-x^2}dx
================================

\sqrt{\pi}
]

Thus:

[
\int_0^\infty e^{-x^2}dx
========================

\frac{\sqrt{\pi}}2
]

Therefore:

[
\Gamma\left(\frac12\right)=\sqrt{\pi}
]

---

# 7. General half-factorials

Using recursion:

[
\Gamma\left(\frac32\right)
==========================

# \frac12\Gamma\left(\frac12\right)

\frac{\sqrt{\pi}}2
]

[
\Gamma\left(\frac52\right)
==========================

# \frac32\cdot\frac12\sqrt{\pi}

\frac{3\sqrt{\pi}}4
]

Thus:

[
\left(\frac12\right)!
=====================

# \Gamma\left(\frac32\right)

\frac{\sqrt{\pi}}2
]

---

# 8. Analytic continuation

The integral definition works only for:

[
\Re(z)>0
]

But the recursion:

[
\Gamma(z)=\frac{\Gamma(z+1)}{z}
]

extends Gamma to almost all complex numbers.

The only singularities occur at:

[
z=0,-1,-2,-3,\dots
]

These are simple poles.

---

# 9. Reflection formula

Euler discovered:

[
\Gamma(z)\Gamma(1-z)
====================

\frac{\pi}{\sin(\pi z)}
]

Visualization:

\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}

This connects:

* trigonometry
* analytic continuation
* poles
* complex analysis

---

# 10. Weierstrass infinite product

Gamma has an infinite-product structure:

[
\frac1{\Gamma(z)}
=================

ze^{\gamma z}
\prod_{n=1}^\infty
\left(1+\frac zn\right)e^{-z/n}
]

where:

* (\gamma) is Euler–Mascheroni constant

This reveals:

* zeros
* poles
* entire-function structure

---

# 11. Stirling’s approximation

For large (n):

[
n!
\sim
\sqrt{2\pi n}\left(\frac ne\right)^n
]

equivalently:

[
\Gamma(z)
\sim
\sqrt{2\pi},
z^{z-\frac12}e^{-z}
]

Visualization:

\Gamma(z)\sim\sqrt{2\pi},z^{z-\frac12}e^{-z}

This is foundational in:

* asymptotic analysis
* statistical mechanics
* entropy
* combinatorics

---

# 12. Connection to Beta function

The Beta function:

[
B(x,y)
======

\int_0^1
t^{x-1}(1-t)^{y-1}dt
]

satisfies:

[
B(x,y)
======

\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}
]

This identity drives huge parts of:

* probability
* quantum field theory
* Feynman parameterization

---

# 13. Gamma inside hypergeometric functions

Recall:

[
(a)_k
=====

\frac{\Gamma(a+k)}{\Gamma(a)}
]

Thus hypergeometric coefficients are fundamentally Gamma ratios.

The entire hypergeometric universe is built from Gamma functions.

---

# 14. Probabilistic meaning

Gamma appears naturally in probability distributions:

* Gamma distribution
* Beta distribution
* Chi-square distribution
* Student-t distribution
* Dirichlet distribution

Normalization constants are Gamma ratios.

Example:

[
f(x)=
\frac{x^{k-1}e^{-x/\theta}}
{\Gamma(k)\theta^k}
]

---

# 15. Geometric meaning

Gamma measures generalized volume growth.

Example:

Volume of the (n)-sphere:

[
V_n
===

\frac{\pi^{n/2}}
{\Gamma\left(\frac n2+1\right)}
]

This is why Gamma appears in:

* geometry
* statistical mechanics
* high-dimensional spaces

---

# 16. Complex-analysis structure

Gamma is:

* meromorphic
* no zeros
* poles at negative integers
* logarithmically convex

It is essentially the unique analytic continuation of factorial satisfying:

[
f(z+1)=zf(z)
]

with mild regularity conditions.

This uniqueness is formalized by the Bohr–Mollerup theorem.

---

# 17. Low-level asymptotic mechanics

Using Laplace’s method on:

[
\Gamma(z)
=========

\int_0^\infty t^{z-1}e^{-t}dt
]

observe exponent:

[
(z-1)\ln t - t
]

Maximum occurs near:

[
t=z
]

Expanding around saddle point produces Stirling’s formula.

This is the birth of steepest-descent asymptotics.

---

# 18. Why Gamma is everywhere

Gamma appears whenever you have:

* repeated multiplicative growth
* continuous factorials
* Gaussian integrals
* normalization constants
* rotational symmetry
* Mellin transforms
* scale invariance

It is one of the central organizing functions of analysis.

At a deep level:

* exponentials linearize addition
* Gamma linearizes multiplication/recurrence structures

That is why it becomes unavoidable across mathematics and physics.


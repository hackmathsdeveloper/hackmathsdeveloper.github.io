---
title: "Euler's Reflection Formula: The Identity That Proves Γ(½) = √π in One Line"
date: 2026-05-27
categories:
  - Special Functions
  - Mathematics
tags:
  - euler-reflection
  - gamma-function
  - beta-function
  - residue-calculus
  - complex-analysis
  - sine-product
share: true
read_time: true
excerpt: "Γ(z)Γ(1−z) = π/sin(πz). Five symbols that connect the Gamma function to trigonometry, explain where √π comes from in half-factorials, encode all of Gamma's poles, and secretly power the functional equation of the Riemann zeta function. This is the story of Euler's most beautiful formula — derived three different ways, from Beta integrals to contour integration to infinite products."
---

**Challenge to the reader:** Set $z = 1/3$ in the reflection formula. What is $\Gamma(1/3)\Gamma(2/3)$? Now compute $\Gamma(1/3)$ numerically (it's about 2.6789). Use the reflection formula to compute $\Gamma(2/3)$ without evaluating any integrals.

---

The identity

$$
\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}
$$

is called the **Euler reflection formula**.

It is one of the deepest formulas in classical analysis because it links:

* the Gamma function
* trigonometric functions
* analytic continuation
* poles and residues
* complex analysis

The derivation is beautiful because it emerges from several seemingly unrelated structures.

---

## 1. Big-picture intuition

The Gamma function generalizes factorials.

The sine function encodes periodicity and zeros at integers.

The reflection formula tells us:

> Gamma values at $z$ and $1-z$ are dual/complementary.

It is essentially a symmetry around $z=\frac12$.

---

## 2. Strategy of derivation

The clean classical derivation proceeds through:

1. Beta function
2. Trigonometric substitution
3. Complex analysis identities

The key bridge is:

$$
B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}
$$

Setting $y=1-x$ gives:

$$
B(z,1-z) = \Gamma(z)\Gamma(1-z)
$$

because $\Gamma(1)=1$.

So the problem reduces to evaluating $B(z,1-z)$.

---

## 3. Start from the Beta integral

The Beta function is:

$$
B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}dt
$$

Substitute $x=z$, $y=1-z$. Then:

$$
B(z,1-z) = \int_0^1 t^{z-1}(1-t)^{-z}dt
$$

Now we must evaluate this integral explicitly.

---

## 4. Trigonometric substitution

Use $t=\frac{1}{1+u}$. Then $dt=-\frac1{(1+u)^2}du$ and $1-t=\frac{u}{1+u}$.

Now compute factors carefully.

First factor:

$$
t^{z-1} = (1+u)^{-(z-1)}
$$

Second factor:

$$
(1-t)^{-z} = \left(\frac{u}{1+u}\right)^{-z} = u^{-z}(1+u)^z
$$

Multiply:

$$
t^{z-1}(1-t)^{-z} = u^{-z}(1+u)
$$

Then include $dt$:

$$
u^{-z}(1+u)\frac{du}{(1+u)^2} = \frac{u^{-z}}{1+u}du
$$

Limits: $t=0 \Rightarrow u=\infty$, $t=1 \Rightarrow u=0$.

Thus:

$$
B(z,1-z) = \int_0^\infty \frac{u^{-z}}{1+u}du
$$

Rewrite exponent: $u^{-z}=u^{(1-z)-1}$. So:

$$
B(z,1-z) = \int_0^\infty \frac{u^{(1-z)-1}}{1+u}du
$$

---

## 5. The crucial contour-integral identity

Complex analysis proves:

$$
\int_0^\infty \frac{x^{a-1}}{1+x}dx = \frac{\pi}{\sin(\pi a)}
$$

for $0 < a < 1$.

Set $a=1-z$. Then:

$$
B(z,1-z) = \frac{\pi}{\sin(\pi(1-z))}
$$

Using $\sin(\pi-\theta)=\sin\theta$, we obtain:

$$
B(z,1-z) = \frac{\pi}{\sin(\pi z)}
$$

Finally:

$$
\boxed{ \Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)} }
$$

---

## 6. Where does the integral identity come from?

The deep core is:

$$
\int_0^\infty \frac{x^{a-1}}{1+x}dx = \frac{\pi}{\sin(\pi a)}
$$

This comes from residue calculus.

---

## 7. Residue-calculus derivation

Consider $f(w)=\frac{w^{a-1}}{1+w}$ where $w^{a-1}=e^{(a-1)\log w}$ has a branch cut along the positive real axis.

Use a keyhole contour around the branch cut.

The function has one pole at $w=-1$ with residue:

$$
\operatorname{Res}_{w=-1}f(w) = (-1)^{a-1} = e^{i\pi(a-1)}
$$

Applying the residue theorem:

$$
(1-e^{2\pi i(a-1)}) \int_0^\infty\frac{x^{a-1}}{1+x}dx = 2\pi i\,e^{i\pi(a-1)}
$$

Simplifying exponentials eventually yields:

$$
\int_0^\infty \frac{x^{a-1}}{1+x}dx = \frac{\pi}{\sin(\pi a)}
$$

This is where sine emerges naturally.

---

## 8. Why sine appears

The sine function encodes periodicity of complex exponentials:

$$
\sin(\pi z) = \frac{e^{i\pi z}-e^{-i\pi z}}{2i}
$$

The reflection formula ultimately comes from:

* winding around the origin
* branch cuts
* exponential phase jumps

The denominator $\sin(\pi z)$ measures the discontinuity of complex powers across the branch cut.

---

## 9. Pole structure

Gamma has poles at $0,-1,-2,\dots$.

The RHS predicts this perfectly because $\sin(\pi z)=0$ at integers.

Thus $\frac{\pi}{\sin(\pi z)}$ has simple poles at integers.

The reflection formula therefore encodes Gamma's singularity structure.

---

## 10. Example: derive $\Gamma(1/2)$

Set $z=\frac12$. Then:

$$
\Gamma\left(\frac12\right)^2 = \frac{\pi}{\sin(\pi/2)}
$$

Since $\sin(\pi/2)=1$, we get:

$$
\Gamma\left(\frac12\right)^2=\pi
$$

thus:

$$
\boxed{ \Gamma\left(\frac12\right)=\sqrt{\pi} }
$$

The reflection formula instantly explains why $\pi$ appears in half-factorials.

---

**Challenge to the reader:** Set $z = 1/4$ in the reflection formula. Express $\Gamma(3/4)$ in terms of $\Gamma(1/4)$ and a trigonometric value. Can you find a closed form for $\Gamma(1/4)\Gamma(3/4)$? What famous constant appears?

---

## 11. Infinite-product derivation

Another derivation uses Euler's infinite products.

Sine has product:

$$
\sin(\pi z) = \pi z \prod_{n=1}^\infty \left(1-\frac{z^2}{n^2}\right)
$$

Gamma has Weierstrass product:

$$
\frac1{\Gamma(z)} = ze^{\gamma z} \prod_{n=1}^\infty \left(1+\frac zn\right)e^{-z/n}
$$

Multiplying $\Gamma(z)\Gamma(1-z)$ causes exponentials to cancel, leaving precisely the sine product.

This derivation reveals the deep algebraic compatibility between Gamma and sine.

---

## 12. Geometric interpretation

Reflection formula represents a symmetry $z \leftrightarrow 1-z$ around $z=\frac12$.

This duality appears everywhere:

* modular forms
* zeta functions
* Fourier transforms
* quantum field theory

---

## 13. Connection to Riemann zeta function

The functional equation of the zeta function depends critically on Gamma reflection:

$$
\zeta(s) = 2^s\pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s)\,\zeta(1-s)
$$

Without Euler reflection, analytic number theory would look very different.

---

## 14. Deep analytic meaning

The reflection formula says: Gamma is not arbitrary.

Its global analytic structure is rigidly tied to:

* periodicity
* complex rotation
* branch cuts
* residues
* trigonometric symmetry

At a deep level, $\Gamma(z)$ is the multiplicative analogue of exponentials, while $\sin(\pi z)$ measures the obstruction to extending factorial symmetry across negative numbers.

That obstruction becomes the reflection formula.

---

**Final challenge:** The reflection formula implies $\Gamma(z)$ never equals zero (because the RHS is $\pi / \sin(\pi z)$ which is never zero). Prove this fact directly from the Euler integral definition — why can't the integral ever vanish for $\Re(z) > 0$?

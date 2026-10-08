
That statement refers to a well-known fact in the theory of equations: **any general quintic can be reduced to the "Bring–Jerrard" normal form**, and then further normalized to a one-parameter family like  

\[
x^5 + px + q = 0
\]

or, after scaling, to something like  

\[
p x^5 + q x + 1 = 0.
\]

Here’s the idea in more detail.

## 1. Removing intermediate terms

A general quintic

\[
a x^5 + b x^4 + c x^3 + d x^2 + e x + f = 0
\]

can be transformed by a sequence of **Tschirnhaus transformations** (rational changes of variable) to eliminate the \(x^4\), \(x^3\), and \(x^2\) terms. The result is the **principal quintic** or **Bring–Jerrard form**:

\[
x^5 + p x + q = 0.
\]

This reduction uses solving only lower-degree equations (quadratics, cubics, quartics) to find the transformation coefficients, so it does not require solving the quintic itself.

## 2. Scaling to \(p x^5 + q x + 1 = 0\)

Starting from

\[
x^5 + p x + q = 0,
\]

if \(q \neq 0\), divide by \(q\):

\[
\frac{1}{q} x^5 + \frac{p}{q} x + 1 = 0.
\]

Let

\[
P = \frac{1}{q}, \qquad Q = \frac{p}{q}.
\]

Then the equation becomes

\[
P x^5 + Q x + 1 = 0,
\]

which is exactly the form you wrote (with \(p,q\) renamed). If \(q = 0\), the equation is \(x^5 + p x = 0\), which is solvable by factoring out \(x\), so the interesting case is \(q \neq 0\).

## 3. Why this matters

- It shows that **the general quintic depends on only two essential parameters** after lower-degree transformations.
- It is the starting point for **Bring radicals**, **elliptic modular solutions**, and the **Klein icosahedral solution** of the quintic.
- It also makes clear why the quintic is not solvable by radicals in general: the reduced form \(x^5 + p x + q = 0\) still cannot be solved by a general radical formula, as proved by Abel and Galois.

So the statement is essentially correct: any quintic can be "retooled" into the form

\[
p x^5 + q x + 1 = 0
\]

with complex \(p,q\) determined by the original coefficients, assuming the original quintic is not degenerate in a way that makes the reduction trivial.

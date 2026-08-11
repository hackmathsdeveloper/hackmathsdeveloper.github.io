
Jacobi elliptic functions are the natural nonlinear generalization of sine and cosine. They arise when you invert an elliptic integral—much as \(\sin\) inverts the elementary integral \(\int d\theta\)—and are central to nonlinear oscillations, elliptic curves, integrable systems, and conformal mapping. [mathworld.wolfram](https://mathworld.wolfram.com/JacobiEllipticFunctions.html)

## Core definition

Fix an elliptic **parameter** \(m\) (often \(0\le m\le1\)); some texts instead use the modulus \(k\), where \(m=k^2\). Define the incomplete elliptic integral of the first kind:

\[
u = F(\phi\mid m)
= \int_0^\phi \frac{d\theta}{\sqrt{1-m\sin^2\theta}}.
\]

Its inverse is the Jacobi amplitude:

\[
\phi = \operatorname{am}(u\mid m).
\]

The three basic functions are then

\[
\operatorname{sn}(u\mid m)=\sin(\operatorname{am}(u\mid m)),
\]

\[
\operatorname{cn}(u\mid m)=\cos(\operatorname{am}(u\mid m)),
\]

\[
\operatorname{dn}(u\mid m)=
\sqrt{1-m\sin^2(\operatorname{am}(u\mid m))}.
\]

They are commonly called *sine-amplitude*, *cosine-amplitude*, and *delta-amplitude*. [mathworld.wolfram](https://mathworld.wolfram.com/JacobiEllipticFunctions.html)

## Why they generalize trigonometry

At \(m=0\), the defining integral is just \(u=\phi\), so the functions reduce exactly to familiar circular functions:

\[
\operatorname{sn}(u\mid0)=\sin u,\qquad
\operatorname{cn}(u\mid0)=\cos u,\qquad
\operatorname{dn}(u\mid0)=1.
\]

At the other degenerate endpoint, \(m=1\),

\[
\operatorname{sn}(u\mid1)=\tanh u,\qquad
\operatorname{cn}(u\mid1)=\operatorname{sech}u,\qquad
\operatorname{dn}(u\mid1)=\operatorname{sech}u.
\]

So \(m\) is a deformation knob taking the system continuously from circular/trigonometric behavior to hyperbolic/soliton-like behavior. This is a useful mental model for nonlinear-wave and nonlinear-oscillator problems.

## Fundamental identities

The analogue of \(\sin^2u+\cos^2u=1\) is:

\[
\operatorname{sn}^2(u\mid m)+\operatorname{cn}^2(u\mid m)=1.
\]

A second identity has no direct ordinary-trig counterpart:

\[
\operatorname{dn}^2(u\mid m)+m\,\operatorname{sn}^2(u\mid m)=1.
\]

Their derivative algebra is compact:

\[
\frac{d}{du}\operatorname{sn}u=\operatorname{cn}u\,\operatorname{dn}u,
\]

\[
\frac{d}{du}\operatorname{cn}u=-\operatorname{sn}u\,\operatorname{dn}u,
\]

\[
\frac{d}{du}\operatorname{dn}u=-m\,\operatorname{sn}u\,\operatorname{cn}u.
\]

Here and below, \(\mid m\) is suppressed when it is fixed.

Combining these yields the elliptic-curve differential equation:

\[
\left(\frac{d}{du}\operatorname{sn}u\right)^2
=
(1-\operatorname{sn}^2u)(1-m\operatorname{sn}^2u).
\]

Writing \(x=\operatorname{sn}(u\mid m)\) and \(y=x'\), the pair lies on

\[
y^2=(1-x^2)(1-mx^2),
\]

a genus-one algebraic curve. That relationship is why these functions are called *elliptic*: they uniformize elliptic curves.

## Periodicity

Unlike sine and cosine, which have one fundamental real period, Jacobi elliptic functions extend to **doubly periodic meromorphic functions** over \(\mathbb C\). Their periods form a lattice in the complex plane. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Jacobi_elliptic_functions)

Define the complete elliptic integral

\[
K(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}},
\]

and let \(K'(m)=K(1-m)\). Along the real axis:

- \(\operatorname{sn}(u\mid m)\) and \(\operatorname{cn}(u\mid m)\) have real period \(4K(m)\).
- \(\operatorname{dn}(u\mid m)\) has real period \(2K(m)\).

As \(m\to0\), \(K(m)\to\pi/2\), recovering the \(2\pi\) period of sine and cosine. As \(m\to1^-\), \(K(m)\to\infty\), which matches the loss of real periodicity in the \(\tanh\) limit.

## The other nine functions

Historically, Jacobi functions are denoted \(\operatorname{pq}(u)\), for \(p,q\in\{s,c,d,n\}\). The primary functions are \(\operatorname{sn}\), \(\operatorname{cn}\), and \(\operatorname{dn}\); \(n\) means “no factor,” i.e. the constant \(1\).

The rest are ratios or reciprocals:

\[
\operatorname{ns}=\frac1{\operatorname{sn}},\quad
\operatorname{nc}=\frac1{\operatorname{cn}},\quad
\operatorname{nd}=\frac1{\operatorname{dn}},
\]

\[
\operatorname{sc}=\frac{\operatorname{sn}}{\operatorname{cn}},\quad
\operatorname{sd}=\frac{\operatorname{sn}}{\operatorname{dn}},\quad
\operatorname{cd}=\frac{\operatorname{cn}}{\operatorname{dn}},
\]

with \(\operatorname{cs}\), \(\operatorname{ds}\), and \(\operatorname{dc}\) their reciprocals. This mirrors \(\tan=\sin/\cos\), but adds a third primitive quantity, \(\operatorname{dn}\). [doc.sagemath](https://doc.sagemath.org/html/en/reference/functions/sage/functions/jacobi.html)

## Canonical example: nonlinear pendulum

For a pendulum of length \(\ell\),

\[
\ddot{\theta}+\frac{g}{\ell}\sin\theta=0.
\]

The usual \(\sin\theta\approx\theta\) approximation gives a sinusoidal solution, but it fails at large amplitude. For a maximum angular displacement \(\theta_0\), define

\[
m=\sin^2\left(\frac{\theta_0}{2}\right).
\]

An exact librating solution can be written as

\[
\sin\frac{\theta(t)}{2}
=
\sqrt m\,
\operatorname{sn}\left(
K(m)-\sqrt{\frac g\ell}\,t
\;\middle|\;m
\right).
\]

Its period is

\[
T=4\sqrt{\frac{\ell}{g}}\,K(m).
\]

This explicitly shows amplitude-dependent period: \(K(m)\) grows with \(m\), so a large-amplitude pendulum oscillates more slowly than the small-angle prediction. Jacobi functions are therefore not merely exotic notation—they are the exact waveform of a standard nonlinear system. [mathworld.wolfram](https://mathworld.wolfram.com/JacobiEllipticFunctions.html)

## Connections useful in practice

- **Integrable PDEs:** \(\operatorname{sn}\), \(\operatorname{cn}\), and \(\operatorname{dn}\) describe periodic traveling-wave solutions of equations such as KdV and nonlinear Schrödinger; soliton profiles often emerge in the \(m\to1\) hyperbolic limit.
- **Elliptic curves:** They provide an analytic parameterization of quartic elliptic curves such as \(y^2=(1-x^2)(1-mx^2)\).
- **Theta functions:** Jacobi elliptic functions can be expressed as quotients of theta functions, which makes modular transformations and complex-period behavior tractable. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Jacobi_elliptic_functions)
- **Numerics:** Most scientific libraries implement them as `ellipj(u, m)` or similarly named routines. Check whether the API expects \(m\) or \(k\): this is the most common source of incorrect results. [johndcook](https://www.johndcook.com/blog/2018/10/12/jacobi-function-nomenclature/)

A concise mnemonic is:

\[
\boxed{\operatorname{sn},\operatorname{cn},\operatorname{dn}
\text{ are } \sin,\cos,1
\text{ deformed by the elliptic parameter }m.}
\]

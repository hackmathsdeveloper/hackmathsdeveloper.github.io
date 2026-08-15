
Starting from the postulates of nonrelativistic quantum mechanics and the harmonic restoring force, the stationary states are Gaussian envelopes multiplied by Hermite polynomials. Normalizability—not merely algebra—forces the energy spectrum to be discrete. [hyperphysics.phy-astr.gsu](http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/hosc2.html)

## 1. Hamiltonian and eigenvalue equation

A one-dimensional oscillator has classical potential

\[
V(x)=\frac12m\omega^2x^2,
\]

so canonical quantization gives

\[
\hat H
=
\frac{\hat p^2}{2m}+\frac12m\omega^2\hat x^2,
\qquad
\hat p=-i\hbar\frac{d}{dx}.
\]

An energy eigenstate satisfies

\[
\hat H\psi(x)=E\psi(x),
\]

or explicitly,

\[
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}
+\frac12m\omega^2x^2\psi(x)
=
E\psi(x).
\tag{1}
\]

The physical boundary condition is

\[
\int_{-\infty}^{\infty}|\psi(x)|^2dx<\infty,
\]

so \(\psi(x)\) must vanish sufficiently rapidly as \(|x|\to\infty\).  [chem.libretexts](https://chem.libretexts.org/Courses/Pacific_Union_College/Quantum_Chemistry/05:_The_Harmonic_Oscillator_and_the_Rigid_Rotor/5.06:_The_Harmonic-Oscillator_Wavefunctions_involve_Hermite_Polynomials)

## 2. Make the equation dimensionless

Define the oscillator length and dimensionless coordinate

\[
\ell=\sqrt{\frac{\hbar}{m\omega}},
\qquad
\xi=\frac{x}{\ell}
=
\sqrt{\frac{m\omega}{\hbar}}\,x.
\]

Also set

\[
\varepsilon=\frac{2E}{\hbar\omega}.
\]

Because

\[
\frac{d^2}{dx^2}
=
\frac{m\omega}{\hbar}\frac{d^2}{d\xi^2},
\]

equation (1) becomes

\[
\frac{d^2\psi}{d\xi^2}
+
\left(\varepsilon-\xi^2\right)\psi=0.
\tag{2}
\]

For large \(|\xi|\), the \(-\xi^2\) term dominates:

\[
\psi''-\xi^2\psi\simeq0.
\]

Its acceptable asymptotic behavior is Gaussian decay, \(\psi\sim e^{-\xi^2/2}\); the alternate behavior \(e^{+\xi^2/2}\) is non-normalizable.

Thus write

\[
\psi(\xi)=e^{-\xi^2/2}h(\xi).
\tag{3}
\]

## 3. Hermite equation

Differentiating (3),

\[
\psi'
=
e^{-\xi^2/2}(h'-\xi h),
\]

\[
\psi''
=
e^{-\xi^2/2}
\left[h''-2\xi h'+(\xi^2-1)h\right].
\]

Substitution into (2) cancels the \(\xi^2\) terms:

\[
h''-2\xi h'+(\varepsilon-1)h=0.
\tag{4}
\]

This is the Hermite differential equation once

\[
\varepsilon-1=2n
\]

for a nonnegative integer \(n\). [lancaster.ac](https://www.lancaster.ac.uk/staff/schomeru/lecturenotes/Quantum%20Mechanics/S6.html)

## 4. Why energy is quantized

Use a power series:

\[
h(\xi)=\sum_{k=0}^{\infty}a_k\xi^k.
\]

Substituting into (4) yields

\[
a_{k+2}
=
\frac{2k+1-\varepsilon}{(k+2)(k+1)}a_k.
\tag{5}
\]

The even coefficients evolve from \(a_0\); odd coefficients evolve from \(a_1\). If the recursion never terminates, \(h(\xi)\) grows asymptotically like \(e^{\xi^2}\). Equation (3) would then give

\[
\psi(\xi)\sim e^{+\xi^2/2},
\]

which cannot be normalized.

The recursion terminates at degree \(n\) only when its numerator vanishes:

\[
2n+1-\varepsilon=0.
\]

Hence

\[
\varepsilon=2n+1,
\qquad n=0,1,2,\ldots,
\]

and therefore

\[
\boxed{E_n=\hbar\omega\left(n+\frac12\right)}.
\]

The terminating polynomial is the physicists’ Hermite polynomial,

\[
H_n(\xi)
=
(-1)^n e^{\xi^2}
\frac{d^n}{d\xi^n}e^{-\xi^2}.
\]

The first few are

\[
H_0=1,\qquad
H_1=2\xi,\qquad
H_2=4\xi^2-2,\qquad
H_3=8\xi^3-12\xi.
\]

## 5. Normalize the eigenfunctions

The unnormalized solution is

\[
\psi_n(x)=C_n
H_n\left(\frac{x}{\ell}\right)
e^{-x^2/(2\ell^2)}.
\]

Using Hermite orthogonality,

\[
\int_{-\infty}^{\infty}
e^{-\xi^2}H_n(\xi)H_m(\xi)\,d\xi
=
\sqrt{\pi}\,2^n n!\,\delta_{nm},
\]

normalization fixes

\[
C_n
=
\frac{1}{\pi^{1/4}\sqrt{2^n n!\,\ell}}.
\]

Therefore the normalized stationary wavefunctions are

\[
\boxed{
\psi_n(x)
=
\frac{1}{\pi^{1/4}\sqrt{2^n n!\,\ell}}
H_n\left(\frac{x}{\ell}\right)
\exp\left(-\frac{x^2}{2\ell^2}\right)
},
\qquad
\ell=\sqrt{\frac{\hbar}{m\omega}}.
\]

Equivalently,

\[
\boxed{
\psi_n(x)
=
\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}
\frac{1}{\sqrt{2^n n!}}
H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right)
e^{-m\omega x^2/(2\hbar)}
}.
\]

This is the expression in your image. It gives a parity \((-1)^n\), has exactly \(n\) nodes, and corresponds to energy \(E_n=\hbar\omega(n+\tfrac12)\). [en.wikipedia](https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator)

## Time dependence

The preceding \(\psi_n(x)\) is the spatial energy eigenfunction. The full stationary solution is

\[
\boxed{
\Psi_n(x,t)
=
\psi_n(x)
e^{-iE_nt/\hbar}
=
\psi_n(x)e^{-i\omega(n+1/2)t}
}.
\]

Its probability density is time-independent:

\[
|\Psi_n(x,t)|^2=|\psi_n(x)|^2.
\]

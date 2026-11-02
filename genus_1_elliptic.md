
The genus-1 case repeats the same logical pattern as genus 0—**iterated integration of simple kernels**—but replaces rational kernels on the sphere with elliptic, doubly periodic kernels on a torus. The formal differential recursion is almost unchanged; the new difficulty is that the kernels depend on both a point on the torus and the torus’s shape parameter \(\tau\). [arxiv](https://arxiv.org/html/1712.07089v1)

## From sphere to torus

At genus 0, the underlying surface is the Riemann sphere \(\mathbb P^1\). The basic kernels are rational:

\[
\frac{dz}{z},\qquad \frac{dz}{1-z},\qquad \frac{dz}{z-a}.
\]

At genus 1, the surface is an elliptic curve

\[
E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),
\qquad \operatorname{Im}\tau>0.
\]

This means that two complex numbers represent the same point if they differ by an element of the lattice

\[
\Lambda_\tau=\mathbb Z+\tau\mathbb Z.
\]

Equivalently, you take the complex plane, draw the parallelogram with vertices \(0,1,1+\tau,\tau\), and glue opposite sides. The result is a torus. [arxiv](https://arxiv.org/html/1712.07089v1)

The parameter \(\tau\) is not just a coordinate; it records the **shape** of the torus. Changing \(\tau\) changes the elliptic curve, so genus-1 functions naturally depend on both:

- \(z\): a point on the torus;
- \(\tau\): the modular parameter describing the torus.

## Why rational kernels fail

On the sphere, \(dz/z\) has a simple pole at \(0\). On a torus, however, a nonconstant meromorphic function cannot have just one simple pole: the total number of zeros must equal the total number of poles, counted with multiplicity. This is a consequence of compactness.

So \(dz/z\) has no direct elliptic analogue. You need kernels that are doubly periodic and have the correct balance of poles. The fundamental generating object is the **Kronecker function**:

\[
F(z,\alpha;\tau)
=
\frac{\theta_1'(0,\tau)\theta_1(z+\alpha,\tau)}
{\theta_1(z,\tau)\theta_1(\alpha,\tau)}.
\]

Here \(\theta_1\) is a Jacobi theta function. The formula looks intimidating, but its role is simple: it is the elliptic replacement for the rational kernel \(1/(z-a)\). [arxiv](https://arxiv.org/html/2606.02744v1)

It has a Laurent expansion in the auxiliary variable \(\alpha\):

\[
F(z,\alpha;\tau)
=
\sum_{n=0}^{\infty}
g^{(n)}(z,\tau)\alpha^{n-1}.
\]

The coefficients

\[
g^{(n)}(z,\tau)
\]

are called **Kronecker–Eisenstein coefficients**. They are the basic integration kernels for elliptic polylogarithms. [arxiv](https://arxiv.org/html/2606.02744v1)

## The elliptic analogue of \(dz/z\)

At genus 0, the first logarithm is

\[
\log z=\int_0^z\frac{dt}{t}.
\]

At genus 1, the corresponding basic integral is

\[
\Gamma^{(n)}(z;\tau)
=
\int_0^z g^{(n)}(t,\tau)\,dt.
\]

For \(n=0\), this is essentially the logarithm on the torus:

\[
\Gamma^{(0)}(z;\tau)
=
\log\frac{\theta_1(z,\tau)}{\eta(\tau)}
\]

up to conventional normalization. Thus the elliptic logarithm is not simply \(\log z\); it is a theta-function expression that respects the periodicity of the torus. [arxiv](https://arxiv.org/html/1712.07089v1)

The differential equation is still first order:

\[
\frac{d}{dz}\Gamma^{(n)}(z;\tau)
=
g^{(n)}(z,\tau).
\]

So the genus-1 analogue of

\[
d\log z=\frac{dz}{z}
\]

is

\[
d\Gamma^{(n)}(z;\tau)
=
g^{(n)}(z,\tau)\,dz.
\]

## Building elliptic polylogarithms

Just as ordinary polylogarithms are built by repeated integration, elliptic polylogarithms are built by nested integration of the kernels \(g^{(n)}\).

For a word of indices \(I=(n_1,\ldots,n_r)\), define

\[
\widetilde\Gamma_I(z;\tau)
=
\int_0^z
g^{(n_1)}(t_1,\tau)\,dt_1
\int_0^{t_1}
g^{(n_2)}(t_2,\tau)\,dt_2
\cdots
\int_0^{t_{r-1}}
g^{(n_r)}(t_r,\tau)\,dt_r.
\]

For example,

\[
\widetilde\Gamma_{(n_1,n_2)}(z;\tau)
=
\int_0^z
g^{(n_1)}(t_1,\tau)
\left(
\int_0^{t_1}
g^{(n_2)}(t_2,\tau)\,dt_2
\right)
dt_1.
\]

This is the elliptic analogue of a multiple polylogarithm such as \(\operatorname{Li}_{2,1}(z)\). [arxiv](https://arxiv.org/pdf/1906.11857v2.pdf)

## The fundamental differential equation

Differentiating with respect to the endpoint \(z\) removes the first index:

\[
\boxed{
\frac{\partial}{\partial z}
\widetilde\Gamma_{(n_1,\ldots,n_r)}(z;\tau)
=
g^{(n_1)}(z,\tau)
\,
\widetilde\Gamma_{(n_2,\ldots,n_r)}(z;\tau).
}
\]

This is exactly parallel to the genus-0 formula

\[
\frac{d}{dz}G(a_1,\ldots,a_r;z)
=
\frac{1}{z-a_1}G(a_2,\ldots,a_r;z).
\]

The only difference is that the rational factor \(1/(z-a_1)\) is replaced by the elliptic kernel \(g^{(n_1)}(z,\tau)\). [arxiv](https://arxiv.org/html/1712.07089v1)

For example,

\[
\frac{\partial}{\partial z}
\widetilde\Gamma_{(n_1,n_2)}(z;\tau)
=
g^{(n_1)}(z,\tau)
\widetilde\Gamma_{(n_2)}(z;\tau),
\]

and

\[
\frac{\partial}{\partial z}
\widetilde\Gamma_{(n_2)}(z;\tau)
=
g^{(n_2)}(z,\tau).
\]

Thus a word of length \(r\) differentiates to a word of length \(r-1\), just as at genus 0.

## A concrete low-depth example

Start with the genus-0 dilogarithm:

\[
\operatorname{Li}_2(z)
=
\int_0^z
\frac{-\log(1-t)}{t}\,dt.
\]

Its derivative is

\[
\operatorname{Li}_2'(z)
=
\frac{-\log(1-z)}{z}.
\]

The elliptic analogue is

\[
\widetilde\Gamma_{(n_1,n_2)}(z;\tau)
=
\int_0^z
g^{(n_1)}(t,\tau)
\widetilde\Gamma_{(n_2)}(t;\tau)\,dt.
\]

Its derivative is

\[
\frac{d}{dz}
\widetilde\Gamma_{(n_1,n_2)}(z;\tau)
=
g^{(n_1)}(z,\tau)
\widetilde\Gamma_{(n_2)}(z;\tau).
\]

So the structural rule is:

\[
\text{elliptic polylogarithm}
\quad\longrightarrow\quad
\text{elliptic kernel}\times\text{shorter elliptic polylogarithm}.
\]

## The role of \(\tau\): modular dependence

At genus 0, the functions depend only on \(z\) and the positions of the poles \(a_i\). At genus 1, they also depend on \(\tau\). Therefore one must consider derivatives with respect to \(\tau\) as well.

The Kronecker coefficients satisfy a differential equation in \(\tau\). In a simplified schematic form,

\[
\frac{\partial}{\partial\tau}g^{(n)}(z,\tau)
=
\text{combination of other }g^{(m)}(z,\tau).
\]

More precisely, the full system couples \(z\)-derivatives and \(\tau\)-derivatives. This is the **elliptic KZB connection**, the genus-1 analogue of the KZ connection. [arxiv](https://arxiv.org/html/2010.05271v2)

At genus 0, the system is essentially:

\[
d\vec F=A(z)\vec F.
\]

At genus 1, it becomes:

\[
d\vec F=
\left(A_z(z,\tau)\,dz+A_\tau(z,\tau)\,d\tau\right)\vec F.
\]

The first term gives the elliptic polylogarithms as functions on the torus. The second term describes how they change when the torus itself is deformed. [arxiv](https://arxiv.org/html/2010.05271v2)

## Elliptic multiple zeta values

At genus 0, evaluating multiple polylogarithms at special points produces multiple zeta values:

\[
\zeta(s_1,\ldots,s_k)
=
\sum_{n_1>\cdots>n_k\ge1}
\frac{1}{n_1^{s_1}\cdots n_k^{s_k}}.
\]

At genus 1, evaluating elliptic polylogarithms along special cycles produces **elliptic multiple zeta values** (eMZVs).

One common \(A\)-cycle version is

\[
I^A(k_1,\ldots,k_r;\tau)
=
\int_{0<z_1<\cdots<z_r<1}
f^{(k_1)}(z_1;\tau)\,dz_1
\cdots
f^{(k_r)}(z_r;\tau)\,dz_r.
\]

These are elliptic analogues of multiple zeta values. They depend on \(\tau\), reflecting the shape of the torus. [www2.mathematik.hu-berlin](http://www2.mathematik.hu-berlin.de/publ/pre/2013/P-2018-02.pdf)

There are also \(B\)-cycle versions, obtained by integrating along the other fundamental cycle of the torus. The two cycles correspond to the two independent loops of the torus. [arxiv](https://arxiv.org/html/1509.08760v1)

## Iterated Eisenstein integrals

The \(\tau\)-dependence of elliptic multiple zeta values can be expressed using **iterated Eisenstein integrals**. Instead of integrating along a path on the torus, one integrates modular forms in the modular parameter \(\tau\):

\[
\omega(0;\tau)=d\tau,
\qquad
\omega(2k;\tau)=2\zeta(2k)\,d\tau,
\qquad
\omega(2k;\tau)=2\pi i\,G_{2k}(\tau)\,d\tau
\quad(k\ge2).
\]

Then one forms iterated integrals such as

\[
\int_0^\tau
\omega(2k_1;\tau_1)
\int_0^{\tau_1}
\omega(2k_2;\tau_2)
\cdots
\int_0^{\tau_{r-1}}
\omega(2k_r;\tau_r).
\]

These functions encode the modular dependence of elliptic multiple zeta values. [arxiv](https://arxiv.org/html/1507.02254v2)

So the genus-1 theory has two related integration directions:

| Direction | Integrated variable | Produces |
|---|---|---|
| Along the torus | \(z\) | Elliptic polylogarithms |
| Along moduli space | \(\tau\) | Iterated Eisenstein integrals |

## Shuffle and functional equations

At genus 0, products of iterated integrals obey the shuffle rule: multiplying two iterated integrals corresponds to summing over all ways of interleaving their integration steps.

The same principle holds for elliptic polylogarithms:

\[
\widetilde\Gamma_I(z;\tau)
\widetilde\Gamma_J(z;\tau)
=
\sum_{K\in I\shuffle J}
\widetilde\Gamma_K(z;\tau).
\]

Here \(I\shuffle J\) denotes all shuffles of the two words \(I\) and \(J\). This is the algebraic mechanism behind many identities among elliptic polylogarithms. [arxiv](https://arxiv.org/pdf/1906.11857v2.pdf)

There are also elliptic analogues of distribution, inversion, and Fay identities. Fay identities relate polylogarithms evaluated at different points on the elliptic curve and are essential for simplifying expressions and proving closure under integration. [arxiv](https://arxiv.org/pdf/1906.11857v2.pdf)

## Brown–Levin viewpoint

Brown and Levin formulated multiple elliptic polylogarithms using a flat connection. Instead of treating each \(\widetilde\Gamma_I\) separately, one packages all of them into a single generating series:

\[
\Gamma(z,\alpha;\tau)
=
\sum_I \widetilde\Gamma_I(z;\tau)\alpha^I.
\]

Then the differential recursion becomes a single equation:

\[
\frac{\partial}{\partial z}\Gamma(z,\alpha;\tau)
=
F(z,\alpha;\tau)\Gamma(z,\alpha;\tau),
\]

where \(F\) is the Kronecker generating kernel. This is the elliptic analogue of packaging all hyperlogarithms into one KZ-type differential equation. [arxiv](https://arxiv.org/html/2606.02744v1)

The advantage is structural: product rules, differential equations, and functional identities can be studied through the algebra of the connection rather than through separate formulas for each word.

## What is genuinely new at genus 1?

| Ingredient | Genus 0 | Genus 1 |
|---|---|---|
| Surface | Sphere | Torus |
| Basic kernel | \(dz/(z-a)\) | \(g^{(n)}(z,\tau)\,dz\) |
| Generating kernel | Hyperlogarithmic letters | Kronecker function \(F(z,\alpha;\tau)\) |
| Differential system | KZ | KZB |
| Extra variable | None | \(\tau\), the torus shape |
| Special constants | Multiple zeta values | Elliptic multiple zeta values |
| Modular forms | Not central | Central |
| Main symmetry | Möbius transformations | \(SL_2(\mathbb Z)\)-modular transformations |

The biggest conceptual novelty is that the elliptic theory is not merely a theory of functions on a fixed torus. It is also a theory of functions on the **moduli space of elliptic curves**—the space of possible torus shapes. [arxiv](https://arxiv.org/html/2010.05271v2)

## A beginner’s mental model

Think of genus 0 as integration on a straight line with a few marked singularities:

\[
0,\quad 1,\quad a_1,\quad a_2,\ldots
\]

Think of genus 1 as integration on a circle-like periodic world with two independent loops. You cannot use ordinary logarithms directly because the world closes up on itself. Instead, you use theta functions and Kronecker kernels, which automatically respect the periodicity.

The central formula remains:

\[
\boxed{
d\Gamma_{\text{long word}}
=
\text{elliptic kernel}\cdot\Gamma_{\text{shorter word}}.
}
\]

Everything else—shuffle relations, elliptic multiple zeta values, Eisenstein integrals, modular transformations, and the KZB connection—is built around this simple recursive principle. [arxiv](https://arxiv.org/html/1712.07089v1)

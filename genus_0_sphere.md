
The core idea is simple: **polylogarithms are built by repeatedly integrating simple differential forms, so their differential equations are algebraic and first order.** The difficulty increases with the “shape” of the surface on which one integrates: sphere (genus 0), torus (genus 1), and then general curved surfaces (higher genus). [hal](https://hal.science/hal-00416166/document)

## Start with logarithms

You already know that

\[
\log z=\int_1^z \frac{dt}{t}.
\]

This is a function obtained by integrating the differential form

\[
\omega_0=\frac{dt}{t}.
\]

The logarithm is the simplest **iterated integral**: it has only one integration step. Its differential equation is

\[
\frac{d}{dz}\log z=\frac1z.
\]

So the derivative is again an elementary algebraic expression. That is the pattern behind all polylogarithms.

## From logarithm to dilogarithm

The **dilogarithm** is defined by

\[
\operatorname{Li}_2(z)=\sum_{n=1}^{\infty}\frac{z^n}{n^2}.
\]

It also has an integral description:

\[
\operatorname{Li}_2(z)=\int_0^z \frac{-\log(1-t)}{t}\,dt.
\]

Therefore,

\[
\frac{d}{dz}\operatorname{Li}_2(z)
=
\frac{-\log(1-z)}{z}.
\]

The derivative of \(\operatorname{Li}_2\) involves \(\log\), and the derivative of \(\log\) involves \(1/z\). Iterating this gives the **trilogarithm**:

\[
\operatorname{Li}_3(z)=\int_0^z \frac{\operatorname{Li}_2(t)}{t}\,dt.
\]

In general,

\[
\operatorname{Li}_{n+1}(z)=\int_0^z \frac{\operatorname{Li}_n(t)}{t}\,dt.
\]

Thus each polylogarithm satisfies a first-order differential equation whose right-hand side is a lower polylogarithm. This is why the family is naturally described by a system of differential equations rather than one isolated equation. [hal](https://hal.science/hal-00416166/document)

## Multiple polylogarithms

A **multiple polylogarithm** is a nested version:

\[
\operatorname{Li}_{s_1,\ldots,s_k}(z)
=
\sum_{n_1>n_2>\cdots>n_k\ge1}
\frac{z^{n_1}}{n_1^{s_1}n_2^{s_2}\cdots n_k^{s_k}}.
\]

For example,

\[
\operatorname{Li}_{2,1}(z)
=
\sum_{n_1>n_2\ge1}
\frac{z^{n_1}}{n_1^2 n_2}.
\]

The same functions can be written as **iterated integrals**. Instead of integrating once, you integrate several times, with each inner integral using the previous result. [hal](https://hal.science/hal-00416166/document)

A compact notation is:

\[
G(a_1,\ldots,a_n;z)
=
\int_0^z
\frac{dt_1}{t_1-a_1}
\int_0^{t_1}
\frac{dt_2}{t_2-a_2}
\cdots
\int_0^{t_{n-1}}
\frac{dt_n}{t_n-a_n}.
\]

Think of each letter \(a_i\) as a “singularity” or pole of the integrand. For ordinary polylogarithms, the important letters are \(0\) and \(1\). [pos.sissa](https://pos.sissa.it/290/015/pdf)

## The genus 0 differential equation

At genus 0, the surface is the Riemann sphere \(\mathbb P^1(\mathbb C)\), essentially the complex plane plus a point at infinity. The differential forms are rational:

\[
\frac{dz}{z}, \qquad \frac{dz}{1-z}, \qquad \frac{dz}{z-a}.
\]

For a multiple polylogarithm \(G(a_1,\ldots,a_n;z)\), differentiation removes the first letter:

\[
\frac{d}{dz}G(a_1,\ldots,a_n;z)
=
\frac{1}{z-a_1}G(a_2,\ldots,a_n;z).
\]

So a word of length \(n\) differentiates to a word of length \(n-1\). Repeated differentiation eventually reaches the constant function \(1\). [pos.sissa](https://pos.sissa.it/290/015/pdf)

For example:

\[
\frac{d}{dz}G(0,1;z)
=
\frac{1}{z}G(1;z),
\]

and

\[
\frac{d}{dz}G(1;z)
=
\frac{1}{z-1}.
\]

This is an “algebraic formula” in the sense that the derivative is built from rational functions and shorter polylogarithms.

## Why this is called KZ

The system can be packaged using matrices. Let \(\vec F(z)\) collect all relevant polylogarithms. Then the differential equations have the form

\[
\frac{d\vec F}{dz}=A(z)\vec F(z),
\]

where \(A(z)\) is a matrix whose entries are rational functions such as \(1/z\) and \(1/(1-z)\). [ihes](https://www.ihes.fr/~vanhove/MotivesF/Matthes-9Decembre2020.pdf)

This is a special case of the **Knizhnik–Zamolodchikov (KZ) equation**, an important differential system in mathematics and physics. The solution is not usually a single elementary function; it is a **path-ordered exponential**:

\[
\vec F(z)=\mathcal P\exp\left(\int A(z)\,dz\right).
\]

For a first-year student, the key point is: **iterated integrals are the systematic way to solve differential equations where the derivative of one unknown function involves the previous unknown functions.** [ihes](https://www.ihes.fr/~vanhove/MotivesF/Matthes-9Decembre2020.pdf)

## A useful analogy

Imagine a chain of functions:

\[
1 \leftarrow \log z \leftarrow \operatorname{Li}_2(z)
\leftarrow \operatorname{Li}_3(z)\leftarrow \cdots
\]

Each arrow means “differentiate the function on the right to get the function on the left, multiplied by a simple rational factor.” Multiple polylogarithms generalize this from a single chain to a branching tree of words.

The algebraic structure is called the **shuffle product**. Roughly, it says that two iterated integrals can be multiplied by interleaving their integration steps in all possible ways. For example, at a formal level,

\[
\log x\log y
\]

can be expressed as a sum of iterated integrals corresponding to the two possible orders of integrating the two logarithmic forms. This shuffle rule is one reason multiple polylogarithms have so many functional identities. [hal](https://hal.science/hal-00416166/document)

## Moving to genus 1: the torus

A genus-1 Riemann surface is a torus. Algebraically, it can be described as

\[
E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),
\]

where \(\tau\) is a complex number with positive imaginary part. You identify points that differ by integers or by multiples of \(\tau\). Geometrically, this is a parallelogram with opposite sides glued together.

On a torus, you cannot use the simple rational forms

\[
\frac{dz}{z-a}
\]

in the same way, because the torus is compact and periodic. You need **elliptic differential forms**. The basic building block is the **Kronecker function**

\[
F(z,\alpha;\tau)
=
\sum_{n\in\mathbb Z}
\frac{e^{2\pi i nz}}{1-e^{2\pi i n\tau}e^{2\pi i\alpha}}.
\]

Its expansion in the auxiliary variable \(\alpha\) gives a family of kernels:

\[
F(z,\alpha;\tau)
=
\sum_{n\ge0} f^{(n)}(z;\tau)\alpha^n.
\]

These \(f^{(n)}\) are the elliptic analogues of the rational letters \(dz/(z-a)\). 

## Elliptic polylogarithms

An **elliptic polylogarithm** is an iterated integral on the torus using these elliptic kernels. Schematically,

\[
\Gamma_{I_1\cdots I_r}(x,y;p)
=
\int_y^x
\omega_{I_1}(t_1)
\int_y^{t_1}
\omega_{I_2}(t_2)
\cdots
\int_y^{t_{r-1}}
\omega_{I_r}(t_r).
\]

The differential equation has exactly the same shape as before:

\[
\frac{\partial}{\partial x}
\Gamma_{I_1\cdots I_r}(x,y;p)
=
\omega_{I_1}(x)
\Gamma_{I_2\cdots I_r}(x,y;p).
\]

The only change is that \(\omega_I(x)\) is now an elliptic kernel rather than a rational function. 

### What changes at genus 1?

| Feature | Genus 0 | Genus 1 |
|---|---|---|
| Underlying surface | Riemann sphere \(\mathbb P^1\) | Torus \(E_\tau\) |
| Basic kernels | \(dz/(z-a)\) | Kronecker/Eisenstein kernels |
| Differential system | KZ-type | KZB-type |
| Special constants | Multiple zeta values | Elliptic multiple zeta values |
| Extra symmetry | Möbius transformations | Modular transformations of \(\tau\) |

The extra parameter \(\tau\) records the shape of the torus. Changing \(\tau\) changes the torus, and the theory must respect transformations such as

\[
\tau\mapsto\frac{a\tau+b}{c\tau+d},
\qquad
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z).
\]

This is the origin of the word **modular** in this subject. 

## Brown–Levin and the modern elliptic theory

The modern theory of **multiple elliptic polylogarithms** was shaped especially by Francis Brown and Andrey Levin. They constructed these functions as iterated integrals associated with a flat connection, making the genus-1 theory closely parallel to the genus-0 theory. 

Later work by **Enriquez and Zerbini** clarified the function-theoretic and Lie-algebraic structure of elliptic hyperlogarithms: how to integrate them, when primitives exist, and how they behave under the natural symmetries of the elliptic curve. 

In physics, these functions appear in Feynman integrals and string amplitudes because many integrals naturally live on elliptic curves rather than on the complex line. 

## What “genus” means

The genus is a basic topological invariant of a surface:

\[
\text{genus} = \text{number of holes}.
\]

- Genus 0: sphere, no holes.
- Genus 1: torus, one hole.
- Genus 2: two-holed surface.
- Genus \(h\): \(h\)-holed surface.

For a first-year student, you can picture a genus-2 surface as a pretzel with two holes. The higher the genus, the more complicated the space of differential forms and the more complicated the symmetries.

## Beyond genus 1

For a genus-\(h\) Riemann surface \(\Sigma_h\), there are \(h\) independent holomorphic differential forms:

\[
\omega_1,\ldots,\omega_h.
\]

At genus 1, there is essentially one basic holomorphic differential, often written \(dx\). At genus 2, there are two. At genus \(h\), there are \(h\). This already makes the theory richer.

Recent constructions define higher-genus polylogarithms as iterated integrals of special kernels built from:

- Abelian differentials \(\omega_I\),
- Green’s functions, which generalize logarithmic potentials,
- Szegő kernels, which are higher-genus analogues of Cauchy kernels,
- modular tensors, which encode the transformation behavior under changes of the complex structure of the surface. [ihes](https://www.ihes.fr/~brown/ColombiaNotes7.pdf)

The differential recursion still looks formally familiar:

\[
\partial_x\Gamma_{I_1\cdots I_r}(x,y;p)
=
\omega_{I_1}(x)\Gamma_{I_2\cdots I_r}(x,y;p).
\]

But the kernels \(\omega_I\) are no longer simple rational or elliptic functions. They are sophisticated modular objects. [webusers.imj-prg](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Chandigarh.pdf)

## Why genus \(\ge2\) is harder

At genus 0, everything is controlled by rational functions. At genus 1, everything is controlled by elliptic functions and one modular parameter \(\tau\). At genus \(h\ge2\), several complications appear:

- There are \(h\) independent holomorphic differentials instead of one.
- The moduli space of surfaces has dimension \(3h-3\), so there are many possible shapes of the surface.
- The kernels depend on the choice of a **spin structure**, a refinement of the surface’s topology.
- Regularization is harder when integration endpoints collide.
- Functional equations become more complicated and are not yet fully classified.

This is why the higher-genus theory is active research rather than a settled textbook subject. [ihes](https://www.ihes.fr/~brown/ColombiaNotes7.pdf)

## The big picture

| Genus | Status | Main objects | Main differential system |
|---|---|---|---|
| 0 | Mature and complete | Classical and multiple polylogarithms | KZ / hyperlogarithmic equations |
| 1 | Well developed, still active | Elliptic multiple polylogarithms | KZB / elliptic iterated integrals |
| \(\ge2\) | Frontier | Higher-genus polylogarithms | Flat connections from modular tensors |

The unifying principle is:

\[
\boxed{
\text{polylogarithms are iterated integrals, and iterated integrals solve first-order differential systems.}
}
\]

At genus 0, the kernels are rational. At genus 1, they are elliptic. At higher genus, they are modular. The formal differential equation remains simple; the geometry and symmetry of the kernels become increasingly rich. 

## Minimal example to remember

For genus 0:

\[
\log z=\int_0^z\frac{dt}{t},
\qquad
\operatorname{Li}_2(z)=\int_0^z\frac{-\log(1-t)}{t}\,dt.
\]

For genus 1, replace \(dt/t\) by an elliptic kernel \(f^{(n)}(x-y;\tau)\,dx\). For genus \(h\), replace it by a higher-genus modular kernel. The recursion

\[
d(\text{long word})=
\text{simple kernel}\times d(\text{shorter word})
\]

is the central formula throughout. [hal](https://hal.science/hal-00416166/document)

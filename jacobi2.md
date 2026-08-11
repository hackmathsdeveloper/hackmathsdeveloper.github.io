
The **Abel–Jacobi theorem** connects meromorphic functions on an algebraic curve with periods of holomorphic differentials. The **Jacobi inversion problem** asks for the reverse construction: recover points on the curve from their Abelian integrals.

## Setup

Let \(X\) be a compact Riemann surface (smooth projective curve) of genus \(g\). Choose:

- a base point \(P_0\in X\);
- a basis \(\omega_1,\ldots,\omega_g\) of holomorphic \(1\)-forms;
- the period lattice \(\Lambda\subset\mathbb C^g\).

The associated **Jacobian** is the complex torus

\[
J(X)=\mathbb C^g/\Lambda.
\]

The Abel map of a point is

\[
A(P)=\left(\int_{P_0}^{P}\omega_1,\ldots,
\int_{P_0}^{P}\omega_g\right)\pmod{\Lambda}.
\]

The individual integrals depend on the path, but their class modulo periods does not. For a divisor \(D=\sum_i n_iP_i\), extend linearly:

\[
A(D)=\sum_i n_i A(P_i).
\]

## Abel’s theorem

For a degree-zero divisor \(D\),

\[
D=\operatorname{div}(f)
\quad\Longleftrightarrow\quad
A(D)=0\in J(X).
\]

In words: a degree-zero divisor is the zero-minus-pole divisor of a global meromorphic function exactly when its Abel–Jacobi image vanishes. Equivalently,

\[
\operatorname{Pic}^0(X)\cong J(X).
\]

More generally, two divisors \(D,E\) of the same degree are linearly equivalent precisely when their difference has trivial Abel–Jacobi image:

\[
D\sim E
\quad\Longleftrightarrow\quad
A(D)=A(E).
\]

This is the global compatibility condition for a desired pattern of zeros and poles. [en.wikipedia](https://en.wikipedia.org/wiki/Abel%E2%80%93Jacobi_map)

## Jacobi inversion

For \(g>1\), \(A:X\to J(X)\) cannot be inverted: \(X\) has complex dimension \(1\), while \(J(X)\) has dimension \(g\).

Instead, take \(g\) points and define the degree-\(g\) Abel map:

\[
A_g:\operatorname{Sym}^g(X)\longrightarrow J(X),
\qquad
(P_1,\ldots,P_g)\mapsto
\sum_{i=1}^{g} A(P_i).
\]

The **Jacobi inversion theorem** states that this map is surjective:

\[
\forall\,u\in J(X),\quad
\exists\,P_1,\ldots,P_g\in X
\quad\text{such that}\quad
u=\sum_{i=1}^g A(P_i).
\]

So every vector of \(g\) Abelian integrals, taken modulo the period lattice, can be inverted by finding a degree-\(g\) effective divisor \(D=P_1+\cdots+P_g\). [wstein](https://wstein.org/projects/kleinerman_99paper.pdf)

## Generic uniqueness

For a generic \(u\in J(X)\), its preimage under \(A_g\) is unique up to permutation of the \(P_i\). Thus,

\[
\operatorname{Sym}^g(X)\dashrightarrow J(X)
\]

is birational.

Non-uniqueness occurs at **special divisors**: divisors \(D\) for which there are unexpectedly many meromorphic functions with poles bounded by \(D\). Geometrically, these exceptional \(u\)'s lie on the theta divisor (after the appropriate translation). [arxiv](https://arxiv.org/pdf/2511.04229.pdf)

## Theta-function solution

Riemann theta functions give an explicit conceptual solution. Given \(u\in J(X)\), form a function of \(P\in X\), schematically

\[
P\longmapsto \theta\bigl(A(P)-u-K\bigr),
\]

where \(K\) is the vector of Riemann constants. For generic \(u\), this function has exactly \(g\) zeros (with multiplicity),

\[
P_1,\ldots,P_g,
\]

and those zeros solve the inversion problem:

\[
u=A(P_1)+\cdots+A(P_g).
\]

Thus **theta-function zeros are the higher-genus analogue of inverse elliptic functions**. [arxiv](https://arxiv.org/pdf/2511.04229.pdf)

## Genus-one example

If \(g=1\), then \(X\) itself is its Jacobian:

\[
J(X)\cong \mathbb C/\Lambda.
\]

The inversion problem becomes inversion of one elliptic integral,

\[
u=\int_{P_0}^{P}\frac{dx}{y}.
\]

Its inverse gives elliptic functions such as Jacobi’s \(\operatorname{sn}(u,k)\) or Weierstrass’s \(\wp(u)\). The general Jacobi inversion problem is the genus-\(g\) extension: one needs **\(g\) points** to invert **\(g\) coupled Abelian integrals**. [fse.studenttheses.ub.rug](https://fse.studenttheses.ub.rug.nl/20211/1/%5BbMath%5D_%5B2019%5D_%5BBerryLJ%5D.pdf)

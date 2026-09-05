
Galois theory is the study of **symmetries of polynomial roots**, expressed through field extensions and groups. Its central payoff is a precise criterion for when polynomial equations can be solved using arithmetic operations and radicals: a polynomial is solvable by radicals exactly when its Galois group is a solvable group. [math.mit](https://math.mit.edu/~dav/galois.pdf)

You cannot literally learn “everything” in one response, but this is a rigorous, end-to-end map of the subject—from prerequisites through the Fundamental Theorem, computations, solvability, finite fields, and modern directions.

## 1. The big idea

Given a polynomial \(f(x)\in K[x]\), adjoin all of its roots to the base field \(K\). This produces its **splitting field** \(L\). The automorphisms of \(L\) that fix \(K\) permute the roots of \(f\), without altering algebraic relationships that are visible over \(K\).

That automorphism group is the **Galois group**:

\[
\operatorname{Gal}(L/K)
=
\{\sigma:L\to L \mid \sigma \text{ is a field automorphism and } \sigma(a)=a\ \forall a\in K\}.
\]

So Galois theory translates:

| Field/polynomial side | Group side |
|---|---|
| Roots and expressions involving them | Permutations of the roots |
| Intermediate fields \(K\subseteq E\subseteq L\) | Subgroups of \(\operatorname{Gal}(L/K)\) |
| Normal intermediate extensions | Normal subgroups |
| Quotient extension symmetries | Quotient groups |
| Expressions by radicals | Solvable groups |

The original motivation was the classical problem: “When can the roots of a polynomial be written with \(+,-,\times,\div\), and \(n\)-th roots?” Galois theory proves that there is no universal formula by radicals for degree-five polynomials, unlike the quadratic, cubic, and quartic cases. [math.mit](https://math.mit.edu/~dav/galois.pdf)

***

## 2. Prerequisites

A standard rigorous treatment needs these foundations.

### Group theory

You should be comfortable with:

- Groups, subgroups, cosets, homomorphisms, kernels, quotient groups.
- Normal subgroups and conjugation.
- Cyclic groups, abelian groups, symmetric groups \(S_n\), alternating groups \(A_n\), dihedral groups \(D_n\).
- Group actions, orbits, stabilizers, and the orbit–stabilizer theorem.
- The correspondence theorem and isomorphism theorems.
- Composition series and solvable groups.

A finite group \(G\) is **solvable** if its derived series terminates at the identity:

\[
G^{(0)}=G,\qquad
G^{(i+1)}=[G^{(i)},G^{(i)}],
\]

and \(G^{(r)}=\{e\}\) for some \(r\).

Equivalently, \(G\) has a subnormal series whose successive quotients are abelian:

\[
\{e\}=G_0\triangleleft G_1\triangleleft \cdots\triangleleft G_r=G,
\qquad G_{i+1}/G_i\text{ abelian}.
\]

### Field theory

You need:

- Fields and field homomorphisms.
- Polynomial rings \(K[x]\).
- Irreducibility, factorization, gcds, and minimal polynomials.
- Vector spaces and dimensions.
- Field extensions \(L/K\).
- Extension degree \([L:K]=\dim_K L\).
- The tower law:

\[
[L:K]=[L:E][E:K]
\]

for \(K\subseteq E\subseteq L\).
- Algebraic and transcendental elements.
- Simple extensions \(K(\alpha)\).

For an algebraic element \(\alpha\) over \(K\),

\[
[K(\alpha):K]=\deg m_{\alpha,K}(x),
\]

where \(m_{\alpha,K}\) is the minimal polynomial of \(\alpha\) over \(K\).

***

## 3. Core field-extension concepts

### Algebraic extensions

An element \(\alpha\in L\) is **algebraic over \(K\)** if it satisfies some nonzero polynomial in \(K[x]\):

\[
f(\alpha)=0,\qquad f(x)\in K[x]\setminus\{0\}.
\]

The extension \(L/K\) is algebraic if every element of \(L\) is algebraic over \(K\).

Examples:

\[
\mathbb Q(\sqrt2)/\mathbb Q
\]

has degree \(2\), because \(\sqrt 2\) has minimal polynomial \(x^2-2\).

\[
\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2})/\mathbb Q
\]

has degree \(3\), because \(x^3-2\) is irreducible over \(\mathbb Q\).

### Splitting fields

A polynomial need not have all roots in the base field. Its **splitting field** is the smallest extension in which it factors fully into linear factors.

For example:

\[
f(x)=x^3-2.
\]

Its roots in \(\mathbb C\) are

\[
\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2},\qquad
\omega\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2},\qquad
\omega^2\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2},
\]

where

\[
\omega=e^{2\pi i/3},\qquad \omega^2+\omega+1=0.
\]

Its splitting field is

\[
L=\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2},\omega).
\]

It is not enough to adjoin \(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2}\): that only gives the real root. Adjoining \(\omega\) provides the remaining two roots.

### Normal extensions

An algebraic extension \(L/K\) is **normal** if every irreducible polynomial \(f\in K[x]\) that has one root in \(L\) splits completely in \(L[x]\).

For finite algebraic extensions, the following are equivalent:

- \(L/K\) is normal.
- \(L\) is the splitting field of a family of polynomials in \(K[x]\).
- Every \(K\)-embedding of \(L\) into an algebraic closure of \(K\) maps \(L\) onto itself.

Examples:

- \(\mathbb Q(\sqrt2)/\mathbb Q\) is normal, since \(x^2-2\) splits there.
- \(\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2)/\mathbb Q\) is not normal, since \(x^3-2\) has only one root in this real field.
- The splitting field \(\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2,\omega)/\mathbb Q\) is normal.

### Separable extensions

An irreducible polynomial is **separable** if it has no repeated roots in an algebraic closure. An algebraic extension is separable if every element has a separable minimal polynomial.

Over fields of characteristic \(0\), including \(\mathbb Q\), \(\mathbb R\), and \(\mathbb C\), every algebraic extension is separable.

In characteristic \(p>0\), inseparability can occur. For example, over

\[
K=\mathbb F_p(t),
\]

the polynomial

\[
x^p-t
\]

has derivative \(px^{p-1}=0\), so it is inseparable. In an algebraic closure it has the repeated-root form

\[
x^p-t=(x-\sqrt[p]{t})^p.
\]

### Galois extensions

A finite extension \(L/K\) is **Galois** precisely when it is both normal and separable. [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)

In characteristic \(0\), finite Galois extensions are simply finite normal extensions.

For a finite Galois extension:

\[
|\operatorname{Gal}(L/K)|=[L:K].
\]

More generally, for a finite extension,

\[
|\operatorname{Aut}_K(L)|\le [L:K],
\]

with equality exactly when the extension is Galois.

***

## 4. Galois groups and root permutations

Every \(\sigma\in\operatorname{Gal}(L/K)\) fixes \(K\) pointwise. Thus it fixes every coefficient of every polynomial in \(K[x]\).

If \(\alpha\) is a root of \(f(x)\in K[x]\), then:

\[
f(\sigma(\alpha))
=
\sigma(f(\alpha))
=
\sigma(0)
=
0.
\]

Therefore \(\sigma\) maps roots of \(f\) to other roots of \(f\). This gives a homomorphism:

\[
\operatorname{Gal}(f/K)
\hookrightarrow S_n,
\]

where \(n\) is the number of distinct roots of \(f\). [people.maths.ox.ac](https://people.maths.ox.ac.uk/rossler/mypage/pdf-files/GTnotesDR.pdf)

The Galois group is not merely an arbitrary permutation group: it consists of exactly the permutations consistent with every algebraic relation over \(K\).

### Example: \(x^2-2\)

The splitting field is

\[
L=\mathbb Q(\sqrt2).
\]

There are two \(\mathbb Q\)-automorphisms:

\[
\operatorname{id}(\sqrt2)=\sqrt2,
\qquad
\sigma(\sqrt2)=-\sqrt2.
\]

Hence

\[
\operatorname{Gal}(\mathbb Q(\sqrt2)/\mathbb Q)
\cong C_2.
\]

### Example: \(x^3-2\)

Let

\[
L=\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2,\omega).
\]

There are six automorphisms, determined by

\[
\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2\mapsto \omega^i\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2,
\qquad
\omega\mapsto \omega \text{ or } \omega^2.
\]

Thus

\[
\operatorname{Gal}(L/\mathbb Q)\cong S_3.
\]

The degree calculation is:

\[
[\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2):\mathbb Q]=3,
\]

and \(\omega\notin\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)2)\subset \mathbb R\), so

\[
[L:\mathbb Q]=2\cdot 3=6.
\]

Since \(S_3\) has order six, this identifies the Galois group.

***

## 5. Fundamental Theorem of Galois Theory

This is the central structural theorem.

Let \(L/K\) be a finite Galois extension, and let

\[
G=\operatorname{Gal}(L/K).
\]

There is an inclusion-reversing bijection:

\[
\left\{
\begin{array}{c}
\text{Intermediate fields } E\\
K\subseteq E\subseteq L
\end{array}
\right\}
\longleftrightarrow
\left\{
\begin{array}{c}
\text{Subgroups } H\\
H\le G
\end{array}
\right\}.
\]

The maps are:

\[
E\longmapsto \operatorname{Gal}(L/E),
\]

and

\[
H\longmapsto L^H
=
\{x\in L:\sigma(x)=x\ \forall \sigma\in H\}.
\]

Here \(L^H\) is called the **fixed field** of \(H\).

The inclusion reverses:

\[
E_1\subseteq E_2
\quad\Longleftrightarrow\quad
\operatorname{Gal}(L/E_2)\subseteq\operatorname{Gal}(L/E_1).
\]

For the corresponding pair \(E\leftrightarrow H\),

\[
[L:E]=|H|,
\qquad
[E:K]=[G:H].
\]

This correspondence is one of the most powerful translations in mathematics: questions about hidden subfields become questions about subgroups, and vice versa. [math.mit](https://math.mit.edu/~dav/galois.pdf)

### Normality and quotients

For an intermediate field \(E\),

\[
E/K\text{ is Galois}
\quad\Longleftrightarrow\quad
\operatorname{Gal}(L/E)\triangleleft G.
\]

When this holds,

\[
\operatorname{Gal}(E/K)
\cong
G/\operatorname{Gal}(L/E).
\]

So the usual group-theoretic quotient construction becomes a field-theoretic Galois group.

***

## 6. A complete small example

Consider

\[
L=\mathbb Q(\sqrt2,\sqrt3).
\]

The roots involved are \(\pm\sqrt2\) and \(\pm\sqrt3\). The independent sign changes give four automorphisms:

\[
\begin{aligned}
\operatorname{id}&:\sqrt2\mapsto\sqrt2,\quad \sqrt3\mapsto\sqrt3,\\
\sigma&:\sqrt2\mapsto-\sqrt2,\quad \sqrt3\mapsto\sqrt3,\\
\tau&:\sqrt2\mapsto\sqrt2,\quad \sqrt3\mapsto-\sqrt3,\\
\sigma\tau&:\sqrt2\mapsto-\sqrt2,\quad \sqrt3\mapsto-\sqrt3.
\end{aligned}
\]

Thus,

\[
\operatorname{Gal}(L/\mathbb Q)
\cong C_2\times C_2,
\]

the Klein four group \(V_4\).

The subgroup lattice is:

| Subgroup \(H\) | Fixed field \(L^H\) |
|---|---|
| \(\{1\}\) | \(\mathbb Q(\sqrt2,\sqrt3)\) |
| \(\langle \sigma\rangle\) | \(\mathbb Q(\sqrt3)\) |
| \(\langle \tau\rangle\) | \(\mathbb Q(\sqrt2)\) |
| \(\langle \sigma\tau\rangle\) | \(\mathbb Q(\sqrt6)\) |
| \(V_4\) | \(\mathbb Q\) |

For example, the fixed field of \(\langle\sigma\rangle\) is \(\mathbb Q(\sqrt3)\), because \(\sigma\) changes the sign of \(\sqrt2\) but leaves \(\sqrt3\) unchanged.

This is the Fundamental Theorem made concrete: the three order-two subgroups correspond exactly to the three quadratic intermediate fields.

***

## 7. Computing Galois groups

In practice, determining a Galois group is often a constrained inference problem: identify a subgroup of \(S_n\) compatible with irreducibility, discriminants, factorization patterns modulo primes, and resolvent polynomials.

### Step 1: Prove irreducibility

For \(f(x)\in\mathbb Q[x]\), common tools include:

- Rational Root Theorem.
- Eisenstein’s criterion.
- Reduction modulo a prime.
- Shifting the variable and applying Eisenstein.
- Modular factorization.

If \(f\) is irreducible of degree \(n\), then the Galois group acts transitively on its \(n\) roots.

### Step 2: Use the discriminant

For roots \(\alpha_1,\dots,\alpha_n\), the discriminant is

\[
\Delta(f)
=
\prod_{i<j}(\alpha_i-\alpha_j)^2.
\]

For an irreducible polynomial over \(\mathbb Q\):

\[
\Delta(f)\text{ is a square in }\mathbb Q
\quad\Longleftrightarrow\quad
\operatorname{Gal}(f/\mathbb Q)\subseteq A_n.
\]

This distinguishes, for example, \(A_n\) from \(S_n\) in many cases.

For a cubic

\[
f(x)=x^3+ax^2+bx+c,
\]

the discriminant is

\[
\Delta
=
a^2b^2-4b^3-4a^3c-27c^2+18abc.
\]

If an irreducible cubic has square discriminant, its Galois group is \(A_3\cong C_3\); otherwise it is \(S_3\).

### Step 3: Factor modulo unramified primes

For a prime \(p\) not dividing \(\Delta(f)\), the degrees of irreducible factors of \(f\bmod p\) determine a cycle type in the Galois group.

For degree five:

| Factorization modulo \(p\) | Cycle type in \(G\subseteq S_5\) |
|---|---|
| Irreducible degree 5 | A 5-cycle |
| \(2+3\) | A disjoint 2-cycle and 3-cycle |
| \(1+4\) | A 4-cycle |
| \(1+1+3\) | A 3-cycle |
| \(1+2+2\) | Two disjoint transpositions |
| Completely split | Identity |

This is a major computational technique, arising from the Frobenius–Dedekind relation between modular factorization and Frobenius conjugacy classes.

### Example: \(x^3-2\)

\[
f(x)=x^3-2
\]

is irreducible over \(\mathbb Q\) by Eisenstein at \(2\). Its discriminant is

\[
\Delta=-108=-2^2\cdot 3^3,
\]

which is not a square in \(\mathbb Q\). Therefore its Galois group is not contained in \(A_3\). Since an irreducible cubic has transitive Galois group, the possibilities are \(A_3\) or \(S_3\), so

\[
\operatorname{Gal}(x^3-2/\mathbb Q)\cong S_3.
\]

### Step 4: Resolvent polynomials

For degree four and degree five, **resolvents** encode particular root combinations. Their factorization can distinguish candidate transitive subgroups.

For quartics, a cubic resolvent helps distinguish groups such as:

\[
S_4,\quad A_4,\quad D_4,\quad V_4,\quad C_4.
\]

For quintics, resolvents and modular data can distinguish candidates such as:

\[
C_5,\quad D_5,\quad F_{20},\quad A_5,\quad S_5.
\]

Software is frequently useful here: SageMath, PARI/GP, Magma, GAP, and Mathematica can calculate or constrain Galois groups, but a mathematical proof usually follows the same structural logic.

***

## 8. Solvability by radicals

A polynomial is **solvable by radicals** over \(K\) if its roots lie in a field built from \(K\) through a tower

\[
K=K_0\subseteq K_1\subseteq\cdots\subseteq K_r
\]

where each step has the form

\[
K_{i+1}=K_i(\alpha_i),
\qquad
\alpha_i^{n_i}\in K_i.
\]

Informally, roots can be obtained through arithmetic and repeated extraction of \(n\)-th roots.

The central theorem is:

\[
\boxed{
f\text{ is solvable by radicals}
\iff
\operatorname{Gal}(f/K)\text{ is a solvable group}.
}
\]

This theorem is the original climax of classical Galois theory. [math.mit](https://math.mit.edu/~dav/galois.pdf)

### Why degrees 2, 3, and 4 work

Every subgroup of \(S_n\) is solvable for \(n\le4\). Therefore every polynomial of degree at most four over characteristic-zero fields is solvable by radicals.

That does not mean the formulas are pleasant. Cubic and quartic formulas are substantially more complicated than the quadratic formula, but they exist.

### Why the general quintic fails

For \(n\ge5\), \(S_n\) is not solvable. In particular:

\[
S_5
\]

is not solvable because it contains \(A_5\), and \(A_5\) is non-abelian simple.

A “generic” degree-five polynomial has Galois group \(S_5\), so no formula by radicals can solve all quintics.

The precise statement is not “quintics cannot be solved.” Many individual quintics are solvable by radicals. Rather:

> There is no formula using only coefficients, arithmetic, and radicals that solves every degree-five polynomial.

Examples of solvable quintics include certain cyclotomic polynomials, binomials such as \(x^5-a\) after adjoining suitable roots of unity, and quintics with cyclic or dihedral Galois groups.

***

## 9. Classical constructions

Galois theory gives clean impossibility proofs for ruler-and-compass problems.

A number is constructible from a unit segment using straightedge and compass exactly when it lies in a field obtained through a tower of quadratic extensions:

\[
\mathbb Q=K_0\subseteq K_1\subseteq\cdots\subseteq K_r,
\qquad [K_{i+1}:K_i]=2.
\]

Thus every constructible number has degree over \(\mathbb Q\) equal to a power of \(2\).

### Doubling the cube

To double a unit cube, one must construct

\[
\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2}.
\]

But

\[
[\mathbb Q(\sqrt [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf){2}):\mathbb Q]=3,
\]

and \(3\) is not a power of \(2\). Therefore it is impossible using only an unmarked straightedge and compass.

### Trisecting an arbitrary angle

Some angles can be trisected, but no universal straightedge-and-compass procedure can trisect every angle.

For example, trisecting \(60^\circ\) would require constructing \(20^\circ\). If

\[
x=2\cos(20^\circ),
\]

then the triple-angle identity gives

\[
x^3-3x-1=0.
\]

This cubic is irreducible over \(\mathbb Q\), so \(x\) has degree \(3\), not a power of \(2\). Thus \(20^\circ\) is not generally constructible.

### Regular polygons

A regular \(n\)-gon is constructible iff

\[
n=2^k p_1p_2\cdots p_r,
\]

where the \(p_i\) are distinct Fermat primes:

\[
p_i=2^{2^{m_i}}+1.
\]

This criterion comes from the cyclotomic field \(\mathbb Q(\zeta_n)\), whose Galois group is

\[
\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)
\cong
(\mathbb Z/n\mathbb Z)^\times.
\]

The 17-gon is constructible because \(17=2^{2^2}+1\) is a Fermat prime.

***

## 10. Cyclotomic fields

Let

\[
\zeta_n=e^{2\pi i/n}
\]

be a primitive \(n\)-th root of unity. The field

\[
\mathbb Q(\zeta_n)
\]

is the \(n\)-th **cyclotomic field**.

Its degree is Euler’s totient:

\[
[\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n).
\]

Its Galois group has a concrete description:

\[
\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)
\cong
(\mathbb Z/n\mathbb Z)^\times,
\]

with \(a\in(\mathbb Z/n\mathbb Z)^\times\) acting as

\[
\sigma_a(\zeta_n)=\zeta_n^a.
\]

Because \((\mathbb Z/n\mathbb Z)^\times\) is abelian, every cyclotomic extension is abelian and therefore solvable.

Example:

\[
\mathbb Q(\zeta_5)/\mathbb Q
\]

has degree

\[
\varphi(5)=4,
\]

and Galois group

\[
(\mathbb Z/5\mathbb Z)^\times\cong C_4.
\]

Cyclotomic fields connect Galois theory to roots of unity, constructible polygons, reciprocity laws, class field theory, Fourier analysis on finite groups, and modern algebraic number theory.

***

## 11. Finite-field Galois theory

Finite fields provide the cleanest and most explicit infinite family of Galois extensions.

For every prime power

\[
q=p^r,
\]

there is, up to isomorphism, exactly one finite field \(\mathbb F_q\) of order \(q\).

For every \(n\ge1\),

\[
\mathbb F_{q^n}/\mathbb F_q
\]

is a Galois extension of degree \(n\), and:

\[
\operatorname{Gal}(\mathbb F_{q^n}/\mathbb F_q)
\cong C_n.
\]

It is generated by the **Frobenius automorphism**:

\[
\operatorname{Frob}_q(x)=x^q.
\]

Its powers are

\[
x\mapsto x^{q^k},
\qquad k=0,\ldots,n-1.
\]

The fixed field of \(x\mapsto x^{q^d}\) is \(\mathbb F_{q^d}\) when \(d\mid n\).

This has major applied consequences:

- AES uses arithmetic in \(\mathbb F_{2^8}\).
- Reed–Solomon codes and many storage systems use finite-field algebra.
- Elliptic-curve and pairing-based cryptography operate over finite fields and extensions.
- The factorization of polynomials over finite fields drives algorithms in coding theory and cryptography.

***

## 12. Infinite Galois theory

For infinite algebraic Galois extensions, ordinary finite groups are replaced by **profinite groups**.

If \(L/K\) is an infinite Galois extension, then

\[
\operatorname{Gal}(L/K)
\]

is given the Krull topology and becomes a compact, totally disconnected Hausdorff topological group. It can be expressed as an inverse limit:

\[
\operatorname{Gal}(L/K)
\cong
\varprojlim_{E}
\operatorname{Gal}(E/K),
\]

where \(E\) ranges over finite Galois subextensions of \(L/K\).

The correspondence becomes:

| Object | Corresponding object |
|---|---|
| Intermediate fields \(K\subseteq E\subseteq L\) | Closed subgroups of \(\operatorname{Gal}(L/K)\) |
| Finite intermediate extensions \(E/K\) | Open subgroups |
| Galois intermediate extensions \(E/K\) | Closed normal subgroups |

The absolute Galois group of a field \(K\) is

\[
G_K=\operatorname{Gal}(K^{\mathrm{sep}}/K),
\]

where \(K^{\mathrm{sep}}\) is a separable closure.

This is a central object in number theory and arithmetic geometry. Studying \(G_{\mathbb Q}\), for example, packages profound information about all finite Galois extensions of \(\mathbb Q\), arithmetic of primes, Galois representations, and the arithmetic of algebraic varieties.

***

## 13. Connections to number theory

Galois theory becomes especially powerful over \(\mathbb Q\), number fields, local fields, and finite fields.

### Prime splitting

Let \(L/K\) be a number-field extension. A prime ideal \(\mathfrak p\) of \(K\) may factor in the ring of integers of \(L\) as

\[
\mathfrak p\mathcal O_L
=
\mathfrak P_1^{e_1}\cdots\mathfrak P_g^{e_g}.
\]

The Galois group controls how primes split, ramify, or remain inert.

For a finite Galois extension, the Galois group acts transitively on primes above a given unramified prime. The Frobenius element at a prime captures the arithmetic action

\[
x\mapsto x^{N\mathfrak p}
\]

on residue fields.

### Quadratic reciprocity

For \(d\) squarefree, the splitting of a prime \(p\) in

\[
\mathbb Q(\sqrt d)
\]

is governed by whether \(d\) is a quadratic residue modulo \(p\). The Legendre symbol and quadratic reciprocity can be understood as statements about Frobenius elements in quadratic Galois groups.

### Class field theory

Class field theory classifies abelian extensions of local and global fields. At a high level, it describes abelianized Galois groups:

\[
G_K^{\mathrm{ab}}
=
G_K/[G_K,G_K]
\]

in terms of arithmetic objects such as idele class groups.

Kronecker–Weber is an early landmark:

> Every finite abelian extension of \(\mathbb Q\) is contained in a cyclotomic field.

***

## 14. Connections to geometry and topology

Galois theory has a geometric analogue.

For a polynomial equation depending on parameters, roots may be viewed as sheets of a covering space. Moving parameters around loops can permute roots; this is **monodromy**. The resulting monodromy group often agrees with or closely reflects the Galois group.

In algebraic geometry:

- A finite field extension corresponds contravariantly to a finite dominant morphism of varieties.
- A finite Galois extension corresponds to a Galois cover.
- The étale fundamental group plays a role analogous to an absolute Galois group.
- Étale cohomology and Galois representations link geometry with arithmetic.

For a variety \(X\) over a field \(K\), the absolute Galois group \(G_K\) acts on geometric invariants of \(X\), including torsion points, étale cohomology, and fundamental groups. This is the language behind many deep results in modern arithmetic geometry.

***

## 15. Differential Galois theory

Classical Galois theory studies algebraic equations. **Differential Galois theory** studies linear differential equations.

For a linear differential equation such as

\[
y''+p(x)y'+q(x)y=0,
\]

one constructs a differential field extension containing all solutions and their derivatives. The differential Galois group consists of automorphisms preserving both the base differential field and differentiation.

It answers questions analogous to radical solvability:

- Can a differential equation be solved in elementary functions?
- Can solutions be expressed using exponentials, logarithms, algebraic functions, and integrals?
- What algebraic relations hold among solutions?

For linear differential equations, Liouvillian solvability is characterized by a solvable differential Galois group, paralleling the radical-solvability criterion in classical Galois theory.

***

## 16. Inverse Galois theory

The **inverse Galois problem** asks:

> Does every finite group occur as \(\operatorname{Gal}(L/\mathbb Q)\) for some finite Galois extension \(L/\mathbb Q\)?

This remains open in full generality.

Many families of finite groups are known to occur over \(\mathbb Q\), but no general construction is known for every finite group. The problem connects algebraic geometry, Hilbert irreducibility, modular forms, rigidity methods, and arithmetic statistics.

A related perspective is regular inverse Galois theory: construct a Galois extension of \(\mathbb Q(t)\) with prescribed finite Galois group, then specialize \(t\) to rational values.

***

## 17. A practical problem-solving workflow

For a polynomial \(f(x)\in\mathbb Q[x]\), a reusable workflow is:

1. **Factor over \(\mathbb Q\).**  
   Work on each irreducible factor separately where appropriate.

2. **Prove irreducibility.**  
   Use rational roots, Eisenstein, or modular reduction.

3. **Determine the degree and possible transitive subgroups.**  
   If \(f\) is irreducible of degree \(n\), then \(G\le S_n\) is transitive.

4. **Compute the discriminant.**  
   Determine whether \(G\subseteq A_n\).

5. **Factor modulo several primes not dividing the discriminant.**  
   Use factor-degree patterns to infer cycle types in \(G\).

6. **Eliminate candidate subgroups.**  
   Combine transitivity, parity, cycle types, and group orders.

7. **Use a resolvent if necessary.**  
   Especially useful for quartics and quintics.

8. **Construct the splitting field if needed.**  
   Adjoin roots and roots of unity in a degree-controlled tower.

9. **Apply the Fundamental Theorem.**  
   Translate intermediate-field questions into subgroup lattice questions.

10. **Test solvability.**  
    Determine whether the identified Galois group is solvable.

***

## 18. Common misconceptions

- “A degree-five polynomial cannot be solved.”  
  Incorrect. Some quintics are solvable; the general quintic is not solvable by radicals.

- “The Galois group is just any permutation group of roots.”  
  Incorrect. It contains only permutations induced by automorphisms fixing the base field.

- “A splitting field is always generated by one root.”  
  Not necessarily. A simple extension \(K(\alpha)\) may fail to contain all conjugate roots.

- “Normal means every element is fixed by automorphisms.”  
  No. Normality means conjugates of elements or roots remain within the field.

- “Every finite extension is Galois.”  
  No. It must be both normal and separable.

- “All degree-\(n\) extensions have Galois group of order \(n\).”  
  No. The equality \(|\operatorname{Gal}(L/K)|=[L:K]\) requires \(L/K\) to be Galois.

- “The Galois group depends only on the degree.”  
  No. Degree-five polynomials can have dramatically different groups: \(C_5\), \(D_5\), Frobenius groups, \(A_5\), \(S_5\), and others.

***

## 19. Suggested learning sequence

For a mathematically strong learner, this sequence is efficient.

1. **Review group actions and quotient groups.**
2. **Master algebraic extensions and minimal polynomials.**
3. **Study splitting fields, normality, and separability.**
4. **Compute elementary Galois groups** for quadratics, cubics, biquadratic fields, cyclotomic fields.
5. **Prove the Fundamental Theorem of Galois Theory.**
6. **Study solvable groups** and prove the radical-solvability theorem.
7. **Work through constructibility and regular polygons.**
8. **Learn finite-field Galois theory and Frobenius maps.**
9. **Study algebraic number theory:** rings of integers, primes, ramification, decomposition groups, Frobenius.
10. **Advance to profinite groups, absolute Galois groups, class field theory, and Galois representations.**

Useful sources from introductory to serious:

- MIT’s introductory notes emphasize roots of polynomials, radicals, and the fundamental theorem. [math.mit](https://math.mit.edu/~dav/galois.pdf)
- Purdue’s notes give a modern field-theoretic development and define a Galois extension as normal plus separable. [math.purdue](https://www.math.purdue.edu/~twooley/2024gt/2024GaloisTheory.pdf)
- Oxford lecture notes develop the relationship between root permutations, splitting fields, and field automorphisms. [people.maths.ox.ac](https://people.maths.ox.ac.uk/rossler/mypage/pdf-files/GTnotesDR.pdf)
- For an intuition-first entry, the NRICH introduction explains the “symmetries of roots” viewpoint and elementary examples. [nrich.maths](https://nrich.maths.org/articles/introduction-galois-theory)

## 20. Essential theorem checklist

A solid first-course command of Galois theory means being able to state and use:

\[
[K(\alpha):K]=\deg m_{\alpha,K}
\]

\[
[L:K]=[L:E][E:K]
\]

\[
L/K\text{ finite Galois}
\iff
L/K\text{ finite, normal, and separable}
\]

\[
|\operatorname{Gal}(L/K)|=[L:K]
\quad\text{for finite Galois }L/K
\]

\[
\operatorname{Gal}(L/K)
\longleftrightarrow
\{\text{intermediate fields}\}
\]

\[
E/K\text{ Galois}
\iff
\operatorname{Gal}(L/E)\triangleleft\operatorname{Gal}(L/K)
\]

\[
\operatorname{Gal}(E/K)
\cong
\operatorname{Gal}(L/K)/\operatorname{Gal}(L/E)
\]

\[
f\text{ solvable by radicals}
\iff
\operatorname{Gal}(f/K)\text{ solvable}
\]

\[
\operatorname{Gal}(\mathbb F_{q^n}/\mathbb F_q)
\cong C_n,
\qquad
x\mapsto x^q
\]

\[
\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)
\cong
(\mathbb Z/n\mathbb Z)^\times.
\]

The deepest enduring insight is that equations are not fundamentally classified by their formulas. They are classified by their symmetries. Galois theory turns those symmetries into a precise algebraic object, then lets group structure determine what can be constructed, solved, or understood.

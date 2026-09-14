https://www.perplexity.ai/search/4558a12b-9557-4511-917e-20841294e316

Below are complete solutions to Questions 1–10. Throughout, let  
\[
\omega=e^{2\pi i/3}=\frac{-1+i\sqrt3}{2},
\]
so \(\omega^3=1\), \(\omega\ne1\), and \(1+\omega+\omega^2=0\).

## 1. Splitting field of \(x^3-2\)

Let  
\[
f(x)=x^3-2.
\]
Its three complex roots are
\[
\alpha=\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\qquad \omega\alpha,\qquad \omega^2\alpha.
\]

Therefore the smallest field containing every root is
\[
L=\mathbb{Q}(\alpha,\omega)
 =\mathbb{Q}\left(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\omega\right).
\]

We now compute its degree.

First, \(x^3-2\) is irreducible over \(\mathbb{Q}\) by Eisenstein’s criterion at \(p=2\). Thus
\[
[\mathbb{Q}(\alpha):\mathbb{Q}]=3.
\]

The field \(\mathbb{Q}(\alpha)\) is contained in \(\mathbb{R}\), since \(\alpha\) is real and all rational expressions in \(\alpha\) are real. But \(\omega\notin\mathbb{R}\), so
\[
\omega\notin\mathbb{Q}(\alpha).
\]
Since \(\omega\) satisfies
\[
x^2+x+1=0,
\]
which is irreducible over every real subfield, we have
\[
[\mathbb{Q}(\alpha,\omega):\mathbb{Q}(\alpha)]=2.
\]

By the tower law,
\[
[L:\mathbb{Q}]
=
[L:\mathbb{Q}(\alpha)]
[\mathbb{Q}(\alpha):\mathbb{Q}]
=
2\cdot3
=
6.
\]

Hence the splitting field and degree are
\[
\boxed{L=\mathbb{Q}(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\omega),\qquad [L:\mathbb{Q}]=6.}
\]

The extension is Galois because it is the splitting field over \(\mathbb{Q}\) of the separable polynomial \(x^3-2\). In characteristic \(0\), all irreducible polynomials are separable. [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

## 2. Splitting field of \(x^4-2\)

Consider
\[
f(x)=x^4-2.
\]
Let
\[
\beta=\sqrt [core.ac](https://core.ac.uk/download/212814013.pdf){2}.
\]
The roots are
\[
\beta,\quad -\beta,\quad i\beta,\quad -i\beta.
\]

Thus the splitting field is
\[
L=\mathbb{Q}(\beta,i)
=
\mathbb{Q}(\sqrt [core.ac](https://core.ac.uk/download/212814013.pdf){2},i).
\]

The roots of unity needed are the fourth roots of unity:
\[
\mu_4=\{1,i,-1,-i\}.
\]
Only \(i\) needs to be adjoined, because \(1,-1\in\mathbb{Q}\).

To calculate the degree, apply Eisenstein’s criterion to
\[
x^4-2
\]
with \(p=2\). It is irreducible over \(\mathbb{Q}\), hence
\[
[\mathbb{Q}(\beta):\mathbb{Q}]=4.
\]

Since \(\mathbb{Q}(\beta)\subseteq \mathbb{R}\) and \(i\notin\mathbb{R}\),
\[
i\notin\mathbb{Q}(\beta).
\]
Also \(i\) has minimal polynomial \(x^2+1\) over \(\mathbb{Q}(\beta)\), so
\[
[\mathbb{Q}(\beta,i):\mathbb{Q}(\beta)]=2.
\]

Therefore,
\[
[L:\mathbb{Q}]=2\cdot4=8.
\]

So
\[
\boxed{
\operatorname{Spl}_{\mathbb{Q}}(x^4-2)
=
\mathbb{Q}(\sqrt [core.ac](https://core.ac.uk/download/212814013.pdf){2},i),
\qquad
[L:\mathbb{Q}]=8.
}
\]

The Galois group has order \(8\), and is isomorphic to the dihedral group \(D_4\), the symmetry group of a square. Indeed, an automorphism may rotate the roots by sending
\[
\beta\mapsto i\beta
\]
while fixing \(i\), and complex conjugation sends
\[
i\mapsto-i,\qquad \beta\mapsto\beta.
\]
These generate the standard dihedral relations. [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

## 3. Field extensions, normality, and Galois extensions

Let \(K\subseteq L\) be fields.

### Field extension

A **field extension** \(L/K\) means that \(K\) is a subfield of \(L\). Equivalently, \(L\) is a field containing \(K\), with the addition and multiplication operations on \(K\) inherited from \(L\).

Examples include
\[
\mathbb{Q}\subseteq\mathbb{Q}(\sqrt2),
\qquad
\mathbb{R}\subseteq\mathbb{C},
\qquad
\mathbb{Q}\subseteq\mathbb{Q}(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\omega).
\]

The degree of the extension,
\[
[L:K],
\]
is the dimension of \(L\) regarded as a vector space over \(K\).

For example,
\[
[\mathbb{Q}(\sqrt2):\mathbb{Q}]=2,
\]
because every element of \(\mathbb{Q}(\sqrt2)\) has the form
\[
a+b\sqrt2,\qquad a,b\in\mathbb{Q}.
\]

### Normal extension

An algebraic extension \(L/K\) is **normal** if every irreducible polynomial in \(K[x]\) that has one root in \(L\) splits completely into linear factors over \(L\).

Equivalently, if \(L/K\) is finite, then \(L/K\) is normal precisely when \(L\) is the splitting field over \(K\) of a collection of polynomials in \(K[x]\).

For example,
\[
\mathbb{Q}(\sqrt2)/\mathbb{Q}
\]
is normal because the minimal polynomial
\[
x^2-2
\]
has both roots \(\sqrt2\) and \(-\sqrt2\) inside \(\mathbb{Q}(\sqrt2)\).

By contrast,
\[
\mathbb{Q}(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2})/\mathbb{Q}
\]
is not normal. The polynomial \(x^3-2\) has the root \(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2}\) in this field, but the other roots
\[
\omega\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\qquad \omega^2\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2}
\]
are nonreal and therefore not in \(\mathbb{Q}(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2})\subseteq\mathbb{R}\).

### Galois extension

An algebraic extension \(L/K\) is **Galois** if it is both:

1. Normal over \(K\), and  
2. Separable over \(K\).

In characteristic \(0\), including extensions of \(\mathbb{Q}\), every algebraic extension is separable. Therefore, for finite extensions over \(\mathbb{Q}\),
\[
\text{Galois} \iff \text{normal}.
\]

For a finite Galois extension,
\[
|\operatorname{Gal}(L/K)|=[L:K].
\]
The group \(\operatorname{Gal}(L/K)\) is the group of all automorphisms of \(L\) that fix every element of \(K\). [ctnt-summer.math.uconn](https://ctnt-summer.math.uconn.edu/wp-content/uploads/sites/1632/2020/06/CTNT-InfGaloisTheory.pdf)

## 4. Fundamental Theorem of Galois Theory

Let \(L/K\) be a finite Galois extension and let
\[
G=\operatorname{Gal}(L/K).
\]

The Fundamental Theorem of Galois Theory states that there is an inclusion-reversing bijection
\[
\left\{
\text{intermediate fields }E:
K\subseteq E\subseteq L
\right\}
\longleftrightarrow
\left\{
\text{subgroups }H\le G
\right\}.
\]

The maps are:

\[
E\longmapsto \operatorname{Gal}(L/E),
\]
the subgroup of \(G\) fixing every element of \(E\), and

\[
H\longmapsto L^H,
\]
where
\[
L^H
=
\{x\in L:\sigma(x)=x\text{ for all }\sigma\in H\}
\]
is the fixed field of \(H\).

The correspondence reverses inclusion:
\[
E_1\subseteq E_2
\quad\Longleftrightarrow\quad
\operatorname{Gal}(L/E_2)
\subseteq
\operatorname{Gal}(L/E_1).
\]

The degree formulas are:
\[
[L:E]=|\operatorname{Gal}(L/E)|,
\]
and
\[
[E:K]=[G:\operatorname{Gal}(L/E)].
\]

A further key result is:
\[
E/K\text{ is Galois}
\quad\Longleftrightarrow\quad
\operatorname{Gal}(L/E)\trianglelefteq G.
\]
If this occurs, then
\[
\operatorname{Gal}(E/K)
\cong
G/\operatorname{Gal}(L/E).
\]

### Example

Take
\[
L=\mathbb{Q}(\sqrt2,\sqrt3).
\]
Its Galois group has four elements:
\[
G\cong C_2\times C_2.
\]
The three order-\(2\) subgroups correspond to the three quadratic intermediate fields:
\[
\mathbb{Q}(\sqrt2),\qquad
\mathbb{Q}(\sqrt3),\qquad
\mathbb{Q}(\sqrt6).
\]

Thus subgroups encode intermediate fields, and group-theoretic properties such as normality encode field-theoretic properties such as whether an intermediate extension is Galois. [ctnt-summer.math.uconn](https://ctnt-summer.math.uconn.edu/wp-content/uploads/sites/1632/2020/06/CTNT-InfGaloisTheory.pdf)

## 5. Action of \(\operatorname{Gal}(x^3-2/\mathbb{Q})\)

Let
\[
\alpha=\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},
\qquad
L=\mathbb{Q}(\alpha,\omega).
\]
The roots of \(x^3-2\) are
\[
\alpha,\qquad\omega\alpha,\qquad\omega^2\alpha.
\]

Every \(\mathbb{Q}\)-automorphism of \(L\) must send \(\alpha\) to another root of its minimal polynomial \(x^3-2\). Therefore,
\[
\sigma(\alpha)\in\{\alpha,\omega\alpha,\omega^2\alpha\}.
\]

Likewise, \(\omega\) must be sent to a root of
\[
x^2+x+1,
\]
so
\[
\sigma(\omega)\in\{\omega,\omega^2\}.
\]

Two useful automorphisms are:

\[
r:\quad
\alpha\mapsto\omega\alpha,\qquad
\omega\mapsto\omega,
\]
and
\[
c:\quad
\alpha\mapsto\alpha,\qquad
\omega\mapsto\omega^2.
\]

The map \(r\) cyclically permutes the roots:
\[
\alpha\mapsto\omega\alpha
\mapsto\omega^2\alpha
\mapsto\alpha.
\]
Thus, on the root set,
\[
r=(\alpha\ \omega\alpha\ \omega^2\alpha).
\]

The map \(c\) is complex conjugation. It fixes the real root \(\alpha\) and swaps the two nonreal roots:
\[
\omega\alpha\longleftrightarrow\omega^2\alpha.
\]
Hence
\[
c=(\omega\alpha\ \omega^2\alpha).
\]

The full set of automorphisms is
\[
\operatorname{Gal}(L/\mathbb{Q})
=
\{1,r,r^2,c,rc,r^2c\}.
\]

Their action gives every permutation of the three roots. In particular,

- \(r\) is a 3-cycle;
- \(c\) is a transposition;
- a 3-cycle and a transposition generate \(S_3\).

The relation
\[
crc=r^{-1}
\]
holds, which is the usual presentation
\[
S_3
=
\langle r,c\mid r^3=c^2=1,\ crc=r^{-1}\rangle.
\]

## 6. Prove \(\operatorname{Gal}(x^3-2/\mathbb{Q})\cong S_3\)

Let
\[
\alpha=\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\qquad
\omega=e^{2\pi i/3},
\]
and let
\[
L=\mathbb{Q}(\alpha,\omega)
\]
be the splitting field of \(x^3-2\).

From Question 1,
\[
[L:\mathbb{Q}]=6.
\]
Since \(L\) is the splitting field of a polynomial over characteristic \(0\), it is a finite Galois extension. Consequently,
\[
|\operatorname{Gal}(L/\mathbb{Q})|
=
[L:\mathbb{Q}]
=
6.
\]

Every automorphism permutes the three roots
\[
\{\alpha,\omega\alpha,\omega^2\alpha\}.
\]
This yields an injective homomorphism
\[
\operatorname{Gal}(L/\mathbb{Q})
\hookrightarrow S_3.
\]

Indeed, an automorphism is determined by what it does to \(\alpha\) and \(\omega\), and fixing all three roots fixes the field they generate, namely \(L\). Thus the action on roots is faithful.

But
\[
|\operatorname{Gal}(L/\mathbb{Q})|=6
\]
and
\[
|S_3|=6.
\]
An injective homomorphism between finite groups of equal order is an isomorphism. Therefore,
\[
\boxed{
\operatorname{Gal}(x^3-2/\mathbb{Q})
=
\operatorname{Gal}(L/\mathbb{Q})
\cong S_3.
}
\]

An alternative proof identifies explicit generators:
\[
r(\alpha)=\omega\alpha,\quad r(\omega)=\omega,
\]
and
\[
c(\alpha)=\alpha,\quad c(\omega)=\omega^2.
\]
The element \(r\) has order \(3\), \(c\) has order \(2\), and
\[
crc=r^{-1}.
\]
These are exactly the relations for the symmetric group \(S_3\). [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

## 7. \(\operatorname{Gal}(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q})\) and intermediate fields

Let
\[
L=\mathbb{Q}(\sqrt2,\sqrt3).
\]

Every element of \(L\) can be uniquely written as
\[
a+b\sqrt2+c\sqrt3+d\sqrt6,
\qquad
a,b,c,d\in\mathbb{Q}.
\]

Since \(\sqrt2\notin\mathbb{Q}\),
\[
[\mathbb{Q}(\sqrt2):\mathbb{Q}]=2.
\]
Also \(\sqrt3\notin\mathbb{Q}(\sqrt2)\). To see this, suppose
\[
\sqrt3=a+b\sqrt2
\]
for rationals \(a,b\). Squaring gives
\[
3=a^2+2b^2+2ab\sqrt2.
\]
The coefficient of \(\sqrt2\) must vanish, so \(2ab=0\). If \(a=0\), then \(3=2b^2\), impossible for \(b\in\mathbb{Q}\); if \(b=0\), then \(3=a^2\), also impossible for \(a\in\mathbb{Q}\). Thus \(\sqrt3\notin\mathbb{Q}(\sqrt2)\).

Hence
\[
[L:\mathbb{Q}]
=
[L:\mathbb{Q}(\sqrt2)]
[\mathbb{Q}(\sqrt2):\mathbb{Q}]
=
2\cdot2
=
4.
\]

The field \(L\) is the splitting field of
\[
(x^2-2)(x^2-3),
\]
so \(L/\mathbb{Q}\) is Galois.

An automorphism must send
\[
\sqrt2\mapsto\pm\sqrt2,
\qquad
\sqrt3\mapsto\pm\sqrt3,
\]
and the sign choices are independent. Thus there are four automorphisms:

\[
\begin{aligned}
1&:\sqrt2\mapsto\sqrt2,\quad \sqrt3\mapsto\sqrt3,\\
\sigma&:\sqrt2\mapsto-\sqrt2,\quad \sqrt3\mapsto\sqrt3,\\
\tau&:\sqrt2\mapsto\sqrt2,\quad \sqrt3\mapsto-\sqrt3,\\
\sigma\tau&:\sqrt2\mapsto-\sqrt2,\quad \sqrt3\mapsto-\sqrt3.
\end{aligned}
\]

Each nonidentity automorphism has order \(2\), and they commute. Therefore,
\[
\boxed{
\operatorname{Gal}(L/\mathbb{Q})
\cong C_2\times C_2,
}
\]
the Klein four-group.

### Intermediate fields

The subgroup lattice of \(C_2\times C_2\) contains:

- The trivial subgroup \(\{1\}\);
- Three subgroups of order \(2\);
- The entire group \(G\).

By the Galois correspondence, the intermediate fields are
\[
\boxed{
\mathbb{Q},\quad
\mathbb{Q}(\sqrt2),\quad
\mathbb{Q}(\sqrt3),\quad
\mathbb{Q}(\sqrt6),\quad
\mathbb{Q}(\sqrt2,\sqrt3).
}
\]

The correspondence is:

| Subgroup of \(G\) | Fixed field |
|---|---|
| \(G\) | \(\mathbb{Q}\) |
| \(\langle\sigma\rangle\) | \(\mathbb{Q}(\sqrt3)\) |
| \(\langle\tau\rangle\) | \(\mathbb{Q}(\sqrt2)\) |
| \(\langle\sigma\tau\rangle\) | \(\mathbb{Q}(\sqrt6)\) |
| \(\{1\}\) | \(\mathbb{Q}(\sqrt2,\sqrt3)\) |

For example, \(\sigma\tau\) changes the signs of both \(\sqrt2\) and \(\sqrt3\), but preserves their product:
\[
(\sigma\tau)(\sqrt6)
=
(\sigma\tau)(\sqrt2\sqrt3)
=
(-\sqrt2)(-\sqrt3)
=
\sqrt6.
\]
Hence its fixed field is \(\mathbb{Q}(\sqrt6)\). [ctnt-summer.math.uconn](https://ctnt-summer.math.uconn.edu/wp-content/uploads/sites/1632/2020/06/CTNT-InfGaloisTheory.pdf)

## 8. Automorphisms of \(\mathbb{Q}(\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\omega)\)

Let
\[
L=\mathbb{Q}(\alpha,\omega),
\qquad
\alpha=\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2}.
\]

We know
\[
\alpha^3=2,
\qquad
\omega^2+\omega+1=0.
\]

Any \(\mathbb{Q}\)-automorphism \(\sigma\) of \(L\) must send \(\alpha\) to a root of \(x^3-2\):
\[
\sigma(\alpha)\in\{\alpha,\omega\alpha,\omega^2\alpha\}.
\]

Likewise,
\[
\sigma(\omega)\in\{\omega,\omega^2\}.
\]

For each
\[
j\in\{0,1,2\}
\quad\text{and}\quad
\varepsilon\in\{1,2\},
\]
define
\[
\sigma_{j,\varepsilon}:
\begin{cases}
\alpha\mapsto \omega^j\alpha,\\
\omega\mapsto\omega^\varepsilon.
\end{cases}
\]

There are \(3\cdot2=6\) such maps. They are all automorphisms because they preserve the defining relations:
\[
(\omega^j\alpha)^3
=
\omega^{3j}\alpha^3
=
2,
\]
and
\[
(\omega^\varepsilon)^2+\omega^\varepsilon+1=0.
\]

Thus all six automorphisms are:

\[
\begin{array}{c|cc}
\text{Automorphism} & \alpha & \omega\\
\hline
1 & \alpha & \omega\\
r & \omega\alpha & \omega\\
r^2 & \omega^2\alpha & \omega\\
c & \alpha & \omega^2\\
rc & \omega\alpha & \omega^2\\
r^2c & \omega^2\alpha & \omega^2
\end{array}
\]

Here one may take
\[
r(\alpha)=\omega\alpha,\qquad r(\omega)=\omega,
\]
and
\[
c(\alpha)=\alpha,\qquad c(\omega)=\omega^2.
\]

Their relations are
\[
r^3=1,\qquad c^2=1,\qquad crc=r^{-1}.
\]

Therefore,
\[
\operatorname{Gal}(L/\mathbb{Q})
=
\{1,r,r^2,c,rc,r^2c\}
\cong S_3.
\]

A subtle point: the notation \(rc\) depends on the convention for composition. If multiplication means “apply the rightmost map first,” then
\[
(rc)(\alpha)
=
r(c(\alpha))
=
r(\alpha)
=
\omega\alpha,
\]
while
\[
(rc)(\omega)
=
r(c(\omega))
=
r(\omega^2)
=
\omega^2.
\]
The table above uses that convention. [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

## 9. Irreducibility implies transitivity

Let \(f(x)\in\mathbb{Q}[x]\) be irreducible, let \(L\) be its splitting field, and let
\[
G=\operatorname{Gal}(L/\mathbb{Q}).
\]
We prove that \(G\) acts transitively on the set of roots of \(f\).

Let \(\alpha\) and \(\beta\) be any two roots of \(f\). Since \(f\) is irreducible over \(\mathbb{Q}\), it is the minimal polynomial of both \(\alpha\) and \(\beta\) over \(\mathbb{Q}\).

There is a \(\mathbb{Q}\)-field isomorphism
\[
\varphi:\mathbb{Q}(\alpha)\to\mathbb{Q}(\beta)
\]
defined by
\[
\varphi(\alpha)=\beta.
\]

Why is it well-defined? Every element of \(\mathbb{Q}(\alpha)\) has the form \(g(\alpha)\) for some rational polynomial \(g\). Define
\[
\varphi(g(\alpha))=g(\beta).
\]
If
\[
g(\alpha)=h(\alpha),
\]
then
\[
(g-h)(\alpha)=0.
\]
Because \(f\) is the minimal polynomial of \(\alpha\), \(f\) divides \(g-h\). Since \(\beta\) is also a root of \(f\),
\[
(g-h)(\beta)=0,
\]
so
\[
g(\beta)=h(\beta).
\]
Thus the map is well-defined.

Since \(L\) is a normal extension of \(\mathbb{Q}\), every embedding of \(\mathbb{Q}(\alpha)\) into an algebraic closure of \(\mathbb{Q}\) extends to an automorphism of \(L\). Hence \(\varphi\) extends to some
\[
\sigma\in\operatorname{Gal}(L/\mathbb{Q})
\]
such that
\[
\sigma(\alpha)=\beta.
\]

Since \(\alpha\) and \(\beta\) were arbitrary roots, for every pair of roots there is a Galois automorphism mapping one to the other. Therefore the action is transitive:
\[
\boxed{
f\text{ irreducible over }\mathbb{Q}
\implies
\operatorname{Gal}(f/\mathbb{Q})
\text{ acts transitively on its roots.}
}
\]

### Example

The polynomial
\[
x^3-2
\]
is irreducible over \(\mathbb{Q}\), and its Galois group \(S_3\) acts transitively on
\[
\left\{
\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\,
\omega\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2},\,
\omega^2\sqrt [oeis](https://oeis.org/wiki/Algebraic_numbers){2}
\right\}.
\]

For comparison, the reducible polynomial
\[
(x^2-2)(x^2-3)
\]
has roots
\[
\pm\sqrt2,\qquad\pm\sqrt3.
\]
Its Galois group cannot send \(\sqrt2\) to \(\sqrt3\), because \(\sqrt2\) and \(\sqrt3\) have different minimal polynomials over \(\mathbb{Q}\). Its action has two separate orbits:
\[
\{\sqrt2,-\sqrt2\},
\qquad
\{\sqrt3,-\sqrt3\}.
\]

## 10. A reducible polynomial with nontrivial Galois group

Consider
\[
f(x)=(x^2-2)(x^2-3).
\]
This polynomial is reducible over \(\mathbb{Q}\), since it is already expressed as a product of two nonconstant polynomials in \(\mathbb{Q}[x]\).

Its roots are
\[
\sqrt2,\quad-\sqrt2,\quad\sqrt3,\quad-\sqrt3.
\]

Therefore its splitting field is
\[
L=\mathbb{Q}(\sqrt2,\sqrt3).
\]

As shown in Question 7,
\[
[L:\mathbb{Q}]=4
\]
and
\[
\operatorname{Gal}(L/\mathbb{Q})
\cong C_2\times C_2.
\]

The four automorphisms independently choose signs:
\[
\begin{aligned}
1&:\sqrt2\mapsto\sqrt2,\quad \sqrt3\mapsto\sqrt3,\\
\sigma&:\sqrt2\mapsto-\sqrt2,\quad \sqrt3\mapsto\sqrt3,\\
\tau&:\sqrt2\mapsto\sqrt2,\quad \sqrt3\mapsto-\sqrt3,\\
\sigma\tau&:\sqrt2\mapsto-\sqrt2,\quad \sqrt3\mapsto-\sqrt3.
\end{aligned}
\]

Thus
\[
\boxed{
f(x)=(x^2-2)(x^2-3)
\text{ is reducible over }\mathbb{Q},
\quad
\operatorname{Gal}(f/\mathbb{Q})
\cong C_2\times C_2\ne\{1\}.
}
\]

This shows that reducibility does not imply a trivial Galois group. Reducibility merely means the polynomial decomposes over the base field. A nontrivial Galois group arises whenever the factor roots still require a nontrivial field extension to obtain.

For a simpler degree-\(2\) example, one can use
\[
f(x)=x^2-2.
\]
It is irreducible, not reducible. So it does **not** answer this particular question. A reducible alternative is
\[
f(x)=(x-1)(x^2-2),
\]
whose splitting field is \(\mathbb{Q}(\sqrt2)\), with Galois group
\[
\operatorname{Gal}(\mathbb{Q}(\sqrt2)/\mathbb{Q})\cong C_2.
\]

The degree-\(4\) example \((x^2-2)(x^2-3)\) is more informative because it exhibits a noncyclic Galois group and several nontrivial intermediate fields. [ctnt-summer.math.uconn](https://ctnt-summer.math.uconn.edu/wp-content/uploads/sites/1632/2020/06/CTNT-InfGaloisTheory.pdf)

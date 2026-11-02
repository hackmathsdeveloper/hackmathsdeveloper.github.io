
The three exercises under the fundamental theorem were:

1. Find the subgroup and intermediate-field lattices for \(\mathbb Q(\sqrt2,\sqrt3)/\mathbb Q\).
2. Do the same for the splitting field of \(x^3-2\).
3. Identify which intermediate fields are Galois over \(\mathbb Q\).

The answers are: the first extension has three proper intermediate fields, all Galois over \(\mathbb Q\); the second has one quadratic and three cubic intermediate fields, of which only the quadratic field is Galois over \(\mathbb Q\). We will derive both using the **correspondence** between subgroups and fixed fields. [math.ucla](https://www.math.ucla.edu/~tsmits/Teaching/110C/Handouts/galcorr.pdf)

## The rule we will use

Let \(L/K\) be a finite Galois extension and \(G=\operatorname{Gal}(L/K)\). For \(H\leq G\), define
\[
L^H=\{x\in L:\sigma(x)=x\text{ for every }\sigma\in H\}.
\]

The fundamental theorem gives
\[
H\longleftrightarrow L^H,
\qquad
[L:L^H]=|H|,
\qquad
[L^H:K]=[G:H].
\]

Moreover,
\[
L^H/K\text{ is Galois}
\iff H\trianglelefteq G,
\]
and when this holds,
\[
\operatorname{Gal}(L^H/K)\cong G/H.
\]

Notice that larger subgroups fix smaller fields. This is why the two lattices are reversed. [en.wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory)

## Exercise 1: \(\mathbb Q(\sqrt2,\sqrt3)/\mathbb Q\)

### Step 1: Compute the degree

Set
\[
L=\mathbb Q(\sqrt2,\sqrt3).
\]

First,
\[
[\mathbb Q(\sqrt2):\mathbb Q]=2.
\]

We claim \(\sqrt3\notin\mathbb Q(\sqrt2)\). Otherwise, there would be \(a,b\in\mathbb Q\) such that
\[
\sqrt3=a+b\sqrt2.
\]
Squaring gives
\[
3=a^2+2b^2+2ab\sqrt2.
\]

Since \(1,\sqrt2\) are linearly independent over \(\mathbb Q\),
\[
ab=0,\qquad a^2+2b^2=3.
\]

- If \(b=0\), then \(a^2=3\), impossible for rational \(a\).
- If \(a=0\), then \(b^2=3/2\), also impossible for rational \(b\).

Thus adjoining \(\sqrt3\) gives another degree-two extension. By the tower law,
\[
[L:\mathbb Q]=2\cdot2=4.
\]

Consequently, every element of \(L\) has a unique expression
\[
u=a+b\sqrt2+c\sqrt3+d\sqrt6,
\qquad a,b,c,d\in\mathbb Q.
\]

Also, \(L\) is the splitting field of the separable polynomial
\[
(x^2-2)(x^2-3),
\]
so \(L/\mathbb Q\) is Galois. [math.ucla](https://www.math.ucla.edu/~tsmits/Teaching/110C/Handouts/galcorr.pdf)

### Step 2: Find the automorphisms

An automorphism fixing \(\mathbb Q\) must send each square root to a root of its own minimal polynomial:
\[
\sqrt2\mapsto\pm\sqrt2,\qquad
\sqrt3\mapsto\pm\sqrt3.
\]

The four independent sign choices give all four automorphisms. [math.hawaii](https://math.hawaii.edu/~tom/old_classes/413notes11.pdf)

Define \(s\) to change the sign of \(\sqrt2\), and \(t\) to change the sign of \(\sqrt3\):

| Automorphism | Image of \(\sqrt2\) | Image of \(\sqrt3\) | Image of \(\sqrt6\) |
|---|---|---|---|
| \(1\) | \(\sqrt2\) | \(\sqrt3\) | \(\sqrt6\) |
| \(s\) | \(-\sqrt2\) | \(\sqrt3\) | \(-\sqrt6\) |
| \(t\) | \(\sqrt2\) | \(-\sqrt3\) | \(-\sqrt6\) |
| \(st\) | \(-\sqrt2\) | \(-\sqrt3\) | \(\sqrt6\) |

They satisfy
\[
s^2=t^2=1,\qquad st=ts.
\]
Hence
\[
G=\{1,s,t,st\}\cong C_2\times C_2,
\]
the Klein four-group.

### Step 3: Compute the fixed fields explicitly

Take
\[
u=a+b\sqrt2+c\sqrt3+d\sqrt6.
\]

For \(s\),
\[
s(u)=a-b\sqrt2+c\sqrt3-d\sqrt6.
\]
Thus \(s(u)=u\) precisely when \(b=d=0\), giving
\[
L^{\langle s\rangle}=\mathbb Q(\sqrt3).
\]

Similarly,
\[
t(u)=a+b\sqrt2-c\sqrt3-d\sqrt6,
\]
so
\[
L^{\langle t\rangle}=\mathbb Q(\sqrt2).
\]

Finally,
\[
st(u)=a-b\sqrt2-c\sqrt3+d\sqrt6,
\]
so
\[
L^{\langle st\rangle}=\mathbb Q(\sqrt6).
\]

These are the three proper intermediate fields in the standard biquadratic correspondence. [en.wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory)

### Step 4: Write the complete correspondence

| Subgroup \(H\) | Order \(|H|\) | Fixed field \(L^H\) | Degree over \(\mathbb Q\) |
|---|---:|---|---:|
| \(\{1\}\) | 1 | \(L\) | 4 |
| \(\langle s\rangle\) | 2 | \(\mathbb Q(\sqrt3)\) | 2 |
| \(\langle t\rangle\) | 2 | \(\mathbb Q(\sqrt2)\) | 2 |
| \(\langle st\rangle\) | 2 | \(\mathbb Q(\sqrt6)\) | 2 |
| \(G\) | 4 | \(\mathbb Q\) | 1 |

The subgroup lattice is

```text
                 G = C₂ × C₂
                /     |     \
             <s>     <t>    <st>
                \     |     /
                     {1}
```

The field lattice is

```text
               L = Q(√2, √3)
                /     |     \
           Q(√3)   Q(√2)   Q(√6)
                \     |     /
                      Q
```

Every edge in these diagrams has index or field degree \(2\).

Why are there no other intermediate fields? Because the subgroup list is complete, and the Galois correspondence is a bijection. [en.wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory)

## Exercise 2: The splitting field of \(x^3-2\)

### Step 1: Construct the splitting field and compute its degree

Let
\[
\alpha=\sqrt [math.dartmouth](https://math.dartmouth.edu/~auel/courses/370s19/docs/syllabus.pdf){2}\in\mathbb R,
\qquad
\omega=e^{2\pi i/3}.
\]
Then
\[
\omega^3=1,\qquad 1+\omega+\omega^2=0,
\]
and the three roots of \(x^3-2\) are
\[
\alpha,\quad \alpha\omega,\quad \alpha\omega^2.
\]

Therefore its splitting field is
\[
L=\mathbb Q(\alpha,\omega).
\]

The polynomial \(x^3-2\) is irreducible by Eisenstein’s criterion at \(2\), so
\[
[\mathbb Q(\alpha):\mathbb Q]=3.
\]

Since \(\mathbb Q(\alpha)\subseteq\mathbb R\) but \(\omega\notin\mathbb R\), we have \(\omega\notin\mathbb Q(\alpha)\). Its polynomial \(x^2+x+1\) therefore remains irreducible over \(\mathbb Q(\alpha)\). Hence
\[
[L:\mathbb Q]=2\cdot3=6.
\]

As the splitting field of a separable cubic, \(L/\mathbb Q\) is Galois. Its group acts faithfully on the three roots, so it is a subgroup of \(S_3\); having order \(6\), it must be all of \(S_3\). [math.hawaii](https://math.hawaii.edu/~tom/old_classes/413notes11.pdf)

### Step 2: Describe its generators

Define
\[
r(\alpha)=\alpha\omega,\qquad r(\omega)=\omega,
\]
and let \(s\) be complex conjugation:
\[
s(\alpha)=\alpha,\qquad s(\omega)=\omega^2.
\]

Their actions on the roots are:

| Automorphism | Action on roots |
|---|---|
| \(r\) | \(\alpha\mapsto\alpha\omega\mapsto\alpha\omega^2\mapsto\alpha\) |
| \(s\) | Fixes \(\alpha\), exchanges \(\alpha\omega\) and \(\alpha\omega^2\) |

Thus \(r\) is a three-cycle and \(s\) is a transposition. They generate \(S_3\). [math.columbia](https://www.math.columbia.edu/~khovanov/ma2_fall/files/g2.pdf)

The relations are
\[
r^3=1,\qquad s^2=1,\qquad srs=r^{-1},
\]
and
\[
G=\{1,r,r^2,s,rs,r^2s\}.
\]

Here products mean composition with the rightmost map applied first: \(rs=r\circ s\).

### Step 3: List every subgroup

The complete subgroup list of \(S_3\) is
\[
\{1\},\quad
\langle s\rangle,\quad
\langle rs\rangle,\quad
\langle r^2s\rangle,\quad
\langle r\rangle=A_3,\quad
S_3.
\]

The three reflection subgroups have order \(2\), and \(A_3\) has order \(3\). Consequently, the corresponding proper intermediate fields consist of three cubic fields and one quadratic field. [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

### Step 4: Identify each fixed field

#### The subgroup \(\langle r\rangle\)

Since \(r\) fixes \(\omega\),
\[
\mathbb Q(\omega)\subseteq L^{\langle r\rangle}.
\]

But the correspondence gives
\[
[L^{\langle r\rangle}:\mathbb Q]
=\frac{6}{3}=2.
\]
Since \(\mathbb Q(\omega)\) already has degree \(2\),
\[
L^{\langle r\rangle}=\mathbb Q(\omega)
=\mathbb Q(\sqrt{-3}).
\]

#### The subgroup \(\langle s\rangle\)

Complex conjugation fixes \(\alpha\), so
\[
\mathbb Q(\alpha)\subseteq L^{\langle s\rangle}.
\]
Both fields have degree \(3\) over \(\mathbb Q\), hence
\[
L^{\langle s\rangle}=\mathbb Q(\alpha).
\]

#### The subgroup \(\langle rs\rangle\)

Compute
\[
(rs)(\alpha\omega^2)
=r\bigl(s(\alpha\omega^2)\bigr)
=r(\alpha\omega)
=\alpha\omega^2.
\]

Therefore \(rs\) fixes \(\alpha\omega^2\). This element has minimal polynomial \(x^3-2\), so its generated field has degree \(3\). Consequently,
\[
L^{\langle rs\rangle}=\mathbb Q(\alpha\omega^2).
\]

#### The subgroup \(\langle r^2s\rangle\)

Likewise,
\[
(r^2s)(\alpha\omega)
=r^2(\alpha\omega^2)
=\alpha\omega,
\]
giving
\[
L^{\langle r^2s\rangle}=\mathbb Q(\alpha\omega).
\]

Thus the four proper intermediate fields are exactly the familiar quadratic field and the three fields generated by individual cube roots of \(2\). [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

### Step 5: Write the complete correspondence

| Subgroup \(H\) | Order \(|H|\) | Fixed field \(L^H\) | Degree over \(\mathbb Q\) |
|---|---:|---|---:|
| \(\{1\}\) | 1 | \(L\) | 6 |
| \(\langle s\rangle\) | 2 | \(\mathbb Q(\alpha)\) | 3 |
| \(\langle rs\rangle\) | 2 | \(\mathbb Q(\alpha\omega^2)\) | 3 |
| \(\langle r^2s\rangle\) | 2 | \(\mathbb Q(\alpha\omega)\) | 3 |
| \(\langle r\rangle=A_3\) | 3 | \(\mathbb Q(\omega)\) | 2 |
| \(S_3\) | 6 | \(\mathbb Q\) | 1 |

The subgroup lattice is

```text
                         S₃
              /        /    \        \
            <s>      <rs>  <r²s>     <r>
              \        \    /        /
                         {1}
```

The corresponding field lattice is

```text
                     L = Q(α, ω)
             /          /    \          \
          Q(α)     Q(αω²)  Q(αω)       Q(ω)
             \          \    /          /
                           Q
```

All four middle fields are incomparable: none contains another.

The three cubic fields are distinct. If one cubic field contained two different roots of \(x^3-2\), their quotient would give \(\omega\) or \(\omega^2\). It would then contain all three roots and hence the degree-six splitting field, which is impossible for a degree-three field. [kconrad.math.uconn](https://kconrad.math.uconn.edu/blurbs/galoistheory/galoiscorrexamples.pdf)

## Exercise 3: Which intermediate fields are Galois over \(\mathbb Q\)?

### First extension: all three are Galois

For
\[
L_1=\mathbb Q(\sqrt2,\sqrt3),
\]
the group \(C_2\times C_2\) is abelian, so every subgroup is normal.

Therefore all three proper intermediate fields are Galois over \(\mathbb Q\):
\[
\mathbb Q(\sqrt2),\qquad
\mathbb Q(\sqrt3),\qquad
\mathbb Q(\sqrt6).
\]

Each has Galois group \(C_2\). Equivalently, each is the splitting field of its respective separable quadratic polynomial. [en.wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory)

### Second extension: only the quadratic intermediate field is Galois

For
\[
L_2=\mathbb Q(\alpha,\omega),
\]
the proper nontrivial normal subgroup of \(S_3\) is
\[
A_3=\langle r\rangle.
\]

Thus the only proper intermediate field Galois over \(\mathbb Q\) is
\[
\mathbb Q(\omega)=\mathbb Q(\sqrt{-3}),
\]
with
\[
\operatorname{Gal}(\mathbb Q(\omega)/\mathbb Q)
\cong S_3/A_3
\cong C_2.
\]

The three cubic fields correspond to nonnormal order-two subgroups, so none is Galois over \(\mathbb Q\). [maths.tcd](https://www.maths.tcd.ie/~mascotn/teaching/2021/MAU34101/2%20Corr.pdf)

You can also see their failure of normality directly: each contains one root of the irreducible polynomial \(x^3-2\), but not all three.

### Final classification

| Ambient extension | Proper intermediate field | Galois over \(\mathbb Q\)? | Galois group if yes |
|---|---|---|---|
| \(\mathbb Q(\sqrt2,\sqrt3)\) | \(\mathbb Q(\sqrt2)\) | Yes | \(C_2\) |
| Same | \(\mathbb Q(\sqrt3)\) | Yes | \(C_2\) |
| Same | \(\mathbb Q(\sqrt6)\) | Yes | \(C_2\) |
| \(\mathbb Q(\alpha,\omega)\) | \(\mathbb Q(\omega)\) | Yes | \(C_2\) |
| Same | \(\mathbb Q(\alpha)\) | No | — |
| Same | \(\mathbb Q(\alpha\omega)\) | No | — |
| Same | \(\mathbb Q(\alpha\omega^2)\) | No | — |

These classifications follow from the normal-subgroup criterion above. The base field \(\mathbb Q\) and the full splitting fields are also Galois over \(\mathbb Q\), but are not counted as proper intermediate fields. [maths.tcd](https://www.maths.tcd.ie/~mascotn/teaching/2021/MAU34101/2%20Corr.pdf)

One important distinction: even when an intermediate field \(E/\mathbb Q\) is not Galois, the extension \(L/E\) is Galois, with group equal to its corresponding subgroup. For example,
\[
\operatorname{Gal}(L_2/\mathbb Q(\alpha))
=\langle s\rangle\cong C_2,
\]
although \(\mathbb Q(\alpha)/\mathbb Q\) is not Galois. [maths.tcd](https://www.maths.tcd.ie/~mascotn/teaching/2021/MAU34101/2%20Corr.pdf)


Yes. The table in your image is actually giving a very strong hint about the **Galois group and splitting field** of

$$
f(x)=x^5+10x^3+20x-4.
$$

There is a beautiful way to solve this polynomial that makes the entire Galois-theoretic structure almost fall out automatically.

---

# 1. First: what is a splitting field?

Let

$$
f(x)\in \mathbb Q[x].
$$

A **splitting field** of \(f\) over \(\mathbb Q\) is the smallest field \(K\supseteq\mathbb Q\) in which \(f(x)\) factors completely into linear factors:

$$
f(x)=(x-\alpha_1)(x-\alpha_2)\cdots(x-\alpha_n),
\qquad \alpha_i\in K.
$$

So there are two requirements:

1. \(K\) contains **all roots** of \(f\).
2. \(K\) contains nothing unnecessary: it is the smallest such field.

For example,

$$
x^2-2=0
$$

has roots

$$
\pm\sqrt2.
$$

Therefore its splitting field over \(\mathbb Q\) is

$$
\boxed{\mathbb Q(\sqrt2)}.
$$

For

$$
x^2+1=0,
$$

the roots are \(i,-i\), so the splitting field is

$$
\boxed{\mathbb Q(i)}.
$$

For our degree-5 polynomial, the interesting question is:

$$
\boxed{\text{What field contains all five roots?}}
$$

---

# 2. The remarkable structure of this polynomial

Look at

$$
x^5+10x^3+20x.
$$

This is not an arbitrary quintic. It is a **Dickson polynomial**:

$$
D_5(x,a)=x^5-5ax^3+5a^2x.
$$

Put

$$
a=-2.
$$

Then

$$
D_5(x,-2)
=x^5+10x^3+20x.
$$

Hence

$$
f(x)=D_5(x,-2)-4.
$$

The key identity for Dickson polynomials is

$$
D_5\left(u+\frac au,a\right)
=
u^5+\frac{a^5}{u^5}.
$$

With \(a=-2\), put

$$
x=u-\frac2u.
$$

Then

$$
\boxed{
x^5+10x^3+20x
=
u^5-\frac{32}{u^5}.
}
$$

This is the crucial substitution.

---

# 3. Transform the quintic into a quadratic

Our equation is

$$
x^5+10x^3+20x-4=0.
$$

Set

$$
x=u-\frac2u.
$$

Then

$$
u^5-\frac{32}{u^5}-4=0.
$$

Multiply by \(u^5\):

$$
u^{10}-4u^5-32=0.
$$

Let

$$
y=u^5.
$$

Then

$$
y^2-4y-32=0.
$$

Factor:

$$
(y-8)(y+4)=0.
$$

Therefore

$$
u^5=8
\qquad\text{or}\qquad
u^5=-4.
$$

This is an enormous simplification.

---

# 4. Why do ten \(u\)'s give only five \(x\)'s?

At first it looks as though we have ten possibilities:

$$
u^5=8
$$

gives five \(u\)'s, and

$$
u^5=-4
$$

gives another five.

But notice that

$$
x=u-\frac2u
$$

is unchanged under

$$
u\longmapsto-\frac2u.
$$

Indeed,

$$
-\frac2u-\frac2{-2/u}
=
-\frac2u+u
=
u-\frac2u.
$$

And

$$
\left(-\frac2u\right)^5
=
-\frac{32}{u^5}.
$$

Thus

$$
u^5=8
\quad\Longrightarrow\quad
\left(-\frac2u\right)^5=-4.
$$

So the ten \(u\)'s pair up to give exactly **five roots of the quintic**.

---

# 5. Write the roots explicitly

Let

$$
b=2^{1/5}
$$

and let

$$
\zeta=\zeta_5=e^{2\pi i/5}
$$

be a primitive fifth root of unity.

Since

$$
b^5=2,
$$

we have

$$
b^3=2^{3/5},
\qquad
b^2=2^{2/5}.
$$

The five solutions of

$$
u^5=8
$$

are

$$
u_k=2^{3/5}\zeta^k=b^3\zeta^k,
\qquad k=0,1,2,3,4.
$$

Therefore

$$
x_k
=
u_k-\frac2{u_k}.
$$

Since

$$
\frac2{b^3}=\frac{b^5}{b^3}=b^2,
$$

we obtain

$$
\boxed{
x_k=b^3\zeta^k-b^2\zeta^{-k}
}
$$

or equivalently

$$
\boxed{
x_k=
2^{3/5}\zeta^k-2^{2/5}\zeta^{-k},
\qquad k=0,\ldots,4.
}
$$

These are the five roots.

So all roots lie in

$$
\boxed{\mathbb Q(2^{1/5},\zeta_5)}.
$$

This immediately gives us a candidate for the splitting field.

---

# 6. Therefore the splitting field is

Define

$$
K=\mathbb Q(2^{1/5},\zeta_5).
$$

We have just shown that every root belongs to \(K\).

Hence the splitting field \(L\) satisfies

$$
L\subseteq K.
$$

In fact,

$$
\boxed{
L=K=\mathbb Q(2^{1/5},\zeta_5).
}
$$

Let's understand why this is true and, more importantly, why its degree is **20**.

---

# 7. Degree of \(\mathbb Q(2^{1/5})\)

Consider

$$
g(x)=x^5-2.
$$

It is Eisenstein at \(2\):

* leading coefficient is 1;
* every other coefficient is divisible by 2;
* the constant term \(-2\) is not divisible by \(4\).

Therefore \(x^5-2\) is irreducible over \(\mathbb Q\).

Thus

$$
[\mathbb Q(2^{1/5}):\mathbb Q]=5.
$$

Let

$$
b=2^{1/5}.
$$

Then

$$
[\mathbb Q(b):\mathbb Q]=5.
$$

---

# 8. Degree of the cyclotomic field

For a primitive fifth root of unity,

$$
\zeta=\zeta_5,
$$

the cyclotomic polynomial is

$$
\Phi_5(x)=x^4+x^3+x^2+x+1.
$$

Therefore

$$
[\mathbb Q(\zeta_5):\mathbb Q]
=
\phi(5)
=
4.
$$

So we have fields of degrees

$$
5
\quad\text{and}\quad
4.
$$

Their compositum has degree

$$
[K:\mathbb Q]=20.
$$

More formally,

$$
[\mathbb Q(b,\zeta):\mathbb Q]
=
[\mathbb Q(b,\zeta):\mathbb Q(\zeta)]
[\mathbb Q(\zeta):\mathbb Q].
$$

Because \(5\) and \(4\) are coprime, the degree-5 and degree-4 extensions have trivial intersection:

$$
\mathbb Q(b)\cap\mathbb Q(\zeta)=\mathbb Q.
$$

Consequently,

$$
\boxed{
[K:\mathbb Q]=5\cdot4=20.
}
$$

---

# 9. Why is the Galois group of order 20?

Now the really interesting part begins.

We have

$$
K=\mathbb Q(b,\zeta),
$$

where

$$
b^5=2,
\qquad
\zeta^5=1.
$$

There are two fundamental automorphisms.

## Automorphism 1: rotate \(b\)

Define

$$
\sigma(b)=\zeta b,
\qquad
\sigma(\zeta)=\zeta.
$$

Since

$$
(\zeta b)^5=\zeta^5b^5=2,
$$

this is a legitimate automorphism.

Applying it five times gives

$$
\sigma^5=1.
$$

Thus

$$
\boxed{\sigma\text{ has order }5.}
$$

---

## Automorphism 2: rotate the fifth roots of unity

Define

$$
\tau(b)=b,
\qquad
\tau(\zeta)=\zeta^2.
$$

Since \(2\) is a primitive element of

$$
(\mathbb Z/5\mathbb Z)^\times,
$$

we have

$$
2^4\equiv1\pmod5.
$$

Thus

$$
\tau^4=1.
$$

So

$$
\boxed{\tau\text{ has order }4.}
$$

Therefore we already have

$$
C_5
\quad\text{and}\quad
C_4.
$$

But they do not commute.

Calculate:

$$
\tau\sigma\tau^{-1}(b).
$$

Since \(\tau^{-1}(b)=b\),

$$
\sigma(b)=\zeta b,
$$

and then

$$
\tau(\zeta b)=\zeta^2b.
$$

But

$$
\sigma^2(b)=\zeta^2b.
$$

Therefore

$$
\boxed{
\tau\sigma\tau^{-1}=\sigma^2.
}
$$

So

$$
\boxed{
\operatorname{Gal}(K/\mathbb Q)
\cong C_5\rtimes C_4.
}
$$

Its order is

$$
5\cdot4=20.
$$

This group is also called the **Frobenius group of order 20**:

$$
\boxed{F_{20}\cong \operatorname{AGL}(1,5).}
$$

---

# 10. How does this group act on the five roots?

This explains your table directly.

Recall

$$
x_k=b^3\zeta^k-b^2\zeta^{-k}.
$$

Apply \(\sigma\):

$$
b\mapsto\zeta b,
\qquad
\zeta\mapsto\zeta.
$$

Therefore

$$
b^3\mapsto\zeta^3b^3
$$

and

$$
b^2\mapsto\zeta^2b^2.
$$

Hence

$$
\sigma(x_k)
=
b^3\zeta^{k+3}
-
b^2\zeta^{2-k}.
$$

But

$$
-(k+3)\equiv2-k\pmod5.
$$

Therefore

$$
\boxed{\sigma(x_k)=x_{k+3}.}
$$

So \(\sigma\) acts on the five roots as a 5-cycle:

$$
(0\,3\,1\,4\,2).
$$

In cycle-type notation:

$$
\boxed{(5)}.
$$

---

Now apply \(\tau\):

$$
b\mapsto b,
\qquad
\zeta\mapsto\zeta^2.
$$

Thus

$$
\tau(x_k)
=
b^3\zeta^{2k}
-
b^2\zeta^{-2k}
=
x_{2k}.
$$

So

$$
k\mapsto2k\pmod5.
$$

The permutation is

$$
0\mapsto0,
$$

and

$$
1\to2\to4\to3\to1.
$$

Therefore

$$
\boxed{
\tau=(1\,2\,4\,3)(0)
}
$$

which has cycle type

$$
\boxed{(1,4)}.
$$

And

$$
\tau^2:k\mapsto4k
$$

gives

$$
(0)(1\,4)(2\,3),
$$

which has cycle type

$$
\boxed{(1,2,2)}.
$$

So the four cycle types in your image are exactly the cycle types occurring in this Galois group:

$$
\boxed{
(1,1,1,1,1),\quad
(1,2,2),\quad
(1,4),\quad
(5).
}
$$

---

# 11. Now the table in your image makes sense

The group has 20 elements.

Let's count them.

### Identity

There is exactly one:

$$
1.
$$

Cycle type:

$$
(1,1,1,1,1).
$$

Expected proportion:

$$
\frac1{20}=5\%.
$$

The table gives

$$
96/2000=4.8\%.
$$

Excellent agreement.

---

### Elements of order 2

There are 5.

They have cycle type

$$
(1,2,2).
$$

Expected proportion:

$$
\frac5{20}=25\%.
$$

Table:

$$
489/2000=24.45\%.
$$

Again, extremely close.

---

### Elements of order 4

There are 10.

They have cycle type

$$
(1,4).
$$

Expected proportion:

$$
\frac{10}{20}=50\%.
$$

Table:

$$
1015/2000=50.75\%.
$$

Again, very close.

---

### Elements of order 5

There are 4.

They have cycle type

$$
(5).
$$

Expected proportion:

$$
\frac4{20}=20\%.
$$

Table:

$$
400/2000=20\%.
$$

Almost exactly what we expect.

So your table is essentially experimentally revealing

$$
\boxed{
|\operatorname{Gal}(f/\mathbb Q)|=20
}
$$

and specifically

$$
\boxed{
\operatorname{Gal}(f/\mathbb Q)\cong C_5\rtimes C_4.
}
$$

---

# 12. Why do primes tell us about the Galois group?

This is the beautiful connection between **finite fields, factorization, and Galois theory**.

Suppose a prime \(p\) does not cause bad reduction and we factor

$$
f(x)\pmod p.
$$

For example, suppose

$$
f(x)\pmod p
$$

factors as

$$
\text{linear}\times\text{irreducible quadratic}\times\text{irreducible quadratic}.
$$

The factor degrees are

$$
1,2,2.
$$

This corresponds to a Frobenius element whose permutation of the five roots has cycle structure

$$
\boxed{(1,2,2)}.
$$

Similarly:

$$
\begin{array}{c|c}
\text{Factorization mod }p & \text{Galois cycle type}\\
\hline
1+1+1+1+1 &(1,1,1,1,1)\\
1+2+2 &(1,2,2)\\
1+4 &(1,4)\\
5 &(5)
\end{array}
$$

This is the fundamental connection behind the table.

---

# 13. Why approximately \(1/20\) of primes split completely

This is where **Chebotarev's density theorem** enters.

For an unramified prime \(p\), the Frobenius element

$$
\operatorname{Frob}_p
$$

is an element of the Galois group.

If

$$
\operatorname{Frob}_p=1,
$$

then every root is fixed.

Therefore

$$
f(x)\pmod p
$$

splits completely into five linear factors.

Since there is only one identity element in a group of order 20, Chebotarev predicts density

$$
\boxed{\frac1{20}}.
$$

That is exactly what your image says:

> type \((1,1,1,1,1)\) is approximately \(1/20\) of all groups, so group size is 20.

More precisely, the mathematical statement is that the density of primes with complete splitting is

$$
\boxed{\frac1{|\operatorname{Gal}(K/\mathbb Q)|}}.
$$

Thus the empirical count

$$
96/2000\approx0.048
$$

suggests

$$
|G|\approx\frac1{0.048}\approx20.83,
$$

which strongly points toward

$$
\boxed{|G|=20}.
$$

---

# 14. Why the polynomial itself is irreducible

There is another elegant fact.

Take

$$
f(x)=x^5+10x^3+20x-4.
$$

Shift \(x\mapsto x-1\):

$$
f(x-1)
=
x^5-5x^4+20x^3-40x^2+55x-35.
$$

Every nonleading coefficient is divisible by \(5\), while

$$
35\not\equiv0\pmod{25}.
$$

Therefore, by Eisenstein's criterion at \(5\),

$$
f(x-1)
$$

is irreducible over \(\mathbb Q\).

Since shifting the variable preserves irreducibility,

$$
\boxed{f(x)\text{ is irreducible over }\mathbb Q.}
$$

Thus if \(\alpha\) is any root,

$$
[\mathbb Q(\alpha):\mathbb Q]=5.
$$

This is important because it tells us that the polynomial's root field is a degree-5 extension, while its splitting field is degree 20.

---

# 15. Root field versus splitting field

This distinction is fundamental.

Take one root, say

$$
\alpha=x_0=b^3-b^2.
$$

Then

$$
[\mathbb Q(\alpha):\mathbb Q]=5.
$$

But \(\mathbb Q(\alpha)\) does **not** contain all five roots.

To get all the roots, we need to adjoin the fifth root of unity:

$$
\zeta_5.
$$

Thus

$$
\boxed{
\mathbb Q(\alpha)
\subsetneq
\mathbb Q(b,\zeta_5).
}
$$

The degrees are

$$
[\mathbb Q(\alpha):\mathbb Q]=5,
$$

whereas

$$
[\mathbb Q(b,\zeta_5):\mathbb Q]=20.
$$

The extension diagram looks like

```text
                    K = Q(2^(1/5), ζ5)
                         degree 20
                       /          \
                     /              \
                   5                  4
                 /                      \
                Q(α)                  Q(ζ5)
              degree 5               degree 4
                 \                      /
                  \                    /
                       Q
```

More precisely, the degree-5 root field corresponds to the subgroup of order 4 fixing one root.

---

# 16. Why \(K\) really is the splitting field

We already know

$$
\{\alpha_0,\ldots,\alpha_4\}\subset K.
$$

So the splitting field \(L\) satisfies

$$
L\subseteq K.
$$

Now consider the action of

$$
G=\operatorname{Gal}(K/\mathbb Q)
$$

on the five roots.

We found

$$
\sigma:k\mapsto k+3
$$

and

$$
\tau:k\mapsto2k.
$$

These permutations generate a faithful group of permutations of the five roots.

Therefore, if an automorphism of \(K\) fixes **every root**, it must induce the identity permutation.

But the only element of \(G\) inducing the identity permutation is the identity automorphism.

Consequently,

$$
\operatorname{Gal}(K/L)=1.
$$

Hence

$$
K=L.
$$

Thus

$$
\boxed{
\operatorname{Spl}_{\mathbb Q}
(x^5+10x^3+20x-4)
=
\mathbb Q(2^{1/5},\zeta_5).
}
$$

And

$$
\boxed{
[\operatorname{Spl}(f):\mathbb Q]=20.
}
$$

---

# 17. The entire structure in one picture

The quintic has the special form

$$
\boxed{
f(x)=D_5(x,-2)-4.
}
$$

Use

$$
\boxed{x=u-\frac2u}
$$

to obtain

$$
D_5(x,-2)
=
u^5-\frac{32}{u^5}.
$$

Thus

$$
u^{10}-4u^5-32=0
$$

and hence

$$
\boxed{u^5=8\quad\text{or}\quad u^5=-4.}
$$

Choose

$$
b=2^{1/5},\qquad \zeta=\zeta_5.
$$

Then

$$
u_k=b^3\zeta^k
$$

and

$$
\boxed{
\alpha_k=b^3\zeta^k-b^2\zeta^{-k}.
}
$$

Therefore

$$
\boxed{
K=\mathbb Q(b,\zeta)
=\mathbb Q(2^{1/5},\zeta_5).
}
$$

Its degree is

$$
\boxed{5\times4=20}.
$$

Its Galois group is

$$
\boxed{
G=C_5\rtimes C_4
}
$$

with relation

$$
\boxed{
\tau\sigma\tau^{-1}=\sigma^2.
}
$$

Its action on the five roots produces exactly

$$
\boxed{
(1^5),\quad(1\,2^2),\quad(1\,4),\quad(5)
}
$$

and Chebotarev explains why the primes in your table occur approximately in the ratios

$$
\boxed{
1:5:10:4
}
$$

or

$$
\boxed{
5\%:25\%:50\%:20\%.
}
$$

---

## One particularly important conceptual point

The **splitting field is not merely "the field containing the solutions"** in an informal sense.

It is the field obtained by adjoining **all conjugate roots simultaneously**:

$$
\boxed{
\operatorname{Spl}(f)
=
\mathbb Q(\alpha_1,\ldots,\alpha_5).
}
$$

For this particular quintic,

$$
\boxed{
\mathbb Q(\alpha_1,\ldots,\alpha_5)
=
\mathbb Q(2^{1/5},\zeta_5).
}
$$

That is why Galois theory cares so much about splitting fields: **every automorphism of the splitting field permutes the roots**, giving a concrete permutation representation

$$
\operatorname{Gal}(f/\mathbb Q)
\hookrightarrow S_5.
$$

Here that subgroup is the 20-element group

$$
\boxed{C_5\rtimes C_4\subset S_5},
$$

rather than the full \(S_5\), which has \(120\) elements.

And the prime-factorization table you showed is essentially an experimental fingerprint of this subgroup.


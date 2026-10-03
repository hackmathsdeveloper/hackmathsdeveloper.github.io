
Yes. This polynomial has a particularly nice hidden structure:

$$
P(x)=x^5+10x^3+20x-4.
$$

The key observation is that

$$
x^5+10x^3+20x=D_5(x,-2),
$$

where \(D_5\) is a Dickson polynomial. This makes the splitting field unusually explicit.

## 1. First: factorization over \(\mathbb Q\)

A quick irreducibility test is modulo \(11\):

$$
P(x)\pmod {11}=x^5-x^3-2x-4.
$$

It is irreducible over \(\mathbb F_{11}\), hence \(P(x)\) is irreducible over \(\mathbb Q\).

So adjoining one root gives a degree-5 extension.

---

# 2. The hidden substitution

Put

$$
x=y-\frac{2}{y}.
$$

Then

$$
\begin{aligned}
x^5+10x^3+20x
&=\left(y-\frac2y\right)^5
+10\left(y-\frac2y\right)^3
+20\left(y-\frac2y\right)\\
&=y^5-\frac{32}{y^5}.
\end{aligned}
$$

Therefore \(P(x)=0\) becomes

$$
y^5-\frac{32}{y^5}=4.
$$

Multiplying by \(y^5\),

$$
y^{10}-4y^5-32=0,
$$

and hence

$$
(y^5-8)(y^5+4)=0.
$$

Thus

$$
y^5=8
$$

or

$$
y^5=-4.
$$

But the second set gives the same \(x\)'s, because if \(y^5=8\), then

$$
\left(-\frac2y\right)^5=-\frac{32}{8}=-4
$$

and

$$
-\frac2y-\frac{2}{-2/y}
=-\frac2y+y
=y-\frac2y.
$$

So we only need the five solutions of

$$
y^5=8.
$$

---

# 3. Explicit roots

Let

$$
\alpha=2^{3/5},
\qquad
\zeta=\zeta_5=e^{2\pi i/5}.
$$

Since

$$
\alpha^5=8,
$$

the five \(y\)'s are

$$
y_k=\alpha\zeta^k,\qquad k=0,1,2,3,4.
$$

Consequently the five roots of \(P\) are

$$
\boxed{
r_k=\alpha\zeta^k-\frac{2}{\alpha\zeta^k}
}
$$

or

$$
\boxed{
r_k=2^{3/5}\zeta^k-2^{2/5}\zeta^{-k},
\qquad k=0,\ldots,4.
}
$$

This immediately exposes the splitting field.

---

# 4. Splitting field

We have

$$
\alpha=2^{3/5}.
$$

But

$$
\frac{\alpha^2}{2}=2^{1/5},
$$

so

$$
\mathbb Q(\alpha)=\mathbb Q(2^{1/5}).
$$

All roots lie in

$$
\mathbb Q(2^{1/5},\zeta_5).
$$

Therefore

$$
\boxed{
K=\mathbb Q(2^{1/5},\zeta_5).
}
$$

Now

$$
[\mathbb Q(2^{1/5}):\mathbb Q]=5
$$

and

$$
[\mathbb Q(\zeta_5):\mathbb Q]=4.
$$

Their intersection is \(\mathbb Q\), since the degrees \(5\) and \(4\) are coprime. Hence

$$
[K:\mathbb Q]=5\cdot4=20.
$$

Thus

$$
\boxed{[K:\mathbb Q]=20}.
$$

In fact \(K\) is exactly the splitting field, not merely a field containing it.

---

# 5. Galois group

There are two particularly useful automorphisms.

Define

$$
\sigma:
\begin{cases}
\alpha\mapsto\zeta\alpha,\\
\zeta\mapsto\zeta,
\end{cases}
$$

and

$$
\tau:
\begin{cases}
\alpha\mapsto\alpha,\\
\zeta\mapsto\zeta^2.
\end{cases}
$$

On the roots \(r_k\),

$$
\sigma(r_k)=r_{k+1},
$$

while

$$
\tau(r_k)=r_{2k}.
$$

Thus the Galois group acts on the five roots as affine transformations

$$
k\longmapsto ak+b
\pmod5,
$$

where

$$
a\in\mathbb F_5^\times,\qquad b\in\mathbb F_5.
$$

Consequently

$$
\boxed{
\operatorname{Gal}(K/\mathbb Q)
\simeq C_5\rtimes C_4
}
$$

of order \(20\).

This is the Frobenius group

$$
\boxed{\operatorname{AGL}(1,5)}
$$

sometimes denoted \(F_{20}\).

It is a subgroup of \(S_5\), but **not** \(D_5\) and not \(S_5\).

---

# 6. Discriminant

The discriminant of \(P\) is

$$
\boxed{\operatorname{disc}(P)=64\,800\,000}
$$

and

$$
\boxed{
\operatorname{disc}(P)=2^8\,3^4\,5^5.
}
$$

There is an important subtlety here.

The polynomial discriminant is divisible by \(3\), but \(3\) is **not** ramified in the splitting field \(K\). The factor \(3^4\) comes from the index of \(\mathbb Z[\theta]\) in the ring of integers.

The actual splitting field

$$
K=\mathbb Q(2^{1/5},\zeta_5)
$$

is ramified only at

$$
\boxed{2,\;5}.
$$

So the clean Frobenius/factorization classification below applies directly to

$$
p\ne2,5.
$$

---

# 7. How \(P(x)\pmod p\) splits

This is where the Galois theory becomes very elegant.

For a prime \(p\ne2,5\), Frobenius acts on

$$
r_k
$$

as

$$
\operatorname{Frob}_p(r_k)=r_{a+pk}
$$

for some \(a\in\mathbb F_5\).

Therefore the factorization of \(P(x)\pmod p\) is determined entirely by

$$
p\bmod5.
$$

There are only **four possible Frobenius types**.

---

## Case A: \(p\equiv1\pmod5\)

Then

$$
k\mapsto k+a.
$$

There are two possibilities.

### A1. \(a=0\)

Every root is fixed.

Therefore

$$
\boxed{P(x)\equiv
(x-r_1)(x-r_2)(x-r_3)(x-r_4)(x-r_5)\pmod p}
$$

and the factorization type is

$$
\boxed{1+1+1+1+1}.
$$

So \(P\) splits completely.

The criterion is

$$
\boxed{
2^{(p-1)/5}\equiv1\pmod p.
}
$$

Equivalently, \(2\) is a fifth power modulo \(p\).

For example:

$$
\boxed{p=151}
$$

and indeed

$$
P(x)\pmod {151}
$$

splits as

$$
\boxed{
(x+8)(x-51)(x-47)(x-35)(x-26).
}
$$

---

### A2. \(a\ne0\)

Then

$$
k\mapsto k+a
$$

is a 5-cycle.

Therefore \(P\) is irreducible modulo \(p\):

$$
\boxed{\text{factorization type }5}.
$$

For example,

$$
p=11:
$$

$$
P(x)\equiv x^5-x^3-2x-4\pmod{11}
$$

is irreducible.

Likewise

$$
p=31:
$$

$$
P(x)\pmod{31}
=x^5+10x^3-11x-4
$$

is irreducible.

So for \(p\equiv1\pmod5\):

$$
\boxed{
\begin{array}{c|c}
2^{(p-1)/5}\pmod p & \text{factorization}\\
\hline
1 & 1+1+1+1+1\\
\ne1 & 5
\end{array}}
$$

---

# 8. Case B: \(p\equiv2\pmod5\)

Now multiplication by \(p\) modulo 5 has order 4:

$$
k\mapsto a+2k.
$$

This affine transformation has exactly one fixed point, while the other four points form a 4-cycle.

Therefore

$$
\boxed{\text{factorization type }1+4}.
$$

For example,

$$
p=7.
$$

We get

$$
P(x)\equiv x^5+3x^3+6x+3\pmod7
$$

and

$$
\boxed{
P(x)
\equiv
(x+1)
(x^4-x^3-3x^2+3x+3)
\pmod7.
}
$$

Thus

$$
\boxed{1+4}.
$$

Another example is \(p=13\):

$$
\boxed{
P(x)\equiv
(x+2)
(x^4-2x^3+x^2-2x-2)
\pmod {13}.
}
$$

Again:

$$
\boxed{1+4}.
$$

---

# 9. Case C: \(p\equiv3\pmod5\)

Now multiplication by \(p\) is multiplication by \(3\), which also has order 4 in \(\mathbb F_5^\times\).

Again there is exactly one fixed point and one 4-cycle.

Hence

$$
\boxed{\text{factorization type }1+4}.
$$

For example,

$$
p=23:
$$

$$
\boxed{
P(x)\equiv
(x+4)
(x^4-4x^3+3x^2+11x-1)
\pmod {23}.
}
$$

So

$$
\boxed{1+4}.
$$

---

# 10. Case D: \(p\equiv4\pmod5\)

Here

$$
p\equiv-1\pmod5.
$$

The Frobenius action is

$$
k\mapsto a-k.
$$

This has exactly one fixed point and two transpositions.

Therefore

$$
\boxed{\text{factorization type }1+2+2}.
$$

For example, \(p=19\):

$$
\boxed{
P(x)\equiv
(x+4)(x^2-3x-8)(x^2-x-7)
\pmod {19}.
}
$$

Thus

$$
\boxed{1+2+2}.
$$

For \(p=29\):

$$
\boxed{
P(x)\equiv
(x-4)(x^2+9x+3)(x^2-5x+10)
\pmod {29}.
}
$$

Again:

$$
\boxed{1+2+2}.
$$

---

# 11. Complete classification

For every unramified prime \(p\ne2,5\):

$$
\boxed{
\begin{array}{c|c|c}
p\bmod5 & \text{Frobenius cycle type} & P(x)\pmod p\\
\hline
1 & 1^5 & 1+1+1+1+1\\
1 & 5 & 5\\
2 & 1\,4 & 1+4\\
3 & 1\,4 & 1+4\\
4 & 1\,2^2 & 1+2+2
\end{array}}
$$

There are therefore exactly **four distinct splitting patterns**:

$$
\boxed{
1+1+1+1+1,\qquad
5,\qquad
1+4,\qquad
1+2+2.
}
$$

The first two occur only for \(p\equiv1\pmod5\), distinguished by whether \(2\) is a fifth power modulo \(p\).

---

# 12. Some explicit primes

Here is a useful sample:

| \(p\) | \(p\bmod5\) | Factorization type | \(P(x)\bmod p\)  |
| ----: | ----------: | ------------------ | ---------------- |
|     7 |           2 | \(1+4\)            | \((x+1)(4)\)     |
|    11 |           1 | \(5\)              | irreducible      |
|    13 |           3 | \(1+4\)            | \((1)(4)\)       |
|    19 |           4 | \(1+2+2\)          | \((1)(2)(2)\)    |
|    23 |           3 | \(1+4\)            | \((1)(4)\)       |
|    29 |           4 | \(1+2+2\)          | \((1)(2)(2)\)    |
|    31 |           1 | \(5\)              | irreducible      |
|    41 |           1 | \(5\)              | irreducible      |
|    43 |           3 | \(1+4\)            | \((1)(4)\)       |
|    59 |           4 | \(1+2+2\)          | \((1)(2)(2)\)    |
|    61 |           1 | \(5\)              | irreducible      |
|    71 |           1 | \(5\)              | irreducible      |
|   151 |           1 | \(1+1+1+1+1\)      | completely split |

The exceptional primes \(2,3,5\) need separate treatment. In particular, \(3\) is a good example of why **polynomial factorization modulo \(p\)** and **Frobenius factorization in the splitting field** aren't always identical when \(p\) divides the polynomial discriminant.

---

# 13. Why the factorization patterns match the Galois group

The conjugacy classes of

$$
G=C_5\rtimes C_4
$$

have precisely these cycle structures in its natural action on five points:

$$
\begin{array}{c|c|c}
\text{Galois element} & \text{order} & \text{cycle structure}\\
\hline
1 & 1 & 1^5\\
\text{nontrivial }C_5 & 5 & 5\\
\text{elements with multiplier }-1 & 2 & 1\,2^2\\
\text{elements with multiplier }2,3 & 4 & 1\,4
\end{array}
$$

So the modular factorizations are literally the cycle decompositions of Frobenius elements.

This is a very nice concrete example of the fundamental correspondence

$$
\boxed{
\text{factorization of }P\bmod p
\quad\longleftrightarrow\quad
\text{Frobenius conjugacy class in }\operatorname{Gal}(K/\mathbb Q).
}
$$

---

## 14. The entire structure in one picture

The algebra can be summarized as

$$
\boxed{
\begin{aligned}
P(x)&=x^5+10x^3+20x-4\\[2mm]
x&=y-\frac2y\\[2mm]
P(x)=0
&\Longleftrightarrow
y^{10}-4y^5-32=0\\
&\Longleftrightarrow
(y^5-8)(y^5+4)=0\\
&\Longrightarrow y^5&=8\\[2mm]
y&=2^{3/5}\zeta_5^k\\[2mm]
x_k&=
2^{3/5}\zeta_5^k-
2^{2/5}\zeta_5^{-k}\\[2mm]
K&=\mathbb Q(2^{1/5},\zeta_5)\\[2mm]
[K:\mathbb Q]&=20\\[2mm]
\operatorname{Gal}(K/\mathbb Q)
&\simeq C_5\rtimes C_4.
\end{aligned}}
$$

And the prime splitting is

$$
\boxed{
\begin{array}{c|c}
p & P(x)\pmod p\\
\hline
p\equiv1\pmod5,\;2^{(p-1)/5}=1
&1+1+1+1+1\\
p\equiv1\pmod5,\;2^{(p-1)/5}\ne1
&5\\
p\equiv2,3\pmod5
&1+4\\
p\equiv4\pmod5
&1+2+2
\end{array}}
$$

This polynomial is therefore a particularly clean example where **Dickson polynomials → explicit radicals → cyclotomic field → Frobenius group of order 20 → prime splitting types** all fit together exactly.


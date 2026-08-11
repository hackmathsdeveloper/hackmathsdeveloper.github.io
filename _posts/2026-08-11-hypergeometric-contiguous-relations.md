---
title: "Why 15 Gauss Relations Collapse Into One Pochhammer Trick — The Strangest Secret of Contiguous Hypergeometric Functions"
date: 2026-08-11
categories:
  - Special Functions
  - Mathematics
tags:
  - hypergeometric-functions
  - gauss-contiguous-relations
  - pochhammer-symbol
  - series-manipulation
  - three-term-recurrence
  - derivative-identities
share: true
read_time: true
excerpt: "Gauss discovered 15 distinct three-term relations among contiguous $${}_2F_1$$ functions. But they all flow from one elementary identity: the difference of two Pochhammer symbols differing by a unit shift. We derive the key relations from scratch — and show how they connect parameter shifts to derivatives."
---

**Challenge to the reader:** Without looking ahead, try to express $${}_2F_1(a,b;c;z) - {}_2F_1(a-1,b;c;z)$$ as a single hypergeometric term times a rational prefactor. The trick is in the Pochhammer symbols — and it takes three lines.

---

For $${}_2F_1$$, there is not just one contiguous relation: Gauss found 15 basic three-term relations. They are all derived by taking simple identities between Pochhammer symbols and applying them coefficient-by-coefficient to the defining series. [arxiv](https://arxiv.org/pdf/math/0109222.pdf)

I will derive a particularly useful one:

$$
\boxed{
{}_2F_1(a,b;c;z)
=
{}_2F_1(a-1,b;c;z)
+
\frac{bz}{c}\,
{}_2F_1(a,b+1;c+1;z).
}
\tag{C}
$$

The three functions differ only by integer shifts of their parameters, so they are *contiguous*. More generally, two $${}_pF_q$$ functions are called contiguous when corresponding parameters differ by integers. [dlmf.nist](https://dlmf.nist.gov/16.3)

---

## 1. Start from the Series

Write

$$
F(a,b;c;z):={}_2F_1(a,b;c;z)
=
\sum_{n=0}^{\infty}
\frac{(a)_n(b)_n}{(c)_n\,n!}z^n.
$$

We seek $$F(a,b;c;z)-F(a-1,b;c;z)$$. Direct substitution gives

$$
F(a,b;c;z)-F(a-1,b;c;z)
=
\sum_{n=0}^{\infty}
\frac{\bigl((a)_n-(a-1)_n\bigr)(b)_n}
{(c)_n\,n!}z^n.
\tag{1}
$$

The $$n=0$$ term is zero, because $$(a)_0=(a-1)_0=1$$.

---

## 2. The Pochhammer Identity — Where Everything Happens

For $$n\geq 1$$,

$$
(a)_n=a(a+1)\cdots(a+n-1),
$$

and

$$
(a-1)_n=(a-1)a\cdots(a+n-2).
$$

Factor out the common portion $$(a)_{n-1}=a(a+1)\cdots(a+n-2)$$:

$$
\begin{aligned}
(a)_n-(a-1)_n
&=(a)_{n-1}\bigl[(a+n-1)-(a-1)\bigr] \\
&=n(a)_{n-1}.
\end{aligned}
\tag{2}
$$

This elementary difference identity is the **entire mechanism**. Every one of Gauss's 15 relations traces back to factoring out a shifted Pochhammer symbol and taking the difference.

**Challenge to the reader:** Prove the dual identity $$(b)_n - (b-1)_n = n(b)_{n-1}$$ and use it to derive the symmetric companion relation (C′). The steps mirror Section 3 exactly — the only change is which parameter you shift.

---

## 3. Apply It to the Series

Insert (2) into (1):

$$
\begin{aligned}
F(a,b;c;z)-F(a-1,b;c;z)
&=
\sum_{n=1}^{\infty}
\frac{n(a)_{n-1}(b)_n}
{(c)_n n!}z^n \\
&=
\sum_{n=1}^{\infty}
\frac{(a)_{n-1}(b)_n}
{(c)_n (n-1)!}z^n.
\end{aligned}
$$

Now use

$$
(b)_n=b(b+1)_{n-1},
\qquad
(c)_n=c(c+1)_{n-1},
$$

to obtain

$$
F(a,b;c;z)-F(a-1,b;c;z)
=
\frac{b}{c}
\sum_{n=1}^{\infty}
\frac{(a)_{n-1}(b+1)_{n-1}}
{(c+1)_{n-1}(n-1)!}z^n.
$$

Reindex with $$m=n-1$$:

$$
\begin{aligned}
&=
\frac{bz}{c}
\sum_{m=0}^{\infty}
\frac{(a)_m(b+1)_m}
{(c+1)_m m!}z^m\\
&=
\frac{bz}{c}F(a,b+1;c+1;z).
\end{aligned}
$$

Rearranging proves (C):

$$
\boxed{
F(a,b;c;z)-F(a-1,b;c;z)
=
\frac{bz}{c}F(a,b+1;c+1;z).
}
$$

---

## 4. Symmetric Companion

By the same argument, shifting $$b$$ rather than $$a$$:

$$
\boxed{
F(a,b;c;z)-F(a,b-1;c;z)
=
\frac{az}{c}F(a+1,b;c+1;z).
}
\tag{C'}
$$

The symmetry is expected because $${}_2F_1(a,b;c;z)$$ is symmetric in its two upper parameters $$a,b$$.

---

## 5. A Relation Without $$z$$

Another basic Gauss relation is

$$
\boxed{
aF(a+1,b;c;z)
-
bF(a,b+1;c;z)
+
(b-a)F(a,b;c;z)
=0.
}
\tag{D}
$$

To derive it, compare the coefficient of $$z^n$$. Multiplying the coefficient of $$F(a+1,b;c;z)$$ by $$a$$ gives

$$
a\frac{(a+1)_n(b)_n}{(c)_n n!}
=
(a+n)\frac{(a)_n(b)_n}{(c)_n n!}.
$$

Similarly,

$$
b\frac{(a)_n(b+1)_n}{(c)_n n!}
=
(b+n)\frac{(a)_n(b)_n}{(c)_n n!}.
$$

Thus the coefficient of the left side of (D) is

$$
\bigl[(a+n)-(b+n)+(b-a)\bigr]
\frac{(a)_n(b)_n}{(c)_n n!}=0.
$$

Since every coefficient vanishes, the relation holds identically. [arxiv](https://arxiv.org/pdf/math/0109222.pdf)

---

## 6. Connection to Derivatives

The derivative identity

$$
\frac{d}{dz}F(a,b;c;z)
=
\frac{ab}{c}F(a+1,b+1;c+1;z)
$$

follows immediately by differentiating the series termwise. Combined with a contiguous relation, it lets you replace derivatives by parameter shifts; for example, [dlmf.nist](https://dlmf.nist.gov/16.3)

$$
\begin{aligned}
z\frac{d}{dz}F(a,b;c;z)
&=
a\left[F(a+1,b;c;z)-F(a,b;c;z)\right] \\
&=
b\left[F(a,b+1;c;z)-F(a,b;c;z)\right].
\end{aligned}
$$

These operator/shift identities, together with the Gauss differential equation, generate the broader family of contiguous relations — including those used to construct Gauss's continued fraction.

---

## 7. Deeper Significance

The Pochhammer identity $$(a)_n - (a-1)_n = n(a)_{n-1}$$ is deceptively simple, but it encodes a structural fact: the ring of sequences with rational term ratios is closed under finite differences. Every contiguous relation is a linear consequence of this one algebraic fact, which is why the 15 Gauss relations form a module over $$\mathbb{Q}(a,b,c,z)$$ of rank only 2. In modern terms, contiguous relations are the **shadows of the Gauss-Manin connection** on the cohomology of the hypergeometric D-module — the same structure that produces monodromy representations, modular forms, and the rigid local systems of Deligne-Simpson theory.

---

**Final challenge to the reader:** Use (C′) and (D) together to eliminate the $$z$$-dependent term and derive a pure three-term recurrence among $${}_2F_1$$ functions with contiguous parameters and no explicit $$z$$ factor. Then verify your identity against (C) — you should recover one of the remaining 13 Gauss relations.

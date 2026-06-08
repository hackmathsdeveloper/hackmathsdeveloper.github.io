Euler computed $\zeta(2k)$ for all positive integers $k$ in terms of Bernoulli numbers:

\zeta(2k)=\frac{(-1)^{k+1}B_{2k}(2\pi)^{2k}}{2(2k)!}

To understand where this comes from, it is best to proceed in two stages:

1. Construct Bernoulli numbers from their defining generating series.
2. Show how that generating series naturally appears in trigonometric expansions whose coefficients are ζ(2k).

---

# 1. Bernoulli numbers arise from a summation generating function

The Bernoulli numbers (B_n) are defined by the exponential generating function

[
\frac{x}{e^x-1}
===============

\sum_{n=0}^{\infty} B_n \frac{x^n}{n!}.
]

This is not merely a definition—it encodes the sums

[
1^m+2^m+\cdots+n^m.
]

---

## Expand the denominator

Start from

[
e^x
===

1+x+\frac{x^2}{2!}
+\frac{x^3}{3!}
+\cdots
]

thus

[
e^x-1
=====

x+\frac{x^2}{2}
+\frac{x^3}{6}
+\frac{x^4}{24}
+\cdots
]

Hence

[
\frac{x}{e^x-1}
===============

\frac{1}
{1+\frac{x}{2}
+\frac{x^2}{6}
+\frac{x^3}{24}
+\cdots}.
]

Now invert the series.

Let

[
\frac{x}{e^x-1}
===============

a_0+a_1x+a_2x^2+a_3x^3+\cdots.
]

Multiplying by the denominator:

[
(a_0+a_1x+a_2x^2+\cdots)
\left(
1+\frac{x}{2}+\frac{x^2}{6}+\cdots
\right)
=1.
]

Matching coefficients:

### Constant term

[
a_0=1.
]

Therefore

[
B_0=1.
]

---

### Coefficient of (x)

[
a_1+\frac12a_0=0.
]

Hence

[
a_1=-\frac12.
]

Thus

[
B_1=-\frac12.
]

---

### Coefficient of (x^2)

[
a_2+\frac12a_1+\frac16a_0=0.
]

Substitute:

[
a_2-\frac14+\frac16=0.
]

[
a_2=\frac1{12}.
]

Since

[
a_2=\frac{B_2}{2!},
]

we obtain

[
B_2=\frac16.
]

---

Continuing:

[
B_0=1,
]

[
B_1=-\frac12,
]

[
B_2=\frac16,
]

[
B_3=0,
]

[
B_4=-\frac1{30},
]

[
B_5=0,
]

[
B_6=\frac1{42},
]

[
B_8=-\frac1{30},
]

[
B_{10}=\frac5{66},
]

etc.

All odd Bernoulli numbers beyond (B_1) vanish.

---

# 2. Bernoulli numbers and power sums

The generating function immediately implies Faulhaber's formula.

For example,

[
1+2+\cdots+n
============

\frac{n^2+n}{2}
]

contains (B_1).

Similarly

[
1^2+2^2+\cdots+n^2
==================

\frac{n^3}{3}
+\frac{n^2}{2}
+\frac{n}{6},
]

where

[
\frac16=B_2.
]

In general

[
\sum_{k=1}^{n}k^m
=================

\frac{1}{m+1}
\sum_{j=0}^{m}
(-1)^j
\binom{m+1}{j}
B_j
n^{m+1-j}.
]

Bernoulli numbers therefore encode the entire hierarchy of polynomial summation formulas.

---

# 3. Why Bernoulli numbers appear in ζ(2k)

The bridge comes from the cotangent function.

Euler discovered

[
\sin x
======

x
\prod_{n=1}^{\infty}
\left(1-\frac{x^2}{n^2\pi^2}\right).
]

This is the analogue of factorizing a polynomial by its roots.

Taking logarithms:

[
\log(\sin x)
============

\log x
+
\sum_{n=1}^{\infty}
\log!\left(
1-\frac{x^2}{n^2\pi^2}
\right).
]

Differentiate:

[
\cot x
======

## \frac1x

2x
\sum_{n=1}^{\infty}
\frac1{n^2\pi^2-x^2}.
]

Now expand

[
\frac1{n^2\pi^2-x^2}
====================

\frac1{n^2\pi^2}
\frac1{1-\frac{x^2}{n^2\pi^2}}
==============================

\sum_{m=0}^{\infty}
\frac{x^{2m}}
{n^{2m+2}\pi^{2m+2}}.
]

Substitute:

[
\cot x
======

## \frac1x

2
\sum_{m=0}^{\infty}
\zeta(2m+2)
\frac{x^{2m+1}}
{\pi^{2m+2}}.
]

Thus

[
x\cot x
=======

## 1

2
\sum_{m=1}^{\infty}
\zeta(2m)
\frac{x^{2m}}
{\pi^{2m}}.
]

This expansion contains the zeta values directly.

---

# 4. Bernoulli numbers appear in the same function

Now examine

[
x\cot x.
]

Using the Bernoulli generating function,

[
\frac{x}{e^x-1}
===============

\sum B_n \frac{x^n}{n!},
]

one can derive

[
x\cot x
=======

\sum_{m=0}^{\infty}
(-1)^m
\frac{2^{2m}B_{2m}}
{(2m)!}
x^{2m}.
]

The first terms are

[
x\cot x
=======

1
-\frac{x^2}{3}
-\frac{x^4}{45}
-\frac{2x^6}{945}
-\cdots.
]

---

# 5. Compare the two expansions

From the zeta expansion:

[
x\cot x
=======

## 1

2\sum_{m=1}^{\infty}
\zeta(2m)
\frac{x^{2m}}{\pi^{2m}}.
]

From the Bernoulli expansion:

[
x\cot x
=======

1+
\sum_{m=1}^{\infty}
(-1)^m
\frac{2^{2m}B_{2m}}
{(2m)!}
x^{2m}.
]

Match coefficients of (x^{2m}):

[
-2\frac{\zeta(2m)}{\pi^{2m}}
============================

(-1)^m
\frac{2^{2m}B_{2m}}
{(2m)!}.
]

Solving:

[
\zeta(2m)
=========

\frac{(-1)^{m+1}B_{2m}(2\pi)^{2m}}
{2(2m)!}.
]

This is Euler's theorem.

---

# First few evaluations

For (m=1),

[
B_2=\frac16
]

giving

[
\zeta(2)
========

\frac{\pi^2}{6}.
]

---

For (m=2),

[
B_4=-\frac1{30}
]

giving

[
\zeta(4)
========

\frac{\pi^4}{90}.
]

---

For (m=3),

[
B_6=\frac1{42}
]

giving

[
\zeta(6)
========

\frac{\pi^6}{945}.
]

---

For (m=4),

[
B_8=-\frac1{30}
]

giving

[
\zeta(8)
========

\frac{\pi^8}{9450}.
]

---

Conceptually, the chain is

[
\boxed{
\frac{x}{e^x-1}
\longrightarrow
B_n
\longrightarrow
x\cot x
\longrightarrow
\sin x
\longrightarrow
\prod_{n=1}^{\infty}
\left(1-\frac{x^2}{n^2\pi^2}\right)
\longrightarrow
\zeta(2k)
}
]

which is one of the most beautiful connections in mathematics: **a generating function for finite sums, a trigonometric function, and an infinite sum over reciprocals of powers all encode exactly the same coefficients.**


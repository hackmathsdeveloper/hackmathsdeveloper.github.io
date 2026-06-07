
Start with the classical Gregory–Leibniz series

[
\frac{\pi}{4}
=============

# 1-\frac13+\frac15-\frac17+\frac19-\cdots

\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
]

The goal is to show how applying Euler's transformation to this alternating series converts the simple rational terms (1/(2n+1)) into a continued fraction whose coefficients are polynomial functions of (n).

---

# 1. Euler transformation of an alternating series

For an alternating series

[
S=\sum_{n=0}^{\infty}(-1)^n a_n,
]

Euler's transformation states

[
S
=

\sum_{n=0}^{\infty}
\frac{\Delta^n a_0}{2^{n+1}},
]

where

[
\Delta a_n=a_n-a_{n+1}
]

is the forward difference operator.

For

[
a_n=\frac1{2n+1},
]

we compute successive differences.

---

## First difference

[
\Delta a_n
==========

## \frac1{2n+1}

# \frac1{2n+3}

\frac{2}{(2n+1)(2n+3)}.
]

At (n=0),

[
\Delta a_0=\frac23.
]

---

## Second difference

[
\Delta^2 a_n
============

\frac{8}
{(2n+1)(2n+3)(2n+5)}.
]

Hence

[
\Delta^2 a_0=\frac8{15}.
]

---

## Third difference

[
\Delta^3 a_n
============

\frac{48}
{(2n+1)(2n+3)(2n+5)(2n+7)}.
]

Hence

[
\Delta^3 a_0=\frac{48}{105}.
]

---

A general formula is

[
\Delta^k a_0
============

\frac{2^k k!}
{1\cdot3\cdot5\cdots(2k+1)}.
]

Therefore Euler's transformed series becomes

[
\frac{\pi}{4}
=============

\frac12
+\frac1{6}
+\frac1{30}
+\frac1{70}
+\frac1{126}
+\cdots.
]

This converges much faster than Gregory–Leibniz.

---

# 2. Hypergeometric form

Observe

[
\frac1{2k+1}
============

\int_0^1 x^{2k},dx.
]

Thus

[
\frac{\pi}{4}
=============

\sum_{k=0}^{\infty}
\frac{(k!)^2}
{(2k+1)!}.
]

Equivalently

[
\frac{\pi}{4}
=============

{}_2F_1!\left(
1,\frac12;\frac32;-1
\right).
]

The appearance of a hypergeometric function is crucial because Euler, Gauss, and later Stieltjes developed systematic transformations from hypergeometric series into continued fractions.

---

# 3. Euler's continued-fraction machinery

Euler discovered that many series

[
1+\frac{a_1}{b_1}
+\frac{a_1a_2}{b_1b_2}
+\cdots
]

can be rewritten as continued fractions.

For a hypergeometric ratio one obtains a J-fraction (Jacobi continued fraction).

Applying Euler's procedure to

[
\arctan x
=========

x-\frac{x^3}{3}
+\frac{x^5}{5}
-\cdots
]

gives

[
\arctan x
=========

\cfrac{x}
{1+\cfrac{1^2x^2}
{3+\cfrac{2^2x^2}
{5+\cfrac{3^2x^2}
{7+\cdots}}}}.
]

This is Euler's continued fraction for the inverse tangent.

---

# 4. Specializing to (x=1)

Since

[
\arctan(1)=\frac{\pi}{4},
]

we obtain

[
\frac{\pi}{4}
=============

\cfrac{1}
{1+\cfrac{1}
{3+\cfrac{4}
{5+\cfrac{9}
{7+\cfrac{16}
{9+\cdots}}}}}.
]

The numerators are

[
1,4,9,16,\ldots=n^2
]

and the denominators are

[
1,3,5,7,9,\ldots=2n+1.
]

Thus the linear denominators from Gregory–Leibniz have been reorganized into a polynomial continued fraction:

[
\frac{\pi}{4}
=============

\cfrac{1}
{1+\cfrac{1^2}
{3+\cfrac{2^2}
{5+\cfrac{3^2}
{7+\cdots}}}}.
]

---

# 5. Why squares appear

The Gregory–Leibniz series has coefficients

[
a_n=\frac{(-1)^n}{2n+1}.
]

After Euler transformation the resulting hypergeometric structure involves ratios

[
\frac{(n+1)^2}{(2n+1)(2n+3)}.
]

When Euler's continued-fraction algorithm is applied, these ratios become the partial numerators

[
1^2,;2^2,;3^2,\ldots
]

while the odd integers remain in the partial denominators.

Hence the linear denominator (2n+1) of the original series is encoded into the odd-denominator ladder

[
1,3,5,7,\ldots
]

and the finite-difference structure generates the quadratic numerators (n^2).

---

# 6. Connection with Lambert's continued fraction

A more general form is

[
\arctan x
=========

\cfrac{x}
{1+\cfrac{1^2x^2}
{3+\cfrac{2^2x^2}
{5+\cfrac{3^2x^2}
{7+\cdots}}}}.
]

This is often attributed to both Euler and Johann Heinrich Lambert.

Setting (x=1) yields the continued fraction for (\pi).

---

# Summary

Starting with

[
\frac{\pi}{4}
=============

\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1},
]

Euler's transformation first rewrites the alternating series in terms of forward differences

[
\frac{\pi}{4}
=============

\sum_{n=0}^{\infty}
\frac{\Delta^n(1)}{2^{n+1}},
]

where

[
\Delta^n!\left(\frac1{2m+1}\right)_{m=0}
========================================

\frac{2^n n!}{(2n+1)!!}.
]

Recognizing the resulting series as hypergeometric and applying Euler's continued-fraction construction gives

[
\boxed{
\frac{\pi}{4}
=============

\cfrac{1}
{1+\cfrac{1^2}
{3+\cfrac{2^2}
{5+\cfrac{3^2}
{7+\cfrac{4^2}
{9+\cdots}}}}}
}
]

which is the polynomial continued fraction arising from the Gregory–Leibniz series after Euler's transformation. The original linear factors (2n+1) become the odd partial denominators, while the Euler-difference structure produces the square numerators (n^2).


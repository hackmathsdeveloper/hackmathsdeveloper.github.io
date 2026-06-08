
The Rogers–Ramanujan continued fraction (RRCF) is

[
R(q)
====

\cfrac{q^{1/5}}
{1+\cfrac{q}
{1+\cfrac{q^2}
{1+\cfrac{q^3}
{1+\cdots}}}},
\qquad |q|<1.
]

One of the most useful ways to study it is through the recurrence relations satisfied by its convergents.

---

# 1. General continued-fraction recurrence

For a continued fraction

[
K=\cfrac{a_0}
{b_0+\cfrac{a_1}
{b_1+\cfrac{a_2}
{b_2+\cdots}}},
]

define convergents

[
K_n=\frac{P_n}{Q_n}.
]

Then

[
P_n=b_nP_{n-1}+a_nP_{n-2},
]

[
Q_n=b_nQ_{n-1}+a_nQ_{n-2}.
]

These are called the continuant recurrences.

---

# 2. Apply to Rogers–Ramanujan

Ignoring the leading factor (q^{1/5}), define

[
F(q)
====

\cfrac{1}
{1+\cfrac{q}
{1+\cfrac{q^2}
{1+\cfrac{q^3}
{\ddots}}}}.
]

Here

[
a_n=q^n,
\qquad
b_n=1.
]

Therefore

[
P_n=P_{n-1}+q^nP_{n-2},
]

[
Q_n=Q_{n-1}+q^nQ_{n-2}.
]

with initial conditions

[
P_{-1}=1,\qquad P_0=1,
]

[
Q_{-1}=0,\qquad Q_0=1.
]

The Rogers–Ramanujan fraction is then

[
R(q)=q^{1/5}\lim_{n\to\infty}\frac{P_n}{Q_n}.
]

---

# 3. First few terms

For numerators:

[
P_0=1
]

[
P_1=1+q
]

[
P_2=1+q+q^2
]

[
P_3
===

1+q+q^2+q^3+q^4
]

[
P_4
===

1+q+q^2+q^3+2q^4+q^5+q^6.
]

Similarly

[
Q_0=1
]

[
Q_1=1
]

[
Q_2=1+q^2
]

[
Q_3=1+q^2+q^3
]

etc.

---

# 4. Three-term q-difference recurrence

Another approach is to truncate the tail.

Define

[
F_n
===

\cfrac{1}
{1+\cfrac{q^n}
{1+\cfrac{q^{n+1}}
{1+\cdots}}}.
]

Then

[
F_n=\frac1{1+q^nF_{n+1}}.
]

Equivalently,

[
F_n(1+q^nF_{n+1})=1.
]

This nonlinear recurrence completely determines the continued fraction.

---

# 5. Linear recurrence from Rogers–Ramanujan identities

The famous identity

[
R(q)
====

q^{1/5}
\frac{
\sum_{n=0}^{\infty}
\dfrac{q^{n^2}}
{(q;q)*n}
}
{
\sum*{n=0}^{\infty}
\dfrac{q^{n(n+1)}}
{(q;q)_n}
}
]

expresses the continued fraction as a ratio of two q-series.

Let

[
G(q)
====

\sum_{n\ge0}
\frac{q^{n^2}}
{(q;q)_n},
]

[
H(q)
====

\sum_{n\ge0}
\frac{q^{n(n+1)}}
{(q;q)_n}.
]

These satisfy Rogers–Ramanujan q-difference equations

[
G(q)=G(q^5)+q,G(q^{25}),
]

[
H(q)=H(q^5)+q^2H(q^{25}),
]

which induce functional equations for (R(q)).

---

# 6. Recurrence for the convergent polynomials

Let

[
A_n(q)=P_n,
\qquad
B_n(q)=Q_n.
]

Then

[
A_n(q)=A_{n-1}(q)+q^nA_{n-2}(q),
]

[
B_n(q)=B_{n-1}(q)+q^nB_{n-2}(q).
]

This is the standard Rogers–Ramanujan recurrence.

Notice its similarity to a Fibonacci recurrence:

[
F_n=F_{n-1}+F_{n-2}.
]

The only difference is that the coefficient of the second term grows geometrically as (q^n).

Thus the Rogers–Ramanujan continued fraction may be viewed as a q-deformed Fibonacci system.

---

# 7. Matrix formulation

Define

[
\mathbf v_n
===========

\begin{pmatrix}
P_n\
P_{n-1}
\end{pmatrix}.
]

Then

[
\mathbf v_n
===========

\begin{pmatrix}
1&q^n\
1&0
\end{pmatrix}
\mathbf v_{n-1}.
]

Hence

[
\mathbf v_n
===========

\left(
\prod_{k=1}^{n}
\begin{pmatrix}
1&q^k\
1&0
\end{pmatrix}
\right)
\mathbf v_0.
]

The continued fraction arises from the infinite matrix product

[
\prod_{k\ge1}
\begin{pmatrix}
1&q^k\
1&0
\end{pmatrix}.
]

This matrix viewpoint is heavily used in modern work connecting Rogers–Ramanujan theory to q-series, modular forms, transfer operators, and statistical mechanics.

In summary, the most common recurrence relation for the Rogers–Ramanujan continued fraction convergents is

[
\boxed{
X_n = X_{n-1}+q^nX_{n-2}
}
]

(with separate numerator and denominator sequences), and the infinite continued fraction is obtained as the limit of the ratios of these recursively generated polynomials.


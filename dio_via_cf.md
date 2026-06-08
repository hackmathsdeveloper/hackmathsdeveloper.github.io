
The connection between **binary quadratic forms** and **continued fractions** is one of the deepest themes in classical number theory. It was developed by Joseph-Louis Lagrange, Carl Friedrich Gauss, and later refined by Charles Hermite and others.

---

# 1. The Starting Point: Quadratic Forms

A binary quadratic form is

[
Q(x,y)=ax^2+bxy+cy^2
]

where (a,b,c) are integers.

Examples:

[
x^2+y^2
]

[
x^2-2y^2
]

[
2x^2+3xy-y^2
]

The key invariant is the discriminant

[
\Delta=b^2-4ac.
]

For example,

[
Q(x,y)=x^2-2y^2
]

has

[
a=1,\quad b=0,\quad c=-2
]

so

[
\Delta=8.
]

---

# 2. A Quadratic Form Defines a Quadratic Irrational

Given

[
ax^2+bxy+cy^2,
]

consider

[
a\left(\frac{x}{y}\right)^2
+b\left(\frac{x}{y}\right)
+c=0.
]

The roots are

[
\alpha
======

\frac{-b+\sqrt{\Delta}}{2a},
]

[
\beta
=====

\frac{-b-\sqrt{\Delta}}{2a}.
]

Thus every quadratic form naturally produces a quadratic irrational.

Example:

[
x^2-2y^2
]

gives

[
z^2-2=0
]

whose root is

[
\sqrt2.
]

---

# 3. Continued Fractions Enter

Lagrange proved:

> A real number has an eventually periodic continued fraction iff it is a quadratic irrational.

Thus

[
\sqrt2=[1;\overline2]
]

[
\sqrt3=[1;\overline1,2]
]

[
\sqrt5=[2;\overline4]
]

etc.

Every indefinite quadratic form therefore determines a periodic continued fraction.

---

# 4. Reduction of Quadratic Forms

Gauss wanted to classify forms.

Many forms are equivalent under

[
\begin{pmatrix}
x\y
\end{pmatrix}
=============

\begin{pmatrix}
p&q\
r&s
\end{pmatrix}
\begin{pmatrix}
X\Y
\end{pmatrix},
]

where

[
ps-qr=1.
]

Such transformations preserve the discriminant.

The transformed coefficients become

[
(a,b,c)\mapsto(a',b',c').
]

Gauss developed a reduction procedure to move a form into a canonical representative.

Surprisingly, this reduction process is exactly Euclid's algorithm in disguise.

---

# 5. Euclid's Algorithm Produces Continued Fractions

Recall

[
\frac{m}{n}
===========

a_0+
\frac1{a_1+
\frac1{a_2+\cdots}}
]

comes from repeated divisions:

[
m=a_0n+r_1
]

[
n=a_1r_1+r_2
]

etc.

The reduction of quadratic forms performs essentially the same repeated division process on

[
\frac{-b+\sqrt{\Delta}}{2a}.
]

Hence:

[
\text{reduction of forms}
\Longleftrightarrow
\text{continued fraction expansion}.
]

---

# 6. Example: (x^2-2y^2)

Consider

[
Q=(1,0,-2).
]

Associated irrational:

[
\alpha=\sqrt2.
]

Compute

[
\sqrt2=[1;\overline2].
]

The period length is 1.

The convergents are

[
1,
\frac32,
\frac75,
\frac{17}{12},
\frac{41}{29},
\ldots
]

These satisfy

[
p_n^2-2q_n^2=\pm1.
]

Thus the continued fraction directly generates solutions to the quadratic form equation

[
Q(x,y)=\pm1.
]

---

# 7. Reduced Forms Correspond to Periodic Cycles

Take discriminant

[
\Delta=61.
]

There are several reduced forms.

Under Gauss reduction they form a cycle:

[
Q_1
\rightarrow
Q_2
\rightarrow
Q_3
\rightarrow
\cdots
\rightarrow
Q_1.
]

Exactly the same cycle appears when expanding

[
\sqrt{61}
]

into a continued fraction.

The period of the continued fraction equals the length of the reduction cycle.

This is one of the fundamental theorems connecting the two subjects.

---

# 8. Pell's Equation

The most famous application is

[
x^2-Dy^2=1.
]

This corresponds to the form

[
(1,0,-D).
]

The root is

[
\sqrt D.
]

The continued fraction of (\sqrt D) gives the fundamental solution.

For

[
D=13,
]

[
\sqrt{13}
=========

[3;\overline{1,1,1,1,6}].
]

The convergents yield

[
649^2-13(180)^2=1.
]

Thus continued fractions solve the Diophantine equation because they arise naturally from the associated quadratic form.

---

# 9. Modern Viewpoint

Today one often describes the connection as

[
\text{Quadratic Forms}
\leftrightarrow
\text{Geodesics on Modular Surface}
\leftrightarrow
\text{Continued Fractions}
\leftrightarrow
\text{Pell Equations}
]

through the action of

[
\mathrm{SL}_2(\mathbb Z).
]

A quadratic form

[
ax^2+bxy+cy^2
]

determines a geodesic joining

[
\frac{-b\pm\sqrt{\Delta}}{2a},
]

and the cutting sequence of that geodesic is exactly the continued fraction expansion.

---

# 10. The Fundamental Correspondence

The whole theory can be summarized by

[
Q(x,y)=ax^2+bxy+cy^2
]

[
\Downarrow
]

[
\alpha=
\frac{-b+\sqrt{\Delta}}{2a}
]

[
\Downarrow
]

continued fraction of (\alpha)

[
\Downarrow
]

reduction cycle of (Q)

[
\Downarrow
]

solutions of

[
Q(x,y)=m
]

especially Pell-type equations.

This is why, historically, continued fractions became one of the primary tools for solving quadratic Diophantine equations: every indefinite quadratic form secretly carries a periodic continued fraction inside it.


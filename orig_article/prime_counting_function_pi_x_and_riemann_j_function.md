
Riemann’s (J(x)) function is one of the central analytic objects in prime number theory.

It is part of Riemann’s strategy for understanding the distribution of primes using complex analysis and the zeta function.

The basic idea is:

* (\pi(x)) counts primes
* (J(x)) is a smoother weighted counting function
* the zeta function encodes (J(x))
* zeros of (\zeta(s)) produce oscillations in prime distribution

This eventually leads to Riemann’s explicit formula.

---

# 1. Prime counting function (\pi(x))

The classical prime counting function is:

[
\pi(x)
======

#{p\le x : p\text{ prime}}
]

Example:

[
\pi(10)=4
]

because:

[
2,3,5,7
]

are primes below 10.

Visualization:

\pi(x)=#{p\le x}

---

# 2. Why (\pi(x)) is difficult

(\pi(x)) is extremely discontinuous.

It jumps by 1 whenever (x) crosses a prime.

Example:

| (x) | (\pi(x)) |
| --- | -------- |
| 10  | 4        |
| 11  | 5        |
| 12  | 5        |
| 13  | 6        |

This jagged structure is difficult to analyze analytically.

Riemann introduced smoother functions.

---

# 3. Definition of Riemann’s (J(x))

Riemann defined:

[
J(x)
====

\sum_{p^k\le x}\frac1k
]

where:

* (p) runs over primes
* (k\ge1)

Equivalently:

[
J(x)
====

\pi(x)
+\frac12\pi(x^{1/2})
+\frac13\pi(x^{1/3})
+\cdots
]

Visualization:

J(x)=\sum_{p^k\le x}\frac1k

---

# 4. What this means

Instead of counting only primes:

[
2,3,5,7,\dots
]

Riemann also counts prime powers:

[
2^2=4,\quad 2^3=8,\quad 3^2=9,\dots
]

but with weights:

[
\frac1k
]

Examples:

| Prime power | Contribution |
| ----------- | ------------ |
| (2)         | 1            |
| (2^2=4)     | (1/2)        |
| (2^3=8)     | (1/3)        |
| (3^2=9)     | (1/2)        |

---

# 5. Example computation

Take:

[
x=10
]

Prime powers below 10:

[
2,3,5,7,4,8,9
]

Contributions:

[
1+1+1+1+\frac12+\frac13+\frac12
]

Thus:

[
J(10)
=====

# 4+\frac12+\frac13+\frac12

\frac{16}{3}
]

---

# 6. Why introduce prime powers?

Because prime powers appear naturally in:

[
\log\zeta(s)
]

This is the key insight.

Euler product:

[
\zeta(s)
========

\prod_p
\frac1{1-p^{-s}}
]

Take logarithm:

[
\log\zeta(s)
============

-\sum_p\log(1-p^{-s})
]

Use:

[
-\log(1-u)
==========

\sum_{k=1}^\infty\frac{u^k}{k}
]

Then:

[
\log\zeta(s)
============

\sum_p\sum_{k=1}^\infty
\frac1k p^{-ks}
]

Visualization of Euler product logarithm:

\log\zeta(s)=\sum_p\sum_{k=1}^{\infty}\frac{1}{k}p^{-ks}

This is exactly the weighting structure of (J(x)).

---

# 7. Mellin-transform viewpoint

Riemann realized:

[
\log\zeta(s)
============

s\int_1^\infty
\frac{J(x)}{x^{s+1}}dx
]

This is essentially a Mellin transform.

Meaning:

* (J(x)) and (\zeta(s)) are dual objects
* understanding one gives information about the other

This is the birth of analytic number theory.

---

# 8. Möbius inversion recovers (\pi(x))

(J(x)) is easier analytically.

But we ultimately want (\pi(x)).

Riemann used Möbius inversion:

[
\pi(x)
======

\sum_{n=1}^\infty
\frac{\mu(n)}{n}
J(x^{1/n})
]

where:

[
\mu(n)
]

is the Möbius function.

Visualization:

\pi(x)=\sum_{n=1}^{\infty}\frac{\mu(n)}{n}J(x^{1/n})

This removes the prime-power overcounting.

---

# 9. Riemann’s explicit formula

Riemann derived a stunning formula:

[
J(x)
====

## \operatorname{Li}(x)

\sum_\rho
\operatorname{Li}(x^\rho)
+\text{corrections}
]

where:

* (\operatorname{Li}(x)) is the logarithmic integral
* (\rho) runs over nontrivial zeros of (\zeta(s))

Visualization:

J(x)=\operatorname{Li}(x)-\sum_{\rho}\operatorname{Li}(x^{\rho})+\cdots

This formula is revolutionary.

It says:

> Prime numbers are controlled by zeta zeros.

---

# 10. Why zeros matter

The main term:

[
\operatorname{Li}(x)
]

gives smooth average prime growth.

The zero terms:

[
\operatorname{Li}(x^\rho)
]

produce oscillations/errors.

Thus:

* smooth trend = logarithmic integral
* fluctuations = zeta zeros

Prime distribution becomes a harmonic-analysis problem.

---

# 11. Connection to the Riemann Hypothesis

Suppose zeros satisfy:

[
\rho=\frac12+it
]

Then:

[
x^\rho
======

# x^{1/2}x^{it}

x^{1/2}e^{it\log x}
]

These become oscillatory waves.

If RH is true:

* oscillations are optimally controlled
* prime counting error becomes minimal

Specifically:

[
\pi(x)
======

\operatorname{Li}(x)
+
O(\sqrt{x}\log x)
]

---

# 12. Why (J(x)) is analytically natural

(J(x)) emerges naturally because:

[
\log\zeta(s)
]

expands into prime powers.

The logarithm converts multiplicative Euler products into additive sums.

This is the same principle as:

[
\log(ab)=\log a+\log b
]

Thus analytic number theory often studies:

* (\log\zeta(s))
* (\zeta'(s)/\zeta(s))

rather than (\zeta(s)) directly.

---

# 13. Von Mangoldt function connection

Define:

[
\Lambda(n)
==========

\begin{cases}
\log p & n=p^k \
0 & \text{otherwise}
\end{cases}
]

Then:

[
-\frac{\zeta'(s)}{\zeta(s)}
===========================

\sum_{n=1}^\infty
\frac{\Lambda(n)}{n^s}
]

This is another encoding of prime powers.

The entire theory revolves around prime-power structures.

---

# 14. Geometric intuition

Think of:

[
\operatorname{Li}(x)
]

as the smooth “background field”.

Then each zeta zero contributes a wave:

[
x^\rho
]

The interference of infinitely many waves produces the irregular spacing of primes.

This is why primes look random yet obey deep hidden structure.

---

# 15. Historical importance

Riemann’s 1859 paper was only a few pages long, but it created:

* analytic number theory
* explicit formulas
* zero analysis
* spectral approaches to primes

Modern subjects descending from this include:

* automorphic forms
* trace formulas
* random matrix theory
* quantum chaos
* Langlands program

---

# 16. Deep structural picture

The pipeline is:

[
\text{Primes}
\rightarrow
\text{Euler product}
\rightarrow
\zeta(s)
\rightarrow
\text{complex zeros}
\rightarrow
\text{oscillations in }J(x)
\rightarrow
\pi(x)
]

Riemann’s (J(x)) is the bridge between:

* discrete arithmetic
* continuous complex analysis

That bridge is one of the deepest constructions in mathematics.


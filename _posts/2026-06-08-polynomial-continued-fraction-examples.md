---
title: "5 Worked Examples of Polynomial Continued Fractions That Will Change How You Compute Limits"
date: 2026-06-08
categories:
  - Number Theory
  - Mathematics
tags:
  - continued-fractions
  - polynomial-continued-fractions
  - convergence
  - bessel-functions
  - complex-analysis
  - pincherle-theorem
share: true
read_time: true
excerpt: "From simple integer limits to complex-valued continued fractions that evaluate to i, these five examples show how polynomial continued fractions encode exact constants — rational, irrational, and complex — within their convergent sequences."
---

**Challenge to the reader:** Before reading the examples, compute the first four convergents of $K_{n=1}^{\infty}\frac{n+1}{n}$ by hand from the bottom up, and observe the oscillation pattern. Can you guess the exact infinite limit?

---

## 1. Example 1: The Simplest Non-Trivial Case

Consider:

$$
K_{n=1}^{\infty}\frac{n+1}{n}
=
\cfrac{2}{1+\cfrac{3}{2+\cfrac{4}{3+\cdots}}}.
$$

This is the special case $\alpha=1$ of the family $K_{n=1}^{\infty}\frac{n^\alpha+1}{n^\alpha}=1$, so its value is exactly $1$.

Let us compute the first few convergents from the bottom upward to see the convergence in action:

- $C_1 = \frac{2}{1} = 2$
- $C_2 = \frac{2}{1+3/2} = \frac{4}{5} = 0.8$
- $C_3 = \frac{2}{1+\frac{3}{2+4/3}} = \frac{14}{13} \approx 1.0769$
- $C_4 = \frac{2}{1+\frac{3}{2+\frac{4}{3+5/4}}} = \frac{44}{53} \approx 0.8302$

The convergents oscillate around the limit $1$, alternately over- and under-shooting as they converge. More generally, replacing $n$ by $n^\alpha$ gives limit $1$ for every $\alpha>0$ — the convergence rate depends on $\alpha$, but the limit does not.

---

**Challenge:** Set $\alpha=2$ and compute $C_1, C_2, C_3$ for $K_{n=1}^{\infty}\frac{n^2+1}{n^2}$. Confirm that the values still oscillate around $1$.

---

## 2. Example 2: A Higher-Degree Rational Limit

Now consider a family whose numerator and denominator both have degree $2$ in $n$:

$$
K_{n=1}^{\infty}\frac{(n+1)^2 f_n+4n+5}{n^2 f_n+4n-4}=4,
$$

valid for any polynomial sequence $f_n \ge 1$. Choosing the simplest option $f_n=1$ yields:

$$
K_{n=1}^{\infty}\frac{n^2+6n+6}{n^2+4n-4}=4.
$$

Write out the first few partial quotients:

- $n=1$: $a_1=13,\; b_1=1$
- $n=2$: $a_2=22,\; b_2=8$
- $n=3$: $a_3=33,\; b_3=17$

The continued fraction begins:

$$
\cfrac{13}{1+\cfrac{22}{8+\cfrac{33}{17+\cdots}}}.
$$

Computing convergents:

- One term: $13$
- Two terms: $\frac{13}{1+22/8} = \frac{104}{30} \approx 3.4667$
- Three terms: $\frac{13}{1+\frac{22}{8+33/17}} \approx 4.189$

The sequence approaches $4$, with the third convergent already within $5\%$ of the exact limit.

## 3. Example 3: When the Limit Is Irrational — Bessel Functions Appear

Not all polynomial continued fractions yield rational limits. Consider:

$$
1-\frac{1}{1+K_{n=1}^{\infty}\frac{n^2}{n^2+2n}}=J_0(2),
$$

where $J_0$ is the Bessel function of the first kind of order $0$. Let:

$$
X=K_{n=1}^{\infty}\frac{n^2}{n^2+2n}.
$$

Then $1-\frac{1}{1+X}=J_0(2)$, and solving for $X$:

$$
X=\frac{J_0(2)}{1-J_0(2)} \approx -0.2239.
$$

Computing convergents of $X$:

- One term: $\frac{1}{3} \approx 0.3333$
- Two terms: $\frac{1}{3+4/8} = \frac{2}{7} \approx 0.2857$
- Three terms: $\frac{1}{3+\frac{4}{8+9/15}} \approx 0.2914$

The convergents creep toward the non-rational constant determined by $J_0(2)$. This example shows that polynomial continued fractions encode special-function values, not merely rational numbers.

## 4. Example 4: Complex Coefficients, Complex Limit

For a genuinely complex example, take $a=1$ and $x=i$ in the general family:

$$
K_{n=1}^{\infty}\frac{(x+na)^2-a^2}{a}=x.
$$

The numerator becomes $(i+n)^2-1 = n^2+2in-2$, with denominator $1$:

$$
K_{n=1}^{\infty}(n^2+2in-2)=i.
$$

Explicitly writing out the first few terms:

$$
\cfrac{-1+2i}{1+\cfrac{2+4i}{1+\cfrac{7+6i}{1+\cfrac{14+8i}{1+\cdots}}}} = i.
$$

The recurrence that proves this uses:

$$
G_{-1}=1,\qquad
G_n=(-1)^{n+1}\prod_{j=0}^{n}(i+j),
$$

with $a_n=(i+n-1)(i+n+1)$ and $b_n=1$. These satisfy $G_n=a_nG_{n-2}+b_nG_{n-1}$, and Pincherle's theorem then yields the limit $-G_0/G_{-1}=i$.

---

**Challenge:** Take $x=1+i$ and $a=1$ in the same family. Write out the first three partial numerators and confirm that the limit should be $1+i$.

---

## 5. Example 5: The Classical Convergent Recurrence

Every continued fraction obeys a two-term recurrence for its convergents. For a continued fraction with partial quotients $a_0, a_1, a_2, \dots$, the convergent numerators $A_n$ and denominators $B_n$ satisfy:

$$
A_n = a_n A_{n-1} + A_{n-2}, \qquad B_n = a_n B_{n-1} + B_{n-2}.
$$

For the classical simple continued fraction $[1;1,1,1,\dots]$ where every partial quotient is $1$, the recurrences become:

$$
A_n = A_{n-1} + A_{n-2}, \qquad B_n = B_{n-1} + B_{n-2},
$$

which is the Fibonacci recurrence. With initial values $A_0=1, A_{-1}=0$ and $B_0=0, B_{-1}=1$, the convergents $A_n/B_n$ are ratios of consecutive Fibonacci numbers, approaching $\frac{1+\sqrt{5}}{2}$ — the golden ratio.

This same recurrence mechanism underlies all polynomial continued fractions: once you identify a compatible auxiliary sequence $G_n$, you can read off the limit without computing any convergents.

---

| Example | Continued Fraction | Limit | Type |
|---|---|---|---|
| 1 | $K\frac{n+1}{n}$ | $1$ | Rational |
| 2 | $K\frac{n^2+6n+6}{n^2+4n-4}$ | $4$ | Rational |
| 3 | $K\frac{n^2}{n^2+2n}$ | $\frac{J_0(2)}{1-J_0(2)}$ | Irrational (Bessel) |
| 4 | $K(n^2+2in-2)$ | $i$ | Complex |
| 5 | $[1;1,1,1,\dots]$ | $\frac{1+\sqrt{5}}{2}$ | Irrational (algebraic) |

---

## 6. Deeper Significance

These examples span the full spectrum: rational limits, irrational limits involving special functions, and complex limits. The unity behind them is Pincherle's theorem: find a sequence $G_n$ satisfying $G_n = a_n G_{n-2} + b_n G_{n-1}$, check the growth condition $G_n/B_n \to 0$, and the continued fraction evaluates to $-G_0/G_{-1}$.

The recurrence viewpoint transforms continued fraction evaluation from a computational slog into an algebraic identification problem. In later posts we will develop this method in full generality and build continued fractions from scratch.

## 7. Final Challenge

**Synthesis challenge:** The family $K_{n=1}^{\infty}\frac{n^\alpha+1}{n^\alpha}=1$ works for any $\alpha>0$. For $\alpha=\frac{1}{2}$:

1. Write out the first three partial quotients explicitly as numerical fractions.
2. Compute $C_1, C_2, C_3$ numerically (to 4 decimal places).
3. Observe whether the convergence is faster or slower than the $\alpha=1$ case, and explain why.

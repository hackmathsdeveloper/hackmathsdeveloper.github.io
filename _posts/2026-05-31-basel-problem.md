---
title: "π²/6: How Euler Cracked the Sum That Stumped a Century — And 20 Ways It Secretly Appears Everywhere"
date: 2026-05-31
categories:
  - Number Theory
  - Mathematics
tags:
  - basel-problem
  - riemann-zeta
  - infinite-series
  - euler
  - fourier-series
  - harmonic-numbers
  - generating-functions
share: true
read_time: true
excerpt: "Why does 1 + 1/4 + 1/9 + 1/16 + ... equal π²/6? Euler's answer to the Basel problem is one of the most beautiful results in all of mathematics — and it spawns an entire universe of related series. From prime reciprocals to Fibonacci squares, here are 20 variations that reveal how deeply π²/6 is woven into the fabric of analysis."
---

**Challenge to the reader:** Without using a calculator or looking it up, compute $\sum_{n=1}^{\infty} \frac{1}{(2n-1)^2}$ given that $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.

---

## 1. The Classical Basel Problem

The **Basel Problem** is to evaluate

$$
\zeta(2) = \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \cdots
$$

In 1734, Leonhard Euler proved the astonishing result:

$$
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
$$

The problem had resisted the Bernoulli brothers, Leibniz, and Stirling for nearly a century. Euler's proof — using the infinite product expansion of $\sin x$ — was a stroke of genius that launched the modern theory of the Riemann zeta function.

---

## 2. Why It Matters

The appearance of $\pi$ in a sum of reciprocal integers is deeply surprising. This result:

- Launched the systematic study of $\zeta(s) = \sum_{n=1}^\infty n^{-s}$
- Connects number theory to complex analysis
- Gives exact values for $\zeta(2k)$ for all positive integers $k$
- Appears in quantum field theory, probability, and random matrix theory

---

## 3. Direct Variants

Once you know $\zeta(2) = \pi^2/6$, a family of related sums follows by elementary manipulation.

### 3.1 Even terms only

$$
\sum_{n=1}^{\infty} \frac{1}{(2n)^2} = \frac{1}{4}\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{24}
$$

**Challenge:** Derive this in your head. It takes one line.

### 3.2 Odd terms only

Subtracting the even terms from the total:

$$
\sum_{n=1}^{\infty} \frac{1}{(2n-1)^2} = \sum_{n=1}^{\infty}\frac{1}{n^2} - \sum_{n=1}^{\infty}\frac{1}{(2n)^2} = \frac{\pi^2}{6} - \frac{\pi^2}{24} = \frac{\pi^2}{8}
$$

### 3.3 Alternating series

The alternating sum yields a smaller multiple of $\pi^2$:

$$
\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2} = \frac{\pi^2}{12}
$$

This follows from splitting even and odd terms with signs: $\eta(2) = (1 - 2^{1-2})\zeta(2) = \frac{1}{2}\zeta(2)$.

---

## 4. Higher Powers: $\zeta(2k)$

Euler went further and computed $\zeta(2k)$ for all positive integers $k$ in terms of Bernoulli numbers:

$$
\zeta(2k) = \frac{(-1)^{k+1} B_{2k} (2\pi)^{2k}}{2(2k)!}
$$

### 4.1 $\zeta(4)$

$$
\sum_{n=1}^{\infty} \frac{1}{n^4} = \frac{\pi^4}{90}
$$

### 4.2 $\zeta(6)$

$$
\sum_{n=1}^{\infty} \frac{1}{n^6} = \frac{\pi^6}{945}
$$

### 4.3 General even argument

For any positive integer $k$, $\zeta(2k)$ is a rational multiple of $\pi^{2k}$. The rational coefficients involve the Bernoulli numbers $B_{2k}$, which grow super-exponentially — yet the resulting sum is always a rational number times the appropriate power of $\pi$.

**Challenge:** Compute $\zeta(8)$ using the Bernoulli number $B_8 = -1/30$. You should get $\pi^8/9450$.

---

## 5. Restricted-Index Variants

What happens when we sum only over primes, triangular numbers, or Fibonacci numbers?

### 5.1 Sum over primes

$$
\sum_{p \text{ prime}} \frac{1}{p^2} \approx 0.4522474200\ldots
$$

This is the *prime zeta function* at $s=2$. Unlike $\zeta(2)$, it has no known closed form in terms of familiar constants. Its value can be expressed using the Möbius inversion formula:

$$
P(2) = \sum_{k=1}^{\infty} \frac{\mu(k)}{k} \log \zeta(2k)
$$

### 5.2 Arithmetic progression

For fixed integers $a, b$ (with no zero denominator):

$$
\sum_{n=1}^{\infty} \frac{1}{(an+b)^2}
$$

can be expressed using the **Hurwitz zeta function** $\zeta(2, b/a)$, or equivalently in terms of the **digamma function** (trigamma, specifically).

### 5.3 Triangular numbers

Let $T_n = \frac{n(n+1)}{2}$ be the $n$-th triangular number. Then:

$$
\sum_{n=1}^{\infty} \frac{1}{T_n^2} = 4\sum_{n=1}^{\infty} \frac{1}{n^2(n+1)^2}
$$

This can be evaluated exactly using partial fractions and telescoping, yielding a rational combination of $\pi^2$ and rational numbers.

### 5.4 Fibonacci reciprocals

$$
\sum_{n=1}^{\infty} \frac{1}{F_n^2}
$$

where $F_n$ is the $n$-th Fibonacci number. This sum converges rapidly (the Fibonacci numbers grow exponentially), but it is not known to have a simple closed form. It is related to the *reciprocal Fibonacci constant* and the theory of $q$-series.

---

## 6. Harmonic-Mixed Variants

Sums involving harmonic numbers $H_n = \sum_{k=1}^n \frac{1}{k}$ produce *Euler sums* or *multiple zeta values*. These were studied extensively by Euler and are connected to deep algebraic structures.

### 6.1 Linear Euler sum

$$
\sum_{n=1}^{\infty} \frac{H_n}{n^2} = 2\zeta(3)
$$

This is a celebrated result: the sum of $H_n/n^2$ evaluates to *twice Apéry's constant*.

### 6.2 Generalized harmonic numbers

Let $H_n^{(2)} = \sum_{k=1}^n \frac{1}{k^2}$. Then:

$$
\sum_{n=1}^{\infty} \frac{H_n^{(2)}}{n^2} = \frac{7}{4}\zeta(4) = \frac{7\pi^4}{360}
$$

### 6.3 Higher-weight Euler sum

$$
\sum_{n=1}^{\infty} \frac{H_n}{n^3} = \frac{5}{4}\zeta(4) = \frac{\pi^4}{72}
$$

### 6.4 Alternating harmonic sum

$$
\sum_{n=1}^{\infty} \frac{(-1)^{n-1} H_n}{n^2}
$$

This is an alternating Euler sum that evaluates to a combination of $\zeta(3)$ and products of $\zeta(2)$ with $\log 2$, involving the trilogarithm $\operatorname{Li}_3(1/2)$.

---

## 7. Function-Based Derivations

The original Basel sum can be derived through multiple independent routes — each illuminating a different mathematical structure.

### 7.1 Infinite product for sine

Euler's original approach: equate the power series and infinite product for $\sin x$:

$$
\frac{\sin x}{x} = \prod_{n=1}^{\infty} \left(1 - \frac{x^2}{n^2 \pi^2}\right)
$$

Expanding both sides and comparing the coefficient of $x^2$ yields $\zeta(2) = \pi^2/6$.

### 7.2 Fourier series / Parseval

Expand $f(x) = x$ or $f(x) = x^2$ on $[-\pi, \pi]$ as a Fourier series and apply Parseval's identity:

$$
\frac{1}{\pi}\int_{-\pi}^{\pi} |f(x)|^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty} (a_n^2 + b_n^2)
$$

For $f(x) = x$, the coefficients are $b_n = 2(-1)^{n+1}/n$, and Parseval gives:

$$
\frac{2\pi^2}{3} = \sum_{n=1}^{\infty} \frac{4}{n^2} \quad\Longrightarrow\quad \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
$$

**Challenge:** Repeat this derivation using $f(x) = x^2$ on $[-\pi, \pi]$ and confirm you get the same result.

### 7.3 Parameter-dependent sum

For real $x > 0$:

$$
\sum_{n=1}^{\infty} \frac{1}{n^2 + x^2} = \frac{\pi}{2x}\coth(\pi x) - \frac{1}{2x^2}
$$

Taking the limit $x \to 0^+$ recovers $\zeta(2) = \pi^2/6$ via the Laurent expansion of $\coth$.

---

## 8. Multidimensional and Parameter Variants

### 8.1 The Riemann zeta function

Study the analytic continuation of:

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}, \quad \Re(s) > 1
$$

At $s = 2$ we have the Basel result. At $s = 3$, Apéry proved in 1978 that $\zeta(3)$ is irrational — but no simple closed form in terms of $\pi^3$ exists. At $s = 4$, we get $\pi^4/90$. The pattern breaks: odd positive integers $s = 3, 5, 7, \ldots$ have no known closed form.

### 8.2 Double sum

Does the double sum converge?

$$
\sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{1}{(m+n)^2}
$$

Let $k = m+n$. The number of pairs $(m,n)$ with $m,n \ge 1$ and $m+n = k$ is $k-1$. So:

$$
\sum_{m,n \ge 1} \frac{1}{(m+n)^2} = \sum_{k=2}^{\infty} \frac{k-1}{k^2} = \sum_{k=2}^{\infty} \left(\frac{1}{k} - \frac{1}{k^2}\right)
$$

The harmonic series $\sum 1/k$ diverges, so the double sum **diverges** — despite each individual sum over $m$ or $n$ converging.

---

## 9. Deeper Significance

The Basel problem is far more than a single sum. It teaches us:

- **Generating functions** encode combinatorial structure in analytic form
- **Symmetry** (even vs. odd, alternating signs) partitions infinite series into algebraic families
- **Special values** of $L$-functions at integer arguments are the key to deep arithmetic
- **Multiple zeta values** form a graded algebra with rich relations — Euler sums are its weight-2 and weight-3 entries

The fact that $\zeta(2) = \pi^2/6$ is the tip of an iceberg that leads directly to the Riemann hypothesis, modular forms, and the Langlands program.

---

## 10. Quick Reference: All 20 Variants

| # | Series | Value / Status |
|---|--------|---------------|
| 1 | $\sum 1/(2n)^2$ | $\pi^2/24$ |
| 2 | $\sum 1/(2n-1)^2$ | $\pi^2/8$ |
| 3 | $\sum (-1)^{n-1}/n^2$ | $\pi^2/12$ |
| 4 | $\sum 1/n^4$ | $\pi^4/90$ |
| 5 | $\sum 1/n^6$ | $\pi^6/945$ |
| 6 | $\sum 1/n^{2k}$ | $(-1)^{k+1} B_{2k} (2\pi)^{2k} / (2(2k)!)$ |
| 7 | $\sum_{p} 1/p^2$ | No simple closed form |
| 8 | $\sum 1/(an+b)^2$ | Hurwitz zeta / trigamma |
| 9 | $\sum 1/T_n^2$ | Closed form in $\pi^2$ + rational |
| 10 | $\sum 1/F_n^2$ | No known closed form |
| 11 | $\sum H_n/n^2$ | $2\zeta(3)$ |
| 12 | $\sum H_n^{(2)}/n^2$ | $7\pi^4/360$ |
| 13 | $\sum H_n/n^3$ | $\pi^4/72$ |
| 14 | $\sum (-1)^{n-1} H_n/n^2$ | $\operatorname{Li}_3(1/2)$ combination |
| 15 | Sine product proof | Euler, 1734 |
| 16 | Fourier/Parseval proof | Standard textbook |
| 17 | Fourier expansion of $x^2$ | Yields $\zeta(2)$ |
| 18 | $\sum 1/(n^2+x^2)$ | $\frac{\pi}{2x}\coth\pi x - \frac{1}{2x^2}$ |
| 19 | $\zeta(s)$ at nearby $s$ | $\zeta(2)=\pi^2/6$, $\zeta(3)$ irrational, $\zeta(4)=\pi^4/90$ |
| 20 | $\sum_{m,n} 1/(m+n)^2$ | Diverges |

---

**Final Challenge:** Euler's formula for $\zeta(2k)$ involves Bernoulli numbers. Compute $B_2$, $B_4$, $B_6$, and $B_8$, then verify the formula gives the correct values for $\zeta(2)$, $\zeta(4)$, $\zeta(6)$, and $\zeta(8)$. Then explain why the formula only works for *even* positive integers — what goes wrong at $s = 3$?

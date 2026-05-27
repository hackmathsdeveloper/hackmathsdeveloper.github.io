---
title: "Newton's Secret: How the Binomial Theorem Escaped the Integers and Took Over Calculus"
date: 2026-05-27
categories:
  - Combinatorics
  - Mathematics
tags:
  - binomial-theorem
  - negative-binomial
  - generating-functions
  - hypergeometric-function
  - combinatorics
  - newton
share: true
read_time: true
excerpt: "You learned (1+x)ⁿ expands into n+1 terms. But Newton asked: what if n is negative? Or a fraction? His answer — an infinite series with binomial coefficients built from Pochhammer symbols — unlocked generating functions, hypergeometric identities, and the deep link between combinatorics and complex analysis. This post derives the negative binomial series (1+z)⁻ⁿ = Σ (−1)ᵏ C(n+k−1,k) zᵏ and shows why those coefficients count stars-and-bars combinations."
---

**Challenge to the reader:** Expand $(1+z)^{-1/2}$ as a power series. Then use that result to compute the Taylor series of $\frac{1}{\sqrt{1+z}}$ around $z=0$ up to $z^4$. What do the coefficients have to do with the central binomial coefficients $\binom{2k}{k}$?

---

This is the **negative binomial series expansion** (also called the generalized binomial theorem for negative integer exponents):

$$
(1+z)^{-n} = \sum_{k=0}^{\infty} (-1)^k \binom{n+k-1}{k} z^k
$$

It is a special case of the generalized binomial theorem.

---

## 1. What the series means

It expands the rational function $\frac{1}{(1+z)^n}$ into an infinite power series around $z=0$.

For example, when $n=1$:

$$
\frac1{1+z} = 1-z+z^2-z^3+\cdots
$$

When $n=2$:

$$
\frac1{(1+z)^2} = 1-2z+3z^2-4z^3+\cdots
$$

When $n=3$:

$$
\frac1{(1+z)^3} = 1-3z+6z^2-10z^3+\cdots
$$

The coefficients are combinatorial numbers: $\binom{n+k-1}{k}$.

---

## 2. Origin: generalized binomial theorem

The ordinary binomial theorem says:

$$
(1+x)^m = \sum_{k=0}^{m} \binom{m}{k}x^k
$$

for integer $m\ge 0$.

But Newton generalized this to arbitrary exponents:

$$
(1+x)^\alpha = \sum_{k=0}^{\infty} \binom{\alpha}{k}x^k
$$

where:

$$
\binom{\alpha}{k} = \frac{ \alpha(\alpha-1)(\alpha-2)\cdots(\alpha-k+1) }{ k! }
$$

Now set $\alpha=-n$. Then:

$$
(1+z)^{-n} = \sum_{k=0}^{\infty} \binom{-n}{k}z^k
$$

The entire derivation reduces to simplifying $\binom{-n}{k}$.

---

## 3. Deriving the coefficient

Start from:

$$
\binom{-n}{k} = \frac{ (-n)(-n-1)(-n-2)\cdots(-n-k+1) }{ k! }
$$

Factor out $(-1)^k$:

$$
(-1)^k \frac{ n(n+1)(n+2)\cdots(n+k-1) }{ k! }
$$

Now rewrite numerator:

$$
n(n+1)\cdots(n+k-1) = \frac{(n+k-1)!}{(n-1)!}
$$

Thus:

$$
\binom{-n}{k} = (-1)^k \frac{(n+k-1)!}{(n-1)!k!}
$$

Recognize the binomial coefficient:

$$
\frac{(n+k-1)!}{(n-1)!k!} = \binom{n+k-1}{k}
$$

Therefore:

$$
\boxed{ \binom{-n}{k} = (-1)^k \binom{n+k-1}{k} }
$$

Substitute back:

$$
\boxed{ (1+z)^{-n} = \sum_{k=0}^{\infty} (-1)^k \binom{n+k-1}{k} z^k }
$$

---

## 4. Radius of convergence

This converges for $\lvert z \rvert < 1$, because the nearest singularity is at $1+z=0 \Rightarrow z=-1$, distance 1 from the origin.

---

## 5. Alternative derivation using geometric series

Start with:

$$
\frac1{1+z} = \sum_{k=0}^{\infty}(-z)^k
$$

Then differentiate repeatedly. Example:

$$
\frac1{(1+z)^2} = \frac{d}{dz}\left(-\frac1{1+z}\right)
$$

Applying derivatives generates factorial/binomial coefficients. This eventually yields the same formula.

---

## 6. Combinatorial interpretation

The coefficient $\binom{n+k-1}{k}$ counts combinations with repetition:

* placing $k$ identical balls into $n$ boxes
* stars-and-bars combinatorics

This is why the series is called the **negative binomial series**. It is deeply connected to:

* negative binomial distribution
* generating functions
* combinatorics
* analytic continuation

---

## 7. Connection to generating functions

This series is the generating function for $\binom{n+k-1}{k}$. Specifically:

$$
\sum_{k=0}^\infty \binom{n+k-1}{k}x^k = \frac1{(1-x)^n}
$$

Replacing $x\to -z$:

$$
\frac1{(1+z)^n} = \sum_{k=0}^\infty (-1)^k \binom{n+k-1}{k}z^k
$$

---

## 8. Low-level algebraic structure

Observe the coefficient $a_k = (-1)^k\binom{n+k-1}{k}$ satisfies:

$$
a_{k+1} = -\frac{n+k}{k+1}a_k
$$

This comes directly from the hypergeometric structure:

$$
(1+z)^{-n} = {}_2F_1(n,1;1;-z)
$$

and the coefficients are hypergeometric ratios.

---

**Challenge to the reader:** Prove the coefficient recurrence $a_{k+1} = -\frac{n+k}{k+1}a_k$ directly from the definition of $\binom{n+k-1}{k}$ without appealing to hypergeometric theory.

---

## 9. Hypergeometric viewpoint

The series can be written as:

$$
(1+z)^{-n} = {}_1F_0(n;;-z)
$$

with coefficient ratio:

$$
\frac{a_{k+1}}{a_k} = -\frac{n+k}{k+1}z
$$

This is why these coefficients naturally appear in:

* differential equations
* Feynman integrals
* asymptotic analysis
* analytic combinatorics

---

## 10. Compact derivation

The cleanest derivation is:

1. Start with $(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k}x^k$ (Newton)
2. Set $\alpha=-n$
3. Use $\binom{-n}{k} = (-1)^k\binom{n+k-1}{k}$

giving:

$$
\boxed{ (1+z)^{-n} = \sum_{k=0}^{\infty} (-1)^k \binom{n+k-1}{k}z^k }
$$

---

**Final challenge:** Use the negative binomial series to compute $\frac{1}{(1-z)^3}$ and verify that the coefficient of $z^k$ is the $(k+1)$-th triangular number, $\frac{(k+1)(k+2)}{2}$. Then generalize: what shape numbers appear in the expansion of $\frac{1}{(1-z)^n}$?

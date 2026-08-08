---
title: "Why GCD × LCM = ab Is Only the Beginning — The Hidden Structure That Controls All Divisibility"
date: 2026-08-08
categories:
  - Number Theory
  - Mathematics
tags:
  - gcd
  - lcm
  - number-theory
  - coprimality
  - prime-factorization
  - euclidean-algorithm
  - divisibility
  - bezout-identity
share: true
read_time: true
excerpt: "The product identity gcd·lcm = ab is only the surface. Underneath lies a lattice of divisibility where gcd is meet and lcm is join, prime exponents run the show, and coprimality becomes geometric visibility. From Bézout to the Chinese Remainder Theorem, discover the hidden structure that unifies them all."
---

**Challenge to the reader:** Given $a = 360$ and $b = 525$, compute $\gcd(a,b)$ and $\operatorname{lcm}(a,b)$ using the Euclidean algorithm. Then verify that $\gcd(a,b) \times \operatorname{lcm}(a,b) = a \times b$. Finally, express both numbers in prime factorization and confirm the min/max exponent rule. Solve this before reading on — the rest of the post gives you the tools.

---

## 1. The Core Identity

For any positive integers $a, b$, the most famous relationship between gcd and lcm is:

$$
\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab.
$$

But this identity is only the surface. The full story involves prime exponents, lattice meet/join operations, and invariants that survive repeated transformations.

Let $d = \gcd(a,b)$. Write $a = dx$ and $b = dy$, where $\gcd(x,y) = 1$. Then $\operatorname{lcm}(a,b) = dxy$, because the common factor is exactly $d$ and the remaining parts are coprime. Hence

$$
\gcd(a,b)\operatorname{lcm}(a,b) = d \cdot dxy = d^2 xy = ab.
$$

From this single identity, several corollaries follow immediately:

- $\gcd(a,b) \mid a$ and $\gcd(a,b) \mid b$.
- $a \mid \operatorname{lcm}(a,b)$ and $b \mid \operatorname{lcm}(a,b)$.
- $\gcd(a,b) \le \min(a,b)$ and $\operatorname{lcm}(a,b) \ge \max(a,b)$.
- $\gcd(a,b) = a$ if and only if $a \mid b$.
- $\operatorname{lcm}(a,b) = a$ if and only if $b \mid a$.

---

## 2. Three Proofs of the Product Identity

Why should you believe $\gcd(a,b)\operatorname{lcm}(a,b) = ab$? Here are three independent proofs — each reveals a different facet of the structure.

### Proof 1: Via Prime Factorization

Write

$$
a = \prod_p p^{\alpha_p}, \qquad b = \prod_p p^{\beta_p}.
$$

Then

$$
\gcd(a,b) = \prod_p p^{\min(\alpha_p,\beta_p)}, \qquad
\operatorname{lcm}(a,b) = \prod_p p^{\max(\alpha_p,\beta_p)}.
$$

Multiplying gives

$$
\prod_p p^{\min(\alpha_p,\beta_p) + \max(\alpha_p,\beta_p)}
= \prod_p p^{\alpha_p + \beta_p} = ab.
$$

The key identity: for any two numbers, $\min(u,v) + \max(u,v) = u + v$.

### Proof 2: Via Coprime Reduction

Let $d = \gcd(a,b)$, so $a = dx$, $b = dy$, with $\gcd(x,y) = 1$.

Because $x$ and $y$ are coprime, $\operatorname{lcm}(x,y) = xy$. Therefore

$$
\operatorname{lcm}(a,b) = d \cdot \operatorname{lcm}(x,y) = dxy,
$$

and thus

$$
\gcd(a,b)\operatorname{lcm}(a,b) = d(dxy) = ab.
$$

This proof shows that the identity reduces to the coprime case $\operatorname{lcm}(x,y) = xy$, which is the conceptually cleanest situation.

### Proof 3: Via the Divisibility Lattice

In the divisibility lattice of positive integers, $\gcd$ is the meet and $\operatorname{lcm}$ is the join. Prime exponents turn this lattice into coordinatewise min/max on exponent vectors. Since for each coordinate

$$
\min(u,v) + \max(u,v) = u + v,
$$

multiplying over all primes yields the identity.

This viewpoint generalizes beyond integers to any lattice with a product structure.

---

## 3. Prime Factorization: The Min/Max Picture

The prime factorization viewpoint is arguably the most powerful way to understand gcd and lcm. Write

$$
a = \prod_p p^{\alpha_p}, \qquad b = \prod_p p^{\beta_p}.
$$

Then:

- $\gcd(a,b)$ takes the **minimum** exponent of each prime.
- $\operatorname{lcm}(a,b)$ takes the **maximum** exponent of each prime.

This means:

> **$\gcd$ keeps the *common part*; $\operatorname{lcm}$ takes the *combined coverage*.**

A concrete example: $a = 12 = 2^2 \cdot 3$ and $b = 18 = 2 \cdot 3^2$.

$$
\gcd(12,18) = 2^{\min(2,1)} \cdot 3^{\min(1,2)} = 2^1 \cdot 3^1 = 6,
$$

$$
\operatorname{lcm}(12,18) = 2^{\max(2,1)} \cdot 3^{\max(1,2)} = 2^2 \cdot 3^2 = 36.
$$

And indeed: $12 \cdot 18 = 216 = 6 \cdot 36$.

**Challenge:** Without a calculator, compute $\gcd(84, 350)$ and $\operatorname{lcm}(84, 350)$ using the prime exponent method. Hint: $84 = 2^2 \cdot 3 \cdot 7$, $350 = 2 \cdot 5^2 \cdot 7$.

---

## 4. Ten Essential Properties

Here are ten fundamental properties that every number theorist should know:

**1. Divisibility order.**
$$
\gcd(a,b) \mid a,\; \gcd(a,b) \mid b, \qquad a \mid \operatorname{lcm}(a,b),\; b \mid \operatorname{lcm}(a,b).
$$

**2. Maximality/minimality.**
$\gcd(a,b)$ is the **largest** integer dividing both $a$ and $b$, while $\operatorname{lcm}(a,b)$ is the **smallest** integer divisible by both.

**3. Coprime criterion.**
$$
\gcd(a,b) = 1 \iff \operatorname{lcm}(a,b) = ab.
$$

**4. Equality criterion.**
$$
\gcd(a,b) = a \iff a \mid b, \qquad \operatorname{lcm}(a,b) = a \iff b \mid a.
$$

**5. Bounds.**
$$
\gcd(a,b) \le \min(a,b), \qquad \operatorname{lcm}(a,b) \ge \max(a,b).
$$

**6. Product relation.**
$$
\gcd(a,b)\operatorname{lcm}(a,b) = ab.
$$

**7. Prime-power behavior.**
If $a = p^\alpha$ and $b = p^\beta$, then
$$
\gcd(a,b) = p^{\min(\alpha,\beta)}, \qquad \operatorname{lcm}(a,b) = p^{\max(\alpha,\beta)}.
$$

**8. Scaling law.**
For any positive integer $k$,
$$
\gcd(ka,kb) = k\gcd(a,b), \qquad \operatorname{lcm}(ka,kb) = k\operatorname{lcm}(a,b).
$$

**9. Absorption identities.**
$$
\gcd(a,\operatorname{lcm}(a,b)) = a, \qquad \operatorname{lcm}(a,\gcd(a,b)) = a.
$$

**10. Monotonicity under divisibility.**
If $a \mid c$ and $b \mid d$, then
$$
\gcd(a,b) \mid \gcd(c,d), \qquad \operatorname{lcm}(a,b) \mid \operatorname{lcm}(c,d).
$$

---

## 5. Less Obvious Properties

Beyond the basics, gcd and lcm exhibit deeper algebraic and lattice-theoretic behaviour. Here are some that reward deeper study:

**Associativity over many numbers.**
$$
\gcd(a_1,\dots,a_n) = \gcd(\gcd(a_1,\dots,a_{n-1}), a_n),
$$
$$
\operatorname{lcm}(a_1,\dots,a_n) = \operatorname{lcm}(\operatorname{lcm}(a_1,\dots,a_{n-1}), a_n).
$$

**Order independence.** Reordering inputs does not change either operation.

**GCD of linear combinations.**
$$
\gcd(a,b) = \gcd(a, b+ka) = \gcd(a+kb, b)
$$
for every integer $k$. This is the basis of the Euclidean algorithm.

**Distributive laws (lattice meet/join).**
$$
\gcd(a, \operatorname{lcm}(b,c)) = \operatorname{lcm}(\gcd(a,b), \gcd(a,c)),
$$
$$
\operatorname{lcm}(a, \gcd(b,c)) = \gcd(\operatorname{lcm}(a,b), \operatorname{lcm}(a,c)).
$$
These are precisely the distributive laws in the divisibility lattice. They mirror the set-theoretic identities $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.

**Symmetric extreme behavior.**
$$
\gcd(a,b) = 1 \iff \operatorname{lcm}(a,b) = ab,
$$
and
$$
\operatorname{lcm}(a,b) = \max(a,b) \iff a \mid b \text{ or } b \mid a.
$$

**Coprime factorization.** If $a = dx$, $b = dy$ with $\gcd(x,y) = 1$, then $\gcd(a,b) = d$ and $\operatorname{lcm}(a,b) = dxy$.

**Common divisor/multiple characterization.** Every common divisor of $a,b$ divides $\gcd(a,b)$, and $\operatorname{lcm}(a,b)$ divides every common multiple of $a,b$.

**Iteration stabilizes quickly.**
$$
\gcd(a, \gcd(a,b)) = \gcd(a,b), \qquad \operatorname{lcm}(a, \operatorname{lcm}(a,b)) = \operatorname{lcm}(a,b).
$$

**Set-theoretic analogy.** The pair $(\gcd, \operatorname{lcm})$ behaves like $(\cap, \cup)$: meet/join, intersection/union, minimum/maximum. The identity $\gcd(a,b)\operatorname{lcm}(a,b) = ab$ resembles

$$
\lvert A \rvert + \lvert B \rvert = \lvert A \cap B \rvert + \lvert A \cup B \rvert.
$$

**Uniqueness from universal properties.** $\gcd(a,b)$ is uniquely determined as the **greatest** element dividing both; $\operatorname{lcm}(a,b)$ is the **least** element divisible by both. This universal characterization is independent of prime factorization.

---

## 6. Comparison Table

| Property | $\gcd(a,b)$ | $\operatorname{lcm}(a,b)$ |
|---|---|---|
| Definition | Greatest common divisor | Least common multiple |
| Divisibility | Divides both $a$ and $b$ | Is divisible by both $a$ and $b$ |
| Size | At most both numbers | At least both numbers |
| Prime exponents | Takes $\min$ of exponents | Takes $\max$ of exponents |
| Symmetry | $\gcd(a,b) = \gcd(b,a)$ | $\operatorname{lcm}(a,b) = \operatorname{lcm}(b,a)$ |
| Coprime case | Equals $1$ | Equals $ab$ |
| Relation | $\gcd(a,b)\operatorname{lcm}(a,b) = ab$ | Same identity |
| Absorption | $\gcd(a,\operatorname{lcm}(a,b)) = a$ | $\operatorname{lcm}(a,\gcd(a,b)) = a$ |
| Computation | Euclidean algorithm | Usually via $ab/\gcd(a,b)$ |

---

## 7. An Invariant Process: The Confucius Problem

Here is a problem that beautifully illustrates the interplay between gcd and lcm as invariants. (The name is whimsical, but the structure is deep.)

Start with $2026$ positive integers, each greater than $1$. At each step, choose two numbers $m, n$ and replace them with:

$$
\gcd(m,n), \qquad \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.
$$

Repeat. What happens?

**Key idea.** Write each number in prime factorization:

$$
a_i = \prod_p p^{e_{i,p}}.
$$

For a chosen pair $m, n$, the two replacement numbers are:

$$
\gcd(m,n) = \prod_p p^{\min(e_p(m),\, e_p(n))},
$$

$$
\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)} = \prod_p p^{\lvert e_p(m) - e_p(n) \rvert}.
$$

So for each prime $p$, if its exponents in the two chosen numbers are $x$ and $y$, they are replaced by

$$
\min(x,y), \quad \lvert x - y \rvert.
$$

**Why the process ends.** For each prime $p$, the **maximum exponent** across all numbers is preserved:

$$
\max(x, y) = \max(\min(x,y),\; \lvert x - y \rvert).
$$

Repeatedly applying this operation concentrates each prime's exponent into fewer and fewer numbers, until eventually exactly one number contains all the maximum exponents and all others reduce to $1$.

**The final value.** For each prime $p$, let

$$
E_p = \max_i e_{i,p}.
$$

This maximum is invariant throughout the process. Hence the sole surviving number greater than $1$ must be

$$
M = \prod_p p^{E_p} = \operatorname{lcm}(a_1, a_2, \dots, a_{2026}).
$$

**Conclusion:**
- After finitely many moves, exactly one integer greater than $1$ remains.
- That integer is **independent** of the choices made at each step.
- It equals the least common multiple of the original $2026$ integers.

**Challenge:** Start with the numbers $6, 10, 15$. Apply the replacement rule repeatedly. Verify that the final non-$1$ number is $\operatorname{lcm}(6,10,15)$. Try a different sequence of pair choices — does the final number change?

---

## 8. Coprimality: When GCD = 1

Coprimality — the condition $\gcd(a,b) = 1$ — is arguably even more important than gcd itself. Here is a compact guide to the patterns and techniques surrounding it.

### Pattern A: Consecutive integers are always coprime

$$
\gcd(n, n+1) = 1.
$$

Proof: any common divisor of $n$ and $n+1$ divides their difference, which is $1$.

### Pattern B: Prime factors decide everything

Two numbers are coprime exactly when their prime factorizations share no prime. For example, $21 = 3 \cdot 7$ and $22 = 2 \cdot 11$, so $\gcd(21,22) = 1$.

### Pattern C: Setwise vs. pairwise coprime

- **Setwise coprime**: $\gcd(a_1, \dots, a_k) = 1$.
- **Pairwise coprime**: every pair has gcd $1$.

These are not equivalent. The classic example: $(6, 10, 15)$ has $\gcd(6,10,15) = 1$ (setwise coprime), but $\gcd(6,10) = 2$, $\gcd(6,15) = 3$, $\gcd(10,15) = 5$ (not pairwise coprime).

### Pattern D: Recursive construction of pairwise coprime families

$$
a_{n+1} = a_1 a_2 \cdots a_n + 1.
$$

Then $a_{n+1}$ is coprime to each earlier term. Example: start with $2, 3$, then

$$
2 \cdot 3 + 1 = 7, \quad 2 \cdot 3 \cdot 7 + 1 = 43, \quad \dots
$$

So $2, 3, 7, 43, \dots$ are pairwise coprime. Note: the resulting number need not be prime — the point is coprimality.

---

### Four Techniques for Testing Coprimality

**Technique 1: Euclidean algorithm.**

$$
\gcd(a,b) = \gcd(b, a \bmod b).
$$

Keep reducing until you reach $1$ (coprime) or a larger divisor (not coprime). Example:

$$
\begin{aligned}
\gcd(1071, 462) &= \gcd(462, 1071 \bmod 462 = 147) \\
&= \gcd(147, 462 \bmod 147 = 21) \\
&= \gcd(21, 147 \bmod 21 = 0) = 21. \quad \text{(not coprime)}
\end{aligned}
$$

**Technique 2: Bézout identity.**
$$
\gcd(a,b) = 1 \iff \exists\, x,y \in \mathbb Z \text{ such that } ax + by = 1.
$$

Example: $8 \cdot 2 + 15 \cdot (-1) = 1$, so $\gcd(8,15) = 1$.

**Technique 3: Modular inverses.**
If $\gcd(a,n) = 1$, then $a$ has a multiplicative inverse modulo $n$. Example: $3^{-1} \pmod 7 = 5$, because $3 \cdot 5 = 15 \equiv 1 \pmod 7$.

**Technique 4: Prime-support reasoning.**
Instead of factoring completely, identify the forbidden primes. For example, any number built only from primes other than $2, 3, 5$ is coprime to $2^4 \cdot 3^2 \cdot 5$. So $77 = 7 \cdot 11$ is coprime to $720$.

---

### Why Coprimality Matters

- **Multiplicative functions behave nicely.** If $\gcd(a,b) = 1$, then $\varphi(ab) = \varphi(a)\varphi(b)$ and similarly for other arithmetic functions.
- **Geometric visibility.** A lattice point $(a,b)$ is visible from the origin if and only if $\gcd(a,b) = 1$.
- **Chinese Remainder Theorem.** If moduli are pairwise coprime, there is a unique combined solution modulo the product. For example, the system

$$
x \equiv 2 \pmod 3,\quad x \equiv 3 \pmod 5,\quad x \equiv 2 \pmod 7
$$

has a unique solution modulo $105$ because $3, 5, 7$ are pairwise coprime.

- **Euclid's lemma.** If $\gcd(a,b) = 1$ and $a \mid bc$, then $a \mid c$. This is one of the most used lemmas in number theory.

---

## 9. The Picture That Unifies Everything

There are several complementary ways to understand the $\gcd$/$\operatorname{lcm}$ duality:

| Viewpoint | $\gcd$ | $\operatorname{lcm}$ |
|---|---|---|
| **Prime exponents** | Coordinatewise $\min$ | Coordinatewise $\max$ |
| **Set theory** | Intersection $\cap$ | Union $\cup$ |
| **Divisibility lattice** | Meet $\wedge$ | Join $\vee$ |
| **Computation** | Euclidean algorithm ($O(\log \min(a,b))$) | Via $ab/\gcd(a,b)$ |
| **Coprime case** | Equals $1$ | Equals $ab$ |

The identity $\gcd(a,b)\operatorname{lcm}(a,b) = ab$ is not a coincidence — it is a manifestation of the fact that, at the level of prime exponents, $\min(u,v) + \max(u,v) = u + v$. Every other property flows from this one algebraic fact.

The invariant process from [Section 7] illustrates this dramatically: the operation $(x,y) \mapsto (\min(x,y), \lvert x - y \rvert)$ preserves the maximum exponent for each prime, which forces the final survivor to be the lcm. The process is a kind of "exponent sorting" — it gradually concentrates extreme values at the expense of intermediate ones, until only the extremes remain.

Coprimality then emerges naturally as the case where the $\min$ is zero for every prime — the two numbers have disjoint prime support, so their product and lcm coincide.

**Challenge:** Prove that $\gcd(a, \operatorname{lcm}(b,c)) = \operatorname{lcm}(\gcd(a,b), \gcd(a,c))$ by expressing $a, b, c$ in terms of prime exponents and reducing to the identity $\min(x, \max(y,z)) = \max(\min(x,y), \min(x,z))$.

---

## 10. Deeper Significance

The $\gcd$/$\operatorname{lcm}$ pair is not just a trick for simplifying fractions — it is a gateway to understanding divisibility as a *structure*. The integers under divisibility form a distributive lattice, and $\gcd$/$\operatorname{lcm}$ are the meet and join operations. This lattice structure generalizes:

- To **ideals** in ring theory, where $\gcd$ becomes ideal sum and $\operatorname{lcm}$ becomes ideal intersection.
- To **principal ideal domains**, where every ideal is generated by a single element and the gcd/lcm correspondence is exact.
- To **order theory**, where meet-semilattices and join-semilattices model many natural "common part / combined coverage" dualities.

Every time you compute a gcd, you are not just finding a number — you are computing the **greatest lower bound** in a partially ordered set. Every lcm is a **least upper bound**. The product identity is the numerical shadow of a far more general structural fact.

---

**Final challenge:** Consider $N$ integers, each greater than $1$. At each step, pick any two numbers and replace them with $\gcd(m,n)$ and $\operatorname{lcm}(m,n)/\gcd(m,n)$. Prove that:

1. The process always terminates with exactly one number greater than $1$.
2. That number equals $\operatorname{lcm}(a_1, \dots, a_N)$, independent of all intermediate choices.
3. The product of all $N$ numbers is invariant throughout the process.

Then, using the Chinese Remainder Theorem and Bézout's identity, construct an explicit example with $N = 4$ where the final number is a product of three distinct primes.

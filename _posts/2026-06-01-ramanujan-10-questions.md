---
title: "10 Questions from Ramanujan's Lost Notebook — The Identities That Prove Mathematics Is Haunted"
date: 2026-06-01
categories:
  - Number Theory
  - Mathematics
tags:
  - ramanujan
  - theta-functions
  - continued-fractions
  - modular-forms
  - partitions
  - eisenstein-series
  - rogers-ramanujan
  - bessel-functions
  - gauss-sums
share: true
read_time: true
excerpt: "Ramanujan recorded thousands of identities without proof — each one a compressed universe of mathematical truth waiting to be unpacked. From partition congruences and continued fraction reciprocity to Eisenstein series differential equations and integral analogues of Gauss sums, here are 10 questions that capture the 'supreme secret' of elegant mathematical relations discovered through deep intuition."
---

**Challenge to the reader:** Take question #1 below. Set $a = 1$ and write out the first 12 coefficients $\lambda_0$ through $\lambda_{11}$. For $p = 5$, check whether $\lambda_{5n+4} \equiv 0 \pmod{5}$ holds for $n = 0, 1$. This is the gateway to Ramanujan's partition congruences.

---

## 1. The Lost Notebook Style

Ramanujan recorded thousands of identities without proof — often on a single line, without commentary. Each one is a compressed universe of mathematical truth that researchers are still unpacking over a century later. His compositions share a distinctive fingerprint:

- **Theta functions and $q$-series** are the fundamental vocabulary
- **Continued fractions** appear as naturally as polynomials
- **Modular equations** link values at $q$ and $q^n$ through algebraic relations
- **Partition statistics** reveal hidden congruences and symmetries
- **Asymptotic expansions** extracted from divergent series with preternatural accuracy

The 10 questions below are styled after compositions from Ramanujan's Lost Notebook. Each is followed by the explorations it makes possible.

---

## 2. Partition Congruences and the Crank

**Question:** Let

$$
F_a(q) = \frac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty} = \sum_{n=0}^{\infty} \lambda_n q^n
$$

For which primes $p$ does a $p$-dissection exist such that

$$
\lambda_{pn+r} \equiv 0 \pmod{\Phi_p(a)}
$$

for some residue $r$?

**Why it matters:** This question drives at the combinatorial explanation of Ramanujan's famous congruences:

$$
p(5n+4) \equiv 0 \pmod{5}, \quad p(7n+5) \equiv 0 \pmod{7}, \quad p(11n+6) \equiv 0 \pmod{11}
$$

The **crank** and **rank** statistics partition the set of partitions into equinumerous classes, providing a visual and structural understanding of *why* certain partition numbers are divisible by 5, 7, or 11. Dyson conjectured the crank; Atkin and Garvan proved its existence in 1988.

**Challenge:** For $p = 5$, the relevant cyclotomic polynomial is $\Phi_5(a) = 1 + a + a^2 + a^3 + a^4$. Set $a = e^{2\pi i/5}$ and compute the first five $\lambda_n$. What pattern emerges?

---

## 3. Reciprocity of the Rogers-Ramanujan Continued Fraction

**Question:** Let $R(q)$ be the Rogers-Ramanujan continued fraction:

$$
R(q) = \cfrac{q^{1/5}}{1 + \cfrac{q}{1 + \cfrac{q^2}{1 + \cfrac{q^3}{1 + \ddots}}}}
$$

If $\alpha\beta = \pi^2$, prove that

$$
\left(\frac{\sqrt{5}+1}{2} + R(e^{-2\alpha})\right)\left(\frac{\sqrt{5}+1}{2} + R(e^{-2\beta})\right) = \frac{5+\sqrt{5}}{2}
$$

**Why it matters:** This reciprocity theorem enables the **evaluation of continued fractions in closed form** when $q = e^{-\pi\sqrt{n}}$ for rational $n$. It links the value at one argument to the value at the complementary argument — a structural mirroring that pervades modular forms.

For example, setting $\alpha = \beta = \pi$ gives:

$$
\frac{\sqrt{5}+1}{2} + R(e^{-2\pi}) = \sqrt{\frac{5+\sqrt{5}}{2}}
$$

which evaluates $R(e^{-2\pi})$ exactly. Ramanujan computed dozens of such singular moduli, each one an algebraic number of deep arithmetic significance.

---

## 4. Differential Equations of Eisenstein Series

**Question:** Define $P, Q, R$ as the normalized Eisenstein series of weights 2, 4, and 6:

$$
P(q) = 1 - 24\sum_{n=1}^{\infty} \frac{n q^n}{1-q^n}, \quad
Q(q) = 1 + 240\sum_{n=1}^{\infty} \frac{n^3 q^n}{1-q^n}, \quad
R(q) = 1 - 504\sum_{n=1}^{\infty} \frac{n^5 q^n}{1-q^n}
$$

Show that Ramanujan's differential system holds:

$$
q\frac{dP}{dq} = \frac{P^2 - Q}{12}, \quad
q\frac{dQ}{dq} = \frac{PQ - R}{3}, \quad
q\frac{dR}{dq} = \frac{PR - Q^2}{2}
$$

**Why it matters:** These three equations form a nonlinear differential system that is the foundation for:

- **Ramanujan-type series for $1/\pi$**, such as

$$
\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)!}{(n!)^4} \cdot \frac{1103 + 26390n}{396^{4n}}
$$

- **Congruences for the Ramanujan tau-function** $\tau(n)$, defined by

$$
q\prod_{n=1}^{\infty}(1-q^n)^{24} = \sum_{n=1}^{\infty} \tau(n) q^n
$$

The differential equations encode the fact that the ring of quasi-modular forms is closed under the Serre derivative $q\,d/dq$.

**Challenge:** Compute $P$, $Q$, and $R$ to order $q^3$ directly from their $q$-expansions and verify that $q\,dP/dq = (P^2 - Q)/12$ holds up to $O(q^3)$.

---

## 5. Double Series of Bessel Functions

**Question:** Let

$$
F(x) = \begin{cases}
\lfloor x \rfloor & \text{if } x \notin \mathbb{Z} \\[4pt]
x - \frac{1}{2} & \text{if } x \in \mathbb{Z}
\end{cases}
$$

Prove that

$$
\sum_{n=1}^{\infty} F\!\left(\frac{x}{n}\right) = \pi x + \sqrt{x} \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \sqrt{\frac{n}{m}}\, J_1\!\left(4\pi\sqrt{mnx}\right)
$$

**Why it matters:** This identity lies at the intersection of:

- The **classical circle problem** (Gauss): counting lattice points inside a circle of radius $\sqrt{x}$
- The **Dirichlet divisor problem**: estimating $\sum_{n \le x} d(n)$ with optimal error terms
- **Weighted divisor sums** and the theory of **conditional convergence in double series**

The left-hand side involves the floor function — a discrete counting device. The right-hand side expresses the same quantity as an oscillatory double sum of Bessel functions. The identity is a manifestation of the **Voronoï summation formula**, which converts sums over divisors into sums over Bessel functions of related arguments.

---

## 6. Identities for the Rogers-Ramanujan Functions

**Question:** Define the Rogers-Ramanujan functions:

$$
G(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n}, \qquad
H(q) = \sum_{n=0}^{\infty} \frac{q^{n(n+1)}}{(q;q)_n}
$$

Prove that

$$
H(q)\,G(q^{11}) - q^2\,G(q)\,H(q^{11}) = 1
$$

**Why it matters:** Ramanujan compiled a list of **forty such identities** relating $G(q)$ and $H(q)$ at powers of $q$. These are modular equations in disguise — each one encodes a relationship between the Rogers-Ramanujan functions at arguments $q$ and $q^n$ for specific degrees $n = 5, 7, 11, \ldots$.

These identities provided the first clues to the theory of **mock theta functions**, which Ramanujan described in his last letter to Hardy. Mock theta functions behave like theta functions near roots of unity but have exponential asymptotic expansions incompatible with true modularity — and the Rogers-Ramanujan identities reveal exactly how they straddle the modular world.

---

## 7. Radical Identities and the *Componendo et Dividendo* Rule

**Question:** Given the sole condition $g^4 = 5$, prove the following equality of nested radicals:

$$
\frac{\sqrt{3+2g} - \sqrt{4-4g}}{\sqrt{3+2g} + \sqrt{4-4g}} = 2 + g + g^2 + g^3
$$

**Why it matters:** This is Ramanujan at his most elementary and most mysterious. From a single minimal condition ($g^4 = 5$), an elaborate algebraic identity emerges. The technique of **componendo et dividendo** — the principle that

$$
\frac{a}{b} = \frac{c}{d} \implies \frac{a-b}{a+b} = \frac{c-d}{c+d}
$$

— is the key that unlocks such radical simplifications.

Ramanujan was a virtuoso of nested radicals. His familiarity with algebraic numbers allowed him to see factorizations and conjugates that remain invisible to most mathematicians. Problems like this remind us that before the theta functions and modular forms, Ramanujan's first love was **algebraic manipulation of radicals**.

**Challenge:** Verify the identity numerically: compute $g = 5^{1/4}$, evaluate the left-hand side and right-hand side to 10 decimal places. Then attempt to prove it algebraically. The denominator rationalization step is the key.

---

## 8. Highly Composite Numbers and Representation by Squares

**Question:** Let $r_{2k}(N)$ denote the number of ways to represent $N$ as a sum of $2k$ squares:

$$
r_{2k}(N) = \#\left\{(x_1, \ldots, x_{2k}) \in \mathbb{Z}^{2k} : x_1^2 + \cdots + x_{2k}^2 = N\right\}
$$

Determine the maximal order of $r_{2k}(N)$ as $N \to \infty$.

**Why it matters:** This extends Ramanujan's study of **highly composite numbers** — integers with more divisors than any smaller integer — to other arithmetic functions. Jakobi's formula expresses $r_{2k}(N)$ in terms of divisor functions, and the maximal order problem asks: how large can this representation-counting function get?

Under the **Riemann Hypothesis**, the maximal order of $\sigma_{-s}(N)$ (the sum of $(-s)$-th powers of divisors) is tightly constrained. The question connects:

- The theory of **theta functions** (generating functions for $r_{2k}(N)$)
- **Largely composite numbers** and their generalizations
- The **Lindelöf hypothesis** for $L$-functions via bounds on divisor sums

---

## 9. Partial Theta Function Transformations

**Question:** Prove the identity

$$
\sum_{n=0}^{\infty} \frac{q^n}{(q;q)_n^2} = \frac{1}{(q;q)_\infty^2} \sum_{n=0}^{\infty} (-1)^n q^{n(n+1)/2}
$$

**Why it matters:** The sums on both sides are **partial theta functions** — series that resemble Jacobi theta functions but sum only over non-negative indices rather than all integers. Unlike genuine theta functions, partial theta functions do **not** satisfy modular transformation laws. They live in a liminal space:

- The left-hand side appears in **combinatorial generating functions** for gradual stacks with summits
- The right-hand side is a **false theta function** — it looks modular but isn't
- **Warnaar's theory** classifies identities of this type into a systematic algebraic framework

These identities provide combinatorial bijections between seemingly unrelated classes of integer partitions — often revealing that two generating functions count the same objects in different ways.

**Challenge:** Expand both sides to $O(q^5)$ by hand and verify the identity term-by-term. The left side involves the $q$-Pochhammer symbol $(q;q)_n = (1-q)(1-q^2)\cdots(1-q^n)$.

---

## 10. Asymptotic Expansion of a Continued Fraction Zero

**Question:** Let $q_0(a)$ be the least positive zero of the continued fraction equation

$$
1 - \cfrac{aq}{1 - \cfrac{aq^2}{1 - \cfrac{aq^3}{1 - \ddots}}} = 0
$$

Show that as $a \to \infty$,

$$
q_0(a) \sim \frac{1}{a} - \frac{1}{a^2} + \frac{2}{a^3} - \frac{6}{a^4} + \cdots
$$

**Why it matters:** This asymptotic expansion facilitates the **numerical approximation of zeros of continued fractions**, which arises in:

- **Birth and death processes** in queueing theory and population dynamics
- The enumeration of **"coins in a fountain"** — a combinatorial problem where coins are stacked so each coin touches two below it
- Comparison of **successive approximation methods** (Euler, Lagrange, Halley) for root-finding

The coefficients $1, 1, 2, 6, \ldots$ are the factorial numbers $(n-1)!$, suggesting a connection to the generating function of permutations. Indeed, the continued fraction is closely related to the $q$-exponential function and the Rogers-Fine identity.

---

## 11. Integral Analogues of Gauss Sums

**Question:** Define the integral transform

$$
\phi_w(t) = \int_0^{\infty} \frac{\cos(\pi t x)}{\cosh(\pi x)} e^{-\pi w x^2}\,dx
$$

Determine the quasiperiodic relation for $\phi_w(t + 2i)$ — that is, how shifting $t$ by $2i$ relates to $\phi_w(t)$.

**Why it matters:** These integrals function as **continuous analogues of Gauss sums**. Classical Gauss sums:

$$
G(a, q) = \sum_{n=0}^{q-1} e^{2\pi i a n^2 / q}
$$

satisfy beautiful reciprocity and factorization laws. The integral $\phi_w(t)$ replaces the discrete sum with a continuous integral, the quadratic exponential with a Gaussian weight $e^{-\pi w x^2}$, and the character with the $\cos(\pi tx)/\cosh(\pi x)$ kernel.

The quasiperiodicity in $t$ mirrors the transformation formulas of Jacobi theta functions:

$$
\vartheta(z; \tau+1) = \vartheta(z; \tau), \qquad
\vartheta(z/\tau; -1/\tau) = \sqrt{-i\tau}\, e^{\pi i z^2/\tau}\,\vartheta(z; \tau)
$$

These integral identities have applications to **Dirichlet $L$-series** at critical values and to the evaluation of **character analogues of Gauss sums** in analytic number theory.

**Challenge:** For $w = 1$ and $t = 0$, evaluate $\phi_1(0)$ in closed form. (Hint: the integral $\int_0^\infty \operatorname{sech}(\pi x)\,dx = 1/2$.)

---

## 12. The Big Picture: Why These 10 Questions Belong Together

| # | Topic | Mathematical Domain | Ramanujan's Tool |
|---|-------|--------------------|-------------------|
| 1 | Partition congruences | Additive combinatorics | $q$-series, crank/rank |
| 2 | Continued fraction reciprocity | Modular forms | Singular moduli |
| 3 | Eisenstein differential equations | Quasi-modular forms | Serre derivative |
| 4 | Bessel double series | Analytic number theory | Voronoï summation |
| 5 | Rogers-Ramanujan identities | $q$-series | Modular equations |
| 6 | Nested radical identities | Algebraic number theory | Componendo et dividendo |
| 7 | Maximal order of $r_{2k}(N)$ | Multiplicative number theory | Divisor function bounds |
| 8 | Partial theta transformations | Combinatorics | False theta functions |
| 9 | Continued fraction zero asymptotics | Applied mathematics | Asymptotic expansion |
| 10 | Integral Gauss sum analogues | Analytic number theory | Transformation formulas |

---

## 13. Deeper Significance

What unifies these 10 questions is Ramanujan's method: **empirical discovery followed by structural revelation**. He worked forward from numerical data to identities, then backward from identities to the theories that explained them.

This is the opposite of the standard pedagogical order, where one first learns the theory of modular forms and then applies it to $q$-series. Ramanujan *invented* the theory by discovering the identities first.

The Lost Notebook continues to yield new mathematics because each identity is a **compressed proof** — a statement that a certain infinite sum, product, or continued fraction collapses to a closed form. Unpacking *why* it collapses reveals the underlying structure.

Modern researchers have built entire careers decoding these compressed proofs:

- **George Andrews** discovered the Lost Notebook in 1976 at Trinity College and has devoted decades to proving its contents
- **Bruce Berndt** and colleagues have produced five volumes systematically proving Ramanujan's formulas
- **Ken Ono** used Ramanujan's work on partitions to solve long-standing congruence conjectures

---

**Final Challenge:** Choose one of the 10 questions above and attempt a full proof. Start with question #6 (nested radicals) — it requires only high-school algebra. Once you've proven it, attempt question #3 (Eisenstein differential equations) using the $q$-expansions of $P$, $Q$, and $R$. The first will teach you Ramanujan's algebraic virtuosity; the second will teach you his analytic machinery.

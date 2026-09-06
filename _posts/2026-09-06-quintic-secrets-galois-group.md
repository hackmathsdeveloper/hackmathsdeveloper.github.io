---
title: "The Quintic That Gives Up All Its Secrets — One Polynomial, Completely Understood"
date: 2026-09-06
categories:
  - Galois Theory
  - Mathematics
tags:
  - de-moivre-quintic
  - dickson-polynomials
  - splitting-fields
  - frobenius-group
  - chebotarev-density
  - modular-factorization
  - discriminant
share: true
read_time: true
excerpt: "One substitution turns x⁵ + 10x³ + 20x − 4 into a quadratic, and the rest is Galois theory: explicit roots, a 20-element Galois group, and a complete classification of how the polynomial factors modulo every prime. A single quintic, understood from every angle."
---

**Challenge to the reader:** Expand $\left(u-\frac{2}{u}\right)^5+10\left(u-\frac{2}{u}\right)^3+20\left(u-\frac{2}{u}\right)$ and watch almost everything cancel: the answer is $u^5-\frac{32}{u^5}$. This one substitution is the key to the whole post.

*Part 4 of four in the series **The Quintic: From Knot to Galois Group**: [Part 1 — The Indivisible Knot]({% post_url 2026-09-06-quintic-knot-indivisible %}) · [Part 2 — The Wall of Five]({% post_url 2026-09-06-s5-wall-no-radical-formula %}) · [Part 3 — Five Quintics]({% post_url 2026-09-06-five-quintics-gallery %}) · [Part 4 — The Quintic That Gives Up All Its Secrets]({% post_url 2026-09-06-quintic-secrets-galois-group %}) (this page)*

## The core statement

For

$$P(x)=x^5+10x^3+20x-4,$$

every object in the theory is completely explicit: the five roots in radicals, the splitting field $\mathbb Q(2^{1/5},\zeta_5)$, and the Galois group $F_{20}\cong C_5\rtimes C_4$ of order 20 — which dictates, through Chebotarev's density theorem, exactly how $P$ factors modulo every prime.

**Why it matters.** The previous parts showed why the general quintic has no radical formula. This one shows the opposite extreme in full detail: a solvable quintic whose symmetry is rich enough (order 20) that factoring it modulo primes becomes a *fingerprint* of its Galois group.

---

## 1. The hidden substitution

The polynomial piece $x^5+10x^3+20x$ is not arbitrary: it is the Dickson polynomial $D_5(x,a)=x^5-5ax^3+5a^2x$ at $a=-2$. Dickson polynomials satisfy the fundamental identity

$$D_5\left(u+\frac{a}{u},a\right)=u^5+\frac{a^5}{u^5}.$$

With $a=-2$ and

$$x=u-\frac{2}{u},$$

the opening challenge gives

$$\boxed{x^5+10x^3+20x=u^5-\frac{32}{u^5}}.$$

## 2. From quintic to quadratic

The equation $P(x)=0$ becomes

$$u^5-\frac{32}{u^5}-4=0.$$

Multiplying by $u^5$:

$$u^{10}-4u^5-32=0.$$

Setting $y=u^5$ turns a quintic into a **quadratic**:

$$y^2-4y-32=0 \implies (y-8)(y+4)=0.$$

So

$$u^5=8 \qquad\text{or}\qquad u^5=-4.$$

## 3. Why ten $u$'s give only five $x$'s

At first there seem to be ten possibilities: five for $u^5=8$ and five for $u^5=-4$. But $x=u-\frac{2}{u}$ is unchanged under the involution

$$u\longmapsto-\frac{2}{u},$$

because $-\frac{2}{u}-\frac{2}{-2/u}=-\frac{2}{u}+u=u-\frac{2}{u}$. And if $u^5=8$, then

$$\left(-\frac{2}{u}\right)^5=-\frac{32}{8}=-4.$$

**Challenge 2:** Check both halves of this involution calculation. The ten $u$'s pair up, producing exactly **five roots** of the quintic.

## 4. The explicit roots

Let $b=2^{1/5}$ and $\zeta=\zeta_5=e^{2\pi i/5}$. The five solutions of $u^5=8$ are

$$u_k=2^{3/5}\zeta^k=b^3\zeta^k,\qquad k=0,1,2,3,4.$$

Since $\frac{2}{b^3}=\frac{b^5}{b^3}=b^2$, the five roots of $P$ are

$$\boxed{x_k=b^3\zeta^k-b^2\zeta^{-k}=2^{3/5}\zeta^k-2^{2/5}\zeta^{-k},\qquad k=0,\dots,4.}$$

Every root lies in $\mathbb Q(2^{1/5},\zeta_5)$ — already a candidate for the splitting field.

## 5. The splitting field

Define $K=\mathbb Q(b,\zeta_5)$. Each root belongs to $K$, so the splitting field $L$ satisfies $L\subseteq K$. The degrees are easy:

$$[\mathbb Q(b):\mathbb Q]=5 \qquad\text{($x^5-2$ is Eisenstein at 2)},$$

$$[\mathbb Q(\zeta_5):\mathbb Q]=\phi(5)=4,$$

and since 5 and 4 are coprime, the two extensions have intersection $\mathbb Q$, so

$$\boxed{[K:\mathbb Q]=5\cdot4=20.}$$

Two subtleties make $L=K$, not a proper subfield. First, adjoining one root $\alpha=x_0=b^3-b^2$ gives only $[\mathbb Q(\alpha):\mathbb Q]=5$ — the **root field** is smaller than the splitting field:

```text
          K = Q(2^(1/5), zeta5)      degree 20
             /            \
           5               4
          /                  \
       Q(alpha)            Q(zeta5)
          \                  /
           \                /
                   Q
```

Second, the Galois group acts faithfully on the five roots (Section 7), so an automorphism of $K$ fixing *every* root is the identity; hence $\operatorname{Gal}(K/L)=1$ and

$$\boxed{\operatorname{Spl}_{\mathbb Q}(x^5+10x^3+20x-4)=\mathbb Q(2^{1/5},\zeta_5),\qquad [L:\mathbb Q]=20.}$$

## 6. The Galois group

There are two fundamental automorphisms of $K=\mathbb Q(b,\zeta)$:

$$\sigma(b)=\zeta b,\quad \sigma(\zeta)=\zeta,
\qquad\qquad
\tau(b)=b,\quad \tau(\zeta)=\zeta^2.$$

Both are legitimate because $(\zeta b)^5=2$ and $\zeta\mapsto\zeta^2$ permutes the primitive fifth roots. They satisfy

$$\sigma^5=1,\qquad \tau^4=1,\qquad \tau\sigma\tau^{-1}=\sigma^2.$$

**Challenge 3:** Verify the last relation directly from the definitions.

Hence

$$\boxed{\operatorname{Gal}(K/\mathbb Q)\cong C_5\rtimes C_4,}$$

the **Frobenius group of order 20**, also written $F_{20}\cong\operatorname{AGL}(1,5)$. It is a subgroup of $S_5$ — but neither $D_5$ nor $S_5$ nor $A_5$.

## 7. How the group acts on the roots

Apply the automorphisms to $x_k=b^3\zeta^k-b^2\zeta^{-k}$:

$$\sigma(x_k)=b^3\zeta^{k+3}-b^2\zeta^{2-k}=x_{k+3},$$

$$\tau(x_k)=b^3\zeta^{2k}-b^2\zeta^{-2k}=x_{2k}.$$

So $\sigma$ is the 5-cycle $k\mapsto k+3 \pmod 5$, and $\tau$ is the 4-cycle $k\mapsto 2k \pmod 5$, fixing the index 0. The full set of cycle types on the five roots:

| element | order | cycle type | count |
|---|---|---|---|
| identity | 1 | $(1,1,1,1,1)$ | 1 |
| nontrivial $C_5$ | 5 | $(5)$ | 4 |
| multiplier $-1$ | 2 | $(1,2,2)$ | 5 |
| multiplier $2,3$ | 4 | $(1,4)$ | 10 |

Total: $1+4+5+10=20$. These four cycle types — and their ratios $1:4:5:10$ — will show up again, statistically, among the primes.

## 8. The discriminant

For this quintic,

$$\boxed{\operatorname{disc}(P)=64{,}800{,}000=2^8\,3^4\,5^5.}$$

Because the exponent of 5 is odd, the discriminant is **not** a square in $\mathbb Q$, so the Galois group is not contained in $A_5$ — consistent with $F_{20}$ (the subgroups $C_5$ and $D_5$ of $F_{20}$ both lie in $A_5$).

There is a subtlety worth knowing. The splitting field $K=\mathbb Q(2^{1/5},\zeta_5)$ is ramified only at **2 and 5**, yet the polynomial discriminant is divisible by $3^4$. The factor $3^4$ comes from the index of $\mathbb Z[\theta]$ in the ring of integers of $K$: modulo 3,

$$P(x)\equiv(x-1)(x^2+2x+2)^2\pmod 3,$$

a repeated quadratic — a symptom of the polynomial's discriminant, not of ramification in $K$. For the clean factorization classification below, this is why we restrict to $p\ne2,5$. (Ramified primes: $P(x)\equiv x^5\pmod 2$ and $P(x)\equiv(x+1)^5\pmod 5$.)

**Challenge 4:** Compute the discriminant of $x^5-2$ (answer: $5^5\cdot2^4=50{,}000$) and check it is not a square. What does that say about $\operatorname{Gal}(x^5-2)\subseteq A_5$?

## 9. How $P$ factors modulo $p$

For a prime $p\ne2,5$, the Frobenius automorphism acts on the roots as $k\mapsto a+pk \pmod 5$ for some $a\in\mathbb F_5$. The factorization of $P(x)\pmod p$ is determined entirely by $p \bmod 5$:

| $p \bmod 5$ | extra condition | Frobenius cycle type | $P(x) \pmod p$ |
|---|---|---|---|
| 1 | $2^{(p-1)/5}\equiv 1$ | $(1,1,1,1,1)$ | splits completely |
| 1 | $2^{(p-1)/5}\not\equiv 1$ | $(5)$ | irreducible |
| 2 | — | $(1,4)$ | linear × irreducible quartic |
| 3 | — | $(1,4)$ | linear × irreducible quartic |
| 4 | — | $(1,2,2)$ | linear × quadratic × quadratic |

**Why the condition for $p\equiv1\pmod5$.** Then $\zeta$ is fixed by Frobenius, and Frobenius acts on $b$ by $b\mapsto b^p=b\cdot2^{(p-1)/5}$ — it fixes $b$ (and hence every root) exactly when $2^{(p-1)/5}\equiv1\pmod p$, i.e. when 2 is a fifth power mod $p$.

Here are verified examples:

- **$p=7$** ($\equiv2$): $P(x)\equiv(x+1)(x^4-x^3-3x^2+3x+3)\pmod7$ — type $1+4$.
- **$p=13$** ($\equiv3$): $P(x)\equiv(x+2)(x^4-2x^3+x^2-2x-2)\pmod{13}$ — type $1+4$.
- **$p=17$** ($\equiv2$): $P(x)\equiv(x-5)(x^4+5x^3+x^2+5x+11)\pmod{17}$ — type $1+4$.
- **$p=19$** ($\equiv4$): $P(x)\equiv(x+4)(x^2-3x-8)(x^2-x-7)\pmod{19}$ — type $1+2+2$.
- **$p=23$** ($\equiv3$): type $1+4$.
- **$p=29$** ($\equiv4$): $P(x)\equiv(x-4)(x^2+9x+3)(x^2-5x+10)\pmod{29}$ — type $1+2+2$.
- **$p=11,31,41,61,71$** ($\equiv1$, with $2^{(p-1)/5}\not\equiv1$): $P(x)$ is irreducible mod $p$ — type $5$.
- **$p=151$** ($\equiv1$, and $2^{30}\equiv1\pmod{151}$): $P(x)$ splits into five linear factors:

$$\boxed{P(x)\equiv(x+8)(x-51)(x-47)(x-35)(x-26)\pmod{151}.}$$

There are exactly four possible splitting patterns: $1+1+1+1+1$, $5$, $1+4$, $1+2+2$ — precisely the cycle types of the Galois group from Section 7. This is the fundamental correspondence

$$\boxed{\text{factorization of } P \bmod p \ \longleftrightarrow\ \text{Frobenius conjugacy class in } \operatorname{Gal}(K/\mathbb Q).}$$

## 10. Why the primes obey the group

Chebotarev's density theorem says that among all primes, the Frobenius elements are distributed over the conjugacy classes in proportion to their size. For our group of order 20:

| cycle type | group elements | predicted density |
|---|---|---|
| $(1,1,1,1,1)$ | 1 | $1/20 = 5\%$ |
| $(5)$ | 4 | $4/20 = 20\%$ |
| $(1,4)$ | 10 | $10/20 = 50\%$ |
| $(1,2,2)$ | 5 | $5/20 = 25\%$ |

An experiment over the first 2000 primes (excluding 2 and 5) gives:

$$96,\quad 400,\quad 1014,\quad 490,$$

i.e. $4.8\%$, $20\%$, $50.7\%$, $24.5\%$ — in remarkable agreement, with small deviations characteristic of Chebotarev's slow convergence. As a bonus datum: among the 496 primes $p\equiv1\pmod5$ in the sample, exactly 96 (about $1/5$) split completely, matching the criterion of Section 9.

---

**Final challenge:** Use the table in Section 9 to predict the factorization of $P(x)$ modulo 211 and modulo 251. (Both are $1\bmod5$ — compute $2^{(p-1)/5}\bmod p$; the answers are irreducible mod 211 and completely split mod 251.) Then verify one of the two by hand or computer.

The whole story in one box:

$$\boxed{\begin{aligned}
P(x)&=x^5+10x^3+20x-4\\
x&=u-\frac{2}{u}\\[1mm]
P(x)=0&\Longleftrightarrow u^{10}-4u^5-32=0\\
&\Longleftrightarrow (u^5-8)(u^5+4)=0\\[1mm]
x_k&=2^{3/5}\zeta_5^k-2^{2/5}\zeta_5^{-k}\\[1mm]
K&=\mathbb Q(2^{1/5},\zeta_5),\qquad [K:\mathbb Q]=20\\[1mm]
\operatorname{Gal}(K/\mathbb Q)&\cong C_5\rtimes C_4=F_{20}
\end{aligned}}$$

Dickson polynomials → explicit radicals → cyclotomic field → Frobenius group of order 20 → prime splitting types: every layer of the theory is visible in this one polynomial.

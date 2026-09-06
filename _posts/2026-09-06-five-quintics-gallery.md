---
title: "Five Quintics You Should Meet — and the One No Formula Can Solve"
date: 2026-09-06
categories:
  - Galois Theory
  - Mathematics
tags:
  - quintic-examples
  - galois-groups
  - cyclotomic-polynomials
  - frobenius-group
  - eisenstein-criterion
  - radical-solvability
share: true
read_time: true
excerpt: "Five quintics, one question: solvable by radicals or not? From fifth roots of unity to a quintic whose roots no formula can write, each example pins down a Galois group — and shows how to find it in practice."
---

**Challenge to the reader:** Verify the radical expression for the fifth root of unity: from $\cos(2\pi/5)=(\sqrt{5}-1)/4$ and $\sin^2+\cos^2=1$, recover

$$\zeta_5=\frac{\sqrt5-1}{4}+i\sqrt{\frac{5+\sqrt5}{8}},$$

and check that its fifth power is 1. This one expression is a quintic solved by radicals.

*Part 3 of four in the series **The Quintic: From Knot to Galois Group**: [Part 1 — The Indivisible Knot]({% post_url 2026-09-06-quintic-knot-indivisible %}) · [Part 2 — The Wall of Five]({% post_url 2026-09-06-s5-wall-no-radical-formula %}) · [Part 3 — Five Quintics]({% post_url 2026-09-06-five-quintics-gallery %}) (this page) · [Part 4 — The Quintic That Gives Up All Its Secrets]({% post_url 2026-09-06-quintic-secrets-galois-group %})*

## The core statement

Here are five representative quintics over $\mathbb Q$, ranging from completely elementary cases to an irreducible quintic whose roots cannot be expressed by radicals. The governing fact:

> A polynomial over $\mathbb Q$ is solvable by radicals exactly when its Galois group over $\mathbb Q$ is a **solvable group**. In particular, an irreducible quintic with Galois group $S_5$ or $A_5$ is not solvable by radicals. [ams](https://www.ams.org/bookstore/pspdf/gsm-165-prev.pdf)

**Why it matters.** "Quintics have no formula" is a false statement; the truth is "there is no radical formula for the *general* quintic." These five examples calibrate the boundary between the solvable and the hopeless.

---

## 1. The cyclotomic quintic

$$x^5-1=0.$$

### Roots

The five roots are the fifth roots of unity:

$$1,\quad \zeta_5,\quad \zeta_5^2,\quad \zeta_5^3,\quad \zeta_5^4,
\qquad
\zeta_5=e^{2\pi i/5}=\cos\frac{2\pi}{5}+i\sin\frac{2\pi}{5}.$$

### Galois-theory analysis

Since $x^5-1=(x-1)\Phi_5(x)$ with $\Phi_5(x)=x^4+x^3+x^2+x+1$, the nontrivial splitting field is $\mathbb Q(\zeta_5)$, and

$$\operatorname{Gal}(\mathbb Q(\zeta_5)/\mathbb Q)\cong(\mathbb Z/5\mathbb Z)^\times\cong C_4.$$

A cyclic group is abelian, hence solvable — so the equation is solvable by radicals. In fact $\zeta_5$ can be built from square roots alone because $5$ is a Fermat prime; the opening challenge exhibits the formula. This is the simplest example of a solvable quintic.

## 2. A reducible quintic

$$x^5-5x^3+4x=0.$$

### Factorization and roots

Factor out $x$ and regard the quartic as a quadratic in $x^2$:

$$x^5-5x^3+4x=x(x^4-5x^2+4)=x(x^2-1)(x^2-4),$$

so the roots are

$$\boxed{-2,\,-1,\,0,\,1,\,2}.$$

### Galois-theory analysis

The polynomial already splits over $\mathbb Q$, so its splitting field is $\mathbb Q$ and its Galois group is trivial:

$$\operatorname{Gal}(\mathbb Q/\mathbb Q)=\lbrace 1\rbrace.$$

The trivial group is solvable. This is a quintic by degree only — reducibility reduces it to lower-degree pieces.

## 3. A binomial quintic

$$x^5-2=0.$$

### Roots

Let $\alpha=\sqrt[5]{2}$. Then the roots are

$$\alpha,\;\alpha\zeta_5,\;\alpha\zeta_5^2,\;\alpha\zeta_5^3,\;\alpha\zeta_5^4,$$

approximately

$$1.148698355,\qquad 0.3550\pm1.0925i,\qquad -0.9294\pm0.6752i.$$

### Galois-theory analysis

The polynomial is irreducible over $\mathbb Q$ by Eisenstein's criterion with $p=2$.

**Challenge 2:** Run Eisenstein for yourself: check the leading coefficient, the divisibility of the others, and the constant term against $p=2$.

Its splitting field is $K=\mathbb Q(\sqrt[5]{2},\zeta_5)$. The automorphisms can

- send $\sqrt[5]{2}\mapsto\zeta_5^a\sqrt[5]{2}$, a cyclic $C_5$-type action;
- send $\zeta_5\mapsto\zeta_5^b$, where $b\in(\mathbb Z/5\mathbb Z)^\times\cong C_4$.

So the Galois group has the form

$$C_5\rtimes C_4,$$

the Frobenius group of order $20$, often denoted $F_{20}$ or $\operatorname{AGL}(1,5)$. It has a normal series

$$\lbrace 1\rbrace\triangleleft C_5\triangleleft C_5\rtimes C_4$$

with abelian quotients, so it is solvable — as is obvious directly from $\sqrt[5]{2}$, but Galois theory explains why adjoining the other four roots introduces no obstruction. For an irreducible quintic over $\mathbb Q$, solvability by radicals occurs precisely when the Galois group is a subgroup of $F_{20}$; the possible transitive solvable groups are $C_5$, $D_5$, and $F_{20}$. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_24_solvability_in_radicals.pdf)

## 4. An irreducible solvable quintic of Frobenius type

$$x^5+120x-1344=0.$$

This one is more interesting than $x^5-2$: it is not visibly built from a single fifth root, yet Galois theory proves it solvable.

### Galois-theory diagnosis

For a Bring–Jerrard quintic $f(x)=x^5+px+q$ there is a classical sextic resolvent. Here $p=120$, $q=-1344$, and the resolvent is

$$y^6+960y^5+576000y^4+276480000y^3+82944000000y^2+\cdots,$$

which has the rational root

$$y=1440.$$

A rational root of this resolvent shows that the Galois group is contained in $F_{20}$, so the quintic is solvable by radicals. The discriminant

$$256p^5+3125q^4=10{,}202{,}775{,}552{,}000{,}000$$

is **not** a square in $\mathbb Q$ (its square root is approximately $101{,}008{,}789.4$), which rules out containment in $A_5$: among the transitive solvable subgroups $C_5$, $D_5$, $F_{20}$ of $S_5$, the first two lie inside $A_5$. The quintic is also irreducible — it has no rational root, and it is irreducible mod 71 — so its Galois group acts transitively. The conclusion:

$$\boxed{\operatorname{Gal}(f/\mathbb Q)\cong F_{20}}.$$

**Challenge 3:** Check that none of the divisors of 1344 gives a rational root of $x^5+120x-1344$. Shortcut: first verify that $d^5\gt120d+1344$ for every integer $d\geq9$ — then it suffices to test the divisors $\pm1,\pm2,\pm3,\pm4,\pm6,\pm7,\pm8$.

### What "find the roots" means here

The roots do have radical expressions, but substantially more complicated ones than for $x^5-2$. A Galois-theoretic algorithm proceeds through a tower of extensions associated with the group structure $F_{20}\cong C_5\rtimes C_4$:

$$\mathbb Q\ \subseteq\ \mathbb Q(\sqrt{\Delta})\ \subseteq\ \text{quartic auxiliary extension}\ \subseteq\ \text{fifth-root extension}\ \subseteq\ K.$$

The important conclusion: **all five roots are expressible by radicals** — but unlike the binomial case, the explicit formulas are not enlightening. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_24_solvability_in_radicals.pdf)

## 5. A nonsolvable quintic

$$x^5-6x+3=0.$$

### Step 1: Irreducibility

Modulo 5,

$$x^5-6x+3\equiv x^5-x+3\pmod 5,$$

which has no roots mod 5 (check $0,1,2,3,4$: each gives 3) and in fact is irreducible mod 5. A factorization mod 5 would descend to a factorization over $\mathbb Q$, so $x^5-6x+3$ is irreducible over $\mathbb Q$ — the Galois group acts transitively on the five roots. [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf)

### Step 2: A transposition in the Galois group

Modulo 17, the polynomial factors as three linear factors times one irreducible quadratic. The corresponding permutation of the roots is a **transposition** — it swaps two roots and fixes the other three.

### Step 3: Jordan's theorem finishes it

A transitive subgroup of $S_5$ that contains a transposition is all of $S_5$ (Part 2's final challenge). Hence

$$\boxed{\operatorname{Gal}(x^5-6x+3\,/\,\mathbb Q)\cong S_5.}$$

### Step 4: Why this blocks radicals

The symmetric group $S_5$ is not solvable: its commutator structure reaches the simple group $A_5$, which has no seams (Parts 1 and 2). Therefore

$$\boxed{x^5-6x+3=0 \text{ cannot be solved by radicals over } \mathbb Q.}$$

Its five roots certainly exist and can be approximated numerically, but no formula using only rational numbers, arithmetic, and finitely many $n$-th roots can produce them. [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf)

---

## 6. Summary table

| Quintic | Roots / method | Galois group over $\mathbb Q$ | Solvable by radicals? |
|---|---|---|---|
| $x^5-1=0$ | Fifth roots of unity | $C_4$ for the nontrivial cyclotomic factor | Yes |
| $x^5-5x^3+4x=0$ | $-2,-1,0,1,2$ | trivial | Yes |
| $x^5-2=0$ | $\sqrt[5]{2}\,\zeta_5^k$ | $C_5\rtimes C_4\cong F_{20}$ | Yes |
| $x^5+120x-1344=0$ | Resolvent method; radical expressions exist but are lengthy | $F_{20}$ | Yes |
| $x^5-6x+3=0$ | Numerical roots only; no radical formula | $S_5$ | No |

## 7. The practical workflow

For a quintic $f(x)\in\mathbb Q[x]$, the decision process is:

1. **Factor $f$ over $\mathbb Q$.** If it factors, solve the lower-degree pieces by familiar formulas.
2. **Check irreducibility.** Rational-root tests, Eisenstein's criterion, and factorization modulo primes.
3. **Compute the discriminant.** If it is a square in $\mathbb Q$, then $\operatorname{Gal}(f/\mathbb Q)\subseteq A_5$; if not, the group is not contained in $A_5$.
4. **Factor $f$ modulo several primes.** For primes not dividing the discriminant, the degrees of the irreducible factors reveal cycle types in the Galois group: irreducible mod $p$ suggests a 5-cycle; $2+3$ a permutation of type $(2,3)$; $1+4$ a 4-cycle; $1+2+2$ a double transposition; $1+1+3$ a 3-cycle; $1+1+1+2$ a transposition.
5. **Identify the subgroup of $S_5$.** If it is $S_5$ or $A_5$, radical formulas are impossible; if it is contained in $F_{20}$, the quintic is solvable by radicals. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_24_solvability_in_radicals.pdf)

The essential outcome: Galois theory does not merely say "quintics are hard." It gives a precise classification — the symmetry group of the roots determines whether a radical solution exists.

---

**Final challenge:** Run the workflow on $x^5-x-1$. Mod 3 it is irreducible (so the group is transitive), and mod 2 it factors as an irreducible quadratic times an irreducible cubic (so the group contains an element of order 6). The transitive subgroups of $S_5$ have orders 5, 10, 20, 60, and 120 — which ones contain an element of order 6? Conclude that $x^5-x-1$ has Galois group $S_5$ and is not solvable by radicals.

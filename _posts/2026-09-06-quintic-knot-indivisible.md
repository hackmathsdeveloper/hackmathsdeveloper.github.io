---
title: "The Knot No Scissors Can Cut — Why the Quintic Has No Formula"
date: 2026-09-06
categories:
  - Galois Theory
  - Mathematics
tags:
  - quintic-equation
  - abel-ruffini-theorem
  - galois-theory
  - alternating-group
  - simple-groups
  - radical-solvability
  - permutations
share: true
read_time: true
excerpt: "Every quintic has five roots; what it lacks is a radical formula that finds them. Using only permutations, counting, and division, this post shows why the symmetry of five roots is an indivisible knot — and where the 'obvious' proof goes wrong."
---

**Challenge to the reader:** Take two permutations of five objects: $(1\,2\,3)$ and $(3\,4\,5)$. Compute the product $(1\,2\,3)(3\,4\,5)$ — apply the rightmost permutation first — and describe the result. The surprise in this tiny computation is the precise reason the quintic has no formula.

*Part 1 of four in the series **The Quintic: From Knot to Galois Group**: [Part 1 — The Indivisible Knot]({% post_url 2026-09-06-quintic-knot-indivisible %}) (this page) · [Part 2 — The Wall of Five]({% post_url 2026-09-06-s5-wall-no-radical-formula %}) · [Part 3 — Five Quintics]({% post_url 2026-09-06-five-quintics-gallery %}) · [Part 4 — The Quintic That Gives Up All Its Secrets]({% post_url 2026-09-06-quintic-secrets-galois-group %})*

## The core statement

The general quintic $x^5 + ax^4 + bx^3 + cx^2 + dx + e = 0$ always has five complex roots. What does **not** exist is a formula for those roots using only $+,-,\times,\div$ and finitely many $n$-th roots — the result proved by Abel and Ruffini and explained by Galois.

**Why it matters.** The obstruction is not that the roots are missing; it is that the symmetry of the roots is too rigid to dismantle. This post proves the rigidity using nothing beyond permutations, counting, and long division — no field theory, no group theory beyond the group $S_5$ itself.

---

## 1. What "solved by a formula" means

Every time you write a square root you get a **2-way choice** ($x^2=4$ gives $2$ and $-2$); a cube root gives a 3-way choice; a fourth root gives a 4-way choice. A radical formula is a chain of such choices built from the coefficients, and nested choices multiply: a square root of a cube root makes $2\times3=6$ branches.

For low degrees the choice-structure matches the problem exactly:

- **Degree 2** — two roots; one square root cuts the 2-way tangle. Done.
- **Degree 3** — three roots; a square root and a cube root, nested, isolate all three.
- **Degree 4** — four roots, and $4=2\times2$: two square roots in sequence do the job.

In every solvable case the roots' symmetry can be *cut into smaller sub-tangles*, one radical at a time. That is what a formula does: it cuts.

## 2. The 5-way knot

A general quintic has 5 roots entangled in a highly asymmetric way: its only guaranteed symmetry is the full symmetric group — **all 120 permutations** of the five roots are admissible. You might hope to cut this knot with a fifth root: a 5th root makes a 5-way choice. But a bare fifth root only ever makes a *uniform* 5-way split — exactly the kind that solves $x^5-2=0$. It cannot reproduce the lopsided, interwoven symmetry of a general quintic.

**Challenge 2:** Solve $x^5-2=0$ by radicals, and notice how "uniform" its five roots are compared with the roots of a general quintic.

## 3. The trap in the obvious argument

Here is where almost every elementary explanation of the Abel–Ruffini theorem goes wrong. The tempting argument runs: *a square root can only swap 2 roots and a cube root can only cycle 3, so chains of square and cube roots can never produce a permutation that moves all 5 roots.*

This is **false** — and your opening computation proves it:

$$(1\,2\,3)(3\,4\,5) = (1\,2\,3\,4\,5),$$

a genuine 5-cycle built from two 3-cycles. (Compute $(3\,4\,5)(1\,2\,3)$ too: the two products differ. The symmetry is noncommutative — and *that* is the real issue.)

So the obstruction is not *which* permutations appear. It is the **order and layering** in which a radical formula is allowed to reveal them.

## 4. What radicals can actually do

Each radical in a formula corresponds to a *layer* of symmetry: adjoining $\sqrt[n]{\phantom{x}}$ can only reveal symmetries that cycle through $n$ states uniformly — technically, each radical step adds a **cyclic** layer of automorphisms. A chain of radicals therefore dismantles the symmetry layer by layer, through a chain of subgroups in which every step is cyclic (abelian).

So the honest question is: can the 120 permutations of the five roots be dismantled by such layers?

## 5. The alternating group has no seams

Inside the 120 permutations of $S_5$ live the 60 **even** permutations, the alternating group $A_5$. Any chain of layers, to pass through $A_5$, needs a nontrivial normal subgroup of $A_5$ — a seam to cut along. It has none. Here is a proof you can check by hand.

The conjugacy classes of $A_5$ have these sizes:

| class | size |
|---|---|
| identity | 1 |
| 3-cycles | 20 |
| double transpositions | 15 |
| 5-cycles (two classes) | 12 + 12 |

**Why these sizes.** A 3-cycle: choose 3 of 5 elements ($\binom{5}{3}=10$ ways) and orient them (2 ways): $10\cdot2=20$. A double transposition: choose the element left out (5 ways) and pair the remaining four (3 ways): $5\cdot3=15$. The $4!=24$ five-cycles split into two classes of 12, because a 5-cycle and its inverse are conjugate in $S_5$ but not in $A_5$.

**Challenge 3:** Verify these counts by hand and show they sum to 60.

A normal subgroup is a union of conjugacy classes that contains the identity, and its order divides the order of the group. So its order must be one of the subset sums of $\lbrace 20,15,12,12\rbrace$ plus 1:

$$1,\ 13,\ 16,\ 21,\ 25,\ 28,\ 33,\ 36,\ 40,\ 45,\ 48,\ 60$$

— and the only ones that divide 60 are $1$ and $60$ themselves.

$$\boxed{A_5 \text{ has no nontrivial proper normal subgroup: it is simple.}}$$

## 6. Why simplicity kills the formula

$A_5$ is also nonabelian — the two products in your opening challenge disagree. A simple nonabelian group cannot be dismantled by a chain of abelian layers: the only available seams are the whole group and nothing. Any chain of subgroups for the general quintic must pass through $A_5$, and there it gets stuck:

$$S_5 \supset A_5 \supset A_5 \supset \cdots$$

The chain never reaches the trivial group, so the general quintic's symmetry cannot be assembled from radical layers. **No radical formula for the general quintic exists.**

## 7. Knots that do come untied

The theorem concerns the *general* quintic. Individual quintics are often solvable: $x^5-2=0$ has roots $2^{1/5}\zeta_5^k$ with $\zeta_5=e^{2\pi i/5}$, and its symmetry group is not all of $S_5$ but a solvable group of order 20 — the knot has a seam, so the scissors work. Part 3 of this series tours five such quintics, and Part 4 dissects one of them completely, all the way down to its Galois group.

---

**Final challenge:** Redo the class-size argument by hand for $A_4$ (order 12): its classes have sizes $1$, $3$, $4$, $4$. Which subset sums containing 1 divide 12? The normal subgroup you find has order 4 — and that seam is exactly why the **quartic** does have a formula while the quintic does not.

---
title: "Why 60° Refuses to Be Cut in Three — and How Paper Folding Cheats the Proof"
date: 2026-10-23
categories:
  - Galois Theory
  - Mathematics
tags:
  - angle-trisection
  - constructible-numbers
  - wantzel-theorem
  - casus-irreducibilis
  - origami-construction
  - neusis-construction
  - transcendental-numbers
  - quadrature-of-circle
share: true
read_time: true
excerpt: "Trisecting an arbitrary angle with compass and straightedge is impossible, and 60° is the cleanest witness: its trisection equation is an irreducible cubic. Allow a marked ruler or a paper fold and the cubic opens; allow the quadratrix and even π falls. The boundary is the operation set."
---

**Challenge to the reader:** Set $x=\cos 20^\circ$. Before reading Section 2, use the identity for $\cos 3\phi$ to write the cubic equation $x$ must satisfy. Test it for rational roots. What does the result forbid?

*Part 4 of four in the series **The Shape of the Possible: Tilings, Curvature, and Construction**: [Part 1 — Four Octagons, One Vertex, 540°]({% post_url 2026-10-23-four-octagons-540-degrees-hyperbolic-tiling %}) · [Part 2 — The 81 Ways to Tile a Plane]({% post_url 2026-10-23-two-orbit-tilings-81-isohedral-types %}) · [Part 3 — The Sevenfold Tiling Flat Paper Forbids]({% post_url 2026-10-23-sevenfold-hyperbolic-tiling %}) · Part 4 — Why 60° Refuses to Be Cut in Three (this page).*

The three classical construction problems — trisecting an angle, doubling a cube, squaring a circle — were settled in the nineteenth century. The answers are not about drawing skill. They are about which numbers a finite sequence of compass-and-straightedge operations can produce.

The shortest route to the obstruction is the $60^\circ$ angle. Its trisection would produce $\cos 20^\circ$, and that number satisfies an irreducible cubic. Constructible numbers live in towers of quadratic extensions, so a degree-3 number is out of reach.

**Why it matters.** The trisection cubic is the smallest example of a general phenomenon: an equation can be solvable by radicals and still be unreachable by straightedge and compass. It is the first step on the ladder that ends at the general quintic. It also shows that "impossible" is always relative to an operation set — change the tools, and the obstruction disappears.

---

## 1. The operation budget

A straightedge-and-compass construction starts with two points, draws lines and circles through points already constructed, and takes intersections. The coordinates of every constructed point lie in a field obtained from $\mathbb{Q}$ by adjoining square roots. Equivalently, the construction builds a tower

$$
\mathbb{Q}=F_0\subset F_1\subset\cdots\subset F_n
$$

where each step has degree $2$. Thus if a real number $x$ is constructible, then $\lbrack\mathbb{Q}(x):\mathbb{Q}\rbrack$ is a power of $2$.

The converse needs a caveat: a number of $2$-power degree is not automatically constructible unless its normal closure also has $2$-power degree. For the impossibility proofs below, the necessary condition is enough: an irreducible cubic gives degree $3$, which is not a power of $2$.

Pierre Wantzel proved in 1837 that the general trisection and the duplication of the cube are impossible. Lindemann proved in 1882 that $\pi$ is transcendental, settling the quadrature of the circle.

**Challenge.** Why does the tower condition force the degree to be a power of $2$? Use the multiplicativity of degrees in a tower.

---

## 2. The trisection cubic

Let the angle to be trisected be $\theta$, and set $x=\cos(\theta/3)$. The triple-angle identity is

$$
\cos 3\phi=4\cos^3\phi-3\cos\phi.
$$

With $\phi=\theta/3$, this becomes

$$
4x^3-3x-\cos\theta=0.
$$

So trisection is the problem of solving a cubic. For $\theta=60^\circ$, $\cos\theta=1/2$, and the equation is

$$
8x^3-6x-1=0,
\qquad\text{or}\qquad
x^3-\frac{3}{4}x-\frac{1}{8}=0.
$$

The rational root test allows $\pm 1,\pm 1/2,\pm 1/4,\pm 1/8$. Substitution gives no zero. An irreducible cubic over $\mathbb{Q}$ has degree $3$, so its roots cannot lie in a tower of quadratic extensions.

**Therefore $60^\circ$ cannot be trisected with compass and straightedge.**

The roots are still real. In fact they are

$$
x_1=\cos 20^\circ,\qquad
x_2=\cos 100^\circ,\qquad
x_3=\cos 140^\circ.
$$

The discriminant is

$$
\Delta=-4\left(-\frac{3}{4}\right)^3-27\left(-\frac{1}{8}\right)^2
  =\frac{108}{64}-\frac{27}{64}
  =\frac{81}{64}\gt 0.
$$

A positive discriminant means three distinct real roots. This is the **casus irreducibilis**: the cubic is irreducible over $\mathbb{Q}$ and has three real roots, so expressing those roots in real radicals is impossible; Cardano's formula necessarily passes through complex numbers.

The Galois group is $A_3$, cyclic of order $3$. The cubic is solvable by radicals. It is not constructible by square roots. Those are different statements.

**Challenge.** Verify that the three roots above sum to $0$ and have pairwise sum $-3/4$. Why does a positive discriminant force three real roots, and why does that make the radical expression pass through complex numbers?

---

## 3. What is and is not forbidden

The impossibility is not uniform across angles. Some angles trisect easily:

- $90^\circ/3=30^\circ$, and $\cos 30^\circ=\sqrt{3}/2$ is constructible.
- $45^\circ/3=15^\circ$, and $\cos 15^\circ=(\sqrt{6}+\sqrt{2})/4$ is constructible.

Others do not:

- $60^\circ/3=20^\circ$ fails by the irreducible cubic above.
- $30^\circ/3=10^\circ$ also fails: $\cos 10^\circ$ has degree $6$ over $\mathbb{Q}$, not a power of $2$.

The general criterion is field-theoretic. Given $\theta$ and $c=\cos\theta$, trisection is possible with compass and straightedge exactly when the cubic $4x^3-3x-c$ has a root in a tower of quadratic extensions of $\mathbb{Q}(c)$. If the cubic is irreducible over $\mathbb{Q}(c)$, its root has degree $3$ over that field, and no quadratic tower can reach it.

**Challenge.** Classify $90^\circ$, $45^\circ$, $30^\circ$, and $60^\circ$ as trisectable or not. For each positive case, give the constructed angle; for each negative case, give the degree obstruction.

---

## 4. Three hierarchies, not one

The trisection cubic exposes a hierarchy of constructibility notions:

| Operation set | Allowed extensions | What it can solve | Trisect $60^\circ$? | Square the circle? |
|---|---|---|---|---|
| Compass and unmarked straightedge | square roots; degree $2^k$ | quadratics | no | no |
| Origami | square and cube roots; $\varphi(n)=2^a3^b$ | cubics and quartics | yes | no |
| Marked ruler (neusis) | cubic extensions | cubics | yes | no |
| Quadratrix of Hippias | includes a transcendental curve | encodes $\pi$ | yes | yes |

The table is the point of the whole subject. "Impossible" is always relative to a list of allowed operations. Wantzel's theorem is not a statement about angles; it is a statement about the closure of the constructible field under square roots.

The same hierarchy continues upward. Radical solvability allows any tower whose successive extensions have solvable Galois groups. The general quintic has Galois group $S_5$, which is not solvable, so no radical formula exists. The trisection cubic is solvable by radicals but not constructible; the general quintic is not even solvable by radicals. The four-part quintic series on this site tells that story: [Part 1 — The Indivisible Knot]({% post_url 2026-09-06-quintic-knot-indivisible %}) · [Part 2 — The Wall of Five]({% post_url 2026-09-06-s5-wall-no-radical-formula %}) · [Part 3 — Five Quintics]({% post_url 2026-09-06-five-quintics-gallery %}) · [Part 4 — The Quintic That Gives Up All Its Secrets]({% post_url 2026-09-06-quintic-secrets-galois-group %}).

**Challenge.** The trisection cubic has Galois group $A_3$, which is abelian and therefore solvable. Explain why "solvable by radicals" and "constructible by straightedge and compass" give different answers for the same equation.

---

## 5. Neusis and origami: adding a cubic operation

A **neusis** construction uses a marked ruler. You slide and rotate the ruler until two marks simultaneously satisfy prescribed conditions. This is not a straightedge operation: the ruler carries a fixed length, and the allowable moves include a continuity argument ("slide until it fits"). The extra freedom is exactly enough to solve a cubic. Trisection by neusis was known in antiquity.

**Origami** is more surprising. The Huzita–Hatori axioms formalize paper folding. Axiom 6 — given two points and two lines, make one fold that places the first point on the first line and the second point on the second line — is equivalent to solving a cubic. The field of origami-constructible numbers is closed under square roots and cube roots, but not arbitrary roots. Consequences:

- Any angle can be trisected.
- The cube can be doubled (the cube root of $2$ is available).
- The regular heptagon can be constructed, because $\varphi(7)=6=2\cdot 3$.
- The regular 11-gon cannot, because $\varphi(11)=10=2\cdot 5$ and the factor $5$ is not available.
- The circle cannot be squared, because every origami-constructible number is algebraic and $\sqrt{\pi}$ is transcendental.

The regular $n$-gon criterion is a clean summary. Compass and straightedge give $n=2^k$ times a product of distinct Fermat primes (Gauss–Wantzel). Origami gives the $n$ with $\varphi(n)=2^a3^b$.

**Challenge.** Compute $\varphi(7)$, $\varphi(9)$, $\varphi(11)$, and $\varphi(13)$. Which of the regular $7$-, $9$-, $11$-, and $13$-gons are origami-constructible? Which are compass-and-straightedge constructible?

---

## 6. Squaring the circle: the transcendental wall

To square a circle of radius $r$, the square's side $s$ must satisfy

$$
s^2=\pi r^2,
\qquad\text{so}\qquad
s=r\sqrt{\pi}.
$$

With $r=1$, the required length is $\sqrt{\pi}$. Lindemann's 1882 theorem says $\pi$ is transcendental; if $\sqrt{\pi}$ were algebraic, then $\pi=(\sqrt{\pi})^2$ would be algebraic, a contradiction. So $\sqrt{\pi}$ is transcendental, while every straightedge-and-compass constructible number is algebraic. The quadrature is impossible.

Allow the **quadratrix of Hippias** and the story changes. In a unit setup, the curve has equation

$$
x=y\cot\left(\frac{\pi y}{2}\right).
$$

As $y\to 0$, the limiting intercept is

$$
\lim_{y\to0} y\cot\left(\frac{\pi y}{2}\right)=\frac{2}{\pi}.
$$

If the curve and that intercept are available, ordinary geometric operations produce $\pi$, then $\sqrt{\pi}$, and hence the square. The catch is that the quadratrix is a transcendental curve. It encodes $\pi$ in its definition; providing it is exactly the extra capability that straightedge and compass lack. Lindemann's theorem is not contradicted, because the allowed operations have changed.

**Challenge.** Why does the quadratrix construction not violate Lindemann's theorem? State precisely which hypothesis of the theorem is being dropped.

---

## 7. The boundary is the operation set

The classical problems are often summarized as "three impossible constructions." That phrasing hides the actual theorem. What Wantzel proved is that the constructible numbers form a field with a restricted closure: square roots only. The impossibility of trisection is a statement about that closure, not about the existence of a trisected angle.

The hierarchy is the real content:

- **Constructible** numbers lie in towers of quadratic extensions.
- **Origami/neusis** numbers lie in towers of quadratic and cubic extensions.
- **Radical** numbers lie in towers with solvable Galois groups.
- **General quintic** roots need a non-solvable group, so no radical tower exists at all.

Each row is a different answer to "what operations are allowed?" The $60^\circ$ angle sits at the first boundary; the general quintic sits at the last. Between them is the whole subject of Galois theory.

The tiling series adds a geometric echo. In the Euclidean plane, only the regular triangles, squares, and hexagons tile — all constructible. In the hyperbolic plane, the regular heptagon tiles, even though the Euclidean heptagon is not compass-and-straightedge constructible. The heptagon is not impossible; it is impossible *with that tool set*. Origami can build it. Hyperbolic space can tile with it. Sevenfold symmetry keeps reappearing at the edge of what flat construction allows.

---

## Final challenge

Prove the necessary condition used throughout: if $x$ is constructible, then $\lbrack\mathbb{Q}(x):\mathbb{Q}\rbrack$ is a power of $2$. Then show that $2\cos(2\pi/7)$ satisfies

$$
u^3+u^2-2u-1=0,
$$

prove this cubic is irreducible over $\mathbb{Q}$, and conclude that the regular Euclidean heptagon is not compass-and-straightedge constructible. Finally, explain why origami succeeds where the straightedge fails.

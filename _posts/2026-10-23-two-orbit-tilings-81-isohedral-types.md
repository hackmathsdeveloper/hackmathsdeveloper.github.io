---
title: "The 81 Ways to Tile a Plane — and the Two-Orbit Secret That Escapes the List"
date: 2026-10-23
categories:
  - Tiling Theory
  - Mathematics
tags:
  - isohedral-tilings
  - transitivity-classes
  - wallpaper-groups
  - symmetry-orbits
  - orbifolds
  - grunbaum-shephard
  - pythagorean-tiling
share: true
read_time: true
excerpt: "A tiling is isohedral when its symmetries can carry any tile to any other. Allow exactly two orbits and the Euclidean census jumps from 81 types to 1,270 proper types — with tile density governed by stabilizers, and colored tilings that can differ from their uncolored versions."
---

**Challenge to the reader:** Color the unit-square grid like a checkerboard. Before reading Section 1, decide how many orbits of squares the *color-preserving* symmetry group has. Then forget the colors and ask the same question about the uncolored grid. The two answers are different, and the difference is the whole subject.

*Part 2 of four in the series **The Shape of the Possible: Tilings, Curvature, and Construction**: [Part 1 — Four Octagons, One Vertex, 540°]({% post_url 2026-10-23-four-octagons-540-degrees-hyperbolic-tiling %}) · Part 2 — The 81 Ways to Tile a Plane (this page) · [Part 3 — The Sevenfold Tiling Flat Paper Forbids]({% post_url 2026-10-23-sevenfold-hyperbolic-tiling %}) · [Part 4 — Why 60° Refuses to Be Cut in Three]({% post_url 2026-10-23-why-60-degrees-cannot-be-trisected %}).*

Count the symmetries of a tiling, and you get a group. Let that group act on the tiles, and you get orbits. The number of orbits is the **isohedral number** $k$. For the Euclidean plane, the case $k=1$ has a famous finite answer: **81 types**. The case $k=2$ has a much larger answer: **1,270 proper types**. The jump between those two numbers is the subject of this post.

**Why it matters.** The isohedral number separates two ideas that are constantly confused: having one tile *shape* and having one tile *orbit*. It also explains why a colored pattern can be less symmetric than the same pattern uncolored, and why the Euclidean census cannot be transplanted to the hyperbolic plane.

---

## 1. Symmetry is an action, not a shape

Let $\mathcal{T}$ be a tiling of the plane and let $G=\operatorname{Sym}(\mathcal{T})$ be its full symmetry group: every isometry that maps the tiling to itself. The group $G$ acts on the set $\mathcal{F}$ of tiles. The **orbit** of a tile $T$ is

$$
G\cdot T=\lbrace gT : g\in G\rbrace,
$$

and its **stabilizer** is

$$
G_T=\lbrace g\in G : gT=T\rbrace.
$$

The **isohedral number** $k$ is the number of orbits of this action. A tiling is **$k$-isohedral** when the number of orbits is exactly $k$. The case $k=1$ is called **isohedral**, or face-transitive: every tile can be carried to every other tile by a symmetry of the whole tiling.

Three distinctions matter:

- **Monohedral** means one tile *shape*. It says nothing about symmetry.
- **Isohedral** means one tile *orbit*. Every isohedral tiling is monohedral, but not conversely.
- **Uniform** means one *vertex* orbit. It is a different condition, dual to isohedral in the sense explained in Section 5.

A brick wall built from congruent rectangles is monohedral. If the rows are shifted in an irregular but periodic pattern, the symmetry group may have several tile orbits, so the same rectangles form a non-isohedral monohedral tiling. Shape alone does not determine the orbit count.

The checkerboard is the cleanest example of the color dependence. As an uncolored square tiling it is 1-isohedral: the full $p4m$ symmetry group acts transitively on squares. As a *colored* tiling, the relevant group is the subgroup that preserves the coloring. That subgroup still acts transitively on black squares and transitively on white squares, but it cannot exchange black with white. So the colored checkerboard is 2-isohedral.

---

## 2. The orbit–stabilizer ledger

For a finite group, the orbit–stabilizer theorem says

$$
\lvert G\rvert=\lvert G\cdot T\rvert\cdot\lvert G_T\rvert.
$$

Wallpaper groups are infinite, but the same accounting works with densities. Let $O=\mathbb{E}^2/G$ be the quotient orbifold, of finite area $A_G$. For a $k$-isohedral tiling, $O$ is partitioned into $k$ regions $R_1,\dots,R_k$, one for each tile orbit. The region $R_i$ is the image of a tile $T_i$ modulo its stabilizer, so

$$
\operatorname{Area}(R_i)=\frac{\operatorname{Area}(T_i)}{\lvert G_{T_i}\rvert},
\qquad
\sum_{i=1}^{k}\operatorname{Area}(R_i)=A_G.
$$

Let $N_i$ be the number of tiles from orbit $i$ per unit area. The fraction of the plane covered by that orbit is $N_i\operatorname{Area}(T_i)$, and it equals $\operatorname{Area}(R_i)/A_G$. Therefore

$$
N_i=\frac{1}{\lvert G_{T_i}\rvert\,A_G}.
$$

This is the key formula: **the number density of a tile orbit depends only on the order of its stabilizer, not on the tile's size.** Two orbits with stabilizers of the same order have equal densities. If the orders differ, then

$$
N_1:N_2=\lvert G_{T_2}\rvert:\lvert G_{T_1}\rvert.
$$

The truncated square tiling $4.8.8$ is the clean example. One square and two octagons meet at each vertex. Squares form one orbit, octagons another; both have $D_4$ stabilizers of order $8$. Their number densities are therefore equal, even though the octagons are much larger. The octagons cover more *area*; the squares are smaller but equally numerous. The common "1:1 ratio" is not a statement about tile size — it is a statement about stabilizer orders.

The Pythagorean tiling makes the same point with two sizes of square. Its symmetry group is $p4$, with no reflections, and both square orbits have $C_4$ stabilizers of order $4$. Their number density is 1:1, while their area ratio is $a^2:b^2$.

**Challenge.** A 2-isohedral tiling has one orbit with stabilizer of order $4$ and one with stabilizer of order $8$. Which orbit is denser, and in what ratio? Does the answer depend on the tile areas?

---

## 3. The 81-type census

For the Euclidean plane, the isohedral tilings by topological disks have been classified. Grünbaum and Shephard's incidence-symbol classification gives 93 types; 12 of them require markings to reduce the tile's symmetry, leaving **81 usual isohedral types**. Earlier classifications (Heesch–Kienzle, Bigalke–Wippermann) organized smaller subsets; the 81 is the standard modern count. [Craig Kaplan's survey](https://isohedral.ca/isohedral-tiles-tilings-and-notations/) gives a detailed account of the classification and the marking issue.

A "type" is not a shape. It is a combinatorial symmetry template: which wallpaper group acts, which edges are identified, and how the tile's stabilizer sits inside the group. Within one type, the tile can be deformed continuously. That is why the classification is finite even though the space of tile shapes is infinite. Each isohedral type is associated with one of the 17 wallpaper groups, but the correspondence is many-to-one: several types can share the same group.

The 81 are Euclidean only. In the hyperbolic plane, even the regular tilings $\lbrace p,q\rbrace$ with $1/p+1/q \lt 1/2$ give infinitely many isohedral types before any general classification begins. The Euclidean census is a special feature of the flat plane, not a universal law.

**Challenge.** Why can't the 81 be a classification of tile shapes? Give two different tiles that belong to the same isohedral type, and explain what stays fixed under the deformation.

---

## 4. Two orbits: the census explodes

For $k=2$, the classification is known, and the number is dramatically larger. Delgado, Huson, and Zamorzaeva classified the **proper 2-isohedral tilings** of the Euclidean plane: there are **1,270 types**. "Proper" means every tile touches at least three other tiles. Their combinatorial enumeration produced 2,268 combinatorially distinct 2-isohedral tilings, of which 1,270 are proper. The result appeared in *Geometriae Dedicata* in 1992. [The classification paper](https://doi.org/10.1007/BF00147644) uses two independent methods: a geometric splitting-and-gluing construction and an enumeration of Delaney–Dress symbols.

So the jump from one orbit to two is not a small perturbation: $81\to 1{,}270$. Adding a second transitivity class multiplies the combinatorial choices — which group, which two stabilizers, how the two regions partition the quotient orbifold, and how the tile boundaries match.

For $k\ge 3$, the lists grow further, and there is no single small census with the cultural status of the 81. Worse, $k$ itself is not bounded. Socolar's hexagonal parquet construction produces $k$-isohedral monotiles with arbitrarily large $k$, using colored edge-matching rules (or a multiply connected or three-dimensional tile). A single prototile can be forced into an arbitrarily large number of symmetry orbits. [Socolar's paper](https://arxiv.org/abs/0708.2663) is the standard reference. There is no largest isohedral number.

**Challenge.** The 81 counts 1-isohedral types; the 1,270 counts proper 2-isohedral types. Why is it not legitimate to compare these numbers as if they measured the same kind of object? Name two extra choices that appear when $k=2$.

---

## 5. Two orbits in the wild

**The truncated square tiling, 4.8.8.** One square and two octagons meet at each vertex. The symmetry group is $p4m$. Squares form one orbit, octagons another; both have $D_4$ stabilizers of order $8$, so the number densities are equal even though the octagons have larger area. This is the cleanest uniform example of a 2-isohedral tiling.

**The Pythagorean tiling.** Squares of two sizes, arranged so every tile has four opposite-size side-neighbours. The symmetry group is $p4$, chiral, with no reflections. Small squares form one orbit and large squares another. Their number density is 1:1; their area ratio is $a^2:b^2$. The pattern is named for the dissection it encodes: a square of side $\sqrt{a^2+b^2}$ is cut into one square of side $a$, one of side $b$, and four right triangles.

**The checkerboard.** As a colored tiling, it is 2-isohedral; as an uncolored tiling, it is 1-isohedral. This is not a contradiction: the isohedral number is computed relative to the symmetry group that preserves the structure you care about.

**A dual pair.** The omnitruncated $\lbrace 7,3\rbrace$ tiling, with vertex configuration $4.6.14$, is uniform: all vertices are equivalent. It has three face orbits — squares, hexagons, and 14-gons. Its dual is the 3-7 kisrhombille, a tiling by congruent right triangles. The dual is 1-isohedral (all triangles are equivalent) but not uniform: its triangles have three vertex classes, corresponding to the three face types of $4.6.14$. Duality swaps vertices and faces, so "uniform" becomes "isohedral" and face orbits become vertex orbits. Part 3 draws this pair.

**Challenge.** The 3-7 kisrhombille is 1-isohedral but not uniform. Its dual $4.6.14$ is uniform but 3-isohedral. Explain why neither statement contradicts the other, using the vertex–face duality.

---

## 6. The quotient picture

The quotient $O=\mathbb{E}^2/G$ is a two-dimensional orbifold. For the 17 wallpaper groups, $O$ is a sphere, disk, projective plane, or torus with a finite list of cone points, mirror edges, and corner reflectors. Conway's orbifold notation encodes this data compactly.

A tiling with symmetry group $G$ is the same thing as a partition of $O$ into tile regions, together with the rule that lifts the partition back to the plane. For a $k$-isohedral tiling, the partition has exactly $k$ regions. For a 1-isohedral tiling, the single region is $T/G_T$.

This is why the counts behave the way they do. The 81 isohedral types are the ways a disk-shaped tile region can sit in a Euclidean orbifold. The 1,270 proper 2-isohedral types are the ways two regions can partition the orbifold, with the additional constraint that every tile touches at least three others. More regions mean more combinatorial partitions, and the number grows quickly.

Delaney–Dress symbols are the standard combinatorial encoding used to enumerate these partitions. They replace the geometry by a finite labelled complex, which is why a computer can exhaust the possibilities.

**Challenge.** Explain why a 1-isohedral tiling has one tile region in $O$ but the tile itself need not be a fundamental domain of $G$. What is the correct area relationship?

---

## 7. Why the orbit count is the right invariant

Symmetry is not a property of a shape; it is a property of a structured object and the transformations you allow. The checkerboard makes this vivid: the same squares are 1-isohedral or 2-isohedral depending on whether the colors count as part of the structure.

The orbit count is the natural invariant because it is what survives when you forget the individual tiles and keep only the action. It connects three ideas:

- **Crystallography.** The 17 wallpaper groups classify periodic patterns; isohedral types refine each group by how the tiles sit inside it.
- **Coloring problems.** A proper coloring, a marking, or an edge label can break symmetry and increase $k$. The isohedral number measures exactly how much symmetry the decoration destroys.
- **Aperiodic order.** Socolar's arbitrarily large $k$ shows that local matching rules can force a pattern to have many symmetry orbits. The gap between "one tile shape" and "one symmetry orbit" can be arbitrarily wide.

Part 1 supplied the curvature that decides which regular tiles exist. Part 3 supplies an infinite hyperbolic family where the Euclidean 81-type census has no analogue. Part 4 shows that even the regular heptagon — a tile that lives happily in hyperbolic space — is unreachable with compass and straightedge. The common thread is that "possible" always means "possible under a specified structure and a specified set of operations."

---

## Final challenge

Color the unit-square grid with period $2$ in both directions, using the four colors $(i\bmod 2, j\bmod 2)$ for the square in column $i$ and row $j$. Show that the color-preserving symmetry group has four tile orbits, so the colored tiling is 4-isohedral. Then merge two of the four colors and recompute $k$. What does the change tell you about the statement "the isohedral number is a property of the tiling alone"?

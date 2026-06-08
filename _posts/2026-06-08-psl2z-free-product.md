---
title: "The Modular Group's Secret: PSL₂(ℤ) Is a Free Product — And Every Element Is a Unique Alternating Word"
date: 2026-06-08
categories:
  - Group Theory
  - Mathematics
tags:
  - modular-group
  - psl2z
  - free-product
  - group-presentation
  - bass-serre-theory
  - generators
  - cyclic-groups
share: true
read_time: true
excerpt: "PSL₂(ℤ), the modular group, is isomorphic to ℤ/2ℤ * ℤ/3ℤ — the free product of a cyclic group of order 2 and a cyclic group of order 3. This means every element can be written uniquely as an alternating word in the generators s and u, with no hidden relations beyond s²=1 and u³=1."
---

**Challenge to the reader:** Write the group element $t = su$ in $PSL_2(\mathbb{Z})$. Since $s^2 = 1$, simplify $t^{-1} = u^2 s$ and verify that $(su)^{3} = 1$ by writing it out as an alternating word and applying the relations.

---

## 1. Defining the Quotient Group

The group $PSL_2(\mathbb{Z})$ (the **Modular Group**) is defined as the quotient:

$$
PSL_2(\mathbb{Z}) = SL_2(\mathbb{Z}) / \{\pm I\}.
$$

The elements of this group are equivalence classes (cosets) of the form $[A] = \{A, -A\}$ for any matrix $A \in SL_2(\mathbb{Z})$. The identity element of this quotient group is $[I] = \{I, -I\}$.

---

## 2. Finding the Generator of Order 2

Let $s$ be the image of the matrix $S$ in the quotient group:

$$
s = [S] = \left[ \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \right].
$$

In $SL_2(\mathbb{Z})$, we know that:

$$
S^2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I.
$$

When we project this into the quotient group $PSL_2(\mathbb{Z})$, the $-I$ becomes the identity element $[I]$:

$$
s^2 = [S^2] = [-I] = [I].
$$

Thus, **$s$ is an element of order 2**.

---

## 3. Finding the Generator of Order 3

Let $u$ be the image of the matrix product $ST$ in the quotient group:

$$
u = [ST] = \left[ \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \right] = \left[ \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix} \right].
$$

Let us calculate $(ST)^3$ in $SL_2(\mathbb{Z})$:

$$
(ST)^2 = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix},
$$

$$
(ST)^3 = \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I.
$$

Projecting into the quotient group:

$$
u^3 = [(ST)^3] = [-I] = [I].
$$

Thus, **$u$ is an element of order 3**.

---

## 4. Proving They Generate the Whole Group

We know $S$ and $T$ generate $SL_2(\mathbb{Z})$. Therefore, their images $s = [S]$ and $t = [T]$ generate $PSL_2(\mathbb{Z})$.

Notice that $u = [ST] = [S][T] = st$. Because $s$ has order 2, its inverse is itself ($s^{-1} = s$). We can solve for $t$:

$$
t = s^{-1}u = su.
$$

Since $s$ and $t$ generate the group, and $t$ can be written entirely in terms of $s$ and $u$, **the elements $s$ and $u$ generate all of $PSL_2(\mathbb{Z})$**.

**Challenge to the reader:** Express the matrix $\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \end{pmatrix}$ as a product of $s$ and $u$ in $PSL_2(\mathbb{Z})$. Write out the alternating word explicitly.

---

## 5. Realization as the Free Product ℤ/2ℤ * ℤ/3ℤ

A group presentation describes a group by its generators and relations. For $PSL_2(\mathbb{Z})$, the generators are $s$ and $u$.

The relations we found are:
1. $s^2 = 1$ (identity)
2. $u^3 = 1$ (identity)

A deep theorem in group theory (often proved using Bass-Serre theory or by analyzing the action of the group on the upper half-plane) states that **there are no other relations** between $s$ and $u$.

Therefore, the presentation of the group is exactly:

$$
PSL_2(\mathbb{Z}) = \langle s, u \mid s^2 = 1, u^3 = 1 \rangle.
$$

This is the exact definition of the **free product** of the cyclic group of order 2 ($\mathbb{Z}/2\mathbb{Z} = \langle s \mid s^2=1 \rangle$) and the cyclic group of order 3 ($\mathbb{Z}/3\mathbb{Z} = \langle u \mid u^3=1 \rangle$):

$$
PSL_2(\mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/3\mathbb{Z}.
$$

---

## 6. What This Means Practically

Because it is a *free* product, every single element in $PSL_2(\mathbb{Z})$ can be written **uniquely** as an alternating word of $s$ and powers of $u$ (where the powers of $u$ are either $u$ or $u^2$, since $u^3 = 1$).

For example, the elements look like:

- $s$
- $u, u^2$
- $su, su^2, us, u^2s$
- $sus, su^2s, usu, u^2su, \dots$

There is no "simplification" possible other than replacing $s^2$ with $1$ and $u^3$ with $1$. This alternating word structure is the hallmark of a free product!

---

## 7. Deeper Significance

The fact that $PSL_2(\mathbb{Z})$ is a free product explains its rich but completely understood structure. Free products are the group-theoretic analog of the free monoid: just as strings in an alphabet form the free monoid (no relations), alternating words in $s$ and $u$ form the free product (only the relations $s^2=1, u^3=1$).

This has profound geometric meaning. $PSL_2(\mathbb{Z})$ acts on the upper half-plane by Möbius transformations, and the quotient is the modular surface — a sphere with one puncture. The free product structure corresponds to the fact that the fundamental group of this punctured sphere is indeed $\mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/3\mathbb{Z}$.

**Final challenge:** Using the free product structure, prove that $PSL_2(\mathbb{Z})$ contains no elements of finite order other than 1, 2, and 3. (Hint: in a free product, the order of an element is determined by the orders of the factors; any element of finite order must be conjugate to an element of one of the free factors.)

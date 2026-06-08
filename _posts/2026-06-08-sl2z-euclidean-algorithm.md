---
title: "The Euclidean Algorithm Wears a Matrix Mask: How S and T Reduce Any SL₂(ℤ) Element to Identity"
date: 2026-06-08
categories:
  - Group Theory
  - Mathematics
tags:
  - sl2z
  - euclidean-algorithm
  - generators
  - continued-fractions
  - matrix-reduction
  - group-theory
  - modular-group
share: true
read_time: true
excerpt: "To prove S and T generate SL₂(ℤ), you use the Euclidean algorithm — the same one you learned for integers. Multiply a matrix on the right by T⁻ⁿ to reduce the top-left entry, then by S to swap rows, and repeat. Each step strictly decreases entries until you hit ±I, proving every matrix is a finite word in S and T."
---

**Challenge to the reader:** Start with $M = \begin{pmatrix} 5 & 2 \\\\ 2 & 1 \end{pmatrix}$. Apply one step of the reduction: divide $5$ by $2$ (quotient $2$, remainder $1$), right-multiply by $T^{-2}$, then by $S$. What matrix do you get? Compare the entries with the original — notice they got smaller.

---

## 1. Basic Operations

First, note what these generators do:

**Powers of T:**

$$
T^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}, \qquad T^{-n} = \begin{pmatrix} 1 & -n \\ 0 & 1 \end{pmatrix}.
$$

**Action on a matrix** $M = \begin{pmatrix} a & b \\\\ c & d \end{pmatrix}$:
- **Right multiplication by $T^n$:** Adds $n$ times column 2 to column 1 (an elementary column operation).
- **Right multiplication by $S$:** Swaps columns with a sign change: $\begin{pmatrix} a & b \\\\ c & d \end{pmatrix} S = \begin{pmatrix} -b & a \\\\ -d & c \end{pmatrix}$.

---

## 2. The Reduction Algorithm

Given any $M = \begin{pmatrix} a & b \\\\ c & d \end{pmatrix} \in SL_2(\mathbb{Z})$, we reduce it to $\pm I$:

**Step 1: If $c = 0$.** Then $ad = 1$, so $a = d = \pm 1$, and $M = \pm T^b$. Done — it is already a product of generators.

**Step 2: If $c \neq 0$.** Use the division algorithm: $a = qc + r$ where $0 \le r \lt |c|$.
- Multiply by $T^{-q}$ on the right to reduce the top-left entry from $a$ to $r$.
- Multiply by $S$ to swap the column entries (bringing $c$ to the top-left position).
- Repeat until the bottom-left entry becomes $0$, then fall back to Step 1.

The process terminates because the absolute values of the entries strictly decrease at each stage — exactly as in the Euclidean algorithm.

**Challenge to the reader:** Apply the reduction to $\begin{pmatrix} 7 & 3 \\\\ 3 & 1 \end{pmatrix}$. Perform the Euclidean steps: $7 = 2 \cdot 3 + 1$, right-multiply by $T^{-2}$, then by $S$. Record the sequence of $T$ and $S$ multiplications that leads to $\pm I$.

---

## 3. Concrete Example 1

Let us generate $M = \begin{pmatrix} 2 & 1 \\\\ 1 & 1 \end{pmatrix}$:

Working backwards from $M$ to $I$:

$$
\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times T^{-1}} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} 0 & 1 \\ -1 & 1 \end{pmatrix} \xrightarrow{\times T} \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = S^2.
$$

**Therefore:**

$$
M = S^2 \cdot S^{-1} \cdot T^{-1} \cdot S^{-1} \cdot T = S \cdot T^{-1} \cdot S \cdot T.
$$

Verification:

$$
S \cdot T^{-1} \cdot S \cdot T = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \;\checkmark
$$

---

## 4. Concrete Example 2

Generate $M = \begin{pmatrix} 3 & 2 \\\\ 1 & 1 \end{pmatrix}$:

Using the Euclidean algorithm on the first column $(3, 1)$:
- $3 = 3 \cdot 1 + 0$

$$
\begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times T^{-3}} \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} -1 & 0 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times T} \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

**Therefore:** $M = S^2 \cdot S^{-1} \cdot T^{-1} \cdot S^{-1} \cdot T^3 = S \cdot T^{-1} \cdot S \cdot T^3$.

---

## 5. The General Pattern

Any matrix $\begin{pmatrix} a & b \\\\ c & d \end{pmatrix}$ can be written as:

$$
M = \pm T^{a_1} S T^{a_2} S \cdots T^{a_k} S T^{a_{k+1}},
$$

where the $a_i$ come from the **continued fraction expansion** of $a/c$ (when $c \neq 0$).

---

## 6. Why This Always Works

1. **Determinant preservation:** Both $S$ and $T$ have $\det = 1$, so all products stay in $SL_2(\mathbb{Z})$.
2. **Euclidean algorithm terminates:** The entries strictly decrease in absolute value.
3. **Eventually reach $\pm I$:** Which are both powers of $S$ (since $S^2 = -I$, $S^4 = I$).
4. **Reverse the process:** If $M \cdot (\text{product}) = I$, then $M = (\text{product})^{-1}$.

This proves that **every element of $SL_2(\mathbb{Z})$ is a finite product of $S$ and $T$!**

---

## 7. Deeper Significance

This proof reveals a beautiful unity: the Euclidean algorithm for integers is the same algorithm that generates $SL_2(\mathbb{Z})$. The continued fraction expansion of $a/c$ is encoded in the sequence $a_1, a_2, \dots, a_k$ — the exponents of $T$ in the word:

$$
\frac{a}{c} = a_1 + \cfrac{1}{a_2 + \cfrac{1}{\ddots + \cfrac{1}{a_k}}}.
$$

This is not a coincidence: it is the reason why modular forms, Diophantine approximation, and the geometry of the upper half-plane are all deeply intertwined. The same matrices that encode rational approximations of real numbers also act as symmetries of the hyperbolic plane.

**Final challenge:** Take a real number $\alpha = \frac{1+\sqrt{5}}{2}$ (the golden ratio). Its continued fraction is $[1; 1, 1, 1, \dots]$. Write the corresponding infinite product of generators $\cdots T S T S T S \cdots$. This infinite word in $S$ and $T$ encodes the "most irrational" number — the one least well approximated by rationals. Explain why this infinite product does not converge in $SL_2(\mathbb{Z})$, but its truncations produce the convergents of the golden ratio.

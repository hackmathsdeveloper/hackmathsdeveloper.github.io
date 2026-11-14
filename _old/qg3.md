
# How S and T Generate All of SL₂(ℤ)

The key idea is to use the **Euclidean algorithm** to reduce any matrix to the identity. Here's how it works:

## Basic Operations

First, note what these generators do:

**Powers of T:**
$$T^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}, \quad T^{-n} = \begin{pmatrix} 1 & -n \\ 0 & 1 \end{pmatrix}$$

**Action on a matrix** $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
- **Right multiplication by Tⁿ**: Adds n times column 2 to column 1
- **Right multiplication by S**: Swaps columns (with sign changes)

## The Reduction Algorithm

Given any $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in SL_2(\mathbb{Z})$, we reduce it to ±I:

### Step-by-Step Process:

1. **If c = 0**: Then ad = 1, so a = d = ±1, and M = ±Tᵇ

2. **If c ≠ 0**: Use division algorithm: a = qc + r where 0 ≤ r < |c|
   - Multiply by T⁻q on the right to reduce the top-left entry
   - Multiply by S to swap entries
   - Repeat until you reach the identity

## Concrete Example 1

Let's generate $M = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$:

**Working backwards from M to I:**

$$\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times T^{-1}} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} 0 & 1 \\ -1 & 1 \end{pmatrix} \xrightarrow{\times T} \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = S^2$$

**Therefore:**
$$M = S^2 \cdot S^{-1} \cdot T^{-1} \cdot S^{-1} \cdot T = S \cdot T^{-1} \cdot S \cdot T$$

Let's verify:
$$S \cdot T^{-1} \cdot S \cdot T = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \checkmark$$

## Concrete Example 2

Generate $M = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}$:

Using the Euclidean algorithm on the first column (3, 1):
- 3 = 3(1) + 0

$$\begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times T^{-3}} \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} -1 & 0 \\ 1 & 1 \end{pmatrix} \xrightarrow{\times T} \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix} \xrightarrow{\times S} \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Therefore:** $M = S^2 \cdot S^{-1} \cdot T^{-1} \cdot S^{-1} \cdot T^3 = S \cdot T^{-1} \cdot S \cdot T^3$

## General Pattern

**Any matrix** $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ can be written as:

$$M = \pm T^{a_1} S T^{a_2} S \cdots T^{a_k} S T^{a_{k+1}}$$

where the $a_i$ come from the **continued fraction expansion** of a/c (when c ≠ 0).

## Why This Always Works

1. **Determinant preservation**: Both S and T have det = 1, so all products stay in SL₂(ℤ)

2. **Euclidean algorithm terminates**: The entries strictly decrease in absolute value

3. **Eventually reach ±I**: Which are both powers of S (since S² = -I, S⁴ = I)

4. **Reverse the process**: If M·(product) = I, then M = (product)⁻¹

This proves that **every element of SL₂(ℤ) is a finite product of S and T**!

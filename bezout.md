
The Bézout Identity states that for any integers $a$ and $b$, there exist integers $x$ and $y$ such that:
$$ ax + by = \gcd(a, b) $$

Furthermore, the linear Diophantine equation $ax + by = c$ has integer solutions **if and only if** $\gcd(a, b) \mid c$.

Below is an extensive collection of examples categorized by technique and complexity. Each demonstrates a different facet of applying Bézout’s Identity.

---

### Category 1: Standard Extended Euclidean Algorithm (EEA)
*The foundational technique. Best for general cases where no shortcuts are obvious.*

#### Example 1.1: Basic Positive Coefficients
**Problem:** Solve $48x + 18y = 6$.

1.  **GCD Check:** $\gcd(48, 18) = 6$. Since $6 \mid 6$, solutions exist.
2.  **Euclidean Algorithm:**
    $$ \begin{aligned} 48 &= 2 \cdot 18 + 12 \\ 18 &= 1 \cdot 12 + 6 \\ 12 &= 2 \cdot 6 + 0 \end{aligned} $$
3.  **Back-Substitution:**
    $$ \begin{aligned} 6 &= 18 - 1 \cdot 12 \\ &= 18 - 1(48 - 2 \cdot 18) \\ &= 18 - 48 + 2 \cdot 18 \\ &= 3(18) - 1(48) \end{aligned} $$
4.  **Particular Solution:** $48(-1) + 18(3) = 6 \implies x_0 = -1, y_0 = 3$.
5.  **General Solution:** Divide coefficients by $\gcd=6$:
    $$ \boxed{x = -1 + 3t, \quad y = 3 - 8t, \quad t \in \mathbb{Z}} $$

#### Example 1.2: Coprime Coefficients with Large Numbers
**Problem:** Solve $127x + 53y = 1$.

1.  **Euclidean Algorithm:**
    $$ \begin{aligned} 127 &= 2 \cdot 53 + 21 \\ 53 &= 2 \cdot 21 + 11 \\ 21 &= 1 \cdot 11 + 10 \\ 11 &= 1 \cdot 10 + 1 \end{aligned} $$
2.  **Back-Substitution:**
    $$ \begin{aligned} 1 &= 11 - 10 \\ &= 11 - (21 - 11) = 2(11) - 21 \\ &= 2(53 - 2 \cdot 21) - 21 = 2(53) - 5(21) \\ &= 2(53) - 5(127 - 2 \cdot 53) = 12(53) - 5(127) \end{aligned} $$
3.  **Result:** $127(-5) + 53(12) = 1$.
    $$ \boxed{x = -5 + 53t, \quad y = 12 - 127t} $$

---

### Category 2: Modular Arithmetic / Congruence Method
*Best when one coefficient is small or has an obvious inverse.*

#### Example 2.1: Small Modulus Shortcut
**Problem:** Solve $7x + 23y = 5$.

1.  Reduce mod 7: $23y \equiv 5 \pmod 7 \implies 2y \equiv 5 \pmod 7$.
2.  Multiply by 4 (inverse of 2 mod 7): $y \equiv 20 \equiv 6 \pmod 7$.
3.  Set $y_0 = 6$: $7x + 23(6) = 5 \implies 7x = 5 - 138 = -133 \implies x_0 = -19$.
4.  **General Solution:**
    $$ \boxed{x = -19 + 23t, \quad y = 6 - 7t} $$

#### Example 2.2: Negative Residue Trick
**Problem:** Solve $13x + 37y = 4$.

1.  Reduce mod 13: $37y \equiv 4 \pmod{13} \implies (-2)y \equiv 4 \pmod{13}$ (since $37 = 3\cdot13 - 2$).
2.  $-2y \equiv 4 \implies y \equiv -2 \equiv 11 \pmod{13}$.
3.  But using $y_0 = -2$ is simpler: $13x + 37(-2) = 4 \implies 13x = 4 + 74 = 78 \implies x_0 = 6$.
4.  **General Solution:**
    $$ \boxed{x = 6 + 37t, \quad y = -2 - 13t} $$

> **Key Insight:** Always choose the residue with smallest absolute value. $y \equiv -2$ is computationally superior to $y \equiv 11$.

---

### Category 3: Inspection & Algebraic Manipulation
*For problems designed to have "nice" numbers or when coefficients share structure.*

#### Example 3.1: Difference of Squares Structure
**Problem:** Solve $15x + 16y = 1$.

Notice $16 - 15 = 1$. Immediately:
$$ 16(1) + 15(-1) = 1 \implies 15(-1) + 16(1) = 1 $$
$$ \boxed{x = -1 + 16t, \quad y = 1 - 15t} $$

#### Example 3.2: Scaling from a Known Identity
**Problem:** Solve $39x + 26y = 65$.

1.  Notice all divisible by 13: $3(3x) + 2(2y) = 5 \cdot 13$. Divide by 13:
    $$ 3x + 2y = 5 $$
2.  Inspect: $3(1) + 2(1) = 5$. So $x_0 = 1, y_0 = 1$.
3.  **General Solution** (for reduced equation):
    $$ \boxed{x = 1 + 2t, \quad y = 1 - 3t} $$

#### Example 3.3: Using $a \cdot 1 - b \cdot k$ Pattern
**Problem:** Solve $100x + 7y = 3$.

1.  Note $100 = 14 \cdot 7 + 2$, so $100 - 14 \cdot 7 = 2$.
2.  We need 3, not 2. Multiply identity by... wait, $\gcd(100,7)=1$, so we first find Bézout for 1:
    $$ 100 - 14 \cdot 7 = 2 \quad \text{and} \quad 7 - 3 \cdot 2 = 1 $$
    Combine: $7 - 3(100 - 14 \cdot 7) = 1 \implies -3(100) + 43(7) = 1$.
3.  Scale by 3: $100(-9) + 7(129) = 3$.
    $$ \boxed{x = -9 + 7t, \quad y = 129 - 100t} $$

---

### Category 4: Blankinship’s Matrix Method
*Systematic tabular approach eliminating back-substitution errors.*

#### Example 4.1: Three-Row Variant for Tracking
**Problem:** Solve $97x + 35y = 1$.

Initialize: $\begin{pmatrix} 97 & 1 & 0 \\ 35 & 0 & 1 \end{pmatrix}$

| Operation | Row 1 | Row 2 |
|-----------|-------|-------|
| Init | $(97, 1, 0)$ | $(35, 0, 1)$ |
| $R_1 - 2R_2$ | $(27, 1, -2)$ | $(35, 0, 1)$ |
| $R_2 - R_1$ | $(27, 1, -2)$ | $(8, -1, 3)$ |
| $R_1 - 3R_2$ | $(3, 4, -11)$ | $(8, -1, 3)$ |
| $R_2 - 2R_1$ | $(3, 4, -11)$ | $(2, -9, 25)$ |
| $R_1 - R_2$ | $(1, 13, -36)$ | $(2, -9, 25)$ |

Read GCD row: $97(13) + 35(-36) = 1261 - 1260 = 1$ ✓
$$ \boxed{x = 13 + 35t, \quad y = -36 - 97t} $$

---

### Category 5: Special Cases & Edge Conditions

#### Example 5.1: One Coefficient is Zero
**Problem:** Solve $0x + 7y = 14$.

$\gcd(0, 7) = 7$, and $7 \mid 14$. Solutions exist.
$7y = 14 \implies y = 2$. $x$ can be **any** integer.
$$ \boxed{x = t, \quad y = 2, \quad t \in \mathbb{Z}} $$

#### Example 5.2: No Solution Exists
**Problem:** Solve $6x + 9y = 4$.

$\gcd(6, 9) = 3$. Does $3 \mid 4$? **No.**
$$ \boxed{\text{No integer solutions exist.}} $$

#### Example 5.3: Negative Coefficients
**Problem:** Solve $-17x + 29y = 1$.

Treat as $17(-x) + 29y = 1$. From earlier work, $17(12) + 29(-7) = 1$.
So $-x = 12 \implies x = -12$, $y = -7$.
$$ \boxed{x = -12 - 29t, \quad y = -7 - 17t} $$
*(Note: sign of $t$ term for $x$ flips because original coefficient was negative.)*

#### Example 5.4: Both Coefficients Negative
**Problem:** Solve $-4x - 6y = 8$.

Equivalent to $4x + 6y = -8$. $\gcd(4,6)=2$, $2 \mid (-8)$ ✓.
Reduce: $2x + 3y = -4$. Inspect: $2(-2) + 3(0) = -4$.
$$ \boxed{x = -2 + 3t, \quad y = 0 - 2t = -2t} $$

---

### Category 6: Parametrization Variants & Minimal Solutions

#### Example 6.1: Finding the Smallest Positive $x$
From Example 1.2: $x = -5 + 53t$. Find smallest positive $x$:
$$ -5 + 53t > 0 \implies t > 5/53 \implies t_{\min} = 1 $$
$$ x_{\min+} = -5 + 53 = 48, \quad y = 12 - 127 = -115 $$

#### Example 6.2: Minimizing $|x| + |y|$
From Example 1.1: $x = -1 + 3t, \; y = 3 - 8t$. Define $f(t) = |-1+3t| + |3-8t|$.
Test near zeros: $t=0 \to 1+3=4$; $t=1 \to 2+5=7$; $t=-1 \to 4+11=15$.
Minimum at $t=0$: $\boxed{(x,y)=(-1,3)}$ with sum 4.

#### Example 6.3: Alternative Parametrization Centered at Particular Solution
Any valid particular solution generates the same set. From Example 2.1, both are valid:
$$ (-19 + 23t, \; 6 - 7t) \quad \text{AND} \quad (4 + 23s, \; -1 - 7s) $$
These describe the **identical** set of lattice points; they just index them differently ($s = t - 1$).

---

### Quick Reference: Decision Flowchart

```
Given ax + by = c
        │
        ▼
Compute d = gcd(a,b)
        │
   d divides c? ──── NO ──→ No solutions
        │ YES
        ▼
Is one coefficient ±1? ── YES → Trivial: x or y = ±c
        │ NO
        ▼
Are coefficients small (< 20)? ── YES → Inspection / Modular
        │ NO
        ▼
Need error-proof computation? ── YES → Blankinship Matrix
        │ NO
        ▼
Standard Extended Euclidean Algorithm
        │
        ▼
Parametrize: x = x₀ + (b/d)t, y = y₀ - (a/d)t
```

### Common Pitfalls to Avoid

| Pitfall | Wrong | Correct |
|---------|-------|---------|
| Forgetting to divide step size by gcd | $x = x_0 + bt$ | $x = x_0 + \frac{b}{d}t$ |
| Sign error in parametrization | $x = x_0 + \frac{b}{d}t, \; y = y_0 + \frac{a}{d}t$ | Signs must be **opposite** |
| Not checking solvability first | Solving $6x+9y=4$ | Check $\gcd \mid c$ first |
| Confusing which variable gets which coefficient | $x = x_0 + \frac{a}{d}t$ | $x$ pairs with $\frac{b}{d}$, $y$ with $\frac{a}{d}$ |
| Back-substitution arithmetic errors | Losing track of signs | Use Blankinship matrix or verify each step |

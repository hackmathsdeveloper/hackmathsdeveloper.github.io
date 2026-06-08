
Here are the elements for each of the five groups listed, along with the verification that each has an order (size) of 4.

### 1. $\mathbf{Z}/(4)$
This is the group of integers modulo 4 under addition.
*   **Elements:** $\{0, 1, 2, 3\}$
*   **Verification:** There are exactly **4** distinct elements.

### 2. $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$
This is the direct product of the group $\mathbf{Z}/(2)$ with itself. The elements are ordered pairs $(a, b)$ where $a, b \in \{0, 1\}$.
*   **Elements:** $\{(0,0), (0,1), (1,0), (1,1)\}$
*   **Verification:** There are exactly **4** distinct pairs.
    *(Note: This is the Klein four-group, where every non-identity element has order 2).*

### 3. $(\mathbf{Z}/(5))^{\times}$
This is the multiplicative group of units modulo 5. The elements are integers $k$ such that $1 \le k < 5$ and $\gcd(k, 5) = 1$. Since 5 is prime, all non-zero residues are units.
*   **Elements:** $\{1, 2, 3, 4\}$
*   **Verification:** There are exactly **4** elements.

### 4. $(\mathbf{Z}/(8))^{\times}$
This is the multiplicative group of units modulo 8. The elements are integers $k$ such that $1 \le k < 8$ and $\gcd(k, 8) = 1$. Since $8 = 2^3$, the units are the odd numbers less than 8.
*   **Elements:** $\{1, 3, 5, 7\}$
*   **Verification:** There are exactly **4** elements.
    *(Note: Like the second group, this is also isomorphic to the Klein four-group).*

### 5. $(\mathbf{Z}/(12))^{\times}$
This is the multiplicative group of units modulo 12. The elements are integers $k$ such that $1 \le k < 12$ and $\gcd(k, 12) = 1$. Since $12 = 2^2 \cdot 3$, we look for numbers not divisible by 2 or 3.
*   Candidates: $1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11$
*   Remove evens (divisible by 2): $1, 3, 5, 7, 9, 11$
*   Remove multiples of 3: $1, 5, 7, 11$
*   **Elements:** $\{1, 5, 7, 11\}$
*   **Verification:** There are exactly **4** elements.

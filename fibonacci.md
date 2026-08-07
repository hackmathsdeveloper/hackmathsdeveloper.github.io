
The Fibonacci sequence, defined by $F_0 = 0$, $F_1 = 1$, and $F_n = F_{n-1} + F_{n-2}$ for $n \geq 2$, is arguably the most studied sequence in number theory. While often introduced via combinatorics or nature, its true depth lies in its **algebraic structure, divisibility properties, and connections to quadratic fields**.

Below is an elaboration on the key patterns of Fibonacci numbers specifically through the lens of number theory.

---

### 1. Divisibility and GCD Structure
The Fibonacci sequence forms a **strong divisibility sequence**, which is its most fundamental number-theoretic property.

#### The GCD Theorem
For any positive integers $m$ and $n$:
$$ \gcd(F_m, F_n) = F_{\gcd(m, n)} $$
**Implications:**
-   $F_m \mid F_n$ if and only if $m \mid n$ (for $m > 2$).
-   Consecutive Fibonacci numbers are always coprime: $\gcd(F_n, F_{n+1}) = F_1 = 1$.
-   This property makes the sequence a prototype for **Lucas sequences**, linking it to elliptic curves and primality testing.

#### p-adic Valuation (Lifting The Exponent)
The exact power of a prime $p$ dividing $F_n$ follows precise rules. For $p=2$:
$$ \nu_2(F_n) = \begin{cases} 0 & \text{if } n \equiv 1, 2 \pmod 3 \\ 1 & \text{if } n \equiv 3 \pmod 6 \\ 3 & \text{if } n \equiv 6 \pmod{12} \\ \nu_2(n) + 2 & \text{if } n \equiv 0 \pmod{12} \end{cases} $$
For odd primes $p$, if $z(p)$ is the **rank of apparition** (the smallest $k$ such that $p \mid F_k$), then:
$$ \nu_p(F_n) = \nu_p(n) + \nu_p(F_{z(p)}) \quad \text{when } z(p) \mid n $$
This is analogous to the Lifting The Exponent Lemma (LTE) and is crucial in Diophantine analysis involving Fibonacci numbers.

---

### 2. Modular Arithmetic and Periodicity

#### Pisano Periods
For any integer $m \geq 2$, the sequence $(F_n \bmod m)$ is **purely periodic**. The period length is denoted $\pi(m)$.
-   $\pi(2) = 3$, $\pi(3) = 8$, $\pi(5) = 20$, $\pi(10) = 60$.
-   If $m = p_1^{e_1} \cdots p_k^{e_k}$, then $\pi(m) = \operatorname{lcm}(\pi(p_1^{e_1}), \dots, \pi(p_k^{e_k}))$.
-   **Wall’s Conjecture (Open):** $\pi(p^e) = p^{e-1} \pi(p)$ for all primes $p$ and $e \geq 1$. Verified for all $p < 10^{14}$ but unproven in general. This connects to Wieferich primes in base related to the golden ratio.

#### Quadratic Residue Characterization
Whether $p \mid F_n$ depends on the Legendre symbol $\left(\frac{5}{p}\right)$:
$$ F_{p - \left(\frac{5}{p}\right)} \equiv 0 \pmod{p} $$
-   If $p \equiv \pm 1 \pmod{5}$, then $p \mid F_{p-1}$.
-   If $p \equiv \pm 2 \pmod{5}$, then $p \mid F_{p+1}$.
-   If $p = 5$, then $5 \mid F_5$.

This is a direct consequence of Binet’s formula interpreted in $\mathbb{F}_p$ or $\mathbb{F}_{p^2}$.

---

### 3. Algebraic Number Theory Connection
The Fibonacci numbers are intrinsically tied to the quadratic field $K = \mathbb{Q}(\sqrt{5})$.

#### Binet’s Formula as a Norm/Trace
$$ F_n = \frac{\varphi^n - \psi^n}{\varphi - \psi}, \quad \varphi = \frac{1+\sqrt{5}}{2}, \;\; \psi = \frac{1-\sqrt{5}}{2} $$
Here $\varphi$ and $\psi$ are conjugate units in the ring of integers $\mathcal{O}_K = \mathbb{Z}[\varphi]$. Note that $\varphi\psi = -1$, so they are **fundamental units**.

-   $F_n$ can be viewed as a "twisted trace" from $K$ to $\mathbb{Q}$.
-   Many identities (Cassini, Catalan, d’Ocagne) are simply norm equations or unit relations in $\mathcal{O}_K$.
-   **Example:** Cassini’s identity $F_{n-1}F_{n+1} - F_n^2 = (-1)^n$ is equivalent to $N(\varphi^n) = (-1)^n$ expressed in the integral basis.

---

### 4. Prime Fibonacci Numbers and Perfect Powers

#### Fibo-Primes
A Fibonacci prime is an $F_n$ that is prime. Known indices include:
$$ n = 3, 4, 5, 7, 11, 13, 17, 23, 29, 43, 47, 83, 131, 137, \dots $$
**Key constraint:** Except for $F_4 = 3$, if $F_n$ is prime then $n$ must be prime. (Contrapositive of the divisibility property.) However, $n$ prime does **not** imply $F_n$ prime (e.g., $F_{19} = 4181 = 37 \times 113$).

> **Open Problem:** Are there infinitely many Fibonacci primes? This is unknown and considered extremely difficult.

#### Perfect Powers in the Sequence
Which $F_n$ are perfect powers ($y^q$ with $q \geq 2$)?
-   **Squares:** Only $F_0 = 0$, $F_1 = 1$, $F_2 = 1$, $F_{12} = 144$. (Proved by Cohn, 1964; Wyler, 1964)
-   **Cubes:** Only $F_0, F_1, F_2, F_6 = 8$. (Proved by London & Finkelstein, 1969)
-   **General Perfect Powers:** Bugeaud, Mignotte, and Siksek (2006) proved using modular methods (Frey curves + modularity theorem) that the **only** perfect powers in the Fibonacci sequence are:
    $$ 0, 1, 8, 144 $$
This was a landmark application of the same machinery used to prove Fermat’s Last Theorem.

---

### 5. Zeckendorf Representation
Every positive integer has a **unique** representation as a sum of non-consecutive Fibonacci numbers:
$$ N = \sum_{i} \epsilon_i F_i, \quad \epsilon_i \in \{0,1\}, \quad \epsilon_i \epsilon_{i+1} = 0 $$
This provides a numeral system analogous to binary but based on Fibonacci growth. In number theory, this connects to:
-   **Greedy algorithms** and partition theory.
-   **Dynamical systems:** The shift space of non-consecutive 0-1 sequences is a subshift of finite type with topological entropy $\log \varphi$.
-   **Additive bases:** Questions about how many Fibonacci numbers are needed to represent elements of arithmetic progressions.

---

### Summary Table of Key Patterns

| Property | Statement | Significance |
| :--- | :--- | :--- |
| **GCD** | $\gcd(F_m,F_n)=F_{\gcd(m,n)}$ | Strong divisibility sequence |
| **Mod p** | $p \mid F_{p-(5/p)}$ | Link to quadratic reciprocity |
| **Period** | $\pi(m)$ exists for all $m$ | Finite automata / dynamical systems |
| **Units** | $\varphi^n \in \mathbb{Z}[\varphi]^\times$ | Real quadratic field arithmetic |
| **Powers** | Only 0, 1, 8, 144 | Modular method / Diophantine geometry |
| **Primes** | $F_n$ prime $\Rightarrow n$ prime (mostly) | Sparse distribution, open infinitude |

The Fibonacci sequence serves as a **testing ground** for deep number-theoretic conjectures. Because its algebraic structure is completely explicit (via $\mathbb{Q}(\sqrt{5})$), problems that are intractable for general sequences become attackable here, making it a bridge between elementary recurrence relations and modern arithmetic geometry.

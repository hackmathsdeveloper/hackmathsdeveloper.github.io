
# The Elliptic Curve $E: y^2 + y = x^3 - x$

This is one of the most celebrated elliptic curves in number theory. It is the curve of **smallest conductor with positive rank** over $\mathbb{Q}$, making it a fundamental object in arithmetic geometry. Below is an extensive exploration of its properties.

---

## 1. Basic Invariants

The curve is given in long Weierstrass form with coefficients:
$$a_1 = 0,\quad a_2 = 0,\quad a_3 = 1,\quad a_4 = -1,\quad a_6 = 0$$

From these we derive the standard quantities:

| Quantity | Value |
|----------|-------|
| $b_2 = a_1^2 + 4a_2$ | $0$ |
| $b_4 = 2a_4 + a_1a_3$ | $-2$ |
| $b_6 = a_3^2 + 4a_6$ | $1$ |
| $b_8 = a_2a_3^2 - a_4^2$ | $-1$ |
| $c_4 = b_2^2 - 24b_4$ | $48$ |
| $c_6 = -b_2^3 + 36b_2b_4 - 216b_6$ | $-216$ |
| **Discriminant** $\Delta$ | $\mathbf{37}$ |
| **$j$-invariant** $= c_4^3/\Delta$ | $\mathbf{110592/37} = 2^{12}\cdot 3^3 / 37$ |
| **Conductor** $N$ | $\mathbf{37}$ |

Since $\Delta = 37$ is prime (and $< 12$ for all prime valuations), this is a **global minimal model**.

Completing the square gives the short Weierstrass form via $Y = y + \tfrac{1}{2}$:
$$Y^2 = x^3 - x + \tfrac{1}{4}$$

---

## 2. A Beautiful Diophantine Equation

Factoring both sides reveals an elegant structure:

$$\boxed{y(y+1) = (x-1)\,x\,(x+1)}$$

> **When is the product of two consecutive integers equal to the product of three consecutive integers?**

This reframing makes the curve accessible even without algebraic geometry. The integer solutions are exactly the eight pairs listed in Section 5.

---

## 3. Mordell–Weil Group

The group of rational points is:
$$E(\mathbb{Q}) \cong \mathbb{Z}$$

- **Rank:** $1$
- **Torsion:** Trivial ($E(\mathbb{Q})_{\text{tors}} = \{\mathcal{O}\}$)
- **Generator:** $P = (0, 0)$

### Successive Multiples of $P$

Using the chord-and-tangent group law (with negation $-(x,y) = (x, -y-1)$):

| $n$ | $nP = (x_n, y_n)$ | Component |
|-----|---------------------|-----------|
| $1$ | $(0,\; 0)$ | Oval |
| $2$ | $(1,\; 0)$ | Unbounded |
| $3$ | $(-1,\; -1)$ | Oval |
| $4$ | $(2,\; -3)$ | Unbounded |
| $5$ | $\left(\frac{1}{4},\; -\frac{5}{8}\right)$ | Oval |
| $6$ | $(6,\; 14)$ | Unbounded |
| $7$ | $\left(-\frac{5}{9},\; \frac{8}{27}\right)$ | Oval |
| $8$ | $\left(\frac{21}{25},\; -\frac{69}{125}\right)$ | Unbounded |
| $9$ | $\left(-\frac{20}{49},\; -\frac{435}{343}\right)$ | Oval |
| $10$ | $\left(\frac{161}{16},\; -\frac{2065}{64}\right)$ | Unbounded |

Notice the alternating pattern: **odd multiples lie on the bounded oval, even multiples on the unbounded branch** (see Section 6).

---

## 4. Integer Points

By Siegel's theorem, there are only finitely many integer points. For this curve they are **completely classified**:

$$\boxed{(-1, 0),\; (-1, -1),\; (0, 0),\; (0, -1),\; (1, 0),\; (1, -1),\; (2, 2),\; (2, -3)}$$

These correspond to $\pm P,\; \pm 2P,\; \pm 3P,\; \pm 4P$. No integer point exists beyond $4P$—the denominators grow rapidly thereafter, as guaranteed by the theory of canonical heights.

In terms of our Diophantine reformulation:
- $0 \cdot 1 = (-1) \cdot 0 \cdot 1 = 0$
- $0 \cdot 1 = 0 \cdot 1 \cdot 2 = 0$
- $2 \cdot 3 = 1 \cdot 2 \cdot 3 = 6$

These are the **only** times this equality holds.

---

## 5. Real Locus and Topology

Setting $f(x) = x^3 - x + \frac{1}{4}$, the curve $Y^2 = f(x)$ has real points where $f(x) \geq 0$. The cubic has three real roots:

$$e_1 \approx -1.107, \quad e_2 \approx 0.270, \quad e_3 \approx 0.837$$

Since $f(x) \geq 0$ on $[e_1, e_2] \cup [e_3, \infty)$, the real locus $E(\mathbb{R})$ has **two connected components**:

1. **A bounded oval** for $x \in [e_1, e_2]$ — the non-identity component
2. **An unbounded branch** for $x \in [e_3, \infty)$ — the identity component (containing $\mathcal{O}$)

The group $E(\mathbb{R}) \cong S^1 \times \mathbb{Z}/2\mathbb{Z}$. Points on the oval are exactly those in the non-trivial coset of $E(\mathbb{R})/E(\mathbb{R})^0$, which is why odd multiples of $P$ alternate onto the oval.

---

## 6. Reduction at Primes

### Good reduction ($p \neq 37$)
For all primes $p \neq 37$, the curve has good reduction. The number of points $\#E(\mathbb{F}_p)$ and trace of Frobenius $a_p = p + 1 - \#E(\mathbb{F}_p)$:

| $p$ | $\#E(\mathbb{F}_p)$ | $a_p$ |
|-----|---------------------|-------|
| $2$ | $5$ | $-2$ |
| $3$ | $7$ | $-3$ |
| $5$ | $8$ | $-2$ |
| $7$ | $9$ | $-1$ |
| $11$ | $17$ | $-5$ |

### Bad reduction ($p = 37$)
The discriminant is $\Delta = 37$, so the curve has **multiplicative reduction** at $37$.

The singular point on the reduced curve is $(x, y) \equiv (5, 18) \pmod{37}$. Translating to the node, the tangent cone is $v^2 = 15u^2$. Since $15$ is **not** a quadratic residue mod $37$ ($15^{18} \equiv -1 \pmod{37}$), the tangent directions are not defined over $\mathbb{F}_{37}$.

> **The reduction at $37$ is non-split multiplicative**, so $a_{37} = -1$.

The **Tamagawa number** is $c_{37} = \gcd(2, v_{37}(\Delta)) = \gcd(2, 1) = 1$.

---

## 7. Modularity and the Associated Modular Form

By the Modularity Theorem (Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor), $E$ corresponds to a **weight-2 newform** $f \in S_2(\Gamma_0(37))$.

The space $S_2(\Gamma_0(37))$ has dimension $2$ (the genus of $X_0(37)$ is $2$). The newform attached to $E$ has the $q$-expansion:

$$f(q) = q - 2q^2 - 3q^3 + 2q^4 - 2q^5 + 6q^6 - q^7 + 0q^8 + 3q^9 + 4q^{10} - 5q^{11} + \cdots$$

The coefficients satisfy:
- **Multiplicativity:** $a_{mn} = a_m a_n$ when $\gcd(m,n) = 1$
- **Recurrence at good primes:** $a_{p^2} = a_p^2 - p$ (e.g., $a_4 = (-2)^2 - 2 = 2$, $a_9 = (-3)^2 - 3 = 6$)

This form can be expressed as an **eta quotient**. The modular parametrization $\phi: X_0(37) \to E$ maps the modular curve onto our elliptic curve.

---

## 8. The $L$-Function and BSD Conjecture

The $L$-function is:
$$L(E, s) = \prod_{p \neq 37} \left(1 - a_p p^{-s} + p^{1-2s}\right)^{-1} \cdot \left(1 + 37^{-s}\right)^{-1}$$

### Functional equation
$$\Lambda(E, s) = -\Lambda(E, 2-s)$$
The **root number** is $w = -1$, forcing $L(E, 1) = 0$ and predicting **odd analytic rank**.

### Analytic rank
The analytic rank is exactly **$1$**, matching the algebraic rank. This is a case where the full Birch and Swinnerton-Dyer conjecture can be tested:

$$\frac{L'(E, 1)}{\Omega} \stackrel{?}{=} \frac{R \cdot |\text{Ш}| \cdot \prod c_p}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

| Quantity | Value |
|----------|-------|
| Real period $\Omega$ | $\approx 5.9869$ |
| Regulator $R = \hat{h}(P)$ | $\approx 0.0511$ |
| $\lvert\text{Ш}\rvert$ | $1$ (verified) |
| Tamagawa product $\prod c_p$ | $1$ |
| $\lvert E(\mathbb{Q})_{\text{tors}}\rvert^2$ | $1$ |
| **Predicted $L'(E, 1)$** | $\approx 0.3059$ |

This has been verified numerically to high precision.

---

## 9. Gross–Zagier and Kolyvagin's Theorems

This curve is a **flagship example** for two landmark theorems:

- **Gross–Zagier (1986):** For an imaginary quadratic field $K = \mathbb{Q}(\sqrt{-D})$ where $37$ splits (e.g., $D = 7$, since $\left(\frac{-7}{37}\right) = +1$), the Heegner point $P_K \in E(K)$ has canonical height proportional to $L'(E/K, 1)$.

- **Kolyvagin (1988):** If the Heegner point is non-torsion (which it is here), then $\text{rank}(E(\mathbb{Q})) = 1$ and $\text{Ш}(E/\mathbb{Q})$ is **finite**. This was one of the first curves where the finiteness of Ш was rigorously established.

---

## 10. Galois Representations

Since $E$ has **no complex multiplication** ($\text{End}(E_{\bar{\mathbb{Q}}}) = \mathbb{Z}$), Serre's Open Image Theorem applies.

- The mod-$\ell$ representation $\bar{\rho}_{E,\ell}: \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to \text{GL}_2(\mathbb{F}_\ell)$ is **surjective for all primes $\ell$**.
- At $\ell = 2$: The $2$-torsion field is the splitting field of $x^3 - x + \frac{1}{4}$, which has discriminant $37/16$ and Galois group $S_3 \cong \text{GL}_2(\mathbb{F}_2)$, so the representation is surjective.
- There are **no exceptional primes** and **no rational isogenies** (the isogeny class contains only this curve).

---

## 11. Elliptic Divisibility Sequences

Writing $x(nP) = A_n / D_n^2$ in lowest terms, the denominators form an **elliptic divisibility sequence** (EDS):

$$D_n: \quad 1,\; 1,\; 1,\; 1,\; 2,\; 1,\; 3,\; 5,\; 7,\; 4,\; \ldots$$

This sequence satisfies the fundamental identity:
$$D_{m+n}\,D_{m-n} = D_{m+1}\,D_{m-1}\,D_n^2 - D_{n+1}\,D_{n-1}\,D_m^2$$

and the **strong divisibility property**:
$$\gcd(D_m, D_n) = D_{\gcd(m,n)}$$

For example, $\gcd(D_8, D_6) = \gcd(5, 1) = 1 = D_{\gcd(8,6)} = D_2$. These sequences, introduced by Ward (1948), have applications in cryptography and the study of prime appearance in recurrence sequences.

---

## 12. Historical and Computational Significance

| Distinction | Detail |
|-------------|--------|
| **Smallest conductor, rank $\geq 1$** | Conductor $37$ is the smallest among all rank-$1$ curves over $\mathbb{Q}$ |
| **First in databases** | Labeled **37a1** (Cremona) / **37.a.1** (LMFDB) — often the first entry in tables |
| **BSD test case** | One of the earliest curves where BSD was numerically verified |
| **Smallest canonical height** | $\hat{h}(P) \approx 0.0511$ is remarkably small, reflecting the curve's "tightness" |
| **No CM** | Endomorphism ring is $\mathbb{Z}$; Sato–Tate group is $\text{SU}(2)$ |
| **Faltings height** | $h_F(E) \approx -0.893$ |

---

## Summary

The curve $y^2 + y = x^3 - x$ is a nexus of deep arithmetic phenomena: a rank-$1$ Mordell–Weil group generated by the humble point $(0,0)$, a prime discriminant forcing non-split multiplicative reduction, a weight-$2$ modular form on $\Gamma_0(37)$, and a showcase for the Birch–Swinnerton-Dyer, Gross–Zagier, and Kolyvagin theorems. Its deceptively simple equation $y(y+1) = (x-1)x(x+1)$ hides a structure that has driven decades of research in number theory.

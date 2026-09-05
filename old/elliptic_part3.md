
# ELLIPTIC CURVES & ELLIPTIC FUNCTIONS

## Part 3 — Counting Points, Keeping Secrets: Elliptic Curves mod $p$

*Level: intermediate. The figure's formulas, now as pure modular arithmetic.*

*Series: [Part 1 — The Circle, the Ellipse, and the Birth of a New Trigonometry](elliptic_part1.md) · [Part 2 — How to Add Points on a Curve: The Chord‑and‑Tangent Method](elliptic_part2.md) · [Part 3 — Counting Points, Keeping Secrets: Elliptic Curves mod $p$](elliptic_part3.md) · [Part 4 — Rational Points and the Rank: The Mordell–Weil Theorem](elliptic_part4.md) · [Part 5 — The Torus, the $\wp$‑Function, and Modularity: The Grand Synthesis](elliptic_part5.md). One figure — the two‑panel derivation of the addition and doubling formulas — is reused throughout the series as a visual anchor.*

---

**1. Counting points and Hasse's bound.** For each prime $p$, reduce the coefficients of $E$ mod $p$ and count solutions. Write
$$a_p=p+1-\#E(\mathbb F_p).$$
**Hasse's theorem** says $|a_p|\le 2\sqrt p$ — the count is always close to $p+1$. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

Let us verify this on our toy curve $E:y^2=x^3+4x+4$ over $\mathbb F_5$. Checking each $x$: $x=0,1,4$ give $x^3+4x+4\equiv 4,4,4$ (a square, two points each); $x=2$ gives $0$ (one point); $x=3$ gives $3$ (a non‑square). Hence the affine points $(0,2),(0,3),(1,2),(1,3),(2,0),(4,2),(4,3)$ plus $\mathcal O$: $\#E(\mathbb F_5)=8$, so
$$a_5=5+1-8=-2,\qquad |a_5|=2\le 2\sqrt5\approx4.47 .$$
The sequence $(a_p)$, as $p$ varies, is far more than bookkeeping: it is the raw material from which the $L$‑function of $E$ is built ([Part 5](elliptic_part5.md)).

![The chord-and-tangent figure, run now as pure modular arithmetic](elliptic.jpeg)

> **Figure (series anchor).** The same two panels and the same boxed formulas as in [Part 2](elliptic_part2.md) — only now the arithmetic lives in $\mathbb F_p$ instead of $\mathbb R$. *Left panel (addition, $P\neq Q$):* the secant through $P$ and $Q$ meets the curve in a third point $R'$; reflection across the $x$‑axis gives $P+Q=R$. *Right panel (doubling, $P=Q$):* the tangent at $P$ meets the curve again in $R'$; reflection gives $2P=R$.

**2. The figure as modular arithmetic.** $E(\mathbb F_p)$ is a finite abelian group, and the figure's formulas compute in it. On our toy curve, $P=(1,3)$ has **order 4**: the right panel gives $2P=(2,0)$ (slope $m=\frac{3+4}{6}\equiv\frac{2}{1}=2$, $x_3=4-2=2$, $y_3=2(1-2)-3\equiv0$); the left panel then gives $3P=2P+P=(1,2)$; and doubling $(2,0)$ hits the vertical‑tangent case, $4P=\mathcal O$. The subgroup $\{\mathcal O,P,2P,3P\}$ has four elements. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

**3. Cryptography.** If instead of $p=5$ we take a huge prime and a point $P$ of large prime order $n$, the map $k\mapsto kP$ (repeated use of the figure's two formulas) is easy, while inverting it — given $P$ and $Q=kP$, find $k$, the **elliptic curve discrete logarithm problem** — is believed hard. This is elliptic curve cryptography (ECC). [people.cs.nycu.edu](https://people.cs.nycu.edu.tw/~rjchen/ECC2012S/Elliptic%20Curves%20Number%20Theory%20And%20Cryptography%202n.pdf) Number theory enters twice: one must ensure $\#E(\mathbb F_p)$ has a large prime factor (Hasse tells you what size to expect), and computing $\#E(\mathbb F_p)$ for large $p$ is done by the **Schoof–Elkies–Atkin** algorithm, whose machinery — modular polynomials, isogenies — links point counting to modular forms, previewing [Part 5](elliptic_part5.md). [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)

Our toy curve is hopelessly insecure; its purpose is to show the entire cryptographic edifice resting on two short formulas and one figure.

---

## The point count, spelled out

For each prime $p$, reduce the coefficients of $E$ modulo $p$ and count points $\#E(\mathbb F_p)$; the definition
$$a_p = p + 1 - \#E(\mathbb F_p)$$
measures the deviation of the count from $p+1$, and Hasse's theorem says
$$|a_p| \le 2\sqrt{p}.$$
Equivalently, $\#E(\mathbb F_p)\approx p$ — the group of points mod $p$ has roughly $p$ elements. [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)

The toy count above is worth doing once by hand. On $E:y^2=x^3+4x+4$ over $\mathbb F_5$, the squares mod 5 are $\{0,1,4\}$, and:

| $x$ | $x^3+4x+4 \pmod 5$ | points $(x,\pm y)$ |
|---|---|---|
| 0 | 4 | $(0,2),(0,3)$ |
| 1 | 4 | $(1,2),(1,3)$ |
| 2 | 0 | $(2,0)$ |
| 3 | 3 (non‑square) | none |
| 4 | 4 | $(4,2),(4,3)$ |

Seven affine points plus the point at infinity $\mathcal O$: $\#E(\mathbb F_5)=8$, so $a_5=5+1-8=-2$, comfortably inside $|a_p|\le 2\sqrt5\approx 4.47$. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

## Why counting points is not bookkeeping

The sequence $a_p$ for varying primes carries deep arithmetic information:

- The $a_p$ appear as coefficients of the **$L$‑function**
$$L(E,s)=\prod_p \left(1-a_p p^{-s} + p^{1-2s}\right)^{-1}.$$
- For modular elliptic curves over $\mathbb Q$, this $L$‑function is the $L$‑function of a **weight‑2 modular form**; this is the content of the modularity theorem (the chain of ideas leading to Fermat's Last Theorem). [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

So "counting points mod $p$" builds global analytic objects that encode the arithmetic of $E$ — the bridge to [Part 5](elliptic_part5.md).

## The cryptographic edifice, on two formulas

In ECC, one chooses a prime $p$ and an elliptic curve $E/\mathbb F_p$, then a point $P\in E(\mathbb F_p)$ of large prime order $n$. [people.cs.nycu.edu](https://people.cs.nycu.edu.tw/~rjchen/ECC2012S/Elliptic%20Curves%20Number%20Theory%20And%20Cryptography%202n.pdf)

- **Forward direction:** given $k$, computing $kP$ is fast — just $O(\log k)$ chord‑and‑tangent steps (double‑and‑add), i.e. repeated use of the two boxed formulas.
- **Inverse direction:** the **discrete logarithm problem** — given $P$ and $Q=kP$, find $k$ — is hard for suitably chosen curves and parameters. [people.cs.nycu.edu](https://people.cs.nycu.edu.tw/~rjchen/ECC2012S/Elliptic%20Curves%20Number%20Theory%20And%20Cryptography%202n.pdf)

Number theory enters in two places: ensuring $\#E(\mathbb F_p)$ has a large prime factor (so that $P$ lives in a large prime‑order subgroup), and computing $\#E(\mathbb F_p)$ efficiently via point‑counting algorithms (Schoof–Elkies–Atkin) built on modular polynomials and isogenies — machinery very close in spirit to the modular‑form side of the story. [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)

The toy curve $E:y^2=x^3+4x+4$ over $\mathbb F_5$ illustrates the mechanism — subgroup $\{\mathcal O,P,2P,3P\}$ of order 4 — and is, of course, trivially breakable. A real system replaces 5 by a 256‑bit prime, and the same two formulas do the work.

---

*Next:* [Part 4 — Rational Points and the Rank: The Mordell–Weil Theorem](elliptic_part4.md), which returns from finite fields to $\mathbb Q$ and asks how many rational points a curve really has.

*References for the curious reader: Wikipedia articles on elliptic curves and elliptic functions; E. Dummit's notes on elliptic curves (Northeastern); the LMFDB database; SageMath documentation on elliptic curves; introductory handouts on elliptic functions (HSE, Leiden, Harvard, UCSB).*

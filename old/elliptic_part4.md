
# ELLIPTIC CURVES & ELLIPTIC FUNCTIONS

## Part 4 — Rational Points and the Rank: The Mordell–Weil Theorem

*Level: intermediate–advanced. From finite groups back to infinite ones.*

*Series: [Part 1 — The Circle, the Ellipse, and the Birth of a New Trigonometry](elliptic_part1.md) · [Part 2 — How to Add Points on a Curve: The Chord‑and‑Tangent Method](elliptic_part2.md) · [Part 3 — Counting Points, Keeping Secrets: Elliptic Curves mod $p$](elliptic_part3.md) · [Part 4 — Rational Points and the Rank: The Mordell–Weil Theorem](elliptic_part4.md) · [Part 5 — The Torus, the $\wp$‑Function, and Modularity: The Grand Synthesis](elliptic_part5.md). One figure — the two‑panel derivation of the addition and doubling formulas — is reused throughout the series as a visual anchor.*

---

**1. Mordell's theorem.** Over $\mathbb Q$ the group $E(\mathbb Q)$ of rational points is finitely generated:
$$E(\mathbb Q)\cong E(\mathbb Q)_{\mathrm{tors}}\oplus\mathbb Z^{\,r},$$
where $r$ is the **rank**. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve) The torsion part we met in [Part 2](elliptic_part2.md) — the order‑2 points $(0,0),(\pm1,0)$ of $y^2=x^3-x$. The rank is the deeper invariant: $r>0$ means *infinitely many rational solutions* of the cubic. For instance on $y^2=x^3-x+1$ the point $P=(0,1)$ has infinite order (its double $2P=(\tfrac14,-\tfrac78)$ is non‑integral, impossible for torsion), and the multiples $nP$ generate infinitely many distinct rational solutions. Diophantinely, "find all solutions of this cubic" has been upgraded to "understand a finitely generated abelian group" — exactly how elliptic curves enter classical problems such as integer points on $y^2=x^3-2$ or the **congruent number problem**.

![Generating infinitely many rational points by repeated chord-and-tangent](elliptic.jpeg)

> **Figure (series anchor).** The two panels of the figure are the machine that generates $nP$ from $P$: doubling (right panel) followed by additions (left panel) walks through the group $E(\mathbb Q)$. If one of these multiples ever returns to $\mathcal O$, the point is torsion; if not — as for $P=(0,1)$ on $y^2=x^3-x+1$ — the multiples fill out an infinite cyclic subgroup, a copy of $\mathbb Z$ inside the Mordell–Weil group.

**2. Finding curves of a given rank.** The reliable route is a verified database. The LMFDB filters curves over $\mathbb Q$ by rank, conductor, torsion, and CM status; [lmfdb](https://www.lmfdb.org/EllipticCurve/Q/?torsion=[]&rank=1&search_type=List) useful small examples:

| Rank | Label | Weierstrass model |
|---|---|---|
| 0 | 11a1 | $y^2+y=x^3-x^2-10x-20$ |
| 1 | 37a1 | $y^2+y=x^3-x$ |
| 2 | 389a1 | $y^2+y=x^3+x^2-2x$ |

The LMFDB's rational‑curve search page supports ranks $0,1,2,\ldots$; it cautions that rank data are not known for every stored curve, so a filtered search excludes curves whose rank has not been computed. [lmfdb](https://www.lmfdb.org/EllipticCurve/Q/)

SageMath ships curated tables and full tooling:

```python
elliptic_curves.rank(rank=1, n=5)            # five rank-1 curves
elliptic_curves.rank(rank=3, tors=2, n=5, labels=True)
E = EllipticCurve("389a1")
E.rank()                 # rigorous Mordell–Weil rank when it succeeds
E.gens(proof=True)       # generators modulo torsion
E.torsion_subgroup()
E.analytic_rank()        # numerical L-function computation; not a proof
E.selmer_rank(2)         # upper-bound information
```

Sage's documented rank tables contain examples through rank 7, with rank‑3 curves in the default dataset and much larger conductors for the higher‑rank examples. [doc.sagemath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ec_database.html)

**3. What proving a rank entails.** To prove $r=k$ you need *both* directions: $k$ **independent** rational points ($r\ge k$), and a matching upper bound ($r\le k$) from a 2‑, 3‑, or higher **descent / Selmer computation**. Merely exhibiting many points proves nothing — they may be dependent, or generate a finite‑index subgroup. The analytic rank guides searches, but its equality with the algebraic rank is conjectural (Birch–Swinnerton‑Dyer); unconditional results need certified generators plus rigorous bounds. [doc.sagemath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html)

**4. Searching by hand — a caution.** One can enumerate short models $E_{A,B}:y^2=x^3+Ax+B$ in a coefficient box:

```python
for A in range(-100,101):
    for B in range(-100,101):
        if 4*A**3+27*B**2 == 0: continue
        E = EllipticCurve([0,0,0,A,B])
        try:
            if E.rank(proof=True) == 3: print(E.ainvs(), E.gens(proof=True))
        except RuntimeError: pass
```

Fine for ranks 1–3 (start from 37a1, 389a1, or Sage's rank‑3 tables); hopeless as a strategy for high rank, which grows increasingly sparse and demands engineered elliptic surfaces with independent sections.

The mystery left hanging: what do the counts $a_p$ of [Part 3](elliptic_part3.md) have to do with the rational points of this part? That bridge is the deepest result in the story.

---

## A practical workflow for finding curves of a given rank

For curves over $\mathbb Q$, the most reliable practical way is to search a verified database by Mordell–Weil rank, then independently certify or recompute the rank in SageMath/Magma if needed. Constructing examples from scratch becomes substantially harder as the target rank rises.

### The SageMath database step

```python
# SageMath

# Fetch up to five rank-r curves from Sage's built-in tables
elliptic_curves.rank(rank=1, n=5)
elliptic_curves.rank(rank=2, n=5)
elliptic_curves.rank(rank=3, n=5)

# Return their Cremona labels instead
elliptic_curves.rank(rank=3, n=5, labels=True)

# Add a torsion-order constraint, e.g. rank 3 and torsion order 2
elliptic_curves.rank(rank=3, tors=2, n=5, labels=True)
```

`E.rank()` combines database information and methods such as descent/Mordell–Weil computations; Sage distinguishes this from analytic‑rank routines, which may rely on numerical $L$‑function calculations. [doc.sagemath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html)

### What "rank $k$" really requires

One seeks $E(\mathbb Q)\cong E(\mathbb Q)_{\rm tors}\oplus\mathbb Z^r$. To prove $r=k$, you need both:

- $k$ independent rational points, giving $r\ge k$;
- a matching upper bound, commonly via a 2‑, 3‑, or higher descent / Selmer computation, giving $r\le k$.

Finding many visible rational points does **not** alone prove rank $k$: they might be dependent, and the subgroup you find may have finite index in a larger Mordell–Weil group. The analytic rank can guide searches, but equality with the algebraic rank is conjectural in general; for an unconditional result, use rigorous rank bounds plus certified generators.

### Choosing a strategy by target rank

- **Rank 1:** choose 37a1, or search LMFDB/Sage directly.
- **Rank 2:** start with 389a1; Sage generally handles many such examples quickly.
- **Rank 3:** retrieve examples through `elliptic_curves.rank(rank=3, ...)`, then verify with `rank(proof=True)` and `gens(proof=True)`.
- **Rank $\ge4$:** use published tables, LMFDB, or dedicated high‑rank constructions; do not expect naive coefficient enumeration to be efficient.

If your goal is a **parametric construction** of curves expected or proven to have a prescribed rank, that is a different problem: one typically constructs an elliptic surface with several independent sections, specializes the parameter, then proves independence and saturates the resulting subgroup.

---

*Next:* [Part 5 — The Torus, the $\wp$‑Function, and Modularity: The Grand Synthesis](elliptic_part5.md), where the counts $a_p$ and the rank finally meet on the torus.

*References for the curious reader: Wikipedia articles on elliptic curves and elliptic functions; E. Dummit's notes on elliptic curves (Northeastern); the LMFDB database; SageMath documentation on elliptic curves; introductory handouts on elliptic functions (HSE, Leiden, Harvard, UCSB).*

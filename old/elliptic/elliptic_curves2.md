
For curves over \(\mathbb Q\), the most reliable practical way is to search a verified database by Mordell–Weil rank, then independently certify or recompute the rank in SageMath/Magma if needed. Constructing examples from scratch becomes substantially harder as the target rank rises.

## Fastest: search a database

The LMFDB lets you filter elliptic curves over \(\mathbb Q\) by rank, conductor, torsion, CM status, and equation. Its rank-1 search, for example, includes

\[
37\mathrm{a}1:\quad y^2+y=x^3-x,
\]

with rank \(1\). [lmfdb](https://www.lmfdb.org/EllipticCurve/Q/?torsion=[]&rank=1&search_type=List)

Useful small examples over \(\mathbb Q\):

| Rank | Cremona/LMFDB label | Weierstrass model |
|---:|---|---|
| 0 | \(11\mathrm{a}1\) | \(y^2+y=x^3-x^2-10x-20\) |
| 1 | \(37\mathrm{a}1\) | \(y^2+y=x^3-x\) |
| 2 | \(389\mathrm{a}1\) | \(y^2+y=x^3+x^2-2x\) |

The LMFDB’s rational-curve search page supports ranks \(0,1,2,\ldots\); it also cautions that rank data are not known for every stored curve, so a filtered search excludes curves whose rank has not been computed. [lmfdb](https://www.lmfdb.org/EllipticCurve/Q/)

## SageMath workflow

Sage ships a curated table of elliptic curves at specified ranks, making this simplest for experimentation:

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

Sage’s documented rank tables contain examples through rank \(7\), with rank-3 curves in the default dataset and much larger conductors for the higher-rank examples. [doc.sagemath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ec_database.html)

For a particular curve:

```python
E = EllipticCurve("389a1")

E.rank()                 # rigorous Mordell–Weil rank when it succeeds
E.gens(proof=True)       # generators of E(Q) modulo torsion
E.torsion_subgroup()
E.analytic_rank()        # analytic/numerical computation; not by itself a proof
E.selmer_rank(2)         # useful upper-bound information
```

`E.rank()` combines database information and methods such as descent/Mordell–Weil computations; Sage distinguishes this from analytic-rank routines, which may rely on numerical \(L\)-function calculations. [doc.sagemath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html)

## If you want to search models yourself

For short integral models

\[
E_{A,B}: y^2=x^3+Ax+B,\qquad 4A^3+27B^2\ne0,
\]

you can enumerate \((A,B)\) in a coefficient box, discard non-minimal/isomorphic duplicates, then compute rank bounds and generators:

```python
for A in range(-100, 101):
    for B in range(-100, 101):
        if 4*A^3 + 27*B^2 == 0:
            continue

        E = EllipticCurve([0, 0, 0, A, B])

        try:
            r = E.rank(proof=True)
            if r == 3:
                print(E.ainvs(), E.conductor(), E.gens(proof=True))
        except RuntimeError:
            pass  # rank not provably resolved by the available methods
```

This is feasible as a **small-scale experiment**, but it is a poor strategy for deliberately finding high rank: rank \(r\) becomes increasingly sparse, and even rank certification can be computationally difficult. Use a database or an explicitly engineered family instead.

## What “rank” verification entails

One seeks

\[
E(\mathbb Q)\cong E(\mathbb Q)_{\rm tors}\oplus\mathbb Z^r.
\]

To prove \(r=k\), you need both:

- \(k\) independent rational points, giving \(r\ge k\);
- a matching upper bound, commonly via a \(2\)-, \(3\)-, or higher descent / Selmer computation, giving \(r\le k\).

Finding many visible rational points does **not** alone prove rank \(k\): they might be dependent, and the subgroup you find may have finite index in a larger Mordell–Weil group. The analytic rank can guide searches, but equality with algebraic rank is conjectural in general; for an unconditional result, use rigorous rank bounds plus certified generators.

## For target ranks 1–3

- **Rank 1:** choose \(37\mathrm{a}1\), or search LMFDB/Sage directly.
- **Rank 2:** start with \(389\mathrm{a}1\); Sage generally handles many such examples quickly.
- **Rank 3:** retrieve examples through `elliptic_curves.rank(rank=3, ...)`, then verify with `rank(proof=True)` and `gens(proof=True)`.
- **Rank \(\ge4\):** use published tables, LMFDB, or dedicated high-rank constructions; do not expect naive coefficient enumeration to be efficient.

If your goal is a **parametric construction** of curves expected or proven to have a prescribed rank, that is a different problem: one typically constructs an elliptic surface with several independent sections, specializes the parameter, then proves independence and saturates the resulting subgroup.

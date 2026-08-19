
A symmetric Hadamard matrix is a \(\{\pm1\}\)-matrix \(H\) with
\[
H=H^{\mathsf T},\qquad HH^{\mathsf T}=nI_n.
\]
For the usual, unrestricted symmetry condition, symmetric examples are known for **every admissible order through 240**: \(n=1,2\), and every multiple of \(4\) from \(4\) to \(240\).

## Orders

\[
\boxed{
1,\ 2,\ 4,\ 8,\ 12,\ 16,\ 20,\ 24,\ 28,\ 32,\ 36,\ 40,\ 44,\ 48,\ 52,\ 56,\ 60,\ 64,\ 68,\ 72,
}
\]
\[
\boxed{
76,\ 80,\ 84,\ 88,\ 92,\ 96,\ 100,\ 104,\ 108,\ 112,\ 116,\ 120,\ 124,\ 128,\ 132,\ 136,\ 140,
}
\]
\[
\boxed{
144,\ 148,\ 152,\ 156,\ 160,\ 164,\ 168,\ 172,\ 176,\ 180,\ 184,\ 188,\ 192,\ 196,\ 200,
}
\]
\[
\boxed{
204,\ 208,\ 212,\ 216,\ 220,\ 224,\ 228,\ 232,\ 236,\ 240.
}
\]

All other \(n\in[1,240]\) are impossible for any Hadamard matrix, apart from the exceptional admissible orders \(1,2\), since an Hadamard matrix of order \(n>2\) requires \(4\mid n\). [webspace.maths.qmul.ac](https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/library/encyc/topics/had.pdf)

## Useful construction families

Several broad construction mechanisms cover the range:

| Family | Symmetric order produced | Applicable parameters |
|---|---:|---|
| Sylvester | \(2^k\) | \(k\ge 0\); \(H_{2^k}\) is symmetric |
| Paley type II | \(2(q+1)\) | \(q\equiv1\pmod4\) a prime power |
| Doubling | \(2n\) | From a symmetric construction when symmetry-preserving formulation is used |
| Williamson / symmetric Goethals–Seidel variants | \(4m\) | From suitable symmetric, pairwise-compatible blocks |
| Propus and related SDS constructions | \(4m\) | Many odd \(m\), including difficult non-Paley cases |

In particular, Paley type II directly gives symmetric Hadamard matrices of order \(2(q+1)\) whenever \(q\equiv1\pmod4\) is a prime power.  The symmetric case is also treated separately in standard construction surveys, including computational constructions and “luchshie” matrices. [arxiv](https://arxiv.org/html/2411.18897v2)

## Caveat: stronger meanings

This list is for **symmetric** \(H\), with no constraint on its diagonal or row sums. Do not conflate it with either stricter class:

- **Regular symmetric Hadamard with constant diagonal / constant row sum:** much more restrictive. If a symmetric Hadamard matrix has constant row sum, its order must be \(4m^2\), hence a square. [webspace.maths.qmul.ac](https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/library/encyc/topics/had.pdf)
- **Circulant symmetric Hadamard:** substantially more restrictive again; no comparable all-orders statement applies.

For implementation, the ordinary `hadamard_matrix(n)` availability tables do not automatically certify symmetry; the cited SageMath construction database explicitly notes that a dedicated symmetric-Hadamard programme remained planned, distinct from its general and skew coverage. [arxiv](https://arxiv.org/html/2411.18897v2)

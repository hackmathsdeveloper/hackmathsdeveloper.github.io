
Any real quadratic form in \(n\) variables over \(\mathbb R\) can be diagonalised by a real invertible linear change of variables into a sum of squares with coefficients in \(\{1,-1,0\}\), and the numbers of positive, negative, and zero coefficients are invariants of the form; this is Sylvester’s law of inertia. [en.wikipedia](https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia)

## Precise statement

Let \(Q:\mathbb R^n \to \mathbb R\) be a real quadratic form, represented by a real symmetric matrix \(A\) so that \(Q(x) = x^{\mathsf T} A x\). [matrix.skku.ac](http://matrix.skku.ac.kr/2014-Album/Quadratic-form/3.Inertia%20of%20Quadratic%20form.htm)
Then there exists an invertible real matrix \(S\) such that, in new coordinates \(y = Sx\), we have
\[
Q(x) = Q(S^{-1}y) = \sum_{i=1}^n b_i y_i^2,
\]
where each \(b_i \in \{1,-1,0\}.\) [theoremoftheday](https://www.theoremoftheday.org/Algebra/Sylvester/TotDSylvester.pdf)

Let:
- \(p = \#\{i : b_i = 1\}\),
- \(q = \#\{i : b_i = -1\}\),
- \(r = \#\{i : b_i = 0\}\).

Sylvester’s law of inertia says that the triple \((p,q,r)\) is uniquely determined by \(Q\) and does not depend on which invertible change of variables \(S\) you use. [en.wikipedia](https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia)

Equivalently:
- \(p\) = number of positive eigenvalues of \(A\),
- \(q\) = number of negative eigenvalues,
- \(r\) = number of zero eigenvalues,  
counted with multiplicity; the triple \((p,q,r)\) is called the inertia of \(A\) or of \(Q\). [matrix.skku.ac](http://matrix.skku.ac.kr/2014-Album/Quadratic-form/3.Inertia%20of%20Quadratic%20form.htm)

## Rank, signature, and invariants

From the inertia \((p,q,r)\) you get two classic invariants: [academic.oup](https://academic.oup.com/book/55003/chapter-abstract/422790564?redirectedFrom=fulltext)

- Rank: \(\operatorname{rank}(Q) = p + q\).  
- Signature: \(\operatorname{sig}(Q) = p - q\).

Sylvester’s law can be restated as: for real quadratic forms, the rank and signature (equivalently the inertia triple) are invariant under real congruence \(A \mapsto S^{\mathsf T} A S\) with \(S\) invertible. [theoremoftheday](https://www.theoremoftheday.org/Algebra/Sylvester/TotDSylvester.pdf)

For a nondegenerate real quadratic form (i.e., \(r = 0\)), you can choose a basis such that \(Q\) is a sum of \(p\) positive and \(q\) negative squares, with no zero coefficients; in this case the inertia is just \((p,q,0).\) [leanprover-community.github](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Real.html)

## Example

Consider
\[
Q(x,y) = 4x^2 + 4xy + y^2.
\]
The associated matrix is
\[
A = \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}.
\]
This is symmetric and has eigenvalues \(0\) and \(5\), so its inertia is \((1,0,1)\): one positive eigenvalue, no negative eigenvalues, one zero eigenvalue. [matrix.skku.ac](http://matrix.skku.ac.kr/2014-Album/Quadratic-form/3.Inertia%20of%20Quadratic%20form.htm)
Sylvester’s law says that by a suitable invertible linear change of variables, you can rewrite \(Q\) as
\[
Q(x,y) = y_1^2 + 0\cdot y_2^2
\]
(and every other diagonalisation will have exactly one \(+1\), no \(-1\), and one \(0\)). [theoremoftheday](https://www.theoremoftheday.org/Algebra/Sylvester/TotDSylvester.pdf)

Would you like a coordinate-free formulation in terms of symmetric bilinear forms and the classification up to isometry of real inner product spaces with fixed signature?

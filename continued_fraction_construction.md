
There is no literal finite list of *all* ways to create continued fractions: a continued fraction can be engineered from almost any rational-approximation process, recurrence, power series, or functional identity. The most useful taxonomy is by the **input structure** you start with.

Write a generalized continued fraction as

\[
b_0+\cfrac{a_1}{b_1+\cfrac{a_2}{b_2+\cfrac{a_3}{b_3+\ddots}}}.
\]

Its \(n\)-th convergent is \(A_n/B_n\), where the numerator and denominator obey the same second-order recurrence:

\[
A_n=b_nA_{n-1}+a_nA_{n-2},\qquad
B_n=b_nB_{n-1}+a_nB_{n-2}.
\]

That recurrence correspondence is the common mechanism behind most constructions.

## Arithmetic constructions

- **Euclidean algorithm — rationals.** For \(x=p/q\), repeatedly divide:
  \[
  p=a_0q+r_1,\quad q=a_1r_1+r_2,\quad \dots
  \]
  The quotients give the finite regular continued fraction \(x=[a_0;a_1,\ldots,a_n]\). This is exact and terminates precisely because the remainders decrease.

- **Floor-and-reciprocal algorithm — arbitrary reals.** For irrational \(x\), set \(a_0=\lfloor x\rfloor\), then iterate
  \[
  x_{n+1}=\frac{1}{x_n-a_n},\qquad a_n=\lfloor x_n\rfloor.
  \]
  This constructs the simple continued fraction of \(x\). Example:
  \[
  \sqrt2=[1;2,2,2,\ldots].
  \]

- **Quadratic-surds algorithm.** If \(x=(P+\sqrt D)/Q\), update the integer triple describing the complete quotient rather than using floating point. This yields the classical result that quadratic irrationals have eventually periodic simple continued fractions—e.g. \(\sqrt{23}=[4;\overline{1,3,1,8}]\).

- **Alternative digit rules.** Replace the floor with nearest-integer, ceiling, odd/even, signed, or restricted-digit choices. These produce nearest-integer CFs, negative CFs, even CFs, Nakada \(\alpha\)-CFs, and related dynamical expansions. The goal is usually smaller partial quotients, symmetry, or a digit system adapted to a group/action.

- **Algebraic or function-field Euclidean algorithms.** Apply polynomial division in \(K[x]\), Laurent-series fields, or algebraic-function fields. This creates continued fractions for rational functions, formal power series, and algebraic functions; it is the direct analogue of the integer Euclidean algorithm.

- **Multidimensional algorithms.** For simultaneous approximation of \((x_1,\ldots,x_d)\), use Jacobi–Perron, Brun, Selmer, or related algorithms. Their output is generally a sequence of matrices or a branched/multidimensional continued fraction rather than one scalar digit stream.

## From recurrences and identities

This is the most general symbolic technique. If a target ratio satisfies a three-term relation, repeatedly substitute the ratio of successive terms.

Suppose
\[
u_{n-1}=b_nu_n+a_nu_{n+1}.
\]
Dividing by \(u_n\) and inverting gives
\[
\frac{u_n}{u_{n-1}}
=
\cfrac{1}{b_n+a_n\frac{u_{n+1}}{u_n}},
\]
and iteration produces a continued fraction. Hypergeometric contiguous relations are a canonical example: Gauss used them to obtain continued fractions for ratios of \({}_2F_1\) functions. [arxiv](https://arxiv.org/pdf/1904.03350.pdf)

Common sources of the recurrence are:

- **Second-order linear difference equations.** Ratios of a minimal/recessive solution and a dominant solution often become continued fractions. This covers Bessel, modified Bessel, Airy-type, Legendre, and many orthogonal-polynomial ratios.

- **Three-term recurrences for orthogonal polynomials.** If
  \[
  P_{n+1}(x)=(x-\alpha_n)P_n(x)-\beta_nP_{n-1}(x),
  \]
  the associated resolvent/Stieltjes transform has a Jacobi or \(J\)-fraction. The recurrence coefficients \(\alpha_n,\beta_n\) become the continued-fraction coefficients. [cirm-math](https://www.cirm-math.fr/RepOrga/2324/Slides/slides_ismail.pdf)

- **Hypergeometric and basic-hypergeometric contiguous relations.** Shift parameters \(a,b,c\) by integers, derive a three-term relation, then take a ratio. This creates Gauss fractions, confluent limits, and \(q\)-continued fractions. The supplied notes describe parameter shifts, specializations, rescaling, and tail manipulation as the main ways of generating Gauss-type variants. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/13148127/41217ef2-a7a6-4487-87f2-823bf7ba9687/gauss_continued_fraction.md?AWSAccessKeyId=ASIA2F3EMEYE32X6YG7I&Signature=34YPkEFh8RIjMIzb4FZtQqJvCgw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCGlofRJOStv7sIoan9OAlcOl4LHBejdhs2p7iu0WTeqgIgImBNAMhEg8x6juLMcC%2FKt050frWXuPQ%2Fl7DCT7e%2B4zIq%2FAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDLpGjtcUTAxoW%2BGSrCrQBKos7NLRykqm2VcjTjXvICXS0uDuokbv0s6CHEWjGYsqpfECzBZj6SYu%2F9oNcUBEot460CmwwqTAIrhmYRKQeCO%2FZvmeIuJlFDePaCtMGfVTTGR%2B8kUsmV5dgtykj3C1UYva3RMbTQDI0RHZVRYondErDM9EsCqbEDS3oBtfx5fTrAoeZbE%2Fw%2F8LIBDj00HEsi8CAZjfscsIc0TsxFZz76tRKciMcAWQruFSZE5y53BxwUuRGPUzJCsHbawcfYHWnA5YbcxQMbcsoC%2BTNPx%2BUkI%2B95w0SioVIdTPU12X6IJwLVCpdiECX1BYZI7SIRyU7pyg7LLm583M7WHSWiE4umRxRYzVGg9iH2cNsgM2gkrmuEZOZJ6oV8rNfyVHwO%2B2%2FUusHVGfqv79wFQUj9moKkdGnULWdbVk85vU5E%2BaEXm3n08GAnopZ7n8W7l4bHKx2PZH8NVYcPkpc0b3a5tNlwbjxII4u7OqRhty3YWzZgKPR09RQHpIgo%2FdEmDDZuZMlNyAThj8Nv5AcOB2mZKVVD8250tLeyFSJQZLyxMytGc2IxuQjavOJiNoh1%2BYXLFuGgwrs92tiF8FH55CZ4kG2ULZPxDwMvXIMjvekUn60qyR5782GNG%2Bw33PREF0neCb4C0zTYx1WaFMDcHdYHafn7AzOkj6EvcOUh4Q9VGyJjrXuM3VMkXTT5RkkMoYo%2BBf5VqREnjasbLGKHDb7R4RP1lS50vvMDix51YqpLlpRna2op113uggjuv8jsLhePzos1Iib75%2FqG3FTwydihvsWMUw3o%2Fm0wY6mAHwXdnDwDG6boFAjSuo%2BWKr3oHMMElGrWE0P5Xst7UxA0lFtpqasPazRRf%2FRAHcDdnX%2F11JXMg%2FdoLezra5%2FTXP2d%2Ff%2BOqSiI7%2FXw1aszy1L2jWbLjUGH%2BsGejGMoUteU%2B48231SlGLbp0BfzrtqUiaSPbMOeu3zLbejNf88cbM3fRy2yUsg4LCdpCtiPuikJ0VSbuQVzR2sA%3D%3D&Expires=1786353073)

- **Functional equations.** If a function admits an identity linking \(f(x)\) to \(f(Tx)\), repeatedly substitute the right-hand side. This yields continued fractions from self-similarity, Riccati equations, Möbius transformations, and certain \(q\)-difference equations.

- **Riccati reduction of a differential equation.** Convert a second-order ODE to a logarithmic derivative \(y'/y\), obtaining a Riccati equation. Expanding or discretizing its recurrence can generate a continued fraction for the logarithmic derivative or for a ratio of adjacent special functions.

## From series, moments, and rational approximation

- **Euler’s series-to-continued-fraction transformation.** Start with a convergent series or a ratio of two series, reorganize partial sums recursively, and obtain a continued fraction. This is especially effective for alternating or hypergeometric terms whose consecutive-term ratio is rational in \(n\).

- **Padé approximation.** Construct rational functions \(P_n(z)/Q_n(z)\) matching as many Taylor coefficients of \(f(z)\) as possible. When successive Padé approximants are linked by a second-order recurrence, their nesting yields a continued fraction. In practice, this produces \(C\)-fractions, \(J\)-fractions, and \(T\)-fractions.

- **Quotient–difference (\(qd\)) algorithms.** Given Taylor coefficients, run a recurrence on coefficient differences and quotients to extract continued-fraction coefficients. This is an algorithmic route from a power series to a \(J\)-fraction or related fraction, and is useful when an explicit symbolic derivation is unavailable.

- **Moment sequences and Stieltjes transforms.** Given moments
  \[
  \mu_n=\int t^n\,d\mu(t),
  \]
  form
  \[
  F(z)=\int \frac{d\mu(t)}{z-t}.
  \]
  Orthogonalizing \(1,t,t^2,\ldots\) produces recurrence coefficients and hence a \(J\)-fraction; for positive Stieltjes moment data one often gets an \(S\)-fraction. [cirm-math](https://www.cirm-math.fr/RepOrga/2324/Slides/slides_ismail.pdf)

- **Integral transforms.** Use integration by parts, contiguous integration identities, or recurrences in an integral parameter to derive a recurrence for related integrals. Their ratios then have continued fractions. This is a frequent route for incomplete gamma, error-function, beta-function, and Bessel-type expressions.

## Transforming an existing fraction

These techniques do not necessarily discover a new value, but they create a more useful representation.

- **Equivalence transformations.** Choose nonzero factors \(c_n\) and rescale coefficients so the convergents remain unchanged. This normalizes coefficients, avoids overflow/underflow, or exposes symmetry.

- **Contraction.** Eliminate every other level of a fraction. An \(S\)-fraction can contract to a \(J\)-fraction; even/odd contractions often reveal a recurrence or a moment interpretation.

- **Extension.** Insert levels into a fraction, the inverse of contraction. This can turn a compact fraction into one with simpler coefficients.

- **Canonical contraction of a regular CF.** Group partial quotients to obtain variants such as negative or nearest-integer expansions, often preserving selected convergents.

- **Tail replacement.** Truncate at depth \(N\) and replace the infinite remainder by an exact, asymptotic, or fixed-point approximation. This is a numerical construction, not generally a new identity. The Gauss-fraction notes specifically identify truncation with tail corrections and shifted starting indices as practical variants. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/13148127/41217ef2-a7a6-4487-87f2-823bf7ba9687/gauss_continued_fraction.md?AWSAccessKeyId=ASIA2F3EMEYE32X6YG7I&Signature=34YPkEFh8RIjMIzb4FZtQqJvCgw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCGlofRJOStv7sIoan9OAlcOl4LHBejdhs2p7iu0WTeqgIgImBNAMhEg8x6juLMcC%2FKt050frWXuPQ%2Fl7DCT7e%2B4zIq%2FAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDLpGjtcUTAxoW%2BGSrCrQBKos7NLRykqm2VcjTjXvICXS0uDuokbv0s6CHEWjGYsqpfECzBZj6SYu%2F9oNcUBEot460CmwwqTAIrhmYRKQeCO%2FZvmeIuJlFDePaCtMGfVTTGR%2B8kUsmV5dgtykj3C1UYva3RMbTQDI0RHZVRYondErDM9EsCqbEDS3oBtfx5fTrAoeZbE%2Fw%2F8LIBDj00HEsi8CAZjfscsIc0TsxFZz76tRKciMcAWQruFSZE5y53BxwUuRGPUzJCsHbawcfYHWnA5YbcxQMbcsoC%2BTNPx%2BUkI%2B95w0SioVIdTPU12X6IJwLVCpdiECX1BYZI7SIRyU7pyg7LLm583M7WHSWiE4umRxRYzVGg9iH2cNsgM2gkrmuEZOZJ6oV8rNfyVHwO%2B2%2FUusHVGfqv79wFQUj9moKkdGnULWdbVk85vU5E%2BaEXm3n08GAnopZ7n8W7l4bHKx2PZH8NVYcPkpc0b3a5tNlwbjxII4u7OqRhty3YWzZgKPR09RQHpIgo%2FdEmDDZuZMlNyAThj8Nv5AcOB2mZKVVD8250tLeyFSJQZLyxMytGc2IxuQjavOJiNoh1%2BYXLFuGgwrs92tiF8FH55CZ4kG2ULZPxDwMvXIMjvekUn60qyR5782GNG%2Bw33PREF0neCb4C0zTYx1WaFMDcHdYHafn7AzOkj6EvcOUh4Q9VGyJjrXuM3VMkXTT5RkkMoYo%2BBf5VqREnjasbLGKHDb7R4RP1lS50vvMDix51YqpLlpRna2op113uggjuv8jsLhePzos1Iib75%2FqG3FTwydihvsWMUw3o%2Fm0wY6mAHwXdnDwDG6boFAjSuo%2BWKr3oHMMElGrWE0P5Xst7UxA0lFtpqasPazRRf%2FRAHcDdnX%2F11JXMg%2FdoLezra5%2FTXP2d%2Ff%2BOqSiI7%2FXw1aszy1L2jWbLjUGH%2BsGejGMoUteU%2B48231SlGLbp0BfzrtqUiaSPbMOeu3zLbejNf88cbM3fRy2yUsg4LCdpCtiPuikJ0VSbuQVzR2sA%3D%3D&Expires=1786353073)

- **Convergence acceleration.** Apply Bauer–Muir transforms, even/odd parts, modified Lentz scaling, or asymptotic tail models. Such transformations can preserve the limit while substantially changing convergence behavior.

## Choosing the method

| Starting information | Best construction route |
|---|---|
| A rational number | Euclidean algorithm |
| A real irrational | Floor/reciprocal or a modified digit algorithm |
| A quadratic irrational | Exact surd recurrence |
| A special-function ratio | Three-term recurrence or contiguous relations |
| A Taylor series | Padé, \(qd\), Euler transformation, or \(C\)-fraction extraction |
| A positive moment sequence or measure | Orthogonal polynomials and \(J/S\)-fractions |
| An integral with a parameter | Integration-by-parts recurrence, then ratio CF |
| A known CF with poor numerical behavior | Equivalence transform, contraction, or tail correction |
| Simultaneous approximation of several numbers | A multidimensional continued-fraction algorithm |

A practical rule: **derive a recurrence when you can; extract a Padé/continued fraction from coefficients when you cannot; use Euclidean-type algorithms when the input is a number or algebraic object.** The key mathematical work is then proving that the chosen tail is the intended solution and that the resulting fraction converges in the parameter region of interest.

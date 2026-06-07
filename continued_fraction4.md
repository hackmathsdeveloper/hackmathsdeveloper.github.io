
Continued fractions of **complex** polynomials usually means one of two nearby topics: polynomial continued fractions, where the partial numerators and denominators are polynomials in an index \(n\), and continued fractions for complex numbers, where partial quotients lie in the Gaussian integers. The literature shows both frameworks allow complex coefficients, and polynomial continued fractions can be analyzed with recurrence methods such as Pincherle’s theorem. [arxiv](https://arxiv.org/abs/1812.08251)

## Two meanings

A polynomial continued fraction has the form \(K_{n=1}^{\infty} a_n/b_n\) where \(a_n\) and \(b_n\) are polynomials in \(n\); the paper *Polynomial Continued Fractions* explicitly allows the relevant auxiliary sequences to take real or complex values.  In that setting, one studies convergence and exact values by linking the continued fraction to a three-term recurrence \(G_n=a_nG_{n-2}+b_nG_{n-1}\), and if \(G_n/B_n \to 0\) then the continued fraction converges to \(-G_0/G_{-1}\). [arxiv](https://arxiv.org/abs/1812.08251)

A different topic is continued fractions for complex numbers themselves, developed using Gaussian integers \(x+iy\). In that theory, a sequence of Gaussian integers \(\{a_n\}\) defines convergents \(p_n/q_n\) by the usual recurrences, and many complex numbers admit such expansions, often non-uniquely. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

## Polynomial case

The polynomial continued fraction paper focuses on higher-degree cases for \(a_n\) and \(b_n\), especially when their degrees are equal, and gives both rational and irrational limits.  It includes examples such as \(K_{n=1}^{\infty}(n^\alpha+1)/n^\alpha = 1\) for \(\alpha>0\), along with families whose limits involve Bessel functions, trigonometric functions, or explicit rational constants. [arxiv](https://arxiv.org/abs/1812.08251)

The same source states many results remain valid when the sequences are more general than real-valued, because Pincherle’s theorem is stated there for real or complex sequences.  So if by “complex polynomials” you mean polynomials with coefficients in \(\mathbb{C}\), the core machinery still applies as long as the recurrence and convergence conditions are met. [arxiv](https://arxiv.org/abs/1812.08251)

## Complex-number case

For genuine continued fractions in \(\mathbb{C}\), Dani and Nogueira study expansions with Gaussian-integer partial quotients and prove convergence of convergents under broad conditions.  They also prove a complex analogue of Lagrange’s theorem: for a large class of algorithms, a complex number has an eventually periodic expansion if and only if it is a quadratic surd over the Gaussian integers. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

That framework is not about “polynomials in \(n\)” directly, but it is the natural notion of a continued fraction for a complex value.  So the phrase “continued fractions of complex polynomials” can mean either “continued fractions built from polynomial sequences with complex coefficients” or “continued fraction expansions of complex algebraic functions or values.” [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

## What is known

A recent source also points to an active line of work called “continued fractions of polynomial type,” including a database project, which suggests the subject is still being systematized and cataloged.  The older polynomial literature had mainly covered low-degree cases, while the Bowman–McLaughlin paper extended this to higher-degree numerator and denominator polynomials and especially equal-degree cases. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

As a concrete illustration, one can start from a recurrence solution \(G_n\) and then engineer infinitely many polynomial continued fractions with prescribed limits using the proposition in the paper.  That is one of the main constructive ideas behind modern work in this area. [arxiv](https://arxiv.org/abs/1812.08251)

## Example

One simple family is  
\[
\mathop{K}\limits_{n=1}^{\infty}\frac{n^\alpha+1}{n^\alpha}=1
\]
for \(\alpha>0\).  This is a polynomial continued fraction with equal degrees in numerator and denominator, and it shows that equal-degree cases do not force irrational limits. [arxiv](https://arxiv.org/abs/1812.08251)



Hypergeometric functions are motivated by a single structural observation: many useful power series have coefficients whose successive ratio is rational in \(n\). The family

\[
{}_pF_q\!\left(
\begin{matrix}a_1,\dots,a_p\\ b_1,\dots,b_q\end{matrix};z
\right)
=
\sum_{n=0}^{\infty}
\frac{(a_1)_n\cdots(a_p)_n}
{(b_1)_n\cdots(b_q)_n}\frac{z^n}{n!}
\]

is the natural closure of that pattern. Here \((a)_n=\Gamma(a+n)/\Gamma(a)\). [math.libretexts](https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_(Herman)/04:_Series_Solutions/4.08:_Hypergeometric_Functions)

## 1–3: Elementary series

| # | Starting problem | Hypergeometric form | Motivation |
|---|---|---|---|
| 1 | Sum a geometric progression | \(\displaystyle \frac{1}{1-z}={}_1F_0(1;;z)\) | The coefficient ratio is \(a_{n+1}/a_n=1\). Hypergeometric series begin by generalizing “constant-ratio” series. |
| 2 | Generalize the binomial theorem | \(\displaystyle (1-z)^{-a}={}_1F_0(a;;z)\) | The coefficient ratio becomes \(\frac{a+n}{n+1}\), already a rational function of \(n\). This is the literal origin of the term “hypergeometric.” |
| 3 | Integrate a rational function | \(\displaystyle \log(1+z)=z\,{}_2F_1(1,1;2;-z)\) | Termwise integration of the geometric series introduces \(1/(n+1)\); the resulting coefficients still have rational successive ratio. |
| 4 | Invert a trigonometric integral | \(\displaystyle \arcsin z=z\,{}_2F_1\!\left(\tfrac12,\tfrac12;\tfrac32;z^2\right)\) | The binomial expansion of \((1-z^2)^{-1/2}\), followed by integration, produces the characteristic Pochhammer products. |

The geometric, binomial, logarithmic, and inverse-sine cases show that hypergeometric notation is not an exotic replacement for elementary functions; it is a parameterized language containing them. [math.libretexts](https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_(Herman)/04:_Series_Solutions/4.08:_Hypergeometric_Functions)

## 5–6: Polynomial and ODE structure

| # | Starting problem | Hypergeometric form | Motivation |
|---|---|---|---|
| 5 | Solve Legendre’s equation | \(\displaystyle P_n(x)={}_2F_1\!\left(-n,n+1;1;\frac{1-x}{2}\right)\) | A terminating numerator parameter \((-n)_k\) turns the infinite series into a degree-\(n\) polynomial. Thus orthogonal polynomial families emerge from the same coefficient rule. |
| 6 | Solve a broad class of second-order ODEs | \(\displaystyle z(1-z)y''+[c-(a+b+1)z]y'-aby=0\) | Frobenius expansion at \(z=0\) gives \(a_{n+1}/a_n=\frac{(n+a)(n+b)}{(n+c)(n+1)}\), hence \(y={}_2F_1(a,b;c;z)\). This is the central reason the Gauss function occurs so broadly. |

The Gauss equation has regular singular points at \(0\), \(1\), and \(\infty\); much of classical special-function theory is reducible to it after changes of variables and gauge factors. [math.libretexts](https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_(Herman)/04:_Series_Solutions/4.08:_Hypergeometric_Functions)

## 7–8: Physics and geometry

| # | Starting problem | Hypergeometric form | Motivation |
|---|---|---|---|
| 7 | Describe oscillation and radial-wave problems | \(\displaystyle J_\nu(z)=\frac{(z/2)^\nu e^{-iz}}{\Gamma(\nu+1)}\,{}_1F_1\!\left(\nu+\tfrac12;2\nu+1;2iz\right)\) | Confluence—merging two regular singularities of the Gauss equation—produces Kummer’s equation and \({}_1F_1\). Bessel-type functions arise in this confluent class. |
| 8 | Compute an elliptic integral / period | \(\displaystyle K(m)=\frac{\pi}{2}\,{}_2F_1\!\left(\tfrac12,\tfrac12;1;m\right)\) | The integral \(\int_0^1[(1-x^2)(1-mx^2)]^{-1/2}dx\) is a period of an elliptic curve. This makes \({}_2F_1\) a bridge from integration to algebraic geometry, modular phenomena, and monodromy. |

The confluent limit is explicitly \({}_1F_1(a;c;u)=\lim_{b\to\infty}{}_2F_1(a,b;c;u/b)\), explaining why many familiar wave and diffusion functions sit near the Gauss family.  The elliptic-integral example is a period of \(y^2=(1-x^2)(1-mx^2)\), a key geometric motivation. [math.libretexts](https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_(Herman)/04:_Series_Solutions/4.08:_Hypergeometric_Functions)

## 9–10: Generalized systems

| # | Starting problem | Hypergeometric form | Motivation |
|---|---|---|---|
| 9 | Invert an algebraic equation such as \(z x^5-x+1=0\) | A solution is expressible through a generalized \({}_4F_3\) after rescaling \(z\) | Lagrange inversion yields coefficients built from factorial ratios such as \(\binom{5n}{n}/(4n+1)\). Factorial ratios decompose into Pochhammer symbols, so generalized hypergeometric series arise naturally. |
| 10 | Model coupled two-variable integrals or PDEs | \(\displaystyle F_1(a;b_1,b_2;c;x,y)=\sum_{m,n\ge0}\frac{(a)_{m+n}(b_1)_m(b_2)_n}{(c)_{m+n}m!n!}x^my^n\) | When coefficient ratios in each discrete direction are rational in \((m,n)\), one reaches Appell/Horn functions. \(F_1\) evaluates integrals involving two independent binomial factors and satisfies a coupled PDE system. |

For the quintic example, Lagrange inversion converts the Bring–Jerrard equation into a generalized hypergeometric series; it illustrates that the family is not limited to differential equations—it also appears in algebraic inversion problems.  Appell \(F_1\) is the two-variable extension of \({}_2F_1\), and it applies directly to integrals of the form \(\int x^r(x+a)^p(x+b)^q\,dx\). [mpmath](https://mpmath.org/doc/current/functions/hypergeometric.html)

## The unifying viewpoint

A series \(\sum c_nz^n\) is hypergeometric when

\[
\frac{c_{n+1}}{c_n}
=
\frac{\prod_i(n+a_i)}
{(n+1)\prod_j(n+b_j)},
\]

a rational function of \(n\). This one recurrence explains the repeated appearance of factorials, binomial coefficients, terminating polynomial series, regular-singular ODEs, integral transforms, algebraic inversion, and multivariable PDE systems. The generalized \({}_pF_q\) class also cleanly signals analytic behavior: except for terminating cases, it has infinite radius of convergence for \(p\le q\), radius \(1\) for \(p=q+1\), and is generally divergent/asymptotic for \(p>q+1\). [mpmath](https://mpmath.org/doc/current/functions/hypergeometric.html)

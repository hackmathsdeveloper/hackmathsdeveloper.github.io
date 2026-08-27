
Here is a practical “100 infinite series to know” list: geometric, Taylor/Maclaurin, Fourier, zeta-type, generating functions, and special functions. It is ordered roughly from core calculus to analysis, probability, physics, and number theory.

Throughout, \((a)_n=a(a+1)\cdots(a+n-1)\) denotes the rising factorial, and \(|x|<1\) where a power-series radius is not otherwise stated. Classical special-function series—including the error function, zeta function, incomplete gamma function, and hypergeometric families—are catalogued by the NIST Digital Library of Mathematical Functions.  [dlmf.nist](https://dlmf.nist.gov/8.7)

## Elementary and geometric

1. **Geometric series**
   \[
   \sum_{n=0}^{\infty}x^n=\frac{1}{1-x}
   \]

2. **Shifted geometric series**
   \[
   \sum_{n=0}^{\infty}x^{n+k}=\frac{x^k}{1-x}
   \]

3. **Alternating geometric series**
   \[
   \sum_{n=0}^{\infty}(-1)^n x^n=\frac{1}{1+x}
   \]

4. **Arithmetic–geometric series**
   \[
   \sum_{n=1}^{\infty}nx^n=\frac{x}{(1-x)^2}
   \]

5. **Quadratic-weighted geometric series**
   \[
   \sum_{n=1}^{\infty}n^2x^n=\frac{x(1+x)}{(1-x)^3}
   \]

6. **Cubic-weighted geometric series**
   \[
   \sum_{n=1}^{\infty}n^3x^n=\frac{x(1+4x+x^2)}{(1-x)^4}
   \]

7. **Binomial-coefficient generator**
   \[
   \sum_{n=0}^{\infty}\binom{n+r}{r}x^n=\frac{1}{(1-x)^{r+1}}
   \]

8. **General binomial series**
   \[
   (1+x)^\alpha=\sum_{n=0}^{\infty}\binom{\alpha}{n}x^n
   \]

9. **Negative binomial series**
   \[
   (1-x)^{-\alpha}=\sum_{n=0}^{\infty}\frac{(\alpha)_n}{n!}x^n
   \]

10. **Logarithm**
   \[
   -\ln(1-x)=\sum_{n=1}^{\infty}\frac{x^n}{n}
   \]

11. **Alternating logarithm**
   \[
   \ln(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n}
   \]

12. **Dilogarithm**
   \[
   \operatorname{Li}_2(x)=\sum_{n=1}^{\infty}\frac{x^n}{n^2}
   \]

13. **Polylogarithm**
   \[
   \operatorname{Li}_s(x)=\sum_{n=1}^{\infty}\frac{x^n}{n^s}
   \]

14. **Harmonic-number generator**
   \[
   \sum_{n=1}^{\infty}H_nx^n=\frac{-\ln(1-x)}{1-x}
   \]

15. **Second-order harmonic generator**
   \[
   \sum_{n=1}^{\infty}H_n^{(2)}x^n=\frac{\operatorname{Li}_2(x)}{1-x}
   \]

16. **Central binomial generator**
   \[
   \sum_{n=0}^{\infty}\binom{2n}{n}x^n=\frac{1}{\sqrt{1-4x}}
   \]

17. **Catalan-number generator**
   \[
   \sum_{n=0}^{\infty}C_nx^n
   =\frac{1-\sqrt{1-4x}}{2x}
   \]

18. **Fibonacci generating function**
   \[
   \sum_{n=0}^{\infty}F_nx^n=\frac{x}{1-x-x^2}
   \]

19. **Lucas generating function**
   \[
   \sum_{n=0}^{\infty}L_nx^n=\frac{2-x}{1-x-x^2}
   \]

20. **Exponential generating function for Bell numbers**
   \[
   \sum_{n=0}^{\infty}B_n\frac{x^n}{n!}
   =\exp(e^x-1)
   \]

## Maclaurin series

21. **Exponential**
   \[
   e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}
   \]

22. **Sine**
   \[
   \sin x=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{(2n+1)!}
   \]

23. **Cosine**
   \[
   \cos x=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}
   \]

24. **Hyperbolic sine**
   \[
   \sinh x=\sum_{n=0}^{\infty}\frac{x^{2n+1}}{(2n+1)!}
   \]

25. **Hyperbolic cosine**
   \[
   \cosh x=\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}
   \]

26. **Arctangent**
   \[
   \arctan x=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{2n+1}
   \]

27. **Inverse hyperbolic tangent**
   \[
   \operatorname{artanh}x=\sum_{n=0}^{\infty}\frac{x^{2n+1}}{2n+1}
   \]

28. **Arcsine**
   \[
   \arcsin x=\sum_{n=0}^{\infty}
   \frac{\binom{2n}{n}}{4^n(2n+1)}x^{2n+1}
   \]

29. **Square root**
   \[
   \sqrt{1+x}
   =\sum_{n=0}^{\infty}\binom{1/2}{n}x^n
   \]

30. **Inverse square root**
   \[
   \frac{1}{\sqrt{1-x}}
   =\sum_{n=0}^{\infty}\frac{\binom{2n}{n}}{4^n}x^n
   \]

31. **Tangent**
   \[
   \tan x=\sum_{n=1}^{\infty}
   (-1)^{n-1}\frac{2^{2n}(2^{2n}-1)B_{2n}}{(2n)!}x^{2n-1}
   \]

32. **Secant**
   \[
   \sec x=\sum_{n=0}^{\infty}(-1)^nE_{2n}\frac{x^{2n}}{(2n)!}
   \]

33. **Logarithmic quotient**
   \[
   \frac{\ln(1+x)}{x}
   =\sum_{n=0}^{\infty}\frac{(-1)^n x^n}{n+1}
   \]

34. **Exponential remainder**
   \[
   \frac{e^x-1}{x}
   =\sum_{n=0}^{\infty}\frac{x^n}{(n+1)!}
   \]

35. **Sinc**
   \[
   \frac{\sin x}{x}
   =\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n+1)!}
   \]

36. **Cosine remainder**
   \[
   \frac{1-\cos x}{x^2}
   =\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n+2)!}
   \]

37. **Bernoulli generating function**
   \[
   \frac{x}{e^x-1}
   =\sum_{n=0}^{\infty}B_n\frac{x^n}{n!}
   \]

38. **Euler-polynomial generator**
   \[
   \frac{2e^{xt}}{e^t+1}
   =\sum_{n=0}^{\infty}E_n(x)\frac{t^n}{n!}
   \]

39. **Stirling-number generator**
   \[
   \frac{(e^x-1)^k}{k!}
   =\sum_{n=k}^{\infty}S(n,k)\frac{x^n}{n!}
   \]

40. **Lambert \(W\)**
   \[
   W(x)=\sum_{n=1}^{\infty}
   \frac{(-n)^{n-1}}{n!}x^n
   \]

## Fourier series

41. **Square wave**
   \[
   \operatorname{sgn}(\sin x)
   =\frac{4}{\pi}\sum_{n=0}^{\infty}
   \frac{\sin((2n+1)x)}{2n+1}
   \]

42. **Sawtooth wave**
   \[
   x=2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx),
   \qquad -\pi<x<\pi
   \]

43. **Even sawtooth / absolute value**
   \[
   |x|=\frac{\pi}{2}
   -\frac{4}{\pi}\sum_{n=1}^{\infty}
   \frac{\cos((2n-1)x)}{(2n-1)^2}
   \]

44. **Quadratic**
   \[
   x^2=\frac{\pi^2}{3}
   +4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos(nx)
   \]

45. **Cubic**
   \[
   x^3=\sum_{n=1}^{\infty}
   (-1)^n\left(\frac{6}{n^3}-\frac{\pi^2}{n}\right)\sin(nx)
   \]

46. **Log sine**
   \[
   -\ln\!\left(2\sin\frac{x}{2}\right)
   =\sum_{n=1}^{\infty}\frac{\cos(nx)}{n}
   \]

47. **Log cosine**
   \[
   \ln\!\left(2\cos\frac{x}{2}\right)
   =\sum_{n=1}^{\infty}\frac{(-1)^{n-1}\cos(nx)}{n}
   \]

48. **Poisson kernel**
   \[
   \frac{1-r^2}{1-2r\cos x+r^2}
   =1+2\sum_{n=1}^{\infty}r^n\cos(nx)
   \]

49. **Conjugate Poisson kernel**
   \[
   \frac{2r\sin x}{1-2r\cos x+r^2}
   =2\sum_{n=1}^{\infty}r^n\sin(nx)
   \]

50. **Jacobi–Anger expansion**
   \[
   e^{iz\cos\theta}
   =\sum_{n=-\infty}^{\infty}i^nJ_n(z)e^{in\theta}
   \]

51. **Plane-wave expansion**
   \[
   e^{z\cos\theta}
   =I_0(z)+2\sum_{n=1}^{\infty}I_n(z)\cos(n\theta)
   \]

52. **Heat kernel on a circle**
   \[
   \frac{1}{2\pi}
   +\frac{1}{\pi}\sum_{n=1}^{\infty}e^{-n^2t}\cos(nx)
   \]

53. **Periodic delta distribution**
   \[
   \delta_{2\pi}(x)
   =\frac{1}{2\pi}\sum_{n=-\infty}^{\infty}e^{inx}
   \]

54. **Dirichlet kernel**
   \[
   D_N(x)=1+2\sum_{n=1}^{N}\cos(nx)
   =\frac{\sin((N+\frac12)x)}{\sin(x/2)}
   \]

55. **Fejér kernel**
   \[
   F_N(x)=\sum_{n=-N}^{N}
   \left(1-\frac{|n|}{N+1}\right)e^{inx}
   \]

## Number theory and constants

56. **Harmonic series**
   \[
   \sum_{n=1}^{\infty}\frac1n
   \]

57. **Alternating harmonic series**
   \[
   \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}n=\ln2
   \]

58. **\(p\)-series / zeta series**
   \[
   \zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s},
   \qquad \Re(s)>1
   \]

59. **Basel series**
   \[
   \sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{6}
   \]

60. **Euler’s \(\zeta(4)\) sum**
   \[
   \sum_{n=1}^{\infty}\frac1{n^4}=\frac{\pi^4}{90}
   \]

61. **Odd reciprocal squares**
   \[
   \sum_{n=0}^{\infty}\frac1{(2n+1)^2}=\frac{\pi^2}{8}
   \]

62. **Odd reciprocal fourth powers**
   \[
   \sum_{n=0}^{\infty}\frac1{(2n+1)^4}=\frac{\pi^4}{96}
   \]

63. **Dirichlet eta function**
   \[
   \eta(s)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^s}
   =(1-2^{1-s})\zeta(s)
   \]

64. **Dirichlet beta function**
   \[
   \beta(s)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^s}
   \]

65. **Catalan’s constant**
   \[
   G=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}
   \]

66. **Euler–Mascheroni constant**
   \[
   \gamma=\lim_{N\to\infty}
   \left(\sum_{n=1}^{N}\frac1n-\ln N\right)
   \]

67. **Apéry’s constant**
   \[
   \zeta(3)=\sum_{n=1}^{\infty}\frac1{n^3}
   \]

68. **Alternating zeta at 3**
   \[
   \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^3}
   =\frac34\zeta(3)
   \]

69. **Leibniz series for \(\pi\)**
   \[
   \frac{\pi}{4}
   =\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}
   \]

70. **Ramanujan-type reciprocal-\(\pi\) series**
   \[
   \frac1\pi
   =\frac{2\sqrt2}{9801}
   \sum_{n=0}^{\infty}
   \frac{(4n)!(1103+26390n)}
   {(n!)^4\,396^{4n}}
   \]

## Probability and combinatorics

71. **Poisson distribution normalization**
   \[
   \sum_{n=0}^{\infty}e^{-\lambda}\frac{\lambda^n}{n!}=1
   \]

72. **Poisson probability generating function**
   \[
   \sum_{n=0}^{\infty}
   e^{-\lambda}\frac{\lambda^n}{n!}z^n
   =e^{\lambda(z-1)}
   \]

73. **Binomial theorem as a PMF**
   \[
   \sum_{k=0}^{n}\binom{n}{k}p^k(1-p)^{n-k}=1
   \]

74. **Negative-binomial normalization**
   \[
   \sum_{n=0}^{\infty}
   \binom{n+r-1}{r-1}(1-p)^rp^n=1
   \]

75. **Geometric-distribution normalization**
   \[
   \sum_{n=0}^{\infty}(1-p)^np=1
   \]

76. **Partition generating function**
   \[
   \sum_{n=0}^{\infty}p(n)q^n
   =\prod_{m=1}^{\infty}\frac1{1-q^m}
   \]

77. **Divisor-sum Lambert series**
   \[
   \sum_{n=1}^{\infty}\sigma_k(n)q^n
   =\sum_{m=1}^{\infty}\frac{m^kq^m}{1-q^m}
   \]

78. **Euler pentagonal-number theorem**
   \[
   \prod_{m=1}^{\infty}(1-q^m)
   =
   \sum_{n=-\infty}^{\infty}
   (-1)^n q^{n(3n-1)/2}
   \]

79. **Jacobi theta function**
   \[
   \vartheta_3(z,q)
   =1+2\sum_{n=1}^{\infty}q^{n^2}\cos(2nz)
   \]

80. **Dedekind eta function**
   \[
   \eta(\tau)
   =q^{1/24}\prod_{n=1}^{\infty}(1-q^n),
   \qquad q=e^{2\pi i\tau}
   \]

## Special functions and physics

81. **Gamma function**
   \[
   \Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt
   \]
   This is an integral definition, but its discrete counterpart \(\Gamma(n+1)=n!\) is indispensable.

82. **Incomplete gamma series**
   \[
   \gamma^*(a,z)
   =e^{-z}\sum_{n=0}^{\infty}
   \frac{z^n}{\Gamma(a+n+1)}
   \]

83. **Error function**
   \[
   \operatorname{erf}(z)
   =\frac{2}{\sqrt{\pi}}
   \sum_{n=0}^{\infty}
   \frac{(-1)^nz^{2n+1}}{n!(2n+1)}
   \]

84. **Complementary error-function asymptotic series**
   \[
   \operatorname{erfc}(x)
   \sim
   \frac{e^{-x^2}}{\sqrt{\pi}x}
   \sum_{n=0}^{\infty}
   \frac{(-1)^n(2n-1)!!}{(2x^2)^n}
   \]

85. **Bessel \(J_\nu\)**
   \[
   J_\nu(z)
   =\sum_{n=0}^{\infty}
   \frac{(-1)^n}{n!\Gamma(n+\nu+1)}
   \left(\frac z2\right)^{2n+\nu}
   \]

86. **Bessel \(J_0\)**
   \[
   J_0(z)
   =\sum_{n=0}^{\infty}
   \frac{(-1)^n(z^2/4)^n}{(n!)^2}
   \]

87. **Modified Bessel \(I_\nu\)**
   \[
   I_\nu(z)
   =\sum_{n=0}^{\infty}
   \frac{1}{n!\Gamma(n+\nu+1)}
   \left(\frac z2\right)^{2n+\nu}
   \]

88. **Airy function**
   \[
   \operatorname{Ai}(x)
   =
   \frac{1}{3^{2/3}\Gamma(2/3)}
   \sum_{n=0}^{\infty}
   \frac{(x^3/9)^n}{n!(2/3)_n}
   -
   \frac{x}{3^{1/3}\Gamma(1/3)}
   \sum_{n=0}^{\infty}
   \frac{(x^3/9)^n}{n!(4/3)_n}
   \]

89. **Confluent hypergeometric function**
   \[
   {}_1F_1(a;b;z)
   =\sum_{n=0}^{\infty}
   \frac{(a)_n}{(b)_n}\frac{z^n}{n!}
   \]

90. **Gauss hypergeometric function**
   \[
   {}_2F_1(a,b;c;z)
   =\sum_{n=0}^{\infty}
   \frac{(a)_n(b)_n}{(c)_n}\frac{z^n}{n!}
   \]

91. **Generalized hypergeometric function**
   \[
   {}_pF_q
   \left(
   \begin{matrix}
   a_1,\ldots,a_p\\
   b_1,\ldots,b_q
   \end{matrix};z
   \right)
   =
   \sum_{n=0}^{\infty}
   \frac{(a_1)_n\cdots(a_p)_n}
   {(b_1)_n\cdots(b_q)_n}
   \frac{z^n}{n!}
   \]

92. **Legendre polynomial**
   \[
   P_n(x)
   =
   \sum_{k=0}^{\lfloor n/2\rfloor}
   \frac{(-1)^k(2n-2k)!}
   {2^n k!(n-k)!(n-2k)!}x^{n-2k}
   \]

93. **Legendre generating function**
   \[
   \frac1{\sqrt{1-2xt+t^2}}
   =\sum_{n=0}^{\infty}P_n(x)t^n
   \]

94. **Hermite generating function**
   \[
   e^{2xt-t^2}
   =\sum_{n=0}^{\infty}H_n(x)\frac{t^n}{n!}
   \]

95. **Laguerre generating function**
   \[
   \frac{1}{1-t}
   \exp\left(-\frac{xt}{1-t}\right)
   =\sum_{n=0}^{\infty}L_n(x)t^n
   \]

96. **Chebyshev generating function**
   \[
   \frac{1-xt}{1-2xt+t^2}
   =\sum_{n=0}^{\infty}T_n(x)t^n
   \]

97. **Spherical Bessel \(j_0\)**
   \[
   j_0(x)=\frac{\sin x}{x}
   =\sum_{n=0}^{\infty}
   (-1)^n\frac{x^{2n}}{(2n+1)!}
   \]

98. **Bose–Einstein sum**
   \[
   \sum_{n=1}^{\infty}e^{-n\beta\varepsilon}
   =\frac{1}{e^{\beta\varepsilon}-1}
   \]

99. **Fermi–Dirac alternating sum**
   \[
   \sum_{n=1}^{\infty}(-1)^{n-1}e^{-n\beta\varepsilon}
   =\frac{1}{e^{\beta\varepsilon}+1}
   \]

100. **Heat-kernel / theta sum**
   \[
   \sum_{n=-\infty}^{\infty}e^{-\pi n^2t}
   =
   \frac{1}{\sqrt{t}}
   \sum_{n=-\infty}^{\infty}e^{-\pi n^2/t},
   \qquad t>0
   \]

## A useful study order

| Stage | Focus | Series |
|---|---|---|
| Calculus | Generating functions and Taylor expansions | 1–40 |
| PDEs and signal processing | Fourier representations and kernels | 41–55 |
| Real and analytic number theory | Zeta, eta, beta, Lambert, theta, partitions | 56–70, 76–80, 100 |
| Probability and discrete mathematics | PGFs, exponential generating functions, combinatorial sequences | 17–20, 71–79 |
| Mathematical physics | Bessel, Airy, orthogonal polynomials, quantum-statistical sums | 50–55, 81–100 |

One caveat: not every display above is an ordinary convergent infinite numerical sum. Some are finite expansions indexed by \(n\), generating functions, Fourier series with pointwise/distributional qualifications, or asymptotic expansions. Treat convergence domain, endpoint behavior, and permissible termwise differentiation/integration as part of learning each result. The error-function series, for example, converges for every finite complex argument, while zeta’s defining Dirichlet series initially requires \(\Re(s)>1\). [dlmf.nist](https://dlmf.nist.gov/7.6)

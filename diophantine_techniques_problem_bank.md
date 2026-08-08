# Diophantine Techniques: A Problem Bank

A broad collection of integer-solution problems, deliberately arranged to expose distinct methods. Unless stated otherwise, variables range over \(\mathbb Z\); for problems involving positive quantities, variables range over \(\mathbb Z_{>0}\). Each entry names the principal technique—not necessarily the only one that works.

## 1. Divisibility, congruences, and valuations

1. **Linear divisibility.** Find all integers \(x,y\) such that \(17x+29y=1\).  
   *Technique:* Extended Euclidean algorithm; parametrization of a linear Diophantine equation.

2. **A non-coprime linear equation.** Solve \(84x+126y=210\).  
   *Technique:* GCD solvability criterion followed by parametrization.

3. **Congruence reduction.** Find all integers \(x,y\) satisfying \(7x+11y=1\) with \(x\equiv 3\pmod 5\).  
   *Technique:* Linear equation plus congruence compatibility.

4. **No solution modulo 4.** Prove that \(x^2+y^2=4z+3\) has no integer solutions.  
   *Technique:* Quadratic residues modulo 4.

5. **No solution modulo 3.** Prove that \(x^2+y^2=3z+2\) has no integer solutions when \(3\mid x+y\).  
   *Technique:* Residue classes and a forced congruence relation.

6. **Cubes modulo 9.** Prove that \(x^3+y^3=9z+4\) has no integer solutions.  
   *Technique:* Cubic residues modulo 9.

7. **Fourth powers modulo 16.** Prove that \(x^4+y^4+z^4=16n+3\) has no integer solutions.  
   *Technique:* Fourth-power residues modulo 16.

8. **A valuation obstruction.** Prove that \(x^2=2y^2+1\) has no solutions with \(x\) even.  
   *Technique:* Parity and 2-adic valuation.

9. **Exact valuation.** Determine all \(n\ge1\) for which \(v_2(n^2-1)\ge 5\).  
   *Technique:* Factor \((n-1)(n+1)\); 2-adic valuation.

10. **Lifting a congruence.** Solve \(x^2\equiv 1\pmod{2^k}\) for every \(k\ge3\).  
    *Technique:* 2-adic lifting and factorization.

11. **Odd-prime valuation.** If \(p\) is an odd prime and \(p\mid x^2+y^2\) with \(p\equiv3\pmod4\), prove \(p\mid x\) and \(p\mid y\).  
    *Technique:* Nonresidue of \(-1\) modulo \(p\).

12. **Descent by a prime divisor.** Prove that \(x^2+y^2=3z^2\) has only the zero solution.  
    *Technique:* Infinite descent using the previous prime-divisor lemma.

13. **Chinese remainder construction.** Find the least positive \(x\) with \(x\equiv2\pmod3\), \(x\equiv3\pmod5\), and \(x\equiv4\pmod7\).  
    *Technique:* Chinese remainder theorem.

14. **CRT inside an equation.** Find all positive \(n\) such that \(n\equiv1\pmod8\), \(n\equiv2\pmod3\), and \(n\) is a square.  
    *Technique:* Local conditions; CRT; square residues.

15. **Prime-modulus obstruction.** Prove that \(x^2+3y^2=5z^2\) has no primitive solution with \(5\nmid x\).  
    *Technique:* Reduction modulo 5.

## 2. Linear equations, inequalities, and semigroups

16. **Coin problem.** Determine every \(n\ge0\) representable as \(4x+7y\) with \(x,y\ge0\).  
    *Technique:* Numerical semigroup / Frobenius coin problem.

17. **Three coin types.** Count the nonnegative solutions of \(3x+5y+7z=50\).  
    *Technique:* Fix one variable; congruence and bounded enumeration.

18. **Restricted linear equation.** Find the positive solutions of \(12x+35y=2024\).  
    *Technique:* Parametrization plus positivity bounds.

19. **Floor-function encoding.** Find the number of lattice points \((x,y)\in\mathbb Z_{\ge0}^2\) satisfying \(5x+8y\le100\).  
    *Technique:* Lattice-point counting with floor sums.

20. **Egyptian unit fraction, two terms.** Find all positive integer solutions to \(\frac1x+\frac1y=\frac1n\).  
    *Technique:* Factorization \((x-n)(y-n)=n^2\).

21. **A shifted unit fraction.** Find all positive solutions of \(\frac1x+\frac1y=\frac16\).  
    *Technique:* Divisor enumeration after completing a rectangle.

22. **Linear fractional equation.** Solve \(\frac{x+1}{y+1}=\frac35\) in positive integers.  
    *Technique:* Cross multiplication and coprime divisibility.

23. **Integer triangles.** Find all positive \((a,b,c)\) with \(a+b+c=30\) and \(a^2+b^2=c^2\).  
    *Technique:* Pythagorean parametrization plus perimeter factorization.

24. **Primitive triples.** Prove every primitive positive solution of \(x^2+y^2=z^2\), with \(x\) odd and \(y\) even, is \((m^2-n^2,2mn,m^2+n^2)\).  
    *Technique:* Coprimality and factorization in \(\mathbb Z\).

25. **Heronian constraint.** Find integer-sided right triangles of area 210.  
    *Technique:* Euclid parametrization and divisor analysis.

## 3. Factorization and difference of squares

26. **Difference of squares.** Solve \(x^2-y^2=2025\).  
    *Technique:* Factor pairs \((x-y)(x+y)=2025\).

27. **Consecutive products.** Find all integer solutions of \(x(x+1)=y(y+3)\).  
    *Technique:* Complete squares / factorization after shifting.

28. **Near-square equation.** Solve \(x^2-5y^2=4\) in integers.  
    *Technique:* Pell-type equation and units.

29. **Product is a square.** Find all coprime positive \(x,y\) such that \(xy\) is a square.  
    *Technique:* Prime-exponent parity; squarefree decomposition.

30. **Product is a cube.** Find all coprime positive \(x,y\) such that \(xy\) is a cube.  
    *Technique:* Unique factorization of integers; exponent decomposition.

31. **Square triangular numbers.** Find positive \(n,m\) with \(n(n+1)/2=m^2\).  
    *Technique:* Transform to Pell equation \((2n+1)^2-8m^2=1\).

32. **Difference of two fourth powers.** Solve \(x^4-y^4=15\).  
    *Technique:* Factorization \((x-y)(x+y)(x^2+y^2)\), inequalities.

33. **Sophie Germain factorization.** Solve \(x^4+4y^4=z^2\).  
    *Technique:* Sophie Germain identity and factor analysis.

34. **A factor-pair elliptic-looking problem.** Find integer solutions to \(xy=x+y+12\).  
    *Technique:* Rearrangement: \((x-1)(y-1)=13\).

35. **Polynomial factorization.** Find integers \(x,y\) satisfying \(x^3-y^3=x-y\).  
    *Technique:* Factor \((x-y)(x^2+xy+y^2-1)=0\).

## 4. Infinite descent and Fermat-style arguments

36. **No square of the form \(2m^2\).** Prove \(x^2=2y^2\) has only \((0,0)\).  
    *Technique:* Parity and infinite descent.

37. **Fermat's right-triangle theorem.** Prove no right triangle with positive integer sides has square area.  
    *Technique:* Infinite descent through primitive Pythagorean triples.

38. **Quartic impossibility.** Prove \(x^4+y^4=z^2\) has no positive integer solutions.  
    *Technique:* Fermat descent using a minimal counterexample.

39. **A descent equation.** Prove \(x^4-y^4=z^2\) has no positive solutions with \(x>y\).  
    *Technique:* Factorization plus descent / the previous theorem.

40. **No primitive solution.** Prove \(x^2+y^2=7z^2\) has no primitive nonzero integer solution.  
    *Technique:* Descent modulo a prime \(7\equiv3\pmod4\).

41. **Sum of two biquadrates.** Determine whether \(x^4+y^4=2z^4\) has nonzero integer solutions.  
    *Technique:* Factorization and descent / parity.

42. **A minimal-counterexample exercise.** Prove that no positive integer cube can be written as the sum of two positive consecutive squares.  
    *Technique:* Factorization \(x^2+(x+1)^2\); congruence or descent.

## 5. Pell equations and continued fractions

43. **Classical Pell.** Find all positive solutions of \(x^2-2y^2=1\).  
    *Technique:* Continued fractions or powers of \(3+2\sqrt2\).

44. **Negative Pell.** Find all positive solutions of \(x^2-2y^2=-1\).  
    *Technique:* Continued fractions; powers of \(1+\sqrt2\).

45. **A nonsquare discriminant.** Find the fundamental positive solution of \(x^2-61y^2=1\).  
    *Technique:* Continued fraction of \(\sqrt{61}\).

46. **Generalized Pell.** Solve \(x^2-5y^2=-4\).  
    *Technique:* Norms in \(\mathbb Z[(1+\sqrt5)/2]\) or recurrence construction.

47. **Triangular square.** Find the first five square triangular numbers.  
    *Technique:* Pell recurrence from \(u^2-8v^2=1\).

48. **Almost-isosceles triangles.** Find integer-sided triangles whose equal sides differ from the base by 1 and whose area is integral.  
    *Technique:* Heron’s formula transformed to Pell equations.

49. **Pell with congruence filter.** Find solutions of \(x^2-3y^2=1\) for which \(x\equiv1\pmod8\).  
    *Technique:* Unit recurrence modulo 8.

50. **Continued-fraction approximation.** Prove that the convergents of \(\sqrt d\) produce candidates for small values of \(|x^2-dy^2|\), then apply this to \(d=13\).  
    *Technique:* Continued fractions and best approximation.

## 6. Quadratic forms and sums of squares

51. **Two squares criterion.** Determine whether 2026 is a sum of two integer squares.  
    *Technique:* Prime factorization and the sum-of-two-squares theorem.

52. **Representations by \(x^2+y^2\).** Find all integer pairs \((x,y)\) with \(x^2+y^2=325\).  
    *Technique:* Gaussian integers or elementary factorization.

53. **A norm equation.** Solve \(x^2+xy+y^2=19\).  
    *Technique:* Eisenstein integers / binary quadratic forms.

54. **Three squares.** Decide which integers of the form \(4^a(8b+7)\) can be represented as \(x^2+y^2+z^2\).  
    *Technique:* Legendre’s three-square theorem; local obstruction.

55. **Four squares.** Exhibit a representation of 2025 as a sum of four squares.  
    *Technique:* Lagrange’s four-square theorem; constructive search.

56. **Primitive representations.** Find all primitive integer solutions to \(x^2+2y^2=z^2\).  
    *Technique:* Parametrization of a conic / factorization over \(\mathbb Z[\sqrt{-2}]\).

57. **Anisotropic form.** Prove \(x^2+xy+y^2=0\) has only \((0,0)\) over \(\mathbb Z\).  
    *Technique:* Positive definiteness, or discriminant \(-3\).

58. **Indefinite form.** Find infinitely many solutions to \(x^2-2xy-y^2=1\).  
    *Technique:* Change variables and reduce to Pell.

## 7. Rational points, conics, and parametrization

59. **Unit circle.** Parametrize all rational solutions of \(x^2+y^2=1\).  
    *Technique:* Line through a known rational point.

60. **Integer Pythagorean triples from rational points.** Derive Euclid’s formula by clearing denominators in the unit-circle parametrization.  
    *Technique:* Rational parametrization of a conic.

61. **Hyperbola.** Parametrize rational solutions of \(xy=1\).  
    *Technique:* Choose a free rational parameter.

62. **A conic with one point.** Find all rational points on \(x^2-2y^2=1\) using lines through \((1,0)\).  
    *Technique:* Chord-and-tangent parametrization.

63. **Integral points after parametrization.** Find primitive integer solutions of \(x^2+xy=2y^2\).  
    *Technique:* Factorization or rational slopes plus integrality constraints.

64. **Pythagorean quadruples.** Find integer solutions to \(x^2+y^2+z^2=w^2\).  
    *Technique:* Stereographic parametrization of a quadric.

## 8. Exponential Diophantine equations

65. **Catalan/Mihăilescu application.** Solve \(x^a-y^b=1\) in integers \(x,y>1\), \(a,b>1\).  
    *Technique:* Mihăilescu’s theorem; exceptional solution \(3^2-2^3=1\).

66. **Elementary exponential equation.** Solve \(2^x+2^y=2^z\) in nonnegative integers.  
    *Technique:* Factor out the smaller power of 2.

67. **Prime-power sum.** Solve \(p^a+q^b=2^n\) under the assumption that \(p,q\) are odd primes.  
    *Technique:* Parity, valuations, and factorization; explore cases.

68. **Ramanujan–Nagell equation.** Solve \(x^2+7=2^n\).  
    *Technique:* Congruences, factorization in quadratic rings, or known theorem.

69. **Lebesgue–Nagell flavor.** Solve \(x^2+1=2y^4\).  
    *Technique:* Factorization in Gaussian integers / descent.

70. **Powers differing by a square.** Solve \(2^n-1=m^2\) in nonnegative integers \(n,m\).  
    *Technique:* Factor \((2^{n/2}-m)(2^{n/2}+m)\) when appropriate; parity cases.

71. **Perfect powers in Fibonacci numbers.** Determine the square Fibonacci numbers.  
    *Technique:* Recurrences, identities, and deep results; useful research-level extension.

72. **Pillai-type exploration.** For fixed \(k=13\), find small solutions of \(x^a-y^b=k\) with \(a,b\ge2\).  
    *Technique:* Modular sieving and bounded computational search, then proof for restricted exponents.

## 9. Divisors, recurrences, and special sequences

73. **Divisor pairing.** Find all \(n\) such that \(\tau(n)=6\).  
    *Technique:* Prime-exponent patterns.

74. **Perfect numbers.** Show that if \(2^p-1\) is prime, then \(2^{p-1}(2^p-1)\) is perfect.  
    *Technique:* Divisor-sum function and geometric series.

75. **Consecutive divisor property.** Find \(n\) for which \(n\mid 2^n-2\).  
    *Technique:* Carmichael numbers / Korselt’s criterion; research-level classification direction.

76. **Wilson-type equation.** Find primes \(p\) satisfying \((p-1)!\equiv-1\pmod p\).  
    *Technique:* Wilson’s theorem.

77. **A recurrence divisibility problem.** Prove \(F_m\mid F_n\) if and only if \(m\mid n\), where \(F_n\) is Fibonacci.  
    *Technique:* Euclidean algorithm on indices; gcd identity.

78. **Lucas-square relation.** Prove \(L_n^2-5F_n^2=4(-1)^n\).  
    *Technique:* Binet identities or matrix recurrences; leads to Pell equations.

## 10. Elliptic curves and higher-genus problems

79. **A Mordell equation.** Find integral solutions of \(y^2=x^3-2\).  
    *Technique:* Factorization in \(\mathbb Z[\sqrt{-2}]\), descent, or elliptic-curve methods.

80. **Congruent numbers.** Determine whether 5 is a congruent number.  
    *Technique:* Rational right triangles; elliptic curve \(y^2=x^3-25x\).

81. **Integral points on an elliptic curve.** Find integer points on \(y^2=x^3-x\).  
    *Technique:* Factorization \(x(x-1)(x+1)\), descent, or elliptic curves.

82. **Fermat cubic.** Find rational solutions to \(x^3+y^3=1\).  
    *Technique:* Elliptic-curve group law; distinguish rational from integer solutions.

83. **A genus-one quartic.** Determine integer solutions of \(y^2=x^4-x\).  
    *Technique:* Quartic-to-elliptic transformation; local sieving.

84. **Generalized Fermat challenge.** Investigate \(x^2+y^3=z^7\) in primitive positive integers.  
    *Technique:* Modular method / arithmetic geometry; research-level.

## Suggested use

Work through the collection in roughly this order: sections 1–3 for elementary tools, sections 4–6 for structural methods, sections 7–9 for parametrization and algebraic number theory, and section 10 for modern arithmetic geometry. For each problem, try to record: (1) local obstructions modulo carefully chosen moduli, (2) gcd and parity reductions, (3) a factorization or parametrization, and (4) whether the resulting family is finite, infinite, or recursively generated.

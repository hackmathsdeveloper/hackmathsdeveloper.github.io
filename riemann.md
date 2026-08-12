
The **Riemann Hypothesis (RH)** says that every *nontrivial zero* of the Riemann zeta function  
\[
\zeta(s)=\sum_{n\ge1}n^{-s}=\prod_{p}(1-p^{-s})^{-1}
\]
has real part exactly \(1/2\). In symbols: if \(\zeta(\rho)=0\) and \(\rho\) is not a trivial zero \(-2,-4,\ldots\), then \(\Re(\rho)=1/2\). It remains unproved. The reason it matters is that zeros of \(\zeta\) govern the error in the average laws describing where primes occur. [claymath](https://www.claymath.org/collections/riemanns-1859-manuscript/)

## Core picture

The Euler product is the bridge:
\[
\zeta(s)=\prod_{p}(1-p^{-s})^{-1}\qquad(\Re(s)>1).
\]

It packages every prime into one analytic object. Riemann showed that prime-counting formulas contain oscillatory terms of the rough form \(x^\rho/\rho\), one for each nontrivial zero \(\rho\). Thus, if every \(\rho\) has real part \(1/2\), the fluctuations in prime counts are essentially “square-root sized,” modulo logarithms and unavoidable secondary effects.

RH is therefore not the prime number theorem itself. The prime number theorem only says
\[
\pi(x)\sim \frac{x}{\log x}.
\]
RH predicts a near-optimal bound on the **error** around that average. [claymath](https://www.claymath.org/collections/riemanns-1859-manuscript/)

## Fifty consequences and formulations

Below, “equivalent” means proving that statement would prove RH and vice versa. “RH implies” means it is a conditional consequence. A few are analytic reformulations rather than applications.

### Prime distribution

1. **Equivalent:** all nontrivial zeta zeros lie on \(\Re s=1/2\).
2. **Equivalent:** \(\zeta(s)\neq0\) for every \(\Re s>1/2\).
3. **RH implies:** primes have near-square-root-scale irregularity around their expected density.
4. **Equivalent:** for every \(\varepsilon>0\),
   \[
   \pi(x)=\operatorname{Li}(x)+O(x^{1/2+\varepsilon}).
   \]
5. **RH implies:**
   \[
   \pi(x)=\operatorname{Li}(x)+O(\sqrt{x}\log x).
   \]
6. **Equivalent:** Chebyshev’s function
   \[
   \psi(x)=\sum_{n\le x}\Lambda(n)
   \]
   satisfies \(\psi(x)=x+O(x^{1/2+\varepsilon})\) for every \(\varepsilon>0\).
7. **RH implies:**
   \[
   \psi(x)=x+O(\sqrt{x}\log^2x).
   \]
8. **RH implies:** the weighted prime sum \(\vartheta(x)=\sum_{p\le x}\log p\) is \(x\) plus a square-root-scale error.
9. **RH implies:** the \(n\)-th prime is very tightly approximated by the inverse of \(\operatorname{Li}\).
10. **RH implies:** the average prime-gap scale \(\log x\) has highly constrained cumulative fluctuations.
11. **RH implies:** estimates for primes in short intervals improve substantially, though RH alone does **not** prove a prime in every interval of the conjecturally shortest possible length.
12. **RH implies:** estimates for the number of prime powers \(p^k\le x\) inherit controlled error terms.
13. **RH implies:** Riemann’s prime-counting function \(J(x)\) differs from its smooth approximation by essentially square-root scale.
14. **RH implies:** explicit formulas for prime counts become quantitatively effective once enough zeros are known.
15. **RH implies:** many bounds for arithmetic functions with Dirichlet series built from \(\zeta(s)\) improve after contour shifting to just right of \(1/2\).

### Möbius, divisors, and integers

16. **Equivalent:** for every \(\varepsilon>0\), the Mertens function satisfies
   \[
   M(x):=\sum_{n\le x}\mu(n)=O(x^{1/2+\varepsilon}).
   \]
17. **Interpretation:** the signs of the Möbius function \(\mu(n)\) exhibit enough cancellation to look “random” at the square-root scale.
18. **RH implies:** sums of \(\mu(n)\) against many sufficiently regular test functions have strong cancellation.
19. **RH implies:** error terms in inclusion–exclusion problems involving divisibility can often be sharpened.
20. **RH implies:** summatory functions involving \(\Lambda(n)\), \(\mu(n)\), and \(1/\zeta(s)\) admit better analytic bounds.
21. **Equivalent (Robin criterion):**
   \[
   \sigma(n)<e^\gamma n\log\log n\qquad(n>5040),
   \]
   where \(\sigma(n)\) is the sum of divisors of \(n\).
22. **Equivalent (Lagarias criterion):**
   \[
   \sigma(n)\le H_n+e^{H_n}\log H_n
   \]
   for every positive integer \(n\), where \(H_n=\sum_{k\le n}1/k\).
23. **RH implies:** extremal behavior of the divisor-sum ratio \(\sigma(n)/n\) is tightly bounded.
24. **RH implies:** related maximal-order estimates for multiplicative functions become more precise.
25. **RH implies:** estimates for summatory generalized divisor functions can be improved in many ranges.
26. **RH implies:** certain lattice-point counting problems with arithmetic restrictions acquire better remainder terms.
27. **RH implies:** error analysis for squarefree and coprimality sieves can be improved when Möbius cancellation is the bottleneck.
28. **RH implies:** several estimates for smooth-number and rough-number counting gain sharper secondary terms.
29. **RH implies:** some average estimates for arithmetic progressions of multiplicative functions improve.
30. **RH does not imply:** simple pointwise randomness of \(\mu(n)\); it constrains partial sums, not individual values.

### Exact analytic criteria

31. **Equivalent (Li criterion):** every Li coefficient \(\lambda_n\) is nonnegative:
   \[
   \lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right]\ge0
   \quad(n\ge1).
   \]
32. **Equivalent (Weil criterion):** a certain family of quadratic forms derived from the explicit formula is nonnegative.
33. **Equivalent (Nyman–Beurling):** a particular subspace generated by fractional-part functions is dense in \(L^2(0,1)\).
34. **Equivalent (Báez-Duarte refinement):** a discrete version of the Nyman–Beurling approximation problem holds.
35. **Equivalent:** the de Bruijn–Newman constant \(\Lambda\) is at most zero.
36. **Equivalent (Balazard–Saias–Yor):** a specific logarithmic integral involving \(\log|\zeta(1/2+it)|\) has its critical value.
37. **Equivalent (Volchkov):** a particular weighted integral of \(\arg \zeta(1/2+it)\) has an exact prescribed value.
38. **Equivalent:** various positivity criteria for transforms of the completed zeta function hold.
39. **Equivalent:** all zeros of the Riemann \(\xi\)-function are real after writing \(s=1/2+it\).
40. **Equivalent:** certain Fourier/cosine-transform kernels associated with \(\xi\) satisfy positivity properties.

The prime-counting, Möbius, Li, Weil, and divisor-sum criteria are standard examples of the fact that RH has many genuinely different-looking equivalent forms. [ams](https://www.ams.org/notices/200303/fea-conrey-web.pdf)

### Other mathematical impacts

41. **RH implies:** the Lindelöf hypothesis:
   \[
   \zeta(1/2+it)\ll_\varepsilon t^\varepsilon.
   \]
42. **RH implies:** improved estimates for many moments and mean values involving \(\zeta(s)\), although it does not settle all moment conjectures.
43. **RH implies:** stronger bounds for errors in some counting problems on algebraic/arithmetic objects governed by zeta quotients.
44. **RH implies:** sharper estimates for some Farey-fraction distribution statistics.
45. **RH implies:** better discrepancy bounds in certain number-theoretic equidistribution problems.
46. **RH implies:** sharper asymptotic formulas for some summatory multiplicative functions.
47. **RH implies:** many algorithms that rely on prime-counting bounds receive certified tighter complexity or search-range estimates.
48. **RH alone does not prove:** the Generalized Riemann Hypothesis (GRH) for Dirichlet \(L\)-functions.
49. **Therefore RH alone does not automatically give:** the usual GRH-conditional results about least primes in residue classes, primitive roots, or polynomial factoring.
50. **It does not endanger modern cryptography if false:** RSA and ECC do not rely on RH being true; RH/GRH mainly give sharper provable bounds for some number-theoretic algorithms.

## Coprimality connection

Two integers \(a,b\) are coprime precisely when \(\gcd(a,b)=1\), equivalently, when no prime divides both. The zeta function enters because each prime \(p\) independently contributes a local exclusion condition.

For two random positive integers, the probability that both are divisible by a fixed prime \(p\) is \(1/p^2\). Hence the heuristic—and, in the limiting-density sense, theorem—is
\[
\Pr(\gcd(a,b)=1)
 =\prod_p\left(1-\frac1{p^2}\right)
 =\frac1{\zeta(2)}
 =\frac6{\pi^2}.
\]
More generally, the probability that \(k\) random integers have no common prime divisor is
\[
\frac1{\zeta(k)}.
\]
This is an exact structural connection between coprimality and \(\zeta\), but it uses the value at \(s=2\), not the zeros in the critical strip. [en.wikipedia](https://en.wikipedia.org/wiki/Coprime_integers)

The combinatorial identity behind it is Möbius inversion:
\[
1_{\gcd(a,b)=1}=\sum_{d\mid \gcd(a,b)}\mu(d).
\]
Therefore
\[
C(N):=\#\{1\le a,b\le N:\gcd(a,b)=1\}
=\sum_{d\le N}\mu(d)\left\lfloor\frac Nd\right\rfloor^2.
\]
Its leading term is
\[
C(N)=\frac{N^2}{\zeta(2)}+\text{error}
=\frac{6}{\pi^2}N^2+\text{error}.
\]

## Where RH enters coprimality

RH is related to coprimality **through the error term**, because the error term above involves sums of \(\mu(d)\), and RH is equivalent to near-square-root cancellation in
\[
M(x)=\sum_{n\le x}\mu(n).
\]

So the hierarchy is:

- The constant \(6/\pi^2\) comes from the Euler product and is already known unconditionally.
- Möbius inversion turns coprimality counts into sums weighted by \(\mu(d)\).
- RH predicts especially strong cancellation among these Möbius weights.
- That cancellation yields sharper error estimates for many refined “visible lattice point” and coprime-tuple counting problems.

Geometrically: integer points \((a,b)\) visible from the origin are exactly those with \(\gcd(a,b)=1\). Their density is \(6/\pi^2\). RH does not change that density; it constrains how irregularly the visible points deviate from that average at large scales. The equivalent Mertens bound is the main analytic expression of this connection. [aimath](https://aimath.org/~kaur/publications/90.pdf)

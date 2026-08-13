
https://chat.qwen.ai/c/43e31e9c-5e4f-4a01-b82a-7c746628495d
Below is a curated list of **55 numbered statements equivalent to the classical Riemann Hypothesis (RH)** for the Riemann zeta-function, followed by a separate, explicitly flagged entry for the **Lindelöf hypothesis**. I have included the requested items on **π(x)**, **M(x)**, **Robin’s inequality**, and **Lindelöf-type formulations**, with growth rates, documentation links, and citations to foundational proofs.

---

## Important caveat about the Lindelöf hypothesis

The classical **Lindelöf hypothesis**,

\[
\zeta(1/2+it)=O_\varepsilon(|t|^\varepsilon)\qquad (|t|\to\infty),
\]

is **not known to be equivalent to RH**. It is a **consequence** of RH, but the converse is open. I therefore list it separately at the end, with its correct logical status, and I include genuinely equivalent **Lindelöf-type** formulations in the main list (e.g. items 26 and 28).

---

## Notation and conventions

- RH means: every non-trivial zero \(\rho=\beta+i\gamma\) of \(\zeta(s)\) satisfies \(\beta=1/2\).
- \(\varepsilon>0\) is arbitrary; constants in \(O_\varepsilon(\cdot)\) may depend on \(\varepsilon\).
- \(\psi(x)=\sum_{n\le x}\Lambda(n)\), \(\theta(x)=\sum_{p\le x}\log p\), \(\pi(x)=\#\{p\le x\}\).
- \(\operatorname{li}(x)\) is the logarithmic integral.
- \(M(x)=\sum_{n\le x}\mu(n)\), \(L(x)=\sum_{n\le x}\lambda(n)\).
- \(\sigma(n)=\sum_{d\mid n}d\), \(\gamma\) is Euler’s constant.
- Links include encyclopedic documentation and/or primary sources. For older results, standard books such as Titchmarsh, Davenport, Edwards, Ivić, and Montgomery–Vaughan are often the best accessible proofs.

Key general references:

- Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed.  
  <https://doi.org/10.1093/oso/9780198533696.001.0001>
- Davenport, *Multiplicative Number Theory*, 3rd ed.  
  <https://doi.org/10.1007/978-1-4757-5927-3>
- Montgomery–Vaughan, *Multiplicative Number Theory I*.  
  <https://doi.org/10.1017/CBO9780511619762>
- Edwards, *Riemann’s Zeta Function*.  
  <https://store.doverpublications.com/0486438139.html>
- Ivić, *The Riemann Zeta-Function*.  
  <https://www.wiley.com/en-us/The+Riemann+Zeta+Function%3A+The+Theory+of+the+Riemann+Zeta+Function+with+Applications-p-9780471806349>

---

# A. Zero-location and function-theoretic equivalences

### 1. Classical zero-line statement

**Statement.** Every non-trivial zero of \(\zeta(s)\) lies on \(\Re(s)=1/2\).  
**Growth/rate.** Zero location: \(\rho=1/2+i\gamma\).  
**Documentation.**  
- Riemann hypothesis: <https://en.wikipedia.org/wiki/Riemann_hypothesis>  
**Foundational proof/citations.** Riemann’s memoir; von Mangoldt’s theory of zeros; Titchmarsh, Ch. 2. The equivalence with all other statements below is ultimately through the zeros \(\rho\) in explicit formulas and Perron integrals.

---

### 2. Zero-free half-plane formulation

**Statement.** RH is equivalent to

\[
\zeta(s)\neq 0 \quad \text{for } \Re(s)>1/2.
\]

**Growth/rate.** Zero-free region: no zeros to the right of the critical line.  
**Documentation.**  
- Functional equation and zeros: <https://en.wikipedia.org/wiki/Riemann_zeta_function>  
**Foundational proof/citations.** Follows immediately from the functional equation and symmetry of zeros about \(\Re(s)=1/2\); Titchmarsh, Ch. 2.

---

### 3. Completed zeta-function \(\xi(s)\) zeros

**Statement.** Let

\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

RH is equivalent to all zeros of \(\xi(s)\) lying on \(\Re(s)=1/2\).  
**Growth/rate.** Zero location for the entire completed zeta-function.  
**Documentation.**  
- Riemann xi-function: <https://en.wikipedia.org/wiki/Riemann_xi_function>  
**Foundational proof/citations.** Hadamard product and functional equation; Edwards, Ch. 2; Titchmarsh, Ch. 2.

---

### 4. Reality of zeros of \(\Xi(t)=\xi(1/2+it)\)

**Statement.** RH is equivalent to the assertion that

\[
\Xi(t)=\xi(1/2+it)
\]

has only real zeros.  
**Growth/rate.** All zeros of the real-even function \(\Xi(t)\) are real.  
**Documentation.**  
- Riemann xi-function: <https://en.wikipedia.org/wiki/Riemann_xi_function>  
**Foundational proof/citations.** Hardy’s \(Z\)-function framework; Titchmarsh, Ch. 6.

---

### 5. Equality of zero-counting functions

**Statement.** Let \(N(T)\) be the number of non-trivial zeros with \(0<\Im\rho<T\), and \(N_0(T)\) the number of zeros on the critical line. RH is equivalent to

\[
N_0(T)=N(T)\quad\text{for all }T>0.
\]

**Growth/rate.** Exact equality of zero counts.  
**Documentation.**  
- Riemann–von Mangoldt formula: <https://en.wikipedia.org/wiki/Riemann%E2%80%93von_Mangoldt_formula>  
**Foundational proof/citations.** Riemann–von Mangoldt counting formula and argument principle; Titchmarsh, Ch. 6.

---

### 6. Laguerre–Pólya class formulation

**Statement.** RH is equivalent to the assertion that the function \(\Xi(z)=\xi(1/2+iz)\) belongs to the Laguerre–Pólya class, i.e. is a locally uniform limit of polynomials with only real zeros.  
**Growth/rate.** Entire-function class condition.  
**Documentation.**  
- Laguerre–Pólya class: <https://en.wikipedia.org/wiki/Laguerre%E2%80%93P%C3%B3lya_class>  
**Foundational proof/citations.** Pólya’s work on \(\Xi\); Titchmarsh, Ch. 10; Edwards, Ch. 10.

---

### 7. Jensen polynomial hyperbolicity

**Statement.** RH is equivalent to the hyperbolicity (all roots real) of all Jensen polynomials attached to the Taylor coefficients of \(\xi\) or \(\Xi\).  
**Growth/rate.** Real-rootedness for an infinite family of polynomials.  
**Documentation.**  
- Jensen polynomials: <https://en.wikipedia.org/wiki/Jensen_polynomial>  
- Griffin–Ono–Rolen–Runkel, “Jensen polynomials and the Turán inequality”: <https://arxiv.org/abs/1901.01160>  
**Foundational proof/citations.** Jensen (1927); modern treatment in Griffin–Ono–Rolen–Runkel.

---

### 8. de Bruijn–Newman constant

**Statement.** Let \(\Lambda\) be the de Bruijn–Newman constant. RH is equivalent to

\[
\Lambda\le 0.
\]

Since Rodgers–Tao proved \(\Lambda\ge 0\), RH is equivalent to \(\Lambda=0\).  
**Growth/rate.** Threshold parameter for zero deformation.  
**Documentation.**  
- de Bruijn–Newman constant: <https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant>  
- Rodgers–Tao: <https://arxiv.org/abs/1801.05914>  
**Foundational proof/citations.** de Bruijn (1950), Newman (1976), Rodgers–Tao (2020).

---

### 9. Li’s criterion

**Statement.** RH is equivalent to the non-negativity of all Li coefficients

\[
\lambda_n=\sum_{\rho}\left[1-\left(1-\frac1\rho\right)^n\right]\ge 0
\qquad(n=1,2,\dots).
\]

**Growth/rate.** \(\lambda_n\sim \frac n2\log n\) under RH; positivity is the criterion.  
**Documentation.**  
- Li’s criterion: <https://en.wikipedia.org/wiki/Li%27s_criterion>  
- Li (1997): <https://doi.org/10.1006/jnth.1997.2131>  
**Foundational proof/citations.** Xian-Jin Li, *J. Number Theory* 65 (1997), 325–333.

---

### 10. Bombieri–Lagarias positivity criterion

**Statement.** RH is equivalent to a positivity condition in the Weil explicit formula: for a suitable class of positive-definite test functions, the sum over zeros satisfies a positivity inequality.  
**Growth/rate.** Positivity of a spectral distribution.  
**Documentation.**  
- Bombieri–Lagarias, “A local Riemann hypothesis, I”: <https://arxiv.org/abs/math/9902059>  
**Foundational proof/citations.** Bombieri–Lagarias, *Math. Res. Lett.* 6 (1999), 1–17.

---

### 11. Weil explicit formula positivity

**Statement.** RH is equivalent to positivity of Weil’s explicit-formula distribution: roughly, the zero side of Weil’s explicit formula defines a positive measure/distribution if and only if RH holds.  
**Growth/rate.** Positivity of a distribution.  
**Documentation.**  
- Conrey, “The Riemann Hypothesis”, *Notices AMS*: <https://www.ams.org/notices/200303/fea-conrey.pdf>  
**Foundational proof/citations.** Weil (1952); exposition in Conrey (2003).

---

### 12. Nyman–Beurling theorem

**Statement.** RH is equivalent to the assertion that the constant function \(1\) lies in the \(L^2(0,1)\)-closure of the span of the fractional-part dilates

\[
x\mapsto \left\{\frac{\theta}{x}\right\},\qquad 0<\theta\le 1.
\]

**Growth/rate.** Density in a Hilbert space.  
**Documentation.**  
- Nyman–Beurling theorem: <https://en.wikipedia.org/wiki/Nyman%E2%80%93Beurling_theorem>  
**Foundational proof/citations.** Nyman (1950), Beurling (1955); see also Báez-Duarte et al.

---

### 13. Báez-Duarte refinement of Nyman–Beurling

**Statement.** RH is equivalent to the vanishing of a certain weighted \(L^2\) distance \(d_N\to0\), where \(d_N\) measures approximation of the constant function by fractional-part/Dirichlet-polynomial approximants.  
**Growth/rate.** \(d_N\to0\).  
**Documentation.**  
- Báez-Duarte, “A note on the Nyman–Beurling criterion”: <https://arxiv.org/abs/math/0302094>  
**Foundational proof/citations.** Báez-Duarte and collaborators (2003).

---

# B. Prime-counting and Chebyshev-function equivalences

### 14. Error term for \(\psi(x)\) with arbitrary \(\varepsilon\)

**Statement.** RH is equivalent to

\[
\psi(x)=x+O_\varepsilon\!\left(x^{1/2+\varepsilon}\right)
\qquad (x\to\infty).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Chebyshev function: <https://en.wikipedia.org/wiki/Chebyshev_function>  
**Foundational proof/citations.** von Mangoldt explicit formula

\[
\psi(x)=x-\sum_\rho \frac{x^\rho}{\rho}+\text{small terms},
\]

and contour shifting/Perron’s formula; Davenport, Ch. 18; Titchmarsh, Ch. 14.

---

### 15. Sharp logarithmic error term for \(\psi(x)\)

**Statement.** RH is equivalent to

\[
\psi(x)=x+O\!\left(x^{1/2}\log^2 x\right).
\]

**Growth/rate.** \(O(x^{1/2}\log^2 x)\).  
**Documentation.**  
- Schoenfeld (1976): <https://doi.org/10.1090/S0025-5718-1976-0457395-6>  
**Foundational proof/citations.** von Mangoldt explicit formula; sharp conditional bounds due to Schoenfeld.

---

### 16. Error term for \(\theta(x)\) with arbitrary \(\varepsilon\)

**Statement.** RH is equivalent to

\[
\theta(x)=x+O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Chebyshev function: <https://en.wikipedia.org/wiki/Chebyshev_function>  
**Foundational proof/citations.** \(\theta\) and \(\psi\) differ by prime powers; standard equivalence; Titchmarsh, Davenport.

---

### 17. Sharp logarithmic error term for \(\theta(x)\)

**Statement.** RH is equivalent to

\[
\theta(x)=x+O\!\left(x^{1/2}\log^2 x\right).
\]

**Growth/rate.** \(O(x^{1/2}\log^2 x)\).  
**Documentation.**  
- Schoenfeld (1976): <https://doi.org/10.1090/S0025-5718-1976-0457395-6>  
**Foundational proof/citations.** Schoenfeld’s conditional Chebyshev bounds.

---

### 18. Prime-counting function with arbitrary \(\varepsilon\)

**Statement.** RH is equivalent to

\[
\pi(x)=\operatorname{li}(x)+O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Prime-counting function: <https://en.wikipedia.org/wiki/Prime-counting_function>  
**Foundational proof/citations.** Partial summation from \(\psi(x)\) or \(\theta(x)\); Titchmarsh, Ch. 14; Davenport, Ch. 18.

---

### 19. Prime-counting function with logarithmic factor

**Statement.** RH is equivalent to

\[
\pi(x)=\operatorname{li}(x)+O\!\left(x^{1/2}\log x\right).
\]

**Growth/rate.** \(O(x^{1/2}\log x)\).  
**Documentation.**  
- Schoenfeld (1976): <https://doi.org/10.1090/S0025-5718-1976-0457395-6>  
**Foundational proof/citations.** Schoenfeld’s conditional bounds; equivalence follows because this error implies the \(O(x^{1/2+\varepsilon})\) criterion.

---

### 20. Schoenfeld’s explicit RH-bound for \(\pi(x)\)

**Statement.** RH is equivalent to the validity, for all \(x\ge 2657\), of

\[
|\pi(x)-\operatorname{li}(x)|
<
\frac{1}{8\pi}\sqrt{x}\log x.
\]

**Growth/rate.** Explicit constant times \(\sqrt{x}\log x\).  
**Documentation.**  
- Schoenfeld (1976): <https://doi.org/10.1090/S0025-5718-1976-0457395-6>  
**Foundational proof/citations.** Schoenfeld proved this bound under RH; if it holds unconditionally, it implies the \(O(\sqrt{x}\log x)\) criterion and hence RH.

---

### 21. Error term for the \(n\)-th prime

**Statement.** RH is equivalent to

\[
p_n=\operatorname{li}^{-1}(n)+O\!\left(\sqrt{n}\log n\right),
\]

or, more explicitly, to the corresponding asymptotic expansion for \(p_n\) with an \(O(\sqrt{n}\log n)\) remainder.  
**Growth/rate.** \(O(\sqrt{n}\log n)\).  
**Documentation.**  
- Prime number theorem and \(n\)-th prime: <https://en.wikipedia.org/wiki/Prime_number_theorem>  
**Foundational proof/citations.** Inversion of the \(\pi(x)\)-estimate; Schoenfeld (1976).

---

# C. Mertens, Möbius, Liouville, and reciprocal-zeta equivalences

### 22. Mertens function with arbitrary \(\varepsilon\)

**Statement.** RH is equivalent to

\[
M(x)=\sum_{n\le x}\mu(n)=O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** Perron formula for \(1/\zeta(s)\) and contour shifting; zeros of \(\zeta\) are poles of \(1/\zeta\). Littlewood; Titchmarsh, Ch. 14; Davenport, Ch. 18.

---

### 23. Weighted Mertens sum \(\sum \mu(n)/n\)

**Statement.** RH is equivalent to

\[
\sum_{n\le x}\frac{\mu(n)}{n}
=
O_\varepsilon\!\left(x^{-1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{-1/2+\varepsilon})\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** Partial summation from \(M(x)\); conversely recover \(M(x)\) by partial summation.

---

### 24. Convergence of the Möbius Dirichlet series for \(\Re(s)>1/2\)

**Statement.** RH is equivalent to convergence of

\[
\sum_{n=1}^\infty \frac{\mu(n)}{n^s}
\]

for every \(s\) with \(\Re(s)>1/2\).  
**Growth/rate.** Abscissa of convergence \(\le 1/2\).  
**Documentation.**  
- Möbius function: <https://en.wikipedia.org/wiki/M%C3%B6bius_function>  
**Foundational proof/citations.** The sum equals \(1/\zeta(s)\) for \(\Re(s)>1\); convergence beyond \(\Re(s)=1\) precludes poles, hence zeros, to the right of \(1/2\). Littlewood; Davenport.

---

### 25. Holomorphy of \(1/\zeta(s)\) to the right of \(1/2\)

**Statement.** RH is equivalent to \(1/\zeta(s)\) being holomorphic in the half-plane

\[
\Re(s)>1/2.
\]

**Growth/rate.** Analytic continuation/no poles.  
**Documentation.**  
- Riemann zeta function: <https://en.wikipedia.org/wiki/Riemann_zeta_function>  
**Foundational proof/citations.** Zeros of \(\zeta\) are poles of \(1/\zeta\); Titchmarsh, Ch. 14.

---

### 26. Lindelöf-type growth for \(1/\zeta(s)\)

**Statement.** RH is equivalent to the assertion that for every fixed \(\delta>0\) and every \(\varepsilon>0\),

\[
\frac1{\zeta(\sigma+it)}=O_{\delta,\varepsilon}(|t|^\varepsilon)
\qquad(\sigma\ge 1/2+\delta,\ |t|\ge 2).
\]

**Growth/rate.** \(O_\varepsilon(|t|^\varepsilon)\) uniformly in \(\sigma\ge 1/2+\delta\).  
**Documentation.**  
- Titchmarsh: <https://doi.org/10.1093/oso/9780198533696.001.0001>  
**Foundational proof/citations.** Under RH, zero-free half-plane plus Littlewood-type bounds; conversely, a pole at a zero \(\rho\) with \(\Re\rho>1/2\) would violate such a bound.

---

### 27. Holomorphy of \(\zeta'(s)/\zeta(s)\) for \(\Re(s)>1/2\)

**Statement.** RH is equivalent to the logarithmic derivative

\[
\frac{\zeta'(s)}{\zeta(s)}
\]

being holomorphic in \(\Re(s)>1/2\).  
**Growth/rate.** No poles to the right of the critical line.  
**Documentation.**  
- Riemann zeta function: <https://en.wikipedia.org/wiki/Riemann_zeta_function>  
**Foundational proof/citations.** Zeros of \(\zeta\) are poles of \(\zeta'/\zeta\); explicit formula proofs use this directly.

---

### 28. Lindelöf-type growth for \(\zeta'(s)/\zeta(s)\)

**Statement.** RH is equivalent to the assertion that for every fixed \(\delta>0\) and every \(\varepsilon>0\),

\[
\frac{\zeta'(\sigma+it)}{\zeta(\sigma+it)}
=
O_{\delta,\varepsilon}(|t|^\varepsilon)
\qquad(\sigma\ge 1/2+\delta,\ |t|\ge 2).
\]

**Growth/rate.** \(O_\varepsilon(|t|^\varepsilon)\).  
**Documentation.**  
- Titchmarsh: <https://doi.org/10.1093/oso/9780198533696.001.0001>  
**Foundational proof/citations.** Littlewood-type conditional bounds; poles of \(\zeta'/\zeta\) correspond to zeros of \(\zeta\).

---

### 29. Analytic branch of \(\log\zeta(s)\) for \(\Re(s)>1/2\)

**Statement.** RH is equivalent to the existence of a single-valued analytic branch of \(\log\zeta(s)\) in the half-plane \(\Re(s)>1/2\).  
**Growth/rate.** Zero-free half-plane.  
**Documentation.**  
- Riemann zeta function: <https://en.wikipedia.org/wiki/Riemann_zeta_function>  
**Foundational proof/citations.** A holomorphic logarithm exists on a simply connected domain iff the function has no zeros there.

---

### 30. Liouville summatory function

**Statement.** RH is equivalent to

\[
L(x)=\sum_{n\le x}\lambda(n)
=
O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Liouville function: <https://en.wikipedia.org/wiki/Liouville_function>  
**Foundational proof/citations.** Dirichlet series \(\sum \lambda(n)n^{-s}=\zeta(2s)/\zeta(s)\); poles occur at zeros of \(\zeta(s)\). Perron contour shifting; Titchmarsh.

---

### 31. Weighted Liouville sum \(\sum \lambda(n)/n\)

**Statement.** RH is equivalent to

\[
\sum_{n\le x}\frac{\lambda(n)}{n}
=
O_\varepsilon\!\left(x^{-1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{-1/2+\varepsilon})\).  
**Documentation.**  
- Liouville function: <https://en.wikipedia.org/wiki/Liouville_function>  
**Foundational proof/citations.** Partial summation from \(L(x)\).

---

### 32. Convergence of the Liouville Dirichlet series for \(\Re(s)>1/2\)

**Statement.** RH is equivalent to convergence of

\[
\sum_{n=1}^\infty \frac{\lambda(n)}{n^s}
\]

for every \(\Re(s)>1/2\).  
**Growth/rate.** Abscissa of convergence \(\le 1/2\).  
**Documentation.**  
- Liouville function: <https://en.wikipedia.org/wiki/Liouville_function>  
**Foundational proof/citations.** Since the series equals \(\zeta(2s)/\zeta(s)\) for \(\Re(s)>1\), zeros of \(\zeta(s)\) are possible singularities.

---

# D. Square-free, \(k\)-free, and weighted summatory-function equivalences

### 33. Square-free counting function

**Statement.** RH is equivalent to

\[
Q(x)=\sum_{n\le x}\mu^2(n)
=
\frac{x}{\zeta(2)}+O_\varepsilon\!\left(x^{1/4+\varepsilon}\right).
\]

**Growth/rate.** Error \(O_\varepsilon(x^{1/4+\varepsilon})\).  
**Documentation.**  
- Square-free integer: <https://en.wikipedia.org/wiki/Square-free_integer>  
**Foundational proof/citations.** Dirichlet series \(\sum \mu^2(n)n^{-s}=\zeta(s)/\zeta(2s)\). Poles from zeros of \(\zeta(2s)\) occur at \(s=\rho/2\); RH puts them on \(\Re(s)=1/4\).

---

### 34. \(k\)-free counting functions

**Statement.** For every fixed integer \(k\ge2\), RH is equivalent to

\[
Q_k(x)
=
\#\{n\le x: n \text{ is }k\text{-free}\}
=
\frac{x}{\zeta(k)}+O_\varepsilon\!\left(x^{1/(2k)+\varepsilon}\right).
\]

**Growth/rate.** Error \(O_\varepsilon(x^{1/(2k)+\varepsilon})\).  
**Documentation.**  
- Square-free integer and generalizations: <https://en.wikipedia.org/wiki/Square-free_integer>  
**Foundational proof/citations.** Dirichlet series \(\zeta(s)/\zeta(ks)\); poles from zeros occur at \(s=\rho/k\).

---

### 35. Power-weighted Möbius sums

**Statement.** For every fixed integer \(m\ge0\), RH is equivalent to

\[
\sum_{n\le x}\mu(n)n^m
=
O_\varepsilon\!\left(x^{m+1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{m+1/2+\varepsilon})\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** Dirichlet series \(\sum \mu(n)n^m n^{-s}=1/\zeta(s-m)\); zeros shift to \(s=m+\rho\).

---

### 36. Power-weighted Liouville sums

**Statement.** For every fixed integer \(m\ge0\), RH is equivalent to

\[
\sum_{n\le x}\lambda(n)n^m
=
O_\varepsilon\!\left(x^{m+1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{m+1/2+\varepsilon})\).  
**Documentation.**  
- Liouville function: <https://en.wikipedia.org/wiki/Liouville_function>  
**Foundational proof/citations.** Dirichlet series \(\zeta(2(s-m))/\zeta(s-m)\); poles from zeros of \(\zeta(s-m)\).

---

### 37. Power-weighted square-free counting

**Statement.** For every fixed integer \(m\ge0\), RH is equivalent to

\[
\sum_{n\le x}\mu^2(n)n^m
=
\frac{x^{m+1}}{(m+1)\zeta(2)}
+
O_\varepsilon\!\left(x^{m+1/4+\varepsilon}\right).
\]

**Growth/rate.** Error \(O_\varepsilon(x^{m+1/4+\varepsilon})\).  
**Documentation.**  
- Square-free integer: <https://en.wikipedia.org/wiki/Square-free_integer>  
**Foundational proof/citations.** Dirichlet series \(\zeta(s-m)/\zeta(2(s-m))\); zeros contribute at \(s=m+\rho/2\).

---

# E. Divisor-sum, harmonic-number, and totient inequality criteria

### 38. Robin’s inequality

**Statement.** RH is equivalent to

\[
\sigma(n)<e^\gamma n\log\log n
\qquad\text{for every integer }n\ge5041.
\]

**Growth/rate.** Maximal order of \(\sigma(n)\) bounded by \(e^\gamma n\log\log n\) beyond 5040.  
**Documentation.**  
- Robin’s theorem: <https://en.wikipedia.org/wiki/Robin%27s_theorem>  
- Robin (1984), Numdam: <https://www.numdam.org/item/JMPA_1984__63_2_187_0/>  
**Foundational proof/citations.** G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*, J. Math. Pures Appl. 63 (1984), 187–213.

---

### 39. Robin’s inequality reduced to extremal integers

**Statement.** RH is equivalent to Robin’s inequality holding for all sufficiently large superabundant (or, in standard refinements, colossally abundant) integers. In particular, if a counterexample exists, there is an extremal counterexample of this type.  
**Growth/rate.** Same inequality as item 38, but only checked on extremal \(n\).  
**Documentation.**  
- Superabundant number: <https://en.wikipedia.org/wiki/Superabundant_number>  
- Robin (1984): <https://www.numdam.org/item/JMPA_1984__63_2_187_0/>  
**Foundational proof/citations.** Robin (1984), using extremal properties from Alaoglu–Erdős.

---

### 40. Lagarias’s harmonic-number criterion

**Statement.** RH is equivalent to

\[
\sigma(n)\le H_n+\exp(H_n)\log H_n
\qquad(n\ge1),
\]

where \(H_n=\sum_{k=1}^n 1/k\).  
**Growth/rate.** Explicit elementary inequality for every \(n\).  
**Documentation.**  
- Lagarias, “An elementary criterion for the Riemann hypothesis”: <https://arxiv.org/abs/math/0008177>  
**Foundational proof/citations.** J. C. Lagarias, 2002; related to Robin’s theorem via harmonic-number asymptotics.

---

### 41. Nicolas’s primorial totient criterion

**Statement.** Let \(N_k=\prod_{j=1}^k p_j\) be the \(k\)-th primorial. RH is equivalent to

\[
\frac{N_k}{\varphi(N_k)}
>
e^\gamma \log\log N_k
\qquad\text{for all }k\ge1.
\]

**Growth/rate.** Inequality comparing \(\prod_{p\le p_k}(1-1/p)^{-1}\) with \(e^\gamma\log\log N_k\).  
**Documentation.**  
- Nicolas, *Petites valeurs de la fonction de Jordan*, JTNB 2008: <https://jtnb.cedram.org/item/?id=JTNB_2008__20_2_407_0>  
**Foundational proof/citations.** J.-L. Nicolas (2008); connects RH to Mertens-product/Chebyshev-function oscillations.

---

# F. Farey sequences, Riesz-type transforms, derivative criteria, and abscissae

### 42. Franel–Landau Farey-sequence discrepancy, absolute value

**Statement.** Let \(F_n\) be the Farey sequence of order \(n\), with length \(A_n=|F_n|\), and terms \(r_k\). RH is equivalent to

\[
\sum_{k=1}^{A_n}\left|r_k-\frac{k}{A_n}\right|
=
O_\varepsilon\!\left(n^{-1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(n^{-1/2+\varepsilon})\).  
**Documentation.**  
- Farey sequence: <https://en.wikipedia.org/wiki/Farey_sequence>  
**Foundational proof/citations.** Franel (1924), Landau (1924); discrepancy is tied to Mertens-function estimates and hence zeros of \(\zeta\).

---

### 43. Landau’s quadratic Farey-sequence discrepancy

**Statement.** With notation as above, RH is equivalent to

\[
\sum_{k=1}^{A_n}\left(r_k-\frac{k}{A_n}\right)^2
=
O_\varepsilon\!\left(n^{-2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(n^{-2+\varepsilon})\).  
**Documentation.**  
- Farey sequence: <https://en.wikipedia.org/wiki/Farey_sequence>  
**Foundational proof/citations.** Landau (1924); equivalent through the same Mertens-function/zero connection.

---

### 44. Riesz function criterion

**Statement.** Define the Riesz function

\[
R(x)=\sum_{n=1}^\infty
\frac{(-1)^{n+1}x^n}{(n-1)!\,\zeta(2n)}.
\]

RH is equivalent to

\[
R(x)=O_\varepsilon\!\left(x^{1/4+\varepsilon}\right)
\qquad(x\to\infty).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/4+\varepsilon})\).  
**Documentation.**  
- MathWorld, Riesz function: <https://mathworld.wolfram.com/RieszFunction.html>  
**Foundational proof/citations.** M. Riesz (1918); see Titchmarsh for the contour-integral proof linking poles to zeros of \(\zeta\).

---

### 45. Speiser’s derivative criterion

**Statement.** RH is equivalent to the assertion that \(\zeta'(s)\) has no zeros in the left half of the critical strip:

\[
0<\Re(s)<\frac12.
\]

**Growth/rate.** Zero-location criterion for \(\zeta'(s)\).  
**Documentation.**  
- MathWorld, Riemann Hypothesis: <https://mathworld.wolfram.com/RiemannHypothesis.html>  
**Foundational proof/citations.** Speiser (1934/1935); see Titchmarsh for the equivalence.

---

### 46. Abscissa of convergence of the Möbius Dirichlet series

**Statement.** RH is equivalent to

\[
\sigma_c\left(\sum_{n=1}^\infty \frac{\mu(n)}{n^s}\right)=\frac12,
\]

where \(\sigma_c\) is the abscissa of ordinary convergence.  
**Growth/rate.** Abscissa exactly \(1/2\).  
**Documentation.**  
- Dirichlet series: <https://en.wikipedia.org/wiki/Dirichlet_series>  
**Foundational proof/citations.** Littlewood’s equivalence; Davenport, Titchmarsh.

---

### 47. Abscissa of convergence of the Liouville Dirichlet series

**Statement.** RH is equivalent to

\[
\sigma_c\left(\sum_{n=1}^\infty \frac{\lambda(n)}{n^s}\right)=\frac12.
\]

**Growth/rate.** Abscissa exactly \(1/2\).  
**Documentation.**  
- Liouville function: <https://en.wikipedia.org/wiki/Liouville_function>  
**Foundational proof/citations.** Same Perron/Dirichlet-series argument using \(\zeta(2s)/\zeta(s)\).

---

### 48. Analytic continuation of the square-free Dirichlet series

**Statement.** RH is equivalent to the meromorphic continuation of

\[
\frac{\zeta(s)}{\zeta(2s)}
\]

to \(\Re(s)>1/4\) with no poles there except the simple pole at \(s=1\).  
**Growth/rate.** Pole-free region \(\Re(s)>1/4\) except \(s=1\).  
**Documentation.**  
- Square-free integer: <https://en.wikipedia.org/wiki/Square-free_integer>  
**Foundational proof/citations.** Poles from zeros of \(\zeta(2s)\) occur at \(s=\rho/2\).

---

### 49. Analytic continuation of the \(k\)-free Dirichlet series

**Statement.** For fixed \(k\ge2\), RH is equivalent to meromorphic continuation of

\[
\frac{\zeta(s)}{\zeta(ks)}
\]

to \(\Re(s)>1/(2k)\) with no poles there except \(s=1\).  
**Growth/rate.** Pole-free region \(\Re(s)>1/(2k)\) except \(s=1\).  
**Documentation.**  
- Square-free integer and generalizations: <https://en.wikipedia.org/wiki/Square-free_integer>  
**Foundational proof/citations.** Poles from zeros occur at \(s=\rho/k\).

---

### 50. Mellin transform of the Mertens function

**Statement.** For \(\Re(s)>1\),

\[
s\int_1^\infty M(x)x^{-s-1}\,dx=\frac1{\zeta(s)}.
\]

RH is equivalent to the analytic continuation of this Mellin transform to \(\Re(s)>1/2\).  
**Growth/rate.** Analytic continuation threshold \(\Re(s)>1/2\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** Perron/Mellin inversion; zeros of \(\zeta\) become poles of \(1/\zeta\).

---

### 51. Mellin transform of the Liouville summatory function

**Statement.** For \(\Re(s)>1\),

\[
s\int_1^\infty L(x)x^{-s-1}\,dx=\frac{\zeta(2s)}{\zeta(s)}.
\]

RH is equivalent to analytic continuation of this transform to \(\Re(s)>1/2\), apart from expected harmless singularities.  
**Growth/rate.** Analytic continuation threshold \(\Re(s)>1/2\).  
**Documentation.**  
- Liouville function: <https://en.wikipedia.org/wiki/Liouville_function>  
**Foundational proof/citations.** Poles from zeros of \(\zeta(s)\) in the denominator.

---

### 52. General power-weighted Möbius partial sums

**Statement.** For every fixed \(0\le \alpha<1\), RH is equivalent to

\[
\sum_{n\le x}\frac{\mu(n)}{n^\alpha}
=
O_\varepsilon\!\left(x^{1/2-\alpha+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2-\alpha+\varepsilon})\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** Partial summation from \(M(x)\); conversely one recovers \(M(x)\).

---

### 53. Logarithmically weighted Möbius sum

**Statement.** RH is equivalent to

\[
\sum_{n\le x}\mu(n)\log\frac{x}{n}
=
O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** This is essentially the inverse Mellin transform of \(1/(s\zeta(s))\); zeros of \(\zeta\) give \(x^\rho\) contributions.

---

### 54. Möbius sum weighted by \(\log n\)

**Statement.** RH is equivalent to

\[
\sum_{n\le x}\mu(n)\log n
=
O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).
\]

**Growth/rate.** \(O_\varepsilon(x^{1/2+\varepsilon})\).  
**Documentation.**  
- Mertens function: <https://en.wikipedia.org/wiki/Mertens_function>  
**Foundational proof/citations.** Dirichlet series is \(-\frac{d}{ds}(1/\zeta(s))=\zeta'(s)/\zeta(s)^2\); zeros of \(\zeta\) produce poles.

---

### 55. Riesz means of the Möbius function

**Statement.** For fixed \(\kappa>0\), let

\[
R_\kappa(x)=\sum_{n\le x}\mu(n)\left(1-\frac{n}{x}\right)^\kappa.
\]

RH is equivalent to

\[
R_\kappa(x)=O_\varepsilon\!\left(x^{1/2-\kappa+\varepsilon}\right).
\]

In particular, for \(\kappa>1/2\), RH is equivalent to \(R_\kappa(x)\to0\).  
**Growth/rate.** \(O_\varepsilon(x^{1/2-\kappa+\varepsilon})\).  
**Documentation.**  
- Riesz mean: <https://en.wikipedia.org/wiki/Riesz_mean>  
**Foundational proof/citations.** Typical-mean theorem and Mellin transform of \(1/\zeta(s)\); Titchmarsh, Davenport.

---

# Requested Lindelöf hypothesis entry

### L. Classical Lindelöf hypothesis

**Statement.** The Lindelöf hypothesis is

\[
\zeta(1/2+it)=O_\varepsilon(|t|^\varepsilon)
\qquad(|t|\to\infty).
\]

**Growth/rate.** \(O_\varepsilon(|t|^\varepsilon)\) on the critical line.  
**Logical status.**  
- RH implies Lindelöf.  
- Lindelöf does **not** currently imply RH, and equivalence is not known.  
**Documentation.**  
- Lindelöf hypothesis: <https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis>  
**Foundational proof/citations.** Lindelöf (1908); standard treatment in Titchmarsh and Ivić.  
**Equivalent Lindelöf-type formulations.** See items **26** and **28**, which are genuinely equivalent to RH because they involve growth of \(1/\zeta(s)\) or \(\zeta'(s)/\zeta(s)\) in the zero-free half-plane, where poles would occur at zeros of \(\zeta\).

---

# Selected foundational papers and books

Below are primary or standard secondary sources for the main proof mechanisms.

## Explicit formulas and zero equivalences

- von Mangoldt explicit formula:  
  <https://en.wikipedia.org/wiki/Explicit_formula>
- Titchmarsh, *The Theory of the Riemann Zeta-Function*:  
  <https://doi.org/10.1093/oso/9780198533696.001.0001>
- Davenport, *Multiplicative Number Theory*:  
  <https://doi.org/10.1007/978-1-4757-5927-3>
- Edwards, *Riemann’s Zeta Function*:  
  <https://store.doverpublications.com/0486438139.html>

## Prime-counting bounds

- Schoenfeld, “Sharper bounds for the Chebyshev function \(\theta(x)\)”:  
  <https://doi.org/10.1090/S0025-5718-1976-0457395-6>

## Mertens/Möbius/Liouville equivalences

- Mertens function overview:  
  <https://en.wikipedia.org/wiki/Mertens_function>
- Liouville function overview:  
  <https://en.wikipedia.org/wiki/Liouville_function>
- Davenport, Ch. 18; Titchmarsh, Ch. 14.

## Robin, Lagarias, Nicolas

- Robin (1984), Numdam:  
  <https://www.numdam.org/item/JMPA_1984__63_2_187_0/>
- Robin’s theorem overview:  
  <https://en.wikipedia.org/wiki/Robin%27s_theorem>
- Lagarias (2002):  
  <https://arxiv.org/abs/math/0008177>
- Nicolas (2008), JTNB:  
  <https://jtnb.cedram.org/item/?id=JTNB_2008__20_2_407_0>

## Li coefficients, positivity, Nyman–Beurling

- Li (1997):  
  <https://doi.org/10.1006/jnth.1997.2131>
- Li’s criterion overview:  
  <https://en.wikipedia.org/wiki/Li%27s_criterion>
- Bombieri–Lagarias:  
  <https://arxiv.org/abs/math/9902059>
- Báez-Duarte:  
  <https://arxiv.org/abs/math/0302094>
- Nyman–Beurling theorem overview:  
  <https://en.wikipedia.org/wiki/Nyman%E2%80%93Beurling_theorem>

## de Bruijn–Newman and Jensen polynomials

- de Bruijn–Newman constant overview:  
  <https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant>
- Rodgers–Tao:  
  <https://arxiv.org/abs/1801.05914>
- Jensen polynomials overview:  
  <https://en.wikipedia.org/wiki/Jensen_polynomial>
- Griffin–Ono–Rolen–Runkel:  
  <https://arxiv.org/abs/1901.01160>

## Riesz and Farey criteria

- MathWorld, Riesz function:  
  <https://mathworld.wolfram.com/RieszFunction.html>
- Farey sequence and Franel–Landau criteria:  
  <https://en.wikipedia.org/wiki/Farey_sequence>

## Lindelöf

- Lindelöf hypothesis overview:  
  <https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis>

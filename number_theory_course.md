
For a rigorous route into number theory, I recommend making **Keith Conrad’s Berkeley Math 115 lectures** your primary elementary course, supplementing them with a problem-centered series, then branching deliberately into algebraic or analytic number theory. Berkeley’s course is explicitly an undergraduate introduction emphasizing primes and Diophantine equations and uses Niven–Zuckerman–Montgomery as its text. [youtube](https://www.youtube.com/watch?v=EzE6it9kAsI)

Because you already lean toward algebraic number theory, \(p\)-adics, partition congruences, and proof-oriented work, the goal should not be “watch all number theory videos.” Build an elementary foundation that supports the advanced branches you actually want.

## Best YouTube series

| Purpose | Series | Best use |
|---|---|---|
| Main rigorous elementary course | **Keith Conrad — Berkeley Math 115: Introduction to Number Theory** | Best overall spine. It starts with a map of primes and Diophantine equations, then develops core material such as divisibility and Euclid’s algorithm in a university-course format. It follows *An Introduction to the Theory of Numbers* by Niven, Zuckerman, and Montgomery.  [youtube](https://www.youtube.com/watch?v=EzE6it9kAsI) |
| Proof-oriented beginner-to-intermediate path | **Introduction to Number Theory — series based on Underwood Dudley** | Good for slower, explicit proof exposition. The opening lecture begins from divisibility and proves a foundational lemma, presenting the material as both elementary number theory and an introduction to mathematical proof.  [youtube](https://www.youtube.com/watch?v=TFqf4FbjK5k) |
| Structured elementary syllabus with exercises | **First Course in Number Theory — Zac Caffeine Machine** | A promising ordered course that recommends Burton’s *Elementary Number Theory*, and explicitly assumes familiarity with mathematical notation and terminology. Use it for a second presentation of foundational material or targeted review.  [youtube](https://www.youtube.com/watch?v=Av2LR82-vXE) |
| Fast global map / review | **Number Theory for Beginners — Full Course** | Useful as a survey or checklist: it includes Euclid’s algorithm, Diophantine equations, congruences, CRT, \(\varphi\), multiplicative functions, Möbius inversion, primitive roots, quadratic reciprocity, sums of squares, and introductory divisor/circle problems. Its compressed format makes it unsuitable as the sole proof course.  [youtube](https://www.youtube.com/watch?v=rW9yyqxZzms) |
| Advanced analytic number theory | **Alex Kontorovich — Rutgers Math 572: Analytic Number Theory** | Strong next-stage course if you want Euler products, \(\zeta(s)\), reciprocal-prime sums, functional-equation ideas, and Poisson summation. The first lecture provides accompanying lecture notes and a course site.  [youtube](https://www.youtube.com/watch?v=2qTz6gJIJvk) |
| Undergraduate analytic transition | **Oxford Mathematics — Analytic Number Theory** | Good bridge into Dirichlet series and the Riemann zeta function, framed as part of a fourth-year undergraduate course; the playlist includes lectures from James Maynard’s course.  [youtube](https://www.youtube.com/watch?v=T7aqj1r7CsA) |
| Supplementary elementary lecture library | **N. K. Vishnu — Elementary Number Theory lectures** | A broad undergraduate sequence based on Thomas Koshy, covering division, gcd/lcm, Bézout, primes, the fundamental theorem of arithmetic, pigeonhole principle, and linear Diophantine equations.  [nkvishnu.wordpress](https://nkvishnu.wordpress.com/video-lectures/) |

## Recommended learning route

### Phase 1: Arithmetic foundations

Use the Berkeley course as the main series, and solve problems from a textbook immediately after each unit.

1. **Divisibility and Euclidean domains**
   - Division algorithm.
   - GCD, extended Euclidean algorithm, Bézout identity.
   - Linear Diophantine equations.
   - Unique factorization in \(\mathbb Z\).

2. **Congruences**
   - Congruence as an equivalence relation.
   - Arithmetic modulo \(n\).
   - Linear congruences.
   - Chinese remainder theorem.
   - Multiplicative inverses modulo \(n\).

3. **Finite multiplicative structure**
   - Euler’s totient function.
   - Fermat’s little theorem and Euler’s theorem.
   - Multiplicative order.
   - Primitive roots.
   - Carmichael function as an optional extension.
   - RSA as an application, but prove the group-theoretic facts rather than treating it as a cryptography recipe.

**Target capability:** You should be able to derive and use
\[
ax \equiv b \pmod n
\]
by reducing it through \(\gcd(a,n)\), and explain precisely when solutions exist and how many distinct solutions occur modulo \(n\).

### Phase 2: Classical elementary number theory

This is the core material that turns modular arithmetic into number theory.

1. **Arithmetic functions**
   - \(\tau(n)\), \(\sigma(n)\), \(\varphi(n)\), \(\mu(n)\), \(\Lambda(n)\).
   - Multiplicative and completely multiplicative functions.
   - Dirichlet convolution.
   - Möbius inversion.

2. **Quadratic residues**
   - Euler’s criterion.
   - Legendre and Jacobi symbols.
   - Gauss’s lemma.
   - Quadratic reciprocity.
   - Supplementary laws for \(\left(\frac{-1}{p}\right)\) and \(\left(\frac{2}{p}\right)\).

3. **Diophantine equations**
   - Pythagorean triples.
   - Sums of two squares.
   - Pell equations and continued fractions.
   - Descent methods.
   - Local obstructions: understand why solvability modulo every \(m\) is necessary but not always sufficient for integer or rational solvability.

4. **Prime distribution**
   - Euclid’s proof of infinitely many primes.
   - Chebyshev functions and elementary estimates.
   - Introduction to \(\pi(x)\), \(\theta(x)\), and \(\psi(x)\).
   - Statement and consequences of the prime number theorem.
   - Dirichlet’s theorem on primes in arithmetic progressions: know the statement early; prove it after analytic prerequisites.

The full-course survey is especially useful as a topic checklist here: it explicitly traverses congruences, CRT, \(\varphi\), multiplicative functions, Möbius inversion, primitive roots, quadratic reciprocity, sums of squares, and introductory analytic problems. [youtube](https://www.youtube.com/watch?v=rW9yyqxZzms)

### Phase 3: Algebraic number theory

For your interests, this should be the first major specialization after a solid elementary course.

1. **Algebra prerequisites**
   - Groups, rings, ideals, quotient rings.
   - Fields and field extensions.
   - Polynomial factorization.
   - Galois theory at least through finite Galois extensions.
   - Tensor products and modules can wait until later, but eventually become helpful.

2. **Quadratic number fields**
   - \(\mathbb Q(\sqrt d)\), rings of integers, discriminants.
   - Norm and trace.
   - Units and Pell-type equations.
   - Prime factorization in \(\mathcal O_K\).
   - Examples of failure of unique factorization, such as in \(\mathbb Z[\sqrt{-5}]\).

3. **Ideals and class groups**
   - Dedekind domains.
   - Unique factorization of nonzero ideals.
   - Fractional ideals.
   - Ideal class group and class number.
   - Minkowski’s bound and concrete class-group computations.

4. **Local methods**
   - \(p\)-adic valuations.
   - Completion of \(\mathbb Q\) to \(\mathbb Q_p\).
   - Hensel’s lemma.
   - Local-global principles, including where they succeed and fail.
   - Ramification, residue degree, splitting of primes.

**Suggested texts:** Marcus, *Number Fields*, for an approachable first pass; Neukirch, *Algebraic Number Theory*, for a deeper reference; and Milne’s freely available course notes for a rigorous, concise route. A current overview video also identifies Milne’s notes and Gouvêa’s \(p\)-adic text as resources, but use the primary texts themselves rather than relying on that overview. [youtube](https://www.youtube.com/watch?v=Aa-SDGeeQE8)

### Phase 4: Analytic number theory

Take this after Phase 2 and basic complex analysis. Kontorovich’s course is the best of the listed options for a serious transition. [youtube](https://www.youtube.com/watch?v=2qTz6gJIJvk)

1. **Complex-analysis prerequisites**
   - Holomorphic functions, contour integration, residues.
   - Uniform convergence of series.
   - Gamma function and Mellin transforms.
   - Fourier analysis and Poisson summation, at least at an introductory level.

2. **Dirichlet series**
   - Absolute convergence and Euler products.
   - Riemann zeta function.
   - \(-\zeta'(s)/\zeta(s)\) and the von Mangoldt function.
   - Dirichlet \(L\)-functions and characters.
   - Analytic continuation and functional equations.

3. **Primes**
   - Nonvanishing of \(\zeta(s)\) on \(\operatorname{Re}(s)=1\).
   - Prime number theorem.
   - Primes in arithmetic progressions.
   - Explicit formulas and zero-free regions.
   - Zero-density estimates and sieve methods later.

Oxford’s material is a useful conceptual bridge because it begins with Dirichlet series and the zeta function; its playlist samples a fourth-year undergraduate course associated with James Maynard. [youtube](https://www.youtube.com/watch?v=T7aqj1r7CsA)

### Phase 5: Modular forms and arithmetic geometry

This is the natural long-term route if you want Ramanujan congruences and modern Diophantine theory.

1. **Modular forms**
   - Modular group action on the upper half-plane.
   - Modular forms and cusp forms.
   - Fourier \(q\)-expansions.
   - Eisenstein series, \(\Delta(q)\), and the Ramanujan \(\tau\)-function.
   - Hecke operators and eigenforms.
   - \(L\)-functions attached to modular forms.

2. **Partitions**
   - Euler’s generating function
     \[
     \sum_{n\ge0}p(n)q^n
       =\prod_{m\ge1}\frac{1}{1-q^m}.
     \]
   - Euler’s pentagonal number theorem.
   - Ramanujan congruences:
     \[
     p(5n+4)\equiv0\pmod5,\qquad
     p(7n+5)\equiv0\pmod7,\qquad
     p(11n+6)\equiv0\pmod{11}.
     \]
   - \(q\)-series identities, eta-products, and modular-form proofs.
   - Hecke operators and congruences in Fourier coefficients.

3. **Elliptic curves**
   - Elliptic curves over \(\mathbb Q\) and finite fields.
   - Rational points and the group law.
   - Reduction modulo primes.
   - Mordell–Weil theorem.
   - Local points, Selmer groups, descent.
   - The modularity theorem and the connection to Fermat’s Last Theorem.

## A 24-week syllabus

| Weeks | Focus | Core outputs |
|---|---|---|
| 1–2 | Divisibility, gcd, Bézout, Euclidean algorithm | Implement extended gcd; solve linear Diophantine equations; prove Bézout’s identity |
| 3–4 | Primes and unique factorization | Prove Euclid’s lemma and FTA; investigate valuations \(v_p(n)\) |
| 5–6 | Congruences and CRT | Solve simultaneous congruences; derive modular inverses and CRT constructively |
| 7–8 | Fermat/Euler, orders, primitive roots | Compute orders; classify primitive roots for small moduli; prove Euler’s theorem |
| 9–10 | Arithmetic functions | Establish multiplicativity; use Dirichlet convolution and Möbius inversion |
| 11–13 | Quadratic residues and reciprocity | Compute Legendre symbols efficiently; prove quadratic reciprocity |
| 14–15 | Diophantine equations | Parameterize Pythagorean triples; solve Pell equations with continued fractions |
| 16–17 | Sums of squares and Gaussian integers | Use \(\mathbb Z[i]\), norms, and factorization to characterize sums of two squares |
| 18–19 | Prime distribution and zeta preview | Derive Euler products; understand why \(\sum_p 1/p\) diverges |
| 20–21 | \(p\)-adic integers and Hensel lifting | Perform Hensel lifts; analyze simple polynomial roots in \(\mathbb Z_p\) |
| 22–24 | Chosen capstone | Complete one proof or computational research project |

## Recommended texts and practice

Use **one** primary text, not five in parallel.

| Level | Recommended text | Role |
|---|---|---|
| Elementary, accessible | Burton, *Elementary Number Theory* | Plenty of examples and exercises; aligns with several video-course syllabi.  [youtube](https://www.youtube.com/watch?v=Av2LR82-vXE) |
| Rigorous classical foundation | Niven, Zuckerman & Montgomery, *An Introduction to the Theory of Numbers* | Best match for the Berkeley lecture course.  [youtube](https://www.youtube.com/watch?v=pVKhDtOjji8) |
| Deeper elementary/classical | Hardy & Wright, *An Introduction to the Theory of Numbers* | Landmark text; rewarding after an initial course, but terse in places |
| Computational exploration | William Stein, *Elementary Number Theory* | Ideal if you want Sage/Python experiments alongside proofs |
| Algebraic number theory | Marcus, *Number Fields* → Neukirch | Friendly first step, then reference-level depth |
| Analytic number theory | Apostol, *Introduction to Analytic Number Theory* → Iwaniec & Kowalski | Strong first text followed by a demanding reference |
| Modular forms | Diamond & Shurman, *A First Course in Modular Forms* | A standard path toward \(q\)-series, modular forms, and arithmetic applications |

## Study method for your goals

Treat video as a **lecture layer**, with formal work occurring elsewhere:

- Watch one or two lectures per week, not an entire playlist at once.
- Write definitions in a “proof dependency” notebook: state every theorem, its hypotheses, and which earlier results its proof needs.
- Solve 8–15 problems per topic, including at least two proof problems and one computation or implementation task.
- Use SageMath, PARI/GP, or Python/SymPy to generate conjectures, but verify claims by proof. For example, test quadratic reciprocity for primes below 1,000, then prove it independently.
- Formalize selected foundational results in Lean or Coq: Euclid’s algorithm correctness, the CRT, multiplicativity of \(\varphi\), or a restricted form of Hensel’s lemma. This meshes well with your interest in automated conjecturing and proof systems.
- Build toward one capstone rather than merely completing lectures.

A good first capstone for you would be: **derive and computationally verify Ramanujan’s partition congruences for a substantial range, then study a modular-form or \(q\)-series proof of the \(p(5n+4)\equiv0\pmod5\) congruence.** This connects elementary congruences, generating functions, formalization, computation, and your stated interest in partition identities.

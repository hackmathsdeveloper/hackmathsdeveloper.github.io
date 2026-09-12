
For algebraic geometry, the most effective route is: **build commutative algebra and classical varieties first; then learn schemes, sheaves, and cohomology; finally specialize into arithmetic geometry, moduli, birational geometry, or computational geometry.** For a rigorous video spine, use **Richard Borcherds’ Algebraic Geometry I: Varieties** followed by his **Schemes** course, and use the current ETH Zürich course for a more modern, carefully staged parallel treatment. [bilibili](https://www.bilibili.com/video/BV1y1zXY8EiB/)

Since you are interested in number theory, \(p\)-adic methods, polynomial algebra, and geometric intuition for Jacobians, I would prioritize the route **affine/projective varieties \(\to\) schemes \(\to\) curves and divisors \(\to\) cohomology \(\to\) arithmetic geometry** rather than approaching the field chiefly through high-dimensional classification or physics.

## Best YouTube series

| Purpose | Series / resource | Why it is useful |
|---|---|---|
| Main first serious course | **Richard Borcherds — Algebraic Geometry I: Varieties** | A substantial graduate-level course that broadly follows Hartshorne Chapter I. Its 51 videos cover affine varieties, projective varieties, morphisms, rational maps, nonsingular varieties and curves, and intersections. The reported total duration is about 1,026 minutes, so it works well as a semester-long primary course.  [bilibili](https://www.bilibili.com/video/BV1y1zXY8EiB/) |
| Main scheme-theory sequel | **Richard Borcherds — Schemes / Algebraic Geometry II** | A natural continuation after varieties, loosely following Hartshorne Chapter II. It introduces sheaves, schemes, fiber products, and more; individual lectures include the relation among abstract, projective, and complete varieties and group schemes.  [youtube](https://www.youtube.com/watch?v=BX3jiLdehA4) |
| Modern, well-sequenced full course | **ETH Zürich — Algebraic Geometry (Andreas Gathmann-aligned)** | A particularly strong course architecture: affine varieties, abstract varieties as ringed spaces, projective varieties and Grassmannians, birational maps, schemes, quasi-coherent sheaves, differentials, and sheaf cohomology. Its short weekly videos—typically 10–20 minutes—are paired with notes and fit independent study very well.  [metaphor.ethz](https://metaphor.ethz.ch/x/2026/fs/401-3146-12L/) |
| Hartshorne companion / visual study guide | **An Introduction to Algebraic Geometry — Hartshorne Chapter I walkthrough** | Useful alongside a text, especially for the first pass through affine varieties. Its opening lesson explicitly covers zero loci, the Zariski topology, ideals versus zero sets, Noetherian spaces, and elementary dimension concepts.  [youtube](https://www.youtube.com/watch?v=OuRDWPHjahg) |
| Schemes intuition and broad survey | **Daniel Tubbenhauer — “What are… schemes?” and algebraic-geometry course** | Helpful when \(\operatorname{Spec} A\), prime ideals, and gluing feel opaque. The course explicitly ranges from classical varieties to schemes and tropical varieties, and supplies slides and exercises.  [youtube](https://www.youtube.com/watch?v=u0IzqT5GefY) |
| First special-topic branch: toric geometry | **Jürgen Hausen — Toric Varieties** | Excellent after basic schemes because toric varieties turn many abstract notions into combinatorics of lattices, cones, fans, and polytopes. The course provides notes and exercises and assumes basic algebraic geometry.  [sites.google](https://sites.google.com/view/eniskaya/math-videos) |
| Broad index of specialist lectures | **Enis Kaya’s mathematics-video collection** | Useful after the foundation phase for curated advanced topics—rational surfaces, arithmetic geometry, tropicalization, and toric schemes—rather than as a first course.  [sites.google](https://sites.google.com/view/eniskaya/math-videos) |

## Recommended starting stack

Do not attempt Hartshorne linearly as your first contact with the subject unless you already have strong commutative algebra and are content with a terse, high-friction experience.

Use one of these two stacks.

| Route | Main resources | Best for |
|---|---|---|
| Geometry-first | Vakil’s *The Rising Sea* or Gathmann’s notes + ETH videos + Borcherds for depth | Developing geometric intuition while learning schemes properly |
| Hartshorne-oriented | Hartshorne Chapter I + Borcherds AG I + Hartshorne Chapter II + Borcherds Schemes | Preparing for a traditional graduate-level algebraic-geometry sequence |
| Computational bridge | Cox–Little–O’Shea + Macaulay2/Singular/Sage + a varieties course | Connecting ideals, Gröbner bases, elimination, and concrete varieties before scheme theory |
| Arithmetic-geometry route | Gathmann/Vakil foundations + curves/divisors + number fields/\(p\)-adics + Silverman | Your most natural longer-term route, given your number-theory interests |

My recommendation is **Gathmann/ETH as the main readable route, Borcherds as the rigorous lecture companion, and Vakil as the conceptual reference**. Use Hartshorne selectively once affine/projective varieties, local rings, and sheaves no longer feel alien.

## Prerequisites

Algebraic geometry is an interface between polynomial algebra and geometry. The basic dictionary begins with an affine algebraic set
\[
V(I)=\{x\in k^n : f(x)=0 \text{ for every } f\in I\},
\]
and its coordinate ring
\[
k[V]=k[x_1,\ldots,x_n]/I(V).
\]

The crucial reversal is that geometric spaces are studied through rings of functions, while maps of spaces correspond contravariantly to homomorphisms of rings.

Before schemes, be fluent with the following.

### Algebra

- Polynomial rings in several variables and ideals.
- Quotient rings, prime ideals, maximal ideals, radicals, and nilpotents.
- Noetherian rings and the Hilbert basis theorem.
- Localization \(S^{-1}A\), especially \(A_{\mathfrak p}\).
- Modules, exact sequences, tensor products, and finitely generated modules.
- Integral extensions, normalization, and basic field extensions.
- Gröbner bases, elimination, and resultants are highly useful computationally but are not logically required for a scheme-first route.

### Geometry and topology

- Linear algebra: rank, kernels, dual spaces, bilinear forms, exterior powers.
- Multivariable calculus: Jacobian matrices and the implicit-function theorem.
- Basic point-set topology: continuity, compactness, connectedness, quotient spaces.
- Differential geometry intuition helps, but do not import Hausdorff-manifold expectations into the Zariski topology.

### Homological algebra

You can delay this initially, but acquire it before serious cohomology:

- Categories and functors.
- Exact sequences, kernels, cokernels, pullbacks, and pushouts.
- Tensor and \(\operatorname{Hom}\).
- Derived functors and \(\operatorname{Ext}\) after basic sheaf cohomology.

A practical readiness check: you should be comfortable explaining why
\[
\operatorname{Spec} k[x,y]/(y^2-x^3)
\]
contains not merely the geometric cusp over \(k\), but also the information encoded by its prime ideals, local rings, and singular point. You should also be able to localize at the ideal \((x,y)\) and interpret that localization as “zooming in” at the cusp.

## Core topic sequence

### 1. Affine algebraic sets and coordinate rings

Start here. It supplies the first algebra–geometry dictionary.

- Zeros of polynomial systems and affine varieties.
- Ideals \(I(X)\) and zero sets \(V(I)\).
- Hilbert’s Nullstellensatz.
- Coordinate rings.
- Zariski topology.
- Irreducible spaces and prime ideals.
- Dimension and chains of irreducible closed subsets.
- Regular functions and local rings.
- Tangent spaces using maximal ideals:
  \[
  T_pX \cong \operatorname{Hom}_k(\mathfrak m_p/\mathfrak m_p^2,k).
  \]

The Hartshorne-oriented introductory lecture is useful precisely for this stage: it covers zero-sets, the Zariski topology, the ideals/zero-set relationship, Noetherian spaces, and basic dimension. [youtube](https://www.youtube.com/watch?v=OuRDWPHjahg)

### 2. Projective geometry and homogeneous algebra

Projective geometry is indispensable. It handles points at infinity, makes many theorems structurally correct, and is the natural home for complete curves and many moduli problems.

- Projective space \(\mathbb P^n_k\).
- Homogeneous polynomials and homogeneous ideals.
- Projective varieties.
- The Proj construction.
- Standard affine charts.
- Projective morphisms.
- Bézout’s theorem and intersection multiplicity.
- Plane curves and projective closure.

**Example:** The affine curve \(y=x^2\) becomes, after homogenization,
\[
YZ=X^2
\]
in \(\mathbb P^2\). The projective closure adds the point \([0:1:0]\), which records the geometry “at infinity.” Such added points often determine whether maps extend, whether intersections are correctly counted, and whether a curve is complete.

### 3. Morphisms, rational maps, and birational geometry

This stage explains which maps are genuinely algebraic and when different equations represent the same geometric object.

- Regular maps and maps induced by ring homomorphisms.
- Rational functions and function fields.
- Rational maps and their indeterminacy loci.
- Dominant, finite, integral, and étale morphisms.
- Birational equivalence.
- Blow-ups and resolution intuition.
- Normality and normalization.
- Properness and completeness.

Borcherds’ first course has an unusually good structural sequence here: after affine and projective varieties, it proceeds through morphisms, rational maps, nonsingular varieties and curves, and intersections. [bilibili](https://www.bilibili.com/video/BV1y1zXY8EiB/)

### 4. Schemes and sheaves

This is the conceptual center of modern algebraic geometry. A scheme is built by gluing affine pieces
\[
\operatorname{Spec} A
\]
equipped with their structure sheaves \(\mathcal O_{\operatorname{Spec}A}\).

Learn this in the following order:

1. Prime spectrum and Zariski topology.
2. Structure sheaf.
3. Locally ringed spaces.
4. Schemes and affine schemes.
5. Gluing schemes from affine opens.
6. Morphisms of schemes.
7. Fiber products.
8. Quasi-coherent and coherent sheaves.
9. Relative \(\operatorname{Spec}\) and \(\operatorname{Proj}\).
10. Base change.
11. Separated, proper, finite-type, smooth, étale, and flat morphisms.

The definition becomes less mystical when you see the role of all prime ideals. Closed points correspond roughly to classical points over algebraically closed fields, while non-maximal prime ideals record irreducible subvarieties and their generic points. Tubbenhauer’s scheme introduction is valuable for this “\(\operatorname{Spec}\) in action” intuition, while Borcherds provides a systematic Hartshorne-Chapter-II-oriented continuation. [youtube](https://www.youtube.com/watch?v=BX3jiLdehA4)

### 5. Curves, divisors, line bundles, and Riemann–Roch

This should be your first major deep-dive after schemes. It is the best meeting point of algebra, geometry, and number theory.

- Smooth projective curves.
- Divisors, principal divisors, and divisor class groups.
- Line bundles and invertible sheaves.
- Canonical divisors and differentials.
- Genus.
- Riemann–Roch:
  \[
  \ell(D)-\ell(K-D)=\deg D+1-g.
  \]
- Jacobians and Picard groups.
- Elliptic curves as genus-one curves with a chosen rational point.
- Maps of curves and ramification.

For your Jacobian interest, this is where the word has two related but distinct roles:

- The **Jacobian matrix** of defining equations tests smoothness locally through rank.
- The **Jacobian variety** \(J(C)\) is a global abelian variety associated to a curve \(C\), encoding degree-zero divisor classes:
  \[
  J(C)\simeq \operatorname{Pic}^0(C).
  \]

### 6. Cohomology and duality

Once sheaves and curves are comfortable, move to cohomology.

- Čech cohomology as a computational starting point.
- Sheaf cohomology \(H^i(X,\mathcal F)\).
- Cohomology of \(\mathcal O_{\mathbb P^n}(d)\).
- Long exact sequences.
- Serre vanishing.
- Serre duality.
- Coherent cohomology and base change.

The ETH course includes quasi-coherent sheaves, differentials, and sheaf cohomology after its varieties-and-schemes foundation, which makes it one of the rare video sequences with a complete logical arc toward modern methods. [metaphor.ethz](https://metaphor.ethz.ch/x/2026/fs/401-3146-12L/)

### 7. Choose a specialization

After the common core, choose one pathway for 8–16 weeks instead of sampling advanced buzzwords.

| Track | Topics | Good outcomes |
|---|---|---|
| Arithmetic geometry | Schemes over \(\operatorname{Spec}\mathbb Z\), elliptic curves, reduction mod \(p\), Néron models, étale cohomology introduction, local-global principles | Connects directly to algebraic number theory, Diophantine equations, and \(p\)-adics |
| Birational geometry | Blow-ups, divisors, intersection theory, surfaces, minimal models, singularities | Explains rational maps and classification questions |
| Moduli theory | Families, representable functors, Hilbert schemes, moduli of curves/vector bundles, stacks introduction | Understands parameter spaces of geometric objects |
| Computational algebraic geometry | Gröbner bases, elimination, syzygies, Hilbert functions, primary decomposition, numerical algebraic geometry | Supports implementable experiments in Macaulay2, Singular, Sage, or Sage+Singular |
| Toric/tropical geometry | Cones, fans, toric varieties, polyhedral geometry, tropicalization | High-intuition bridge between combinatorics and modern geometry; Hausen’s course is an accessible entry after fundamentals.  [sites.google](https://sites.google.com/view/eniskaya/math-videos) |
| Derived geometry | Derived categories, derived functors, dg-algebras, derived schemes/stacks | Advanced; defer until cohomology, homological algebra, and scheme theory are routine |

## A 30-week syllabus

This assumes roughly 8–12 focused hours per week: 3–5 hours of lectures/reading and 5–7 hours of exercises, computations, and proof-writing.

| Weeks | Topic | Outputs |
|---|---|---|
| 1–2 | Commutative algebra review | Prove the correspondence among radical ideals and algebraic sets; compute prime and maximal ideals in simple quotient rings |
| 3–4 | Affine varieties and coordinate rings | Compute \(I(X)\), coordinate rings, irreducible components, and dimensions for explicit plane curves |
| 5–6 | Nullstellensatz and Zariski topology | Prove weak Nullstellensatz in a chosen framework; identify closures, dense opens, and generic points |
| 7–8 | Local rings, smoothness, tangent spaces | Compute \(\mathfrak m/\mathfrak m^2\) and tangent spaces; classify simple plane-curve singularities |
| 9–10 | Projective varieties and Proj | Homogenize equations, construct projective closures, cover \(\mathbb P^n\) by affine charts |
| 11–12 | Morphisms and rational maps | Translate regular maps into ring maps; analyze rational maps and function fields |
| 13–14 | Curves and divisors | Compute divisors of rational functions on \(\mathbb P^1\) and simple plane curves |
| 15–16 | Blow-ups, normalization, birational maps | Work through the blow-up of \(\mathbb A^2\) at the origin; normalize a nodal or cuspidal curve |
| 17–18 | Schemes and structure sheaves | Construct \(\operatorname{Spec}A\); calculate standard opens \(D(f)\) and their coordinate rings |
| 19–20 | Gluing and projective schemes | Glue affine schemes; build \(\mathbb P^1\) from two affine lines; understand \(\operatorname{Proj}\) |
| 21–22 | Quasi-coherent sheaves and fiber products | Translate modules into quasi-coherent sheaves; calculate simple fiber products/base changes |
| 23–24 | Differentials, smoothness, étale preview | Use Kähler differentials; compare Jacobian-rank and local-algebra smoothness criteria |
| 25–26 | Cohomology and line bundles | Compute \(H^i(\mathbb P^1,\mathcal O(d))\); prove basic consequences using Čech complexes |
| 27–28 | Riemann–Roch, genus, Jacobians | Apply Riemann–Roch on \(\mathbb P^1\) and elliptic curves; connect \(\operatorname{Pic}^0\) to Jacobians |
| 29–30 | Specialization and capstone | Produce a written proof notebook plus a computational or theoretical mini-project |

## Texts and software

| Need | Recommendation | How to use it |
|---|---|---|
| Friendly rigorous first text | **Gathmann, *Algebraic Geometry*** | Strong first full set of notes; aligns particularly well with the ETH course structure.  [metaphor.ethz](https://metaphor.ethz.ch/x/2026/fs/401-3146-12L/) |
| Broad conceptual reference | **Vakil, *The Rising Sea: Foundations of Algebraic Geometry*** | Read selectively and slowly; excellent explanations and exercises |
| Classical graduate reference | **Hartshorne, *Algebraic Geometry*** | Use after or alongside a more explanatory text; Borcherds’ courses are organized around its Chapters I and II.  [bilibili](https://www.bilibili.com/video/BV1y1zXY8EiB/) |
| Classical varieties | **Shafarevich, *Basic Algebraic Geometry I*** | Strong variety-first perspective and many geometric examples |
| Computational entry | **Cox, Little & O’Shea, *Ideals, Varieties, and Algorithms*** | Best first exposure to Gröbner bases and explicit algebraic computations |
| Computational next step | **Cox, Little & O’Shea, *Using Algebraic Geometry*** | More advanced elimination, projective techniques, syzygies, and applications |
| Curves and arithmetic geometry | **Silverman & Tate, *Rational Points on Elliptic Curves*** | Excellent first bridge from algebraic geometry into arithmetic questions |
| Advanced arithmetic geometry | **Qing Liu, *Algebraic Geometry and Arithmetic Curves*** | Long-term reference after schemes, commutative algebra, and basic number theory |

For computation, use:

- **SageMath** for symbolic experiments, finite fields, curves, and number-theory integration.
- **Singular** for fast Gröbner-basis and commutative-algebra calculations.
- **Macaulay2** for graded rings, projective schemes, resolutions, and sheaf-oriented commutative algebra.
- **Magma** if you have access and want an especially capable environment for algebraic curves, number fields, and arithmetic geometry.

## Capstones tailored to your interests

Choose one and make it a reproducible notebook plus a short mathematical write-up.

- **Singular plane curves:** Start with \(y^2=x^3\), compute the Jacobian ideal, locate the singularity, normalize the curve, and compare the cusp with a nodal cubic.
- **Elliptic curves over finite fields:** For \(E:y^2=x^3+ax+b\), count \(\#E(\mathbb F_p)\) for many primes; examine the Frobenius trace \(a_p=p+1-\#E(\mathbb F_p)\); relate reduction modulo \(p\) to arithmetic questions.
- **The scheme \(\operatorname{Spec}\mathbb Z\):** Explicitly analyze its generic point, closed points \((p)\), Zariski-open sets \(D(n)\), and why it is a geometric object encoding all primes simultaneously.
- **Gröbner-basis elimination:** Eliminate parameters from a parametrized curve or surface, derive an implicit equation, and compare the algebraic ideal computation against a geometric projection.
- **Toric variety from a fan:** Construct a low-dimensional toric variety from cones, determine its affine charts, and connect its combinatorics to divisors and singularities.
- **Arithmetic surface mini-study:** Investigate a family of elliptic curves over \(\operatorname{Spec}\mathbb Z\), identify bad reduction primes from the discriminant, and relate the result to local behavior over \(\mathbb Q_p\).

The best first capstone for you is the **singular cubic-to-elliptic-curve route**: it unifies polynomial equations, Jacobian calculations, local rings, normalization, projective closure, divisors, and arithmetic reduction—then naturally leads into both elliptic curves and arithmetic geometry.

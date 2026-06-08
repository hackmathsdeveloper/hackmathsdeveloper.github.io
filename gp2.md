
Lie groups and algebraic groups are both “groups with geometry,” but the geometry is different: Lie groups are smooth manifolds over \(\mathbb R\) or \(\mathbb C\), while algebraic groups are varieties defined by polynomial equations over a field (often \(\mathbb C\), \(\mathbb Q\), or finite fields). This leads to different categories, morphisms, and phenomena, even though over \(\mathbb C\) there is a large overlap (complex algebraic groups give complex Lie groups). [en.wikipedia](https://en.wikipedia.org/wiki/Lie_group)

***

## Underlying objects

- **Lie group**: A group \(G\) that is also a finite‑dimensional smooth manifold such that multiplication and inversion are smooth maps. [math.toronto](https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf)
- **Algebraic group**: A group \(G\) that is an algebraic variety over a field \(k\), with group operations given by regular (polynomial) maps. [jmilne](https://www.jmilne.org/math/CourseNotes/LAG.pdf)

So a Lie group lives in the category of smooth manifolds; an algebraic group lives in the category of algebraic varieties (or schemes).  

***

## Nature of morphisms

- **Lie group homomorphisms** are required to be both group homomorphisms and smooth maps between manifolds. [math.toronto](https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf)
- **Algebraic group homomorphisms** must be group homomorphisms and regular (polynomial) maps of varieties. [jmilne](https://www.jmilne.org/math/CourseNotes/ALA.pdf)

A continuous or smooth group homomorphism between complex Lie groups need not be algebraic; algebraic morphisms are a much smaller and more rigid class. [mathweb.ucsd](https://mathweb.ucsd.edu/~nwallach/chapter1.pdf)

***

## Allowed coordinate functions

- For Lie groups, coordinate charts and maps can be arbitrary smooth (often even analytic) functions. [en.wikipedia](https://en.wikipedia.org/wiki/Lie_group)
- For algebraic groups, all defining and structural maps must be polynomial (or regular rational maps), so you cannot use transcendental functions like \(\exp\), \(\sin\), etc., in the structure. [jmilne](https://www.jmilne.org/math/CourseNotes/LAG.pdf)

Example: \((\mathbb R,+)\) is a Lie group but not an affine algebraic group over \(\mathbb R\) in a natural way, while \(\mathbb G_a\) and \(\mathbb G_m\) (additive and multiplicative groups) are algebraic groups over any field. [jmilne](https://www.jmilne.org/math/CourseNotes/ALA.pdf)

***

## Base fields vs base manifolds

- Lie groups are typically considered over \(\mathbb R\) or \(\mathbb C\), with topology and smooth structure coming from those fields. [math.toronto](https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf)
- Algebraic groups are defined over arbitrary fields \(k\) (e.g., \(\mathbb C\), \(\mathbb Q\), number fields, finite fields, \(\overline{\mathbb Q}_p\), etc.), and one studies their \(k\)‑rational points and behavior under field extensions. [jmilne](https://www.jmilne.org/math/CourseNotes/LAG.pdf)

This allows algebraic groups to connect directly to arithmetic geometry and Galois theory, where \(k\) is number‑theoretic rather than analytic.  

***

## Topology and analysis vs arithmetic/algebra

- Lie groups come with a natural topology and smooth structure, so you can do differential geometry, harmonic analysis, representation theory using analytic tools (e.g., Haar measure, unitary representations on Hilbert spaces). [math.stonybrook](https://www.math.stonybrook.edu/~kirillov/mat552/liegroups.pdf)
- Algebraic groups are more rigid, geared towards algebraic and arithmetic structure: you study them using algebraic geometry (line bundles, cohomology, group schemes, reduction modulo primes, etc.). [jmilne](https://www.jmilne.org/math/CourseNotes/ALA.pdf)

For a complex algebraic group \(G\) over \(\mathbb C\), the set of complex points \(G(\mathbb C)\) is a complex Lie group, and analytic methods apply—but not every complex Lie group comes from an algebraic group. [mathweb.ucsd](https://mathweb.ucsd.edu/~nwallach/chapter1.pdf)

***

## Examples and non‑examples

- **Lie groups that are algebraic** (over \(\mathbb C\)):  
  - \( \mathrm{GL}_n(\mathbb C)\), \( \mathrm{SL}_n(\mathbb C)\), orthogonal, symplectic groups, etc., are both complex Lie groups and complex algebraic groups. [en.wikipedia](https://en.wikipedia.org/wiki/Lie_group)
- **Lie groups that are not algebraic**:  
  - Many compact Lie groups like a generic compact torus \(T^n = (\mathbb S^1)^n\) are not (affine) algebraic over \(\mathbb R\) as varieties; as complex groups they are complex Lie groups but not complex algebraic groups (they are quotients \(\mathbb C^n / \Lambda\) by lattices instead of varieties defined by polynomials). [en.wikipedia](https://en.wikipedia.org/wiki/Lie_group)
- **Algebraic groups without a “real Lie” structure**:  
  - Algebraic groups over finite fields, like \(\mathrm{SL}_2(\mathbb F_p)\), have no meaningful manifold structure over \(\mathbb F_p\); they are purely algebraic objects (though their groups of complex points can be Lie groups if you extend scalars). [jmilne](https://www.jmilne.org/math/CourseNotes/LAG.pdf)

So “algebraic group over \(\mathbb C\)” ⇒ complex Lie group, but the converse fails in general.  

***

## Lie algebras and tangent structure

Both frameworks have an associated Lie algebra, but with slightly different perspectives: [math.stonybrook](https://www.math.stonybrook.edu/~kirillov/mat552/liegroups.pdf)

- For a Lie group, the Lie algebra is the tangent space at the identity with the bracket from commutators of left‑invariant vector fields.  
- For an algebraic group over a field of characteristic zero, the Lie algebra is the tangent space at the identity of the variety, with a bracket induced algebraically from the group structure.  

If \(G\) is a complex algebraic group, the Lie algebra defined algebraically coincides with the Lie algebra of the complex Lie group \(G(\mathbb C)\). The representation theories of the algebraic group and its Lie algebra are closely related, but for Lie groups you can also consider many analytic representation notions (unitary, smooth, etc.) that have no purely algebraic analogue. [mathweb.ucsd](https://mathweb.ucsd.edu/~nwallach/chapter1.pdf)

***

## “Classification” viewpoints

- **Lie groups** (compact or semisimple) are classified up to local isomorphism by root data and Dynkin diagrams, with additional global topological information (fundamental group, center, coverings). This classification is analytic–topological in nature. [math.stonybrook](https://www.math.stonybrook.edu/~kirillov/mat552/liegroups.pdf)
- **Algebraic groups** (connected reductive over algebraically closed fields) are similarly classified by root systems, but with extra arithmetic data when defined over non‑algebraically‑closed fields (Galois action on root data, Tits indices, etc.). [jmilne](https://www.jmilne.org/math/CourseNotes/ALA.pdf)

Thus, the overlap in classification reflects the shared root‑system structure, but algebraic groups carry more arithmetic structure (e.g., forms over \(\mathbb Q\), reduction modulo primes) that Lie groups, as purely real/complex manifolds, do not encode.  

***

## Practical rule of thumb

- Use **Lie groups** when you care about smooth symmetries, differential equations, harmonic analysis, or representation theory on Hilbert/Banach spaces (physics, PDEs, analytic number theory, etc.). [math.stonybrook](https://www.math.stonybrook.edu/~kirillov/mat552/liegroups.pdf)
- Use **algebraic groups** when you care about polynomial symmetries, varieties, and arithmetic (Galois representations, automorphic forms, motives, reduction mod \(p\), etc.). [arxiv](https://arxiv.org/pdf/1210.0222.pdf)

But over \(\mathbb C\), you can often shuttle between the two by passing from an algebraic group to its Lie group of complex points and back, provided you stay within the “algebraic” subclass of Lie groups.  

If you tell me your main use case (e.g., representation theory, arithmetic geometry, or differential equations), I can highlight the most relevant aspects of this distinction for that context.

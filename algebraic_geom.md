
Algebraic geometry studies spaces defined by polynomial equations—such as curves, surfaces, and higher-dimensional varieties—and the algebraic structures encoded by their coordinate rings. There is no single official list of “types”; the field is commonly divided both by its **ambient setting** and by its **methods/applications**. [britannica](https://www.britannica.com/science/algebraic-geometry)

## Foundational settings

| Type | What it studies | Typical example / purpose |
|---|---|---|
| **Affine algebraic geometry** | Zero sets of polynomial equations in affine space \( \mathbb A^n \). Algebraically, it corresponds to finitely generated coordinate rings such as \(k[x_1,\ldots,x_n]/I\). | \(y^2=x^3-x\) in \( \mathbb A^2 \); useful for explicit equations and computation. |
| **Projective algebraic geometry** | Homogeneous polynomial equations in projective space \( \mathbb P^n \), where points differing by a nonzero scale are identified. This adds “points at infinity” and makes intersection behavior more complete. | A projective plane cubic \(Y^2Z=X^3-aXZ^2-bZ^3\); elliptic curves are naturally treated this way. |
| **Quasi-affine / quasi-projective geometry** | Open subsets of affine or projective varieties. These cover most classical varieties encountered in practice: they may exclude a divisor, a singular locus, or points at infinity. | \( \mathbb P^1\setminus\{\infty\}\cong \mathbb A^1\). |
| **Scheme theory** | The modern foundation: schemes glue spectra of commutative rings and retain nilpotents, multiplicities, and arithmetic information that point-set varieties can lose. | \(\operatorname{Spec}\mathbb Z\) places prime numbers and the generic characteristic-zero point in one geometric object. Affine, projective, and quasi-projective varieties are special cases.  [math.uchicago](https://www.math.uchicago.edu/~emerton/algebraic-geometry-2014/notes.pdf) |

## By base field

- **Complex algebraic geometry** studies varieties over \( \mathbb C \). It connects strongly to complex analysis, topology, and differential geometry: a smooth complex projective variety is also a compact complex manifold, and often admits Kähler methods. This is the usual setting for Hodge theory and much of classical geometry. [en.wikipedia](https://en.wikipedia.org/wiki/Algebraic_geometry)

- **Real algebraic geometry** studies polynomial equations over \( \mathbb R \), focusing on their real solution sets and questions involving signs, inequalities, semialgebraic sets, and sums of squares. A polynomial can have rich complex geometry but few—or no—real points. [en.wikipedia](https://en.wikipedia.org/wiki/Algebraic_geometry)

- **Arithmetic / Diophantine geometry** studies varieties over \( \mathbb Q \), number fields, finite fields, and \(p\)-adic fields, asking about rational, integral, or local points. It is a central bridge to number theory; elliptic curves, modular curves, and the geometry underlying Fermat’s Last Theorem are standard examples. [britannica](https://www.britannica.com/science/algebraic-geometry)

- **Finite-field geometry** focuses on varieties over \( \mathbb F_q \), especially point counts, Frobenius actions, and zeta functions. It matters in coding theory, cryptography, and the Weil conjectures.

## By geometric question

- **Birational geometry** classifies varieties up to rational maps that are invertible away from lower-dimensional subsets. It asks which varieties are “the same” from the standpoint of rational functions, and includes the minimal model program. For example, blowing up a point changes the variety but is a birational modification. [en.wikipedia](https://en.wikipedia.org/wiki/Category:Algebraic_geometry)

- **Intersection theory** assigns rigorous multiplicities to intersections. Two curves may meet at a point with multiplicity greater than one—for instance, a tangent line meets a conic with multiplicity two—so simply counting visible points is insufficient. [en.wikipedia](https://en.wikipedia.org/wiki/Category:Algebraic_geometry)

- **Singularity theory** analyzes non-smooth points, where a variety fails locally to resemble affine space. It develops invariants and procedures such as resolution of singularities, which replaces a singular space with a smoother one while controlling what changed. [en.wikipedia](https://en.wikipedia.org/wiki/Algebraic_geometry)

- **Moduli theory** constructs spaces whose points themselves represent geometric objects, such as curves, vector bundles, or elliptic curves. A moduli space turns a classification problem into geometry; the moduli stack of elliptic curves is the prototypical example.

- **Algebraic groups and representation-theoretic geometry** studies varieties with compatible group laws and spaces acted on by groups. Linear algebraic groups, flag varieties, Grassmannians, and Schubert varieties link geometry to Lie theory and representations. [math.ru](https://www.math.ru.nl/~bmoonen/AlgGeom/alggeom.pdf)

## Computational and newer directions

- **Computational algebraic geometry** develops algorithms for ideals, Gröbner bases, elimination, decomposition, and explicit invariants. It is the practical interface with computer algebra systems such as Singular, Macaulay2, Magma, and SageMath. [en.wikipedia](https://en.wikipedia.org/wiki/Algebraic_geometry)

- **Tropical geometry** replaces algebraic equations with piecewise-linear “tropical” analogues, preserving combinatorial shadows of varieties. It can turn difficult intersection and degeneration problems into polyhedral calculations. [en.wikipedia](https://en.wikipedia.org/wiki/Category:Algebraic_geometry)

- **Toric geometry** studies varieties built from combinatorial data such as fans and polytopes. It provides an unusually explicit class of varieties and is useful in mirror symmetry, combinatorics, and optimization-adjacent methods.

- **Noncommutative algebraic geometry** extends geometric ideas to noncommutative algebras, where an ordinary prime-spectrum picture may be inadequate. It appears in representation theory, quantum groups, and certain mathematical-physics settings. [en.wikipedia](https://en.wikipedia.org/wiki/Category:Algebraic_geometry)

- **Derived algebraic geometry** enriches schemes with homological and higher-categorical data, so intersections and deformation spaces retain hidden higher-order information. A motivating situation is a non-transverse intersection: derived structure records the excess-intersection data that ordinary geometry collapses. [ncatlab](https://ncatlab.org/nlab/show/algebraic+geometry)

## A useful mental map

For a technical entry point, think in layers:

1. **Classical layer:** affine and projective varieties over an algebraically closed field.
2. **Modern foundation:** schemes, sheaves, cohomology, and morphisms.
3. **Arithmetic layer:** rational/integral points, Galois actions, and local-global principles.
4. **Classification layer:** birational geometry, moduli, and singularities.
5. **Computational/higher layer:** Gröbner bases, tropical/toric techniques, stacks, and derived methods.

If you are interested in cryptography and number-theory interests, **arithmetic geometry** is the most natural branch to pursue first—particularly elliptic curves, abelian varieties, algebraic curves over finite fields, and moduli.

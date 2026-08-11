
Geometric algebra (GA) is a family of Clifford algebras built from a vector space plus a quadratic form/metric. Most named “types” are not competing algebras—they are different **signatures** and geometric models chosen for the transformations and objects you want to represent. The central product is

\[
ab = a\cdot b + a\wedge b,
\]

so one operation simultaneously carries metric information (inner product) and oriented-subspace information (outer product). [studenttheses.uu](https://studenttheses.uu.nl/bitstream/handle/20.500.12932/33645/IntroductionToGeometricAlgebraV2.pdf)

## The common foundation

For a real vector space with signature \((p,q,r)\), the algebra is commonly written \(Cl(p,q,r)\) or \(\mathcal G(p,q,r)\):

- \(p\): basis directions squaring to \(+1\)
- \(q\): basis directions squaring to \(-1\)
- \(r\): null/degenerate directions squaring to \(0\)
- An \(n\)-dimensional base vector space generates a \(2^n\)-dimensional GA, whose elements are **multivectors**: scalars, vectors, bivectors, trivectors, and so on.

“Vector-space GA” is therefore best understood as ordinary GA constructed from a vector space, not a separate geometry model. Vectors are grade-1 elements; bivectors naturally encode oriented planes and infinitesimal rotations. [assets.cambridge](https://assets.cambridge.org/052148/0221/sample/0521480221WS.pdf)

## Major models

| Name | Typical algebra | What it models well | Main transformations |
|---|---:|---|---|
| Euclidean / vector GA | \(Cl(2,0)\), \(Cl(3,0)\) | Vectors, oriented subspaces through the origin | Rotations, reflections |
| Algebra of physical space (APS) | Usually \(Cl(3,0)\) | Classical 3D physics, rotations; can encode relativity in a different formulation | \(SO(3)\) rotations |
| Spacetime algebra (STA) | \(Cl(1,3)\) or \(Cl(3,1)\), convention-dependent | Minkowski events, worldlines, electromagnetic field, Lorentz geometry | Lorentz rotations and boosts |
| Projective GA (PGA) | Often \(Cl(3,0,1)\) or dual convention \(Cl(0,3,1)\) for 3D Euclidean geometry | Points, lines, planes, rigid bodies, Euclidean incidence | Rotations, translations, screws |
| Conformal GA (CGA) | \(Cl(4,1)\) or \(Cl(1,4)\) for Euclidean 3D | Points, lines, planes, circles, spheres, tangency | Rigid motions plus dilations and inversions |
| Conformal spacetime algebra (CSTA) | \(Cl(4,2)\) or convention variant | Compactified Minkowski spacetime, light cones, conformal spacetime symmetry | Spacetime conformal group |

The sign ordering is not universal: authors may write \(Cl(1,3)\) versus \(Cl(3,1)\) depending on whether time or space has positive square. Those are related in purpose but not literally identical real algebras, so always check the author’s metric convention. STA is specifically the GA of Minkowski \(3+1\) spacetime and is used to express Lorentz boosts and rotations geometrically. [en.wikipedia](https://en.wikipedia.org/wiki/Geometric_algebra)

## PGA: projective, rigid geometry

PGA adds one **null homogeneous dimension** to Euclidean space. This lets it represent Euclidean points, lines, and planes uniformly—including ideal elements such as directions at infinity—and perform translations through versor multiplication, alongside rotations and reflections. [projectivegeometricalgebra](https://projectivegeometricalgebra.org/)

For practical 3D rigid-body work, PGA is especially elegant:

- A point, line, plane, and their joins/meets live in the same algebra.
- A motor encodes a rotation plus translation—the GA analogue of a unit dual quaternion.
- Intersections are algebraic: e.g., plane \(\wedge\) plane gives their line of intersection, with the exact representation depending on whether you use the primal or dual PGA convention.

Choose PGA when your domain is CAD, robotics, kinematics, computational geometry, ray/plane/line incidence, or \(SE(3)\) transformations. PGA subsumes the roles commonly split among homogeneous coordinates, Plücker line coordinates, quaternions, and dual quaternions. [projectivegeometricalgebra](https://projectivegeometricalgebra.org/)

## CGA: conformal geometry

CGA adds **two** extra dimensions and embeds Euclidean points as null vectors. In 3D Euclidean CGA, this leads to a five-dimensional model, often denoted \(Cl(4,1)\). [en.wikipedia](https://en.wikipedia.org/wiki/Geometric_algebra)

Its key payoff is that it treats flat and round geometry uniformly:

- Planes and lines are included.
- Circles and spheres have direct algebraic representations.
- A plane can be viewed as a sphere of infinite radius.
- Rotations, translations, dilations, and inversions are all versor actions; compositions of these generate conformal transformations. [projectivegeometricalgebra](https://projectivegeometricalgebra.org/)

Choose CGA when circles, spheres, tangency, inversive geometry, camera/vision constraints, or non-rigid conformal transformations are first-class concerns. For purely rigid 3D geometry, PGA is typically smaller and simpler.

## Spacetime and conformal spacetime

**STA** starts from Minkowski spacetime, rather than Euclidean 3-space. A spacetime vector can be written schematically as

\[
x = ct\,\gamma_0 + x^1\gamma_1+x^2\gamma_2+x^3\gamma_3.
\]

The spacetime interval is \(x^2=x\cdot x\); its sign separates timelike, null, and spacelike vectors. The electromagnetic field is compactly represented as a bivector \(F\), which is one reason STA can make relativistic electromagnetism notably compact. The standard STA basis has metric \(\operatorname{diag}(+,-,-,-)\) in one prevalent convention. [geometry.mrao.cam.ac](https://geometry.mrao.cam.ac.uk/wp-content/uploads/2015/02/03lda_tenn.pdf)

**CSTA** extends this further to model conformal spacetime symmetry. It can represent spacetime spheres/circles analogues, light-cone structures, and certain accelerated trajectories in a linear-versor framework; it is related conceptually to twistor-style conformal treatments. [en.wikipedia](https://en.wikipedia.org/wiki/Geometric_algebra)

## A useful selection rule

- **Linear algebra, rotations, cross-product replacement:** \(Cl(3,0)\).
- **Rigid Euclidean geometry and robotics:** PGA.
- **Spheres, circles, inversions, tangent geometry:** CGA.
- **Special relativity and relativistic field theory:** STA.
- **Conformal compactification or conformal field/spacetime work:** CSTA.

The unifying idea is: change the underlying metric and embedding, then the same GA operations model a different geometry.

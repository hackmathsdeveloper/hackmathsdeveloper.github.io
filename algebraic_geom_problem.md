
Here are 50 varied algebraic-geometry problems, moving from affine varieties and projective curves to schemes, sheaves, cohomology, and intersection theory. They reflect standard exercise themes such as Zariski topology, coordinate rings, singularities, scheme-theoretic intersections, and Bézout-type questions. [people.maths.ox.ac](https://people.maths.ox.ac.uk/ritter/algebraic-geometry/exercises-alg-geom-01.pdf)

## Affine geometry

1. Describe all Zariski-closed subsets of \(\mathbb A^1_k\) for an algebraically closed field \(k\).

2. Prove that \(\mathbb A^n_k\) is irreducible.

3. Show that \(V(xy)\subset \mathbb A^2_k\) is reducible, and find its irreducible components.

4. Determine whether the ideal \((xy,xz)\subset k[x,y,z]\) is prime, radical, or neither; describe its zero locus.

5. Compute the coordinate ring of \(V(y-x^2)\subset\mathbb A^2_k\), and prove that this variety is isomorphic to \(\mathbb A^1_k\).

6. Find the irreducible components of \(V(xz,yz)\subset\mathbb A^3_k\).

7. Determine all singular points of the affine plane curve \(y^2=x^3-x^2\).

8. Find the tangent cone at the origin of \(V(y^2-x^3)\subset\mathbb A^2_k\).

9. Prove that an affine variety \(X\) is irreducible iff every nonempty open subset of \(X\) is dense.

10. Let \(X=V(y^2-x^3)\). Compute the normalization of its coordinate ring.

11. Show that \(k[x,y]/(y^2-x^2(x+1))\) is not integrally closed.

12. For \(f=x^2+y^2-1\) over \(\mathbb C\), determine whether \(V(f)\) is smooth and compute its dimension.

13. Describe the morphism \(\mathbb A^1\to V(y-x^2)\) induced by \(t\mapsto(t,t^2)\), and show it is an isomorphism.

14. Prove that a morphism \(F:X\to Y\) of affine varieties is dominant iff the induced map \(F^*:k[Y]\to k[X]\) is injective. [people.maths.ox.ac](https://people.maths.ox.ac.uk/ritter/algebraic-geometry/exercises-alg-geom-01.pdf)

15. Give an example of an injective morphism of affine varieties that is not a closed immersion.

## Projective varieties and curves

16. Prove that every homogeneous polynomial defines a closed subset of \(\mathbb P^n_k\).

17. Show that the projective plane curve \(V(Y^2Z-X^3)\subset\mathbb P^2_k\) is singular, and locate all singularities.

18. Compute the tangent line to the smooth projective curve \(F(X,Y,Z)=0\) at a given point \(P\), using the partial derivatives of \(F\). [jmilne](https://www.jmilne.org/math/CourseNotes/AG522.pdf)

19. Prove that a nonsingular conic in \(\mathbb P^2_k\) with a \(k\)-rational point is isomorphic to \(\mathbb P^1_k\).

20. Show that \(V(XY-Z^2)\subset\mathbb P^2_k\) is isomorphic to \(\mathbb P^1_k\) via the degree-two Veronese map.

21. Determine the genus of a smooth plane curve of degree \(d\).

22. Use Bézout’s theorem to determine the number of intersection points, counted with multiplicity, of a general plane cubic and a general plane quartic.

23. Find the intersection multiplicity at \((0,0)\) of the curves \(y=0\) and \(y=x^m\) in \(\mathbb A^2_k\).

24. Determine the points at infinity of the affine curve \(y^2=x^5-x\), and study whether its projective closure is smooth there.

25. Prove that every regular function on \(\mathbb P^n_k\) is constant.

26. Show that \(\mathbb P^n_k\) is complete, while \(\mathbb A^n_k\) is not.

27. Compute the Hilbert polynomial of a degree-\(d\) hypersurface in \(\mathbb P^n_k\).

28. Compute the Hilbert polynomial and arithmetic genus of a plane curve of degree \(d\).

29. Let \(C\subset\mathbb P^3\) be a smooth complete intersection of surfaces of degrees \(a\) and \(b\). Compute \(\deg C\) and its arithmetic genus.

30. Prove that two projective plane curves with no common irreducible component have finitely many intersection points.

## Schemes and morphisms

31. Show that \(\operatorname{Spec} k[\varepsilon]/(\varepsilon^2)\) has one point but is not reduced.

32. Describe the prime ideals, topology, and local rings of \(\operatorname{Spec}\mathbb Z\).

33. Prove that \(\operatorname{Spec} A\) is irreducible iff the nilradical \(\sqrt{(0)}\) is prime.

34. Let \(A=k[x,y]/(xy)\). Determine the minimal primes, associated geometry, and local ring at the origin.

35. Prove that a scheme is reduced iff all its local rings are reduced.

36. Construct the scheme-theoretic intersection of \(V(y)\) and \(V(y-x^2)\) in \(\mathbb A^2_k\), and compare it with their set-theoretic intersection.

37. Give two plane curves that meet at exactly one closed point but whose scheme-theoretic intersection has length greater than one. [websites.umich](https://websites.umich.edu/~pixton/classes/631-F24/pset9.pdf)

38. Show that the fiber product
\[
\operatorname{Spec} A \times_{\operatorname{Spec} R}\operatorname{Spec} B
\]
is isomorphic to \(\operatorname{Spec}(A\otimes_R B)\).

39. Compute \(\operatorname{Spec}(k[x]\otimes_k k[y])\) and interpret it geometrically.

40. Let \(X\) be obtained by gluing two copies of \(\mathbb A^1_k\) along \(\mathbb A^1_k\setminus\{0\}\). Prove that \(X\) is not separated.

## Sheaves and cohomology

41. Define the structure sheaf on \(\operatorname{Spec} A\), then compute \(\mathcal O_{\operatorname{Spec}A}(D(f))\).

42. Prove that quasi-coherent sheaves on \(\operatorname{Spec} A\) correspond to \(A\)-modules.

43. Compute \(H^0(\mathbb P^n_k,\mathcal O_{\mathbb P^n}(d))\) for \(d\ge0\).

44. Show that \(H^0(\mathbb P^1_k,\mathcal O_{\mathbb P^1}(d))\) has dimension \(d+1\) for \(d\ge0\).

45. Compute \(H^1(\mathbb P^1_k,\mathcal O_{\mathbb P^1}(d))\) for all integers \(d\).

46. Use the standard affine cover of \(\mathbb P^1\) to show that \(\operatorname{Pic}(\mathbb P^1_k)\cong\mathbb Z\).

47. Prove that every line bundle on \(\mathbb P^1_k\) is isomorphic to \(\mathcal O_{\mathbb P^1}(d)\) for a unique integer \(d\).

48. Let \(C\) be a smooth projective curve of genus \(g\). Use Riemann–Roch to compute \(\ell(D)\) when \(\deg D>2g-2\).

## Intersection theory and moduli

49. In \(\mathbb P^3\), show that there are exactly two lines meeting four general lines. Interpret this as an intersection calculation on the Grassmannian \(\mathrm{Gr}(1,3)\). [math.stonybrook](https://www.math.stonybrook.edu/~fgreer/IntersectionTheoryNotes.pdf)

50. Let \(f\in H^0(\mathbb P^1\times\mathbb P^1,\mathcal O(m,n))\) define a smooth curve \(C\). Compute its arithmetic genus and relate the result to adjunction. [websites.umich](https://websites.umich.edu/~pixton/classes/632-W23/pset6.pdf)

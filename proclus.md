
Proclus’s mathematical legacy is chiefly his exposition, criticism, and preservation of earlier Greek mathematics—not a collection of discoveries all attributable to him. The essential distinction is **authorship**: a result appearing in Proclus’s writings is not necessarily a result discovered by Proclus. His principal surviving mathematical work is his *Commentary on the First Book of Euclid’s Elements*; he also wrote on mathematical astronomy. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

Below is a catalogue of all 48 numbered propositions of Euclid’s Book I—the core mathematical sequence covered by his commentary—followed by important additional mathematical material associated with his writings. This is not an exhaustive transcription of every auxiliary lemma, alternative proof, historical report, or philosophical claim in the commentary. Calling such a list “all Proclus’s original results” would be misleading. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

## 1. The 48 propositions covered in his commentary

These are Euclid’s propositions as discussed by Proclus, not 48 discoveries by Proclus. The statements below use modern terminology and notation. A “construction” means a straightedge-and-compass construction; \([ABC]\) denotes the area of triangle \(ABC\). [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### I.1–I.10: Basic constructions and triangle congruence

1. I.1 — Equilateral triangle construction.  
   On any given nonzero segment \(AB\), construct an equilateral triangle:
   \[
   AB=BC=CA.
   \]

2. I.2 — Transfer a length to a specified point.  
   Given a point \(A\) and a segment of length \(l\), construct a segment starting at \(A\) with length \(l\).

3. I.3 — Cut off a prescribed length.  
   Given two unequal segments, cut from the greater a segment equal to the smaller.

4. I.4 — Side–angle–side congruence.  
   Two triangles are congruent if two corresponding sides and the included angle are equal:
   \[
   AB=DE,\quad AC=DF,\quad
   \angle BAC=\angle EDF
   \Longrightarrow
   \triangle ABC\cong\triangle DEF.
   \]

5. I.5 — Base angles of an isosceles triangle.  
   If \(AB=AC\), then
   \[
   \angle ABC=\angle BCA.
   \]
   When the equal sides are extended beyond the base, the corresponding exterior angles are also equal.

6. I.6 — Converse of the isosceles-triangle theorem.  
   If two angles of a triangle are equal, the opposite sides are equal.

7. I.7 — Uniqueness of a triangle on a fixed base and side.  
   On the same side of a fixed segment \(AB\), there cannot be two distinct points \(C,D\) satisfying both
   \[
   AC=AD,\qquad BC=BD.
   \]

8. I.8 — Side–side–side congruence.  
   Triangles with three equal corresponding sides are congruent.

9. I.9 — Angle bisection.  
   Construct the bisector of a given rectilinear angle.

10. I.10 — Segment bisection.  
    Construct the midpoint of a given segment.

These propositions establish the basic construction and congruence machinery used throughout the subsequent geometry. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### I.11–I.20: Perpendiculars, angles, and triangle inequalities

11. I.11 — Perpendicular at a point on a line.  
    Construct a perpendicular to a given line through a specified point on it.

12. I.12 — Perpendicular from an external point.  
    Construct a perpendicular to a given line through a point not on it.

13. I.13 — Adjacent angles on a straight line.  
    A ray standing on a straight line forms adjacent angles whose sum is two right angles:
    \[
    \alpha+\beta=180^\circ.
    \]

14. I.14 — Converse of the straight-angle theorem.  
    If two adjacent angles, with their noncommon sides on opposite sides of the common side, sum to \(180^\circ\), those noncommon sides form one straight line.

15. I.15 — Vertically opposite angles.  
    When two straight lines intersect, their vertically opposite angles are equal.

16. I.16 — Exterior-angle inequality.  
    An exterior angle of a triangle exceeds either remote interior angle.

17. I.17 — Two-angle inequality.  
    Any two angles of a triangle have sum less than two right angles:
    \[
    \alpha+\beta<180^\circ.
    \]

18. I.18 — Greater side, greater opposite angle.  
    In a triangle,
    \[
    AB>AC\Longrightarrow\angle ACB>\angle ABC.
    \]

19. I.19 — Greater angle, greater opposite side.  
    Conversely,
    \[
    \angle ACB>\angle ABC\Longrightarrow AB>AC.
    \]

20. I.20 — Triangle inequality.  
    Any two sides of a triangle together exceed the third:
    \[
    AB+AC>BC,
    \]
    with analogous inequalities for the other pairs.

These results develop triangle geometry without yet invoking Euclid’s fifth postulate. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### I.21–I.31: Triangle comparisons and parallel lines

21. I.21 — Broken-line comparison inside a triangle.  
    If \(D\) lies inside triangle \(ABC\), then
    \[
    BD+DC<BA+AC,
    \qquad
    \angle BDC>\angle BAC.
    \]

22. I.22 — Construct a triangle from three lengths.  
    Three given lengths can be made into a triangle when every pair has sum greater than the remaining length.

23. I.23 — Copy an angle.  
    At a specified point on a given line, construct an angle equal to a given rectilinear angle.

24. I.24 — Hinge theorem.  
    If two triangles have two corresponding sides equal, the triangle with the greater included angle has the greater opposite side.

25. I.25 — Converse hinge theorem.  
    If two triangles have two corresponding sides equal, the triangle with the greater third side has the greater included angle.

26. I.26 — Angle–side–angle and angle–angle–side congruence.  
    Two triangles are congruent when two corresponding angles and an appropriate corresponding side are equal.

27. I.27 — Equal alternate angles imply parallelism.  
    If a transversal makes equal alternate interior angles with two lines, the lines are parallel.

28. I.28 — Further sufficient conditions for parallelism.  
    Two lines are parallel if a transversal makes either:
    - an exterior angle equal to its interior opposite angle; or
    - same-side interior angles summing to \(180^\circ\).

29. I.29 — Angle properties of parallel lines.  
    A transversal crossing parallel lines produces:
    - equal alternate interior angles;
    - equal corresponding angles;
    - same-side interior angles summing to \(180^\circ\).

30. I.30 — Lines parallel to the same line.  
    Two distinct lines parallel to the same straight line are parallel to each other.

31. I.31 — Construct a parallel through a point.  
    Through a specified point, draw a straight line parallel to a given straight line.

The distinction between I.27–I.28 and I.29 matters: the former establish sufficient conditions for parallelism, whereas I.29 establishes the angle consequences of parallelism and brings the fifth postulate into the proof sequence. Proclus’s discussion of this issue is one of the commentary’s important foundational passages. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### I.32–I.40: Triangle angle sums and area equality

32. I.32 — Triangle angle sum and exterior-angle equality.  
    In any triangle,
    \[
    \alpha+\beta+\gamma=180^\circ.
    \]
    An exterior angle equals the sum of the two remote interior angles.

33. I.33 — Joining equal parallel segments.  
    The segments joining the corresponding endpoints of two equal and parallel segments, in the same direction, are themselves equal and parallel.

34. I.34 — Properties of a parallelogram.  
    Opposite sides and opposite angles are equal. A diagonal divides a parallelogram into two equal-area triangles.

35. I.35 — Parallelograms on the same base.  
    Parallelograms on the same base and between the same parallels have equal areas.

36. I.36 — Parallelograms on equal bases.  
    Parallelograms on equal bases and between the same parallels have equal areas.

37. I.37 — Triangles on the same base.  
    Triangles on the same base and between the same parallels have equal areas.

38. I.38 — Triangles on equal bases.  
    Triangles on equal bases and between the same parallels have equal areas.

39. I.39 — Converse for triangles on the same base.  
    Equal-area triangles on the same base and on the same side of it lie between the same parallels: the line joining their other vertices is parallel to the base.

40. I.40 — Converse for triangles on equal collinear bases.  
    Equal-area triangles on equal bases lying on the same straight line, and on the same side of that line, lie between the same parallels.

In these area propositions, “equal” does not mean “congruent”: figures can have equal areas but different shapes. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### I.41–I.48: Area constructions and the Pythagorean theorem

41. I.41 — Parallelogram–triangle area relation.  
    A parallelogram has twice the area of a triangle on the same base and between the same parallels:
    \[
    A_{\mathrm{parallelogram}}=2A_{\mathrm{triangle}}.
    \]

42. I.42 — Construct a parallelogram equal to a triangle.  
    Construct a parallelogram equal in area to a given triangle and having a specified angle.

43. I.43 — Complements about a parallelogram’s diagonal.  
    When two lines through a point on a parallelogram’s diagonal are drawn parallel to its sides, the two complementary parallelograms not traversed by the diagonal have equal areas.

44. I.44 — Apply a given area to a given segment.  
    On a specified segment, construct a parallelogram equal in area to a given triangle and having a specified angle.

45. I.45 — Construct a parallelogram equal to a rectilinear figure.  
    Construct a parallelogram equal in area to a given rectilinear figure and having a specified angle.

46. I.46 — Square construction.  
    Construct a square on a given segment.

47. I.47 — Pythagorean theorem.  
    If \(c\) is the hypotenuse of a right triangle with legs \(a,b\), then
    \[
    c^2=a^2+b^2.
    \]

48. I.48 — Converse of the Pythagorean theorem.  
    If a triangle’s side lengths satisfy
    \[
    c^2=a^2+b^2,
    \]
    then the angle opposite \(c\) is a right angle.

These complete the numbered proposition sequence of the Book I commentary. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

## 2. Additional mathematical material in Proclus

The numbered propositions are only the framework of the commentary. Proclus also discusses axioms, auxiliary arguments, objections, alternative approaches, and astronomical geometry. The following items need a different attribution from the 48 Euclidean propositions. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

### 2.1 The parallel-line intersection principle

Proclus presents an argument for the statement:

> A straight line that intersects one of two parallel straight lines also intersects the other.

He attempts to use this to establish Euclid’s fifth postulate. His argument appeals to the claim that the separation of two indefinitely extended lines forming an angle eventually exceeds any assigned finite magnitude. [amazon](https://www.amazon.com/Proclus-Commentary-First-Euclids-Elements/dp/0691071608)

Its status must be stated carefully: this is not a successful derivation of the fifth postulate from Euclid’s remaining assumptions. The account of his argument identifies a hidden assumption concerning the separation of parallel lines. Thus it belongs in a catalogue as a foundational argument or attempted proof, not as an independently established replacement for the parallel postulate. [amazon](https://www.amazon.com/Proclus-Commentary-First-Euclids-Elements/dp/0691071608)

### 2.2 Equality of right angles

Proclus discusses a superposition-style argument for the equality of all right angles:

\[
\angle ABC=\angle DEF=90^\circ.
\]

However, he expressly says that the argument had also been given by other expositors. It should therefore not be presented as his original discovery. His discussion concerns whether the statement belongs among axioms, postulates, or demonstrable propositions. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### 2.3 Equality of multiples and preservation of differences

His discussion of common notions includes consequences expressible in modern notation as:

- If \(a=b\), then corresponding equal multiples are equal:
  \[
  na=nb.
  \]
- Adding equal quantities preserves a difference:
  \[
  (a+c)-(b+c)=a-b.
  \]
- Adding unequal quantities to equal quantities produces a difference equal to that of the unequal additions:
  \[
  a=b\Longrightarrow(a+c)-(b+d)=c-d.
  \]

These are modern algebraic renderings of arguments about quantities, not symbolic formulas written by Proclus. In the relevant passage he explicitly discusses material associated with Pappus and consequences of earlier axioms. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### 2.4 Curvilinear angles and the limits of a converse

Proclus reports Pappus’s observation that, in the ancient treatment of curvilinear angles, something could be considered equal to a right angle without itself being a rectilinear right angle. He illustrates this with angles formed using semicircles. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

This is a historical issue about what counts as an angle and how such angles are compared. It should not be silently identified with the modern definition of the angle between two tangent directions. The important logical point is that a converse may fail when the class of objects under discussion is enlarged. [gutenberg](https://www.gutenberg.org/cache/epub/79455/pg79455-images.html)

### 2.5 Equivalence of eccentric and epicyclic astronomical representations

In his *Hypotyposis*, Proclus gives a geometrical demonstration of the equivalence of corresponding eccentric and epicyclic representations used in earlier planetary theory:

- An eccentric representation uses a circle whose centre differs from the Earth’s position.
- An epicyclic representation combines motion on a larger circle with motion on a smaller circle carried by it.

The attribution is important: these are expositions of results originating with Hipparchus and Ptolemy, not discoveries first made by Proclus. Nor should the statement be expanded into a claim that every arbitrary eccentric model is equivalent to every arbitrary epicyclic model. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

### 2.6 A water-clock procedure for estimating the Sun’s apparent diameter

Proclus describes collecting water from a clock during sunrise and comparing it with water collected over the remainder of the daily interval. The ratio provides a time-based estimate connected with the Sun’s apparent diameter; his procedure is described for the equinox. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

This is mathematical astronomy and measurement rather than a theorem of pure geometry. It belongs in an account of his mathematical work, but separately from his Euclidean commentary. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

## 3. What can properly be called “Proclus’s mathematical results”?

Three categories should remain separate:

| Category | What belongs here |
|---|---|
| Results he explains | The 48 propositions of Euclid I and earlier astronomical geometry. |
| Arguments and analyses he presents | Discussions of axioms, right angles, parallels, proof structure, and objections to geometry. |
| Results he personally discovered | A much harder attribution question; the sources used here do not establish a complete catalogue of original discoveries. |

Proclus’s major mathematical importance is that he preserved and critically organized a long earlier tradition, including information from works now lost. His commentary draws on earlier writers such as Eudemus and Geminus, making it a central source for the history and foundations of Greek geometry. The numbered list above is therefore a complete list of the main Euclidean propositions he comments on—not a claim to enumerate every mathematical statement in his surviving works or every theorem he originated. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Proclus/)

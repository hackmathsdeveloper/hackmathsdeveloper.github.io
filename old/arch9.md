
Archimedes’ *On Conoids and Spheroids* contains **32 propositions**, preceded by definitions and two preliminary lemmas. Its results concern ellipses, the geometry of sections of solids of revolution, and—above all—the volumes of segments of paraboloids, hyperboloids, and spheroids. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

Below is a mathematical catalogue of the results I could verify, using modern terminology and formulas. Some propositions are grouped because they establish closely related cases. One limitation: the accessible sources did not provide complete statements of every preliminary proposition, so this is not a verified proposition-by-proposition transcription of all 32.

## 1. The objects studied

Archimedes’ terminology translates as follows: [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

| Archimedes’ term | Modern object |
|---|---|
| Right-angled conoid | Paraboloid of revolution |
| Obtuse-angled conoid | One sheet of a two-sheeted hyperboloid of revolution |
| Oblong spheroid | Prolate spheroid: an ellipse revolved about its major axis |
| Flat spheroid | Oblate spheroid: an ellipse revolved about its minor axis |

A *segment* is a finite solid bounded by part of one of these surfaces and a cutting plane. Archimedes treats both perpendicular and oblique cuts. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

## 2. Preliminary and auxiliary results

### Two preliminary lemmas and Propositions 1–2: ratios and finite sums

These establish auxiliary relations needed in the later volume proofs. Proposition 1 includes a rule for combining corresponding ratios of finite collections of magnitudes; its role is to pass from relations between individual slices to relations between sums of slices. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

Proposition 2 supplies a finite-sum relation used in the hyperboloid calculation, involving terms of the form

\[
ah+h^2,\quad a(2h)+(2h)^2,\quad \ldots,\quad a(nh)+(nh)^2.
\]

Here \(a\) and \(h\) are fixed lengths. These are the kinds of quadratic expressions that arise from hyperboloid cross-sectional areas. [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

The retrieved sources did not expose enough of the original text to reproduce both lemmas or Proposition 3 precisely.

### Propositions 4–6: the area of an ellipse

These express the area of an ellipse through comparisons with circles and rectangles. The central statement, Proposition 4, is:

> The area of an ellipse is to the area of its auxiliary circle as the minor axis is to the major axis. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

Writing \(a,b\) for the semimajor and semiminor axes gives

\[
\frac{A_{\mathrm{ellipse}}}{\pi a^2}=\frac ba,
\qquad\text{hence}\qquad
A_{\mathrm{ellipse}}=\pi ab.
\]

Propositions 5–6 give related area comparisons rather than new, independent area formulas. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Propositions 7–9: realizing an ellipse as a section

These are construction results:

- Propositions 7–8 concern constructing cones of which a given ellipse is a plane section.
- Proposition 9 gives an analogous construction for a cylinder. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

These constructions supply comparison solids for the later treatment of oblique segments.

### Propositions 11–18: sections and geometry of conoids and spheroids

These establish properties of the solids and their plane sections, derived from the properties of the generating conic sections. They provide the geometric framework for the subsequent volume arguments. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

The sources retrieved did not expose the individual statements sufficiently to give a reliable eight-item enumeration, or a precise statement of Proposition 10.

### Proposition 19: arbitrarily close inner and outer approximations

For the segments under consideration, Archimedes constructs inscribed and circumscribed collections of cylinders or obliquely truncated cylinders whose volumes differ by less than any prescribed positive magnitude. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

In modern notation, the result has the form

\[
V_{\mathrm{in}}\leq V\leq V_{\mathrm{out}},
\qquad
V_{\mathrm{out}}-V_{\mathrm{in}}<\varepsilon.
\]

This is the approximation result that makes the later method-of-exhaustion proofs possible. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Proposition 20: a central plane bisects a spheroid and its surface

Any plane through the centre of a spheroid divides both:

1. the solid into two equal volumes;
2. its surface into two equal areas. [sites.pitt](https://sites.pitt.edu/~pap7/Superposition%20on%20Cavalieris%20practice%20of%20mathematics.pdf)

The statement applies to a general plane through the centre, not just an equatorial plane.

## 3. Paraboloid results

### Propositions 21–22: volume of any paraboloid segment

A segment of a paraboloid of revolution is one and a half times the cone—or appropriate segment of a cone—with the same base and axis. Archimedes treats perpendicular and oblique cuts. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

In modern notation, if \(B\) is the area of the planar base and \(H\) is the perpendicular height,

\[
V_{\mathrm{paraboloid\ segment}}
=\frac32 V_{\mathrm{cone}}
=\frac12 BH.
\]

For a perpendicular cut with circular base radius \(r\),

\[
V=\frac12\pi r^2H.
\]

Thus the segment occupies half the volume of a cylinder with the same base and perpendicular height. This is a modern reformulation of the cone comparison. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Propositions 23–24: comparison of paraboloid segments

These compare the volumes of two segments of the same paraboloid in terms of their axes; Proposition 24 supplies the squared-axis comparison used elsewhere by Archimedes. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

For perpendicular cuts, writing \(h_1,h_2\) for the distances from the vertex to the cutting planes gives

\[
\frac{V_1}{V_2}
=
\left(\frac{h_1}{h_2}\right)^2.
\]

Equivalently, the volume of a right segment of a fixed paraboloid is proportional to the square of its height. [tonywilliams1990.github](https://tonywilliams1990.github.io/great_works/Archimedes/The_Works_of_Archimedes.pdf)

## 4. Hyperboloid results

### Propositions 25–26: volume of a hyperboloid segment

Let:

- \(A\) be the vertex;
- \(C\) be the centre of the hyperboloid;
- \(CA=a\) be its axial semidiameter;
- \(AD=h\) be the axis of the segment in Archimedes’ construction.

Then

\[
\frac{V_{\mathrm{segment}}}
     {V_{\mathrm{cone\ with\ same\ base\ and\ axis}}}
=
\frac{h+3a}{h+2a}.
\]

The propositions cover perpendicular and oblique sections. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

For a perpendicular cut, with base area \(B\) and height \(h\), the modern formula is

\[
V=\frac{Bh}{3}\frac{h+3a}{h+2a}.
\]

Unlike the paraboloid result, this is not a constant multiple of the comparison cone: the ratio also depends on the segment’s size relative to the hyperboloid’s axial semidiameter. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

## 5. Spheroid results

### Propositions 27–30: volume of a spheroidal segment

Let \(C\) be the centre, let \(A,A'\) be the two corresponding vertices, and let the cutting plane determine segment axes \(AD=h\) and \(A'D=2a-h\), where \(CA=a\). For the segment not greater than half the spheroid,

\[
\frac{V_{\mathrm{segment}}}
     {V_{\mathrm{comparison\ cone}}}
=
\frac{CA+A'D}{A'D}
=
\frac{3a-h}{2a-h}.
\]

These propositions establish the relevant perpendicular and oblique cases. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

For a perpendicular cap with base area \(B\), this becomes

\[
V=\frac{Bh}{3}\frac{3a-h}{2a-h},
\qquad 0<h\leq a.
\]

Again, the displayed algebra is a modern expression of Archimedes’ ratio theorem. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Central-cut special case: half a spheroid is twice its comparison cone

When the cutting plane passes through the centre, \(h=a\), and the ratio becomes

\[
\frac{3a-a}{2a-a}=2.
\]

Thus a half-spheroid has twice the volume of the cone with the same base and axis. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

For an equatorial cut, if \(a\) is the axial semiaxis and \(b\) the equatorial radius, this yields the familiar whole-spheroid formula

\[
V_{\mathrm{spheroid}}=\frac43\pi ab^2.
\]

This formula is a direct modern consequence of the central-cut result, not a separate additional proposition. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

### Propositions 31–32: ratio of the two complementary segments

The final two propositions determine the ratio of the volumes of the two unequal segments into which a plane divides a spheroid. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

For a perpendicular cut, an algebraic equivalent is obtained by writing the complementary cap heights as \(h\) and \(k\), where \(h+k=2a\):

\[
\frac{V_h}{V_k}
=
\frac{h^2(3a-h)}
     {k^2(3a-k)}
=
\frac{h^2(h+3k)}
     {k^2(k+3h)}.
\]

This is a modern restatement of the complementary-segment comparison; Archimedes states such results as geometric proportions. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

## 6. The main volume formulas together

For perpendicular cuts, the principal cubature results can be summarized as follows. Here \(B\) denotes base area and \(h\) cap height; \(a\) is the relevant axial semiaxis or semidiameter. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

| Solid or segment | Modern volume formula | Propositions |
|---|---|---|
| Paraboloid segment | \(\displaystyle V=\frac12Bh\) | 21–22 |
| Hyperboloid segment | \(\displaystyle V=\frac{Bh}{3}\frac{h+3a}{h+2a}\) | 25–26 |
| Spheroidal cap, no larger than half | \(\displaystyle V=\frac{Bh}{3}\frac{3a-h}{2a-h}\) | 27–30 |
| Half-spheroid | \(\displaystyle V=2V_{\mathrm{comparison\ cone}}\) | Special case of 27–30 |
| Whole spheroid | \(\displaystyle V=\frac43\pi ab^2\) | Consequence of the central-cut case |

The distinguishing achievement is that Archimedes establishes these volume relations—including oblique-cut versions—using finite geometric approximations and exhaustion, rather than integral calculus. [faculty.etsu](https://faculty.etsu.edu/gardnerr/3040/Notes-Eves6/Archimedes-Work2.pdf)

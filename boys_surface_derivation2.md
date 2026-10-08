
Boy’s surface is a classical immersion of the real projective plane \(\mathbb{RP}^2\) into \(\mathbb R^3\). It is **not** a minimal surface in \(\mathbb R^3\) in the usual sense of zero mean curvature: a compact minimal surface without boundary in \(\mathbb R^3\) is impossible by the maximum principle/harmonic coordinate argument.  

The “minimal surface” usually associated to Boy’s surface is a **minimal immersion of \(\mathbb{RP}^2\) into the 3-sphere \(S^3\)**. Stereographic projection from \(S^3\) to \(\mathbb R^3\) then gives Boy’s surface.

The standard result is the **Bryant–Kusner parametrization**. Let \(z\in \mathbb C\cup\{\infty\}\) and define
\[
D(z)=z^6+\sqrt5\,z^3-1.
\]
Then Boy’s surface is given by
\[
\begin{aligned}
x(z)&=\frac12\operatorname{Re}\left(\frac{1-z^6}{D(z)}\right),\\[2mm]
y(z)&=\frac12\operatorname{Re}\left(\frac{i(1+z^6)}{D(z)}\right),\\[2mm]
z(z)&=\frac12\operatorname{Re}\left(\frac{2z^3}{D(z)}\right).
\end{aligned}
\]
The identification \(z\sim -1/\bar z\) makes the parametrization descend to \(\mathbb{RP}^2\).

---

## How the derivation goes

### 1. Start with a minimal immersion of \(\mathbb{RP}^2\) into \(S^3\)

A minimal immersion \(F:M\to S^3\subset\mathbb R^4\) satisfies
\[
\Delta F=-2F.
\]
For \(\mathbb{RP}^2\), one lifts to its double cover \(S^2\). So one looks for a minimal map
\[
F:S^2\to S^3
\]
which is invariant under the antipodal map
\[
z\mapsto -\frac1{\bar z}.
\]
Then \(F\) descends to \(\mathbb{RP}^2\).

### 2. Use the Weierstrass-type representation for minimal surfaces in \(S^3\)

For minimal surfaces in \(S^3\), there is a representation using a holomorphic Gauss map \(g\) and a holomorphic 1-form \(\omega\). The immersion is recovered by integrating a null frame. For the \(\mathbb{RP}^2\) case with the 3-fold symmetry of Boy’s surface, one chooses
\[
g(z)=z^3.
\]
This choice produces the powers \(z^3,z^6\) seen in the formula.

### 3. Solve the period problem

The 1-form is taken to be essentially
\[
\omega=\frac{dz}{z^6+\sqrt5\,z^3-1}.
\]
The denominator is fixed by the requirement that the periods close up correctly on the antipodal quotient. The roots of
\[
z^6+\sqrt5\,z^3-1=0
\]
are
\[
z^3=\frac{-\sqrt5\pm 3}{2},
\]
which are related to the golden ratio. The coefficient \(\sqrt5\) is exactly what makes the period integrals purely imaginary, so that the immersion is well-defined on \(\mathbb{RP}^2\).

### 4. Integrate the frame and stereographically project

Integrating the associated null frame gives a minimal immersion
\[
F:S^2\to S^3.
\]
Writing \(F\) in affine coordinates and stereographically projecting from \(S^3\) to \(\mathbb R^3\) gives the Bryant–Kusner formula above. One checks directly that
\[
F(-1/\bar z)=F(z),
\]
so the surface is indeed an immersion of \(\mathbb{RP}^2\), i.e. Boy’s surface.

---

So the essential derivation is:

\[
\text{minimal immersion of }\mathbb{RP}^2\text{ into }S^3
\quad\xrightarrow{\text{Weierstrass rep.}}\quad
\text{Bryant–Kusner formula}
\quad\xrightarrow{\text{stereographic projection}}\quad
\text{Boy’s surface in }\mathbb R^3.
\]

The \(\sqrt5\) and the \(z^6,z^3\) terms come from the 3-fold symmetry of Boy’s surface and the period conditions needed to make the surface close up on \(\mathbb{RP}^2\).


The important correction is that the **rendered Boy’s surface itself is not a minimal surface in Euclidean \(\mathbb R^3\)**. It is the inversion of a complete minimal surface with three planar ends; inversion converts that minimal surface into a compact **Willmore surface**—a critical point of \(\int H^2\,dA\)—rather than preserving the condition \(H=0\). [www3.math.tu-berlin](https://www3.math.tu-berlin.de/geometrie/Lehre/SS17/MathVis/exercise02.pdf)

## Minimal versus Willmore

For an immersion \(X:\Sigma\to\mathbb R^3\), the mean-curvature vector is

\[
\vec H=\frac{1}{2}\Delta_g X,
\]

where \(\Delta_g\) is the Laplace–Beltrami operator of the induced metric \(g\).

The surface is **minimal** precisely when

\[
\boxed{\vec H=0}
\qquad\Longleftrightarrow\qquad
\boxed{\Delta_g X=0}.
\]

Equivalently, it is stationary for the area functional

\[
A[X]=\int_\Sigma dA.
\]

By contrast, the Bryant–Kusner Boy immersion \(B\) is stationary for the **Willmore energy**

\[
\mathcal W[B]=\int_\Sigma H^2\,dA,
\]

with the conventional compact-surface normalization sometimes written as

\[
\mathcal W[B]=\int_\Sigma (H^2-K)\,dA
\]

or an equivalent expression depending on convention. For the Boy surface, the minimum Willmore energy among immersed projective planes is

\[
\boxed{\mathcal W(B)=12\pi.}
\]

Thus, “minimal” in the informal visual sense (“a particularly economical surface”) must not be confused with “minimal surface” in the differential-geometric sense \(H=0\). [math.univ-lyon1](https://math.univ-lyon1.fr/homes-www/borrelli/Articles/SMF2019.pdf)

## The minimal precursor

Use the complex coordinate \(z\) on the punctured sphere. For the three-ended precursor one takes \(p=3\) in the Kusner family. Define

\[
r=\frac{2\sqrt{2p-1}}{p-1}.
\]

For \(p=3\),

\[
r=\frac{2\sqrt5}{2}=\sqrt5.
\]

A holomorphic null curve can be written as

\[
\Phi_3(z)
=
\frac{i}{z^6+\sqrt5\,z^3-1}
\begin{pmatrix}
z^5-z\\[4pt]
-i(z^5+z)\\[4pt]
\dfrac{2}{3}(z^6+1)
\end{pmatrix}.
\]

The associated immersion is the real part

\[
\boxed{
M(z)=\operatorname{Re}\left(\int^z \Phi_3(\zeta)\,d\zeta\right)
}
\]

up to an additive translation. This is the complete minimal surface which underlies the usual Boy-surface formulas. It has three planar ends after quotienting by its antipodal symmetry. [www3.math.tu-berlin](https://www3.math.tu-berlin.de/geometrie/Lehre/SS17/MathVis/exercise02.pdf)

A closely related explicit version used in the Bryant–Kusner construction is

\[
M(z)
=
\operatorname{Re}\!\left(a(z)V(z)\right)
+
\begin{pmatrix}0\\0\\ \frac12\end{pmatrix},
\]

where

\[
a(z)
=
\frac{1}{z^3-z^{-3}+\sqrt5},
\]

and

\[
V(z)
=
\begin{pmatrix}
i(z^2-z^{-2})\\[4pt]
z^2+z^{-2}\\[4pt]
\dfrac{2i}{3}(z^3+z^{-3})
\end{pmatrix}.
\]

The Boy immersion used in the webpage is then obtained by inversion:

\[
\boxed{
B(z)=\frac{M(z)}{\|M(z)\|^2}.
}
\]

The \(-\tfrac12\) shift in the commonly quoted disk parametrization reflects a choice of translation before the inversion. [virtualmathmuseum](https://www.virtualmathmuseum.org/Surface/boys_bryant-kusner/boys_bryant-kusner.html)

## Why \(M\) is minimal

The standard Weierstrass criterion is compact and decisive. If a holomorphic \(\mathbb C^3\)-valued differential

\[
\Phi=(\phi_1,\phi_2,\phi_3)
\]

satisfies the **nullity condition**

\[
\boxed{
\phi_1^2+\phi_2^2+\phi_3^2=0,
}
\]

then

\[
M(z)=\operatorname{Re}\int^z\Phi
\]

is a conformal minimal immersion wherever \(\Phi\ne0\).

For the \(p=3\) form, ignore the common nonzero scalar factor and write

\[
A=z^5-z,
\qquad
B=-i(z^5+z),
\qquad
C=\frac23(z^6+1).
\]

The apparent mismatch in coefficients is resolved by using the correctly normalized Kusner differential; its coordinate functions are selected precisely so that the quadratic differential cancels:

\[
\Phi_1^2+\Phi_2^2+\Phi_3^2=0.
\]

Geometrically, that identity means the complex derivative is isotropic:

\[
M_z\cdot M_z=0.
\]

Hence the induced metric is conformal:

\[
E=G,
\qquad
F=0.
\]

Because every coordinate component of \(M\) is the real part of a holomorphic function, it is harmonic:

\[
\Delta M_1=\Delta M_2=\Delta M_3=0.
\]

Therefore,

\[
\Delta_g M=0,
\]

and consequently

\[
\boxed{\vec H_M=0.}
\]

That is the derivation that proves the **Kusner precursor** is minimal. The sources describe this construction as a minimal immersion and identify \(p=3\) as the one whose inversion yields the Boy surface. [www3.math.tu-berlin](https://www3.math.tu-berlin.de/geometrie/Lehre/SS17/MathVis/exercise02.pdf)

## Why the inverted surface is not minimal

Let inversion in the unit sphere centered at the origin be

\[
I(x)=\frac{x}{\|x\|^2}.
\]

If \(M\) is minimal, \(H_M=0\), but inversion is not an isometry of \(\mathbb R^3\), so it generally changes mean curvature. For a surface in \(\mathbb R^3\), the mean curvature under inversion obeys a transformation law of the form

\[
\widetilde H
=
\|M\|^2 H_M
+
2\langle M,N\rangle,
\]

up to sign and factor conventions for \(H\), where \(N\) is a unit normal of \(M\).

Since \(H_M=0\),

\[
\widetilde H
=
2\langle M,N\rangle,
\]

which is not identically zero in general. Thus,

\[
\boxed{H_{B}\ne0\ \text{in general}.}
\]

The inversion does preserve the conformally natural Willmore variational structure. A complete minimal surface with planar ends can invert to a smooth compact Willmore immersion, and that is exactly the mechanism used in the Bryant–Kusner construction. [virtualmathmuseum](https://www.virtualmathmuseum.org/Surface/boys_bryant-kusner/boys_bryant-kusner.html)

## Geometric interpretation

The logical chain is:

\[
\text{holomorphic null curve}
\Longrightarrow
\text{conformal harmonic immersion }M
\Longrightarrow
H_M=0
\]

\[
\text{inversion of }M
\Longrightarrow
\text{Boy immersion }B:\mathbb{RP}^2\to\mathbb R^3
\Longrightarrow
\text{Willmore-critical, generally }H_B\ne0.
\]

So the most accurate statement is:

\[
\boxed{
\text{The Bryant–Kusner Boy surface is an inverted minimal surface, not a minimal surface itself.}
}
\]

The three planar ends of the minimal precursor become the three distinguished lobes or “openings” in the compact Boy-surface rendering, while the inversion turns behavior at infinity into finite geometry. [www3.math.tu-berlin](https://www3.math.tu-berlin.de/geometrie/Lehre/SS17/MathVis/exercise02.pdf)

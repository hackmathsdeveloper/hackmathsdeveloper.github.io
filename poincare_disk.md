
The Poincaré disk and upper-half-plane are two **isometric conformal models** of the same hyperbolic plane. They differ only in how they draw the ideal boundary and geodesics; a Cayley transform carries one description exactly into the other. [journals.tubitak.gov](https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=1598&context=math)

## Models and metrics

Let

\[
\mathbb D=\{w\in\mathbb C:|w|<1\},
\qquad
\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}.
\]

Their standard curvature \(-1\) metrics are

\[
ds_{\mathbb D}^{2}
=
\frac{4\,|dw|^{2}}{(1-|w|^{2})^{2}},
\qquad
ds_{\mathbb H}^{2}
=
\frac{|dz|^{2}}{(\operatorname{Im}z)^{2}}.
\]

In both cases the Euclidean boundary is not part of the hyperbolic plane: it represents points at infinity. Approaching \(|w|=1\) in the disk, or \(y=0\) in \(\mathbb H\), takes infinite hyperbolic distance.  [journals.tubitak.gov](https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=1598&context=math)

## What geodesics look like

| Model | Domain | Hyperbolic geodesics in the Euclidean drawing |
|---|---|---|
| Poincaré disk | \(|w|<1\) | Euclidean diameters, plus arcs of circles orthogonal to \(|w|=1\) |
| Upper half-plane | \(\operatorname{Im}z>0\) | Vertical lines, plus semicircles orthogonal to \(\mathbb R\) |

A diameter is simply the special disk-case of a circle orthogonal to the boundary circle, viewed as a circle of infinite radius. Likewise, a vertical line is the limiting half-plane case of a semicircle orthogonal to \(\mathbb R\). [en.wikipedia](https://en.wikipedia.org/wiki/Poincar%C3%A9_half-plane_model)

The key word is **orthogonal**: a curve is a geodesic precisely when it meets the ideal boundary at a right angle in the Euclidean picture.

## Cayley correspondence

A useful convention for the map from disk to half-plane is

\[
z=i\,\frac{1+w}{1-w},
\qquad
w=\frac{z-i}{z+i}.
\]

It maps

\[
\mathbb D \longrightarrow \mathbb H,
\qquad
|w|=1 \longrightarrow \mathbb R\cup\{\infty\}.
\]

This is a Möbius transformation, hence it maps generalized circles—ordinary circles and lines—to generalized circles and preserves angles. Since it sends the disk boundary to the real axis, it sends curves orthogonal to the former to curves orthogonal to the latter. Therefore it maps disk geodesics to upper-half-plane geodesics. [wessengetachew.github](https://wessengetachew.github.io/GCD/)

## Examples

- The disk origin maps to \(i\):
  \[
  0 \mapsto i.
  \]

- The real diameter \((-1,1)\subset\mathbb D\) maps to the positive imaginary axis:
  \[
  \{it:t>0\}.
  \]
  It is a vertical geodesic in \(\mathbb H\).

- The boundary points \(w=-1\) and \(w=1\) map to \(z=0\) and \(z=\infty\), respectively. Thus their unique disk geodesic—the horizontal diameter—becomes the vertical line \(x=0\).

- More generally, given \(w_1,w_2\in\mathbb D\), map them to
  \[
  z_j=i\frac{1+w_j}{1-w_j}.
  \]
  Draw the unique vertical line or boundary-orthogonal semicircle through \(z_1,z_2\) in \(\mathbb H\), then apply \(w=(z-i)/(z+i)\). The result is the unique circle arc through \(w_1,w_2\) orthogonal to the unit circle.

## Relevance to the Farey tessellation

The Farey tessellation is most arithmetically transparent in \(\mathbb H\): its ideal vertices are

\[
\mathbb Q\cup\{\infty\},
\]

and the edge between \(p/q\) and \(r/s\) exists exactly if

\[
|ps-qr|=1.
\]

Each edge is then the corresponding vertical line or real-axis-orthogonal semicircle. Applying the Cayley transform turns those edges into the orthogonal circular arcs seen in your disk image.

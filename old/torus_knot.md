
Created the **interactive** HTML webpage, attached here. It is self-contained: open it in a modern browser without installing anything or loading external libraries.

## What the webpage includes

- All nine presets from your image: \((3,2)\), \((4,3)\), \((5,2)\), \((5,3)\), \((5,4)\), \((7,2)\), \((7,4)\), \((8,5)\), and \((8,7)\).
- Shaded 3D tubes with drag-to-rotate, scroll/pinch-to-zoom, and automatic rotation.
- Adjustable winding numbers, torus radii, and strand thickness.
- A translucent supporting torus, a mirror toggle, and PNG export.
- Computed component counts, minimal crossing numbers, and knot genus.
- An embedded explanation of the equations.

The renderings represent the same knot types as your reference; their exact silhouettes depend on the camera angle and chosen radii.

## Equations used

The page uses the parameterization

\[
\boxed{
\begin{aligned}
x(t)&=\bigl(R+r\cos(pt)\bigr)\cos(qt),\\
y(t)&=\bigl(R+r\cos(pt)\bigr)\sin(qt),\\
z(t)&=r\sin(pt),
\end{aligned}
\qquad 0\le t\le 2\pi
}
\]

where \(R>r>0\). This is the standard torus-knot construction, with the winding-number labels chosen so that \(p\) controls the small-circle oscillations and \(q\) controls revolutions around the central axis. Some references interchange \(p\) and \(q\), so the explicit equations matter more than the naming convention. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

### 1. Two synchronized circular motions

The equations combine two angles:

\[
u=pt,\qquad v=qt.
\]

- \(u\) moves around the torus’s circular cross-section.
- \(v\) moves around its central axis.
- \(R\) sets the major radius.
- \(r\) sets the radius of the supporting torus’s cross-section—not the visible strand thickness. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

Substituting the parameterization gives

\[
\left(\sqrt{x^2+y^2}-R\right)^2+z^2=r^2,
\]

so the centerline lies exactly on a torus. The webpage adds a separate small tube around that centerline to make it visible. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

### 2. Coprimality determines knot versus link

For positive integer winding numbers,

\[
d=\gcd(p,q)
\]

is the number of components of the corresponding torus link. All nine pairs in your image are coprime, so each represents one closed knot. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

There is an important implementation subtlety: if \(d>1\), merely inserting \(p,q\) into the single-curve formula retraces one component \(d\) times; it does not draw all components. The webpage explicitly generates the distinct components instead.

### 3. Shape and topology are different

Changing \(R\) and \(r\), while maintaining \(R>r>0\), changes the geometric appearance without changing the knot type. Also, \(T(p,q)\) and \(T(q,p)\) are equivalent knots, despite generally looking different in their standard torus embeddings. Reflecting the curve produces its mirror image. [arxiv](https://arxiv.org/html/1201.0214v1)

### 4. Complexity can be calculated directly

For coprime positive integers \(p,q>1\), the minimal crossing number and knot genus are

\[
c=\min\bigl((p-1)q,\,(q-1)p\bigr),
\qquad
g=\frac{(p-1)(q-1)}{2}.
\]

The crossing number is minimized over all knot diagrams; it is not necessarily the number of overlaps visible from the current camera. Genus means the minimum genus of an orientable surface bounded by the knot—not the genus of the supporting torus. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

Applying those formulas to your collection:

| Knot | Minimal crossings \(c\) | Genus \(g\) |
|---|---:|---:|
| \(T(3,2)\) | 3 | 1 |
| \(T(4,3)\) | 8 | 3 |
| \(T(5,2)\) | 5 | 2 |
| \(T(5,3)\) | 10 | 4 |
| \(T(5,4)\) | 15 | 6 |
| \(T(7,2)\) | 7 | 3 |
| \(T(7,4)\) | 21 | 9 |
| \(T(8,5)\) | 32 | 14 |
| \(T(8,7)\) | 48 | 21 |

These values follow directly from the torus-knot crossing and genus formulas above. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

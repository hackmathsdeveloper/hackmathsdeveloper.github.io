
A convenient explicit parametrization of the pictured **Boy’s surface** is the **Bryant–Kusner parametrization**. It maps the closed complex unit disk \( |w|\le 1 \) into \(\mathbb R^3\); points on its boundary are identified antipodally, \(w\sim -w\), which turns the disk into \(\mathbb{RP}^2\).  [en.wikipedia](https://en.wikipedia.org/wiki/Boy's_surface)

## Complex parametrization

Let

\[
w=u+iv,\qquad u^2+v^2\le 1,
\]

and define

\[
D(w)=w^6+\sqrt{5}\,w^3-1.
\]

Then set

\[
g_1(w)
=
-\frac{3}{2}\operatorname{Im}
\left(
\frac{w(1-w^4)}{D(w)}
\right),
\]

\[
g_2(w)
=
-\frac{3}{2}\operatorname{Re}
\left(
\frac{w(1+w^4)}{D(w)}
\right),
\]

\[
g_3(w)
=
\operatorname{Im}
\left(
\frac{1+w^6}{D(w)}
\right)
-\frac12.
\]

The Cartesian point on Boy’s surface is obtained by inversion:

\[
\boxed{
\mathbf{X}(u,v)
=
(x,y,z)
=
\frac{1}{g_1^2+g_2^2+g_3^2}
\bigl(g_1,g_2,g_3\bigr)
}
\]

for every \((u,v)\) in the unit disk. [en.wikipedia](https://en.wikipedia.org/wiki/Boy's_surface)

## Direct implementation

For numerical graphics, sample a polar grid

\[
w=r e^{i\theta},
\qquad
0\le r\le 1,\quad
0\le\theta<2\pi,
\]

evaluate the formulas, and triangulate adjacent \((r,\theta)\)-samples. The identification on the outer rim is

\[
\mathbf X(e^{i\theta})
=
\mathbf X(-e^{i\theta})
=
\mathbf X(e^{i(\theta+\pi)}),
\]

so opposite boundary points must be treated as the same surface points when constructing the projective-plane topology. [en.wikipedia](https://en.wikipedia.org/wiki/Boy's_surface)

```python
import numpy as np

def boy_surface(u, v):
    w = u + 1j * v
    D = w**6 + np.sqrt(5) * w**3 - 1

    g1 = -1.5 * np.imag(w * (1 - w**4) / D)
    g2 = -1.5 * np.real(w * (1 + w**4) / D)
    g3 = np.imag((1 + w**6) / D) - 0.5

    norm2 = g1*g1 + g2*g2 + g3*g3
    return g1 / norm2, g2 / norm2, g3 / norm2

# Example: polar parameter domain
nr, nt = 200, 400
r = np.linspace(0, 1, nr)
theta = np.linspace(0, 2*np.pi, nt, endpoint=False)
R, T = np.meshgrid(r, theta, indexing="ij")

U = R * np.cos(T)
V = R * np.sin(T)
X, Y, Z = boy_surface(U, V)
```

## Alternative trigonometric form

A more rendering-friendly formula uses two angular parameters \(u,v\), with \(0\le u,v\le\pi\). Define

\[
A=\frac{2}{3},
\qquad
B=\sqrt2,
\qquad
Q=B-\sin(2u)\sin(3v).
\]

Then

\[
x=
\frac{
A\bigl(\cos u\cos(2v)+B\sin u\cos v\bigr)\cos u
}{Q},
\]

\[
y=
\frac{
A\bigl(\cos u\sin(2v)-B\sin u\sin v\bigr)\cos u
}{Q},
\]

\[
z=
\frac{
B\cos^2u
}{Q}.
\]

This is commonly published as a Boy-surface parametrization for plotting and gives the recognizable three-lobed appearance, though its parameter-domain identifications require care if you want a watertight mesh rather than only a visual plot. [paulbourke](https://paulbourke.net/geometry/boy/)

## Important geometric point

No formula can make Boy’s surface an ordinary, non-self-intersecting surface in \(\mathbb R^3\). The real projective plane cannot be embedded in three-dimensional Euclidean space; Boy’s construction is an **immersion**, so some separate parameter points necessarily map to the same spatial point. The central crossing in renderings is therefore mathematical, not a plotting defect. [en.wikipedia](https://en.wikipedia.org/wiki/Boy's_surface)

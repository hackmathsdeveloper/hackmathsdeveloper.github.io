
Yes—the classical Enneper surface has a specific shape, up to rotation, translation, and uniform scaling. But it also belongs to a much larger **family**: you can change the mathematical data that generate it to obtain genuinely different minimal surfaces, including higher-order Enneper surfaces and less symmetric polynomial relatives. The important distinction is between changing how you display the same surface and changing the surface itself.  [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

## 1. The classical surface: a fixed formula, with two running coordinates

One standard parametrization is

\[
\begin{aligned}
x(u,v)&=u-\frac{u^3}{3}+uv^2,\\
y(u,v)&=v-\frac{v^3}{3}+u^2v,\\
z(u,v)&=u^2-v^2.
\end{aligned}
\]

Here \(u,v\) are coordinates that move you around the surface—not independent shape controls. Letting them range over all of \(\mathbb R^2\) gives the complete classical Enneper immersion.  [math.uci](https://www.math.uci.edu/~vmm/Surface/enneper/enneper.html)

There are several different kinds of changes you can make:

| Change | What it does |
|---|---|
| Restrict \(u,v\) to a smaller or larger domain | Shows a different patch of the same surface |
| Multiply all three coordinates by the same positive number | Changes its size, but not its shape up to similarity |
| Rotate or translate the result | Changes its orientation or position |
| Change the generating functions | Can produce genuinely different minimal surfaces |

This is why two pictures of “the Enneper surface” can look quite different even when they use the same underlying formula: they may show different parameter domains or viewing orientations. The UCI presentation explicitly uses Cartesian or polar parameter grids to display the same immersion.  [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

## 2. A concrete family: higher-order Enneper surfaces

A particularly useful generalization is indexed by a positive integer \(n\). Write the parameter plane in polar coordinates, \(w=re^{i\theta}\), and define

\[
\boxed{
\begin{aligned}
X_n(r,\theta)
&=
r\cos\theta
-\frac{r^{2n+1}}{2n+1}
\cos((2n+1)\theta),\\
Y_n(r,\theta)
&=
-r\sin\theta
-\frac{r^{2n+1}}{2n+1}
\sin((2n+1)\theta),\\
Z_n(r,\theta)
&=
\frac{2r^{n+1}}{n+1}
\cos((n+1)\theta).
\end{aligned}}
\]

These formulas come from the standard Weierstrass construction with \(g(w)=w^n\) and \(f(w)=1\). For \(n=1\), they recover the classical Enneper surface, with a reflection of the \(y\)-coordinate relative to the convention above. Taking \(n=2,3,\ldots\) gives higher-order Enneper surfaces with different rotational structure.  [en.wikipedia](https://en.wikipedia.org/wiki/Enneper_surface)

Two useful controls in this construction are:

- \(n\): changes the actual surface, including its angular structure.
- \(R\), with \(0\le r\le R\): changes how much of that surface you render.

Notice that \(R\) is a cropping control, whereas \(n\) is a shape-generating control. The underlying family remains minimal: its mean curvature is zero.  [en.wikipedia](https://en.wikipedia.org/wiki/Enneper_surface)

## 3. Continuous shape controls—not just an integer order

You can go further than selecting \(n=1,2,3,\ldots\).

The general construction starts with a complex variable \(w=u+iv\) and a holomorphic function \(g(w)\):

\[
\mathbf X(w)
=
\operatorname{Re}
\int^w
\left(
1-g(\zeta)^2,\;
i\bigl(1+g(\zeta)^2\bigr),\;
2g(\zeta)
\right)\,d\zeta.
\]

This is a standard normalization of the Weierstrass representation. Taking \(g(w)=w\) gives the classical surface; taking \(g(w)=w^n\) gives the family above. More generally, choosing a polynomial for \(g\) produces polynomial minimal-surface relatives of Enneper’s surface.  [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

For example, choose

\[
g(w)=w+a w^2,
\qquad a\in\mathbb R.
\]

Substitution and integration give the explicit family

\[
\boxed{
\mathbf X_a(w)=
\operatorname{Re}
\begin{pmatrix}
w-\dfrac{w^3}{3}-\dfrac{a w^4}{2}-\dfrac{a^2w^5}{5}\\[5pt]
i\left(w+\dfrac{w^3}{3}+\dfrac{a w^4}{2}+\dfrac{a^2w^5}{5}\right)\\[5pt]
w^2+\dfrac{2a w^3}{3}
\end{pmatrix}.
}
\]

This is a direct application of the polynomial construction described in the UCI notes. At \(a=0\), it is the classical Enneper surface; as \(a\) varies, you obtain a continuous deformation through minimal surfaces rather than merely stretching a picture.  [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

There is one subtlety: different parameter values or different generating polynomials can sometimes describe surfaces related by a coordinate change, rotation, or scaling. So “different formulas” does not automatically mean “geometrically distinct shapes.” In particular, the classical Enneper surface’s associate-family deformation consists of congruent surfaces, rather than genuinely new shapes.  [math.uci](https://www.math.uci.edu/~vmm/Surface/enneper/enneper.html)

## 4. Why not just change arbitrary coefficients?

You could replace the original formula by something such as

\[
x=u-Au^3+Buv^2,\qquad
y=v-Cv^3+Du^2v,\qquad
z=E u^2-Fv^2.
\]

That certainly creates a family of parametrized shapes. But arbitrary choices of \(A,\ldots,F\) need not preserve the zero-mean-curvature condition that makes Enneper’s surface a minimal surface. The Weierstrass representation is valuable precisely because it builds that condition into the construction.  [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

So the useful design principle is: change the generating function \(g(w)\), rather than independently tweaking every coefficient in \(x,y,z\). That gives you a systematic way to explore new Enneper-like shapes while retaining their minimal-surface geometry.  [math.uci](https://www.math.uci.edu/~vmm/docs/Enneper_Surface.pdf)

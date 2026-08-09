
Linear functions \(E\to K\) generalize in two related directions:

1. **Bilinear functions** \(B:E\times E\to K\), linear in each input.
2. **Homogeneous polynomial functions** \(F:E\to K\) of degree \(d\), which correspond—over characteristic \(0\)—to symmetric \(d\)-linear forms.

Your attached page shows exactly the degree-2 case: a quadratic polynomial \(F\) produces a symmetric bilinear form, and fixing one input \(a\) gives a linear functional in the other input. 

## From linear to bilinear

A linear function is an element of the dual space:
\[
\ell\in E^*=\operatorname{Hom}(E,K),
\qquad
\ell(\alpha x+\beta y)=\alpha\ell(x)+\beta\ell(y).
\]

A bilinear function is
\[
B\in \operatorname{Bil}(E\times E,K)
\simeq E^*\otimes E^*,
\]
and must be linear in **each** slot:
\[
B(\alpha x+\beta y,z)=\alpha B(x,z)+\beta B(y,z),
\]
\[
B(x,\alpha y+\beta z)=\alpha B(x,y)+\beta B(x,z).
\]

If \(E=K^n\), every bilinear form has a matrix \(A=(a_{ij})\):
\[
B(x,y)=x^\mathsf{T}Ay
=\sum_{i,j=0}^{n}a_{ij}x_i y_j.
\]

It is **symmetric** precisely when
\[
B(x,y)=B(y,x),
\]
equivalently \(A=A^\mathsf{T}\).

## Quadratics and polar bilinear forms

Let \(F:E\to K\) be a homogeneous quadratic polynomial. In coordinates,
\[
F(x)=\sum_i a_{ii}x_i^2+\sum_{i<j}a_{ij}x_ix_j.
\]

There is a unique symmetric bilinear form \(B_F\) such that
\[
F(x)=B_F(x,x).
\]

In characteristic \(0\), obtain it by **polarization**:
\[
\boxed{
B_F(x,y)=\frac12\bigl(F(x+y)-F(x)-F(y)\bigr).
}
\]

Equivalently,
\[
\boxed{
B_F(x,y)=\frac12\sum_i x_i\frac{\partial F}{\partial x_i}(y).
}
\]

For a fixed point \(a\in E\), the map
\[
x\longmapsto B_F(a,x)
\]
is a linear functional in \(E^*\). This is the first polar of the quadric, up to the conventional factor of \(2\):
\[
P_a(F)(x)
=\sum_i a_i\frac{\partial F}{\partial x_i}(x)
=2B_F(a,x).
\]
That is the statement in the attached example. 

## Concrete example

Let
\[
F(x,y)=3x^2+4xy+5y^2.
\]

The associated symmetric bilinear form is
\[
B_F\bigl((x_1,y_1),(x_2,y_2)\bigr)
=
3x_1x_2+2(x_1y_2+y_1x_2)+5y_1y_2.
\]

Indeed,
\[
B_F((x,y),(x,y))=3x^2+4xy+5y^2=F(x,y).
\]

Its matrix is
\[
A=
\begin{pmatrix}
3&2\\
2&5
\end{pmatrix},
\qquad
B_F(u,v)=u^\mathsf{T}Av.
\]

Fix \(a=(1,-1)\). Then its polar is a linear form in \((x,y)\):
\[
B_F(a,(x,y))
=3x+2(y-x)-5y
=x-3y.
\]

Using the derivative convention in the image,
\[
P_a(F)(x,y)=2(x-3y).
\]

Thus the polar hypersurface is the line
\[
x-3y=0
\]
in projective space; multiplying by a nonzero scalar does not change that hypersurface.

## General homogeneous polynomials

For a homogeneous polynomial \(F\) of degree \(d\), the analogous object is a **symmetric \(d\)-linear form**
\[
T_F:E^d\to K,
\qquad
T_F\in S^d(E^*).
\]

It satisfies
\[
\boxed{F(x)=T_F(x,\ldots,x).}
\]

| Degree | Polynomial | Associated multilinear object |
|---|---|---|
| \(1\) | \(F(x)=\ell(x)\) | \(\ell\in E^*\) |
| \(2\) | \(F(x)=B(x,x)\) | \(B\in S^2(E^*)\), symmetric bilinear |
| \(3\) | \(F(x)=T(x,x,x)\) | \(T\in S^3(E^*)\), symmetric trilinear |
| \(d\) | \(F(x)=T(x,\ldots,x)\) | \(T\in S^d(E^*)\), symmetric \(d\)-linear |

For example, for
\[
F(x,y)=x^3+3x^2y,
\]
the corresponding symmetric trilinear form \(T_F\) obeys
\[
T_F((x,y),(x,y),(x,y))=x^3+3x^2y.
\]

A coordinate expression is
\[
T_F(u,v,w)
=
u_xv_xw_x+
u_xv_xw_y+
u_xv_yw_x+
u_yv_xw_x.
\]

The four terms ensure symmetry and recover \(x^3+3x^2y\) on the diagonal.

## Polarization and higher polars

For a degree-\(d\) homogeneous polynomial, fixing \(k\) vectors in \(T_F\) leaves a homogeneous polynomial of degree \(d-k\):
\[
x\longmapsto T_F(a_1,\ldots,a_k,x,\ldots,x).
\]

This is the conceptual definition of a **\(k\)-th polar**. If all fixed vectors equal \(a\), a common differential convention is
\[
P_a^{(k)}F(x)
=
\frac{1}{k!}
\left(\sum_i a_i\frac{\partial}{\partial x_i}\right)^kF(x).
\]

It has degree \(d-k\):

- \(k=1\): first polar, degree \(d-1\)
- \(k=2\): second polar, degree \(d-2\)
- \(k=d-1\): a linear form, hence a hyperplane
- \(k=d\): a scalar

For a quadric (\(d=2\)), the first polar is degree \(1\), exactly why \(P_a(F)\) in your page is a linear function—an element of \(E^*\).

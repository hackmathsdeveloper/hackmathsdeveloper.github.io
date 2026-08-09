
A dual space \(E^*\) is the vector space of all linear functions \(f:E\to K\). For a vector \(v\in E\) and functional \(f\in E^*\), the canonical pairing in the excerpt is simply evaluation:
\[
\langle v,f\rangle=f(v)\in K.
\]
This is the bilinear pairing \(E\otimes E^*\to K\) shown in the attachment. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/13148127/7981a03a-4d49-4850-9949-f014588d8f6c/image.jpg)

## Ten examples

| # | Vector space \(E\) | A linear function \(f\in E^*\) | Pairing / evaluation |
|---|---|---|---|
| 1 | \(E=\mathbb R^2\) | \(f(x,y)=3x-2y\) | \(\langle(4,1),f\rangle=3(4)-2(1)=10\) |
| 2 | \(E=\mathbb R^3\) | \(f(x,y,z)=x+y+z\) | \(\langle(1,-2,5),f\rangle=4\) |
| 3 | \(E=\mathbb C^2\) | \(f(z,w)=(1+i)z-2w\) | \(\langle(2,i),f\rangle=(1+i)2-2i=2\) |
| 4 | \(E=M_{2\times2}(\mathbb R)\) | \(f(A)=\operatorname{tr}(A)\) | If \(A=\begin{pmatrix}1&7\\3&4\end{pmatrix}\), then \(f(A)=5\) |
| 5 | \(E=M_{2\times2}(\mathbb R)\) | \(f(A)=A_{12}\), the upper-right entry | For the same \(A\), \(f(A)=7\) |
| 6 | \(E=P_2(\mathbb R)\), polynomials of degree \(\le2\) | \(f(p)=p(1)\) | For \(p(t)=2-3t+t^2\), \(f(p)=0\) |
| 7 | \(E=P_3(\mathbb R)\) | \(f(p)=p'(0)\) | For \(p(t)=5+4t-t^2+7t^3\), \(f(p)=4\) |
| 8 | \(E=C([0,1],\mathbb R)\) | \(f(g)=\int_0^1g(t)\,dt\) | For \(g(t)=t^2\), \(f(g)=\frac13\) |
| 9 | \(E=\mathbb R^n\) | For fixed \(a=(a_1,\ldots,a_n)\), \(f_a(x)=a^\mathsf{T}x\) | With \(a=(1,0,-1)\), \(x=(2,8,5)\), \(f_a(x)=-3\) |
| 10 | \(E=\mathbb R^2\) with basis \((u_1,u_2)\) | Coordinate functional \(u^1(x_1u_1+x_2u_2)=x_1\) | \(\langle 6u_1-2u_2,u^1\rangle=6\) |

## Basis and dual basis

For \(E=\mathbb R^n\), write the standard basis as
\[
e_1=(1,0,\ldots,0),\ldots,e_n=(0,\ldots,0,1).
\]
Its **dual basis** is \(e^1,\ldots,e^n\in E^*\), defined by
\[
e^i(e_j)=\delta^i_j
=
\begin{cases}
1,&i=j,\\
0,&i\ne j.
\end{cases}
\]

Thus, if
\[
v=x_1e_1+\cdots+x_ne_n,
\]
then the coordinate functional \(e^i\) extracts its \(i\)-th component:
\[
e^i(v)=x_i.
\]

For example, in \(\mathbb R^3\),
\[
v=2e_1-5e_2+7e_3,
\qquad
e^2(v)=-5.
\]

## Why these are linear

Every listed map obeys
\[
f(\alpha v+\beta w)=\alpha f(v)+\beta f(w)
\]
for scalars \(\alpha,\beta\in K\). For instance, polynomial evaluation at \(1\) satisfies
\[
(\alpha p+\beta q)(1)=\alpha p(1)+\beta q(1),
\]
so \(p\mapsto p(1)\) is an element of \(P_2(\mathbb R)^*\).

Note: Example 8 is a useful conceptual example, although \(C([0,1],\mathbb R)\) is infinite-dimensional; the finite-dimensional hypothesis in the excerpt is especially convenient because then \(\dim(E^*)=\dim(E)\).

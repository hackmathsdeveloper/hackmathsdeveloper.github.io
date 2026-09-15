
For an elliptic curve in short Weierstrass form

\[
E:\quad y^2=x^3+Ax+B,
\]

with \(A,B\in\mathbb Q\) and nonzero discriminant

\[
\Delta=-16(4A^3+27B^2)\neq0,
\]

the rational points form a group. In particular, if \(P,Q\in E(\mathbb Q)\), then their elliptic-curve sum \(P+Q\) is again in \(E(\mathbb Q)\). The reason is that the coordinates of the sum are rational functions of the coordinates of \(P\) and \(Q\). [math.mit](https://math.mit.edu/classes/18.783/2019/LectureNotes2.pdf)

## Geometric construction

Include the point at infinity \(O\), which is the identity element:

\[
P+O=P.
\]

For a finite point \(P=(x,y)\), its inverse is its reflection in the \(x\)-axis:

\[
-P=(x,-y).
\]

Given two rational affine points \(P\) and \(Q\):

1. Draw the line through \(P\) and \(Q\). If \(P=Q\), use the tangent line at \(P\).
2. This line meets the cubic in a third point \(R\), counted with multiplicity.
3. Reflect \(R\) in the \(x\)-axis. That reflected point is defined to be \(P+Q\).

Equivalently,

\[
P+Q+R=O.
\]

The key arithmetic fact is that the line through rational points has rational coefficients; substituting it into the cubic yields a cubic polynomial over \(\mathbb Q\). Since two of its intersection roots are already rational, Vieta’s formulas force the third root to be rational too. Reflecting it preserves rationality. [old.mccme](https://old.mccme.ru/ium/library/pdf/Ostrik-Tsfasman.pdf)

## Addition formulas

Let

\[
P=(x_1,y_1),\qquad Q=(x_2,y_2)
\]

be rational points on \(E\).

### Distinct non-opposite points

Suppose \(x_1\neq x_2\). The slope of the line through them is

\[
m=\frac{y_2-y_1}{x_2-x_1}\in\mathbb Q.
\]

Writing the line as

\[
y=m(x-x_1)+y_1,
\]

and substituting into \(y^2=x^3+Ax+B\), one finds that the third intersection has \(x\)-coordinate

\[
x_R=m^2-x_1-x_2.
\]

Because \(P+Q\) is the reflection of \(R\), its coordinates are

\[
\boxed{
x_{P+Q}=m^2-x_1-x_2
}
\]

and

\[
\boxed{
y_{P+Q}=m(x_1-x_{P+Q})-y_1.
}
\]

Every expression on the right lies in \(\mathbb Q\), so

\[
P,Q\in E(\mathbb Q)
\quad\Longrightarrow\quad
P+Q\in E(\mathbb Q).
\]

### Doubling a point

If \(P=Q=(x_1,y_1)\) and \(y_1\neq0\), differentiate the curve equation:

\[
2y\frac{dy}{dx}=3x^2+A.
\]

Therefore, the tangent slope is

\[
m=\frac{3x_1^2+A}{2y_1}\in\mathbb Q.
\]

The same formulas give

\[
\boxed{
x_{2P}=m^2-2x_1
}
\]

and

\[
\boxed{
y_{2P}=m(x_1-x_{2P})-y_1.
}
\]

Again, \(2P\) is rational whenever \(P\) is rational and \(y_1\neq0\). [math.mit](https://math.mit.edu/classes/18.783/2019/LectureNotes2.pdf)

## Exceptional cases

The formula has natural special cases:

| Situation | Sum |
|---|---|
| \(P+O\) | \(P\) |
| \(P=(x,y)\), \(-P=(x,-y)\) | \(P+(-P)=O\) |
| \(P=(x,0)\) | \(P=-P\), hence \(2P=O\) |
| \(P=Q\), \(y\neq0\) | Use the tangent formula above |

Thus the projective rational points

\[
E(\mathbb Q)=\{(x,y)\in\mathbb Q^2:y^2=x^3+Ax+B\}\cup\{O\}
\]

are closed under the addition law.

## Worked example

Take

\[
E:\quad y^2=x^3-2.
\]

Two rational points are

\[
P=(3,5),\qquad Q=(3,-5)=-P,
\]

because

\[
5^2=25=3^3-2.
\]

Since they are vertical reflections of one another,

\[
P+Q=P+(-P)=O.
\]

For a nontrivial addition example, double \(P=(3,5)\). The tangent slope is

\[
m=\frac{3(3)^2+0}{2(5)}
=\frac{27}{10}.
\]

Then

\[
x_{2P}
=
\left(\frac{27}{10}\right)^2-2(3)
=
\frac{729}{100}-\frac{600}{100}
=
\frac{129}{100}.
\]

And

\[
y_{2P}
=
\frac{27}{10}\left(3-\frac{129}{100}\right)-5
=
\frac{27}{10}\cdot\frac{171}{100}-5
=
-\frac{383}{1000}.
\]

Hence

\[
\boxed{
2(3,5)
=
\left(\frac{129}{100},-\frac{383}{1000}\right).
}
\]

This is visibly rational, and it does lie on \(E\):

\[
\left(-\frac{383}{1000}\right)^2
=
\left(\frac{129}{100}\right)^3-2.
\]

So one rational point can be repeatedly added to itself to generate further rational points—though eventually it may cycle back to \(O\) if the point has finite order.

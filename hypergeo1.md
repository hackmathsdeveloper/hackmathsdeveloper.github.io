
You derive the differential equation by translating the coefficient recurrence of the power series into an operator identity. The key operator is the Euler operator

\[
\theta:=z\frac{d}{dz},
\qquad
\theta(z^n)=n z^n.
\]

So any polynomial \(P(\theta)\) acts diagonally on a power series: if \(y(z)=\sum_{n\ge0}c_nz^n\), then

\[
P(\theta)y=\sum_{n\ge0}P(n)c_nz^n.
\]

## General derivation

Start from

\[
y(z)={}_pF_q\!\left(
\begin{matrix}a_1,\ldots,a_p\\b_1,\ldots,b_q\end{matrix};z
\right)
=
\sum_{n=0}^{\infty}c_nz^n,
\]

with

\[
c_n=
\frac{(a_1)_n\cdots(a_p)_n}
{(b_1)_n\cdots(b_q)_n\,n!}.
\]

Its coefficient ratio is

\[
\frac{c_n}{c_{n-1}}
=
\frac{\prod_{i=1}^{p}(n+a_i-1)}
{n\prod_{j=1}^{q}(n+b_j-1)}.
\]

Equivalently,

\[
n\prod_{j=1}^{q}(n+b_j-1)c_n
=
\prod_{i=1}^{p}(n+a_i-1)c_{n-1}.
\tag{1}
\]

Now compare coefficients of \(z^n\) in the following two expressions:

\[
\theta\prod_{j=1}^{q}(\theta+b_j-1)y
\]

and

\[
z\prod_{i=1}^{p}(\theta+a_i)y.
\]

The first has coefficient

\[
n\prod_{j=1}^{q}(n+b_j-1)c_n,
\]

while the second has coefficient

\[
\prod_{i=1}^{p}(n+a_i-1)c_{n-1}.
\]

They agree by (1), giving the generalized hypergeometric differential equation:

\[
\boxed{
\left[
\theta\prod_{j=1}^{q}(\theta+b_j-1)
-
z\prod_{i=1}^{p}(\theta+a_i)
\right]y=0.
}
\]

This is the compact “coefficient recurrence \(\Rightarrow\) ODE” recipe. [dlmf.nist](https://dlmf.nist.gov/16.8)

## Gauss \({}_2F_1\)

Let

\[
y(z)={}_2F_1(a,b;c;z)
=
\sum_{n=0}^{\infty}
\frac{(a)_n(b)_n}{(c)_n n!}z^n.
\]

The coefficient recurrence is

\[
\frac{c_n}{c_{n-1}}
=
\frac{(n+a-1)(n+b-1)}
{n(n+c-1)}.
\]

Hence

\[
n(n+c-1)c_n
=
(n+a-1)(n+b-1)c_{n-1}.
\]

Replace \(n\) with \(\theta\), remembering that the shift due to the leading \(z\) changes \(n\) to \(n-1\) on the right:

\[
\boxed{
\left[\theta(\theta+c-1)-z(\theta+a)(\theta+b)\right]y=0.
}
\tag{2}
\]

Expanding the Euler operators,

\[
\theta y=zy',
\qquad
\theta^2y=z^2y''+zy',
\]

turns (2) into the familiar Gauss hypergeometric equation:

\[
\boxed{
z(1-z)y''
+
\bigl[c-(a+b+1)z\bigr]y'
-ab\,y
=0.
}
\]

The three regular singular points \(z=0,1,\infty\) follow immediately from this standard form. [famaf.unc.edu](https://www.famaf.unc.edu.ar/documents/892/BMat48-2.pdf)

## Worked coefficient check

The first few terms are

\[
y(z)=1+\frac{ab}{c}z
+\frac{a(a+1)b(b+1)}{2c(c+1)}z^2+\cdots.
\]

For \(n=2\), the recurrence claims

\[
2(c+1)c_2=(a+1)(b+1)c_1.
\]

Indeed,

\[
2(c+1)
\frac{a(a+1)b(b+1)}{2c(c+1)}
=
(a+1)(b+1)\frac{ab}{c}.
\]

That equality is exactly what causes the coefficient of each \(z^n\) in the ODE to vanish.

## Two useful specializations

| Series | Operator equation | Usual ODE |
|---|---|---|
| \(\displaystyle {}_1F_1(a;c;z)\) | \(\displaystyle [\theta(\theta+c-1)-z(\theta+a)]y=0\) | \(\displaystyle zy''+(c-z)y'-ay=0\) |
| \(\displaystyle {}_0F_1(;c;z)\) | \(\displaystyle [\theta(\theta+c-1)-z]y=0\) | \(\displaystyle zy''+cy'-y=0\) |

The first is Kummer’s confluent hypergeometric equation, obtained as a confluence/limit of the Gauss family. The second is closely related to Bessel functions after a change of variable and elementary prefactor. [math.libretexts](https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_(Herman)/04:_Series_Solutions/4.08:_Hypergeometric_Functions)

## Reverse direction

The method is reversible. Given an ODE written as a polynomial expression in \(z\) and \(\theta\), substitute

\[
y=\sum_{n\ge0}c_nz^n,
\]

read off the recurrence for \(c_n\), and factor its numerator and denominator into linear terms in \(n\). If the result is

\[
\frac{c_n}{c_{n-1}}
=
\frac{\prod_i(n+\alpha_i)}
{n\prod_j(n+\beta_j)},
\]

then the local series solution is hypergeometric, with parameters determined by those roots. This is the Frobenius-series mechanism behind why hypergeometric functions solve so many regular-singular equations. [dlmf.nist](https://dlmf.nist.gov/16.8)

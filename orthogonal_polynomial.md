
A sequence \(\{p_n\}_{n\ge0}\) is **orthogonal** with respect to a weight \(w\) on an interval \(I\) when \(\deg p_n=n\) and

\[
\langle p_n,p_m\rangle
=\int_I p_n(x)p_m(x)w(x)\,dx
=h_n\delta_{nm},
\qquad h_n>0.
\]

Thus distinct-degree polynomials have zero weighted inner product. Such sequences can be constructed by applying Gram–Schmidt to \(1,x,x^2,\ldots\). [dlmf.nist](https://dlmf.nist.gov/18.2)

## Demonstration: Legendre polynomials

Take \(I=[-1,1]\) and \(w(x)=1\). The inner product is

\[
\langle f,g\rangle=\int_{-1}^{1} f(x)g(x)\,dx.
\]

Starting with monomials:

\[
P_0(x)=1,
\]

\[
P_1(x)=x,
\]

because \(\langle 1,x\rangle=0\) by odd symmetry.

For degree \(2\), subtract the component of \(x^2\) parallel to \(P_0\):

\[
q_2(x)=x^2-\frac{\langle x^2,1\rangle}{\langle1,1\rangle}.
\]

Since

\[
\langle x^2,1\rangle=\int_{-1}^1x^2\,dx=\frac23,
\qquad
\langle1,1\rangle=2,
\]

we get

\[
q_2(x)=x^2-\frac13.
\]

Choosing the conventional normalization \(P_2(1)=1\),

\[
P_2(x)=\frac12(3x^2-1).
\]

Continuing produces

\[
P_3(x)=\frac12(5x^3-3x),
\]

\[
P_4(x)=\frac18(35x^4-30x^2+3).
\]

## Orthogonality check

For example,

\[
\int_{-1}^{1}P_0(x)P_2(x)\,dx
=
\int_{-1}^{1}\frac12(3x^2-1)\,dx
=0,
\]

and

\[
\int_{-1}^{1}P_1(x)P_3(x)\,dx
=
\int_{-1}^{1}
x\frac12(5x^3-3x)\,dx
=0.
\]

In full generality, Legendre polynomials satisfy

\[
\int_{-1}^{1}P_n(x)P_m(x)\,dx
=
\frac{2}{2n+1}\delta_{nm}.
\]

Therefore the normalized functions

\[
\widehat P_n(x)=\sqrt{\frac{2n+1}{2}}\,P_n(x)
\]

form an orthonormal sequence in \(L^2([-1,1])\).

## Three-term recurrence

A central feature of orthogonal-polynomial sequences is a three-term recurrence. For Legendre polynomials,

\[
(n+1)P_{n+1}(x)
=
(2n+1)xP_n(x)-nP_{n-1}(x),
\]

with \(P_0(x)=1\) and \(P_1(x)=x\). More generally, every orthogonal polynomial system associated with a positive measure obeys a three-term recurrence (Favard structure). [warwick.ac](https://warwick.ac.uk/fac/sci/maths/research/grants/equip/grouplunch/ma4k0_notes_r21_ch8_2.pdf)

## Other standard examples

| Family | Interval/domain | Weight |
|---|---:|---:|
| Legendre \(P_n\) | \([-1,1]\) | \(1\) |
| Chebyshev \(T_n\) | \([-1,1]\) | \((1-x^2)^{-1/2}\) |
| Hermite \(H_n\) | \((-\infty,\infty)\) | \(e^{-x^2}\) |
| Laguerre \(L_n^{(\alpha)}\) | \([0,\infty)\) | \(x^\alpha e^{-x}\), \(\alpha>-1\) |

The choice of interval and weight is essential: it determines which polynomial sequence is orthogonal. [dlmf.nist](https://dlmf.nist.gov/18.2)

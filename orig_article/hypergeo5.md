
Gauss’s continued fraction expresses a ratio of contiguous Gaussian hypergeometric functions as a continued fraction. A standard form is

\[
\frac{{}_2F_1(a,b+1;c+1;z)}
{{}_2F_1(a,b;c;z)}
=
\cfrac{1}{
1-\cfrac{
\frac{a(c-b)}{c(c+1)}z
}{
1-\cfrac{
\frac{(b+1)(c-a+1)}{(c+1)(c+2)}z
}{
1-\cfrac{
\frac{(a+1)(c-b+1)}{(c+2)(c+3)}z
}{
1-\cfrac{
\frac{(b+2)(c-a+2)}{(c+3)(c+4)}z
}{\ddots}
}}}}
\]

where

\[
{}_2F_1(a,b;c;z)
=
\sum_{n=0}^{\infty}
\frac{(a)_n(b)_n}{(c)_n\,n!}z^n,
\]

and \((q)_n=q(q+1)\cdots(q+n-1)\) is the rising factorial. [math.tugraz](https://www.math.tugraz.at/~prodinger/Avery-contribution-July-2012.pdf)

## Why it matters

It converts a hypergeometric-function ratio into a three-term-recurrence structure. This is useful because continued fractions can be numerically stable for evaluating certain function ratios—particularly in parameter or argument ranges where directly summing the power series is slow or ill-conditioned. The identity comes from *contiguous relations*: linear identities among \({}_2F_1\) functions whose parameters differ by integers. [en.wikipedia](https://en.wikipedia.org/wiki/Gauss's_continued_fraction)

## Equivalent sign convention

You will often see the same fraction written as

\[
\frac{{}_2F_1(a+1,b;c+1;z)}
{{}_2F_1(a,b;c;z)}
=
\cfrac{1}{
1+\cfrac{k_1z}{
1+\cfrac{k_2z}{
1+\cfrac{k_3z}{\ddots}}}},
\]

with coefficients alternating as

\[
k_{2m+1}
=
\frac{(a-c-m)(b+m)}
{(c+2m)(c+2m+1)},
\qquad
k_{2m+2}
=
\frac{(b-c-m-1)(a+m+1)}
{(c+2m+1)(c+2m+2)}.
\]

This is the same underlying result, just using a different contiguous ratio and absorbing minus signs into the partial numerators. [en.wikipedia](https://en.wikipedia.org/wiki/Hypergeometric_function)

It is called “Gauss’s” continued fraction because Gauss derived it in the context of hypergeometric functions; it is a general template that specializes to continued fractions for more familiar functions such as logarithmic, inverse-trigonometric, and Bessel-related expressions. [en.wikipedia](https://en.wikipedia.org/wiki/Gauss's_continued_fraction)

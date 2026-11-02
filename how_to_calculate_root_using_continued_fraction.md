
To find the **simple continued fraction** of \(\sqrt n\), repeatedly take the integer part, subtract it, and take the reciprocal. For a square root, use the conjugate to rationalize each denominator; the process will eventually return to an earlier complete quotient, giving a repeating block. [math.stackexchange](https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root)

## The algorithm

Let \(n\) be a positive integer that is not a perfect square. Define
\[
x_0=\sqrt n,\qquad
a_i=\lfloor x_i\rfloor,\qquad
x_{i+1}=\frac1{x_i-a_i}.
\]
Then
\[
\sqrt n=[a_0;a_1,a_2,\ldots].
\]
The key practical step is to write each \(x_i\) in the form
\[
x_i=\frac{\sqrt n+b_i}{c_i},
\]
where \(b_i,c_i\) are integers. Then
\[
a_i=\left\lfloor\frac{\sqrt n+b_i}{c_i}\right\rfloor.
\]
After subtracting \(a_i\), rationalize using the conjugate:
\[
x_{i+1}
=\frac{c_i}{\sqrt n+b_i-a_ic_i}
=\frac{c_i(\sqrt n+a_ic_i-b_i)}
{n-(b_i-a_ic_i)^2}.
\]
This again has the form \((\sqrt n+b_{i+1})/c_{i+1}\). [math.stackexchange](https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root)

Stop when a complete quotient \(x_i\) repeats. Since \(\sqrt n\) is a quadratic irrational, Lagrange’s theorem guarantees that its simple continued fraction is eventually periodic. [en.wikipedia](https://en.wikipedia.org/wiki/Square_root_algorithms)

## Example: \(\sqrt{7}\)

First find
\[
a_0=\lfloor\sqrt7\rfloor=2,
\]
because \(2^2<7<3^2\). Thus
\[
x_0=\sqrt7,\qquad a_0=2.
\]

Now
\[
x_1=\frac1{\sqrt7-2}.
\]
Rationalize:
\[
x_1=\frac{\sqrt7+2}{7-4}
=\frac{\sqrt7+2}{3}.
\]
Since \(2<\sqrt7<3\), we have
\[
\frac43<x_1<\frac53,
\]
so
\[
a_1=1.
\]

Next,
\[
x_2=\frac1{x_1-1}
=\frac1{\frac{\sqrt7+2}{3}-1}
=\frac3{\sqrt7-1}.
\]
Rationalize:
\[
x_2=\frac{3(\sqrt7+1)}{7-1}
=\frac{\sqrt7+1}{2}.
\]
Since \(3<\sqrt7+1<4\), we get
\[
\frac32<x_2<2,
\]
so
\[
a_2=1.
\]

Next,
\[
x_3=\frac1{x_2-1}
=\frac1{\frac{\sqrt7+1}{2}-1}
=\frac2{\sqrt7-1}.
\]
Rationalize:
\[
x_3=\frac{2(\sqrt7+1)}{6}
=\frac{\sqrt7+1}{3}.
\]
Since \(3<\sqrt7+1<4\),
\[
1<x_3<\frac43,
\]
so
\[
a_3=1.
\]

Next,
\[
x_4=\frac1{x_3-1}
=\frac1{\frac{\sqrt7+1}{3}-1}
=\frac3{\sqrt7-2}.
\]
Rationalize:
\[
x_4=\frac{3(\sqrt7+2)}{3}
=\sqrt7+2.
\]
Since \(4<\sqrt7+2<5\),
\[
a_4=4.
\]

Finally,
\[
x_5=\frac1{x_4-4}
=\frac1{\sqrt7-2}
=x_1.
\]

Because \(x_5=x_1\), the partial quotients from \(a_1\) onward repeat:
\[
\boxed{\sqrt7=[2;\overline{1,1,1,4}].}
\]

## Compact table method

For \(\sqrt n\), track three quantities:

\[
x_i=\frac{\sqrt n+b_i}{c_i}.
\]

At each step:

1. Compute \(a_i=\left\lfloor\frac{\sqrt n+b_i}{c_i}\right\rfloor\).
2. Update
   \[
   b_{i+1}=a_ic_i-b_i.
   \]
3. Update
   \[
   c_{i+1}=\frac{n-b_{i+1}^2}{c_i}.
   \]
4. Stop when the pair \((b_i,c_i)\) repeats.

For \(\sqrt7\), this gives:

| \(i\) | \(b_i\) | \(c_i\) | \(a_i\) |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 2 |
| 1 | 2 | 3 | 1 |
| 2 | 1 | 2 | 1 |
| 3 | 1 | 3 | 1 |
| 4 | 2 | 1 | 4 |
| 5 | 2 | 3 | repeats |

The repeated pair \((2,3)\) confirms
\[
\sqrt7=[2;\overline{1,1,1,4}].
\]
This tabular method avoids repeated rationalization and is the standard efficient way to compute the expansion by hand. [math.stackexchange](https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root)

## A useful special case

If \(n=s^2+r\), where \(s=\lfloor\sqrt n\rfloor\) and \(r>0\), then \(\sqrt n\) also has a **generalized continued fraction**
\[
\sqrt n=s+\cfrac{r}{2s+\cfrac{r}{2s+\cfrac{r}{2s+\ddots}}}.
\]
This is often easy to write down, but it is not generally the simple continued fraction, because its numerators are \(r\) rather than \(1\). [en.wikipedia](https://en.wikipedia.org/wiki/Square_root_algorithms)

For example, with \(n=7\), \(s=2\) and \(r=3\):
\[
\sqrt7=2+\cfrac3{4+\cfrac3{4+\cfrac3{4+\ddots}}}.
\]
This is correct, but the simple continued fraction is the different expression
\[
\sqrt7=[2;\overline{1,1,1,4}].
\]
Be careful not to confuse the two forms. [math.stackexchange](https://math.stackexchange.com/questions/980470/find-the-continued-fraction-of-the-square-root-of-a-given-integer)

## Quick checks

- If \(n\) is a perfect square, \(\sqrt n\) is an integer and its continued fraction terminates.
- If \(n\) is not a perfect square, \(\sqrt n\) is irrational and has an infinite eventually periodic simple continued fraction. [en.wikipedia](https://en.wikipedia.org/wiki/Square_root_algorithms)
- The first term is always \(a_0=\lfloor\sqrt n\rfloor\). [math.stackexchange](https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root)
- For \(\sqrt n\), the repeating block always ends with \(2a_0\); for \(\sqrt7\), that final entry is \(4=2\cdot2\). This is a useful check, though the earlier entries require the algorithm. [en.wikipedia](https://en.wikipedia.org/wiki/Square_root_algorithms)

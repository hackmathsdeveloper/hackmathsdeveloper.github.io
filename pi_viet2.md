
Ludolph van Ceulen did not use Viète’s infinite product exactly as we now write it, but he used the same underlying engine: **repeated angle bisection** and increasingly fine regular polygons. He bounded \(\pi\) between the perimeters of polygons inscribed in and circumscribed about a circle, repeatedly doubling their number of sides until the two bounds agreed for 35 decimal places. His last computation reached polygons with \(2^{62}\) sides—about \(4.61\times10^{18}\) sides. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Van_Ceulen/)

## The geometric setup

Choose a circle of radius \(r=1\). Its circumference is \(2\pi\). For a regular \(n\)-gon:

- The inscribed polygon lies inside the circle, so its perimeter \(p_n\) is too small:
  \[
  p_n<2\pi.
  \]

- The circumscribed polygon lies outside the circle, so its perimeter \(P_n\) is too large:
  \[
  2\pi<P_n.
  \]

Thus,

\[
p_n<2\pi<P_n.
\]

Dividing by \(2\) gives direct lower and upper bounds for \(\pi\):

\[
n\sin\left(\frac{\pi}{n}\right)
<
\pi
<
n\tan\left(\frac{\pi}{n}\right).
\]

The formulae come from one of the \(n\) congruent central triangles:

\[
p_n = 2n\sin\left(\frac{\pi}{n}\right),
\qquad
P_n = 2n\tan\left(\frac{\pi}{n}\right).
\]

Van Ceulen did not possess modern trigonometric notation in this form, but his chord and tangent calculations implement exactly these quantities.

## Why doubling sides worked

The key operation was

\[
n \longrightarrow 2n.
\]

Instead of computing a new polygon from scratch, he bisected each central angle. If a side of the inscribed \(n\)-gon is a chord, then the side of the inscribed \(2n\)-gon is the chord of half the angle.

Modernly, if

\[
s_n=2\sin\left(\frac{\pi}{n}\right)
\]

is the side length of the inscribed \(n\)-gon in a unit circle, then the side length after doubling is

\[
s_{2n}
=
\sqrt{2-\sqrt{4-s_n^2}}.
\]

This is simply the cosine half-angle formula in geometric disguise. To see it, write

\[
s_n=2\sin\theta,
\qquad
\theta=\frac{\pi}{n}.
\]

Then

\[
s_{2n}
=
2\sin\left(\frac{\theta}{2}\right)
=
\sqrt{2-2\cos\theta},
\]

and since

\[
\cos\theta=\sqrt{1-\sin^2\theta}
=
\sqrt{1-\frac{s_n^2}{4}},
\]

we get

\[
s_{2n}
=
\sqrt{2-\sqrt{4-s_n^2}}.
\]

So one square root operation turns the side length for an \(n\)-gon into that for a \(2n\)-gon.

For circumscribed polygons, the corresponding tangent-side recurrence can be written as

\[
t_{2n}
=
\frac{\sqrt{4+t_n^2}-2}{t_n},
\]

where

\[
t_n=2\tan\left(\frac{\pi}{n}\right)
\]

is the side length of the circumscribed \(n\)-gon around a unit circle. In practical historical computation, variants based on semiperimeters, chords, and “sagittae” were often more convenient because they reduced the arithmetic burden.

## A modern reconstruction

One clean way to reproduce the method uses polygon perimeters directly.

Let

\[
a_n=n\sin\left(\frac{\pi}{n}\right),
\qquad
b_n=n\tan\left(\frac{\pi}{n}\right).
\]

Then

\[
a_n<\pi<b_n.
\]

Start with an inscribed square and a circumscribed square:

\[
a_4
=
4\sin\left(\frac{\pi}{4}\right)
=
2\sqrt2
\approx 2.8284271247,
\]

\[
b_4
=
4\tan\left(\frac{\pi}{4}\right)
=
4.
\]

Therefore,

\[
2.8284271247<\pi<4.
\]

After doubling to an octagon,

\[
a_8
=
8\sin\left(\frac{\pi}{8}\right)
=
4\sqrt{2-\sqrt2}
\approx 3.0614674589,
\]

\[
b_8
=
8\tan\left(\frac{\pi}{8}\right)
=
8(\sqrt2-1)
\approx 3.3137084990.
\]

Hence,

\[
3.0614674589<\pi<3.3137084990.
\]

The interval narrows every time the number of sides doubles:

\[
4,\ 8,\ 16,\ 32,\ldots,\ 2^{62}.
\]

At a very large \(n\), both expressions are extremely close to \(\pi\):

\[
n\sin\left(\frac{\pi}{n}\right)
\approx
\pi-\frac{\pi^3}{6n^2},
\]

\[
n\tan\left(\frac{\pi}{n}\right)
\approx
\pi+\frac{\pi^3}{3n^2}.
\]

So the total width of the enclosure is approximately

\[
b_n-a_n
\approx
\frac{\pi^3}{2n^2}.
\]

For \(n=2^{62}\), this is of order

\[
\frac{\pi^3}{2(2^{62})^2}
\approx 7.3\times 10^{-37},
\]

which is comfortably narrower than \(10^{-35}\). That is why a \(2^{62}\)-gon can certify about 35 decimal digits.

## Relation to Viète’s formula

Viète’s formula results from tracking the same halving process multiplicatively. Starting with

\[
\sin x
=
2\sin\left(\frac{x}{2}\right)
\cos\left(\frac{x}{2}\right),
\]

and repeating the identity gives

\[
\sin x
=
2^m\sin\left(\frac{x}{2^m}\right)
\prod_{k=1}^{m}
\cos\left(\frac{x}{2^k}\right).
\]

With \(x=\pi/2\),

\[
1
=
2^m\sin\left(\frac{\pi}{2^{m+1}}\right)
\prod_{k=1}^{m}
\cos\left(\frac{\pi}{2^{k+1}}\right).
\]

As \(m\to\infty\),

\[
2^m\sin\left(\frac{\pi}{2^{m+1}}\right)
\longrightarrow
\frac{\pi}{2},
\]

giving

\[
\frac{2}{\pi}
=
\prod_{k=1}^{\infty}
\cos\left(\frac{\pi}{2^{k+1}}\right).
\]

Van Ceulen’s polygon sequence and Viète’s nested radicals therefore encode the same geometry:

| Aspect | Viète | Van Ceulen |
|---|---|---|
| Core operation | Halve a central angle | Double the number of polygon sides |
| Algebraic result | Product of half-angle cosines | Recursive chord/tangent computations |
| Geometric object | Usually presented through polygon areas or perimeters | Explicit inner and outer polygon bounds |
| Output | An infinite product for \(2/\pi\) | Certified decimal interval containing \(\pi\) |
| Certainty | Convergence in the limit | A rigorous lower and upper bound at each finite stage |

Viète had published a 20-decimal value in *Van den Circkel* in 1596, using polygonal computation; his later work extended the result. The 35-digit result was completed before van Ceulen’s death in 1610, but the full value appeared posthumously in Willebrord Snellius’s *Cyclometricus* in 1621. A 1615 posthumous publication reported 33 digits. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/Biographies/Van_Ceulen/)

## The 35-digit result

The celebrated value is

\[
\pi
\approx
3.14159265358979323846264338327950288.
\]

It became known in parts of Europe as the **Ludolphine number**. The digits were famously associated with van Ceulen’s tombstone in Leiden; the original stone was lost, and a replacement was installed in 2000. [en.wikipedia](https://en.wikipedia.org/wiki/Ludolph_van_Ceulen)

What made this extraordinary was not a new shortcut, but the scale and reliability of the hand computation. Each doubling required high-precision square-root extraction, multiplication, division, and careful control of lower and upper bounds. Doing that repeatedly—without electronic calculation, modern decimal arithmetic, or symbolic trigonometric notation—over decades was an immense computational achievement.

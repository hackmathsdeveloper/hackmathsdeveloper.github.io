Here is the “dual” derivation for \(\sin(\pi z)\) using Mittag–Leffler on \(\pi\cot(\pi z)\), then integrating to get the sine product. This mirrors what we did for \(\tan\).

***

## 1. Meromorphic data for \(\pi \cot(\pi z)\)

Consider \(F(z) = \pi\cot(\pi z)\). It is meromorphic on \(\mathbb{C}\) with:

- Poles at all integers \(n\in\mathbb{Z}\). [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function)
- All poles simple, with residue \(1\) at each integer (since \(\cot w\) has residue \(1\) at \(w=k\pi\), and the factor \(\pi\) from \(w=\pi z\) cancels with the Jacobian \(dw = \pi\,dz\)). [math.nie.edu](https://math.nie.edu.sg/research/Maths2011/M2011-2.pdf)

Mittag–Leffler’s theorem gives an expansion of a meromorphic function as a sum of its principal parts plus (at most) an entire function. For \(F(z)\), these principal parts are [en.wikipedia](https://en.wikipedia.org/wiki/Mittag-Leffler's_theorem)
\[
\frac{1}{z-n},\quad n\in\mathbb{Z}.
\]

A standard symmetric choice of expansion is
\[
\pi\cot(\pi z) 
= \frac{1}{z} + \sum_{n\neq 0}\left(\frac{1}{z-n} + \frac{1}{n}\right),[][]
\]
where the \(\tfrac{1}{n}\) terms are inserted to make the resulting series converge normally; they contribute an entire function which is absorbed globally. [ncatlab](https://ncatlab.org/nlab/show/product+formula+for+the+sine+function)

Grouping \(n\) and \(-n\) yields the more familiar form
\[
\pi\cot(\pi z)
= \frac{1}{z} + \sum_{n=1}^{\infty}\left(\frac{1}{z-n} + \frac{1}{z+n}\right).[][]
\]
Compute the combined fraction:
\[
\frac{1}{z-n} + \frac{1}{z+n}
= \frac{(z+n) + (z-n)}{z^{2} - n^{2}}
= \frac{2z}{z^{2} - n^{2}},
\]
so
\[
\boxed{
\pi\cot(\pi z)
= \frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2}-n^{2}},\quad z\notin\mathbb{Z}.
}[][]

This is the Mittag–Leffler partial fraction expansion for \(\pi\cot(\pi z)\).[]

***

## 2. Recognize \(\pi\cot(\pi z)\) as a logarithmic derivative

Let \(f(z) = \sin(\pi z)\). Then
\[
\frac{d}{dz}\log f(z)
= \frac{f'(z)}{f(z)}
= \frac{\pi\cos(\pi z)}{\sin(\pi z)}
= \pi\cot(\pi z),\quad z\notin\mathbb{Z}. [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function)
\]

So we have
\[
\frac{d}{dz}\log\sin(\pi z)
= \frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2} - n^{2}}. [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function/Proof_1)

The right-hand side is already a convergent sum of rational functions on any compact set avoiding the integers, so we can integrate termwise there.

***

## 3. Integrate the partial fraction expansion

Integrate both sides with respect to \(z\):
\[
\log\sin(\pi z)
= \int\left(\frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2}-n^{2}}\right)\,dz.
\]

Compute the integrals:

- \(\displaystyle \int \frac{1}{z}\,dz = \log z\) (up to additive constant). [theoremoftheday](https://www.theoremoftheday.org/GeometryAndTrigonometry/EulerSine/TotDEulerSine.pdf)
- For each \(n\ge 1\),
  \[
  \int \frac{z}{z^{2}-n^{2}}\,dz 
  = \frac{1}{2}\log(z^{2}-n^{2}) + \text{const},
  \]
  since the derivative of \(z^{2} - n^{2}\) is \(2z\). [theoremoftheday](https://www.theoremoftheday.org/GeometryAndTrigonometry/EulerSine/TotDEulerSine.pdf)

Thus
\[
\log\sin(\pi z)
= \log z + \sum_{n=1}^{\infty}\log(z^{2}-n^{2}) + C,[]
\]
where \(C\) is a constant of integration.

Rewrite \(\log(z^{2}-n^{2})\) as \(\log n^{2} + \log\left(1 - \tfrac{z^{2}}{n^{2}}\right)\):
\[
\log(z^{2}-n^{2}) = \log n^{2} + \log\left(1 - \frac{z^{2}}{n^{2}}\right).[]

Substitute:
\[
\log\sin(\pi z)
= \log z + \sum_{n=1}^{\infty}\left[\log n^{2} + \log\left(1 - \frac{z^{2}}{n^{2}}\right)\right] + C. [theoremoftheday](https://www.theoremoftheday.org/GeometryAndTrigonometry/EulerSine/TotDEulerSine.pdf)
\]

The \(\sum_{n=1}^{\infty}\log n^{2}\) piece depends only on \(n\), not on \(z\); it can be absorbed into the constant \(C\).[] Denote by \(C'\) the new constant:
\[
\log\sin(\pi z)
= C' + \log z + \sum_{n=1}^{\infty}\log\left(1 - \frac{z^{2}}{n^{2}}\right). [theoremoftheday](https://www.theoremoftheday.org/GeometryAndTrigonometry/EulerSine/TotDEulerSine.pdf)

Exponentiate:
\[
\sin(\pi z)
= e^{C'}\,z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).[][]

So we have
\[
\boxed{
\sin(\pi z)
= C\,z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right),
}
\]
for some constant \(C = e^{C'}\).[][]

***

## 4. Fix the multiplicative constant

To determine \(C\), compare behavior near \(z=0\).

Using the usual Taylor series,
\[
\sin(\pi z) = \pi z - \frac{\pi^{3}}{6}z^{3} + O(z^{5}),\quad z\to 0. [en.wikipedia](https://en.wikipedia.org/wiki/Sine_and_cosine)

On the other hand, expand the product:
\[
z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
= z\left(1 + O(z^{2})\right),
\]
so the leading term is just \(z\). [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

Thus near zero,
\[
\sin(\pi z) \sim \pi z,\qquad
C\,z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)\sim C z.[][]

Therefore \(C = \pi\), and we obtain Euler’s product:
\[
\boxed{
\sin(\pi z)
= \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right),\quad z\in\mathbb{C}.
} [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

Returning to \(x = \pi z\), this is
\[
\sin x = x\prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right).[][]

***

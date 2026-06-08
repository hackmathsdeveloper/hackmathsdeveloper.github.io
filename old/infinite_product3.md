
Here is a derivation of the infinite product for \(\tan(\pi z)\) that starts from its poles and residues via Mittag–Leffler, and only at the very end integrates to recover the product.

***

## 1. Set up the meromorphic data for \(\tan(\pi z)\)

Consider \(f(z) = \tan(\pi z)\). It is meromorphic on \(\mathbb{C}\) with:

- Poles at \(z_k = k + \tfrac{1}{2}\), \(k \in \mathbb{Z}\). [en.wikipedia](https://en.wikipedia.org/wiki/Mittag-Leffler's_theorem)
- All poles are simple, and the residue at each pole is \(-1/\pi\) (because \(\tan w\) has residue \(1\) at its poles \(w = \tfrac{\pi}{2} + k\pi\), and the factor \(\pi\) in \(\tan(\pi z)\) contributes a Jacobian \(\pi\)). [en.wikipedia](https://en.wikipedia.org/wiki/Partial_fractions_in_complex_analysis)

Mittag–Leffler’s theorem tells us that we can expand a meromorphic function as a sum of its principal parts, possibly plus an entire function. For \(f(z) = \pi\tan(\pi z)\) the theorem gives the explicit partial fraction expansion [en.wikipedia](https://en.wikipedia.org/wiki/Mittag-Leffler's_theorem)
\[
\pi \tan(\pi z)
= \lim_{N\to\infty}\sum_{k=-N}^{N}\frac{-1}{z - (k+\tfrac{1}{2})}
= 2z\sum_{n=0}^{\infty}\frac{-1}{z^{2} - (n+\tfrac{1}{2})^{2}},[]
\]
where the second equality is obtained by pairing terms \(k\) and \(-k-1\) and simplifying. [en.wikipedia](https://en.wikipedia.org/wiki/Mittag-Leffler's_theorem)

Equivalently,
\[
\tan(\pi z)
= -\frac{2z}{\pi}\sum_{n=0}^{\infty}\frac{1}{z^{2} - (n+\tfrac{1}{2})^{2}}.
\] [en.wikipedia](https://en.wikipedia.org/wiki/Mittag-Leffler's_theorem)

***

## 2. Relate \(\tan(\pi z)\) to \(\cos(\pi z)\)

We now look at the logarithmic derivative of \(\cos(\pi z)\). Define
\[
g(z) := \cos(\pi z).
\]
Then
\[
\frac{g'(z)}{g(z)} = \frac{d}{dz}\log g(z)
= -\pi\tan(\pi z).[]
\]

On the other hand, \(\cos(\pi z)\) is an entire function whose zeros are exactly the half-integers \(z_k = k+\tfrac{1}{2}\), all simple. For such a function, the logarithmic derivative can be written using the zeros: [sertoz.bilkent.edu](https://sertoz.bilkent.edu.tr/courses/math503/2012/exam09-sol.pdf)
\[
\frac{g'(z)}{g(z)}
= \sum_{k\in\mathbb{Z}}\frac{1}{z - z_k} + \text{(entire correction)}.[][]
\]

But by the Mittag–Leffler expansion above, we already know that
\[
\pi\tan(\pi z) = \sum_{k\in\mathbb{Z}} \frac{-1}{z - (k+\tfrac{1}{2})},[]
\]
hence
\[
-\pi\tan(\pi z)
= \sum_{k\in\mathbb{Z}} \frac{1}{z - (k+\tfrac{1}{2})}.[]
\]

So we have
\[
\frac{g'(z)}{g(z)} = -\pi\tan(\pi z)
= \sum_{k\in\mathbb{Z}} \frac{1}{z - (k+\tfrac{1}{2})}.
\] [en.wikipedia](https://en.wikipedia.org/wiki/Mittag-Leffler's_theorem)

The right-hand side is already a convergent Mittag–Leffler expansion (principal parts only), so the “entire correction” term is actually zero. In other words, there is no extra entire function; the logarithmic derivative is fully determined by the poles. [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler's_Expansion_Theorem)

***

## 3. Integrate the logarithmic derivative to get a product

Integrate \(\dfrac{g'(z)}{g(z)}\) with respect to \(z\). Formally,
\[
\log g(z) = \int \frac{g'(z)}{g(z)}\,dz
= \int \sum_{k\in\mathbb{Z}}\frac{1}{z - (k+\tfrac{1}{2})}\,dz.
\]

Integrating term by term (justified by uniform convergence on compact subsets away from the zeros/poles),
\[
\log g(z) = \sum_{k\in\mathbb{Z}}\log\bigl(z - (k+\tfrac{1}{2})\bigr) + C,
\]
and exponentiating,
\[
g(z) = C\prod_{k\in\mathbb{Z}}\bigl(z - (k+\tfrac{1}{2})\bigr).
\]

To normalize and get something symmetric (and absolutely convergent as a product), it is standard to group terms \(k\) and \(-k-1\). This gives factors of the form
\[
\bigl(z - (k+\tfrac{1}{2})\bigr)\bigl(z - (-k-\tfrac{1}{2})\bigr)
= z^{2} - \bigl(k+\tfrac{1}{2}\bigr)^{2},
\]
so we can write
\[
\cos(\pi z)
= C\prod_{n=0}^{\infty}\left(1 - \frac{z^{2}}{(n+\tfrac{1}{2})^{2}}\right).[][]
\]

Choosing \(z=0\) gives
\[
1 = \cos(0) = C\prod_{n=0}^{\infty}\left(1 - 0\right) = C,
\]
hence \(C = 1\). Furthermore, recognizing that \((n+\tfrac{1}{2}) = \tfrac{2n+1}{2}\) and reindexing, [sertoz.bilkent.edu](https://sertoz.bilkent.edu.tr/courses/math503/2012/exam09-sol.pdf)
\[
\cos(\pi z) = \prod_{n=1}^{\infty}\left(1 - \frac{4z^{2}}{(2n-1)^{2}}\right).[][]

***

## 4. Use \(\tan(\pi z) = \dfrac{\sin(\pi z)}{\cos(\pi z)}\) to get the product

From the earlier sine product (which you already saw):
\[
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right). [people.math.binghamton](https://people.math.binghamton.edu/dikran/478/Ch6.pdf)

Combine this with the cosine product:
\[
\cos(\pi z)
= \prod_{n=1}^{\infty}\left(1 - \frac{4z^{2}}{(2n-1)^{2}}\right).[][]

Then
\[
\tan(\pi z)
= \frac{\sin(\pi z)}{\cos(\pi z)}
= \frac{\pi z\prod_{n=1}^{\infty}\left(1 - \dfrac{z^{2}}{n^{2}}\right)}
       {\prod_{n=1}^{\infty}\left(1 - \dfrac{4z^{2}}{(2n-1)^{2}}\right)}. [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)
\]

Thus the Mittag–Leffler route gives, up to the normalization we fixed via \(\cos(0)=1\),
\[
\boxed{
\tan(\pi z)
= \pi z\prod_{n=1}^{\infty}
\frac{1 - \dfrac{z^{2}}{n^{2}}}{1 - \dfrac{4z^{2}}{(2n-1)^{2}}}
}.
\][][]

In the usual variable \(x = \pi z\),
\[
\boxed{
\tan x
= x\prod_{n=1}^{\infty}
\frac{1 - \dfrac{x^{2}}{\pi^{2}n^{2}}}{1 - \dfrac{4x^{2}}{\pi^{2}(2n-1)^{2}}}
}.
\][][]

***

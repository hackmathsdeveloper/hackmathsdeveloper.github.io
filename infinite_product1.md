
You can derive Euler’s infinite product for sine by factoring it using its zeros and then fixing the multiplicative constant via a local expansion at 0. The final result is
\[
\sin x = x \prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right).
\] [youtube](https://www.youtube.com/watch?v=wUsIlK_sP60)

***

## 1. State the target formula

We want to show
\[
\sin(\pi z) = \pi z \prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)\quad(z\in\mathbb{C}),
\] [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)
which is equivalent, after substituting \(z = x/\pi\), to
\[
\sin x = x \prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right).\] [youtube](https://www.youtube.com/watch?v=wUsIlK_sP60)

***

## 2. Use zeros to guess a product

Key observations:

- \(\sin(\pi z)\) is an entire function of order 1 with simple zeros at all integers \(z = n \in \mathbb{Z}\). [en.wikipedia](https://en.wikipedia.org/wiki/Sine_and_cosine)
- A natural “Weierstrass-style” product with exactly these zeros is
  \[
  f(z) := z \prod_{n=1}^{\infty}\left(1 - \frac{z}{n}\right)\left(1 + \frac{z}{n}\right)
       = z \prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).
  \] [en.wikipedia](https://en.wikipedia.org/wiki/Infinite_product)

Provided the product converges (which it does, by standard infinite product theory for entire functions of small order), \(f\) is entire and has simple zeros exactly at \(z \in \mathbb{Z}\). Thus \(\sin(\pi z)\) and \(f(z)\) are both entire with the same zero set and multiplicities. [en.wikipedia](https://en.wikipedia.org/wiki/Infinite_product)

By the identity theorem for holomorphic functions, their ratio has no zeros or poles, hence is an entire function with no zeros. Therefore [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)
\[
\frac{\sin(\pi z)}{f(z)} = e^{g(z)}
\]
for some entire function \(g(z)\). [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

***

## 3. Show the ratio is actually constant

Define
\[
h(z) := \frac{\sin(\pi z)}{z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)}.
\] [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

From above, \(h(z) = e^{g(z)}\) is entire and never zero. [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

To see that \(g\) is constant, one classical route is via the logarithmic derivative:

1. Start from the known partial fraction expansion of \(\pi \cot(\pi z)\):
   \[
   \pi \cot(\pi z) = \frac{1}{z} + \sum_{n=1}^{\infty} \frac{2z}{z^{2} - n^{2}},\quad z\notin\mathbb{Z}.[]
   \]
   This can be obtained, for example, by residue calculus or Mittag–Leffler. [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

2. Note that
   \[
   \frac{d}{dz}\log\sin(\pi z)
   = \frac{\sin'(\pi z)}{\sin(\pi z)}\cdot\pi
   = \pi\cot(\pi z).
   \] [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

3. Compute the logarithmic derivative of the candidate product:
   \[
   \log\big(\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})\big)
   = \log(\pi z) + \sum_{n=1}^{\infty}\log\left(1 - \frac{z^{2}}{n^{2}}\right).
   \] [en.wikipedia](https://en.wikipedia.org/wiki/Infinite_product)

   Differentiating termwise (justified by uniform convergence on compact sets away from the zeros),
   \[
   \frac{d}{dz}\log\big(\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})\big)
   = \frac{1}{z} + \sum_{n=1}^{\infty}\frac{-2z/n^{2}}{1 - z^{2}/n^{2}}
   = \frac{1}{z} + \sum_{n=1}^{\infty}\frac{2z}{z^{2} - n^{2}}.
   \] [en.wikipedia](https://en.wikipedia.org/wiki/Infinite_product)

4. Compare with the expansion from step 1:
   \[
   \frac{d}{dz}\log\sin(\pi z) = \frac{d}{dz}\log\Big(\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})\Big).\] [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

Hence
\[
\frac{d}{dz}\log\frac{\sin(\pi z)}{\pi z\prod_{n=1}^{\infty}(1 - z^{2}/n^{2})} = 0,
\]
so the logarithm of the ratio is constant; i.e., \(g(z)\) is constant and
\[
\sin(\pi z) = C\,\pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
\]
for some constant \(C\in\mathbb{C}\). [math.ucdavis](http://math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/mat205a-2018-hw5.pdf)

***

## 4. Determine the constant via the Taylor expansion

Finally, expand near \(z=0\).

- Maclaurin for \(\sin(\pi z)\) is
  \[
  \sin(\pi z) = \pi z - \frac{\pi^{3}}{6}z^{3} + O(z^{5}).
  \] [en.wikipedia](https://en.wikipedia.org/wiki/Sine_and_cosine)

- For the product side, note that
  \[
  \prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
  = 1 - \left(\sum_{n=1}^{\infty}\frac{1}{n^{2}}\right)z^{2} + O(z^{4}),
  \] [youtube](https://www.youtube.com/watch?v=wUsIlK_sP60)
  because the linear term vanishes and the quadratic term is minus the sum of \(1/n^{2}\). [youtube](https://www.youtube.com/watch?v=wUsIlK_sP60)

  So
  \[
  \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right)
  = \pi z - \pi z\left(\sum_{n=1}^{\infty}\frac{1}{n^{2}}\right)z^{2} + O(z^{5})
  = \pi z - \pi\left(\sum_{n=1}^{\infty}\frac{1}{n^{2}}\right)z^{3} + O(z^{5}).
  \] [youtube](https://www.youtube.com/watch?v=wUsIlK_sP60)

Comparing coefficients of \(z\) shows immediately that \(C = 1\). (The comparison at \(z^{3}\) then retrieves the Basel sum \(\sum_{n=1}^{\infty}1/n^{2} = \pi^{2}/6\), but you do not need that to fix \(C\) if you simply look at the leading term.) [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

Thus
\[
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right),
\] [ams](https://www.ams.org/bookstore/pspdf/gsm-97-prev.pdf)
and in the original variable \(x\),
\[
\boxed{\sin x = x\prod_{n=1}^{\infty}\left(1 - \frac{x^{2}}{\pi^{2}n^{2}}\right).}[][]

***

## 5. Alternative, more “Weierstrass” viewpoint

There is a closely related derivation using general Weierstrass factorization: for an entire function of order 1 whose zeros are the integers, Weierstrass theory gives a product of the form
\[
\sin(\pi z) = e^{az+b}z\prod_{n\neq 0}\left(1 - \frac{z}{n}\right)e^{z/n},\][][]
and additional symmetry (oddness and boundedness on vertical strips) forces \(a = 0\), while scaling at 0 fixes \(b = 0\), leading again to Euler’s product.[][]


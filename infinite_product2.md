
There is a clean infinite product for \(\tan x\) built from its zeros and poles, analogous to \(\sin x\), but \(\arctan x\) does **not** admit a nontrivial global Weierstrass-type product as an entire function because it is not entire and has no zeros. So I’ll give a rigorous product for \(\tan x\), and explain why an analogous one for \(\arctan x\) is not available in the same sense.

***

## Infinite product for \(\tan x\)

Recall Euler’s sine product
\[
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right), 
\]
and similarly for cosine, from which we can get a product for \(\tan(\pi z) = \dfrac{\sin(\pi z)}{\cos(\pi z)}\). [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

### Step 1: Products for \(\sin\) and \(\cos\)

Using Weierstrass (or the earlier derivation you saw) we have
\[
\sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1 - \frac{z^{2}}{n^{2}}\right).[][]
\]

There is a corresponding product for \(\cos(\pi z)\) whose zeros are at the half-integers:
\[
\cos(\pi z) = \prod_{n=1}^{\infty}\left(1 - \frac{4z^{2}}{(2n-1)^{2}}\right).[]
\]
This comes from the same logic: entire function, zeros at \(z=\tfrac{2n-1}{2}\), simple, order 1; then fix the multiplicative constant by comparing the value at \(z=0\). [www-elsa.physik.uni-bonn](http://www-elsa.physik.uni-bonn.de/~dieckman/InfProd/InfProd.html)

### Step 2: Divide to get \(\tan\)

Define
\[
\tan(\pi z) = \frac{\sin(\pi z)}{\cos(\pi z)}.
\]
Using the two products above,
\[
\tan(\pi z)
= \frac{\pi z\prod_{n=1}^{\infty}\left(1 - \dfrac{z^{2}}{n^{2}}\right)}
       {\prod_{n=1}^{\infty}\left(1 - \dfrac{4z^{2}}{(2n-1)^{2}}\right)}.[][]
\]

Thus
\[
\boxed{
\tan(\pi z)
= \pi z\prod_{n=1}^{\infty}
\frac{1 - \dfrac{z^{2}}{n^{2}}}{1 - \dfrac{4z^{2}}{(2n-1)^{2}}}
}.
\] [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

In the usual variable \(x\), putting \(z = x/\pi\),
\[
\boxed{
\tan x = x\prod_{n=1}^{\infty}
\frac{1 - \dfrac{x^{2}}{\pi^{2}n^{2}}}{1 - \dfrac{4x^{2}}{\pi^{2}(2n-1)^{2}}}
}.
\] [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

This is the natural “Euler-type” infinite product for \(\tan x\), expressed purely in terms of its zeros \(x = k\pi\) and poles \(x = \tfrac{\pi}{2} + k\pi\). [parabola.unsw.edu](https://www.parabola.unsw.edu.au/sites/default/files/2024-02/vol57_no2_3.pdf)

If you want a “from scratch” derivation similar in spirit to the cotangent–Mittag-Leffler argument, you can also start from the partial fraction expansion
\[
\pi \cot(\pi z) = \frac{1}{z} + \sum_{n=1}^{\infty}\frac{2z}{z^{2}-n^{2}},\quad
\pi \tan(\pi z) = \sum_{n=-\infty}^{\infty}\frac{1}{z - (n+\tfrac12)}, 
\]
then integrate to get a logarithm of a product, and finally exponentiate. The result matches the product above up to a constant factor, which you fix by local expansion near \(0\). [people.math.binghamton](https://people.math.binghamton.edu/dikran/478/Ch6.pdf)

***

## Why there is no analogous infinite product for \(\arctan x\)

A Weierstrass-style “infinite product representation” is fundamentally a representation of **entire** functions in terms of their zeros:
\[
f(z) = e^{g(z)}\prod_{n} E_p\left(\frac{z}{z_n}\right),
\]
where \(z_n\) are zeros of \(f\). [en.wikipedia](https://en.wikipedia.org/wiki/Infinite_product)

\(\arctan z\) is not a suitable candidate for such a product:

- \(\arctan z\) is not entire: it is only analytic on \(\mathbb{C}\setminus\{i,-i\}\) because it satisfies \(\tan(\arctan z) = z\) and \(\tan w\) has poles at \(\frac{\pi}{2}+k\pi\), which translate into logarithmic branch points for \(\arctan\) in its complex definition. [en.wikipedia](https://en.wikipedia.org/?title=Tan%28x%29)
- Over \(\mathbb{C}\), the standard branch of \(\arctan z\) has no zeros other than \(z=0\), so there is no nontrivial infinite set of zeros to encode in a product. [en.wikipedia](https://en.wikipedia.org/wiki/Arctangent_series)

Instead, \(\arctan x\) is naturally represented by **series** or integrals, not products, e.g.
\[
\arctan x = \int_{0}^{x}\frac{1}{1+t^{2}}\,dt
= x - \frac{x^{3}}{3} + \frac{x^{5}}{5} - \cdots,\quad |x|\le 1.[]
\]
There are also various special arctan identities (Machin-type formulas) that express constants like \(\pi\) as finite linear combinations of \(\arctan(1/n)\), but these are finite combinations, not infinite products for the function \(\arctan x\) itself. [en.wikipedia](https://en.wikipedia.org/wiki/Arctangent_series)

You can of course produce **products whose values are arctan constants**, for example by integrating products involving \(\cos x\) or \(\sin x\) and comparing to \(\arctan\) limits, but there is no standard closed-form infinite product “for \(\arctan x\)” analogous to Euler’s sine product or the \(\tan x\) product above. [www-elsa.physik.uni-bonn](http://www-elsa.physik.uni-bonn.de/~dieckman/InfProd/InfProd.html)

***


Sure — here are a few worked examples, starting from the simplest polynomial case and then moving to a genuinely complex-coefficient example. The main tool is to compute convergents and, when possible, identify the limit from a recurrence or a known theorem. [arxiv](https://arxiv.org/abs/1812.08251)

## Example 1

Consider
\[
K_{n=1}^{\infty}\frac{n+1}{n}
=
\cfrac{2}{1+\cfrac{3}{2+\cfrac{4}{3+\cdots}}}.
\]
This is the special case \(\alpha=1\) of the family \(K_{n=1}^{\infty}(n^\alpha+1)/n^\alpha=1\), so its value is exactly 1. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

To see it numerically, compute the first few convergents from the bottom upward:
- \(C_1=2/1=2\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- \(C_2=2/(1+3/2)=4/5=0.8\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- \(C_3=2/(1+3/(2+4/3))=14/13\approx 1.0769\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- \(C_4=2/(1+3/(2+4/(3+5/4)))=44/53\approx 0.8302\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

These oscillate, but the theorem gives the exact limit 1. More generally, replacing \(n\) by \(n^\alpha\) still gives limit 1 for every \(\alpha>0\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

## Example 2

Now take a higher-degree rational-limit example from the paper:
\[
K_{n=1}^{\infty}\frac{(n+1)^2f_n+4n+5}{n^2f_n+4n-4}=4,
\]
for suitable polynomial sequences \(f_n\ge 1\).  If we choose the simplest option \(f_n=1\), this becomes [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
\[
K_{n=1}^{\infty}\frac{n^2+6n+6}{n^2+4n-4}=4.
\]
That is already a bona fide polynomial continued fraction with equal numerator and denominator degree. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

Let us write out the first terms:
- \(n=1\): \(a_1=13,\ b_1=1\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- \(n=2\): \(a_2=22,\ b_2=8\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- \(n=3\): \(a_3=33,\ b_3=17\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

So the continued fraction begins
\[
\cfrac{13}{1+\cfrac{22}{8+\cfrac{33}{17+\cdots}}}.
\]
Using only the first term gives \(13\); using two terms gives \(13/(1+22/8)=104/30\approx 3.4667\); using three terms gives \(13/(1+22/(8+33/17))\approx 4.189\).  The exact theorem says the infinite limit is 4. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

## Example 3

Here is an irrational-limit polynomial continued fraction:
\[
1-\frac{1}{1+K_{n=1}^{\infty}\frac{n^2}{n^2+2n}}=J_0(2),
\]
where \(J_0\) is the Bessel function of the first kind of order 0.  This shows that polynomial continued fractions do not just give rational constants; they can also encode special-function values. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

Let
\[
X=K_{n=1}^{\infty}\frac{n^2}{n^2+2n}.
\]
Then the identity says \(1-\frac{1}{1+X}=J_0(2)\), so solving for \(X\) gives
\[
X=\frac{J_0(2)}{1-J_0(2)}.
\]
That algebra is immediate from the stated formula. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

A few convergents of \(X\) are easy to compute:
- First term: \(1/3\approx 0.3333\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- Two terms: \(1/(3+4/8)=2/7\approx 0.2857\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
- Three terms: \(1/(3+4/(8+9/15))\approx 0.2914\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

So the value settles near a non-rational constant determined by \(J_0(2)\). The paper presents this as one of its basic irrational examples. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

## Example 4

For a truly complex-parameter example, the paper proves that if \(x,a\in\mathbb{C}\), \(a\neq 0\), and \(x\neq -ka\) for positive integers \(k\), then
\[
\frac{x+a}{a+K_{n=1}^{\infty}\frac{(x+na)^2-a^2}{a}}=1.
\]
Equivalently,
\[
K_{n=1}^{\infty}\frac{(x+na)^2-a^2}{a}=x.
\]
So this gives a family of continued fractions whose value is a prescribed complex number \(x\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

Pick \(a=1\) and \(x=i\). Then
\[
K_{n=1}^{\infty}\big((i+n)^2-1\big)=i,
\]
because the denominator polynomial is the constant 1.  Expanding the numerator, [arxiv](https://arxiv.org/pdf/2409.06086.pdf)
\[
(i+n)^2-1=n^2+2in-2.
\]
So the continued fraction is
\[
\cfrac{-1+2i}{1+\cfrac{2+4i}{1+\cfrac{7+6i}{1+\cfrac{14+8i}{1+\cdots}}}}.
\]
This is a worked example of a polynomial continued fraction with complex coefficients and complex value \(i\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

The recurrence used in the proof is
\[
G_{-1}=1,\qquad
G_n=(-1)^{n+1}\prod_{j=0}^{n}(i+j),
\]
with \(a_n=(i+n-1)(i+n+1)\) and \(b_n=1\). Those satisfy \(G_n=a_nG_{n-2}+b_nG_{n-1}\), and Pincherle’s theorem then yields limit \(-G_0/G_{-1}=i\). [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

## Example 5

It also helps to remember the “classical” convergent recurrence. For a continued fraction with partial quotients \(a_0,a_1,a_2,\dots\), the convergent numerators and denominators satisfy \(A_n=a_nA_{n-1}+A_{n-2}\) and \(B_n=a_nB_{n-1}+B_{n-2}\).  In the real case, the Utah notes work this out explicitly for examples such as \([1;1,1,1,\dots]\), whose convergents are Fibonacci ratios approaching \((1+\sqrt5)/2\). [arxiv](https://arxiv.org/abs/1812.08251)

That same recurrence viewpoint is what sits behind many polynomial continued fractions too: once you identify a compatible recurrence sequence \(G_n\), you can often read off the limit.  In practice, that is the cleanest way to build worked examples rather than trying to guess the limit from raw expansion alone. [arxiv](https://arxiv.org/pdf/2409.06086.pdf)

Would you like the next batch to focus on complex-valued examples only, or on examples where we derive the limit step by step from the recurrence?

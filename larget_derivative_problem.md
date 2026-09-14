For  
\[
f(x)=e^{2x}\sin(3x),
\]
find the \(n\)-th derivative, eg, n=3030.    
\[
\boxed{f^{(n)}(x)=13^{n/2}e^{2x}\sin\!\left(3x+n\arctan\frac{3}{2}\right)}
\]

Equivalently, since \(\sqrt{13}^{\,n}=13^{n/2}\),

\[
\boxed{f^{(n)}(x)=(\sqrt{13})^n e^{2x}\sin\!\left(3x+n\tan^{-1}\!\frac32\right)}.
\]

This follows from the product rule and chain rule: differentiating \(e^{2x}\) contributes a factor of \(2\), while differentiating \(\sin(3x)\) contributes a factor of \(3\) and changes sine to cosine. Higher derivatives of a product can also be expressed through the generalized product (Leibniz) rule. [math.ucdavis](https://math.ucdavis.edu/~kouba/Math17BHWDIRECTORY/Derivatives.pdf)

## First few derivatives

\[
f(x)=e^{2x}\sin(3x)
\]

\[
f'(x)=e^{2x}\bigl(2\sin(3x)+3\cos(3x)\bigr)
\]

\[
f''(x)=e^{2x}\bigl(-5\sin(3x)+12\cos(3x)\bigr)
\]

\[
f^{(3)}(x)=e^{2x}\bigl(-46\sin(3x)+9\cos(3x)\bigr)
\]

So the coefficients of \(\sin(3x)\) and \(\cos(3x)\) change each time, but the functional shape never leaves

\[
e^{2x}\bigl(A_n\sin(3x)+B_n\cos(3x)\bigr).
\]

## Why the factor is \(\sqrt{13}\)

Suppose one derivative has the form

\[
e^{2x}\left(A\sin(3x)+B\cos(3x)\right).
\]

Differentiating gives

\[
\frac{d}{dx}
\left[e^{2x}(A\sin 3x+B\cos 3x)\right]
=
e^{2x}\left((2A-3B)\sin 3x+(3A+2B)\cos 3x\right).
\]

Thus the coefficient pair evolves as

\[
\begin{pmatrix}
A_{n+1}\\
B_{n+1}
\end{pmatrix}
=
\begin{pmatrix}
2 & -3\\
3 & 2
\end{pmatrix}
\begin{pmatrix}
A_n\\
B_n
\end{pmatrix}.
\]

That transformation is “multiply by” the complex number \(2+3i\), whose magnitude is

\[
|2+3i|=\sqrt{2^2+3^2}=\sqrt{13},
\]

and whose argument is

\[
\theta=\arctan\!\left(\frac32\right).
\]

Every differentiation therefore:

- multiplies the amplitude by \(\sqrt{13}\);
- advances the trigonometric phase by \(\theta=\arctan(3/2)\).

After \(n\) derivatives, the amplitude is \((\sqrt{13})^n\) and the accumulated phase shift is \(n\theta\).

## Alternative exact form

Using complex exponentials,

\[
e^{2x}\sin(3x)=\Im\left(e^{(2+3i)x}\right).
\]

Since differentiating \(e^{(2+3i)x}\) \(n\) times multiplies it by \((2+3i)^n\),

\[
f^{(n)}(x)=\Im\left((2+3i)^n e^{(2+3i)x}\right).
\]

This is also a compact and useful form:

\[
\boxed{
f^{(n)}(x)=\Im\left((2+3i)^n e^{(2+3i)x}\right)
}.
\]

For example, putting \(n=1\) in the phase formula gives

\[
\sqrt{13}e^{2x}\sin\left(3x+\arctan\frac32\right)
=
e^{2x}\bigl(2\sin 3x+3\cos 3x\bigr),
\]

which agrees with the direct derivative.


Great — let’s build one ourselves from scratch by choosing a simple \(G_n\), forcing the recurrence, and then reading off the limit. This is exactly the constructive idea behind Proposition 1 and Corollary 5 in the paper. [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

## Setup

Start with the recurrence
\[
a_nG_{n-2}+b_nG_{n-1}-G_n=0.
\]
If we can find sequences \(G_n,a_n,b_n\) satisfying this, then Proposition 1 lets us create a new continued fraction with partial numerators and denominators
\[
s_n=f_nG_{n-1}+a_n,\qquad t_n=f_nG_{n-2}-b_n,
\]
and its limit is
\[
\frac{G_0}{G_{-1}},
\]
provided \(G_n/B_n\to 0\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

So the plan is:
- Choose an easy polynomial \(G_n\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)
- Solve for simple \(a_n,b_n\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)
- Insert any polynomial \(f_n\ge 1\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)
- Get a whole family of polynomial continued fractions with a known limit. [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

## Choose \(G_n\)

Let us choose
\[
G_n=(n+2)^2.
\]
This is a simple quadratic, so
\[
G_{n-2}=n^2,\qquad G_{n-1}=(n+1)^2,\qquad G_n=(n+2)^2.
\]
This is the same seed used in Corollary 5(iii), but here we will derive the continued fraction instead of just quoting it. [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

We now want linear polynomials
\[
a_n=An+B,\qquad b_n=Cn+D
\]
such that
\[
(An+B)n^2+(Cn+D)(n+1)^2=(n+2)^2
\]
for all \(n\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

## Solve for \(a_n,b_n\)

Expand the left-hand side:
\[
(An+B)n^2=An^3+Bn^2,
\]
and
\[
(Cn+D)(n+1)^2=(Cn+D)(n^2+2n+1)=Cn^3+(2C+D)n^2+(C+2D)n+D.
\]
So the total is
\[
(A+C)n^3+(B+2C+D)n^2+(C+2D)n+D.
\]
We want this to equal
\[
(n+2)^2=n^2+4n+4.
\]
Matching coefficients gives
\[
A+C=0,\qquad B+2C+D=1,\qquad C+2D=4,\qquad D=4.
\]
From \(D=4\), the third equation gives \(C=-4\), then \(A=4\), and then \(B+2(-4)+4=1\) gives \(B=5\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

So we have found
\[
a_n=4n+5,\qquad b_n=-4n+4.
\]
That means the recurrence
\[
(4n+5)G_{n-2}+(-4n+4)G_{n-1}=G_n
\]
holds identically. [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

## Build the fraction

Now apply Proposition 1. Pick any polynomial sequence \(f_n\ge 1\), for example \(f_n=n^{10}\), and define
\[
s_n=f_nG_{n-1}+a_n,\qquad t_n=f_nG_{n-2}-b_n.
\]
Since \(G_{n-1}=(n+1)^2\) and \(G_{n-2}=n^2\), this becomes
\[
s_n=(n+1)^2f_n+4n+5,
\]
\[
t_n=n^2f_n+4n-4.
\]
Therefore
\[
K_{n=1}^{\infty}\frac{(n+1)^2f_n+4n+5}{n^2f_n+4n-4}
\]
is a polynomial continued fraction built directly from our chosen recurrence. [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

The limit is now immediate:
\[
\frac{G_0}{G_{-1}}=\frac{(0+2)^2}{(-1+2)^2}=\frac{4}{1}=4.
\]
So we have derived from scratch the family
\[
K_{n=1}^{\infty}\frac{(n+1)^2f_n+4n+5}{n^2f_n+4n-4}=4.
\]
This is exactly Corollary 5(iii). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

## Concrete instance

Take \(f_n=n^{10}\). Then
\[
K_{n=1}^{\infty}\frac{n^{10}(n+1)^2+4n+5}{n^{12}+4n-4}=4.
\]
Expanding the numerator gives
\[
n^{12}+2n^{11}+n^{10}+4n+5,
\]
so we recover the explicit example
\[
K_{n=1}^{\infty}\frac{n^{12}+2n^{11}+n^{10}+4n+5}{n^{12}+4n-4}=4,
\]
which appears in the paper as equation (1.9). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

The first few partial quotients are:
- \(n=1\): \(13/1\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)
- \(n=2\): \(9225/4104\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)
- \(n=3\): \(248066/531453\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

Even though the terms look messy, the recurrence certificate \(G_n=(n+2)^2\) tells us the infinite value is exactly 4. That is the main power of the method. [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

## Pattern to reuse

This derivation is reusable. Pick a polynomial \(G_n\), usually of low degree, then solve the identity
\[
a_nG_{n-2}+b_nG_{n-1}=G_n
\]
for lower-degree polynomials \(a_n,b_n\); after that, Proposition 1 turns the seed solution into infinitely many polynomial continued fractions with limit \(G_0/G_{-1}\). [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

A good next exercise is to start with a different seed, such as \(G_n=mn+k\) or \(G_n=n(n+1)m+1\), and derive a family with limit \(k/(k-m)\) or 1 in the same way.  Would you like to do the next one with a linear \(G_n\) or a complex-valued seed \(G_n\)? [fim.uni-passau](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf)

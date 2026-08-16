
https://www.perplexity.ai/search/cccfe100-0282-40d2-9a2c-4e633b2f29dc

Analytic continuation is the process of extending a holomorphic function beyond the region where one formula—often a power series—initially converges, while preserving its values on the overlap. The key fact is **uniqueness**: on a connected domain, two holomorphic extensions that agree on any open region must agree everywhere they are both defined. [math.berkeley](https://math.berkeley.edu/~nikhil/courses/185.f15/1123.pdf)

## The basic idea

A Taylor series is a *local* description. Its radius of convergence is limited by the nearest singularity of the represented function—not necessarily by a true boundary of the function’s natural domain.

Suppose \(f\) is holomorphic on \(U\), and \(F\) is holomorphic on a larger domain \(V\supset U\). If

\[
F(z)=f(z)\qquad(z\in U),
\]

then \(F\) is an analytic continuation of \(f\) from \(U\) to \(V\).

Think of it as overlapping coordinate charts: define the function near one point, then use an equivalent holomorphic formula on an overlapping region, and keep moving outward.

## Example 1: A geometric series

Start with the elementary power series

\[
f(z)=1+z+z^2+z^3+\cdots=\sum_{n=0}^{\infty}z^n,
\qquad |z|<1.
\]

Within \(|z|<1\), finite geometric-sum algebra gives

\[
(1-z)\sum_{n=0}^{N}z^n=1-z^{N+1}.
\]

Taking \(N\to\infty\) when \(|z|<1\) yields

\[
f(z)=\frac{1}{1-z}.
\]

The series itself stops converging once \(|z|\ge 1\), but the rational function

\[
F(z)=\frac{1}{1-z}
\]

is holomorphic on the much larger domain \(\mathbb C\setminus\{1\}\). Therefore \(F\) is the analytic continuation of the original series.

For example, the series does not converge at \(z=2\), but analytic continuation assigns

\[
f(2)\quad\leadsto\quad F(2)=\frac{1}{1-2}=-1.
\]

This does **not** mean \(1+2+4+\cdots=-1\) in the ordinary sense. It means the holomorphic function initially represented by that series has a well-defined extension whose value at \(2\) is \(-1\). This standard example appears in complex-analysis notes as continuation from the unit disk to \(\mathbb C\setminus\{1\}\). [math.uci](https://www.math.uci.edu/~brusso/220C051908.pdf)

## Polynomial functions: continuation is already global

Let

\[
p(z)=z^4-3z^2+2z+7.
\]

You could encounter it locally through its Taylor expansion about, say, \(z_0=1\):

\[
p(z)=7+? 
\]

More systematically, because \(p\) is a polynomial, its Taylor expansion about any center \(a\) is finite:

\[
p(z)=\sum_{k=0}^{4}\frac{p^{(k)}(a)}{k!}(z-a)^k.
\]

A finite polynomial expansion converges for every \(z\in\mathbb C\). Thus a polynomial is entire: it has no finite singularities and needs no nontrivial analytic continuation beyond \(\mathbb C\).

This illustrates a useful rule:

- The Taylor radius for a polynomial is \(\infty\).
- The Taylor radius for a non-polynomial holomorphic function equals the distance to the closest obstruction to holomorphic extension.

For example, if you were only given local data

\[
f(z)=1+2(z-1)+3(z-1)^2+(z-1)^4,
\]

that formula already defines the same polynomial everywhere in \(\mathbb C\). Analytic continuation is immediate and unique.

## Rational functions: poles are the obstructions

Consider

\[
R(z)=\frac{1}{1+z^2}.
\]

Around \(z=0\), use the geometric-series identity with \(w=-z^2\):

\[
\frac{1}{1+z^2}
=
\frac{1}{1-(-z^2)}
=
\sum_{n=0}^{\infty}(-1)^n z^{2n},
\qquad |z|<1.
\]

So locally,

\[
1-z^2+z^4-z^6+\cdots.
\]

Why only \(|z|<1\)? The rational function has poles at

\[
z=i,\qquad z=-i,
\]

both distance \(1\) from \(0\). The local series cannot cross those singularities. But the function itself is perfectly holomorphic at every other point, so its analytic continuation is simply

\[
R(z)=\frac{1}{1+z^2}
\quad\text{on}\quad
\mathbb C\setminus\{i,-i\}.
\]

For instance, at \(z=2\), the original series diverges, but the continuation gives

\[
R(2)=\frac{1}{5}.
\]

More generally, every rational function

\[
\frac{P(z)}{Q(z)}
\]

is holomorphic on \(\mathbb C\) except at the zeros of \(Q\) that do not cancel with \(P\). Its Taylor series centered at \(a\) converges up to the nearest such pole.

## A removable-singularity example

Consider the formula

\[
f(z)=\frac{z^2-1}{z-1},
\qquad z\ne 1.
\]

Algebraically,

\[
f(z)=z+1,\qquad z\ne 1.
\]

The expression appears undefined at \(z=1\), but this is not a genuine singularity: define

\[
F(z)=z+1
\]

for every \(z\in\mathbb C\). Then \(F\) is entire and agrees with \(f\) wherever \(f\) was originally defined. Hence \(F\) is the analytic continuation across the removable singularity, with

\[
F(1)=2.
\]

Contrast that with

\[
\frac{1}{z-1}.
\]

At \(z=1\) the singularity is a pole, so no holomorphic continuation across \(1\) exists.

## Beyond rational functions: logarithm

The logarithm shows that continuation may depend on the path used. Near \(z=1\),

\[
\log z
=
\sum_{n=1}^{\infty}
\frac{(-1)^{n+1}}{n}(z-1)^n,
\qquad |z-1|<1.
\]

This gives a local holomorphic branch satisfying \(\log 1=0\). One can continue it throughout a slit plane such as

\[
\mathbb C\setminus(-\infty,0],
\]

giving the principal branch \(\operatorname{Log}z\). But continuing around a closed loop encircling \(0\) changes the value by \(2\pi i\):

\[
\log z \longmapsto \log z+2\pi i.
\]

So unlike a rational function, there is no single-valued holomorphic logarithm on all of \(\mathbb C\setminus\{0\}\). A branch cut selects a simply connected domain on which one branch is single-valued. [en.wikipedia](https://en.wikipedia.org/wiki/Analytic_continuation)

The hierarchy is therefore:

| Function type | Natural holomorphic domain | What blocks continuation? |
|---|---|---|
| Polynomial | All \(\mathbb C\) | Nothing at finite points |
| Rational function | \(\mathbb C\) minus poles | Genuine poles |
| Removable rational singularity | All \(\mathbb C\) after filling in | Only an artificial formula-level hole |
| \(\log z\) | A chosen slit domain | Branch point at \(0\), with monodromy |
| Algebraic roots such as \(\sqrt z\) | A chosen slit domain / Riemann surface | Branch point and sheet switching |

The central lesson: power-series convergence may end, yet the analytic function can persist. Analytic continuation discovers the larger object; genuine singularities and branch behavior determine where—and in what sense—the extension can exist.


A q-series is, broadly, a power series or infinite product whose terms depend on a parameter \(q\), usually with \(|q|<1\), and much of the subject is built around the q-shifted factorial \((a;q)_n=(1-a)(1-aq)\cdots(1-aq^{n-1})\).  [qseries](https://qseries.org/berndt-on-q.pdf)  
They matter because they connect several big areas at once: partitions, theta functions, q-analogues of classical formulas, and basic hypergeometric series. [qseries](https://qseries.org/berndt-on-q.pdf)

## Core idea

A standard starting point is the q-shifted factorial and its infinite version \((a;q)_\infty\), which appears naturally in many identities and product formulas. [arxiv](https://arxiv.org/pdf/1901.01109.pdf)
From this viewpoint, a q-series is not just “a series with q in it,” but a family of expressions whose behavior often recovers ordinary formulas when \(q \to 1\). [qseries](https://qseries.org/berndt-on-q.pdf)

One basic example is the q-binomial theorem,
\[
\sum_{n=0}^{\infty}\frac{(a;q)_n}{(q;q)_n}z^n=\frac{(az;q)_\infty}{(z;q)_\infty},
\]
valid for \(|q|<1\) and \(|z|<1\).  [qseries](https://qseries.org/berndt-on-q.pdf)  
This is central because many other q-identities can be viewed as refinements, consequences, or extensions of it. [arxiv](https://arxiv.org/pdf/1901.01109.pdf)

## Why \(q\) matters

The parameter \(q\) usually acts like a deformation variable: when \(q\to 1\), q-objects often limit to classical ones. [qseries](https://qseries.org/berndt-on-q.pdf)
For instance, \(\lim_{q\to 1}\frac{(q^\alpha;q)_n}{(1-q)^n}=(\alpha)_n\), which links q-shifted factorials to ordinary rising factorials from hypergeometric series. [arxiv](https://arxiv.org/pdf/1901.01109.pdf)

That is why people call many formulas “q-analogues.” [qseries](https://qseries.org/berndt-on-q.pdf)
A q-analogue preserves the structure of a classical identity while adding finer information through powers of \(q\). [arxiv](https://arxiv.org/pdf/1901.01109.pdf)

## Main families

One major family is the basic hypergeometric series
\[
{}_{p+1}\phi_p(a_1,\dots,a_{p+1};\,b_1,\dots,b_p;\,q,t),
\]
whose successive term ratio is a rational function of \(q^n\). [qseries](https://qseries.org/berndt-on-q.pdf)
These are the q-counterparts of ordinary hypergeometric series and form a large part of the modern theory. [arxiv](https://arxiv.org/pdf/1901.01109.pdf)

Another major family is theta functions, which are also treated as q-series because they arise naturally in identities and infinite product formulas. [qseries](https://qseries.org/berndt-on-q.pdf)
For example, the Jacobi triple product gives a bridge between an infinite sum and an infinite product, making theta functions central to the subject. [qseries](https://qseries.org/berndt-on-q.pdf)

## Combinatorics link

q-series are deeply tied to partition theory through generating functions. [qseries](https://qseries.org/berndt-on-q.pdf)
A famous example is
\[
\sum_{n=0}^{\infty}p(n)q^n=\frac{1}{(q;q)_\infty},
\]
where \(p(n)\) counts partitions of \(n\). [qseries](https://qseries.org/berndt-on-q.pdf)

Euler’s pentagonal number theorem and the Rogers–Ramanujan identities are classic examples showing how q-series encode subtle counting statements about partitions. [qseries](https://qseries.org/berndt-on-q.pdf)
This combinatorial side is one reason q-series show up so often in number theory. [qseries](https://qseries.org/berndt-on-q.pdf)

## Concrete intuition

If ordinary power series are like smooth expansions in a variable, q-series are often like **weighted** expansions where powers of \(q\) record arithmetic or combinatorial structure. [arxiv](https://arxiv.org/pdf/1901.01109.pdf)
For example, \((q;q)_\infty^{-1}\) does not just define a function; it packages all partition numbers into one object. [qseries](https://qseries.org/berndt-on-q.pdf)

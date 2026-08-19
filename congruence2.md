
Let’s unpack the cleanest case:  
\[
p(5n+4)\equiv 0\pmod 5.
\]
The modulus \(5\) enters twice: first through the binomial “freshman’s dream” congruence \((1-q^m)^5\equiv1-q^{5m}\pmod5\), and then through a striking restriction of the residue classes appearing in Euler’s and Jacobi’s \(q\)-series. [maths.unsw.edu](https://www.maths.unsw.edu.au/sites/default/files/mikeh/prc1.pdf)

## Start with Euler’s generating function

Let
\[
E(q):=(q;q)_\infty=\prod_{m\ge1}(1-q^m).
\]
Euler’s partition generating function is
\[
\sum_{n\ge0}p(n)q^n=\frac1{E(q)}.
\]

We want to show that every coefficient whose exponent is \(4\pmod5\) is divisible by \(5\).

The key elementary congruence is
\[
(1-x)^5 \equiv 1-x^5\pmod5,
\]
because every intermediate binomial coefficient \(\binom5j\) is divisible by \(5\). Multiplying this identity with \(x=q^m\) over all \(m\ge1\) yields
\[
E(q)^5
=\prod_{m\ge1}(1-q^m)^5
\equiv
\prod_{m\ge1}(1-q^{5m})
=E(q^5)
\pmod5.
\]

Therefore
\[
\frac1{E(q)}
=\frac{E(q)^4}{E(q)^5}
\equiv
\frac{E(q)^4}{E(q^5)}
\pmod5.
\]

Now write \(J(q):=E(q)^3\). Then
\[
E(q)^4=E(q)J(q),
\]
so
\[
\boxed{
\sum_{n\ge0}p(n)q^n
\equiv
\frac{E(q)J(q)}{E(q^5)}
\pmod5.
}
\]

This is the main reduction: \(1/E(q^5)\) contains only powers \(q^{5r}\), so it cannot change an exponent’s residue class modulo \(5\). Thus we only need to prove that \(E(q)J(q)\) has no terms \(q^{5r+4}\) modulo \(5\). [maths.unsw.edu](https://www.maths.unsw.edu.au/sites/default/files/mikeh/prc1.pdf)

## The residue classes in \(E(q)\)

Euler’s pentagonal-number theorem says
\[
E(q)=\sum_{r\in\mathbb Z}(-1)^r q^{r(3r-1)/2}.
\]

The exponent is a generalized pentagonal number:
\[
\pi(r)=\frac{r(3r-1)}2.
\]

Modulo \(5\), as \(r\) ranges through \(0,1,2,3,4\), these exponents are
\[
0,\ 1,\ 0,\ 2,\ 2 \pmod5.
\]
Hence only the residues \(0,1,2\) occur.

Write
\[
E(q)=E_0(q)+E_1(q)+E_2(q),
\]
where \(E_i\) collects terms with exponent congruent to \(i\pmod5\). In particular,
\[
E_i(q)\in q^i\mathbb Z[[q^5]].
\]

For example, the beginning of \(E(q)\) is
\[
E(q)=1-q-q^2+q^5+q^7-q^{12}-q^{15}+\cdots,
\]
and indeed the exponents reduce mod \(5\) only to \(0,1,2\).

## The residue classes in \(J(q)=E(q)^3\)

Jacobi’s identity gives
\[
J(q)=E(q)^3
=
\sum_{r\ge0}(-1)^r(2r+1)q^{r(r+1)/2}.
\]

The triangular-number exponent is
\[
T(r)=\frac{r(r+1)}2.
\]

Modulo \(5\), the residues of \(T(r)\) are \(0,1,3\). But whenever
\[
T(r)\equiv3\pmod5,
\]
the coefficient \(2r+1\) is divisible by \(5\). Indeed,
\[
T(r)\equiv3\pmod5
\quad\Longleftrightarrow\quad
r(r+1)\equiv1\pmod5,
\]
which happens for \(r\equiv2\pmod5\), and then
\[
2r+1\equiv2(2)+1\equiv0\pmod5.
\]

So after reduction modulo \(5\), all \(q^{5s+3}\)-terms in \(J(q)\) vanish. Therefore
\[
J(q)\equiv J_0(q)+J_1(q)\pmod5,
\]
where
\[
J_i(q)\in q^i\mathbb F_5[[q^5]].
\]

The first few terms make this visible:
\[
J(q)=1-3q+5q^3-7q^6+9q^{10}-11q^{15}+\cdots.
\]
The \(q^3\) coefficient is \(5\), hence zero modulo \(5\); all of the would-be residue-\(3\) terms share that divisibility phenomenon. [maths.unsw.edu](https://www.maths.unsw.edu.au/sites/default/files/mikeh/prc1.pdf)

## Why residue \(4\) disappears

Modulo \(5\),
\[
E(q)J(q)
\equiv
(E_0+E_1+E_2)(J_0+J_1).
\]

The possible exponent residues are therefore only
\[
\{0,1,2\}+\{0,1\}
=
\{0,1,2,3\}\pmod5.
\]

Explicitly:
\[
\begin{array}{c|cc}
 & J_0 & J_1\\
\hline
E_0 & 0 & 1\\
E_1 & 1 & 2\\
E_2 & 2 & 3
\end{array}
\pmod5.
\]

Residue \(4\) never occurs. Consequently,
\[
[q^{5n+4}]\,E(q)J(q)\equiv0\pmod5.
\]

Since
\[
\frac1{E(q^5)}\in\mathbb Z[[q^5]]
\]
only shifts exponents by multiples of \(5\), multiplying by it cannot create a residue-\(4\) term. Thus
\[
[q^{5n+4}]\frac{E(q)J(q)}{E(q^5)}
\equiv0\pmod5.
\]

But this coefficient is exactly \(p(5n+4)\). Therefore
\[
\boxed{p(5n+4)\equiv0\pmod5.}
\]
This is a streamlined version of Ramanujan’s mod-\(5\) argument. [maths.unsw.edu](https://www.maths.unsw.edu.au/sites/default/files/mikeh/prc1.pdf)

## What is special about \(5\)?

The proof succeeds because of a highly coordinated coincidence.

| Ingredient | Modulo \(5\) phenomenon |
|---|---|
| Binomial coefficients | \((1-x)^5\equiv1-x^5\pmod5\) |
| Euler product \(E(q)\) | Pentagonal exponents occupy only \(0,1,2\pmod5\) |
| Jacobi cube \(E(q)^3\) | After coefficient reduction mod \(5\), only \(0,1\pmod5\) remain |
| Sumset of supports | \(\{0,1,2\}+\{0,1\}\) omits \(4\pmod5\) |
| Partition series | The missing class forces \(p(5n+4)\equiv0\pmod5\) |

So the congruence is not merely a numerological pattern in partition counts. It comes from a “support obstruction” in the relevant \(q\)-series modulo \(5\): there is simply no way to assemble exponent class \(4\) from the surviving components.

## Ramanujan’s stronger identity

Ramanujan proved the exact generating-function identity
\[
\boxed{
\sum_{n\ge0}p(5n+4)q^n
=
5\,\frac{(q^5;q^5)_\infty^5}{(q;q)_\infty^6}.
}
\]

The right-hand side is visibly \(5\) times a power series with integer coefficients, immediately proving the congruence coefficient-by-coefficient. [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586220/)

The residue-support proof above explains *why mod \(5\) can eliminate the class \(5n+4\)*. Ramanujan’s identity gives a much sharper result: it identifies the entire extracted subsequence \(\{p(5n+4)\}_{n\ge0}\) as a concrete eta quotient.

## Modular-form viewpoint

Using Dedekind’s eta function
\[
\eta(\tau)=q^{1/24}(q;q)_\infty,
\qquad q=e^{2\pi i\tau},
\]
the partition generating series becomes
\[
\frac1{\eta(\tau)}
=
q^{-1/24}\sum_{n\ge0}p(n)q^n.
\]

More generally, modulo a prime \(\ell\),
\[
\eta(\tau)^\ell\equiv\eta(\ell\tau)\pmod\ell,
\]
which is the eta-function incarnation of
\[
E(q)^\ell\equiv E(q^\ell)\pmod\ell.
\]

Hence
\[
\frac1{\eta(\tau)}
\equiv
\frac{\eta(\tau)^{\ell-1}}{\eta(\ell\tau)}
\pmod\ell.
\]

For \(\ell=5,7,11\), the numerator \(\eta(\tau)^{\ell-1}\) has especially useful theta-series descriptions. Those descriptions show that its nonzero exponents avoid the class \(0\pmod\ell\); because the partition coefficient \(p(n)\) occurs at exponent \(24n-1\), the forbidden condition
\[
24n-1\equiv0\pmod\ell
\]
is equivalent to the three Ramanujan progressions:
\[
\begin{aligned}
24n&\equiv1\pmod5 &&\Longleftrightarrow&& n\equiv4\pmod5,\\
24n&\equiv1\pmod7 &&\Longleftrightarrow&& n\equiv5\pmod7,\\
24n&\equiv1\pmod{11} &&\Longleftrightarrow&& n\equiv6\pmod{11}.
\end{aligned}
\]
That produces the compact uniform formulation
\[
\boxed{
24n\equiv1\pmod\ell
\quad\Longrightarrow\quad
p(n)\equiv0\pmod\ell,
\qquad \ell\in\{5,7,11\}.
}
\]
 [people.mpim-bonn.mpg](https://people.mpim-bonn.mpg.de/zagier/files/preprints/RamanujanCongruence.2015.pdf)

The \(5\)-case is therefore a prototype: the prime modulus enters via Frobenius/binomial reduction, while the “missing progression” comes from the modular or theta-theoretic support of a transformed eta product.

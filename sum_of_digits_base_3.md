
Let \(S(n)\) denote the sum of the base-\(3\) digits of a nonnegative integer \(n\). If
\[
n=\sum_{i=0}^{r} a_i3^i,\qquad a_i\in\{0,1,2\},
\]
then
\[
S(n)=\sum_{i=0}^{r}a_i.
\]
Below is a broad catalogue of useful properties—some are immediate, some invite proof, and some lead naturally to deeper conjectures.

## Fundamental identities

The base-\(3\) expansion gives the recursion
\[
S(3n)=S(n),\qquad S(3n+1)=S(n)+1,\qquad S(3n+2)=S(n)+2.
\]

More generally, for every \(k\ge 0\) and \(0\le r<3^k\),
\[
S(3^k n+r)=S(n)+S(r).
\]
This is because the final \(k\) ternary digits of \(3^k n+r\) are precisely the \(k\)-digit ternary representation of \(r\), allowing leading zeros.

Appending a digit gives:
\[
S(3n+d)=S(n)+d,\qquad d\in\{0,1,2\}.
\]

In particular, multiplying by a power of \(3\) just appends zeros:
\[
S(3^k n)=S(n).
\]

The digit sum is invariant under reversal of the ternary digits. For example,
\[
(21012)_3 \mapsto (21012)_3
\]
has the same digit sum, and in general any permutation of the digits preserves \(S\).

## Congruence and bounds

Since \(3\equiv 1\pmod 2\),
\[
n=\sum_i a_i3^i\equiv \sum_i a_i=S(n)\pmod 2.
\]
Therefore,
\[
\boxed{S(n)\equiv n\pmod 2.}
\]

This is the base-\(3\) analogue of the familiar base-\(10\) congruence modulo \(9\): in base \(b\), digit sum is congruent to the number modulo \(b-1\). [math.hkust.edu](https://www.math.hkust.edu.hk/excalibur/v22_n3.pdf)

Consequences:

- \(n\) is even if and only if \(S(n)\) is even.
- \(n\) is odd if and only if \(S(n)\) is odd.
- The iterated ternary digital root is \(1\) for odd \(n\) and \(2\) for positive even \(n\):
  \[
  S^{\circ m}(n)\in\{1,2\}
  \]
  for all sufficiently large \(m\), with its value equal to \(n\bmod 2\).

If \(3^{r-1}\le n<3^r\), so that \(n\) has \(r\) ternary digits, then
\[
1\le S(n)\le 2r.
\]
The maximum occurs exactly at
\[
n=3^r-1=(\underbrace{22\cdots 2}_{r})_3,
\]
where \(S(n)=2r\).

Thus, for \(n\ge 1\),
\[
S(n)\le 2\bigl(\lfloor\log_3 n\rfloor+1\bigr).
\]
In particular,
\[
S(n)=O(\log n),
\]
while \(n\) itself grows exponentially in the digit length.

Also,
\[
S(n)\le n,
\]
with equality only for \(n=0,1,2\). For \(n\ge 3\), place value makes \(n\) strictly larger than its digit sum.

## Addition, subtraction, and carries

Digit sums are subadditive:
\[
\boxed{S(a+b)\le S(a)+S(b).}
\]

More exactly, every ternary carry replaces a digit-sum contribution of \(3\) by \(1\), decreasing the total digit sum by \(2\). Hence
\[
\boxed{S(a+b)=S(a)+S(b)-2C(a,b),}
\]
where \(C(a,b)\) is the total number of carries that occur when \(a\) and \(b\) are added in base \(3\), counting cascaded carries.

Therefore:

- \(S(a+b)=S(a)+S(b)\) iff there are no carries in ternary addition.
- The difference
  \[
  S(a)+S(b)-S(a+b)
  \]
  is always a nonnegative even integer.
- Equivalently,
  \[
  S(a+b)\equiv S(a)+S(b)\pmod 2,
  \]
  which also follows from \(S(n)\equiv n\pmod2\).

A convenient no-carry criterion: if
\[
a=\sum a_i3^i,\qquad b=\sum b_i3^i,
\]
then
\[
S(a+b)=S(a)+S(b)
\]
exactly when
\[
a_i+b_i\le2
\]
for every digit position \(i\).

For subtraction, if \(a\ge b\), then borrows increase the digit sum by \(2\) each:
\[
S(a-b)=S(a)-S(b)+2B(a,b),
\]
where \(B(a,b)\) is the number of borrows in the ternary subtraction algorithm.

A particularly useful special case is
\[
\boxed{S(3^k-1-n)=2k-S(n)\qquad(0\le n<3^k).}
\]
Indeed, \(3^k-1=(22\cdots2)_3\), so subtraction causes no borrows: each ternary digit \(a_i\) becomes \(2-a_i\).

Thus the digit sums on \([0,3^k-1]\) are symmetric:
\[
S(n)+S(3^k-1-n)=2k.
\]

## Multiplication and special forms

For all nonnegative integers \(a,b\),
\[
\boxed{S(ab)\le S(a)S(b).}
\]

One way to see this is to write \(a\) as a sum of \(S(a)\) powers of \(3\), with repetitions allowed:
\[
a=\sum_{j=1}^{S(a)}3^{u_j}.
\]
Then
\[
ab=\sum_{j=1}^{S(a)}3^{u_j}b.
\]
Before carrying, the digit sum is \(S(a)S(b)\); carrying can only reduce it by multiples of \(2\).

Likewise,
\[
S(ab)\le aS(b),\qquad S(ab)\le bS(a).
\]

Useful special cases:

\[
S(2n)\le 2S(n).
\]

Equality \(S(2n)=2S(n)\) holds exactly when doubling the ternary digits creates no carries, i.e. when every ternary digit of \(n\) is \(0\) or \(1\). Thus:
\[
S(2n)=2S(n)
\iff
n\text{ has no ternary digit }2.
\]

If \(n\) has only ternary digits \(0,1\), then
\[
S(n)=\#\{\text{nonzero ternary digits of }n\},
\]
so \(S(n)\) is the Hamming weight of its ternary representation.

For repunits,
\[
R_k=1+3+\cdots+3^{k-1}=\frac{3^k-1}{2}=(\underbrace{11\cdots1}_k)_3,
\]
we have
\[
S(R_k)=k.
\]

For the all-\(2\) numbers,
\[
3^k-1=(\underbrace{22\cdots2}_k)_3,
\]
we have
\[
S(3^k-1)=2k.
\]

More generally, if \(0\le n<3^k\), then
\[
3^k n-n=(3^k-1)n,
\]
and its digit behavior may be studied as a shifted subtraction; such expressions often create structured carry patterns.

## Exact distribution on ternary blocks

Among the integers
\[
0,1,\ldots,3^k-1,
\]
every ternary string of length \(k\) occurs exactly once. Hence the generating polynomial for the digit sums is
\[
\boxed{\sum_{n=0}^{3^k-1}x^{S(n)}=(1+x+x^2)^k.}
\]

Therefore the number of \(n\in[0,3^k)\) with \(S(n)=m\) equals
\[
[x^m](1+x+x^2)^k.
\]

Equivalently,
\[
\#\{0\le n<3^k:S(n)=m\}
=
\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{k!}{j!(m-2j)!(k-m+j)!},
\]
where \(j\) is the number of digits equal to \(2\), \(m-2j\) is the number equal to \(1\), and the remaining digits are \(0\).

Examples:

- \(S(n)=0\): exactly one number, \(n=0\).
- \(S(n)=1\): exactly \(k\) numbers, namely \(3^0,3^1,\ldots,3^{k-1}\).
- \(S(n)=2\): there are
  \[
  k+\binom{k}{2}
  \]
  such numbers: one digit \(2\), or two digits \(1\).
- \(S(n)=2k\): exactly one number, \(3^k-1\).

The distribution is symmetric:
\[
\#\{n<3^k:S(n)=m\}
=
\#\{n<3^k:S(n)=2k-m\}.
\]
This follows either from the polynomial identity
\[
x^{2k}(1+x^{-1}+x^{-2})^k=(1+x+x^2)^k,
\]
or from the complement map \(n\mapsto3^k-1-n\).

The mean digit sum on this full block is
\[
\frac1{3^k}\sum_{n=0}^{3^k-1}S(n)=k,
\]
because each ternary digit has mean
\[
\frac{0+1+2}{3}=1.
\]

Thus
\[
\boxed{\sum_{n=0}^{3^k-1}S(n)=k3^k.}
\]

The variance is
\[
k\cdot\operatorname{Var}(\text{one ternary digit})
=
k\left(\frac{0^2+1^2+2^2}{3}-1^2\right)
=
\frac{2k}{3}.
\]

For large \(k\), \(S(n)\) for uniformly random \(n<3^k\) is approximately normal:
\[
\frac{S(n)-k}{\sqrt{2k/3}}
\approx N(0,1).
\]
This is an instance of the usual central-limit behavior of digit sums. [math.dartmouth](https://math.dartmouth.edu/~carlp/digits.pdf)

## Further conjectures and research directions

Here are natural statements to investigate; some are standard consequences of digit-sum theory, while others are genuinely deeper.

### 1. Every admissible digit sum occurs infinitely often

For every \(m\ge0\), there are infinitely many \(n\) such that
\[
S(n)=m.
\]

This is immediate: choose \(m\) distinct large positions and let
\[
n=3^{e_1}+3^{e_2}+\cdots+3^{e_m}.
\]
Then \(S(n)=m\). There are infinitely many choices of the exponents.

Moreover, for each fixed \(m\), the count
\[
\#\{n\le x:S(n)=m\}
\]
grows polylogarithmically in \(x\), roughly on the scale of \((\log x)^m\), because numbers with small digit sum correspond to sparse selections of ternary digit positions.

### 2. Typical order

For “most” \(n\le x\),
\[
S(n)\approx \log_3 x.
\]

More precisely, the expected ternary digit sum of a number with about \(k\) digits is \(k\), and \(k\sim \log_3 n\). Thus one expects
\[
S(n)=\log_3 n+O(\sqrt{\log n})
\]
for a typical integer, in a probabilistic sense.

This sharply contrasts with the extremal range:
\[
1\le S(n)\le 2\log_3 n+O(1).
\]

### 3. Parity balance

Since
\[
S(n)\equiv n\pmod2,
\]
exactly half of integers in every sufficiently natural interval have even digit sum and half have odd digit sum whenever the interval contains equally many even and odd integers.

On the exact block \(0\le n<3^k\), there are
\[
\frac{3^k+1}{2}
\]
numbers with even \(S(n)\), including \(0\), and
\[
\frac{3^k-1}{2}
\]
with odd \(S(n)\), because \(3^k\) is odd.

### 4. Values along arithmetic progressions

For fixed \(a,m\), investigate the distribution of
\[
S(an+b)\pmod m.
\]

Natural conjecture: unless a congruence obstruction forces otherwise, these values should become equidistributed as \(n\to\infty\). The modulus \(2\) is exceptional in the strongest possible way:
\[
S(an+b)\equiv an+b\pmod2.
\]

For moduli not explained by the base-\(3\) congruence, digit sums are expected to behave pseudorandomly in many settings.

### 5. Prime inputs

A natural deep conjecture is that the ternary digit sums of primes are normally distributed around \(\log_3 p\). More concretely, among primes \(p<3^k\), one expects \(S(p)\) to be concentrated near \(k\), with fluctuations of order \(\sqrt{k}\).

There is an unavoidable parity restriction:
\[
p\text{ odd}\quad\Longrightarrow\quad S(p)\text{ odd},
\]
apart from the prime \(2\). Therefore, one should only expect distribution among odd digit sums.

A plausible refined heuristic is:
\[
\#\{p<3^k:S(p)=m\}
\]
should be approximately proportional to the number of \(k\)-digit ternary strings with sum \(m\), restricted to odd \(m\), after accounting for primality density.

### 6. Carry statistics

For a fixed \(t\), study
\[
\Delta_t(n)=S(n+t)-S(n).
\]

Because carries reduce digit sum by \(2\),
\[
\Delta_t(n)\equiv t\pmod2.
\]

For \(t=1\), if the ternary expansion of \(n\) ends in exactly \(r\) digits equal to \(2\), then adding \(1\) changes those \(r\) digits to \(0\) and increments the preceding digit:
\[
\boxed{S(n+1)-S(n)=1-2r.}
\]

So:

- If \(n\not\equiv2\pmod3\), then \(S(n+1)-S(n)=1\).
- If \(n\) ends in one \(2\), the change is \(-1\).
- If \(n\) ends in two \(2\)'s, the change is \(-3\).
- In general, arbitrarily large negative jumps occur.

The density of integers ending in exactly \(r\) copies of the digit \(2\) is
\[
\frac{2}{3^{r+1}},
\]
for \(r\ge0\), assuming the digit before that terminal run is \(0\) or \(1\). Hence the increment distribution is explicitly geometric:
\[
S(n+1)-S(n)=1-2r
\]
with asymptotic frequency \(2/3^{r+1}\).

This gives a beautiful phenomenon: although the average change is essentially zero over long intervals, individual changes are highly asymmetric—frequent \(+1\) steps and rarer but arbitrarily large downward drops.

### 7. Self-numbers and Harshad-type questions

One can study ternary analogues of Niven/Harshad numbers:
\[
n\equiv0\pmod{S(n)}.
\]

Natural questions include:

- Are there infinitely many ternary Harshad numbers with prescribed digit sum?
- How often does \(S(n)\mid n\)?
- Are there infinitely many primes \(p\) for which \(S(p)\mid p-1\)?
- For which \(m\) are there infinitely many \(n\) such that \(S(n)=m\) and \(m\mid n\)?

The general idea of a number divisible by its digit sum is the standard Niven/Harshad notion. [ijopcm](https://www.ijopcm.org/Vol/10/IJOPCM(vol.3.2.3.J.10).pdf)

### 8. Digit-sum level sets

For fixed \(m\), the set
\[
A_m=\{n:S(n)=m\}
\]
is very sparse but infinite. It has a clean combinatorial structure: \(n\in A_m\) exactly when its ternary expansion contains a finite multiset of \(m\) “units” spread among place values, with at most two units at each position.

One can ask for additive properties:

- Does \(A_m+A_m\) contain infinitely many elements of \(A_{2m}\)? Yes: choose two members with disjoint nonzero digit positions, so no carries occur.
- Can \(A_m+A_m\) intersect \(A_j\) for every admissible even-parity value \(j\le2m\)? Carries suggest yes, and one can construct many examples.
- Which \(m\) make \(A_m\) contain arbitrarily long arithmetic progressions? Since multiplication by \(3^k\) preserves \(S\), every \(A_m\) contains progressions of the form
  \[
  3^k a,\ 3^k(a+3^\ell),\ 3^k(a+2\cdot3^\ell),\ldots
  \]
  when the digit supports can be arranged without interference.

The base-\(3\) digit-sum function is therefore simultaneously simple—fully determined by ternary digits—and rich enough to encode carries, probabilistic laws, sparse combinatorial sets, and deep questions about primes and arithmetic progressions.

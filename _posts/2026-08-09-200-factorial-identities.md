---
title: "The 200 Factorial Identities You'll Wish You Knew Sooner — From Permutations to the Prime Zoo"
date: 2026-08-09
categories:
  - Combinatorics
  - Mathematics
tags:
  - factorial
  - binomial-coefficients
  - combinatorics
  - stirling-numbers
  - number-theory
  - gamma-function
  - permutations
  - generating-functions
share: true
read_time: true
excerpt: "Factorials generate patterns in divisibility, combinatorics, asymptotics, prime structure, and special functions. These 200 identities span from the elementary to the deep — Legendre's valuation formula, Stirling numbers, Bell numbers, Kummer's theorem, and Wilson primes — weaving together permutations, partitions, and the gamma function into a unified tapestry."
---

**Challenge to the reader:** Compute the number of trailing zeros in $1000!$ without a calculator. Then find the exponent of $7$ in $1000!$ using Legendre's formula. Finally, determine whether $\binom{100}{50}$ is even or odd using Kummer's theorem. All three answers are derivable from the identities in this post.

---

Below, $n, m, k$ are non-negative integers unless stated otherwise; $p$ is prime.

---

## 1. Basic and Divisibility Patterns

**1.** $0! = 1$

**2.** $1! = 1$

**3.** $n! = 1 \cdot 2 \cdot 3 \cdots n$

**4.** $n! = n(n-1)!$ for $n \ge 1$

**5.** $\frac{n!}{(n-1)!} = n$

**6.** Factorials begin $1, 1, 2, 6, 24, 120, 720, \dots$

**7.** $n!$ is strictly increasing for $n \ge 1$

**8.** $n! \mid m!$ whenever $n \le m$

**9.** $\gcd(m!, n!) = \min(m, n)!$

**10.** Every integer $k$ with $1 \le k \le n$ divides $n!$

**11.** Every prime $p \le n$ divides $n!$

**12.** No prime $p > n$ divides $n!$

**13.** $n!$ is even for every $n \ge 2$

**14.** $n!$ is divisible by $6$ for every $n \ge 3$

**15.** $n!$ ends in at least one zero for every $n \ge 5$

**16.** $n! \equiv 0 \pmod n$ for $n \ge 1$

**17.** $n! \equiv 0 \pmod m$ whenever $n \ge m$

**18.** $n! + 1$ is coprime to every $k \in \lbrace 2, \dots, n \rbrace$

**19.** $n! - 1$ is coprime to every $k \in \lbrace 2, \dots, n \rbrace$

**20.** $n! + k \equiv 0 \pmod k$ for each $1 \le k \le n$

**21.** $\operatorname{lcm}(1, 2, \dots, n) \mid n!$

**22.** If $n > 4$ is composite, then $n \mid (n-1)!$

**23.** For prime $p$, $(p-1)! \equiv -1 \pmod p$ — **Wilson's theorem**

**24.** Conversely, if $(n-1)! \equiv -1 \pmod n$, then $n$ is prime

**25.** For prime $p$, $p! \equiv 0 \pmod p$

---

## 2. Prime Factors and Decimal Patterns

The fundamental tool for prime valuations in factorials is Legendre's formula.

**26.** The exponent of prime $p$ in $n!$ is

$$
v_p(n!) = \sum_{j \ge 1} \left\lfloor \frac{n}{p^j} \right\rfloor.
$$

**27.** Equivalently,

$$
v_p(n!) = \frac{n - s_p(n)}{p-1},
$$

where $s_p(n)$ is the sum of the base-$p$ digits of $n$.

**28.** The exponent of $p$ increases by one or more exactly when $n$ is divisible by $p$.

**29.** More precisely, $v_p(n!) - v_p((n-1)!) = v_p(n)$.

**30.** The number of trailing decimal zeros is

$$
v_{10}(n!) = \sum_{j \ge 1} \left\lfloor \frac{n}{5^j} \right\rfloor.
$$

**31.** There are more factors of $2$ than factors of $5$ in $n!$ for $n \ge 1$.

**32.** Therefore, trailing zeros of $n!$ are controlled solely by the number of factors of $5$.

**33.** The trailing-zero count jumps at multiples of $5$.

**34.** It jumps by at least two at multiples of $25$.

**35.** It jumps by at least three at multiples of $125$.

**36.** $v_2(n!) = n - s_2(n)$, using the binary digit sum.

**37.** $n!$ is never prime for $n \ge 2$.

**38.** $n!$ is not a perfect square for $n > 1$.

**39.** In fact, $n!$ is not a nontrivial perfect power for $n > 1$.

**40.** The prime factorization of $n!$ contains exactly the primes no larger than $n$.

---

## 3. Combinatorial Patterns

**41.** $n!$ counts permutations of $n$ distinct objects.

**42.** $\frac{n!}{(n-r)!}$ counts ordered selections of $r$ objects from $n$.

**43.** $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ counts unordered selections of $r$ objects.

**44.** Every binomial coefficient is an integer because $r!(n-r)! \mid n!$.

**45.** The binomial theorem:

$$
(x+y)^n = \sum_{r=0}^{n} \binom{n}{r} x^r y^{n-r}.
$$

**46.** $\sum_{r=0}^{n} \binom{n}{r} = 2^n$

**47.** $\sum_{r=0}^{n} (-1)^r \binom{n}{r} = 0$ for $n \ge 1$

**48.** $\sum_{r=0}^{n} r \binom{n}{r} = n 2^{n-1}$

**49.** $\sum_{r=0}^{n} \binom{n}{r}^2 = \binom{2n}{n}$

**50.** Vandermonde's identity:

$$
\sum_r \binom{a}{r} \binom{b}{n-r} = \binom{a+b}{n}.
$$

**51.** The multinomial coefficient is

$$
\binom{n}{n_1, \dots, n_t} = \frac{n!}{n_1! \cdots n_t!}.
$$

**52.** It counts arrangements of a multiset with multiplicities $n_1, \dots, n_t$.

**53.** The number of cyclic orderings of $n$ labeled objects is $(n-1)!$.

**54.** The number of derangements is

$$
!n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}.
$$

**55.** The derangement count is the nearest integer to $n!/e$.

**56.** The Catalan number is

$$
C_n = \frac{(2n)!}{(n+1)! n!}.
$$

**57.** $C_n = \frac{1}{n+1} \binom{2n}{n}$

**58.** The central binomial coefficient is $\binom{2n}{n} = (2n)! / (n!)^2$.

**59.** The number of ways to partition $n$ labeled objects into blocks of specified sizes uses factorial quotients.

**60.** The unsigned Stirling numbers of the first kind satisfy

$$
\sum_{k=0}^{n} \genfrac{[}{]}{0pt}{}{n}{k} = n!.
$$

---

## 4. Identities and Series

**61.** $k \cdot k! = (k+1)! - k!$

**62.** Hence,

$$
\sum_{k=1}^{n} k \cdot k! = (n+1)! - 1.
$$

**63.** For $n \ge 2$,

$$
n! < \sum_{k=0}^{n} k! < 2n!.
$$

**64.** The reciprocal factorial series gives the most famous constant:

$$
e = \sum_{k=0}^{\infty} \frac{1}{k!}.
$$

**65.** More generally,

$$
e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}.
$$

**66.** The exponential generating function of $n!$ is formally

$$
\sum_{n \ge 0} \frac{n!}{n!} x^n = \frac{1}{1-x}.
$$

**67.** The Gamma function extends factorials:

$$
\Gamma(n+1) = n!.
$$

**68.** Integral form:

$$
n! = \int_0^{\infty} x^n e^{-x}\, dx.
$$

**69.** The beta integral gives

$$
\int_0^1 x^m (1-x)^n\, dx = \frac{m! n!}{(m+n+1)!}.
$$

**70.** The falling factorial is

$$
(x)_{\underline{n}} = x(x-1)\cdots(x-n+1).
$$

**71.** For integer $x = n$, $(n)_{\underline{r}} = n!/(n-r)!$.

**72.** The rising factorial is

$$
(x)^{\overline{n}} = x(x+1)\cdots(x+n-1).
$$

**73.** $(x)_{\underline{n}} = (-1)^n (-x)^{\overline{n}}$

**74.** Falling factorials expand through signed Stirling numbers:

$$
(x)_{\underline{n}} = \sum_{k=0}^{n} s(n,k) x^k.
$$

**75.** $n!$ is the product of the first $n$ positive integers, while $n!!$ skips every other integer.

---

## 5. Growth and Generalized Factorials

**76.** $n! < n^n$ for $n \ge 2$.

**77.** $n! / n^n$ decreases toward zero.

**78.** $n!$ eventually exceeds $a^n$ for every fixed constant $a > 0$.

**79.** Factorial growth is faster than exponential growth but slower than $n^n$.

**80.** Stirling's approximation:

$$
n! \sim \sqrt{2\pi n} \left( \frac{n}{e} \right)^n.
$$

**81.** A refined Stirling approximation multiplies this by approximately $1 + \frac{1}{12n}$.

**82.** Taking logarithms gives

$$
\log(n!) = \sum_{k=1}^{n} \log k.
$$

**83.** Asymptotically,

$$
\log(n!) = n \log n - n + O(\log n).
$$

**84.** The number of decimal digits of $n!$ is

$$
\lfloor \log_{10}(n!) \rfloor + 1.
$$

**85.** The factorial sequence is log-convex:

$$
(n!)^2 < (n-1)! (n+1)!.
$$

**86.** The ratio of adjacent factorials is linear: $n! / (n-1)! = n$.

**87.** The ratio of adjacent reciprocal factorials is $1/n$.

**88.** Even double factorials satisfy

$$
(2n)!! = 2^n n!.
$$

**89.** Odd double factorials satisfy

$$
(2n-1)!! = \frac{(2n)!}{2^n n!}.
$$

**90.** Therefore,

$$
(2n)! = (2n)!! (2n-1)!!.
$$

**91.** The product of the first $n$ odd numbers is $(2n-1)!!$.

**92.** The half-integer Gamma identity:

$$
\Gamma\!\left(n + \tfrac{1}{2}\right) = \frac{(2n)!}{4^n n!} \sqrt{\pi}.
$$

**93.** The $q$-factorial is

$$
[n]_q! = \prod_{k=1}^{n} \frac{1 - q^k}{1 - q}.
$$

**94.** As $q \to 1$, $[n]_q! \to n!$.

**95.** The Gaussian binomial coefficient is

$$
\genfrac{[}{]}{0pt}{}{n}{r}_q = \frac{[n]_q!}{[r]_q! [n-r]_q!}.
$$

**96.** In factorial-base notation, every nonnegative integer has a unique expansion

$$
a_1(1!) + a_2(2!) + \cdots + a_t(t!),
$$

with $0 \le a_i \le i$.

**97.** The superfactorial is $\prod_{k=1}^{n} k!$.

**98.** The hyperfactorial is $\prod_{k=1}^{n} k^k$.

**99.** The central factorial ratio $(2n)!/(n!)^2$ is approximately $4^n / \sqrt{\pi n}$.

**100.** The leading digits of factorials follow Benford-type behavior in the long run.

---

**Mid-post challenge:** Prove that the number of odd entries in row $n$ of Pascal's triangle is $2^{s_2(n)}$, where $s_2(n)$ is the binary digit sum of $n$. Hint: use Kummer's theorem (identity 179) and the fact that no carries occur in binary addition only when the bit patterns are disjoint.

---

## 6. Factorial Quotients and Binomials

**101.** $\frac{(n+r)!}{n!} = (n+1)(n+2)\cdots(n+r)$

**102.** $\frac{n!}{(n-r)!} = n(n-1)\cdots(n-r+1)$

**103.** $\binom{n}{r} = \frac{n^{\underline{r}}}{r!}$, where $n^{\underline{r}}$ is a falling factorial.

**104.** $\binom{n+r-1}{r} = \frac{n^{\overline{r}}}{r!}$, where $n^{\overline{r}}$ is a rising factorial.

**105.** Binomial symmetry: $\binom{n}{r} = \binom{n}{n-r}$.

**106.** Pascal recurrence: $\binom{n}{r} = \binom{n-1}{r} + \binom{n-1}{r-1}$.

**107.** Absorption identity: $r \binom{n}{r} = n \binom{n-1}{r-1}$.

**108.** Complementary absorption: $(n-r) \binom{n}{r} = n \binom{n-1}{r}$.

**109.** Hockey-stick identity:

$$
\sum_{k=r}^{n} \binom{k}{r} = \binom{n+1}{r+1}.
$$

**110.** Alternating hockey-stick identity:

$$
\sum_{k=r}^{n} (-1)^k \binom{k}{r} = (-1)^n \binom{n-1}{r-1}.
$$

**111.** Binomial inversion: if $b_n = \sum_{k=0}^{n} \binom{n}{k} a_k$, then

$$
a_n = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} b_k.
$$

**112.** The number of $r$-element subsets of an $n$-set is $\binom{n}{r}$.

**113.** The number of ordered $r$-tuples of distinct elements from an $n$-set is $n!/(n-r)!$.

**114.** The number of $r$-element multisets drawn from $n$ types is $\binom{n+r-1}{r}$.

**115.** The number of nonnegative solutions of $x_1 + \cdots + x_n = r$ is $\binom{n+r-1}{r}$.

**116.** The number of positive solutions of $x_1 + \cdots + x_n = r$ is $\binom{r-1}{n-1}$.

**117.** $\binom{-n}{r} = (-1)^r \binom{n+r-1}{r}$

**118.** The generalized binomial series is

$$
(1+x)^\alpha = \sum_{r \ge 0} \binom{\alpha}{r} x^r.
$$

**119.** For integer $n$, $\binom{n}{0} = \binom{n}{n} = 1$.

**120.** The largest binomial coefficient in row $n$ occurs at $r = \lfloor n/2 \rfloor$ or $r = \lceil n/2 \rceil$.

**121.** The adjacent ratio is

$$
\frac{\binom{n}{r+1}}{\binom{n}{r}} = \frac{n-r}{r+1}.
$$

**122.** Therefore, binomial coefficients increase up to the middle of Pascal's triangle and then decrease symmetrically.

**123.** $\sum_{r=0}^{n} r(r-1) \binom{n}{r} = n(n-1) 2^{n-2}$

**124.** $\sum_{r=0}^{n} r^2 \binom{n}{r} = n(n+1) 2^{n-2}$

**125.** $\sum_{r=0}^{n} (-1)^r r \binom{n}{r} = 0$ for $n \ge 2$

**126.** $\sum_{r=0}^{n} (-1)^r r^n \binom{n}{r} = (-1)^n n!$

**127.** More generally, $\sum_{r=0}^{n} (-1)^{n-r} \binom{n}{r} r^m = 0$ for $m < n$.

**128.** For $m = n$, that same finite-difference sum equals $n!$.

**129.** $\binom{2n}{n}$ is always even for $n \ge 1$.

**130.** $\binom{2n}{n} \sim \frac{4^n}{\sqrt{\pi n}}$

---

## 7. Stirling, Partitions, and Permutations

**131.** The Stirling number of the second kind satisfies

$$
S(n,k) = \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} j^n.
$$

**132.** $S(n,k)$ counts partitions of an $n$-element set into exactly $k$ nonempty unlabeled blocks.

**133.** $S(n,k)$ obeys $S(n,k) = k S(n-1,k) + S(n-1,k-1)$.

**134.** The number of surjections from an $n$-set onto a $k$-set is $k! S(n,k)$.

**135.** The number of injective maps from an $r$-set to an $n$-set is $n!/(n-r)!$.

**136.** The number of all functions from an $n$-set to a $k$-set is $k^n$.

**137.** Inclusion–exclusion gives surjections as

$$
\sum_{j=0}^{k} (-1)^j \binom{k}{j} (k-j)^n.
$$

**138.** The unsigned Stirling number $\genfrac{[}{]}{0pt}{}{n}{k}$ counts permutations of $n$ objects with exactly $k$ cycles.

**139.** These satisfy

$$
\genfrac{[}{]}{0pt}{}{n}{k} = \genfrac{[}{]}{0pt}{}{n-1}{k-1} + (n-1)\genfrac{[}{]}{0pt}{}{n-1}{k}.
$$

**140.** $\sum_{k=0}^{n} \genfrac{[}{]}{0pt}{}{n}{k} = n!$

**141.** The signed Stirling numbers expand falling factorials:

$$
x^{\underline{n}} = \sum_{k=0}^{n} s(n,k) x^k.
$$

**142.** The second-kind Stirling numbers invert that relation:

$$
x^n = \sum_{k=0}^{n} S(n,k) x^{\underline{k}}.
$$

**143.** The two Stirling-number matrices are inverses:

$$
\sum_{k} s(n,k) S(k,m) = \delta_{nm}.
$$

**144.** Bell numbers satisfy $B_n = \sum_{k=0}^{n} S(n,k)$.

**145.** $B_n$ counts all set partitions of an $n$-element set.

**146.** Dobinski's formula:

$$
B_n = \frac{1}{e} \sum_{k=0}^{\infty} \frac{k^n}{k!}.
$$

**147.** The exponential generating function for Bell numbers is $\exp(e^x - 1)$.

**148.** The number of involutions satisfies $I_n = I_{n-1} + (n-1) I_{n-2}$.

**149.** An involution is a permutation equal to its own inverse.

**150.** The number of even permutations of $n$ objects is $n!/2$, for $n \ge 2$.

**151.** The number of odd permutations is also $n!/2$, for $n \ge 2$.

**152.** The signed sum of all permutations is zero for $n \ge 2$.

**153.** The determinant expansion of an $n \times n$ matrix has $n!$ permutation terms.

**154.** The permanent expansion also has $n!$ terms, but without permutation signs.

**155.** The number of ways to arrange a multiset with multiplicities $a_1, \dots, a_t$ is

$$
\frac{(a_1 + \cdots + a_t)!}{a_1! \cdots a_t!}.
$$

---

## 8. Probability and Analysis

**156.** A uniformly random permutation of $n$ elements has probability $1/n!$ of being any particular permutation.

**157.** The probability that a random permutation is a derangement is $!n / n!$.

**158.** This derangement probability tends to $1/e$.

**159.** The expected number of fixed points in a random permutation is $1$.

**160.** The expected number of cycles in a random permutation is

$$
H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}.
$$

**161.** The probability that a particular $r$-subset appears in a uniformly random ordering in a prescribed relative order is $1/r!$.

**162.** A Poisson random variable satisfies

$$
\Pr(X = k) = e^{-\lambda} \frac{\lambda^k}{k!}.
$$

**163.** The Poisson probabilities sum to $1$ because of the exponential series.

**164.** Taylor's formula uses factorial normalization:

$$
f(x) = \sum_{n \ge 0} \frac{f^{(n)}(a)}{n!} (x-a)^n.
$$

**165.** $\frac{d^n}{dx^n} x^m = \frac{m!}{(m-n)!} x^{m-n}$ for $m \ge n$.

**166.** $\frac{d^n}{dx^n} x^n = n!$

**167.** The sine series:

$$
\sin x = \sum_{n \ge 0} (-1)^n \frac{x^{2n+1}}{(2n+1)!}.
$$

**168.** The cosine series:

$$
\cos x = \sum_{n \ge 0} (-1)^n \frac{x^{2n}}{(2n)!}.
$$

**169.** The hyperbolic sine series:

$$
\sinh x = \sum_{n \ge 0} \frac{x^{2n+1}}{(2n+1)!}.
$$

**170.** The hyperbolic cosine series:

$$
\cosh x = \sum_{n \ge 0} \frac{x^{2n}}{(2n)!}.
$$

**171.** Gamma recurrence: $\Gamma(z+1) = z \Gamma(z)$.

**172.** Gamma reflection formula:

$$
\Gamma(z) \Gamma(1-z) = \frac{\pi}{\sin(\pi z)}.
$$

**173.** Gamma duplication formula:

$$
\Gamma(z) \Gamma\!\left(z + \tfrac{1}{2}\right) = 2^{1-2z} \sqrt{\pi}\, \Gamma(2z).
$$

**174.** The beta function is

$$
B(x,y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}.
$$

**175.** For integers $m, n \ge 0$,

$$
B(m+1, n+1) = \frac{m! n!}{(m+n+1)!}.
$$

---

## 9. Number Theory and Advanced Patterns

**176.** The Wilson quotient for prime $p$ is

$$
W_p = \frac{(p-1)! + 1}{p},
$$

which is always an integer.

**177.** A Wilson prime is a prime $p$ satisfying $(p-1)! \equiv -1 \pmod{p^2}$.

**178.** The $p$-adic valuation of a binomial coefficient:

$$
v_p\!\left(\binom{n}{r}\right) = v_p(n!) - v_p(r!) - v_p((n-r)!).
$$

**179. Kummer's theorem:** this valuation equals the number of carries when adding $r$ and $n-r$ in base $p$.

**180.** $\binom{n}{r}$ is odd exactly when every binary $1$-bit of $r$ is also a $1$-bit of $n$.

**181.** The number of odd entries in row $n$ of Pascal's triangle is $2^{s_2(n)}$, where $s_2(n)$ is the binary digit sum of $n$.

**182.** $\gcd(n!, n!+1) = 1$

**183.** $\gcd(n!, n!-1) = 1$

**184.** $\gcd(n!, (n+1)!) = n!$

**185.** $\operatorname{lcm}(n!, (n+1)!) = (n+1)!$

**186.** The divisor count of $n!$ is

$$
\tau(n!) = \prod_{p \le n} \bigl(v_p(n!) + 1\bigr).
$$

**187.** The divisor-sum function of $n!$ is

$$
\sigma(n!) = \prod_{p \le n} \frac{p^{v_p(n!) + 1} - 1}{p - 1}.
$$

**188.** Euler's totient of $n!$ is

$$
\varphi(n!) = n! \prod_{p \le n} \left(1 - \frac{1}{p}\right).
$$

**189.** The least common multiple $\operatorname{lcm}(1, \dots, n)$ consists of the largest prime powers $p^a \le n$.

**190.** Its logarithm is the Chebyshev function:

$$
\log \operatorname{lcm}(1, \dots, n) = \sum_{p^a \le n} \log p.
$$

**191.** $\binom{n}{r}$ is integral because every prime valuation in its factorial quotient is nonnegative.

**192.** The factorial sequence is divisible by every fixed positive integer from some point onward.

**193.** For any fixed modulus $m$, $n! \equiv 0 \pmod m$ for all $n \ge m$.

**194.** Consequently, the sequence $n! \bmod m$ eventually becomes permanently zero.

**195.** $\frac{1}{n!}$ decreases faster than any geometric sequence $c^{-n}$ for fixed $c > 0$.

**196.** The series $\sum_{n \ge 0} 1/n!$ converges absolutely.

**197.** The series $\sum_{n \ge 0} n! / x^n$ diverges for every fixed finite nonzero $x$.

**198.** The ordinary generating function $\sum_{n \ge 0} n! x^n$ therefore has radius of convergence $0$.

**199.** The exponential generating function of the factorial sequence is

$$
\sum_{n \ge 0} \frac{n!}{n!} x^n = \frac{1}{1-x}.
$$

**200.** Factorials act as the normalization that turns many combinatorial counting sequences into well-behaved exponential generating functions.

---

## 10. The Three-Lens Pattern Engine

A compact way to navigate these 200 identities is to start from the recurrence $n! = n(n-1)!$ and then inspect it through **three lenses**:

| Lens | What it reveals | Key identities |
|---|---|---|
| **Prime valuations** $v_p(n!)$ | Legendre's formula, trailing zeros, Kummer's theorem | 26–40, 178–181 |
| **Factorial quotients** $\frac{n!}{r!(n-r)!}$ | Binomial coefficients, Stirling numbers, partitions | 41–60, 101–155 |
| **Logarithms / Stirling** | Asymptotic growth, digit count, analytic continuation | 76–100, 164–175 |

These three lenses — prime structure, combinatorial structure, and asymptotic structure — capture essentially everything there is to know about the factorial. The identities above are all manifestations of one or more of these perspectives interacting.

The factorial is deceptively simple in definition ($n! = 1 \cdot 2 \cdots n$) but its reach extends to the heart of number theory (Wilson's theorem, Kummer's theorem), combinatorics (binomial identities, Stirling and Bell numbers, partitions), analysis (Taylor series, gamma function, beta integrals), and probability (Poisson, derangements, random permutations). The 200 identities above are not a random collection — they are the inevitable consequences of a single, unified structure.

---

**Final challenge:** Let $n = 2^{10} = 1024$. 

1. Compute $v_2(n!)$ using Legendre's formula. Then compute it using the binary digit sum formula $v_2(n!) = n - s_2(n)$ and verify they agree.
2. Use Kummer's theorem to determine whether $\binom{2n}{n} = \binom{2048}{1024}$ is even or odd.
3. Find the number of trailing zeros of $n!$ in base $10$.
4. Using Stirling's approximation, estimate $\log_{10}(n!)$ and compare with the exact value from identity 84.

All four answers follow directly from identities in this post.

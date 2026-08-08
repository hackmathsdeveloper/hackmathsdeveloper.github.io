
Factorials generate patterns in divisibility, combinatorics, asymptotics, prime structure, and special functions. Below, \(n,m,k\) are non-negative integers unless stated otherwise; \(p\) is prime. The definition, recurrence, permutation interpretation, prime valuations, and asymptotic behavior are standard factorial properties. [mathworld.wolfram](https://mathworld.wolfram.com/Factorial.html)

## Basic and divisibility patterns

1. \(0!=1\)
2. \(1!=1\)
3. \(n!=1\cdot2\cdot3\cdots n\)
4. \(n!=n(n-1)!\) for \(n\ge1\)
5. \(\frac{n!}{(n-1)!}=n\)
6. Factorials begin \(1,1,2,6,24,120,720,\ldots\)
7. \(n!\) is strictly increasing for \(n\ge1\)
8. \(n!\mid m!\) whenever \(n\le m\)
9. \(\gcd(m!,n!)=\min(m,n)!\)
10. Every integer \(k\) with \(1\le k\le n\) divides \(n!\)
11. Every prime \(p\le n\) divides \(n!\)
12. No prime \(p>n\) divides \(n!\)
13. \(n!\) is even for every \(n\ge2\)
14. \(n!\) is divisible by \(6\) for every \(n\ge3\)
15. \(n!\) ends in at least one zero for every \(n\ge5\)
16. \(n!\equiv0\pmod n\) for \(n\ge1\)
17. \(n!\equiv0\pmod m\) whenever \(n\ge m\)
18. \(n!+1\) is coprime to every \(k\in\{2,\ldots,n\}\)
19. \(n!-1\) is coprime to every \(k\in\{2,\ldots,n\}\)
20. \(n!+k\equiv0\pmod k\) for each \(1\le k\le n\)
21. \(\operatorname{lcm}(1,2,\ldots,n)\mid n!\)
22. If \(n>4\) is composite, then \(n\mid(n-1)!\)
23. For prime \(p\), \((p-1)!\equiv-1\pmod p\) — Wilson’s theorem
24. Conversely, if \((n-1)!\equiv-1\pmod n\), then \(n\) is prime
25. For prime \(p\), \(p!\equiv0\pmod p\)

## Prime factors and decimal patterns

26. The exponent of prime \(p\) in \(n!\) is
   \[
   v_p(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{p^j}\right\rfloor.
   \]
27. Equivalently,
   \[
   v_p(n!)=\frac{n-s_p(n)}{p-1},
   \]
   where \(s_p(n)\) is the sum of the base-\(p\) digits of \(n\).
28. The exponent of \(p\) increases by one or more exactly when \(n\) is divisible by \(p\).
29. More precisely, \(v_p(n!)-v_p((n-1)!)=v_p(n)\).
30. The number of trailing decimal zeros is
   \[
   v_{10}(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{5^j}\right\rfloor.
   \]
31. There are more factors of \(2\) than factors of \(5\) in \(n!\) for \(n\ge1\).
32. Therefore, trailing zeros of \(n!\) are controlled solely by the number of factors of \(5\).
33. The trailing-zero count jumps at multiples of \(5\).
34. It jumps by at least two at multiples of \(25\).
35. It jumps by at least three at multiples of \(125\).
36. \(v_2(n!)=n-s_2(n)\), using the binary digit sum.
37. \(n!\) is never prime for \(n\ge2\).
38. \(n!\) is not a perfect square for \(n>1\).
39. In fact, \(n!\) is not a nontrivial perfect power for \(n>1\).
40. The prime factorization of \(n!\) contains exactly the primes no larger than \(n\).

Legendre’s valuation formula gives items 26–36 and explains the zero-count rule. [mathworld.wolfram](https://mathworld.wolfram.com/Factorial.html)

## Combinatorial patterns

41. \(n!\) counts permutations of \(n\) distinct objects.
42. \(\frac{n!}{(n-r)!}\) counts ordered selections of \(r\) objects from \(n\).
43. \(\binom nr=\frac{n!}{r!(n-r)!}\) counts unordered selections of \(r\) objects.
44. Every binomial coefficient is an integer because \(r!(n-r)!\mid n!\).
45. The binomial theorem is
   \[
   (x+y)^n=\sum_{r=0}^{n}\binom nr x^r y^{n-r}.
   \]
46. \(\sum_{r=0}^{n}\binom nr=2^n\)
47. \(\sum_{r=0}^{n}(-1)^r\binom nr=0\) for \(n\ge1\)
48. \(\sum_{r=0}^{n}r\binom nr=n2^{n-1}\)
49. \(\sum_{r=0}^{n}\binom nr^2=\binom{2n}{n}\)
50. Vandermonde’s identity:
   \[
   \sum_r\binom ar\binom b{n-r}=\binom{a+b}{n}.
   \]
51. The multinomial coefficient is
   \[
   \binom{n}{n_1,\ldots,n_t}=\frac{n!}{n_1!\cdots n_t!}.
   \]
52. It counts arrangements of a multiset with multiplicities \(n_1,\ldots,n_t\).
53. The number of cyclic orderings of \(n\) labeled objects is \((n-1)!\).
54. The number of derangements is
   \[
   !n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
   \]
55. The derangement count is the nearest integer to \(n!/e\).
56. The Catalan number is
   \[
   C_n=\frac{(2n)!}{(n+1)!n!}.
   \]
57. \(C_n=\frac{1}{n+1}\binom{2n}{n}\)
58. The central binomial coefficient is \(\binom{2n}{n}=(2n)!/(n!)^2\).
59. The number of ways to partition \(n\) labeled objects into blocks of specified sizes uses factorial quotients.
60. The unsigned Stirling numbers of the first kind satisfy
   \[
   \sum_{k=0}^{n}\left[{n\atop k}\right]=n!.
   \]

## Identities and series

61. \(k\cdot k!=(k+1)!-k!\)
62. Hence,
   \[
   \sum_{k=1}^{n} k\,k!=(n+1)!-1.
   \]
63. For \(n\ge2\),
   \[
   n!<\sum_{k=0}^{n}k!<2n!.
   \]
64. The reciprocal factorial series gives
   \[
   e=\sum_{k=0}^{\infty}\frac1{k!}.
   \]
65. More generally,
   \[
   e^x=\sum_{k=0}^{\infty}\frac{x^k}{k!}.
   \]
66. The exponential generating function of \(n!\) is formally
   \[
   \sum_{n\ge0}\frac{n!}{n!}x^n=\frac1{1-x}.
   \]
67. The Gamma function extends factorials:
   \[
   \Gamma(n+1)=n!.
   \]
68. Integral form:
   \[
   n!=\int_0^\infty x^n e^{-x}\,dx.
   \]
69. The beta integral gives
   \[
   \int_0^1x^m(1-x)^n\,dx=\frac{m!n!}{(m+n+1)!}.
   \]
70. The falling factorial is
   \[
   (x)_{\underline n}=x(x-1)\cdots(x-n+1).
   \]
71. For integer \(x=n\), \((n)_{\underline r}=n!/(n-r)!\).
72. The rising factorial is
   \[
   (x)^{\overline n}=x(x+1)\cdots(x+n-1).
   \]
73. \((x)_{\underline n}=(-1)^n(-x)^{\overline n}\)
74. Falling factorials expand through signed Stirling numbers:
   \[
   (x)_{\underline n}=\sum_{k=0}^{n}s(n,k)x^k.
   \]
75. \(n!\) is the product of the first \(n\) positive integers, while \(n!!\) skips every other integer.

## Growth and generalized factorials

76. \(n!<n^n\) for \(n\ge2\).
77. \(n!/n^n\) decreases toward zero.
78. \(n!\) eventually exceeds \(a^n\) for every fixed constant \(a>0\).
79. Factorial growth is faster than exponential growth but slower than \(n^n\).
80. Stirling’s approximation is
   \[
   n!\sim\sqrt{2\pi n}\left(\frac ne\right)^n.
   \]
81. A refined Stirling approximation multiplies this by approximately \(1+\frac1{12n}\).
82. Taking logarithms gives
   \[
   \log(n!)=\sum_{k=1}^{n}\log k.
   \]
83. Asymptotically,
   \[
   \log(n!)=n\log n-n+O(\log n).
   \]
84. The number of decimal digits of \(n!\) is
   \[
   \left\lfloor\log_{10}(n!)\right\rfloor+1.
   \]
85. The factorial sequence is log-convex:
   \[
   (n!)^2<(n-1)!(n+1)!.
   \]
86. The ratio of adjacent factorials is linear: \(n!/ (n-1)!=n\).
87. The ratio of adjacent reciprocal factorials is \(1/n\).
88. Even double factorials satisfy
   \[
   (2n)!!=2^n n!.
   \]
89. Odd double factorials satisfy
   \[
   (2n-1)!!=\frac{(2n)!}{2^n n!}.
   \]
90. Therefore,
   \[
   (2n)!=(2n)!!(2n-1)!!.
   \]
91. The product of the first \(n\) odd numbers is \((2n-1)!!\).
92. The half-integer Gamma identity is
   \[
   \Gamma\left(n+\tfrac12\right)=\frac{(2n)!}{4^n n!}\sqrt{\pi}.
   \]
93. The \(q\)-factorial is
   \[
   [n]_q!=\prod_{k=1}^{n}\frac{1-q^k}{1-q}.
   \]
94. As \(q\to1\), \([n]_q!\to n!\).
95. The Gaussian binomial coefficient is
   \[
   {n\brack r}_q=\frac{[n]_q!}{[r]_q![n-r]_q!}.
   \]
96. In factorial-base notation, every nonnegative integer has a unique expansion
   \[
   a_1(1!)+a_2(2!)+\cdots+a_t(t!),
   \]
   with \(0\le a_i\le i\).
97. The superfactorial is \(\prod_{k=1}^{n}k!\).
98. The hyperfactorial is \(\prod_{k=1}^{n}k^k\).
99. The central factorial ratio \((2n)!/(n!)^2\) is approximately \(4^n/\sqrt{\pi n}\).
100. The leading digits of factorials follow Benford-type behavior in the long run. [en.wikipedia](https://en.wikipedia.org/wiki/Factorial)

A useful compact “pattern engine” is: start from \(n!=n(n-1)!\), then inspect it through three lenses—prime valuations \(v_p(n!)\), factorial quotients such as \(\frac{n!}{r!(n-r)!}\), and logarithms/Stirling’s formula.

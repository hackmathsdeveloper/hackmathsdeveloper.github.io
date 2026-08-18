
Congruence modulo \(n\) is the foundational equivalence relation on \(\mathbb Z\) that underlies Ramanujan’s congruences; its structure is rich enough to recover most of elementary number theory, finite ring/field theory, and a lot of the machinery behind modular forms. [tjyusun](https://tjyusun.com/mat202/sec-congruence)

Below is a structured “tour” of the key properties and themes, starting from the bare definition and going all the way up to the kind of phenomena Ramanujan exploited.

***

## Basic definition and equivalence relation

For a positive integer \(n\), we say \(a \equiv b \pmod n\) if \(n \mid (a-b)\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)
Equivalently, \(a\) and \(b\) have the same remainder when divided by \(n\). [codecademy](https://www.codecademy.com/resources/docs/discrete-math/congruences)

This relation is:

- Reflexive: \(a \equiv a \pmod n\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)
- Symmetric: \(a \equiv b \pmod n \Rightarrow b \equiv a \pmod n\). [reddit](https://www.reddit.com/r/explainlikeimfive/comments/hufwo4/eli5_how_does_a_congruence_modulo_work/)
- Transitive: \(a \equiv b\) and \(b \equiv c \Rightarrow a \equiv c \pmod n\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

Thus “\(\equiv \pmod n\)” is an equivalence relation on \(\mathbb Z\), partitioning the integers into residue classes mod \(n\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

***

## Arithmetic of congruences

Congruences behave well with respect to the usual ring operations, which is why modular arithmetic feels like “integer arithmetic with wraparound.” [tjyusun](https://tjyusun.com/mat202/sec-congruence)

If \(a \equiv b \pmod n\) and \(c \equiv d \pmod n\), then:

- Addition and subtraction: \(a + c \equiv b + d \pmod n\), \(a - c \equiv b - d \pmod n\). [tjyusun](https://tjyusun.com/mat202/sec-congruence)
- Multiplication: \(ac \equiv bd \pmod n\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)
- Powers and polynomials: \(a^k \equiv b^k \pmod n\) for any integer \(k \ge 1\), and more generally \(P(a) \equiv P(b) \pmod n\) for any integer-coefficient polynomial \(P\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

These properties can be summarized as: the natural projection \(\mathbb Z \to \mathbb Z/n\mathbb Z\) is a ring homomorphism, and congruence “respects” any algebraic expression built from \(+,-,\times\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

***

## Residue classes and canonical representatives

Each equivalence class modulo \(n\) is a residue class \([a]_n = \{a + kn : k \in \mathbb Z\}\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)
Every integer is congruent to a unique remainder \(r \in \{0,1,\dots,n-1\}\), which gives canonical representatives of the classes. [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

Addition and multiplication of residue classes are defined by \([a]_n + [b]_n := [a+b]_n\) and \([a]_n[b]_n := [ab]_n\), making \(\mathbb Z/n\mathbb Z\) a finite ring with \(n\) elements. [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

This point of view is the right abstraction behind “clock arithmetic” and is the entry point to seeing congruences as ring-theoretic rather than just “remainders.” [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

***

## Divisibility, gcd, and cancellation

The relationship with divisibility is encoded directly in the definition: \(a \equiv 0 \pmod n\) iff \(n \mid a\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)
If \(a \equiv b \pmod n\), then \(\gcd(a,n) = \gcd(b,n)\); gcd is constant on residue classes. [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

Cancellation in congruences is subtle:

- If \(ca \equiv cb \pmod n\) and \(\gcd(c,n)=1\), then \(a \equiv b \pmod n\) (you can cancel \(c\)). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)
- If \(\gcd(c,n) \ne 1\), cancellation may fail; instead one typically reduces the modulus by the gcd. A standard statement: if \(ca \equiv cb \pmod n\) and \(d = \gcd(c,n)\), then \(a \equiv b \pmod{n/d}\) under appropriate divisibility conditions. [youtube](https://www.youtube.com/watch?v=B1gD6540uWA)

This is exactly the phenomenon behind “do not divide congruences blindly” and leads to the concept of units modulo \(n\). [youtube](https://www.youtube.com/watch?v=B1gD6540uWA)

***

## Chinese Remainder Theorem and combining moduli

If \(n\) and \(m\) are coprime and \(a \equiv b \pmod n\) and \(a \equiv b \pmod m\), then \(a \equiv b \pmod{nm}\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)
Conversely, if \(n \mid m\) and \(a \equiv b \pmod m\) then \(a \equiv b \pmod n\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

The full Chinese Remainder Theorem (CRT) says: for pairwise coprime \(n_1,\dots,n_k\), the map \(\mathbb Z/N\mathbb Z \to \prod_i \mathbb Z/n_i\mathbb Z\) with \(N = \prod_i n_i\) is a ring isomorphism. [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)
In practice, it lets you convert a single congruence modulo \(N\) into a system mod prime powers, and vice versa—this is absolutely central in many deeper congruence phenomena (including Ramanujan-type statements modulo \(5^k,7^k,11^k,\dots\)). [pnas](https://www.pnas.org/doi/10.1073/pnas.191488598)

***

## Units, inverses, and solving linear congruences

In \(\mathbb Z/n\mathbb Z\), a residue class \([a]_n\) is invertible (a unit) iff \(\gcd(a,n)=1\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)
The set of units forms a multiplicative group \((\mathbb Z/n\mathbb Z)^\times\), whose order is Euler’s totient \(\varphi(n)\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

Solving a linear congruence \(ax \equiv b \pmod n\) reduces to gcd conditions:

- A solution exists iff \(\gcd(a,n)\) divides \(b\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)
- When it exists, there are exactly \(\gcd(a,n)\) solutions modulo \(n\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

Conceptually, this is just the Euclidean algorithm carried out in the quotient ring \(\mathbb Z/n\mathbb Z\). [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

***

## Classical theorems: Fermat, Euler, and exponent cycles

Several central number-theoretic theorems are naturally congruence statements:

- Fermat’s little theorem: if \(p\) is prime and \(p \nmid a\), then \(a^{p-1} \equiv 1 \pmod p\). [codecademy](https://www.codecademy.com/resources/docs/discrete-math/congruences)
- Euler’s theorem: if \(\gcd(a,n)=1\), then \(a^{\varphi(n)} \equiv 1 \pmod n\). [codecademy](https://www.codecademy.com/resources/docs/discrete-math/congruences)

These yield cyclic behavior of powers modulo \(n\) and underlie “last digit” problems, discrete logs, and many Olympiad-style computations with huge exponents. [youtube](https://www.youtube.com/watch?v=B1gD6540uWA)

***

## Quadratic and higher-power congruences

Beyond linear congruences, one studies quadratic congruences like \(x^2 \equiv a \pmod n\), leading to quadratic residues and nonresidues. [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)
When \(n\) is prime, these are governed by the Legendre symbol and quadratic reciprocity; for composite \(n\), CRT decomposes the problem into prime powers. [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

Higher-power congruences \(x^k \equiv a \pmod n\) connect to the structure of \((\mathbb Z/n\mathbb Z)^\times\), primitive roots when they exist, and more generally to group-theoretic questions about exponent and order. [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

***

## Congruences and generating functions

Ramanujan’s congruences for the partition function \(p(n)\) are archetypal examples of congruences in arithmetic combinatorics. [en.wikipedia](https://en.wikipedia.org/wiki/Ramanujan's_congruences)

The basic statements are, for all \(n \ge 0\): [people.mpim-bonn.mpg](https://people.mpim-bonn.mpg.de/zagier/files/preprints/RamanujanCongruences.pdf)

- \(p(5n+4) \equiv 0 \pmod 5\).  
- \(p(7n+5) \equiv 0 \pmod 7\).  
- \(p(11n+6) \equiv 0 \pmod{11}\).

Modern work shows these come from deep congruence properties of modular forms and their \(q\)-expansions, where coefficients of certain power series satisfy infinite families of congruences modulo powers of primes. [emergentmind](https://www.emergentmind.com/topics/ramanujan-s-congruences)

***

## Modular forms and congruence subgroups

From a higher vantage point, congruence conditions on coefficients of modular forms are tied to the arithmetic of congruence subgroups of \(\mathrm{SL}_2(\mathbb Z)\). [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)

Key themes include:

- Congruence subgroups \(\Gamma_0(N)\), \(\Gamma_1(N)\), etc., where modular forms have Fourier expansions whose coefficients often obey congruence relations mod primes or prime powers. [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)
- Hecke operators acting on spaces of modular forms; congruences between eigenforms correspond to congruence properties of eigenvalues and coefficients. [emergentmind](https://www.emergentmind.com/topics/ramanujan-s-congruences)

Ramanujan’s congruences for \(p(n)\) are explained via the modularity of the generating function \(\sum_{n\ge0} p(n) q^n\) and congruences between that modular form and others of related level/weight. [pnas](https://www.pnas.org/doi/10.1073/pnas.191488598)

***

## Lifting, prime powers, and Ramanujan-type congruences

Many congruence identities first discovered modulo a prime extend to prime powers; this is part of the “Ramanujan-type” story. [research.chalmers](https://research.chalmers.se/publication/532051/file/532051_Fulltext.pdf)

Examples (roughly stated):

- Congruences \(p(n) \equiv 0 \pmod{\ell^k}\) for infinite families of \(n\) in arithmetic progressions, for primes \(\ell \ge 5\). [pnas](https://www.pnas.org/doi/10.1073/pnas.191488598)
- Relations among different Ramanujan-type congruences, where congruences mod different primes interact via CRT and modular-form congruences. [research.chalmers](https://research.chalmers.se/publication/532051/file/532051_Fulltext.pdf)

Conceptually, this is about lifting congruences from \(\mathbb F_\ell\) to \(\mathbb Z_\ell\), using \(p\)-adic modular forms and deformation theory. [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)

***

## Congruences as ring homomorphisms and factor rings

Abstractly, working modulo \(n\) is passing from the ring \(\mathbb Z\) to its quotient ring \(\mathbb Z/n\mathbb Z\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)

Important ring-theoretic properties:

- The kernel of the natural map \(\mathbb Z \to \mathbb Z/n\mathbb Z\) is precisely \(n\mathbb Z\), so \(a \equiv b \pmod n\) iff \(a-b \in n\mathbb Z\). [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.01.html)
- Many statements “mod \(n\)” are just statements about images under a ring homomorphism; this viewpoint generalizes to congruences modulo ideals in arbitrary rings. [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

This is essential for transporting the notion of congruence into other algebraic contexts (e.g. working mod ideals in \(\mathbb Z[x]\) or number fields), which is exactly how one generalizes modular congruences to, say, congruences of Galois representations. [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)

***

## Algorithmic and computational aspects

From a computational perspective, congruences underpin:

- Fast exponentiation modulo \(n\) for cryptographic primitives (RSA, Diffie–Hellman, etc.) via repeated squaring and modular reduction. [codecademy](https://www.codecademy.com/resources/docs/discrete-math/congruences)
- Efficient solving of systems of congruences via CRT decompositions, which allows working modulo many small primes in parallel, then recombining. [sites.math.washington](https://sites.math.washington.edu/~greenber/Congruences.pdf)

Congruence-based arguments also drive many primality tests and factorization heuristics, where nontrivial congruence relations provide certificates of compositeness. [codecademy](https://www.codecademy.com/resources/docs/discrete-math/congruences)

***

## How this ties back to Ramanujan’s congruences

Ramanujan’s partition congruences sit at the intersection of: [en.wikipedia](https://en.wikipedia.org/wiki/Ramanujan's_congruences)

- Basic congruence arithmetic (properties of \(\mathbb Z/n\mathbb Z\), CRT).  
- Generating functions and \(q\)-series, viewed modulo primes and prime powers.  
- Modular forms, congruence subgroups, and congruences between modular forms.

In that sense, they are a “tip of the iceberg” illustrating how far simple-looking congruence conditions can go once you combine them with analytic and algebraic structure.

***

If you’d like, I can zoom in next on a specific direction—for example, classify all the group-theoretic properties of \((\mathbb Z/n\mathbb Z)^\times\), or unpack one of Ramanujan’s congruences starting directly from the generating function and showing where the modulus \(5\), \(7\), or \(11\) actually enters.

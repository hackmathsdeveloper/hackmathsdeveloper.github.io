## 1) Core patterns of coprimality

Coprimality means $\gcd(a,b)=1$. But the interesting part is not just *what* it means — it is *how often it appears* and *what structures force it*.[^1][^2]

### Pattern A: Consecutive integers are always coprime

A basic but powerful pattern is:

$$
\gcd(n,n+1)=1.
$$

Why? Any common divisor of $n$ and $n+1$ must also divide their difference $1$, so it can only be $1$.[^3][^4]

Examples:

- $\gcd(14,15)=1$
- $\gcd(99,100)=1$
- $\gcd(2^{20}, 2^{20}+1)=1$

A good question to ask yourself: if two numbers are *almost* consecutive, what extra condition breaks coprimality? For example, $\gcd(12,14)=2$, so being close is not enough — the exact arithmetic relation matters.

### Pattern B: Prime factors decide everything

Two numbers are coprime exactly when their prime factorizations share no prime.[^5][^6]

Examples:

- $21=3\cdot 7$ and $22=2\cdot 11$, so $\gcd(21,22)=1$.
- $18=2\cdot 3^2$ and $35=5\cdot 7$, so $\gcd(18,35)=1$.
- $18$ and $30$ are not coprime because both contain $2$ and $3$.

A useful question: given a number $n$, which numbers are automatically coprime to it?
Answer: any number built only from primes not dividing $n$. If $n=2^3\cdot 3\cdot 5$, then any number whose prime factors are only $7,11,13,\dots$ is coprime to $n$.

### Pattern C: Pairwise coprime vs setwise coprime

This is a very common source of confusion.

- **Setwise coprime**: $\gcd(a_1,\dots,a_k)=1$.
- **Pairwise coprime**: every pair has gcd $1$.[^2][^7][^1]

Example:

$$
(6,10,15)
$$

has

$$
\gcd(6,10,15)=1,
$$

so it is setwise coprime, but:

- $\gcd(6,10)=2$
- $\gcd(6,15)=3$
- $\gcd(10,15)=5$

So it is not pairwise coprime.

A good question: can a collection be setwise coprime but not pairwise coprime? Yes, and this is the standard example.

### Pattern D: Pairwise coprime families can be built recursively

A famous construction is:

$$
a_{n+1}=a_1a_2\cdots a_n+1.
$$

Then $a_{n+1}$ is coprime to each earlier term.

Example:

- Start with $2, 3$
- Next term: $2\cdot 3+1=7$
- Next term: $2\cdot 3\cdot 7+1=43$

So $2,3,7,43,\dots$ are pairwise coprime.

Question to ask: does $a_1a_2\cdots a_n+1$ have to be prime? No. The point is coprimality, not primality.

## 2) Useful techniques to test coprimality

### Technique 1: Euclidean algorithm

The fastest general test is:

$$
\gcd(a,b)=\gcd(b,a\bmod b).
$$

Keep reducing until you get $1$ or a larger divisor.[^4][^8][^5]

Example:

$$
\gcd(1071,462)
$$

Compute:

- $1071=462\cdot 2+147$
- $462=147\cdot 3+21$
- $147=21\cdot 7+0$

So $\gcd(1071,462)=21$, not coprime.

Now compare:

$$
\gcd(1071,463)
$$

This is not obvious by inspection, so the Euclidean algorithm is the right tool.

A question you can pose: when is the Euclidean algorithm better than factorization?
Answer: almost always for large numbers, because factorization is much harder.

### Technique 2: Bézout identity

$$
\gcd(a,b)=1 \iff \exists x,y\in\mathbb Z \text{ such that } ax+by=1.
$$

[^9][^2]

Example:

$$
8\cdot (-1)+15\cdot 1=7
$$

not enough, but:

$$
8\cdot 2 + 15\cdot (-1)=1.
$$

So $8$ and $15$ are coprime.

This is a very powerful question-generator:

- Can I write $1$ as a linear combination of the two numbers?
- If yes, they are coprime.
- If not, they are not.

This is the same idea behind modular inverses.

### Technique 3: Modular inverse viewpoint

If $\gcd(a,n)=1$, then $a$ has an inverse modulo $n$.[^9]

Example:

- $3^{-1}\pmod 7 = 5$, because $3\cdot 5=15\equiv 1\pmod 7$
- $10^{-1}\pmod{17}=12$, because $10\cdot 12=120\equiv 1\pmod{17}$

Question: why is this useful?
Because coprimality becomes an algebraic condition that lets you solve congruences.

### Technique 4: Prime-support reasoning

Instead of factoring completely, sometimes you only need to know the **shared prime support**.

Example:

- $84=2^2\cdot 3\cdot 7$
- Any number of the form $5^a11^b13^c$ is coprime to $84$

So:

- $55=5\cdot 11$ is coprime to $84$
- $105=3\cdot 5\cdot 7$ is not coprime to $84$

Question to ask: what primes are forbidden if I want a number coprime to $n$?
Answer: exactly the primes dividing $n$.

## 3) Patterns that appear in proof and construction

### Pattern E: Multiplicative structure

If $\gcd(a,b)=1$, then many arithmetic functions behave nicely. For example:

$$
\varphi(ab)=\varphi(a)\varphi(b)
$$

when $a$ and $b$ are coprime. This is one reason coprimality is central in number theory.

Example:

- $\varphi(12)=4$
- $\varphi(5)=4$
- Since $\gcd(12,5)=1$, $\varphi(60)=\varphi(12)\varphi(5)=16$

Question: why does multiplicativity fail without coprimality?
Because shared primes create overlap in divisibility counts.

### Pattern F: Coprime pairs as lattice visibility

A geometric interpretation: $(a,b)$ is “visible” from the origin if and only if $\gcd(a,b)=1$.[^9]

Examples:

- $(3,2)$ is visible
- $(6,4)$ is not, because $\gcd(6,4)=2$

This gives a very concrete question:

- Which lattice points on a line segment from the origin are hidden behind others?
- Answer: exactly those with gcd greater than $1$.


### Pattern G: Coprime moduli in CRT

If moduli are pairwise coprime, the Chinese remainder theorem gives a unique combined solution modulo the product.[^10]

Example:

$$
x\equiv 2 \pmod 3,\quad x\equiv 3 \pmod 5,\quad x\equiv 2 \pmod 7
$$

Since $3,5,7$ are pairwise coprime, there is a unique solution mod $105$.

Question: what breaks if moduli are not coprime?
Then congruences may be inconsistent or may not yield a unique solution modulo the product.

## 4) Example-driven questions to deepen understanding

Here are some “math-question-posing” prompts you can use.

### Easy checks

- Is $(14,25)$ coprime?
- Is $(18,35)$ coprime?
- Is $(21,28)$ coprime?

Answers:

- Yes, $\gcd(14,25)=1$
- Yes, $\gcd(18,35)=1$
- No, $\gcd(21,28)=7$


### Structural questions

- Why are $n$ and $n+1$ always coprime?
- Can a set be setwise coprime but not pairwise coprime?
- Can a number be coprime to many others without being prime?


### Construction questions

- Build three numbers that are pairwise coprime but not all prime.
- Build a sequence where every new term is coprime to all earlier terms.
- Find a number coprime to $2^4\cdot 3^2\cdot 5$.

Example answers:

- $8, 9, 25$ are pairwise coprime.
- $2, 3, 7, 43$ is one recursive coprime sequence.
- Any number using only primes other than $2,3,5$, like $7, 11, 13, 77$, is coprime to $2^4\cdot 3^2\cdot 5$.


### Proof-style questions

- Prove that if $\gcd(a,b)=1$, then $\gcd(a,ab+1)=1$.
- Prove that if $\gcd(a,b)=1$ and $a\mid bc$, then $a\mid c$.
- Prove that if $a$ and $b$ are coprime, then so are $a$ and $b+ka$ for any integer $k$.

These are excellent because they train you to recognize coprimality as a structural property, not just a test.

## 5) A concise way to think about it

Coprimality is best understood as **disjoint prime structure**.

- Euclidean algorithm detects it.
- Bézout explains it.
- Modular inverses use it.
- CRT depends on it.
- Totients and Möbius inversion count with it.
- Recursive constructions generate it.

<div align="center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/Coprime_integers

[^2]: https://www.southampton.ac.uk/~wright/1001/coprime-integers.html

[^3]: https://www.mathsisfun.com/numbers/coprime.html

[^4]: https://tutorax.com/blogue/en/what-are-relatively-prime-numbers/

[^5]: https://www.scienceaq.com/Article/Math/398377.html

[^6]: https://www.mathwords.com/c/coprime.htm

[^7]: https://www.cl.cam.ac.uk/teaching/2324/DiscMath/solutions/DiscMaths3_Sols.pdf

[^8]: https://www.vedantu.com/maths/co-prime-numbers

[^9]: http://library.snls.org.sz/archive/doc/wikipedia/wikipedia-terodump-0.1/tero-dump/wikipedia/co/Coprime.html

[^10]: https://oeis.org/wiki/Chinese_remainder_theorem

[^11]: https://arxiv.org/pdf/1310.4681.pdf

[^12]: https://math.libretexts.org/Courses/Mount_Royal_University/Higher_Arithmetic/4:_Greatest_Common_Divisor_least_common_multiple_and_Euclidean_Algorithm/4.4:_Relatively_Prime_numbers

[^13]: https://www.youtube.com/watch?v=eKVH0iCMoZ4

[^14]: https://www.cip.ifi.lmu.de/~grinberg/t/23wd/lec10.pdf

[^15]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5FC095323A9274D8557BAF9C20E66EF7/S0004972716000083a.pdf/topics-in-divisibility-pairwise-coprimality-the-gcd-of-shifted-sets-and-polynomial-irreducibility.pdf

[^16]: https://math.dartmouth.edu/~carlp/matchingtalk.pdf

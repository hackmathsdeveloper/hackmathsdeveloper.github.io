
Wilson’s theorem is a number-theory result about primes: for an integer \(p>1\), \(p\) is prime **if and only if** \((p-1)! \equiv -1 \pmod p\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

## Meaning

Here, \((p-1)!\) means \(1\cdot 2\cdot 3\cdots (p-1)\), and “\(\equiv -1 \pmod p\)” means that when you divide \((p-1)!\) by \(p\), the remainder is \(p-1\), which is the same as \(-1\) modulo \(p\). [geeksforgeeks](https://www.geeksforgeeks.org/dsa/wilsons-theorem/)

## Example

Take \(p=5\): then \((5-1)! = 4! = 24\), and \(24 \equiv -1 \pmod 5\) because \(24\) leaves remainder \(4\) when divided by \(5\). [britannica](https://www.britannica.com/science/Wilsons-theorem)

For a composite number such as \(p=6\), \((6-1)! = 120\), and \(120 \not\equiv -1 \pmod 6\), so the theorem correctly says 6 is not prime. [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

## Why it works

For a prime \(p\), every nonzero residue modulo \(p\) has a multiplicative inverse, and except for \(1\) and \(-1\), the numbers pair off with distinct inverses; each pair multiplies to \(1\) modulo \(p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)

That leaves only \(1\) and \(-1\), so the whole product \(1\cdot 2\cdots (p-1)\) becomes \(-1\) modulo \(p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)

## Use in practice

Wilson’s theorem gives a correct primality test, but it is usually not efficient for large numbers because computing \((p-1)!\) is expensive compared with modern primality tests. [whitman](https://www.whitman.edu/mathematics/higher_math_online/section03.10.html)

A compact way to remember it is: “A number \(p>1\) is prime exactly when \((p-1)!+1\) is divisible by \(p\).” [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)

Yes. Starting from Wilson’s theorem,
\[
(p-1)! \equiv -1 \pmod p
\]
for prime \(p\), you can derive many standard congruence facts by multiplying both sides by inverses, splitting the factorial product, or pairing residues with their inverses modulo \(p\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

## Direct congruences

Below, \(p\) is an odd prime unless noted otherwise. Each item is a direct consequence of Wilson’s theorem plus basic modular arithmetic on invertible residues modulo a prime. [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)

1. \(p \mid \big((p-1)!+1\big)\). [britannica](https://www.britannica.com/science/Wilsons-theorem)
2. \((p-1)! \equiv p-1 \pmod p\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)
3. \((p-2)! \equiv 1 \pmod p\), since \((p-1)!=(p-1)(p-2)!\equiv - (p-2)! \pmod p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
4. \((p-3)! \equiv -\frac{1}{2} \pmod p\), because \((p-1)!=(p-1)(p-2)(p-3)!\equiv 2(p-3)! \pmod p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
5. \((p-4)! \equiv \frac{1}{6} \pmod p\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)
6. In general, for \(1\le k\le p-1\),
\[
(p-k)! \equiv \frac{(-1)^k}{(k-1)!}\pmod p.
\]
This comes from writing \((p-1)!=(p-1)(p-2)\cdots (p-k+1)(p-k)!\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
7. Special case of the previous formula:
\[
(p-k)!(k-1)! \equiv (-1)^k \pmod p.
\]
 [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
8. \(\big((p-1)/2\big)!^2 \equiv (-1)^{(p+1)/2} \pmod p\), by setting \(k=(p+1)/2\) in item 7. [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)
9. Therefore, if \(p\equiv 1\pmod 4\), then \(\big((p-1)/2\big)!^2 \equiv -1 \pmod p\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
10. If \(p\equiv 3\pmod 4\), then \(\big((p-1)/2\big)!^2 \equiv 1 \pmod p\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

## Symmetric product identities

These come from replacing \(p-j\) by \(-j\) modulo \(p\) and grouping terms symmetrically in the factorial. [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)

11. \[
\prod_{j=1}^{(p-1)/2} j(p-j) \equiv -1 \pmod p.
\]
This is just another way to write \((p-1)!\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
12. Since \(j(p-j)\equiv -j^2\pmod p\),
\[
(-1)^{(p-1)/2}\left(\left(\frac{p-1}{2}\right)!\right)^2 \equiv -1 \pmod p.
\]
 [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
13. Equivalently,
\[
\left(\left(\frac{p-1}{2}\right)!\right)^2 \equiv (-1)^{(p+1)/2}\pmod p.
\]
 [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)
14. \[
\prod_{j=1}^{(p-1)/2}(p-j)\equiv (-1)^{(p-1)/2}\left(\frac{p-1}{2}\right)! \pmod p.
\]
 [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
15. \[
\frac{(p-1)!}{\left(\frac{p-1}{2}\right)!}
\equiv (-1)^{(p-1)/2}\left(\frac{p-1}{2}\right)! \pmod p.
\]
This follows from the previous item by expressing the top half of the factorial. [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)

## Binomial-coefficient consequences

Wilson-type factorial substitutions immediately give congruences for central and near-central binomial coefficients modulo a prime. [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

16. \[
\binom{p-1}{k}\equiv (-1)^k \pmod p
\]
for \(0\le k\le p-1\), since
\[
\binom{p-1}{k}=\frac{(p-1)!}{k!(p-1-k)!}.
\]
 [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
17. In particular, \(\binom{p-1}{1}\equiv -1\pmod p\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
18. \(\binom{p-1}{2}\equiv 1\pmod p\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
19. \(\binom{p-1}{3}\equiv -1\pmod p\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
20. More generally,
\[
k!(p-1-k)! \equiv (-1)^{k+1}\pmod p.
\]
This is item 16 rearranged using \((p-1)!\equiv -1\pmod p\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)
21. Setting \(k=(p-1)/2\),
\[
\binom{p-1}{(p-1)/2}\equiv (-1)^{(p-1)/2}\pmod p.
\]
 [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
22. Hence, if \(p\equiv 1\pmod 4\), then
\[
\binom{p-1}{(p-1)/2}\equiv 1\pmod p.
\]
 [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)
23. If \(p\equiv 3\pmod 4\), then
\[
\binom{p-1}{(p-1)/2}\equiv -1\pmod p.
\]
 [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)

## Inverse-pairing facts

The standard proof of Wilson’s theorem uses the fact that, modulo a prime, every nonzero class has a unique inverse and only \(1\) and \(-1\) are self-inverse. Those same pairings produce further consequences. [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)

24. The product of all nonzero residues modulo \(p\) is \(-1\) modulo \(p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
25. The product of all residues except \(1\) and \(-1\) is \(1\) modulo \(p\), because inverse pairs cancel. [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
26. The only self-inverse nonzero residues modulo a prime \(p\) are \(1\) and \(-1\), since \(a^2\equiv 1\pmod p\) implies \(a\equiv \pm 1\pmod p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
27. Therefore the nonzero residue classes modulo \(p\) can be partitioned into inverse pairs together with the singleton classes \(1\) and \(-1\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)
28. If \(S\) is any subset of nonzero residues closed under inversion and containing neither \(1\) nor \(-1\), then \(\prod_{a\in S} a\equiv 1\pmod p\). [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)

## Primality and composite-number consequences

Wilson’s theorem is an if-and-only-if statement, so it also yields clean characterizations of prime and composite integers. [britannica](https://www.britannica.com/science/Wilsons-theorem)

29. For every integer \(n>1\),
\[
n \text{ is prime } \iff (n-1)! \equiv -1 \pmod n.
\]
 [britannica](https://www.britannica.com/science/Wilsons-theorem)
30. For every composite \(n>4\),
\[
(n-1)! \equiv 0 \pmod n,
\]
because \(n\) has proper factors that both appear inside \((n-1)!\), except for the exceptional composite \(n=4\). [math.libretexts](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Barrus_and_Clark)/01:_Chapters/1.24:_Theorems_of_Wilson_Euler_and_Fermat)

## Example

For \(p=11\), item 3 gives \(9! \equiv 1 \pmod{11}\), and item 8 gives \(5!^2 \equiv 1 \pmod{11}\) because \(11\equiv 3\pmod 4\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)
Indeed, \(5!=120\equiv 10\pmod{11}\), so \(5!^2\equiv 10^2=100\equiv 1\pmod{11}\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)




Here is the short modular-arithmetic proof for Wilson theorem. For a prime \(p\), every nonzero residue modulo \(p\) has a unique multiplicative inverse, because \(\mathbb{Z}/p\mathbb{Z}\) is a field. [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

## Proof

Consider the nonzero residue classes
\[
1,2,3,\dots,p-1
\]
modulo \(p\). Each element \(a\) has an inverse \(a^{-1}\), and if \(a=a^{-1}\), then \(a^2\equiv 1\pmod p\), so \(p\mid (a-1)(a+1)\), which implies \(a\equiv 1\) or \(a\equiv -1\pmod p\) because \(p\) is prime. [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)

So among \(1,2,\dots,p-1\), the only self-inverse elements are \(1\) and \(p-1\), while every other element can be paired with a distinct inverse. [eg.bucknell](https://www.eg.bucknell.edu/~ncr006/teaching/209/f11/handouts/notes9.pdf)

Therefore,
\[
(p-1)! = 1\cdot 2\cdot 3\cdots (p-1)
\]
is congruent modulo \(p\) to
\[
1\cdot (p-1)\cdot \prod (aa^{-1}),
\]
where the remaining factors are taken over the inverse pairs. Each pair contributes \(1\), so
\[
(p-1)! \equiv 1\cdot (p-1)\equiv -1 \pmod p.
\]
 [youtube](https://www.youtube.com/watch?v=uWoKhyKcEH4)

## One-line version

Pair every nonzero residue mod \(p\) with its inverse; all pairs multiply to \(1\), except the two self-inverse residues \(1\) and \(-1\), so the total product is \(-1\). [artofproblemsolving](https://artofproblemsolving.com/wiki/index.php/Wilson's_Theorem)

## Tiny example

For \(p=7\), the inverses are \(1^{-1}=1\), \(6^{-1}=6\), \(2^{-1}=4\), and \(3^{-1}=5\), so
\[
6! \equiv 1\cdot 6\cdot (2\cdot 4)\cdot (3\cdot 5)\equiv 1\cdot (-1)\cdot 1\cdot 1\equiv -1 \pmod 7.
\]
 [eg.bucknell](https://www.eg.bucknell.edu/~ncr006/teaching/209/f11/handouts/notes9.pdf)

Now we will prove the converse:

why \((n-1)!\equiv -1\pmod n\) forces \(n\) to be prime.

Yes. The converse is short too: if \((n-1)! \equiv -1 \pmod n\), then \(n\) must be prime. [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

## Converse proof

Assume, for contradiction, that \(n\) is composite. Then \(n\) has a proper divisor \(a\) with \(1<a<n\). [planetmath](https://planetmath.org/converseofwilsonstheorem)

Because \(a\) is one of the integers \(1,2,\dots,n-1\), it appears as a factor of \((n-1)!\), so \(a\mid (n-1)!\). [mathcenter.oxford.emory](https://mathcenter.oxford.emory.edu/site/math125/wilsonsConverse/)

Now suppose \((n-1)! \equiv -1 \pmod n\). This means \(n \mid \big((n-1)!+1\big)\), and therefore every divisor of \(n\), including \(a\), also divides \((n-1)!+1\). [en.wikipedia](https://en.wikipedia.org/wiki/Wilson%27s_theorem)

So \(a\) divides both \((n-1)!\) and \((n-1)!+1\). Then \(a\) must divide their difference,
\[
\big((n-1)!+1\big)-(n-1)! = 1,
\]
which is impossible since \(a>1\). [mathcenter.oxford.emory](https://mathcenter.oxford.emory.edu/site/math125/wilsonsConverse/)

That contradiction shows \(n\) cannot be composite, so \(n\) is prime. [planetmath](https://planetmath.org/converseofwilsonstheorem)

## Stronger fact

In fact, aside from the exception \(n=4\), every composite \(n\) satisfies
\[
(n-1)! \equiv 0 \pmod n,
\]
not \(-1\). [es.scribd](https://es.scribd.com/document/356683700/Wilson-s-Theorem)

For example, when \(n=6\), we get \(5!=120\), and \(120 \equiv 0 \pmod 6\). [planetmath](https://planetmath.org/converseofwilsonstheorem)

## Combined statement

So Wilson’s theorem is an if-and-only-if criterion:
\[
n>1 \text{ is prime } \iff (n-1)! \equiv -1 \pmod n.
\]
 [britannica](https://www.britannica.com/science/Wilsons-theorem)

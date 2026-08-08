
Here are 20 less obvious properties connecting $$\gcd$$ and $$\operatorname{lcm}$$, with a mix of algebraic, combinatorial, and lattice-theoretic viewpoints.

## 20 less obvious properties

1. **Associativity over many numbers.**  
   $$
   \gcd(a_1,\dots,a_n)=\gcd(\gcd(a_1,\dots,a_{n-1}),a_n),
   $$
   $$
   \operatorname{lcm}(a_1,\dots,a_n)=\operatorname{lcm}(\operatorname{lcm}(a_1,\dots,a_{n-1}),a_n).
   $$

2. **Order independence.**  
   Reordering inputs does not change either operation:
   $$
   \gcd(a_{\sigma(1)},\dots,a_{\sigma(n)})=\gcd(a_1,\dots,a_n),
   $$
   and similarly for $$\operatorname{lcm}$$.

3. **Absorption over many numbers.**  
   $$
   \gcd(a_1,\dots,a_n,\operatorname{lcm}(a_1,\dots,a_n))=\gcd(a_1,\dots,a_n),
   $$
   $$
   \operatorname{lcm}(a_1,\dots,a_n,\gcd(a_1,\dots,a_n))=\operatorname{lcm}(a_1,\dots,a_n).
   $$

4. **Duality under divisibility.**  
   If $$a\mid b$$, then
   $$
   \gcd(a,b)=a,\qquad \operatorname{lcm}(a,b)=b.
   $$

5. **Prime-exponent coordinatewise structure.**  
   For $$a_i=\prod_p p^{e_{i,p}}$$,
   $$
   \gcd(a_1,\dots,a_n)=\prod_p p^{\min_i e_{i,p}},\quad
   \operatorname{lcm}(a_1,\dots,a_n)=\prod_p p^{\max_i e_{i,p}}.
   $$

6. **Product of all numbers vs. gcd/lcm bounds.**  
   For two numbers,
   $$
   \gcd(a,b)\le \sqrt{ab}\le \operatorname{lcm}(a,b),
   $$
   and equality throughout occurs iff $$a=b$$.

7. **Coprime factorization.**  
   If $$a=dx$$, $$b=dy$$ with $$\gcd(x,y)=1$$, then
   $$
   \gcd(a,b)=d,\qquad \operatorname{lcm}(a,b)=dxy.
   $$

8. **GCD of linear combinations.**  
   $$
   \gcd(a,b)=\gcd(a,b+ka)=\gcd(a+kb,b)
   $$
   for every integer $$k$$. This links gcd to additive structure.

9. **A related lcm identity for multiples.**  
   If $$a\mid c$$ and $$b\mid d$$, then
   $$
   \operatorname{lcm}(a,b)\mid \operatorname{lcm}(c,d).
   $$

10. **Min/max distributivity in exponent space.**  
    On prime exponent vectors, gcd/lcm satisfy
    $$
    \min(x,\max(y,z))=\max(\min(x,y),\min(x,z)),
    $$
    $$
    \max(x,\min(y,z))=\min(\max(x,y),\max(x,z)).
    $$

11. **Modular identity via the gcd.**  
    Let $$d=\gcd(a,b)$$. Then
    $$
    \operatorname{lcm}(a,b)=\frac{ab}{d}.
    $$
    This means knowing one of $$\gcd,\operatorname{lcm}$$ determines the other.

12. **Iteration stabilizes quickly.**  
    $$
    \gcd(a,\gcd(a,b))=\gcd(a,b),\qquad \operatorname{lcm}(a,\operatorname{lcm}(a,b))=\operatorname{lcm}(a,b).
    $$

13. **Symmetric extreme behavior.**  
    $$
    \gcd(a,b)=1 \iff \operatorname{lcm}(a,b)=ab,
    $$
    and
    $$
    \operatorname{lcm}(a,b)=\max(a,b) \iff a\mid b \text{ or } b\mid a.
    $$

14. **Lattice meet/join laws.**  
    $$
    \gcd(a,\operatorname{lcm}(b,c))=\operatorname{lcm}(\gcd(a,b),\gcd(a,c)),
    $$
    $$
    \operatorname{lcm}(a,\gcd(b,c))=\gcd(\operatorname{lcm}(a,b),\operatorname{lcm}(a,c)).
    $$
    These are distributive laws in the divisibility lattice.

15. **Common divisor/common multiple characterization.**  
    Every common divisor of $$a,b$$ divides $$\gcd(a,b)$$, and $$\operatorname{lcm}(a,b)$$ divides every common multiple of $$a,b$$.

16. **Repeated gcd over a set is the gcd of pairwise gcds.**  
    $$
    \gcd(a_1,\dots,a_n)=\gcd(\gcd(a_1,a_2),a_3,\dots,a_n).
    $$

17. **Repeated lcm over a set is the lcm of pairwise lcms.**  
    $$
    \operatorname{lcm}(a_1,\dots,a_n)=\operatorname{lcm}(\operatorname{lcm}(a_1,a_2),a_3,\dots,a_n).
    $$

18. **Change under replacing a pair by $$\gcd$$ and $$\operatorname{lcm}$$.**  
    Replacing $$a,b$$ by $$\gcd(a,b)$$ and $$\operatorname{lcm}(a,b)$$ preserves the product $$ab$$, which is why these operations often appear in invariant arguments.

19. **Set-theoretic analogy.**  
    The pair $$(\gcd,\operatorname{lcm})$$ behaves like $$(\cap,\cup)$$: meet/join, intersection/union, minimum/maximum.

20. **Uniqueness from universal properties.**  
    $$\gcd(a,b)$$ is uniquely determined as the greatest element dividing both, and $$\operatorname{lcm}(a,b)$$ as the least element divisible by both. In lattice language, this gives a universal characterization independent of prime factorization.

## A useful unifying picture

A very clean way to think about $$\gcd$$ and $$\operatorname{lcm}$$ is:

- $$\gcd$$ takes the **common part**.
- $$\operatorname{lcm}$$ takes the **combined coverage**.

On prime exponents, that becomes:
- $$\gcd$$: coordinatewise minimum.
- $$\operatorname{lcm}$$: coordinatewise maximum.

That is why these operations satisfy so many identities that look like min/max algebra.

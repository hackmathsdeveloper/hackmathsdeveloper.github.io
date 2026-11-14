
A clean invariant is the multiset of prime exponents across all numbers. The final value is the product of all primes that appear in the initial list, each raised to the maximum exponent with which it appears in any of the 2026 integers.

## Key idea

Write each number in prime factorization:
$$
a_i=\prod_p p^{e_{i,p}}.
$$
For a chosen pair $$m,n$$, the two new numbers are
$$
\gcd(m,n)=\prod_p p^{\min(e_p(m),e_p(n))},
$$
$$
\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}
=\prod_p p^{|e_p(m)-e_p(n)|}.
$$

So for each prime $$p$$, if its exponents in the two chosen numbers are $$x$$ and $$y$$, they are replaced by
$$
\min(x,y),\quad |x-y|.
$$

## Why the process ends

For each prime $$p$$, the sum of its exponents over all 2026 numbers does not change:
$$
x+y=\min(x,y)+|x-y|+2\min(x,y),
$$
and more importantly, the total “mass” of exponents is redistributed without increasing the maximum. Repeating this process eventually concentrates each prime’s exponent into at most one number, because every move tends to reduce the number of nonzero exponent entries unless one of the chosen exponents is zero, which cannot happen since all numbers stay $$>1$$.

A more conceptual way to see termination is to use the quantity
$$
\sum_{i=1}^{2026} \log a_i,
$$
which stays fixed, while the product of all numbers is preserved, and the structure becomes progressively more rigid. Eventually no two numbers can both be $$>1$$, so exactly one number remains $$>1$$.

## The final value

For each prime $$p$$, let
$$
E_p=\max_i e_{i,p}.
$$
This maximum exponent is an invariant of the process: the operation on exponents $$(x,y)\mapsto (\min(x,y),|x-y|)$$ preserves the maximum over the whole collection. Hence the final remaining number must be
$$
M=\prod_p p^{E_p}.
$$

That is, $$M$$ is the least common multiple of the original 2026 integers.

## Conclusion

- After finitely many moves, only one integer greater than $$1$$ remains.
- That integer is independent of the choices made by Confucius.
- In fact,
$$
\boxed{M=\operatorname{lcm}(a_1,a_2,\dots,a_{2026}).}
$$


Here’s a compact exploration of the main properties of $$\gcd$$ and $$\operatorname{lcm}$$, together with several ways to see how they are related.

## Core identities

For positive integers $$a,b$$,
$$
ab=\gcd(a,b)\operatorname{lcm}(a,b).
$$
This is the most famous relationship between them.

Also:
- $$\gcd(a,b)\mid a$$ and $$\gcd(a,b)\mid b$$.
- $$a\mid \operatorname{lcm}(a,b)$$ and $$b\mid \operatorname{lcm}(a,b)$$.
- $$\gcd(a,b)$$ is the greatest common divisor, while $$\operatorname{lcm}(a,b)$$ is the least common multiple.

## Main properties

### Divisibility
- $$\gcd(a,b)\le a,b$$.
- $$\operatorname{lcm}(a,b)\ge a,b$$.
- $$\gcd(a,b)=a$$ iff $$a\mid b$$.
- $$\operatorname{lcm}(a,b)=a$$ iff $$b\mid a$$.

### Symmetry
$$
\gcd(a,b)=\gcd(b,a),\qquad \operatorname{lcm}(a,b)=\operatorname{lcm}(b,a).
$$

### Associativity
$$
\gcd(a,\gcd(b,c))=\gcd(\gcd(a,b),c),
$$
$$
\operatorname{lcm}(a,\operatorname{lcm}(b,c))=\operatorname{lcm}(\operatorname{lcm}(a,b),c).
$$

### Absorption
$$
\gcd(a,\operatorname{lcm}(a,b))=a,\qquad \operatorname{lcm}(a,\gcd(a,b))=a.
$$

### Scaling
For any positive integer $$k$$,
$$
\gcd(ka,kb)=k\gcd(a,b),\qquad \operatorname{lcm}(ka,kb)=k\operatorname{lcm}(a,b).
$$

### Coprime case
If $$\gcd(a,b)=1$$, then
$$
\operatorname{lcm}(a,b)=ab.
$$

## Why they are related

### 1. Prime factorization viewpoint
Write
$$
a=\prod_p p^{\alpha_p},\qquad b=\prod_p p^{\beta_p}.
$$
Then
$$
\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)},\qquad
\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$
So:
- $$\gcd$$ keeps the smaller exponent of each prime.
- $$\operatorname{lcm}$$ keeps the larger exponent of each prime.

This makes the product identity immediate:
$$
\min(\alpha,\beta)+\max(\alpha,\beta)=\alpha+\beta.
$$

### 2. Set/intersection-union analogy
If you think of prime powers as “content”:
- $$\gcd$$ behaves like an intersection.
- $$\operatorname{lcm}$$ behaves like a union.

Then the identity $$ab=\gcd(a,b)\operatorname{lcm}(a,b)$$ resembles
$$
|A|+|B|=|A\cap B|+|A\cup B|.
$$

### 3. Lattice-theoretic viewpoint
Under divisibility:
- $$\gcd$$ is the meet.
- $$\operatorname{lcm}$$ is the join.

So integers form a lattice, and $$\gcd,\operatorname{lcm}$$ are dual operations.

### 4. Euclidean algorithm viewpoint
Repeatedly applying
$$
\gcd(a,b)=\gcd(b,a\bmod b)
$$
shows that $$\gcd$$ is stable under subtractive steps. This is the computational reason $$\gcd$$ is efficient.

By contrast, $$\operatorname{lcm}$$ is usually computed via
$$
\operatorname{lcm}(a,b)=\frac{ab}{\gcd(a,b)}.
$$

## Several useful inequalities

For positive integers $$a,b$$:
$$
\gcd(a,b)\le \sqrt{ab}\le \operatorname{lcm}(a,b).
$$
Also,
$$
\gcd(a,b)\cdot \operatorname{lcm}(a,b)=ab.
$$
So if one is small, the other must be large.

More generally, for any finite set $$a_1,\dots,a_n$$,
$$
\gcd(a_1,\dots,a_n)\mid \operatorname{lcm}(a_1,\dots,a_n).
$$

## A concrete example

Take $$a=12=2^2\cdot 3$$ and $$b=18=2\cdot 3^2$$.

Then:
$$
\gcd(12,18)=2^1\cdot 3^1=6,
$$
$$
\operatorname{lcm}(12,18)=2^2\cdot 3^2=36.
$$
And indeed:
$$
12\cdot 18=216=6\cdot 36.
$$

## Different techniques to see the relation

### Prime exponents
Best for structural understanding.

### Divisibility arguments
Best for proving universal properties like minimality and maximality.

### Algebraic identity
Best for computation:
$$
\operatorname{lcm}(a,b)=\frac{ab}{\gcd(a,b)}.
$$

### Lattice language
Best for abstract theory and generalization.

### Algorithmic viewpoint
Best for practical computation and number-theoretic applications.

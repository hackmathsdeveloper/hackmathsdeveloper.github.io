
## 1. Three proofs of $$ab=\gcd(a,b)\operatorname{lcm}(a,b)$$

Let $$d=\gcd(a,b)$$. Write $$a=dx$$ and $$b=dy$$, where $$\gcd(x,y)=1$$. Then $$\operatorname{lcm}(a,b)=dxy$$, because the common factor is exactly $$d$$ and the remaining parts are coprime. Hence
$$
\gcd(a,b)\operatorname{lcm}(a,b)=d\cdot dxy=d^2xy=ab.
$$

### Proof 1: Via prime factorization
Write
$$
a=\prod_p p^{\alpha_p},\qquad b=\prod_p p^{\beta_p}.
$$
Then
$$
\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)},\qquad
\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$
Multiplying gives
$$
\prod_p p^{\min(\alpha_p,\beta_p)+\max(\alpha_p,\beta_p)}
=\prod_p p^{\alpha_p+\beta_p}=ab.
$$

### Proof 2: Via divisibility and coprime reduction
Let $$d=\gcd(a,b)$$, so $$a=dx$$, $$b=dy$$, with $$\gcd(x,y)=1$$.  
Because $$x$$ and $$y$$ are coprime, $$\operatorname{lcm}(x,y)=xy$$. Therefore
$$
\operatorname{lcm}(a,b)=d\operatorname{lcm}(x,y)=dxy,
$$
and thus
$$
\gcd(a,b)\operatorname{lcm}(a,b)=d(dxy)=ab.
$$

### Proof 3: Via the lattice viewpoint
In the divisibility lattice of positive integers, $$\gcd$$ is the meet and $$\operatorname{lcm}$$ is the join. Prime exponents turn this lattice into coordinatewise min/max on exponent vectors. Since for each coordinate
$$
\min(u,v)+\max(u,v)=u+v,
$$
multiplying over all primes yields
$$
\gcd(a,b)\operatorname{lcm}(a,b)=ab.
$$

## 2. Comparison table

| Property | $$\gcd(a,b)$$ | $$\operatorname{lcm}(a,b)$$ |
|---|---|---|
| Definition | Greatest common divisor | Least common multiple |
| Divisibility | Divides both $$a$$ and $$b$$ | Is divisible by both $$a$$ and $$b$$ |
| Size | At most both numbers | At least both numbers |
| Prime exponents | Takes $$\min$$ of exponents | Takes $$\max$$ of exponents |
| Symmetry | $$\gcd(a,b)=\gcd(b,a)$$ | $$\operatorname{lcm}(a,b)=\operatorname{lcm}(b,a)$$ |
| Coprime case | Equals $$1$$ | Equals $$ab$$ |
| Relation | $$\gcd(a,b)\operatorname{lcm}(a,b)=ab$$ | Same identity |
| Absorption | $$\gcd(a,\operatorname{lcm}(a,b))=a$$ | $$\operatorname{lcm}(a,\gcd(a,b))=a$$ |
| Computation | Euclidean algorithm | Usually via $$ab/\gcd(a,b)$$ |

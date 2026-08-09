
The identity

[
(1+z)^{-n} = {}_2F_1(n,1;1;-z)
]

connects an elementary rational function to the **Gaussian hypergeometric function**.

This is important because hypergeometric functions are the “universal language” behind a huge number of special functions, differential equations, combinatorial sequences, and physics integrals.

The expression can be visualized as:

(1+z)^{-n}={}_2F_1(n,1;1;-z)

---

# 1. What is ({}_2F_1)?

The Gaussian hypergeometric function is defined by the power series

[
{}_2F_1(a,b;c;z)
================

\sum_{k=0}^{\infty}
\frac{(a)_k (b)_k}{(c)_k}
\frac{z^k}{k!}
]

where:

* (a,b,c) are parameters
* ((x)_k) is the **Pochhammer symbol** (rising factorial)

---

# 2. Pochhammer symbol

The rising factorial is:

[
(x)_k
=====

x(x+1)(x+2)\cdots(x+k-1)
]

with:

[
(x)_0 = 1
]

Examples:

[
(3)_4
=====

# 3\cdot4\cdot5\cdot6

360
]

[
(1)_k = k!
]

because:

[
1\cdot2\cdot3\cdots k = k!
]

---

# 3. Substitute the parameters

Now plug into:

[
{}_2F_1(n,1;1;-z)
]

We get:

[
{}_2F_1(n,1;1;-z)
=================

\sum_{k=0}^{\infty}
\frac{(n)_k (1)_k}{(1)_k}
\frac{(-z)^k}{k!}
]

Since:

[
(1)_k = k!
]

the numerator and denominator cancel:

# [

\sum_{k=0}^{\infty}
\frac{(n)_k}{k!}
(-z)^k
]

Now:

[
(n)_k
=====

# n(n+1)\cdots(n+k-1)

\frac{(n+k-1)!}{(n-1)!}
]

Thus:

[
\frac{(n)_k}{k!}
================

\binom{n+k-1}{k}
]

So:

[
{}_2F_1(n,1;1;-z)
=================

\sum_{k=0}^{\infty}
(-1)^k
\binom{n+k-1}{k}
z^k
]

which is exactly:

[
(1+z)^{-n}
]

---

# 4. Why this identity works structurally

The key mechanism is:

[
\frac{(1)_k}{(1)_k}=1
]

This collapses the general hypergeometric series into the negative binomial series.

So this particular hypergeometric function is “degenerate” into a simple elementary function.

---

# 5. Differential equation viewpoint

Hypergeometric functions solve the hypergeometric differential equation:

[
z(1-z)y''
+
[c-(a+b+1)z]y'
-ab,y
=0
]

Substitute:

[
a=n,\quad b=1,\quad c=1
]

Then:

[
z(1-z)y''
+
[1-(n+2)z]y'
-n y
=0
]

The solution:

[
y=(1+z)^{-n}
]

satisfies this ODE.

This is extremely important:

Many elementary functions are actually hidden hypergeometric functions.

---

# 6. Why hypergeometric functions are universal

The hypergeometric series coefficient ratio is:

[
\frac{a_{k+1}}{a_k}
===================

\frac{(a+k)(b+k)}{(c+k)(k+1)}
z
]

This rational ratio property makes hypergeometric functions the natural endpoint of many:

* combinatorial sums
* recurrence relations
* differential equations
* Feynman integrals
* orthogonal polynomials

---

# 7. Connection to binomial theorem

The generalized binomial theorem says:

[
(1-z)^{-a}
==========

\sum_{k=0}^{\infty}
\frac{(a)_k}{k!}z^k
]

But this is exactly:

[
{}_1F_0(a;;z)
]

since:

[
{}_1F_0(a;;z)
=============

\sum_{k=0}^{\infty}
\frac{(a)_k}{k!}z^k
]

Thus:

[
(1-z)^{-a}
==========

{}_1F_0(a;;z)
]

and because:

[
{}_2F_1(a,b;b;z)
================

{}_1F_0(a;;z)
]

you obtain:

[
{}_2F_1(a,b;b;z)
================

(1-z)^{-a}
]

Setting:

[
a=n,\quad z\to -z
]

gives:

[
{}_2F_1(n,1;1;-z)
=================

(1+z)^{-n}
]

---

# 8. Gamma function formulation

Pochhammer symbols are really gamma functions:

[
(a)_k
=====

\frac{\Gamma(a+k)}{\Gamma(a)}
]

Thus:

[
{}_2F_1(a,b;c;z)
================

\sum_{k=0}^{\infty}
\frac{
\Gamma(a+k)\Gamma(b+k)\Gamma(c)
}{
\Gamma(a)\Gamma(b)\Gamma(c+k)
}
\frac{z^k}{k!}
]

This reveals the analytic continuation structure.

Hypergeometric functions are fundamentally built from gamma functions.

---

# 9. Analytic continuation

The power series converges only for:

[
|z|<1
]

But hypergeometric functions can be analytically continued to much larger domains.

That is why expressing elementary functions as hypergeometric functions is powerful:

it allows:

* contour integral representations
* branch cut analysis
* monodromy study
* asymptotics
* Mellin-Barnes transforms

---

# 10. Low-level coefficient mechanics

Observe:

[
a_k
===

\frac{(n)_k}{k!}(-1)^k
]

Then:

[
\frac{a_{k+1}}{a_k}
===================

-\frac{n+k}{k+1}
]

This rational ratio is the signature of a hypergeometric sequence.

A sequence is hypergeometric iff:

[
\frac{a_{k+1}}{a_k}
]

is rational in (k).

---

# 11. Deeper significance

Almost all classical special functions are hypergeometric descendants:

| Function             | Hypergeometric representation |
| -------------------- | ----------------------------- |
| Exponential          | ({}_0F_0)                     |
| Binomial functions   | ({}_1F_0)                     |
| Bessel functions     | ({}_0F_1)                     |
| Legendre polynomials | ({}_2F_1)                     |
| Elliptic integrals   | ({}_2F_1)                     |
| Airy-type structures | confluent hypergeometrics     |

So:

[
(1+z)^{-n}
]

being hypergeometric means it belongs to this enormous algebraic ecosystem.

---

# 12. The key identity behind everything

The crucial identity is:

[
{}_2F_1(a,b;b;z)
================

(1-z)^{-a}
]

Visualization of this hypergeometric reduction:

{}_2F_1(a,b;b;z)=(1-z)^{-a}

Your example is simply:

[
a=n,\quad b=1,\quad z\to -z
]

giving:

[
\boxed{
{}_2F_1(n,1;1;-z)
=================

(1+z)^{-n}
}
]


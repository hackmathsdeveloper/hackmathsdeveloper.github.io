
Here are five representative quintic equations over \(\mathbb Q\), ranging from completely elementary cases to irreducible quintics whose roots cannot be expressed by radicals. The governing Galois-theoretic fact is:

> A polynomial over \(\mathbb Q\) is solvable by radicals exactly when its Galois group over \(\mathbb Q\) is a **solvable group**. In particular, an irreducible quintic with Galois group \(S_5\) or \(A_5\) is not solvable by radicals. [ams](https://www.ams.org/bookstore/pspdf/gsm-165-prev.pdf)

A crucial caveat: “quintics have no formula” is false. The correct statement is that there is **no radical formula for the general quintic**. Many individual quintics are solvable.

## 1. Cyclotomic quintic

\[
x^5-1=0.
\]

### Roots

The five roots are the fifth roots of unity:

\[
1,\quad \zeta_5,\quad \zeta_5^2,\quad \zeta_5^3,\quad \zeta_5^4,
\]

where

\[
\zeta_5=e^{2\pi i/5}
=
\cos\left(\frac{2\pi}{5}\right)
+i\sin\left(\frac{2\pi}{5}\right).
\]

Equivalently,

\[
\zeta_5^k=e^{2\pi i k/5}, \qquad k=0,1,2,3,4.
\]

### Galois-theory analysis

Because

\[
x^5-1=(x-1)\Phi_5(x)
\]

with

\[
\Phi_5(x)=x^4+x^3+x^2+x+1,
\]

the nontrivial splitting field is

\[
\mathbb Q(\zeta_5).
\]

Its Galois group is

\[
\operatorname{Gal}(\mathbb Q(\zeta_5)/\mathbb Q)
\cong
(\mathbb Z/5\mathbb Z)^\times
\cong C_4.
\]

Since \(C_4\) is abelian, hence solvable, the equation is solvable by radicals. In fact, \(\zeta_5\) can be built using square roots because \(5\) is a Fermat prime.

For example,

\[
\cos\left(\frac{2\pi}{5}\right)=\frac{\sqrt5-1}{4}.
\]

Thus

\[
\zeta_5=
\frac{\sqrt5-1}{4}
+i\sqrt{\frac{5+\sqrt5}{8}}.
\]

This is the simplest example showing that a quintic can be solvable.

## 2. A reducible quintic

\[
x^5-5x^3+4x=0.
\]

### Factorization and roots

Factor out \(x\):

\[
x(x^4-5x^2+4)=0.
\]

Now regard the quartic as a quadratic in \(x^2\):

\[
x^4-5x^2+4=(x^2-1)(x^2-4).
\]

Therefore,

\[
x(x^2-1)(x^2-4)=0.
\]

The roots are

\[
\boxed{-2,\,-1,\,0,\,1,\,2}.
\]

### Galois-theory analysis

The polynomial already splits over \(\mathbb Q\), so its splitting field is just

\[
\mathbb Q.
\]

Hence the Galois group is trivial:

\[
\operatorname{Gal}(\mathbb Q/\mathbb Q)=\{1\}.
\]

The trivial group is solvable. This is a quintic by degree, but not a genuinely difficult one: reducibility reduces it to lower-degree factors.

## 3. A quintic with a binomial radical solution

\[
x^5-2=0.
\]

### Roots

Let

\[
\alpha=\sqrt [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf){2}.
\]

Then the roots are

\[
\boxed{
\alpha,\;
\alpha\zeta_5,\;
\alpha\zeta_5^2,\;
\alpha\zeta_5^3,\;
\alpha\zeta_5^4
}.
\]

Numerically, they are approximately

\[
1.148698355,
\]

\[
0.3550\pm1.0925i,
\]

\[
-0.9294\pm0.6752i.
\]

### Galois-theory analysis

The polynomial is irreducible over \(\mathbb Q\) by Eisenstein’s criterion with \(p=2\). Its splitting field is

\[
K=\mathbb Q(\sqrt [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf){2},\zeta_5).
\]

The relevant automorphisms can:

- send \(\sqrt [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf){2}\mapsto \zeta_5^a\sqrt [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf){2}\), giving a cyclic \(C_5\)-type action;
- send \(\zeta_5\mapsto \zeta_5^b\), where \(b\in(\mathbb Z/5\mathbb Z)^\times\cong C_4\).

Thus its Galois group has the form

\[
C_5\rtimes C_4,
\]

the Frobenius group of order \(20\), often denoted \(F_{20}\) or \(\operatorname{AGL}(1,5)\).

Because it has a normal series

\[
\{1\}\triangleleft C_5\triangleleft C_5\rtimes C_4,
\]

whose successive quotients are abelian, it is solvable. Therefore the quintic is solvable by radicals—as is obvious directly from \(\sqrt [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf){2}\), but Galois theory explains why adjoining the other four roots does not introduce an obstruction.

For an irreducible quintic over \(\mathbb Q\), solvability by radicals occurs precisely when its Galois group is a subgroup of the Frobenius group \(F_{20}\); possible transitive solvable groups include \(C_5\), \(D_5\), and \(F_{20}\). [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_24_solvability_in_radicals.pdf)

## 4. An irreducible solvable quintic of Frobenius type

\[
x^5+120x-1344=0.
\]

This is more interesting than \(x^5-2\): it is not visibly built from a single fifth root, but Galois theory still proves that it is solvable by radicals.

### Galois-theory diagnosis

For a Bring–Jerrard quintic

\[
f(x)=x^5+px+q,
\]

there is a classical sextic resolvent. In this case,

\[
p=120,\qquad q=-1344.
\]

The associated resolvent is

\[
R(y)
=
y^6+960y^5+576000y^4+276480000y^3
+82944000000y^2
+\cdots,
\]

and it has the rational root

\[
y=1440.
\]

The existence of a rational root of this resolvent shows that the Galois group is contained in \(F_{20}\), so the original quintic is solvable by radicals. The discriminant is not a square in \(\mathbb Q\), which rules out containment in \(A_5\); the Galois group is therefore the full Frobenius group

\[
\boxed{\operatorname{Gal}(f/\mathbb Q)\cong F_{20}}.
\]

This example is specifically documented with discriminant and resolvent data in the algebra lecture notes. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_24_solvability_in_radicals.pdf)

### What “find the roots” means here

The roots do have radical expressions, but they are substantially more complicated than the roots of \(x^5-2\). A Galois-theoretic algorithm proceeds through a tower of extensions associated with the group structure

\[
F_{20}\cong C_5\rtimes C_4.
\]

Conceptually, the field tower has the form

\[
\mathbb Q
\subseteq
\mathbb Q(\sqrt{\Delta})
\subseteq
\text{quartic/cyclotomic auxiliary extension}
\subseteq
\text{fifth-root extension}
\subseteq
K.
\]

The important conclusion is:

\[
\boxed{\text{All five roots are expressible by radicals.}}
\]

But unlike the binomial case, their explicit formulas are not usually enlightening.

## 5. A nonsolvable quintic

\[
x^5-6x+3=0.
\]

### Step 1: Show irreducibility

Modulo \(2\),

\[
x^5-6x+3\equiv x^5+1
\equiv (x+1)(x^4+x^3+x^2+x+1)
\pmod 2,
\]

which does not alone establish irreducibility. A more appropriate approach is to use modular factorizations at carefully selected primes, together with the fact that the polynomial has no rational root.

A standard Galois-theoretic analysis shows that this polynomial is irreducible over \(\mathbb Q\) and that its Galois group is \(S_5\). This example is commonly used precisely as an explicit nonsolvable quintic. [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf)

### Step 2: Identify the Galois group

The conclusion is

\[
\boxed{
\operatorname{Gal}(x^5-6x+3\,/\,\mathbb Q)\cong S_5.
}
\]

One typical strategy for proving \(S_5\) is:

1. Prove irreducibility, so the Galois group acts transitively on five roots.
2. Reduce modulo primes not dividing the discriminant.
3. Read the factorization degrees modulo those primes as cycle types in the Galois group.
4. Obtain enough cycle types to force the group to be \(S_5\).

For instance, the presence of appropriate factorizations can show that the group contains:

- a \(5\)-cycle, from irreducibility/transitivity;
- a transposition;
- an element of cycle type \((2)(3)\), or a \(4\)-cycle.

Among transitive subgroups of \(S_5\), these conditions force \(S_5\).

### Step 3: Why this blocks radicals

The symmetric group \(S_5\) is not solvable. Its commutator structure reaches the nonabelian simple group \(A_5\):

\[
S_5' = A_5,
\]

and \(A_5\) has no nontrivial proper normal subgroups. Thus no chain of normal subgroups can have all abelian quotients.

Therefore,

\[
\boxed{x^5-6x+3=0\text{ cannot be solved by radicals over }\mathbb Q.}
\]

Its five roots certainly exist and can be approximated numerically, but there is no formula using only rational numbers, arithmetic operations, and finitely many \(n\)-th roots. The cited notes explicitly establish \(S_5\) for this polynomial and hence nonsolvability by radicals. [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf)

## Summary table

| Quintic | Roots / method | Galois group over \(\mathbb Q\) | Solvable by radicals? |
|---|---|---:|---:|
| \(x^5-1=0\) | Fifth roots of unity | \(C_4\) for the nontrivial cyclotomic factor | Yes |
| \(x^5-5x^3+4x=0\) | \(-2,-1,0,1,2\) | Trivial | Yes |
| \(x^5-2=0\) | \(\sqrt [math.toronto](https://www.math.toronto.edu/~herzig/347-18-w24.pdf){2}\zeta_5^k\) | \(C_5\rtimes C_4\cong F_{20}\) | Yes |
| \(x^5+120x-1344=0\) | Resolvent method; radical expressions exist but are lengthy | \(F_{20}\) | Yes |
| \(x^5-6x+3=0\) | Numerical roots possible; no radical formula | \(S_5\) | No |

## Practical Galois-theory workflow

For a quintic \(f(x)\in\mathbb Q[x]\), a useful decision process is:

1. **Factor \(f\) over \(\mathbb Q\).**  
   If it factors, solve its degree-\(\leq4\) pieces using the familiar formulas or structural simplifications.

2. **Check irreducibility.**  
   Rational-root tests, Eisenstein’s criterion, and factorization modulo primes are effective tools.

3. **Compute the discriminant.**  
   If the discriminant is a square in \(\mathbb Q\), then

   \[
   \operatorname{Gal}(f/\mathbb Q)\subseteq A_5.
   \]

   If it is not a square, the Galois group is not contained in \(A_5\).

4. **Factor \(f\) modulo several primes.**  
   For primes not dividing the discriminant, the degrees of irreducible factors reveal cycle types in the Galois group. For example:
   - irreducible mod \(p\) suggests a \(5\)-cycle;
   - factorization \(2+3\) suggests a permutation of cycle type \((2)(3)\);
   - factorization \(1+4\) suggests a \(4\)-cycle;
   - factorization \(1+1+3\) suggests a \(3\)-cycle.

5. **Identify the subgroup of \(S_5\).**  
   If it is \(S_5\) or \(A_5\), radical formulas are impossible. If it is contained in \(F_{20}\), the quintic is solvable by radicals. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/teaching_fa20_5111/5111_lecture_24_solvability_in_radicals.pdf)

The essential outcome is that Galois theory does not merely say “quintics are hard.” It gives a precise classification: the symmetry group of the roots determines whether a radical solution exists.

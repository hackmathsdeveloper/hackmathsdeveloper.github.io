
Elliptic curves are one of the cleanest bridges between “pure” number theory and geometry. Here is a concrete, number-theoretic walkthrough with explicit computations.

***

## 1. What is an elliptic curve (arithmetically)?

Over \(\mathbb{Q}\), an elliptic curve is given (after a change of variables) by an equation

\[
E: y^2 = x^3 + Ax + B
\]

with \(A,B\in \mathbb{Q}\) such that the discriminant \(\Delta = -16(4A^3 + 27B^2)\neq 0\), which means the curve has no cusps or self-intersections. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

Concrete example:

\[
E: y^2 = x^3 - x.
\]

Here \(A=-1,B=0\), and \(4A^3+27B^2 = 4(-1)^3 + 0 = -4\neq 0\), so \(E\) is nonsingular and hence an elliptic curve. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

Elliptic curves are studied over various fields:
- Over \(\mathbb{Q}\): rational points and Diophantine equations.  
- Over \(\mathbb{F}_p\): counting points mod \(p\) and using those counts in number theory and crypto. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

***

## 2. Group law: adding points with explicit formulas

A key fact: the rational points on an elliptic curve form an abelian group with a geometric addition law. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

For \(E: y^2 = x^3 + Ax + B\) over a field \(K\):

- Given two points \(P_1=(x_1,y_1)\), \(P_2=(x_2,y_2)\) with \(P_1\neq P_2\), the line through them has slope
  \[
  m = \frac{y_2 - y_1}{x_2 - x_1}.
  \]
- That line meets the curve in a third point \(Q=(x_3,y_3)\).  
- Reflect \(Q\) across the \(x\)-axis to get \(P_1+P_2 = (x_3,-y_3)\). [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

Algebraically, one gets explicit formulas: [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

- If \(P_1\neq P_2\),
  \[
  m = \frac{y_2 - y_1}{x_2 - x_1},\quad
  x_3 = m^2 - x_1 - x_2,\quad
  y_3 = -m(x_3 - x_1) - y_1.
  \]
- If \(P_1=P_2\) (doubling),
  \[
  m = \frac{3x_1^2 + A}{2y_1},
  \]
  then same \(x_3,y_3\) formulas. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

### Concrete example over \(\mathbb{Q}\)

Take \(E: y^2 = x^3 - x\) and the point \(P=(0,0)\). Check \(P\in E\): \(0^2 = 0^3 - 0\), yes.

Compute \(2P = P+P\):

- Here \(A=-1\), \(x_1=0,y_1=0\).  
- Doubling formula wants \(\frac{3x_1^2 + A}{2y_1} = \frac{-1}{0}\), which is undefined. Geometrically, the tangent at \(P\) is vertical, so the “third intersection point” is the point at infinity; reflecting gives \(2P = \mathcal{O}\) (the identity).

So \(P\) has order 2 in \(E(\mathbb{Q})\). This is pure group theory, but it’s already number theory, because we are talking about rational solutions to a cubic.

You can do the same arithmetic mod a prime \(p\):

**Example over \(\mathbb{F}_5\)**: curve \(E: y^2 = x^3 + 4x + 4\) modulo 5, as in Dummit’s notes. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

Take \(P_1=(1,3)\), \(P_2=(0,2)\) in \(\mathbb{F}_5^2\). Compute \(P_1+P_2\):

- Slope
  \[
  m = (2-3)/(0-1) = (-1)/(-1) = 1 \pmod 5.
  \]
- Then
  \[
  x_3 = m^2 - x_1 - x_2 = 1 - 1 - 0 = 0 \pmod 5,
  \]
  \[
  y_3 = -m(x_3 - x_1) - y_1 = -1(0-1) - 3 = -(-1) - 3 = 1 - 3 = -2 \equiv 3 \pmod 5.
  \]
So \(P_1 + P_2 = (0,3)\) in \(E(\mathbb{F}_5)\). [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

This concrete group structure over \(\mathbb{F}_p\) is used heavily in number theory and cryptography.

***

## 3. Number theory example 1: counting points mod \(p\) and Hasse’s bound

For each prime \(p\), reduce the coefficients of \(E\) modulo \(p\) and count points \(\#E(\mathbb{F}_p)\). [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

Definition:

\[
a_p = p + 1 - \#E(\mathbb{F}_p).
\]

Hasse’s theorem says

\[
|a_p| \le 2\sqrt{p}.[]
\]

Concrete example: stick with \(E: y^2 = x^3 + 4x + 4\) mod 5 from above. [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

One can list all \(x\in\mathbb{F}_5\) and check whether \(x^3+4x+4\) is a square mod 5; Dummit does this and finds a finite list of points including the point at infinity, say \(\#E(\mathbb{F}_5)=N\) (the notes spell out the exact count). [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

Suppose (for illustration) \(\#E(\mathbb{F}_5) = 9\). Then

\[
a_5 = 5 + 1 - 9 = -3,
\]
and indeed \(|a_5|=3 \le 2\sqrt{5}\approx 4.47\).

The sequence \(a_p\) for varying primes carries deep arithmetic information:
- They appear as coefficients of the \(L\)-function \(L(E,s)=\prod_p (1-a_p p^{-s} + p^{1-2s})^{-1}\).  
- For modular elliptic curves over \(\mathbb{Q}\), this \(L\)-function is a modular form’s L-function; this is the content of modularity theorems leading to Fermat’s Last Theorem. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

So “counting points mod \(p\)” is not just bookkeeping; it builds global analytic objects (L-functions) that encode the arithmetic of \(E\).

***

## 4. Number theory example 2: solving Diophantine equations via rank

Let \(E(\mathbb{Q})\) be the group of rational points; Mordell’s theorem:  

\[
E(\mathbb{Q}) \cong E(\mathbb{Q})_{\text{tors}} \oplus \mathbb{Z}^r,
\]

where \(r\) is the rank. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)
Rank \(r>0\) means infinitely many rational points (solutions) to the cubic equation.

Concrete example: \(E: y^2 = x^3 - x\) again. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

- We saw \(P=(0,0)\) has order 2.  
- One can find other rational points like \(Q=(2, \pm \sqrt{6})\) are not rational, but \(P=(0,0)\), \((\pm1,0)\) are torsion, etc.  
- For some curves (e.g. \(y^2 = x^3 - x + 1\)), you can find a point \(P\) of infinite order and then generate infinitely many distinct rational solutions by taking multiples \(nP\).

From a Diophantine perspective, you have upgraded “find all integer solutions to this cubic” to “understand the structure of a finitely generated abelian group”, which is much more tractable conceptually.

This is exactly how elliptic curves enter classical Diophantine problems (e.g., integer points on curves like \(y^2 = x^3 - 2\), congruent number problems, etc.). [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)

***

## 5. Number theory example 3: elliptic curves over \(\mathbb{F}_p\) and crypto

Over a finite field \(\mathbb{F}_p\), \(E(\mathbb{F}_p)\) is a finite abelian group; Hasse’s theorem gives \(\#E(\mathbb{F}_p)\approx p\). [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)

In elliptic curve cryptography (ECC):

- Choose a prime \(p\) and an elliptic curve \(E/\mathbb{F}_p\).  
- Choose a point \(P\in E(\mathbb{F}_p)\) of large prime order \(n\).  
- The **discrete logarithm problem**: given \(P\) and \(Q=kP\), find \(k\). This is hard for suitably chosen curves and parameters. [people.cs.nycu.edu](https://people.cs.nycu.edu.tw/~rjchen/ECC2012S/Elliptic%20Curves%20Number%20Theory%20And%20Cryptography%202n.pdf)

Concrete arithmetic example on a toy curve (small field, so not secure but illustrative):

Let \(p=5\), \(E: y^2 = x^3 + 4x + 4\) over \(\mathbb{F}_5\) as before. Dummit shows: [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)

- \(P=(1,3)\) has order 4: 
  - \(2P=(2,0)\), \(3P=(1,2)\), \(4P=\mathcal{O}\). [dummit.cos.northeastern](https://dummit.cos.northeastern.edu/docs/numthy_7_elliptic_curves.pdf)
- Then the subgroup generated by \(P\) has 4 elements: \(\{\mathcal{O}, P,2P,3P\}\).

If this were a large prime order subgroup in a big field, the map \(k\mapsto kP\) would be one-way. Number theory enters in:

- Ensuring \(\#E(\mathbb{F}_p)\) has a large prime factor.  
- Using point-counting algorithms (Schoof–Elkies–Atkin) based on the arithmetic of \(E\) and modular polynomials to compute \(\#E(\mathbb{F}_p)\) efficiently. [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)

Those point-counting algorithms themselves rely on deep links between elliptic curves, modular forms, and isogenies—very close in spirit to the modular-form/partition-story you were reading.

***

## 6. How this ties back to modular forms and partitions

Elliptic curves, modular forms, and number theory are tightly coupled:

- Each elliptic curve over \(\mathbb{C}\) is analytically isomorphic to a complex torus \(\mathbb{C}/\Lambda\) built from a lattice \(\Lambda\). [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)
- The invariants of \(\Lambda\) (like its \(j\)-invariant) are modular functions of the lattice parameter \(\tau\); thus elliptic curves are parameterized by modular curves (quotients of the upper half-plane by subgroups of \(\mathrm{SL}_2(\mathbb{Z})\)). [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)
- For elliptic curves over \(\mathbb{Q}\), the \(L\)-function \(L(E,s)\) is the same as the \(L\)-function of a weight 2 modular form; this is the modularity theorem. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)
- In the thesis you read, modular forms of higher weight/level are used similarly to encode arithmetic data (here, partition numbers instead of \(a_p\)), and Hecke operators play the role of capturing the prime-by-prime structure.

So elliptic curves provide one of the “simplest” contexts where modular forms and number theory interact; partitions are another, more combinatorially flavored one.

***

To connect with what is most useful for you: would you like to go deeper into (i) the explicit arithmetic of \(E(\mathbb{F}_p)\) and point counting, (ii) the modularity/L-function side for elliptic curves over \(\mathbb{Q}\), or (iii) how to explicitly compute with elliptic curves (e.g., Sage examples) to see these number-theoretic phenomena in practice?

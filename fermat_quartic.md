
Your title seems to be cut off, and “Fermat’s quartic” can mean two closely related but different equations. I’ll give the local-solubility answer for the two most common meanings.

## Quick summary

1. **Projective Fermat quartic curve**
   \[
   C:\;X^4+Y^4+Z^4=0.
   \]
   - It has **no real point**, so it is **not locally soluble over \(\mathbb R\)**.
   - At finite primes, it has a \(\mathbb Q_p\)-point **iff**
     \[
     p\notin\{2,5,29\}.
     \]
   So among finite places the exceptional primes are \(2,5,29\).

2. **FLT-style Fermat quartic**
   \[
   D:\;X^4+Y^4=Z^4.
   \]
   - It has local points over **every** \(\mathbb Q_v\), including \(\mathbb R\).
   - In fact, it has points with \(XYZ\neq 0\) over every \(\mathbb Q_v\).
   - Nevertheless it has **no nonzero rational solution** by Fermat’s theorem for exponent \(4\).

Below are the details.

---

# 1. The curve \(C: X^4+Y^4+Z^4=0\)

## Real place

Over \(\mathbb R\), every fourth power is nonnegative, so
\[
X^4+Y^4+Z^4=0
\]
forces \(X=Y=Z=0\), which is not a projective point. Thus
\[
C(\mathbb R)=\varnothing.
\]

So if “locally soluble” includes the real place, the answer is immediately **no**.

---

## The prime \(p=2\)

Suppose there were a \(\mathbb Q_2\)-point. Scaling gives a primitive triple
\[
(X,Y,Z)\in\mathbb Z_2^3,
\]
not all divisible by \(2\).

For any \(2\)-adic integer \(u\),

- if \(u\) is even, then \(u^4\equiv 0\pmod{16}\);
- if \(u\) is odd, then \(u^4\equiv 1\pmod{16}\).

Thus \(X^4+Y^4+Z^4\) is congruent modulo \(16\) to the number of odd coordinates among \(X,Y,Z\). Since the triple is primitive, that number is \(1,2,\) or \(3\), never \(0\). Hence
\[
X^4+Y^4+Z^4\not\equiv 0\pmod{16}.
\]
Therefore
\[
C(\mathbb Q_2)=\varnothing.
\]

---

## Odd primes: reduction to \(\mathbb F_p\)

For \(p\neq 2\), the curve has good reduction over \(\mathbb F_p\), because the partial derivatives are
\[
4X^3,\quad 4Y^3,\quad 4Z^3,
\]
and they cannot all vanish at a projective point modulo \(p\).

Therefore, for odd \(p\),
\[
C(\mathbb Q_p)\neq\varnothing
\quad\Longleftrightarrow\quad
C(\mathbb F_p)\neq\varnothing.
\]

So the question becomes: for which odd primes \(p\) does
\[
X^4+Y^4+Z^4=0
\]
have a nontrivial solution modulo \(p\)?

---

## Case 1: \(p\equiv 3\pmod 4\)

If \(p\equiv 3\pmod 4\), then \(\gcd(4,p-1)=2\), so the fourth powers in \(\mathbb F_p^\times\) are exactly the squares.

Over any finite field \(\mathbb F_p\) with \(p\) odd, the quadratic equation
\[
u^2+v^2+w^2=0
\]
has a nontrivial solution. One elementary proof is: the set of squares in \(\mathbb F_p\) has size \((p+1)/2\), and the sets
\[
S=\{u^2:u\in\mathbb F_p\},\qquad -1-S=\{-1-v^2:v\in\mathbb F_p\}
\]
both have size \((p+1)/2\), so they intersect. Thus there are \(u,v\) with
\[
u^2+v^2+1=0.
\]

Since every square is a fourth power when \(p\equiv 3\pmod 4\), the values \(u^2,v^2,1\) are fourth powers. Hence we obtain a point on \(C(\mathbb F_p)\).

Thus:
\[
p\equiv 3\pmod 4 \implies C(\mathbb Q_p)\neq\varnothing.
\]

---

## Case 2: \(p\equiv 1\pmod 8\)

If \(p\equiv 1\pmod 8\), then \(-1\) is a fourth power in \(\mathbb F_p^\times\). Choose \(a\in\mathbb F_p\) such that
\[
a^4=-1.
\]
Then
\[
(a:1:0)\in C(\mathbb F_p),
\]
because
\[
a^4+1^4+0^4=-1+1+0=0.
\]
By Hensel’s lemma this lifts to a \(\mathbb Q_p\)-point. Hence
\[
p\equiv 1\pmod 8 \implies C(\mathbb Q_p)\neq\varnothing.
\]

---

## Case 3: \(p\equiv 5\pmod 8\)

This is the subtle case. Here \(-1\) is not a fourth power, so the previous boundary-point trick does not work.

For large primes, Weil’s bound for smooth plane curves settles it. The curve \(C\) is a smooth plane quartic, hence has genus
\[
g=\frac{(4-1)(4-2)}2=3.
\]
Hasse–Weil gives
\[
\#C(\mathbb F_p)\ge p+1-2g\sqrt p
= p+1-6\sqrt p.
\]
For \(p\ge 37\),
\[
p+1-6\sqrt p>0,
\]
so \(C(\mathbb F_p)\neq\varnothing\), and hence
\[
C(\mathbb Q_p)\neq\varnothing.
\]

Thus only the primes
\[
p\equiv 5\pmod 8,\qquad p<37
\]
need to be checked directly. These are
\[
5,\;13,\;29.
\]

### \(p=5\)

In \(\mathbb F_5\), the only fourth powers are \(0\) and \(1\). A sum of three elements from \(\{0,1\}\) can be \(0,1,2,3\) modulo \(5\), but it is \(0\) only if all three are \(0\). Thus there is no nontrivial projective solution. So
\[
C(\mathbb Q_5)=\varnothing.
\]

### \(p=13\)

There is a solution:
\[
(1:2:6)\in C(\mathbb F_{13}),
\]
because
\[
1^4+2^4+6^4\equiv 1+3+9=13\equiv 0\pmod{13}.
\]
Thus
\[
C(\mathbb Q_{13})\neq\varnothing.
\]

### \(p=29\)

The nonzero fourth powers modulo \(29\) are
\[
H=\{1,7,16,20,23,24,25\}.
\]
One checks that no three elements of \(H\cup\{0\}\), not all zero, sum to \(0\pmod{29}\). Equivalently, the pair-sum set \(H+H\) is disjoint from \(-H\). Hence
\[
C(\mathbb F_{29})=\varnothing,
\]
and therefore
\[
C(\mathbb Q_{29})=\varnothing.
\]

---

## Finite-prime conclusion for \(X^4+Y^4+Z^4=0\)

Combining the cases:

\[
C(\mathbb Q_p)\neq\varnothing
\quad\Longleftrightarrow\quad
p\notin\{2,5,29\}.
\]

Including the real place, \(C\) is **not** locally soluble because \(C(\mathbb R)=\varnothing\).

---

# 2. The curve \(D: X^4+Y^4=Z^4\)

This is the Fermat equation of exponent \(4\). If coordinate-zero points are allowed, local solubility is trivial because, for example,
\[
(1:0:1)\in D(\mathbb Q).
\]
The more interesting statement is that \(D\) has local points with
\[
XYZ\neq 0
\]
at every place.

---

## Real place

Over \(\mathbb R\), take
\[
X=Y=1,\qquad Z=2^{1/4}.
\]
Then
\[
1^4+1^4=(2^{1/4})^4=2.
\]
So
\[
D(\mathbb R)\neq\varnothing.
\]

---

## Odd primes

Let \(p\) be odd. Choose \(t\in p\mathbb Z_p\), for example \(t=p\). We want a \(p\)-adic solution to
\[
Z^4=1+t^4.
\]
Consider
\[
f(Z)=Z^4-(1+t^4).
\]
Then
\[
f(1)=-t^4\equiv 0\pmod p,
\]
and
\[
f'(1)=4\not\equiv 0\pmod p
\]
because \(p\) is odd. By Hensel’s lemma, there exists \(z\in\mathbb Z_p\) such that
\[
z^4=1+t^4.
\]
Thus
\[
(t:1:z)\in D(\mathbb Q_p),
\]
with \(t,1,z\neq 0\). Hence
\[
D(\mathbb Q_p)\neq\varnothing
\]
for every odd prime \(p\).

---

## The prime \(p=2\)

We need a \(2\)-adic solution to, for example,
\[
Z^4=17.
\]
A standard fact about \(\mathbb Q_2\) is:

> A unit \(u\in\mathbb Z_2^\times\) is a fourth power iff \(u\equiv 1\pmod{16}\).

Since
\[
17\equiv 1\pmod{16},
\]
there exists \(z\in\mathbb Z_2^\times\) with
\[
z^4=17.
\]
Therefore
\[
(2:1:z)\in D(\mathbb Q_2),
\]
with all coordinates nonzero.

So
\[
D(\mathbb Q_2)\neq\varnothing.
\]

---

## Global contrast

Although \(D\) has local points with \(XYZ\neq 0\) everywhere, Fermat’s theorem for exponent \(4\) says there is no nonzero integer solution to
\[
X^4+Y^4=Z^4.
\]
Equivalently, there is no rational projective point on \(D\) with \(XYZ\neq 0\).

Thus the open curve
\[
D^\circ:\;X^4+Y^4=Z^4,\quad XYZ\neq 0
\]
is everywhere locally soluble but has no rational point. The full projective curve \(D\) itself does have rational points, namely the “trivial” ones with one coordinate zero.

---

## If you meant \(X^4+Y^4=Z^2\)

This is another common “Fermat quartic” related to Fermat’s right-triangle theorem. It is also locally soluble everywhere with \(XYZ\neq 0\). The proof is the same but uses square roots instead of fourth roots:

- For odd \(p\), solve
  \[
  Z^2=1+p^4
  \]
  by Hensel’s lemma.
- For \(p=2\), note that \(17\equiv 1\pmod 8\), so \(17\) is a square in \(\mathbb Q_2\).

Globally, however, \(X^4+Y^4=Z^2\) has no nonzero integer solutions.

---

If you had a specific Fermat quartic equation in mind, send the exact equation and I can tailor the local-solubility argument to that one.

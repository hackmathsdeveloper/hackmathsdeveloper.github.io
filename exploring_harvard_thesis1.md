
[https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)
explain in outline the article, and extract all the important points of the thesis and for each extracted point, elaborate in details by using concrete examples so as to meet a wider reader audience.


## 1. Big-picture outline of the thesis

The thesis studies how modular forms can be used to prove deep congruence properties of the partition function \(p(n)\), especially generalizing Ramanujan’s classical congruences like \(p(5n+4)\equiv 0 \pmod 5\).

At a high level, the structure is:

- **Section 1:** Partitions and Ramanujan-type congruences; motivation from combinatorics and their surprising modular-form proofs.  
- **Section 2:** Core theory of modular forms: modular group, fundamental domain, Eisenstein series, valence/dimension formulas, congruence subgroups, Hecke operators, half-integral weight forms.  
- **Section 3:** Using modular forms to reprove Ramanujan’s congruences modulo 5, 7, 11.  
- **Section 4:** Another family of partition congruences using Hecke operators on integral-weight forms (mod 13,17,19,23,29,31).  
- **Sections 5–6:** Heavy-duty modular-forms machinery (Shimura correspondence, half-integral weight Hecke operators, Serre’s theorem) to prove that for every \(m\) coprime to 6, there are infinitely many linear progressions \(an+b\) on which \(p(an+b)\equiv 0 \pmod m\).  
- **Section 7:** Practical algorithmic method to extract explicit congruences from those existence results (following Weaver) and concrete examples for primes \(13\le m\le 31\).

The rest of this answer isolates the main “important points” and for each gives a fairly concrete explanation with examples that do not assume prior modular forms background.

As you read, it may help to keep the mental model: 

> “Partitions are combinatorial; modular forms are analytic. The thesis explains how analytic symmetry properties of certain \(q\)-series encode combinatorial congruences for partitions.”

***

## 2. The partition function and Ramanujan’s congruences

### 2.1 The partition function and its generating series

- **Definition:** \(p(n)\) is the number of ways to write \(n\) as a sum of positive integers in nondecreasing order; by convention \(p(0)=1\).  
  Example: For \(n=5\), the partitions are  
  \[
  5,\ 4+1,\ 3+2,\ 3+1+1,\ 2+2+1,\ 2+1+1+1,\ 1+1+1+1+1,
  \]  
  so \(p(5)=7\).

- The **generating function** of \(p(n)\) is
  \[
  \sum_{n\ge 0} p(n) q^n = \prod_{n\ge 1} \frac{1}{1-q^n},
  \]
  which is an infinite product encoding all partitions at once.  
  This product is key: it is essentially \(\eta(z)^{-1}\), where \(\eta\) is Dedekind’s eta function, a modular object.

- There is a famous asymptotic formula
  \[
  p(n) \sim \frac{1}{4n\sqrt{3}} \exp\!\left(\pi\sqrt{\frac{2n}{3}}\right)
  \]
  derived by Hardy and Ramanujan using the circle method; this already uses analytic tools.

**Concrete viewpoint:**  

If you know basic generatingfunctionology, \(\prod_{n\ge 1} (1-q^n)^{-1}\) is the “coin-change” generating function where you have infinitely many coins of each denomination. The thesis uses that this generating function is essentially a modular form (up to a factor) to deduce congruences.

### 2.2 Ramanujan’s congruences and their generalization

Ramanujan discovered three striking congruences:

- \(p(5n+4) \equiv 0 \pmod 5\)  
- \(p(7n+5) \equiv 0 \pmod 7\)  
- \(p(11n+6) \equiv 0 \pmod{11}\)

For example, check the first one for small \(n\):

- \(p(4)=5\equiv 0\pmod 5\)  
- \(p(9)=30\equiv 0\pmod 5\)  
- \(p(14)=135\equiv 0\pmod 5\)

Ramanujan conjectured these were essentially the only “simple” congruences of the form \(p(\ell n + \beta)\equiv 0 \pmod \ell\) with \(\ell\) prime and valid for all \(n\); this was later proved.

But the story **does not stop** with these three primes. There are more complicated congruences, like (Atkin, O’Brien, etc.):

- \(p(11^3 \cdot 13n + 237) \equiv 0 \pmod{13}\)  
- \(p(594 \cdot 13n + 111247) \equiv 0 \pmod{13}\)

These look bizarre combinatorially but become natural when viewed through the lens of modular forms and Hecke operators.

**The thesis’ main “global” result:**  

Following Ahlgren–Ono, the thesis explains that for every integer \(m\) with \(\gcd(m,6)=1\), there exist infinitely many arithmetic progressions \(an+b\) such that
\[
p(an+b) \equiv 0 \pmod m\quad\text{for all }n \ge 0.[file:0]
\]

This tells you: congruence phenomena for \(p(n)\) modulo “nice” moduli are not rare accidents – they are ubiquitous, but detecting them requires modular forms.

***

## 3. Core modular forms toolkit (Section 2)

### 3.1 Modular group, action, and fundamental domain

- The **upper half-plane** is \(\mathbb{H} = \{z\in\mathbb{C} : \operatorname{Im} z > 0\}\).  
- The group \(\mathrm{SL}_2(\mathbb{Z})\) acts on \(\mathbb{H}\) via Möbius transformations
  \[
  \gamma z = \frac{az+b}{cz+d}, \quad \gamma=\begin{pmatrix} a & b \\ c & d\end{pmatrix}.[file:0]
  \]
- The “modular group” often means \(\mathrm{PSL}_2(\mathbb{Z})\), i.e. modding out by \(\pm I\) since \(-I\) acts trivially.

Key geometric fact: \(\mathrm{SL}_2(\mathbb{Z})\) has a standard **fundamental domain**
\[
\mathcal{F}=\{ z\in\mathbb{H} : |z|\ge 1,\ |\Re z|\le 1/2\},
\]
so every orbit meets \(\mathcal{F}\) and no two interior points are equivalent.

This is your “unit cell” for the action. Many modular form arguments count zeros in \(\mathcal{F}\) and at the cusps.

**Example of the action:**  

Take \(z=i\) and \(\gamma=\begin{pmatrix}0 & -1 \\ 1 & 0\end{pmatrix}\). Then \(\gamma z = -1/z = -1/i = i\). So \(i\) is a fixed point of that matrix, which explains why it gets special weight in the valence formula later.

### 3.2 Definition of modular forms and \(q\)-expansions

For \(\mathrm{SL}_2(\mathbb{Z})\):

- A modular form of **weight** \(k\) is a holomorphic function \(f:\mathbb{H}\to\mathbb{C}\) such that  
  \[
  f\!\left(\frac{az+b}{cz+d}\right) = (cz+d)^k\,f(z)\quad\forall \begin{pmatrix}a&b\\ c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb{Z}),
  \]
  and \(f\) is bounded as \(\operatorname{Im} z\to\infty\).

- The condition \(f(z+1)=f(z)\) implies \(f\) is periodic and can be written as a holomorphic function in \(q=e^{2\pi i z}\):  
  \[
  f(z)=\sum_{n\ge 0} a(n)\,q^n.[file:0]
  \]
  This is the **\(q\)-expansion**. A **cusp form** is one with \(a(0)=0\).

**Concrete example of the idea:**  

Even without knowing explicit modular forms, if you take any periodic holomorphic function with good growth, you can Fourier-expand it. The modular condition is just a highly symmetric version of “nice periodicity” under a bigger group than translations.

For congruence subgroups \(\Gamma_0(N),\Gamma_1(N)\), the definition is similar but you only impose the transformation law for \(\gamma\in \Gamma\), and you must be holomorphic (or vanish) at **every cusp**, not just \(\infty\).

### 3.3 Eisenstein series and the \(\Delta\)-function

For even \(k\ge 4\), define the (unnormalized) Eisenstein series
\[
G_k(z)= \sum_{(m,n)\in\mathbb{Z}^2\setminus\{(0,0)\}} \frac{1}{(mz+n)^k},[file:0]
\]
which converges and is a modular form.

After normalizing using values of the zeta function and Bernoulli numbers \(B_k\), one gets
\[
E_k(z)=1 - \frac{2k}{B_k}\sum_{n\ge 1} \sigma_{k-1}(n) q^n,
\]
where \(\sigma_{k-1}(n)=\sum_{d\mid n} d^{k-1}\).

These \(E_4, E_6,\dots\) generate the ring of modular forms for \(\mathrm{SL}_2(\mathbb{Z})\). In particular, the unique cusp form of weight 12 is
\[
\Delta(z)=\frac{1}{1728}\big(E_4(z)^3 - E_6(z)^2\big)=\sum_{n\ge 1}\tau(n)q^n.[file:0]

**Concrete arithmetic identity via dimension theory:**  

Using the dimension formula (see below), one knows \(M_8\) is 1-dimensional; both \(E_4^2\) and \(E_8\) are nonzero and have constant term 1, so they must be equal: \(E_4^2 = E_8\).[file:0]

Equate coefficients of \(q^n\):
\[
\left(1 + 240\sum_{n\ge1}\sigma_3(n)q^n\right)^2 
= 1 + 480\sum_{n\ge1}\sigma_7(n)q^n,
\]
which yields a purely arithmetic identity expressing \(\sigma_7(n)\) in terms of \(\sigma_3\) and its convolution.[file:0]  
This is a paradigm: analytic structure forces combinatorial/number-theoretic identities.

\(\Delta\) and its coefficients \(\tau(n)\) are also deeply connected to partitions (through \(\eta\)-products) and appear later when building modular forms whose coefficients encode partition values.

### 3.4 Valence and dimension formulas

For a nonzero modular form \(f\), the **valence formula** relates the sum of orders of zeros (including cusps) to the weight \(k\).[file:0] For \(\mathrm{SL}_2(\mathbb{Z})\),
\[
\operatorname{ord}_\infty(f) 
+\tfrac12\operatorname{ord}_i(f) 
+\tfrac13\operatorname{ord}_\rho(f)
+\sum_{z \in \mathcal{F}'} \operatorname{ord}_z(f) = \frac{k}{12},
\]
where \(\rho=e^{2\pi i/3}\) and the sum is over remaining interior points in the fundamental domain.[file:0]

Combine this with the fact that modular forms are holomorphic ⇒ orders are nonnegative ⇒ strong constraints on how many zeros (and of what orders) are possible. This leads to a **dimension formula** for \(M_k(\mathrm{SL}_2(\mathbb{Z}))\) and for cusp forms \(S_k\).[file:0]

**Example use:**  

- For weight \(k<0\) there can be no nonzero modular forms: the valence formula would force a negative sum of nonnegative integers.[file:0]  
- For small positive even \(k\), you can show \(\dim M_k = 1\), so any nonzero form is a scalar multiple of \(E_k\). This is exactly what was used above to show \(E_4^2=E_8\).[file:0]

This “finite dimensionality + explicit basis” is *the* mechanism the thesis uses to compare modular forms that encode the partition generating series with other known modular forms.

### 3.5 Hecke operators (integral weight)

Hecke operators are linear operators on spaces of modular forms that act in a very arithmetic way on the \(q\)-coefficients.[file:0]

For example, for level 1, weight \(k\), the Hecke operator \(T(m)\) acts by a double-coset formula; concretely, in terms of \(q\)-series,
\[
\left(\sum_{n\ge0} a(n)q^n\right)\Big|T(m)
= \sum_{n\ge0} b(n)q^n,
\]
where
\[
b(n)=\sum_{d\mid \gcd(n,m)} d^{k-1}\,a\!\left(\frac{mn}{d^2}\right).
\]

Properties:

- They preserve the space \(M_k\) and also the cusp subspace \(S_k\).[file:0]  
- For fixed \(k\), the Hecke operators commute and can be simultaneously diagonalized; eigenforms have multiplicative coefficients that behave like eigenvalues.[file:0]

**Concrete feel:**  

If you think of \(a(n)\) as Fourier coefficients like \(\tau(n)\) or partition-related coefficients, the action of \(T(\ell)\) mixes them in a controlled way using divisors and powers of \(\ell\). For eigenforms, you get multiplicative relations like
\[
a(\ell n) = a(\ell) a(n) - \ell^{k-1} a(n/\ell),
\]
which are key in controlling arithmetic properties.

The thesis later uses Hecke operators to build modular forms whose coefficients are \(p(n)\) modulo \(\ell\) and then enforces vanishing of those coefficients via spectral properties.

### 3.6 Half-integral weight forms and Shimura correspondence (preview)

The thesis briefly introduces modular forms of half-integral weight (like weight \(k+1/2\)), which are subtler objects living on congruence subgroups with multipliers.[file:0]

Key tools later:

- **Eta-products:** expressions involving powers of Dedekind’s \(\eta(z)\), which often yield half-integral weight forms.[file:0]  
- **Shimura correspondence:** a deep map between half-integral weight eigenforms and integral weight eigenforms, preserving Hecke eigenvalues in a controlled way.[file:0]

These underlie Ahlgren–Ono’s machinery: starting from partition-type generating functions (involving \(\eta^{-1}\)), one constructs half-integral weight objects, then uses Shimura to connect them to better-understood integral weight forms where Hecke theory and Serre’s theorem can be applied.

***

## 4. The Ramanujan congruences via modular forms (Section 3)

The thesis gives a modular-form-based proof of Ramanujan’s congruences.[file:0]

Key conceptual steps (without going into full technical details):

1. **Express the generating function in modular terms:**  
   Use
   \[
   \prod_{n\ge 1} \frac{1}{1-q^n} = q^{-1/24}\,\eta(z)^{-1},
   \]
   where \(\eta(z)\) is a weight \(1/2\) modular form (up to a multiplier system).[file:0] This means the partition generating function is a modular object of half-integral weight.

2. **Consider specific linear combinations that pick out arithmetic progressions:**  
   For example, to study \(p(5n+4)\), one considers a modular form whose \(q\)-series is
   \[
   \sum_{n\ge0} p(5n+4) q^n
   \]
   times an explicit modular factor to adjust weight and level.[file:0]

3. **Use congruences between modular forms:**  
   Show that this constructed modular form is congruent modulo \(\ell\) to a modular form that vanishes (or has forced zeros) because of dimension constraints or eigenvalue conditions.[file:0]

4. **Conclude coefficient-wise vanishing:**  
   Since two modular forms are congruent modulo \(\ell\), their coefficients are congruent modulo \(\ell\). If one form is zero (or has coefficients in a sparse pattern), this gives the desired congruence for \(p(n)\).[file:0]

**Concrete analogy:**  

Imagine you build a \(q\)-series \(F(q)=\sum a(n) q^n\) whose coefficients are \(a(n)\equiv p(5n+4)\pmod 5\). If you can prove \(F\) is a modular form of low weight and dimension 1 (mod 5), then \(F\) must be a scalar multiple of some known form modulo 5. If that known form vanishes, you get \(a(n)\equiv 0\), i.e. \(p(5n+4)\equiv 0\pmod 5\).

The thesis gives a clean exposition of such a modular proof, connecting directly to the general techniques later (Sections 4–6).[file:0]

***

## 5. Hecke-operator-based families of congruences (Section 4)

Section 4 focuses on congruences that can be obtained using only integral-weight modular forms over \(\mathrm{SL}_2(\mathbb{Z})\) and Hecke operators, plus computer-checkable calculations.[file:0]

### 5.1 Construction of forms \(F(\ell,k;z)\)

The thesis considers modular forms \(F(\ell,k;z)\) whose coefficients encode partition numbers in a way adapted to modulus \(\ell\) and a parameter \(k\).[file:0] Roughly:

- Start from \(\eta(z)^{-1}\) or related forms.  
- Multiply by suitable powers of \(\Delta(z)\) and Eisenstein series to achieve integral weight and level 1.  
- Possibly apply operators like the Serre derivative or Hecke operators.

The details are technical, but the pattern is: build a modular form whose coefficients “are” the quantities you want to study modulo \(\ell\).

### 5.2 Hecke action and congruences modulo primes

For primes \(\ell\in\{13,17,19,23,29,31\}\), Ono’s original method produced congruences involving \(p(n)\) modulo \(\ell\). Narayanan tweaks Ono’s constructions to create a more uniform framework, then extends explicitly to \(\ell=29,31\).[file:0]

The strategy:

- Show that \(F(\ell,k;z)\) is an eigenfunction (or nearly so) for certain Hecke operators modulo \(\ell\).[file:0]  
- Use the eigenvalue relations to force patterns in the coefficients, implying that along certain progressions \(an+b\), the coefficients vanish modulo \(\ell\).[file:0]

**Concrete flavor of a result (schematically):**  

You end up with congruences like
\[
p(A\ell^\alpha n + B) \equiv 0 \pmod \ell
\]
for appropriately chosen \(A,B,\alpha\) depending on \(\ell\). The exact tuples are tabulated in the thesis and derived via modular/Hecke computations, with explicit checks done by computer for finitely many coefficients (enough because of dimension bounds).[file:0]

***

## 6. Heavy background: orders, eta-products, Shimura, Serre (Section 5)

Section 5 assembles a toolkit of general modular-forms results that Ahlgren–Ono need.[file:0]

Important components:

1. **Computing orders at cusps:**  
   Formulas for \(\operatorname{ord}_\alpha(f)\) in terms of the \(q\)-expansions under various slash operators. Necessary to show holomorphy/vanishing and to control where zeros are.[file:0]

2. **Conversions between modular forms at different levels and weights:**  
   How to transform a form on \(\Gamma_0(N)\) to one on \(\Gamma_0(M)\) via operators like \(f(z)\mapsto f(az)\) or Atkin–Lehner involutions, while tracking orders and weights.[file:0]

3. **Eta-products:**  
   Rational combinations of products
   \[
   \prod_{d\mid N} \eta(dz)^{r_d}
   \]
   with integer exponents \(r_d\), which under certain linear constraints give modular forms of half-integral weight on \(\Gamma_0(N)\).[file:0] These are a natural way to build modular objects directly from the partition generating function.

4. **Shimura correspondence:**  
   A correspondence between certain half-integral weight cusp forms on \(\Gamma_0(4N)\) and integral weight forms on \(\Gamma_0(N)\), preserving Hecke eigenvalues in a predictable way.[file:0] This acts as a bridge: start with something partition-flavored (half-integral), move to an integral-weight world where Serre-type theorems apply.

5. **Half-integral weight Hecke operators on \(\Gamma_1(N)\):**  
   The Hecke action is more complicated than in integral weight but still manageable; one gets relations resembling those in integral weight but with different local factors.[file:0]

6. **Serre’s theorem on Hecke operators:**  
   A deep result controlling the density and distribution of coefficients of modular forms modulo primes; roughly, it says that Hecke eigenvalues modulo a prime are distributed in such a way that you can force infinitely many coefficients to vanish on arithmetic progressions.[file:0]

**Concrete upshot for the thesis:**  

These tools collectively allow one to take “partition-modular” generating functions, push them through Shimura to get to integral weight, then apply Serre’s theorem to conclude: for each modulus \(m\) coprime to 6, there are infinitely many congruences of the shape \(p(an+b)\equiv 0 \pmod m\).[file:0]

***

## 7. Ahlgren–Ono’s general congruence theorem (Section 6)

Sections 5–6 reproduce and elaborate Ahlgren–Ono’s main result.[file:0]

### 7.1 Statement in accessible terms

Let \(m\) be a positive integer with \(\gcd(m,6)=1\). Then there exist infinitely many pairs \((a,b)\) of positive integers such that
\[
p(an+b)\equiv 0 \pmod m \quad\text{for all }n\ge 0.
\]

What does this mean?

- Fix, say, \(m=13\). Then there are infinitely many arithmetic progressions of the form \(an+b\) so that all partition numbers along that progression are multiples of 13.[file:0]  
- The theorem guarantees their existence but does not directly give a closed-form description of all such \((a,b)\).

### 7.2 Proof strategy (high level)

The proof follows this conceptual chain:

1. Construct a half-integral weight modular form \(f(z)\) whose coefficients are closely related to \(p(n)\) modulo \(m\).[file:0]  
   This uses eta-products and manipulations like multiplying by powers of \(\Delta\) to get holomorphy and finite level.

2. Use the Shimura correspondence to map \(f\) to an integral weight modular form \(F\) on some \(\Gamma_0(N)\).[file:0]

3. Use Serre’s theorem (and related algebraic properties of Hecke eigenvalues) to show that there are infinitely many primes \(\ell\) for which the action of \(T(\ell)\) modulo \(m\) forces a long pattern of zero coefficients along certain residue classes.[file:0]

4. Trace back through the Shimura correspondence and the definitions to interpret those zero coefficients as congruences for \(p(n)\) on progressions \(an+b\).[file:0]

Conceptually, Hecke eigenvalues and their reduction modulo \(m\) encode arithmetic structure of the coefficients. When those eigenvalues satisfy certain congruences, the coefficients of the form become zero modulo \(m\) on structured sets; those sets translate to congruences for \(p(n)\).

***

## 8. From existence to explicit congruences (Section 7)

The final section addresses a practical question:  

> Given the existence results, how can one **compute explicit congruences** for specific moduli like \(13,17,\dots,31\)?[file:0]

The method, following a paper of Weaver:

1. For a fixed prime \(m\), construct an explicit modular form \(f_m(z)\) whose coefficients encode \(p(n) \pmod m\), using the general scheme from Sections 5–6 but specialized so that levels and weights are controllable.[file:0]

2. Use the known dimension of the relevant space of modular forms to bound how many Fourier coefficients need to be checked in order to identify \(f_m(z)\) in the basis of that space (modulo \(m\)).[file:0]

3. Compute those coefficients explicitly for \(n\) up to some bound (software or custom code) and solve the resulting linear system modulo \(m\) to identify \(f_m\) as a combination of basis forms.[file:0]

4. Once \(f_m\) is expressed in terms of Hecke eigenforms, apply Hecke relations modulo \(m\) to deduce patterns of vanishing of coefficients, i.e. explicit congruences for \(p(n)\).[file:0]

The appendix includes a table of concrete \((\ell,m)\) pairs producing explicit congruences.[file:0] These are the analogs of classical Ramanujan-type congruences but for higher primes, generated in a systematic, modular-forms-driven way.

**Concrete computational perspective:**  

If you wanted to “reproduce” some of these numerically, you could:

- Work in Sage/Magma, construct the relevant space \(S_k(\Gamma_0(N))\).  
- Compute Hecke operators and eigenbases.  
- Build the \(q\)-series from the partition generating function.  
- Match coefficients modulo \(m\) and solve for relations.

Narayanan’s thesis explains the theoretical justification for why such finite computation suffices (dimension and valence formulas) and how to choose \(k, N\) so the construction lands in a tractable space.[file:0]

***

## 9. For a wider audience: Intuition recap

For a non-expert mathematically literate reader, the core story can be rephrased as:

- The partition function \(p(n)\) counts ways of writing \(n\) as a sum; its generating function is a product \(\prod (1-q^n)^{-1}\).[file:0]
- That product is closely related to special analytic functions called modular forms, which are functions on the upper half-plane invariant under a group of fractional linear transformations.[file:0]
- Because modular forms live in finite-dimensional spaces and are acted on by powerful symmetry operators (Hecke operators), one can show that certain patterns in their coefficients must repeat or vanish.[file:0]
- By encoding partition numbers into modular forms and then applying these symmetry constraints, one proves that \(p(n)\) satisfies infinitely many congruences of the form “all values in this arithmetic progression are divisible by \(m\)” for any \(m\) coprime to 6.[file:0]
- The thesis both explains the general existence theory and shows how to extract explicit congruences for specific small primes using computation guided by modular-form theory.[file:0]

***


Here is a reasonably detailed “modern” modular-form proof outline of Ramanujan’s three congruences that should mesh with your background.

***

## 1. Put \(p(n)\) into the modular-forms world

The partition generating function is

\[
\sum_{n\ge 0} p(n) q^n = \prod_{m\ge 1} \frac{1}{1-q^m}
  = q^{-1/24}\,\eta(\tau)^{-1},
\]

with \(q = e^{2\pi i\tau}\) and \(\eta(\tau)=q^{1/24}\prod_{m\ge 1}(1-q^m)\) the Dedekind eta function. [en.wikipedia](https://en.wikipedia.org/wiki/Ramanujan's_congruences)

Facts you use:

- \(\eta(\tau)\) is a modular form of weight \(1/2\) (with a multiplier) on \(\mathrm{SL}_2(\mathbb Z)\).  
- Thus \(\eta(\tau)^{-1}\) is a modular form of weight \(-1/2\) in a suitable generalized sense, and its powers/eta‑quotients live in standard modular-form spaces. [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)

To avoid half-integral weights, one typically works with \(\eta(\tau)^{24}\), the discriminant form \(\Delta(\tau)\) of weight 12, and suitable combinations so that you remain in integer weight. [math.ucla](https://www.math.ucla.edu/~wdduke/preprints/ramanujan.pdf)

***

## 2. Isolate the arithmetic progressions via modular substitution

You want to study \(p(\ell n + a)\) for \(\ell\in\{5,7,11\}\). The modular-forms trick is:

1. Consider the function
   \[
   F(\tau) := \eta(\tau)^{-1} = \sum_{n\ge -1/24} a_n q^{n} 
   \quad\text{with}\quad a_{n+1/24} = p(n).
   \]
2. Apply the Hecke-style operator or, more concretely, the “\(\ell\)-dissection” operator which extracts coefficients in a given congruence class mod \(\ell\). At the level of \(q\)-series, this can be encoded as combinations of \(F(\tau)\) and \(F\left(\frac{\tau+r}{\ell}\right)\) for \(r=0,\dots,\ell-1\). [math.vanderbilt](https://math.vanderbilt.edu/rolenl/ModularFormsLecture17.pdf)

   Roughly: linear combinations of \(F\left(\frac{\tau+r}{\ell}\right)\) isolate those coefficients \(a_n\) with \(n\equiv a/24 \pmod{\ell}\), i.e. pick out \(p(\ell n + b)\) for specific \(b\).

3. Because \(\eta(\tau)\) is modular, the transforms \(\eta\left(\frac{\tau+r}{\ell}\right)\) are again modular forms of weight \(1/2\) (on congruence subgroups), and appropriate linear combinations become honest modular forms (or eta‑quotients) of integer weight on \(\Gamma_0(\ell)\). [math.ucla](https://www.math.ucla.edu/~wdduke/preprints/ramanujan.pdf)

For \(\ell=5,7,11\), there is a small-dimensional space of weight-\(k\) modular forms on \(\Gamma_0(\ell)\), which allows explicit identification of the resulting function.

***

## 3. Construct the key eta‑quotients \(P_\ell(q)\)

The “Ramanujan–Serre–Zagier” style proof packages these dissections into clean eta‑quotient identities. For each \(\ell\in\{5,7,11\}\), one shows that

\[
P_\ell(q) := \sum_{n\ge 0} p(\ell n + a_\ell) q^n
\]

is an eta-quotient modular form on \(\Gamma_0(\ell)\) with a very specific shape. Concretely, Ramanujan obtained identities such as [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586220/)

\[
P_5(q) = \sum_{n\ge 0} p(5n+4) q^n =
5\, \frac{(q^5;q^5)_\infty^5}{(q;q)_\infty^6},
\]

\[
P_7(q) = \sum_{n\ge 0} p(7n+5) q^n =
7\,\frac{(q^7;q^7)_\infty^3}{(q;q)_\infty^4}
+49q\,\frac{(q^7;q^7)_\infty^7}{(q;q)_\infty^8},
\]

and an analogous (more complicated) formula for \(\ell=11\). [en.wikipedia](https://en.wikipedia.org/wiki/Ramanujan's_congruences)

Conceptually:

- The left side is “take the generating function and project onto one residue class”.  
- The right side is an eta‑quotient of positive weight on \(\Gamma_0(\ell)\), pinned down by:  
  - the weight,  
  - the order of vanishing at each cusp,  
  - a few initial Fourier coefficients (dimension argument). [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)

Zagier‑style proofs use that the space \(M_k(\Gamma_0(\ell))\) is spanned by a handful of eta‑products, so you only need to compute a finite number of coefficients to identify the form uniquely. [math.harvard](https://www.math.harvard.edu/media/Narayanan-Modular-Forms-Thesis.pdf)

***

## 4. Deduce divisibility from the form of the identity

Once you have the eta‑quotient expression, the congruence is immediate. E.g. for \(\ell=5\),

\[
\sum_{n\ge 0} p(5n+4) q^n =
5\,\frac{(q^5;q^5)_\infty^5}{(q;q)_\infty^6}.
\]

The right-hand side has all Fourier coefficients in \(5\mathbb Z\), because there is a global multiplicative factor 5 and the remaining series has integer coefficients.  Thus every coefficient of the left-hand side, i.e. every \(p(5n+4)\), is divisible by 5. [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586220/)

Similarly, for \(\ell=7\) the right-hand side is a sum of two terms, with prefactors \(7\) and \(49\); the product pieces again have integer coefficients, so all coefficients are multiples of 7. [en.wikipedia](https://en.wikipedia.org/wiki/Ramanujan's_congruences)

The mod 11 identity has an overall factor 11 (or is a sum where each term has such a factor), implying \(p(11n+6)\equiv 0\pmod{11}\) in the same way. [en.wikipedia](https://en.wikipedia.org/wiki/Ramanujan's_congruences)

So the analytic/modular-form content is all in step 3; the congruence is a one-line corollary once those identities are in place.

***

## 5. A more structural modular-forms view (Serre/Ono/Ahlgren–Boylan)

There is also a slightly more conceptual modular-forms explanation of *why only* these congruences appear:

- Reinterpret \(F(\tau)=\eta(\tau)^{-1}\) as a modular form of half-integral weight with \(p(n)\) as its Fourier coefficients.  
- Use congruence theory of modular forms: modulo a prime \(\ell\), modular forms form a finite-dimensional vector space over \(\mathbb F_\ell\), and the operators \(\Theta=q\frac{d}{dq}\), Hecke operators, etc., constrain when a sequence of coefficients can vanish in an arithmetic progression. [arxiv](https://arxiv.org/pdf/1601.05287.pdf)
- Kiming–Olsson, Ahlgren–Boylan and others prove that if \(p(\ell n + b)\equiv 0\pmod{\ell}\) for all \(n\), then the progression parameters must satisfy \(24b\equiv 1 \pmod{\ell}\); and for the partition function, only \(\ell=5,7,11\) actually occur. [cambridge](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E12C94E0FE4635F84D825932F94293EE/S0008414X00007008a.pdf/div-class-title-non-existence-of-ramanujan-congruences-in-modular-forms-of-level-four-div.pdf)

This elevates Ramanujan’s three congruences to a uniqueness theorem within the modular-forms framework.

***

From here, the “in-depth” part, if you want, is to actually walk through one case (say mod 5) and derive the 5-dissection of \(\eta(\tau)^{-1}\), then match it to the eta‑quotient \(5(q^5;q^5)_\infty^5/(q;q)_\infty^6\) using dimension of \(M_k(\Gamma_0(5))\) and cusp behavior.

What would you like to focus on next: the explicit 5-dissection/eta-product calculation for the mod 5 case, or the abstract modular-forms congruence machinery (Θ‑operator, filtration, etc.) that explains why these are the only prime-mod congruences?

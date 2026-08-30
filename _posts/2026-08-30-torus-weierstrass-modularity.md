---
title: "The Torus Reveal: Why the Chord-and-Tangent Trick Is Just Addition in Disguise"
date: 2026-08-30
categories:
  - Elliptic Curves
  - Mathematics
tags:
  - elliptic-functions
  - weierstrass-p
  - complex-tori
  - modular-forms
  - modularity-theorem
share: true
read_time: true
excerpt: "The torus C/Λ explains the chord-and-tangent law, ℘ is a nonlinear cosine, and modularity turns point counts into modular forms. Part 5 of the five-part elliptic curves series."
---

**Challenge to the reader:** Verify that $\cos$ "parametrizes the circle" — check $\cos^2 z+\sin^2 z=1$ and the linear ODE $\cos''=-\cos$ — then state the two facts about Weierstrass's $\wp$ that are the exact nonlinear analogues. (The answers are in §2.)

*Part 5 of five in the series **Elliptic Curves & Elliptic Functions**: [Part 1 — The Circle, the Ellipse, and the Birth of a New Trigonometry]({% post_url 2026-08-30-ellipse-secret-elliptic-integrals %}) · [Part 2 — How to Add Points on a Curve]({% post_url 2026-08-30-chord-and-tangent-group-law %}) · [Part 3 — Counting Points, Keeping Secrets]({% post_url 2026-08-30-point-counting-hasse-cryptography %}) · [Part 4 — Rational Points and the Rank]({% post_url 2026-08-30-mordell-weil-rank-rational-points %}) · [Part 5 — The Torus, the $\wp$-Function, and Modularity]({% post_url 2026-08-30-torus-weierstrass-modularity %}) (this page). One figure — the two-panel derivation of the addition and doubling formulas — is reused throughout the series as a visual anchor.*

## The core theorem

As a complex manifold, $y^2=\phi(x)$ (with $\phi$ cubic) is a torus $\mathbb C/\Lambda$; the chord-and-tangent group law of Part 2 is literally addition on that torus; and the numbers $a_p$ of Part 3 are Fourier coefficients of a modular form — the **modularity theorem**, the chain of ideas that led to Fermat's Last Theorem. Everything in the series connects here.

**Why it matters.** This part replaces "the figure looks like it works" with a reason: chords and tangents are shadows of linear algebra on a lattice. The same mechanism explains why one pair of formulas computes correctly over $\mathbb Q$, $\mathbb F_p$, and $\mathbb C$ — and why counting points mod $p$ encodes the rank of the rational points.

---

## 1. From integrals to the torus

Return to $y^2=\phi(x)$ with $\phi$ cubic. As a complex manifold this curve is a torus $\mathbb C/\Lambda$, $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$, where the periods $\omega_1,\omega_2$ are the integrals $\int dx/y$ over the two independent homology cycles — the two periods glimpsed in Part 1. A meromorphic function periodic with respect to a rank-2 lattice is, by definition, an **elliptic function**; Jacobi's $\mathrm{sn},\mathrm{cn},\mathrm{dn}$ and Weierstrass's $\wp$ are two coordinate systems on the same object. [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)

## 2. Weierstrass's $\wp$: nonlinear cosine

Weierstrass built the basic elliptic function for a lattice $\Lambda$:
$$\wp(z)=\frac{1}{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\left(\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}\right),$$
doubly periodic, even, with a double pole at each lattice point, satisfying
$$(\wp'(z))^2=4\wp(z)^3-g_2\,\wp(z)-g_3 .$$
Hence $(x,y)=(\wp(z),\wp'(z))$ parametrizes the curve $y^2=4x^3-g_2x-g_3$. The analogy is precise: $\cos z$ parametrizes the circle and satisfies the *linear* ODE $\cos''=-\cos$; $\wp$ parametrizes an elliptic curve and satisfies a *nonlinear* ODE cubic in $\wp$. Elliptic functions are "nonlinear trigonometric functions," adapted to tori instead of circles. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_function)

**Challenge:** Show directly from the defining series that $\wp$ is even: compare the summands for $\omega$ and $-\omega$.

## 3. Why the figure works

Here is the payoff for Part 2's diagram. On the torus, addition is ordinary addition in $\mathbb C/\Lambda$; under $(\wp,\wp')$ this projects to exactly the chord-and-tangent law of the figure — three points $(\wp(z_i),\wp'(z_i))$ are collinear if and only if $z_1+z_2+z_3=0$ in $\mathbb C/\Lambda$. The secant, the tangent, and the reflection across the $x$-axis are shadows of linear algebra on the lattice. That is why the same formulas computed correctly over $\mathbb Q$, over $\mathbb F_5$, and over $\mathbb C$.

![The chord-and-tangent law, now revealed as the shadow of addition on the torus](/elliptic.jpeg)

> **Figure (series anchor).** The final reading of the anchor figure. *Left panel:* the secant through $P$ and $Q$ meets the curve in $R'$; reflecting gives $P+Q$. *Right panel:* the tangent at $P$ meets the curve in $R'$; reflecting gives $2P$. On the torus $\mathbb C/\Lambda$ this is ordinary addition: the collinearity condition is exactly $z_1+z_2+z_3=0$ mod $\Lambda$, and the reflection is the change $z\mapsto -z$. The same two formulas therefore compute correctly over every field — the geometry of chords and tangents *is* the algebra of the lattice.

**Challenge:** Explain why $z\mapsto -z$ on the torus is the $x$-axis reflection under $(\wp,\wp')$ — use that $\wp$ is even and $\wp'$ is odd.

## 4. Modularity

Over $\mathbb C$, the lattice's $j$-invariant is a modular function of the lattice parameter $\tau$, so elliptic curves are parametrized by modular curves (quotients of the upper half-plane by subgroups of $\mathrm{SL}_2(\mathbb Z)$). [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf) Over $\mathbb Q$, the numbers $a_p$ of Part 3 assemble into the $L$-function
$$L(E,s)=\prod_p\left(1-a_p p^{-s}+p^{1-2s}\right)^{-1},$$
and the **modularity theorem** asserts that $L(E,s)$ is the $L$-function of a weight-2 modular form whose Fourier coefficients are exactly the $a_p$ — the chain of ideas that led to Fermat's Last Theorem. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve) Counting points mod $p$ is thus not bookkeeping; it builds a global analytic object encoding the rank and torsion of Part 4.

## 5. Coda

Elliptic curves are the cleanest bridge between number theory and geometry; partitions provide another, more combinatorial one, where modular forms of higher weight and level encode partition numbers instead of $a_p$, and Hecke operators capture the prime-by-prime structure. [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf) And the series closes its circle: the ellipse's arc length (Part 1) forced us to elliptic integrals; their inversion gave doubly periodic functions on a torus (this part); the torus is an elliptic curve, whose points add by chords and tangents (Part 2); counting those points mod $p$ feeds cryptography (Part 3) and, through modularity, the deepest arithmetic of rational points (Part 4). One figure, two formulas, and a torus — that is the whole story.

---

## 6. The connection table: circle versus torus

| | Trigonometric (circle) | Elliptic (torus) |
|---|---|---|
| Parametrization | $(\cos,\sin)$ maps $\mathbb R$ onto $x^2+y^2=1$ | $(\wp,\wp')$ maps $\mathbb C/\Lambda$ onto $y^2=4x^3-g_2x-g_3$ |
| Governing ODE | Linear: $\cos''=-\cos$ | Cubic: $(\wp')^2=4\wp^3-g_2\wp-g_3$ |
| Periods | One: $2\pi$ | Two: lattice $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$ |
| Group law | Addition in $\mathbb R/2\pi\mathbb Z$ | Addition in $\mathbb C/\Lambda$ = chord-and-tangent |
| Inverse construction | $\arcsin$ integral | Elliptic integral of the first kind |

## 7. Appendix — Thirty examples of elliptic functions

An elliptic function is a meromorphic function that is doubly periodic. Standard examples include $\wp(z)$, its derivative $\wp'(z)$, and rational combinations of the Jacobi functions $\operatorname{sn}(z,k)$, $\operatorname{cn}(z,k)$, $\operatorname{dn}(z,k)$ — sums, products, and quotients of elliptic functions are elliptic whenever they remain meromorphic. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_function)

**Weierstrass examples.** Fix a lattice $\Lambda\subset\mathbb{C}$ and let $\wp(z)=\wp(z;\Lambda)$. The derivative $\wp'(z)$ is elliptic with the same lattice, and any rational function of $\wp(z)$ and $\wp'(z)$ is again elliptic:

1. $\wp(z)$
2. $\wp'(z)$
3. $\wp(z)^2$
4. $\wp(z)^3$
5. $\dfrac{1}{\wp(z)-a}$, where $a$ is a constant not making the function identically singular
6. $\dfrac{\wp'(z)}{\wp(z)-a}$
7. $\dfrac{\wp'(z)^2}{\wp(z)-a}$
8. $\wp(z)+\wp'(z)$
9. $\dfrac{\wp(z)^2+1}{\wp'(z)}$
10. $\dfrac{\wp'(z)^2+\wp(z)}{\wp(z)^2-1}$

**Jacobi examples.** Fix a modulus $k$. The classical secondary Jacobi functions are formed by taking reciprocals and quotients of the three basic ones $\operatorname{sn},\operatorname{cn},\operatorname{dn}$: [en.wikipedia](https://en.wikipedia.org/wiki/Jacobi_elliptic_functions)

11. $\operatorname{sn}(z,k)$
12. $\operatorname{cn}(z,k)$
13. $\operatorname{dn}(z,k)$
14. $\operatorname{ns}(z,k)=1/\operatorname{sn}(z,k)$
15. $\operatorname{nc}(z,k)=1/\operatorname{cn}(z,k)$
16. $\operatorname{nd}(z,k)=1/\operatorname{dn}(z,k)$
17. $\operatorname{sc}(z,k)=\operatorname{sn}(z,k)/\operatorname{cn}(z,k)$
18. $\operatorname{sd}(z,k)=\operatorname{sn}(z,k)/\operatorname{dn}(z,k)$
19. $\operatorname{cd}(z,k)=\operatorname{cn}(z,k)/\operatorname{dn}(z,k)$
20. $\operatorname{cs}(z,k)=\operatorname{cn}(z,k)/\operatorname{sn}(z,k)$
21. $\operatorname{ds}(z,k)=\operatorname{dn}(z,k)/\operatorname{sn}(z,k)$
22. $\operatorname{dc}(z,k)=\operatorname{dn}(z,k)/\operatorname{cn}(z,k)$

**More constructed examples:**

23. $\operatorname{sn}(z,k)^2$
24. $\operatorname{cn}(z,k)^2$
25. $\operatorname{dn}(z,k)^2$
26. $\operatorname{sn}(z,k)\operatorname{cn}(z,k)$
27. $\operatorname{sn}(z,k)\operatorname{dn}(z,k)$
28. $\operatorname{cn}(z,k)\operatorname{dn}(z,k)$
29. $\dfrac{\operatorname{sn}(z,k)^2}{\operatorname{dn}(z,k)}$
30. $\dfrac{\operatorname{cn}(z,k)+\operatorname{dn}(z,k)}{\operatorname{sn}(z,k)}$

To be fully rigorous as a list of elliptic functions, it is understood that we choose parameters so denominators do not vanish identically; isolated poles are allowed because elliptic functions are meromorphic, not necessarily entire. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_function)

## 8. Elliptic curves and partitions: two bridges to modular forms

Elliptic curves, modular forms, and number theory are tightly coupled:

- Each elliptic curve over $\mathbb C$ is analytically isomorphic to a complex torus $\mathbb C/\Lambda$ built from a lattice $\Lambda$. [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)
- The invariants of $\Lambda$ (like its $j$-invariant) are modular functions of the lattice parameter $\tau$; thus elliptic curves are parameterized by modular curves (quotients of the upper half-plane by subgroups of $\mathrm{SL}_2(\mathbb Z)$). [math.u-bordeaux](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/slides/2011-03-Bordeaux.pdf)
- For elliptic curves over $\mathbb Q$, the $L$-function $L(E,s)$ is the same as the $L$-function of a weight-2 modular form; this is the modularity theorem. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve)
- Partitions provide a second, more combinatorial context: modular forms of higher weight and level encode partition numbers instead of the $a_p$, and Hecke operators play the role of capturing the prime-by-prime structure.

So elliptic curves provide one of the "simplest" contexts where modular forms and number theory interact; partitions are another, more combinatorially flavored one.

---

## Deeper significance

The series' opening question — what does ellipse arc length have to do with anything? — has by now acquired a complete answer: the ellipse's arc length forced elliptic integrals (Part 1); inverting them gave doubly periodic functions on a torus (this part); the torus is an elliptic curve, whose points add by chords and tangents (Part 2); counting those points mod $p$ fed cryptography (Part 3) and, through modularity, the deepest arithmetic of rational points (Part 4). One figure, two formulas, and a torus.

---

**Final challenge:** Assemble the full chain in one paragraph: starting from $L(E,s)=\prod_p(1-a_p p^{-s}+p^{1-2s})^{-1}$, explain how the $a_p$ of Part 3 "know" the rank of Part 4 — naming the two statements (modularity theorem; Birch–Swinnerton-Dyer) that make the chain rigorous.

*References for the curious reader: Wikipedia articles on elliptic curves and elliptic functions; E. Dummit's notes on elliptic curves (Northeastern); the LMFDB database; SageMath documentation on elliptic curves; introductory handouts on elliptic functions (HSE, Leiden, Harvard, UCSB).*

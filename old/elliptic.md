
# ELLIPTIC CURVES & ELLIPTIC FUNCTIONS
### A five‑part series for the curious reader — from the arc length of an ellipse to modularity

*Editor's note: This series grew out of a set of lecture notes on elliptic integrals, elliptic functions, the arithmetic of elliptic curves, and their number‑theoretic applications. The parts are ordered by difficulty: Parts 1–2 require only calculus, Parts 3–4 some algebra, Part 5 complex analysis. One figure — the two‑panel derivation of the addition and doubling formulas — is reused throughout the series as a visual anchor.*

---

## PART 1 — The Circle, the Ellipse, and the Birth of a New Trigonometry
*Level: gentle. The question: where do elliptic functions come from?*

**1. The circle and its functions.** Start with the unit circle $x^2+y^2=1$. It is parametrized by angle:
$$x=\cos t,\qquad y=\sin t,$$
and these functions are periodic with one fundamental period $2\pi$. Because the circle is perfectly symmetric, arc length from angle $0$ to $t$ is simply proportional to $t$: "angle" and "arc length" are the same variable up to scaling. This is why trigonometry is elementary. Equivalently, the angle $t$ recovered from the height $x=\sin t$ is an integral, $t=\int_0^x \frac{du}{\sqrt{1-u^2}}$, and *sine is the inverse of that integral*.

**2. Now replace the circle by an ellipse** $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$. Try the same game — parametrize arc length $s$ by an angular parameter $\phi$ — and you immediately hit
$$s(\phi)=\int_0^{\phi}\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}\,d\theta .$$
These are **elliptic integrals** — the reason for the name is exactly this geometric origin — and they cannot be expressed in elementary functions. The moral: for circles the natural parametrization leads to elementary functions; for ellipses it forces you into a new class of integrals.

**3. What counts as an elliptic integral?** In general, integrals of the shape
$$z(u)=\int_{x_0}^{u} R\big(x,\sqrt{\phi(x)}\big)\,dx,$$
with $R$ rational and $\phi$ a cubic or quartic polynomial. A canonical example (Legendre's form) is the incomplete elliptic integral of the first kind,
$$F(\phi,k)=\int_0^{\phi}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}}.$$

**4. The Abel–Jacobi idea: invert them.** Sine was born by inverting an arc‑length integral on the circle; Abel and Jacobi did the same for the ellipse. Write $z=F(\phi,k)$ and, instead of expressing $z$ in terms of $\phi$, solve for $\phi$ as a function of $z$: the **Jacobi amplitude** $\phi=\operatorname{am}(z;k)$. Then define
$$\mathrm{sn}(z;k)=\sin(\operatorname{am}(z;k)),\qquad \mathrm{cn}(z;k)=\cos(\operatorname{am}(z;k)),\ \dots$$
the **Jacobi elliptic functions**. Elliptic functions are thus the inverses of elliptic integrals, exactly as sine is the inverse of the circle's arc‑length integral.

**5. Physical interlude: the pendulum.** The same functions emerge from physics. The full, non‑small‑angle pendulum satisfies the nonlinear equation $\theta''(t)+\frac{g}{\ell}\sin\theta(t)=0$. Energy conservation gives $\theta'(t)^2=2\frac{g}{\ell}\big(\cos\theta(t)-\cos\theta_0\big)$, and after a substitution this becomes
$$\left(\frac{d\phi}{dt}\right)^2=(1-\phi^2)(1-k^2\phi^2).$$
Integrating gives an elliptic integral; inverting yields $\phi(t)=\mathrm{sn}(t;k)$. Linear systems give sines and cosines; *nonlinear but integrable* systems give elliptic functions — the same story appears in the Euler top, the shape of a rotating string, and certain soliton equations.

**6. A first glimpse of the torus.** Here is the subtle point we will unpack in Part 5: because of the square root of a cubic or quartic, the integral really lives on a two‑sheeted surface which, once compactified, is a **torus**. Integrating over its two independent cycles produces *two* independent periods. So the inverted functions are periodic with respect to a rank‑2 lattice — "doubly periodic" — while sine and cosine have only one period. Intuitively: **trigonometric functions live on the circle (one cycle); elliptic functions live on the torus (two cycles).**

And the curve $y^2=\text{cubic}$ hiding inside those integrals is precisely an *elliptic curve* — the protagonist of the rest of this series.

---

## PART 2 — How to Add Points on a Curve: The Chord‑and‑Tangent Method
*Level: elementary. The figure makes its first appearance.*

**1. The curve.** Over a field, an elliptic curve is given (after a change of variables) by
$$E:\ y^2=x^3+ax+b,$$
with the discriminant condition $\Delta=-16(4a^3+27b^2)\neq 0$, which guarantees no cusps or self‑intersections. A concrete example: $E: y^2=x^3-x$, where $4(-1)^3+27\cdot 0=-4\neq0$.

**2. The surprise.** The points of $E$, together with a point at infinity $\mathcal O$, form an **abelian group**, and the addition law is geometric — the *chord‑and‑tangent method* depicted in the figure accompanying this series:

> **Figure.** *Left panel (addition, $P\neq Q$):* the secant through $P=(x_1,y_1)$ and $Q=(x_2,y_2)$ meets the curve in a third point $R'=(x_3,y_3')$; reflecting across the $x$‑axis gives $P+Q=R$. *Right panel (doubling, $P=Q$, $y_1\neq0$):* the tangent at $P$ meets the curve again in $R'$; reflecting gives $2P=R$.

**3. Addition, following the left panel.** The secant slope is $m=\frac{y_2-y_1}{x_2-x_1}$; the line is $y=m(x-x_1)+y_1$. Substituting into $y^2=x^3+ax+b$ and collecting terms yields a monic cubic in $x$ whose $x^2$‑coefficient is $-m^2$, having exactly $x_1,x_2,x_3$ as roots. Vieta's formula (sum of roots $=-c_2$) gives
$$x_1+x_2+x_3=m^2\ \Longrightarrow\ x_3=m^2-x_1-x_2 .$$
The third intersection has $y_3'=m(x_3-x_1)+y_1$; reflecting across the $x$‑axis:
$$y_3=-y_3'=m(x_1-x_3)-y_1 .$$
(If $x_1=x_2$ with $y_1=-y_2$, the chord is vertical and $P+Q=\mathcal O$.)

**4. Doubling, following the right panel.** Now the line is the tangent. Implicit differentiation of $y^2=x^3+ax+b$ gives $2y\,\frac{dy}{dx}=3x^2+a$, hence
$$m=\left.\frac{dy}{dx}\right|_{P}=\frac{3x_1^2+a}{2y_1}.$$
The tangency means $x_1$ is a *double* root, so Vieta reads $x_1+x_1+x_3=m^2$, i.e. $x_3=m^2-2x_1$, with the same reflection $y_3=m(x_1-x_3)-y_1$.

**5. Summary table** (the boxed formulas at the bottom of the figure):

| Operation | Slope $m$ | Output $(x_3,y_3)$ |
|---|---|---|
| Addition $P\neq Q$ | $\frac{y_2-y_1}{x_2-x_1}$ | $x_3=m^2-x_1-x_2$, $\ y_3=m(x_1-x_3)-y_1$ |
| Doubling $P=Q$ | $\frac{3x_1^2+a}{2y_1}$ | $x_3=m^2-2x_1$, $\ y_3=m(x_1-x_3)-y_1$ |

**6. A worked example over $\mathbb Q$.** On $E:y^2=x^3-x$, take $P=(0,0)$ (indeed $0^2=0^3-0$). The doubling slope would be $\frac{3\cdot0-1}{2\cdot0}=\frac{-1}{0}$, undefined: the tangent at $P$ is vertical, the "third intersection" is $\mathcal O$, and $2P=\mathcal O$. So $P$ has **order 2** — and the same holds for $(\pm1,0)$. This is already number theory: we are making group‑theoretic statements about *rational solutions of a cubic*.

**7. The same figure over a finite field.** Nothing in the figure's algebra required real numbers. Reduce $E:y^2=x^3+4x+4$ modulo $5$, and take $P_1=(1,3)$, $P_2=(0,2)$. Left panel, step by step, in $\mathbb F_5$:
$$m=\frac{2-3}{0-1}=\frac{-1}{-1}=1,\quad x_3=1-1-0=0,\quad y_3=1\cdot(1-0)-3=-2\equiv 3 .$$
So $P_1+P_2=(0,3)$ in $E(\mathbb F_5)$. The picture of chords and reflections was drawn over $\mathbb R$, but the *formulas* are field‑independent — a fact we exploit in Part 3, and whose deepest explanation arrives only in Part 5.

---

## PART 3 — Counting Points, Keeping Secrets: Elliptic Curves mod $p$
*Level: intermediate. The figure's formulas, now as pure modular arithmetic.*

**1. Counting points and Hasse's bound.** For each prime $p$, reduce the coefficients of $E$ mod $p$ and count solutions. Write
$$a_p=p+1-\#E(\mathbb F_p).$$
**Hasse's theorem** says $|a_p|\le 2\sqrt p$ — the count is always close to $p+1$.

Let us verify this on our toy curve $E:y^2=x^3+4x+4$ over $\mathbb F_5$. Checking each $x$: $x=0,1,4$ give $x^3+4x+4\equiv 4,4,4$ (a square, two points each); $x=2$ gives $0$ (one point); $x=3$ gives $3$ (a non‑square). Hence the affine points $(0,2),(0,3),(1,2),(1,3),(2,0),(4,2),(4,3)$ plus $\mathcal O$: $\#E(\mathbb F_5)=8$, so
$$a_5=5+1-8=-2,\qquad |a_5|=2\le 2\sqrt5\approx4.47 .$$
The sequence $(a_p)$, as $p$ varies, is far more than bookkeeping: it is the raw material from which the $L$‑function of $E$ is built (Part 5).

**2. The figure as modular arithmetic.** $E(\mathbb F_p)$ is a finite abelian group, and the figure's formulas compute in it. On our toy curve, $P=(1,3)$ has **order 4**: the right panel gives $2P=(2,0)$ (slope $m=\frac{3+4}{6}\equiv\frac{2}{1}=2$, $x_3=4-2=2$, $y_3=2(1-2)-3\equiv0$); the left panel then gives $3P=2P+P=(1,2)$; and doubling $(2,0)$ hits the vertical‑tangent case, $4P=\mathcal O$. The subgroup $\{\mathcal O,P,2P,3P\}$ has four elements.

**3. Cryptography.** If instead of $p=5$ we take a huge prime and a point $P$ of large prime order $n$, the map $k\mapsto kP$ (repeated use of the figure's two formulas) is easy, while inverting it — given $P$ and $Q=kP$, find $k$, the **elliptic curve discrete logarithm problem** — is believed hard. This is elliptic curve cryptography (ECC). Number theory enters twice: one must ensure $\#E(\mathbb F_p)$ has a large prime factor (Hasse tells you what size to expect), and computing $\#E(\mathbb F_p)$ for large $p$ is done by the **Schoof–Elkies–Atkin** algorithm, whose machinery — modular polynomials, isogenies — links point counting to modular forms, previewing Part 5.

Our toy curve is hopelessly insecure; its purpose is to show the entire cryptographic edifice resting on two short formulas and one figure.

---

## PART 4 — Rational Points and the Rank: The Mordell–Weil Theorem
*Level: intermediate–advanced. From finite groups back to infinite ones.*

**1. Mordell's theorem.** Over $\mathbb Q$ the group $E(\mathbb Q)$ of rational points is finitely generated:
$$E(\mathbb Q)\cong E(\mathbb Q)_{\mathrm{tors}}\oplus\mathbb Z^{\,r},$$
where $r$ is the **rank**. The torsion part we met in Part 2 — the order‑2 points $(0,0),(\pm1,0)$ of $y^2=x^3-x$. The rank is the deeper invariant: $r>0$ means *infinitely many rational solutions* of the cubic. For instance on $y^2=x^3-x+1$ the point $P=(0,1)$ has infinite order (its double $2P=(\tfrac14,-\tfrac78)$ is non‑integral, impossible for torsion), and the multiples $nP$ generate infinitely many distinct rational solutions. Diophantinely, "find all solutions of this cubic" has been upgraded to "understand a finitely generated abelian group" — exactly how elliptic curves enter classical problems such as integer points on $y^2=x^3-2$ or the **congruent number problem**.

**2. Finding curves of a given rank.** The reliable route is a verified database. The LMFDB filters curves over $\mathbb Q$ by rank, conductor, torsion, and CM status; useful small examples:

| Rank | Label | Weierstrass model |
|---|---|---|
| 0 | 11a1 | $y^2+y=x^3-x^2-10x-20$ |
| 1 | 37a1 | $y^2+y=x^3-x$ |
| 2 | 389a1 | $y^2+y=x^3+x^2-2x$ |

SageMath ships curated tables and full tooling:

```python
elliptic_curves.rank(rank=1, n=5)            # five rank-1 curves
elliptic_curves.rank(rank=3, tors=2, n=5, labels=True)
E = EllipticCurve("389a1")
E.rank()                 # rigorous Mordell–Weil rank when it succeeds
E.gens(proof=True)       # generators modulo torsion
E.torsion_subgroup()
E.analytic_rank()        # numerical L-function computation; not a proof
E.selmer_rank(2)         # upper-bound information
```

**3. What proving a rank entails.** To prove $r=k$ you need *both* directions: $k$ **independent** rational points ($r\ge k$), and a matching upper bound ($r\le k$) from a 2‑, 3‑, or higher **descent / Selmer computation**. Merely exhibiting many points proves nothing — they may be dependent, or generate a finite‑index subgroup. The analytic rank guides searches, but its equality with the algebraic rank is conjectural (Birch–Swinnerton‑Dyer); unconditional results need certified generators plus rigorous bounds.

**4. Searching by hand — a caution.** One can enumerate short models $E_{A,B}:y^2=x^3+Ax+B$ in a coefficient box:

```python
for A in range(-100,101):
    for B in range(-100,101):
        if 4*A**3+27*B**2 == 0: continue
        E = EllipticCurve([0,0,0,A,B])
        try:
            if E.rank(proof=True) == 3: print(E.ainvs(), E.gens(proof=True))
        except RuntimeError: pass
```

Fine for ranks 1–3 (start from 37a1, 389a1, or Sage's rank‑3 tables); hopeless as a strategy for high rank, which grows increasingly sparse and demands engineered elliptic surfaces with independent sections.

The mystery left hanging: what do the counts $a_p$ of Part 3 have to do with the rational points of this part? That bridge is the deepest result in the story.

---

## PART 5 — The Torus, the $\wp$‑Function, and Modularity: The Grand Synthesis
*Level: advanced. Everything connects: Part 1's integrals, Part 2's figure, Parts 3–4's arithmetic.*

**1. From integrals to the torus.** Return to $y^2=\phi(x)$ with $\phi$ cubic. As a complex manifold this curve is a torus $\mathbb C/\Lambda$, $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$, where the periods $\omega_1,\omega_2$ are the integrals $\int dx/y$ over the two independent homology cycles — the two periods glimpsed in Part 1. A meromorphic function periodic with respect to a rank‑2 lattice is, by definition, an **elliptic function**; Jacobi's $\mathrm{sn},\mathrm{cn},\mathrm{dn}$ and Weierstrass's $\wp$ are two coordinate systems on the same object.

**2. Weierstrass's $\wp$: nonlinear cosine.** Weierstrass built the basic elliptic function for a lattice $\Lambda$:
$$\wp(z)=\frac{1}{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\left(\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}\right),$$
doubly periodic, even, with a double pole at each lattice point, satisfying
$$(\wp'(z))^2=4\wp(z)^3-g_2\,\wp(z)-g_3 .$$
Hence $(x,y)=(\wp(z),\wp'(z))$ parametrizes the curve $y^2=4x^3-g_2x-g_3$. The analogy is precise: $\cos z$ parametrizes the circle and satisfies the *linear* ODE $\cos''=-\cos$; $\wp$ parametrizes an elliptic curve and satisfies a *nonlinear* ODE cubic in $\wp$. Elliptic functions are "nonlinear trigonometric functions," adapted to tori instead of circles.

**3. Why the figure works.** Here is the payoff for Part 2's diagram. On the torus, addition is ordinary addition in $\mathbb C/\Lambda$; under $(\wp,\wp')$ this projects to exactly the chord‑and‑tangent law of the figure — three points $(\wp(z_i),\wp'(z_i))$ are collinear if and only if $z_1+z_2+z_3=0$ in $\mathbb C/\Lambda$. The secant, the tangent, and the reflection across the $x$‑axis are shadows of linear algebra on the lattice. That is why the same formulas computed correctly over $\mathbb Q$, over $\mathbb F_5$, and over $\mathbb C$.

**4. Modularity.** Over $\mathbb C$, the lattice's $j$‑invariant is a modular function of the lattice parameter $\tau$, so elliptic curves are parametrized by modular curves (quotients of the upper half‑plane by subgroups of $\mathrm{SL}_2(\mathbb Z)$). Over $\mathbb Q$, the numbers $a_p$ of Part 3 assemble into the $L$‑function
$$L(E,s)=\prod_p\left(1-a_p p^{-s}+p^{1-2s}\right)^{-1},$$
and the **modularity theorem** asserts that $L(E,s)$ is the $L$‑function of a weight‑2 modular form whose Fourier coefficients are exactly the $a_p$ — the chain of ideas that led to Fermat's Last Theorem. Counting points mod $p$ is thus not bookkeeping; it builds a global analytic object encoding the rank and torsion of Part 4.

**5. Coda.** Elliptic curves are the cleanest bridge between number theory and geometry; partitions provide another, more combinatorial one, where modular forms of higher weight and level encode partition numbers instead of $a_p$, and Hecke operators capture the prime‑by‑prime structure. And the series closes its circle: the ellipse's arc length (Part 1) forced us to elliptic integrals; their inversion gave doubly periodic functions on a torus (this part); the torus is an elliptic curve, whose points add by chords and tangents (Part 2); counting those points mod $p$ feeds cryptography (Part 3) and, through modularity, the deepest arithmetic of rational points (Part 4). One figure, two formulas, and a torus — that is the whole story.

---

*References for the curious reader: Wikipedia articles on elliptic curves and elliptic functions; E. Dummit's notes on elliptic curves (Northeastern); the LMFDB database; SageMath documentation on elliptic curves; introductory handouts on elliptic functions (HSE, Leiden, Harvard, UCSB).*

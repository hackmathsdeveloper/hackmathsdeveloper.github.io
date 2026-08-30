---
title: "The Ellipse's Secret: How Arc Length Birthed a New Trigonometry"
date: 2026-08-30
categories:
  - Elliptic Curves
  - Mathematics
tags:
  - elliptic-integrals
  - elliptic-functions
  - jacobi-elliptic-functions
  - arc-length
  - pendulum
share: true
read_time: true
excerpt: "Circle arc length gives sine; ellipse arc length gives elliptic integrals — and inverting them produces doubly periodic functions, a new 'nonlinear trigonometry.' Part 1 of the five-part elliptic curves series."
---

**Challenge to the reader:** Verify that $t=\int_0^x \frac{du}{\sqrt{1-u^2}}=\arcsin x$ by differentiating both sides, and show that at modulus $k=0$ Legendre's $F(\phi,k)$ reduces to plain arc length $\phi$.

*Part 1 of five in the series **Elliptic Curves & Elliptic Functions**: [Part 1 — The Circle, the Ellipse, and the Birth of a New Trigonometry]({% post_url 2026-08-30-ellipse-secret-elliptic-integrals %}) (this page) · [Part 2 — How to Add Points on a Curve]({% post_url 2026-08-30-chord-and-tangent-group-law %}) · [Part 3 — Counting Points, Keeping Secrets]({% post_url 2026-08-30-point-counting-hasse-cryptography %}) · [Part 4 — Rational Points and the Rank]({% post_url 2026-08-30-mordell-weil-rank-rational-points %}) · [Part 5 — The Torus, the $\wp$-Function, and Modularity]({% post_url 2026-08-30-torus-weierstrass-modularity %}). Parts 1–2 require only calculus, Parts 3–4 some algebra, Part 5 complex analysis.*

## The core idea

Sine is the *inverse of the circle's arc-length integral*:
$$t=\int_0^x \frac{du}{\sqrt{1-u^2}},\qquad x=\sin t.$$
Elliptic functions are the same construction run on an ellipse instead of a circle — and the price of that one swap is a whole new class of functions.

**Why it matters.** Every "impossible" integral of the shape $\int R\big(x,\sqrt{\phi(x)}\big)\,dx$ with $\phi$ cubic or quartic — arc lengths of ellipses, pendulum periods, rotating tops — hides a new kind of symmetry: *two* periods instead of one. This part sets up where those functions come from; the rest of the series follows them into number theory and cryptography.

---

## 1. The circle and its functions

Start with the unit circle $x^2+y^2=1$. It is parametrized by angle:
$$x=\cos t,\qquad y=\sin t,$$
and these functions are periodic with one fundamental period $2\pi$. Because the circle is perfectly symmetric, arc length from angle $0$ to $t$ is simply proportional to $t$: "angle" and "arc length" are the same variable up to scaling. This is why trigonometry is elementary. Equivalently, the angle $t$ recovered from the height $x=\sin t$ is an integral, $t=\int_0^x \frac{du}{\sqrt{1-u^2}}$, and *sine is the inverse of that integral*.

## 2. Now replace the circle by an ellipse

Now replace the circle by the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$. Try the same game — parametrize arc length $s$ by an angular parameter $\phi$ — and you immediately hit
$$s(\phi)=\int_0^{\phi}\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}\,d\theta .$$
These are **elliptic integrals** — the reason for the name is exactly this geometric origin — and they cannot be expressed in elementary functions. The moral: for circles the natural parametrization leads to elementary functions; for ellipses it forces you into a new class of integrals.

## 3. What counts as an elliptic integral?

In general, integrals of the shape
$$z(u)=\int_{x_0}^{u} R\big(x,\sqrt{\phi(x)}\big)\,dx,$$
with $R$ rational and $\phi$ a cubic or quartic polynomial. A canonical example (Legendre's form) is the incomplete elliptic integral of the first kind,
$$F(\phi,k)=\int_0^{\phi}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}}.$$

**Challenge:** Show that at $k=0$ the Jacobi functions collapse to the classical ones: $\mathrm{sn}(z;0)=\sin z$ and $\mathrm{cn}(z;0)=\cos z$. (Hint: $F(\phi,0)=\phi$.)

## 4. The Abel–Jacobi idea: invert them

Sine was born by inverting an arc-length integral on the circle; Abel and Jacobi did the same for the ellipse. Write $z=F(\phi,k)$ and, instead of expressing $z$ in terms of $\phi$, solve for $\phi$ as a function of $z$: the **Jacobi amplitude** $\phi=\operatorname{am}(z;k)$. Then define
$$\mathrm{sn}(z;k)=\sin(\operatorname{am}(z;k)),\qquad \mathrm{cn}(z;k)=\cos(\operatorname{am}(z;k)),\ \dots$$
the **Jacobi elliptic functions**. Elliptic functions are thus the inverses of elliptic integrals, exactly as sine is the inverse of the circle's arc-length integral.

## 5. Physical interlude: the pendulum

The same functions emerge from physics. The full, non-small-angle pendulum satisfies the nonlinear equation $\theta''(t)+\frac{g}{\ell}\sin\theta(t)=0$. Energy conservation gives $\theta'(t)^2=2\frac{g}{\ell}\big(\cos\theta(t)-\cos\theta_0\big)$, and after a substitution this becomes
$$\left(\frac{d\phi}{dt}\right)^2=(1-\phi^2)(1-k^2\phi^2).$$
Integrating gives an elliptic integral; inverting yields $\phi(t)=\mathrm{sn}(t;k)$. Linear systems give sines and cosines; *nonlinear but integrable* systems give elliptic functions — the same story appears in the Euler top, the shape of a rotating string, and certain soliton equations.

**Challenge:** From the pendulum equation and energy conservation above, derive the $\left(\frac{d\phi}{dt}\right)^2=(1-\phi^2)(1-k^2\phi^2)$ form — naming your substitution. (Classic choice: $\sin(\theta/2)=k\sin\phi$ with $k=\sin(\theta_0/2)$, then scale time.)

## 6. A first glimpse of the torus

Here is the subtle point we unpack in Part 5: because of the square root of a cubic or quartic, the integral really lives on a two-sheeted surface which, once compactified, is a **torus**. Integrating over its two independent cycles produces *two* independent periods. So the inverted functions are periodic with respect to a rank-2 lattice — "doubly periodic" — while sine and cosine have only one period. Intuitively: **trigonometric functions live on the circle (one cycle); elliptic functions live on the torus (two cycles).**

**Challenge:** Explain in one sentence why the two independent cycles on the torus force two independent periods — and why the circle has only one.

And the curve $y^2=\text{cubic}$ hiding inside those integrals is precisely an *elliptic curve* — the protagonist of the rest of this series.

![The two-panel derivation of the chord-and-tangent addition and doubling formulas — the series' visual anchor](/elliptic.jpeg)

> **Figure (series anchor).** *Left panel (addition, $P\neq Q$):* the secant through $P=(x_1,y_1)$ and $Q=(x_2,y_2)$ meets the curve in a third point $R'=(x_3,y_3')$; reflecting across the $x$-axis gives $P+Q=R$. *Right panel (doubling, $P=Q$, $y_1\neq0$):* the tangent at $P$ meets the curve again in $R'$; reflecting gives $2P=R$. The figure is dissected panel by panel in [Part 2]({% post_url 2026-08-30-chord-and-tangent-group-law %}); here it already hints at the destination: an elliptic curve, a group law, and a torus.

---

## 7. Why the ordering circle → ellipse → elliptic functions is natural

A good introduction presents elliptic functions and elliptic integrals as the **next natural step** after elementary functions and elementary integrals: first come rational functions and logarithms, then trigonometric functions and inverse trigonometric integrals, and then elliptic integrals and their inverses. [matematicas.uam](http://matematicas.uam.es/~fernando.chamizo/asignaturas/2425cryptography/lectures/lecture04.pdf)

- Start from familiar examples such as $\int \frac{dx}{1+x^2}=\arctan x$ and $\int \frac{dx}{\sqrt{1-x^2}}=\arcsin x$, where the integral introduces a new inverse function of great usefulness. This lets one see the pattern: when integration produces something not obviously algebraic, the answer may still define an important new class of functions. [jstor](https://www.jstor.org/stable/pdf/1967677.pdf)
- Contrast polynomial square roots by degree: when the polynomial under the square root has degree 1 or 2, substitutions often reduce the integral to elementary form, but when the degree is 3 or 4, one reaches elliptic integrals. Elliptic integrals arise not as exotic inventions but as the natural endpoint of trying to integrate slightly more complicated algebraic expressions. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_integral)
- The historical geometric example is the **arc length of an ellipse**, which leads to an integral that cannot in general be expressed by elementary functions. This is why they are called elliptic integrals: the name comes from the ellipse, even though the resulting theory reaches far beyond that single curve. [math.hse](https://math.hse.ru/data/2020/02/19/1575196181/introduction.pdf)
- A very effective classroom transition: **circle arc length leads to trigonometric functions, while ellipse arc length leads to elliptic integrals.** That comparison immediately explains both the limitation of elementary methods and the need for a broader function theory. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/HistTopics/Elliptic_functions/)

## 8. From integrals to functions — and why two periods appear

Just as $\sin$ and $\cos$ are tied to the inversion of inverse trigonometric integrals, elliptic functions arise as inverses of elliptic integrals. [math.hse](https://math.hse.ru/data/2020/02/19/1575196181/introduction.pdf) This is the point where the subject suddenly becomes more interesting than "just another hard integral," because the inverse functions have rich algebraic identities, differential equations, and periodic behavior. In particular, Jacobi's elliptic functions satisfy differential equations analogous to the trigonometric ones, but with an extra parameter (the modulus $k$) that captures more complicated geometry. [math.hse](https://math.hse.ru/data/2020/02/19/1575196181/introduction.pdf)

For ordinary trigonometric functions, periodicity reflects the geometry of the circle. For elliptic functions, inverting elliptic integrals in the complex domain produces meromorphic functions with **two independent periods**, which is why elliptic functions are defined as doubly periodic meromorphic functions on $\mathbb{C}$. [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_function) Elliptic functions are not merely "harder trig functions"; they encode the geometry of a torus or elliptic curve. In modern language, they connect analysis, geometry, algebraic curves, and eventually number theory. [math.hse](https://math.hse.ru/data/2020/02/19/1575196181/introduction.pdf)

## 9. The connection table: circle versus ellipse

| | Circle | Ellipse |
|---|---|---|
| Curve | $x^2+y^2=1$ | $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ |
| Arc-length integral | Elementary: $\arcsin x$ | Elliptic integral of the first kind |
| Inverted functions | $\sin,\cos$ — one period $2\pi$ | Jacobi $\mathrm{sn},\mathrm{cn},\mathrm{dn}$ — two periods |
| Geometry underneath | The circle: one cycle | The torus: two cycles |
| Governing ODE | Linear: $\cos''=-\cos$ | Nonlinear cubic (Part 5) |

---

## Deeper significance

The whole arc of this series is compressed into this table: replace a circle by an ellipse, and every layer of the theory — the integral, its inverse, the period structure, the geometry — upgrades one level. Elementary integration gives logarithms and inverse trigonometric functions; more complicated algebraic integrals, especially with square roots of cubic or quartic polynomials, lead to elliptic integrals; inverting those integrals produces elliptic functions, which have addition laws and differential equations resembling trigonometric functions but are doubly periodic. [matematicas.uam](http://matematicas.uam.es/~fernando.chamizo/asignaturas/2425cryptography/lectures/lecture04.pdf) These functions are useful in applications such as pendulum motion, rotating rigid bodies, elastic curves, integrable systems, and fast algorithms related to the arithmetic–geometric mean and even computations of $\pi$. [math.hse](https://math.hse.ru/data/2020/02/19/1575196181/introduction.pdf)

> "Trigonometric functions solve the geometry of the circle; elliptic functions solve the geometry that appears when the circle is replaced by more complicated algebraic curves." [matematicas.uam](http://matematicas.uam.es/~fernando.chamizo/asignaturas/2425cryptography/lectures/lecture04.pdf)

---

**Final challenge:** Assemble the full pendulum chain: start from $\theta''(t)+\frac{g}{\ell}\sin\theta(t)=0$, use energy conservation to get $\theta'(t)^2=2\frac{g}{\ell}\big(\cos\theta(t)-\cos\theta_0\big)$, apply the substitution $\sin(\theta/2)=k\sin\phi$ with $k=\sin(\theta_0/2)$, and check that the result is exactly the equation whose inversion is a Jacobi elliptic function.

*Next: [Part 2 — How to Add Points on a Curve: The Chord-and-Tangent Method]({% post_url 2026-08-30-chord-and-tangent-group-law %}), where the curve $y^2=x^3+ax+b$ acquires a group law and the anchor figure is dissected panel by panel.*

*References for the curious reader: Wikipedia articles on elliptic curves and elliptic functions; E. Dummit's notes on elliptic curves (Northeastern); the LMFDB database; SageMath documentation on elliptic curves; introductory handouts on elliptic functions (HSE, Leiden, Harvard, UCSB).*

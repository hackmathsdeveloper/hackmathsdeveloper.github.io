---
title: "The Change of Variable That Changed Mathematics — How Euler Derived the Gamma Integral"
date: 2026-06-20
categories:
  - Special Functions
  - Mathematics
tags:
  - gamma-function
  - euler
  - integral-derivation
  - infinite-product
  - change-of-variables
  - special-functions
  - mathematical-history
share: true
read_time: true
excerpt: "The Gamma integral ∫₀^∞ t^{z-1} e^{-t} dt is one of the most famous formulas in mathematics. But Euler didn't pull it from thin air — he started with an infinite product for the factorial, took logarithms, passed to a limit, and made a single brilliant substitution. This is the step-by-step derivation, from discrete product to continuous integral, that changed analysis forever."
---

**Challenge to the reader:** Start from Euler's logarithmic integral $\Gamma(x) = \int_0^1 (-\log t)^{x-1} dt$. Make the single substitution $t = e^{-u}$ and watch the standard Gamma integral appear. Then reverse-engineer the derivation: can you see why Euler would have thought to try this substitution in the first place?

---

Euler's starting point was an *infinite product* that exactly interpolates factorials; from that product you can derive the now-standard integral form via a limit and a change of variables. Below is a reasonably tight derivation, keeping the historical flavor but in modern notation. [[en.wikipedia](https://en.wikipedia.org/wiki/Gamma_function)]

---

## 1. Euler's Product Definition for $\Gamma$

One of Euler's definitions (in modernized form) is the product [[scipp.ucsc](http://scipp.ucsc.edu/~haber/archives/physics116A10/gamma.pdf)]

$$
\Gamma(s)
= \frac{1}{s}\,\prod_{n=1}^{\infty}
\frac{\left(1+\dfrac{1}{n}\right)^s}{1+\dfrac{s}{n}}
\quad (\text{Re}(s)>0).
\tag{E1}
$$

You can think of this as coming from the limit

$$
\Gamma(s)
= \lim_{N\to\infty}
\frac{N^s\,N!}{s(s+1)\cdots(s+N)},
\tag{E2}
$$

which Euler wrote down for real $s>0$. Indeed, rewriting [[web.maths.unsw.edu](https://web.maths.unsw.edu.au/~iand/5685/weeks6-7.pdf)]

$$
\frac{N!}{s(s+1)\cdots(s+N)}
= \frac{1}{s}\prod_{n=1}^N\frac{n}{s+n}
= \frac{1}{s}\prod_{n=1}^N
\frac{\dfrac{n}{n}(1+\tfrac{1}{n})^s}{1+\tfrac{s}{n}}
= \frac{1}{s}\prod_{n=1}^N
\frac{\left(1+\dfrac{1}{n}\right)^s}{1+\dfrac{s}{n}},
$$

then multiplying by $N^s$ and letting $N\to\infty$ gives the product (E1). This product converges for $\text{Re}(s)>0$ and satisfies the factorial recursion $\Gamma(s+1)=s\Gamma(s)$, so it's already a legitimate "continuous factorial." [[arxiv](https://arxiv.org/pdf/math/0202270.pdf)]

**Challenge to the reader:** Verify that (E2) satisfies $\Gamma(s+1) = s\Gamma(s)$ by direct algebraic manipulation of the limit expression. (Hint: write out the ratio $\Gamma(s+1)/\Gamma(s)$.)

---

## 2. Passing from Product to Exponential of a Sum

Take logs of (E1):

$$
\log \Gamma(s)
= -\log s
+ \sum_{n=1}^{\infty}
\left[
s\log\left(1+\frac{1}{n}\right)
- \log\left(1+\frac{s}{n}\right)
\right].
\tag{E3}
$$

For fixed $s$ and large $n$, expand the logarithms:

- $\log\left(1+\dfrac{1}{n}\right) = \dfrac{1}{n} - \dfrac{1}{2n^2} + O(n^{-3})$.
- $\log\left(1+\dfrac{s}{n}\right) = \dfrac{s}{n} - \dfrac{s^2}{2n^2} + O(n^{-3})$.

Hence for large $n$,

$$
s\log\left(1+\frac{1}{n}\right)
- \log\left(1+\frac{s}{n}\right)
= \left(s\cdot\frac{1}{n} - \frac{s}{n}\right)
+ O\!\left(\frac{1}{n^2}\right)
= O\!\left(\frac{1}{n^2}\right).
$$

So the series in (E3) converges absolutely for $\text{Re}(s)>0$. This allows us to interpret the sum [[arxiv](https://arxiv.org/pdf/math/0202270.pdf)]

$$
\sum_{n=1}^{\infty}
\left[
s\log\left(1+\frac{1}{n}\right)
- \log\left(1+\frac{s}{n}\right)
\right]
$$

as something akin to a Riemann sum that will turn into an integral in the limit.

---

## 3. Riemann-Sum Heuristic to an Integral

Focus on the term $-\log\left(1+\dfrac{s}{n}\right)$. For large $n$, you can write

$$
-\log\left(1+\frac{s}{n}\right)
= -\log\left(1+\frac{s}{n}\right)\cdot 1
= -\log\left(1+\frac{s}{n}\right)\,\Delta n,
$$

and think of $\Delta n = 1$ as a step size. With the change of variables $x = \dfrac{s}{n}$, so $n = \dfrac{s}{x}$ and $\Delta n \sim -\dfrac{s}{x^2}\,dx$, the sum has a heuristic relation to an integral involving $\log(1+x)$ and a power $x^{s-1}$. [[eulerarchive.maa](http://eulerarchive.maa.org/hedi/HEDI-2007-09.pdf)]

A more systematic way — which is how modern expositions do it — is to start from Euler's *logarithmic* integral representation

$$
\Gamma(x)
= \int_0^1 (-\log t)^{x-1}\,dt,
\quad x>0,
\tag{E4}
$$

which Euler himself wrote down in a 1730 letter. From this you can recover the standard $\int_0^\infty t^{x-1}e^{-t}dt$ form by a clean change of variables. Historically, the product and this integral are two equivalent faces of the same object; technically, one can show they define the same function by analyzing their logarithmic derivatives and boundary values. [[eulerarchive.maa](http://eulerarchive.maa.org/hedi/HEDI-2007-09.pdf)]

Let me show the clean part of the derivation: (E4) $\Rightarrow$ the usual $\int_0^\infty$ integral.

---

## 4. From Euler's Logarithmic Integral to the Standard Gamma Integral

Start from Euler's real-variable integral (modern notation): [[scipp.ucsc](http://scipp.ucsc.edu/~haber/archives/physics116A10/gamma.pdf)]

$$
\Gamma(x)
= \int_0^1 (-\log t)^{x-1}\,dt
\quad (x>0).
\tag{E4}
$$

Now make the substitution

$$
t = e^{-u},\quad u\in(0,\infty).
$$

Then

- $-\log t = u$,
- $dt = -e^{-u}du$,
- when $t$ goes from $0$ to $1$, $u$ goes from $\infty$ down to $0$.

So (E4) becomes

$$
\Gamma(x)
= \int_{t=0}^{1} (-\log t)^{x-1}\,dt
= \int_{u=\infty}^{0} u^{x-1}(-e^{-u})\,du
= \int_0^{\infty} u^{x-1} e^{-u}\,du.
\tag{E5}
$$

This is exactly the standard Euler integral of the second kind:

$$
\Gamma(x) = \int_0^\infty u^{x-1}e^{-u}du,\quad x>0.
$$

Thus the "modern" Gamma integral is just Euler's logarithmic integral under the exponential change of variable $t=e^{-u}$. [[en.wikipedia](https://en.wikipedia.org/wiki/Gamma_function)]

**Challenge to the reader:** The substitution $t = e^{-u}$ seems magical. Derive it backwards: start from $\int_0^\infty u^{x-1}e^{-u}du$, set $u = -\log t$, and recover the logarithmic form. Which direction feels more natural to you, and why?

---

## 5. Why the Product and the Integral Define the Same Function

From a modern perspective, you prove equivalence as follows.

1. **Both definitions satisfy the same functional equation.**
   - From the product: direct manipulation gives $\Gamma(s+1) = s\Gamma(s)$. [[arxiv](https://arxiv.org/pdf/math/0202270.pdf)]
   - From the integral: integration by parts gives
     $$
     \int_0^\infty t^{s}e^{-t}dt = s\int_0^\infty t^{s-1}e^{-t}dt,
     $$
     i.e. $\Gamma(s+1)=s\Gamma(s)$. [[en.wikipedia](https://en.wikipedia.org/wiki/Gamma_function)]

2. **Both agree at a reference point.**
   Using either definition, one checks $\Gamma(1)=1$. [[scipp.ucsc](http://scipp.ucsc.edu/~haber/archives/physics116A10/gamma.pdf)]

3. **Both are analytic for $\text{Re}(s)>0$.**
   The product converges normally there, and the integral converges absolutely and defines a holomorphic function of $s$. [[en.wikipedia](https://en.wikipedia.org/wiki/Gamma_function)]

4. **Uniqueness on a half-plane.**
   The difference of two such analytic functions satisfying the same recursion and initial value must vanish on $\text{Re}(s)>0$ (this can be formalized using the identity theorem on an appropriate domain).

Hence, Euler's product, his logarithmic integral, and the now-standard $\int_0^\infty$ integral are all just different representations of the same function $\Gamma$ on $\text{Re}(s)>0$. [[scipp.ucsc](http://scipp.ucsc.edu/~haber/archives/physics116A10/gamma.pdf)]

---

## 6. The Big Picture: From Discrete to Continuous

Informally you can view the chain as:

1. Start with **discrete factorial** and a limit/product representation that extends it:
   $\Gamma(s) = \lim_{N\to\infty} \dfrac{N! N^s}{s(s+1)\cdots(s+N)}$. [[web.maths.unsw.edu](https://web.maths.unsw.edu.au/~iand/5685/weeks6-7.pdf)]

2. Rewrite that limit as an **infinite product** over $n$, giving (E1). [[arxiv](https://arxiv.org/pdf/math/0202270.pdf)]

3. Interpret the logarithm of the product as a series approximating an **integral over a continuous variable**, which leads to Euler's logarithmic integral $\int_0^1 (-\log t)^{s-1}dt$. [[eulerarchive.maa](http://eulerarchive.maa.org/hedi/HEDI-2007-09.pdf)]

4. Make the substitution $t=e^{-u}$ to get the **standard Gamma integral**
   $\Gamma(s) = \int_0^\infty u^{s-1}e^{-u}du$. [[scipp.ucsc](http://scipp.ucsc.edu/~haber/archives/physics116A10/gamma.pdf)]

Historically Euler did these steps in a more heuristic, computational manner, then later analysis (Cauchy, Weierstrass, etc.) put them on firm footing; but conceptually, that's the bridge from Euler's product to the familiar integral.

---

## 7. Why This Derivation Still Matters

The product-to-integral bridge isn't just a historical curiosity — it's a pattern that recurs throughout analysis:

| Setting | Discrete (Product/Sum) | Continuous (Integral) | Bridge |
|---------|----------------------|----------------------|--------|
| Gamma function | Euler product | $\int_0^\infty t^{z-1}e^{-t}dt$ | $t = e^{-u}$ |
| Riemann zeta | Euler product over primes | Mellin transform of theta | Mellin inversion |
| q-analogues | q-Gamma product | Jackson integral | $q \to 1^-$ limit |
| Weierstrass factorization | Canonical product | Entire function representation | Logarithmic derivative |

The same "take a discrete interpolating product, convert to a sum via logs, then recognize as a Riemann sum" pattern shows up whenever you need to analytically continue a function defined on integers to the complex plane.

**Final challenge:** Try to derive the Gamma integral starting from Euler's *other* definition — the limit $\Gamma(s) = \lim_{N\to\infty} \frac{N! N^s}{s(s+1)\cdots(s+N)}$. Take logs, recognize a Riemann sum, and see if you can directly arrive at $\int_0^\infty t^{s-1}e^{-t}dt$ without passing through the logarithmic integral as an intermediate step. (Hint: you'll need the identity $\log N = \sum_{k=1}^N \frac{1}{k} - \gamma + o(1)$ involving the Euler–Mascheroni constant.)

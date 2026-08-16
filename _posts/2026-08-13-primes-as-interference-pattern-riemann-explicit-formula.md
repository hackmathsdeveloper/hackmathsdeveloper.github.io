---
title: "The Primes Are an Interference Pattern — How ζ(s)'s Zeros Rebuild π(x)"
date: 2026-08-13
categories:
  - Number Theory
  - Mathematics
tags:
  - prime-counting
  - riemann-zeta
  - euler-product
  - mobius-inversion
  - explicit-formula
  - prime-powers
  - mellin-transform
  - riemann-hypothesis
share: true
read_time: true
excerpt: "π(x) counts primes as a staircase; ζ(s) encodes them as an Euler product; Riemann's explicit formula rebuilds the staircase from the zeros of ζ(s). Follow the single thread — sieve → product → weighted prime powers → Mellin inversion — that turns primes into an interference pattern."
---

**Challenge to the reader:** Compute $J(10)$ by hand: list every prime power $p^m \le 10$, weight each one by $1/m$, and confirm the total is $16/3$. Then do the same for $J(100)$ and check you get $428/15$. Keep both values handy — you will invert them back into $\pi(x)$ in Section 5.

---

Here is the whole story of this post in one displayed equation, Riemann's explicit formula:

$$
J(x)=\operatorname{Li}(x)-\sum_{\rho}\operatorname{Li}(x^{\rho})+\bigl(\text{trivial zeros and constants}\bigr),
$$

where $\rho$ runs over the non-trivial zeros of the Riemann zeta function. Read it right-to-left and it says something almost unbelievable: the staircase that counts primes — a discrete, jumpy, arithmetic object — can be **rebuilt from a smooth curve plus a sum of oscillatory waves, one wave for each zero of $\zeta(s)$**. The primes, in other words, are an interference pattern.

**Why it matters.** There is no formula for the $n$-th prime, and no recurrence that produces primes in order. Yet the *entire* distribution of primes is recoverable from a single analytic function $\zeta(s)$ — specifically from the locations of its zeros. The point of this post is to walk the single logical thread that connects a childhood sieve to the Riemann Hypothesis, pausing at every junction to make the hand-off from one idea to the next explicit.

---

## 1. The Staircase Nobody Can Analyze Directly

Let $\pi(x)$ count the primes up to $x$:

$$
\pi(x)=\#\lbrace p \le x : p \text{ prime}\rbrace.
$$

It is a staircase: it jumps by $1$ exactly at $2,3,5,7,11,\dots$ and is flat everywhere else. The first few values — $\pi(10)=4$, $\pi(100)=25$ — are easy, but the function resists smooth analysis because it is constant except at isolated, irregularly spaced jumps.

Two classical observations tame the *average* behavior. The density $\pi(x)/x$ falls as $x$ grows (primes thin out), and the average gap $x/\pi(x)$ grows roughly like $\log x$. Here is the progress of the staircase at the powers of ten:

| $x$ | $\pi(x)$ | $\pi(x)/x$ | $1/\pi(x)$ | $x/\pi(x)$ |
|---:|---:|---:|---:|---:|
| $10$ | $4$ | $0.4$ | $0.25$ | $2.5$ |
| $10^2$ | $25$ | $0.25$ | $0.04$ | $4$ |
| $10^3$ | $168$ | $0.168$ | $0.005952$ | $5.952$ |
| $10^4$ | $1\,229$ | $0.1229$ | $0.0008137$ | $8.137$ |
| $10^5$ | $9\,592$ | $0.09592$ | $0.00010425$ | $10.43$ |
| $10^6$ | $78\,498$ | $0.078498$ | $0.000012739$ | $12.74$ |
| $10^7$ | $664\,579$ | $0.0664579$ | $0.000001505$ | $15.05$ |
| $10^8$ | $5\,761\,455$ | $0.05761455$ | $0.0000001736$ | $17.36$ |

Read down the columns. $\pi(x)$ climbs, the density $\pi(x)/x$ drifts toward zero (primes thin out, slowly), and $1/\pi(x)$ collapses — nothing in the first four columns happens quickly. The last column, the average gap $x/\pi(x)$, is the informative one: compare it with $\log x = 2.303, 4.605, 6.908, 9.210, 11.513, 13.816, 16.118, 18.421$ at the same points. The gap tracks $\log x$ with a nearly constant offset — indeed $\log x - x/\pi(x)$ settles down toward about $1.08$. That heuristic becomes the Prime Number Theorem:

$$
\pi(x)\sim\frac{x}{\log x},
$$

with the logarithmic integral $\operatorname{Li}(x)=\int_2^x \frac{dt}{\log t}$ supplying a much better smooth fit. But — and this is the crucial frustration — these smooth curves capture only the *trend*. They say nothing about *where* the jumps sit. If we want the jumps themselves, we need a completely different tool. That tool is the zeta function.

---

## 2. The Sieve, Rewritten as an Infinite Product

The link between primes and analysis begins with Euler, and it begins with a trick you already know. The **sieve of Eratosthenes** removes multiples of $2$, then $3$, then $5$, and so on; what survives is exactly the primes. Euler discovered that the same "removal" can be performed algebraically on an infinite series.

Start with the zeta series

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}
=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\frac{1}{5^s}+\frac{1}{6^s}+\cdots,
$$

which converges for $\Re(s) \gt 1$. This is the **additive format**: one term for every integer. The sieve will convert it into the **multiplicative format**: one factor for every prime.

Multiply by $1-2^{-s}$ and watch the terms cancel in pairs:

$$
\begin{aligned}
(1-2^{-s})\,\zeta(s)
&=\Bigl(1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\frac{1}{5^s}+\frac{1}{6^s}+\cdots\Bigr)
-\Bigl(\frac{1}{2^s}+\frac{1}{4^s}+\frac{1}{6^s}+\frac{1}{8^s}+\frac{1}{10^s}+\frac{1}{12^s}+\cdots\Bigr)\\
&=1+\frac{1}{3^s}+\frac{1}{5^s}+\frac{1}{7^s}+\frac{1}{9^s}+\cdots.
\end{aligned}
$$

Every term whose denominator is divisible by $2$ has canceled; the odd denominators survive. Multiply again by $1-3^{-s}$: every surviving term whose denominator is divisible by $3$ is removed, and what remains are the integers divisible by neither $2$ nor $3$:

$$
(1-3^{-s})(1-2^{-s})\,\zeta(s)
=1+\frac{1}{5^s}+\frac{1}{7^s}+\frac{1}{11^s}+\frac{1}{13^s}+\frac{1}{17^s}+\cdots.
$$

One more factor, $1-5^{-s}$, strips out the multiples of $5$:

$$
(1-5^{-s})(1-3^{-s})(1-2^{-s})\,\zeta(s)
=1+\frac{1}{7^s}+\frac{1}{11^s}+\frac{1}{13^s}+\frac{1}{17^s}+\frac{1}{19^s}+\frac{1}{23^s}+\cdots.
$$

Continuing over all primes, each integer $n$ is deleted exactly once — at the prime it "carries" in its factorization — until only $n=1$ survives. Rearranging what is left gives the identity

$$
\zeta(s)=\frac{1}{(1-2^{-s})(1-3^{-s})(1-5^{-s})(1-7^{-s})\cdots}
=\prod_{p}\left(1-\frac{1}{p^s}\right)^{-1},
$$

the **Euler product**.

The bridge, stated plainly: *the sieve works because every integer has a unique prime factorization.* The product over primes is literally a multiplicative encoding of unique factorization, and $\zeta(s)$ is the object in which that encoding is made analytic. This is the single most important hand-off in the whole story — a discrete counting fact (unique factorization) has been traded for a smooth complex function.

The factor $(1-p^{-s})^{-1}$ deserves one more look, because it will recur in disguise. Expanding it as a geometric series:

$$
\left(1-\frac{1}{p^s}\right)^{-1}
=1+\frac{1}{p^s}+\frac{1}{p^{2s}}+\frac{1}{p^{3s}}+\frac{1}{p^{4s}}+\frac{1}{p^{5s}}+\frac{1}{p^{6s}}+\cdots.
$$

Each prime contributes not just $p^{-s}$ but *all* powers $p^{-ms}$ — here is where the extra terms are *generated*: every factor of the product, expanded, produces an entire infinite series of prime powers, and because each integer has a unique factorization, multiplying all of these series together reassembles the original additive series term by term. The product and the sum encode exactly the same information; the product is simply organized prime-by-prime instead of integer-by-integer. We are about to take a logarithm to see those powers explicitly.

**Challenge to the reader:** Multiply out the truncated product $(1-2^{-s})^{-1}(1-3^{-s})^{-1}(1-5^{-s})^{-1}$ as a power series in $n^{-s}$. Which integer coefficients are now equal to $1$, and which are missing? How does this partial product differ from $\zeta(s)$?

---

## 3. The Logarithm Turns the Product into Prime Powers

Products are multiplicative and therefore awkward to compare with the *additive* structure of a counting function. So take logarithms — the standard move that converts a product into a sum:

$$
\log\zeta(s)=-\sum_{p}\log\left(1-p^{-s}\right).
$$

Now expand each term using the ordinary power series

$$
-\log(1-u)=\sum_{m\ge 1}\frac{u^m}{m}=u+\frac{u^2}{2}+\frac{u^3}{3}+\cdots,
$$

and substitute $u=p^{-s}$:

$$
\log\zeta(s)=\sum_{p}\sum_{m\ge 1}\frac{1}{m\,p^{ms}}.
$$

Read this carefully, because it contains the next hand-off. The left side is a single smooth function. The right side is a double sum over *prime powers* $p^m$, each weighted by $1/m$. The prime $p$ contributes with weight $1$; its square $p^2$ contributes with weight $1/2$; its cube with $1/3$; and so on.

So $\zeta(s)$ encodes primes multiplicatively, while $\log\zeta(s)$ exposes them as a weighted enumeration of prime powers. The weight $1/m$ is not a coincidence we are free to ignore — it is exactly the weight that will define Riemann's counting function. This is the transition from "a function that knows about primes" to "a function whose coefficients literally count something."

---

## 4. $J(x)$: The Weighted Staircase

A Dirichlet series $\sum_n a_n n^{-s}$ is only useful to number theorists once we can read off its coefficients $a_n$. Here the coefficients are

$$
a_n=\begin{cases}1/m, & n=p^m \text{ is a prime power},\\ 0, & \text{otherwise}.\end{cases}
$$

Riemann's weighted counting function is simply the partial sum of these coefficients:

$$
J(x)=\sum_{\substack{p^m \le x \\ m \ge 1}}\frac{1}{m}.
$$

Concretely: the prime $2$ contributes $1$, the prime power $2^2=4$ contributes $1/2$, $2^3=8$ contributes $1/3$, and so on. Because $J(x)$ jumps at every *prime power* (not just at primes), and because its jump heights shrink as $1/m$, it is *smoother* than $\pi(x)$ in a precise sense — its jumps are smaller and more regularly layered, which is exactly what makes it tractable to analytic techniques.

Worked values make the definition concrete, and it is worth starting at the bottom. Nothing up to and including $1$ is a prime power, so the sum is empty:

$$
J(1)=0.
$$

The staircase sits at zero until its very first jump — of height $1$ — at $x=2$. At $x=10$,

$$
J(10)=\underbrace{4}_{\text{primes }2,3,5,7}+\underbrace{\frac12+\frac12}_{4=2^2,\ 9=3^2}+\underbrace{\frac13}_{8=2^3}=\frac{16}{3}\approx 5.33.
$$

At $x=100$ there are $25$ primes, plus four squares ($2^2,3^2,5^2,7^2$), two cubes ($2^3,3^3$), two fourth powers ($2^4,3^4$), one fifth power ($2^5$), and one sixth power ($2^6$):

$$
J(100)=25+4\left(\frac12\right)+2\left(\frac13\right)+2\left(\frac14\right)+\frac15+\frac16=\frac{428}{15}\approx 28.53.
$$

There is a direct relationship between the two staircases, and it is the key to moving between them. A prime power $p^m\le x$ is the same thing as a prime $p\le x^{1/m}$. Counting the latter with $\pi$ and weighting by $1/m$ gives

$$
J(x)=\sum_{m\ge 1}\frac{1}{m}\,\pi\!\left(x^{1/m}\right)
=\pi(x)+\frac12\pi(\sqrt x)+\frac13\pi(x^{1/3})+\cdots.
$$

So $J(x)$ is the prime staircase $\pi(x)$ plus all of its "prime-power layers." The layered form also makes larger values mechanical to compute, because each layer is just $\pi$ evaluated at an $m$-th root. At $x=1000$ the layers are: $168$ primes ($m=1$); $\pi(\sqrt{1000})=\pi(31)=11$ squares; $\pi(\sqrt[3]{1000})=\pi(10)=4$ cubes; $\pi(1000^{1/4})=\pi(5)=3$ fourth powers; two fifth powers ($2^5=32$, $3^5=243$) and two sixth powers ($2^6=64$, $3^6=729$); then only powers of $2$ survive, one per layer from $m=7$ through $m=9$:

$$
J(1000)=168+11\left(\frac12\right)+4\left(\frac13\right)+3\left(\frac14\right)+2\left(\frac15\right)+2\left(\frac16\right)+\frac17+\frac18+\frac19=\frac{445273}{2520}\approx 176.70.
$$

At $x=10^4$ the pattern continues — $25$ squares ($p\le 100$), $8$ cubes ($p\le 21$), $4$ fourth powers ($p\le 10$), $3$ fifths ($p\le 6$), two sixths, two sevenths, and two eighths ($p\le 4$, $p\le 3$, $p\le 3$), and then single powers of $2$ from $m=9$ through $m=13$:

$$
J(10^4)=1229+25\left(\frac12\right)+8\left(\frac13\right)+4\left(\frac14\right)+3\left(\frac15\right)+2\left(\frac16\right)+2\left(\frac17\right)+2\left(\frac18\right)+\frac19+\frac1{10}+\frac1{11}+\frac1{12}+\frac1{13}\approx 1247.10.
$$

The progression is worth tabulating:

| $x$ | $\pi(x)$ | $J(x)$ | $J(x)-\pi(x)$ |
|---:|---:|---:|---:|
| $1$ | $0$ | $0$ | $0$ |
| $10$ | $4$ | $16/3\approx 5.33$ | $1.33$ |
| $10^2$ | $25$ | $428/15\approx 28.53$ | $3.53$ |
| $10^3$ | $168$ | $\approx 176.70$ | $8.70$ |
| $10^4$ | $1\,229$ | $\approx 1247.10$ | $18.10$ |
| $10^5$ | $9\,592$ | $\approx 9633.77$ | $41.77$ |

Two features of the table are worth saying out loud. First, **the expansion terminates:** layer $m$ exists only while $x^{1/m}\ge 2$, i.e. while $m\le\log_2 x$. That is why $J(10)$ has $3$ layers, $J(100)$ six, $J(1000)$ nine, $J(10^4)$ thirteen, $J(10^5)$ sixteen — each decade of $x$ buys about $\log_2 10\approx 3.32$ new layers. Second, **the layers form only a thin crust:** at $x=10^4$ the entire excess over $\pi(x)$ is a mere $18$, and most of it — $25/2=12.5$ — comes from the square layer alone. Because the crust is dominated by $\tfrac12\pi(\sqrt x)$, it grows like $\sqrt{x}/\log x$, a vanishing fraction of $\pi(x)$ itself.

This is not just notation: it tells us that $J$ and $\pi$ contain the *same information*, just packaged differently — and that packaging is about to be inverted.

---

## 5. Möbius Inversion Gives $\pi$ Back

If $J(x)=\pi(x)+\tfrac12\pi(\sqrt x)+\tfrac13\pi(x^{1/3})+\cdots$, then $\pi(x)$ is hiding inside $J(x)$ and we need to undo the prime-power layers. The tool is the **Möbius function**:

$$
\mu(n)=\begin{cases}1,&n=1,\\ (-1)^k,&n \text{ is a product of } k \text{ distinct primes},\\ 0,&n \text{ has a repeated prime factor}.\end{cases}
$$

Its role is precisely to be the "arithmetic inverse" of the all-ones function: it cancels layered sums back down to their base terms. Applying it layer-by-layer recovers ordinary prime counting:

$$
\pi(x)=\sum_{m\ge 1}\frac{\mu(m)}{m}\,J\!\left(x^{1/m}\right).
$$

The first few terms,

$$
\pi(x)=J(x)-\frac12 J(x^{1/2})-\frac13 J(x^{1/3})-\frac15 J(x^{1/5})+\frac16 J(x^{1/6})-\cdots,
$$

are worth staring at: the $m=4$ term is *absent* because $\mu(4)=0$ — squares of squares are already handled. A worked check at $x=100$,

$$
\pi(100)=J(100)-\frac12 J(10)-\frac13 J(100^{1/3})-\frac15 J(100^{1/5})+\frac16 J(100^{1/6})=25,
$$

confirms the machinery. This closes one loop: **know $J(x)$, and Möbius inversion hands you $\pi(x)$ exactly.** The remaining, and deepest, question is whether we can get $J(x)$ itself from analysis.

**Challenge to the reader:** Use the $\pi$-values $\pi(100)=25$ and $\pi(10)=4$ (plus $\pi(\sqrt{100})=\pi(10)=4$) to recompute $J(100)$ directly from the layered formula $J(x)=\sum_m \tfrac1m \pi(x^{1/m})$. Confirm you recover $428/15$. Notice how few of the layers are actually nonzero.

---

## 6. The Bridge: A Dirichlet Series Is a Mellin Transform

Everything so far is arithmetic. Here is where it becomes analysis, and it is the single most important hand-off in the post — so it deserves its own section.

The double sum for $\log\zeta(s)$ is a sum over prime powers with jump data given by $J(x)$. We can rewrite that sum as an integral against the staircase's jumps, a Stieltjes integral:

$$
\log\zeta(s)=\sum_{p^m}\frac{1}{m}p^{-ms}
=\int_{1^-}^{\infty} x^{-s}\,dJ(x)
=s\int_{1}^{\infty} J(x)\,x^{-s-1}\,dx.
$$

This is a **Mellin transform**: it converts the counting function $J(x)$ into the analytic function $\log\zeta(s)$. And Mellin transforms can be inverted. The inverse is a contour integral,

$$
J(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{\log\zeta(s)}{s}\,x^{s}\,ds,\qquad c \gt 1.
$$

Stop and absorb what just happened. $J(x)$, a discrete staircase, and $\log\zeta(s)$, a complex-analytic function, are now **two faces of the same object** — dual under the Mellin transform. To understand the distribution of prime powers, we do not need to touch primes directly; we need only to understand where the function $\log\zeta(s)$ is large, small, or singular. That is the entire program of analytic number theory compressed into two lines.

| Arithmetic side (discrete) | Analytic side (continuous) |
|---|---|
| primes $p$ | factors of the Euler product $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ |
| prime powers $p^m$, weight $1/m$ | terms of $\log\zeta(s)=\sum_{p,m}\frac{1}{m}p^{-ms}$ |
| the weighted staircase $J(x)$ | the function $\log\zeta(s)$ (a Mellin pair) |
| the plain staircase $\pi(x)$ | recovered from $\log\zeta(s)$ via Möbius inversion |
| the jumps of $J(x)$ | the **zeros** of $\zeta(s)$ (next section) |

The last row of the table is not yet justified — it is the claim we now prove.

---

## 7. The Explicit Formula: Zeros Rebuild the Staircase

The contour integral for $J(x)$ can be evaluated by the method of residues: push the contour to the left and collect what it passes over. Three kinds of singularities of $\log\zeta(s)$ lie in the way, and each one tells a different part of the story of the primes.

First, $\zeta(s)$ has a simple **pole at $s=1$**. Its residue contributes the leading smooth term $\operatorname{Li}(x)$ — the same logarithmic integral that Section 1 met as a mere approximation. The approximation is now *derived*: it is the exact shadow of the pole.

Second, $\zeta(s)$ vanishes at the **trivial zeros** $s=-2,-4,-6,\dots$; these produce the smaller, unremarkable constants and correction terms in the explicit formula.

Third — and this is where the magic lives — $\zeta(s)$ vanishes at the **non-trivial zeros** $\rho$ inside the critical strip $0\lt\Re(\rho)\lt 1$. Each such zero contributes a term $-\operatorname{Li}(x^{\rho})$. Collecting everything gives Riemann's explicit formula in its genuine form:

$$
J(x)=\operatorname{Li}(x)-\sum_{\rho}\operatorname{Li}(x^{\rho})+\text{(trivial zeros and constants)}.
$$

This formula *is* the answer to the question posed in Section 1. The staircase that resisted analysis is now written as a smooth trend $\operatorname{Li}(x)$ plus a sum of oscillatory corrections, one per non-trivial zero. Adding more zero terms progressively restores more of the jumpy, discontinuous staircase from the smooth curve — the zeros *locate* the primes.

Because the non-trivial zeros come in conjugate pairs $\rho=\beta+i\gamma$ and $\bar\rho=\beta-i\gamma$, each pair combines into a real oscillation, so the sum is real despite being built from complex pieces.

**Challenge to the reader:** Suppose a zero has the form $\rho=\tfrac12+i\gamma$. Show that $\operatorname{Li}(x^{\rho})$ oscillates with frequency $\gamma\log x$ and amplitude controlled by $x^{1/2}$. In words: what happens to the amplitude of the correction as $x$ grows, and why does this make the trend $\operatorname{Li}(x)$ dominant?

---

## 8. The Riemann Hypothesis and the Interference Pattern

Everything is now in place for the final, most famous claim. The non-trivial zeros live somewhere in the strip $0\lt\Re(\rho)\lt 1$, but *where* in the strip determines exactly how tightly the primes cluster around the trend line $\operatorname{Li}(x)$.

The **Riemann Hypothesis** asserts that every non-trivial zero lies exactly on the midline:

$$
\Re(\rho)=\frac12 \quad\Longleftrightarrow\quad \rho=\frac12+i\gamma.
$$

If that is true, every oscillatory correction is of the form $x^{1/2+i\gamma}$, so its amplitude is exactly $x^{1/2}$ — the smallest possible amplitude consistent with all the known constraints, and hence the best possible control on the error between $\pi(x)$ and $\operatorname{Li}(x)$. In that sense the Riemann Hypothesis is not an arbitrary conjecture about a special function; it is the claim that *the primes deviate from their smooth average as gently as the laws of the problem allow*.

The video's culminating image, and the title of this post, is now fully justified. Think of $\operatorname{Li}(x)$ as a steady background field and each zero as a wave $\operatorname{Li}(x^{\rho})$. The primes are not generated by any local rule; they are the *interference pattern* formed when infinitely many of these waves superpose. The smooth curve gives the trend, the zeros give the oscillations, and together they resolve the individual jumps of $\pi(x)$.

---

## 9. Deeper Significance

Why does this chain matter beyond its own elegance? Because it made a problem about *integers* into a problem about *frequencies* — and frequency problems are where the rest of mathematics already excels.

The passage from $\pi(x)$ to $\zeta(s)$ to the zeros of $\zeta(s)$ is a spectral decomposition: a messy object is written as a sum of pure tones. The same pattern shows up again and again — in the trace formulas of automorphic forms, in random matrix theory (where the zeros of $\zeta$ are conjectured to behave like the eigenvalues of random Hermitian matrices), in quantum chaos, and in the Langlands program. Each of these modern subjects is a descendant of Riemann's insight that counting primes and locating zeros are the *same* problem, viewed from two sides of a Mellin transform.

For the full tour of how $\zeta(s)$ concretely encodes primes, see [the ten instantiations of the zeta function]({% post_url 2026-05-25-riemann-zeta-function %}); for the companion treatment of $J(x)$ itself, see [Riemann's $J(x)$ and the music of the primes]({% post_url 2026-05-27-prime-counting-function-pi-x-and-riemann-j-function %}); and for the very first step — where $\zeta(2)=\pi^2/6$ — see [the Basel problem]({% post_url 2026-05-31-basel-problem %}).

---

**Final challenge to the reader:** Build the entire chain in miniature. (1) Write down the Euler product for $\zeta(s)$. (2) Take its logarithm and expand to find the weight $1/m$ on prime powers. (3) Define $J(x)$ from those weights. (4) Invert with Möbius to express $\pi(x)$ in terms of $J$. (5) Explain, in one sentence, which singularity of $\zeta(s)$ gives the leading term $\operatorname{Li}(x)$ and which singularities give the oscillations. If you can write those five steps from memory, you have internalized the single most important bridge in analytic number theory.

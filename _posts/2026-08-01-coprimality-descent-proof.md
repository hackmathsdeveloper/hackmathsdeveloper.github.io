---
title: "The Fraction That Can't Stop Simplifying — Until It Must"
date: 2026-08-01
categories:
  - Number Theory
  - Mathematics
tags:
  - number-theory
  - gcd
  - descent-argument
  - recurrence
  - coprime
  - olympiad-problem
share: true
read_time: true
excerpt: "Start with two distinct positive integers and iterate: reduce the fraction (2m+1)/(2n+1) to lowest terms. At each step, the new numerator and denominator can share a common factor with their doubled-plus-one counterparts — but only finitely many times. The proof uses a cunning descent argument that shows the sum m+n must shrink whenever a common factor survives."
---

**Challenge to the reader:** Pick any two distinct positive integers — say 2 and 5. Form the fraction $$\frac{2\cdot 2 + 1}{2\cdot 5 + 1} = \frac{5}{11}$$ (already reduced). Now repeat: $$\frac{2\cdot 5 + 1}{2\cdot 11 + 1} = \frac{11}{23}$$. Keep going. At which step do the numerator and denominator share a common factor? Can you find a starting pair that *never* produces a coprime pair after the first step? Try before reading on.

---

## 1. The Problem

Let $$m_0$$ and $$n_0$$ be **distinct** positive integers. For every positive integer $$k$$, define $$m_k$$ and $$n_k$$ to be the *relatively prime* positive integers such that

$$
\frac{m_k}{n_k} = \frac{2m_{k-1} + 1}{2n_{k-1} + 1}.
$$

In other words, we take the fraction on the right, reduce it to lowest terms, and call the result $$m_k / n_k$$.

**Prove:** $$2m_k + 1$$ and $$2n_k + 1$$ are relatively prime for all but finitely many positive integers $$k$$.

---

## 2. Why This Is Surprising

At first glance, nothing about the recurrence forces coprimality. The map

$$
\frac{m}{n} \;\longmapsto\; \frac{2m+1}{2n+1}
$$

can easily produce numerator and denominator with a common factor. When that happens, we reduce, and the reduced pair feeds the next step. The question is: can this reduction happen *infinitely often*, or does the process eventually "settle down"?

The answer is it must settle down — and the proof fits in a few lines once you spot the right invariant.

---

## 3. Recasting the Recurrence

Define

$$
a_k = 2m_k + 1, \qquad b_k = 2n_k + 1, \qquad g_k = \gcd(a_k, b_k).
$$

The goal is to show $$g_k = 1$$ for all sufficiently large $$k$$.

Because $$m_k, n_k$$ are obtained by reducing the previous fraction, we have

$$
m_k = \frac{2m_{k-1} + 1}{g_{k-1}} = \frac{a_{k-1}}{g_{k-1}}, \qquad
n_k = \frac{2n_{k-1} + 1}{g_{k-1}} = \frac{b_{k-1}}{g_{k-1}}.
$$

Now write $$a_{k-1} = g_{k-1} x_{k-1}$$ and $$b_{k-1} = g_{k-1} y_{k-1}$$, where by construction

$$
\gcd(x_{k-1}, y_{k-1}) = 1.
$$

(After all, $$g_{k-1}$$ is the *greatest* common divisor — stripping it leaves a coprime pair.)

Then

$$
a_k = 2m_k + 1 = 2x_{k-1} + 1, \qquad
b_k = 2n_k + 1 = 2y_{k-1} + 1.
$$

And crucially,

$$
x_k = \frac{a_k}{g_k} = \frac{2x_{k-1} + 1}{g_k}, \qquad
y_k = \frac{2y_{k-1} + 1}{g_k}.
$$

---

## 4. A Parity Observation

Since $$a_k = 2m_k + 1$$ is always odd, and likewise $$b_k$$ is odd, their gcd $$g_k$$ must be **odd**.

Consequence: if $$g_k > 1$$, then $$g_k \geq 3$$. The factor 2 is never available — any common factor is at least 3. This innocent observation is what makes the descent work.

---

## 5. The Descent

Consider the sum

$$
s_k = m_k + n_k = x_k + y_k.
$$

When $$g_k > 1$$, we have $$g_k \geq 3$$, and

$$
s_k = x_k + y_k = \frac{2x_{k-1} + 1}{g_k} + \frac{2y_{k-1} + 1}{g_k}
     = \frac{2(x_{k-1} + y_{k-1}) + 2}{g_k}
     \leq \frac{2s_{k-1} + 2}{3}.
$$

Now ask: when is $$\frac{2s + 2}{3}$$ smaller than $$s$$ itself?

$$
\frac{2s + 2}{3} < s \;\Longleftrightarrow\; 2s + 2 < 3s \;\Longleftrightarrow\; s > 2.
$$

Since $$m_{k-1}$$ and $$n_{k-1}$$ are distinct positive integers, their sum is at least $$1 + 2 = 3$$. So $$s_{k-1} \geq 3$$, and the inequality holds:

$$
s_k \leq \frac{2s_{k-1} + 2}{3} < s_{k-1} \qquad \text{whenever } g_k > 1.
$$

The sum $$s_k$$ is a **positive integer** that strictly decreases every time $$g_k > 1$$.

---

**Challenge to the reader:** Prove that $$g_k$$ cannot equal 2. (Hint: look at the form of $$a_k$$.) Then verify the inequality $$\frac{2s + 2}{3} < s$$ for all $$s \geq 3$$ by induction on $$s$$ — or just solve the linear inequality as above. Which method generalizes better?

---

## 6. Why This Forces Finiteness

A positive integer can strictly decrease only finitely many times. The sum $$s_k = m_k + n_k$$ starts at $$s_0 = m_0 + n_0$$ and drops by at least 1 each time $$g_k > 1$$ occurs. Therefore:

> $$g_k > 1$$ can happen at most $$s_0 - 3$$ times.

After that, $$g_k = 1$$ forever — meaning $$\gcd(2m_k + 1, \, 2n_k + 1) = 1$$ from that point onward.

That completes the proof.

---

## 7. What Happens When the Sum Is Small?

The edge cases are instructive. The smallest possible sum for distinct positive integers is $$1 + 2 = 3$$. Let's trace it:

- $$(m_0, n_0) = (1, 2)$$: then $$a_1 = 3, b_1 = 5, g_1 = \gcd(3,5) = 1$$. Already coprime — zero "bad" steps.
- $$(m_0, n_0) = (1, 4)$$: $$a_1 = 3, b_1 = 9, g_1 = 3$$. Then $$m_1 = 1, n_1 = 3$$. Next: $$a_2 = 3, b_2 = 7, g_2 = 1$$. Exactly one bad step, then done.

Try $$(m_0, n_0) = (1, 3k+1)$$ for any $$k \geq 0$$ — you'll see the descent in action, with $$g_1 = 3$$ reducing the pair in one step.

---

## 8. Deeper Significance

This problem is a gem because it teaches a **meta-technique** that appears across number theory, dynamics, and algebra:

> Define a **complexity measure** that strictly decreases under "bad" conditions. Since the measure is bounded below, bad behaviour must terminate.

In our case:
- **Bad condition:** $$g_k > 1$$ (the pair $$2m_k+1, 2n_k+1$$ share a factor).
- **Complexity measure:** $$s_k = m_k + n_k$$.
- **Descent lemma:** $$g_k > 1 \implies s_k < s_{k-1}$$.
- **Termination:** positive integers cannot descend forever.

The same template proves:
- Termination of the Euclidean algorithm (remainder decreases).
- Finiteness of ideal class groups in number fields (norm bounded below by Minkowski's bound).
- Preperiodicity of rational points under certain dynamical systems (canonical height descends).
- The ACC/DCC chain conditions in commutative algebra.

We'll explore these connections in companion posts — but for now, the takeaway is: **when you're stuck proving something happens only finitely often, look for a positive-integer-valued function that drops at every occurrence.**

---

**Final challenge:** Generalize the result. For which linear fractional transformations

$$
\frac{m}{n} \;\longmapsto\; \frac{am + b}{cn + d}
$$

(always reduced to lowest terms) does the analogous statement hold — that $$\gcd(\alpha m_k + \beta, \, \gamma n_k + \delta) = 1$$ for all but finitely many $$k$$? Experiment with small integer parameters and see if you can formulate a theorem.

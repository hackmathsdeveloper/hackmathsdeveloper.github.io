
**Problem** Let $m_0$ and $n_0$ be distinct positive integers. For every positive integer $k$, define $m_k$ and $n_k$ to be the relatively prime positive integers such that

$$ \frac{m_k}{n_k} = \frac{2m_{k-1} + 1}{2n_{k-1} + 1}. $$

Prove that $2m_k + 1$ and $2n_k + 1$ are relatively prime for all but finitely many positive integers $k$.


**Answer** We are given distinct positive integers $ m_0, n_0 $, and for each positive integer $ k $, we define **relatively prime** positive integers $ m_k, n_k $ such that:

$$
\frac{m_k}{n_k} = \frac{2m_{k-1} + 1}{2n_{k-1} + 1}
$$

That is, the fraction $ \frac{2m_{k-1} + 1}{2n_{k-1} + 1} $ is reduced to lowest terms to get $ \frac{m_k}{n_k} $. So:

$$
m_k = \frac{2m_{k-1} + 1}{d_k}, \quad n_k = \frac{2n_{k-1} + 1}{d_k}, \quad \text{where } d_k = \gcd(2m_{k-1} + 1, 2n_{k-1} + 1)
$$

Our goal is to prove that **for all but finitely many $ k $**, the numbers $ 2m_k + 1 $ and $ 2n_k + 1 $ are relatively prime.

---

Let’s denote:

$$
a_k = 2m_k + 1, \quad b_k = 2n_k + 1
$$

Then from the recurrence:

$$
\frac{m_k}{n_k} = \frac{a_{k-1}}{b_{k-1}} \Rightarrow \frac{a_k - 1}{2} / \frac{b_k - 1}{2} = \frac{a_{k-1}}{b_{k-1}} \Rightarrow \frac{a_k - 1}{b_k - 1} = \frac{a_{k-1}}{b_{k-1}}
$$

So:

$$
(a_k - 1) b_{k-1} = (b_k - 1) a_{k-1}
\Rightarrow a_k b_{k-1} - b_{k-1} = b_k a_{k-1} - a_{k-1}
\Rightarrow a_k b_{k-1} - b_k a_{k-1} = b_{k-1} - a_{k-1}
$$

This seems messy. Let's try a different approach.

---

## Key Idea: Track the GCDs

Define:

$$
g_k = \gcd(a_k, b_k) = \gcd(2m_k + 1, 2n_k + 1)
$$

We want to show that $ g_k = 1 $ for all sufficiently large $ k $.

Note that by definition of $ m_k, n_k $, they are obtained by reducing $ \frac{a_{k-1}}{b_{k-1}} $, so:

$$
m_k = \frac{a_{k-1}}{d_k}, \quad n_k = \frac{b_{k-1}}{d_k}, \quad \text{where } d_k = \gcd(a_{k-1}, b_{k-1}) = g_{k-1}
$$

Therefore:

$$
a_k = 2m_k + 1 = 2 \cdot \frac{a_{k-1}}{g_{k-1}} + 1 = \frac{2a_{k-1}}{g_{k-1}} + 1
$$
$$
b_k = 2n_k + 1 = \frac{2b_{k-1}}{g_{k-1}} + 1
$$

So we have the recurrence:

$$
a_k = \frac{2a_{k-1}}{g_{k-1}} + 1, \quad b_k = \frac{2b_{k-1}}{g_{k-1}} + 1
$$

and $ g_k = \gcd(a_k, b_k) $

---

## Step 1: Show that $ g_k $ divides some fixed number eventually?

Suppose $ p $ is a prime dividing $ g_k $ for infinitely many $ k $. We will derive a contradiction or show this can only happen finitely often.

Assume $ p \mid g_k = \gcd(a_k, b_k) $. Then $ p \mid a_k $ and $ p \mid b_k $.

From above:

$$
a_k = \frac{2a_{k-1}}{g_{k-1}} + 1, \quad b_k = \frac{2b_{k-1}}{g_{k-1}} + 1
$$

So modulo $ p $:

$$
0 \equiv \frac{2a_{k-1}}{g_{k-1}} + 1 \pmod{p}, \quad 0 \equiv \frac{2b_{k-1}}{g_{k-1}} + 1 \pmod{p}
$$

Thus:

$$
\frac{2a_{k-1}}{g_{k-1}} \equiv -1 \pmod{p}, \quad \frac{2b_{k-1}}{g_{k-1}} \equiv -1 \pmod{p}
\Rightarrow \frac{2a_{k-1}}{g_{k-1}} \equiv \frac{2b_{k-1}}{g_{k-1}} \pmod{p}
\Rightarrow 2a_{k-1} \equiv 2b_{k-1} \pmod{p g_{k-1}}? 
$$

Wait — better to multiply both sides by $ g_{k-1} $:

Since $ g_{k-1} \mid a_{k-1} $ and $ g_{k-1} \mid b_{k-1} $, let’s write:

Let $ a_{k-1} = g_{k-1} \cdot x_{k-1} $, $ b_{k-1} = g_{k-1} \cdot y_{k-1} $, with $ \gcd(x_{k-1}, y_{k-1}) = 1 $.

Then:

$$
a_k = 2x_{k-1} + 1, \quad b_k = 2y_{k-1} + 1
$$

And $ g_k = \gcd(2x_{k-1} + 1, 2y_{k-1} + 1) $

But note: since $ \gcd(x_{k-1}, y_{k-1}) = 1 $, what can we say about $ \gcd(2x_{k-1}+1, 2y_{k-1}+1) $?

Let $ d = \gcd(2x_{k-1}+1, 2y_{k-1}+1) $. Then $ d \mid (2x_{k-1}+1) $ and $ d \mid (2y_{k-1}+1) $, so:

$$
d \mid [2x_{k-1} + 1 - (2y_{k-1} + 1)] = 2(x_{k-1} - y_{k-1})
$$

Also, $ d \mid 2x_{k-1} + 1 $, so if $ d $ is odd (which it must be, since $ 2x_{k-1}+1 $ is odd), then $ d \mid x_{k-1} - y_{k-1} $.

Moreover, since $ d \mid 2x_{k-1} + 1 $ and $ d \mid x_{k-1} - y_{k-1} $, then:

Let’s suppose $ d > 1 $. Then there exists an odd prime $ p \mid d $, so:

$$
2x_{k-1} \equiv -1 \pmod{p}, \quad 2y_{k-1} \equiv -1 \pmod{p}
\Rightarrow x_{k-1} \equiv y_{k-1} \pmod{p}
$$

So $ p \mid x_{k-1} - y_{k-1} $, and also $ p \mid 2x_{k-1} + 1 $.

Now, recall that $ x_{k-1} = a_{k-1}/g_{k-1} $, $ y_{k-1} = b_{k-1}/g_{k-1} $, and $ \gcd(x_{k-1}, y_{k-1}) = 1 $.

So if $ p \mid x_{k-1} - y_{k-1} $ and $ p \mid 2x_{k-1} + 1 $, then:

From $ x_{k-1} \equiv y_{k-1} \pmod{p} $, and $ \gcd(x_{k-1}, y_{k-1}) = 1 $, we cannot have $ p \mid x_{k-1} $ and $ p \mid y_{k-1} $, unless $ p=1 $, which is impossible.

Actually, since $ \gcd(x_{k-1}, y_{k-1}) = 1 $, any common divisor of $ x_{k-1} - y_{k-1} $ and $ x_{k-1} $ would divide $ y_{k-1} $, hence divide 1. So $ \gcd(x_{k-1}, x_{k-1} - y_{k-1}) = \gcd(x_{k-1}, y_{k-1}) = 1 $.

Similarly, $ \gcd(y_{k-1}, x_{k-1} - y_{k-1}) = 1 $.

But here, $ p \mid x_{k-1} - y_{k-1} $ and $ p \mid 2x_{k-1} + 1 $. Since $ p \nmid x_{k-1} $ (because otherwise $ p \mid y_{k-1} $, contradicting coprimality), we can solve:

From $ 2x_{k-1} \equiv -1 \pmod{p} $, we get $ x_{k-1} \equiv -2^{-1} \pmod{p} $, and similarly $ y_{k-1} \equiv -2^{-1} \pmod{p} $, so indeed $ x_{k-1} \equiv y_{k-1} \pmod{p} $, consistent.

The key point is: **if $ p \mid g_k $, then $ p \mid 2x_{k-1} + 1 $ and $ p \mid 2y_{k-1} + 1 $, and $ x_{k-1} \equiv y_{k-1} \pmod{p} $, and $ \gcd(x_{k-1}, y_{k-1}) = 1 $.**

This implies that $ p $ does not divide $ x_{k-1} $ or $ y_{k-1} $, and in fact, $ x_{k-1} \not\equiv 0 \pmod{p} $, etc.

---

## Step 2: Use descent or boundedness

Let’s consider the sequence $ g_k = \gcd(a_k, b_k) $. Suppose $ g_k > 1 $ for infinitely many $ k $. Then there is a prime $ p $ that divides $ g_k $ for infinitely many $ k $.

Fix such a prime $ p $. For each such $ k $, we have:

$$
a_k \equiv 0 \pmod{p}, \quad b_k \equiv 0 \pmod{p}
\Rightarrow \frac{2a_{k-1}}{g_{k-1}} + 1 \equiv 0 \pmod{p}, \quad \frac{2b_{k-1}}{g_{k-1}} + 1 \equiv 0 \pmod{p}
$$

As before, this implies:

$$
\frac{2a_{k-1}}{g_{k-1}} \equiv -1 \pmod{p}, \quad \frac{2b_{k-1}}{g_{k-1}} \equiv -1 \pmod{p}
\Rightarrow \frac{2a_{k-1}}{g_{k-1}} \equiv \frac{2b_{k-1}}{g_{k-1}} \pmod{p}
\Rightarrow 2a_{k-1} \equiv 2b_{k-1} \pmod{p g_{k-1}}? 
$$

Better: Multiply both sides by $ g_{k-1} $:

$$
2a_{k-1} \equiv -g_{k-1} \pmod{p g_{k-1}}, \quad 2b_{k-1} \equiv -g_{k-1} \pmod{p g_{k-1}}
$$

Wait — actually, since $ g_{k-1} \mid a_{k-1} $ and $ g_{k-1} \mid b_{k-1} $, let’s write $ a_{k-1} = g_{k-1} x_{k-1} $, $ b_{k-1} = g_{k-1} y_{k-1} $, with $ \gcd(x_{k-1}, y_{k-1}) = 1 $.

Then:

$$
a_k = 2x_{k-1} + 1, \quad b_k = 2y_{k-1} + 1
$$

So $ p \mid 2x_{k-1} + 1 $ and $ p \mid 2y_{k-1} + 1 $, so:

$$
2x_{k-1} \equiv -1 \pmod{p}, \quad 2y_{k-1} \equiv -1 \pmod{p}
\Rightarrow x_{k-1} \equiv y_{k-1} \pmod{p}
$$

Let $ z_{k-1} = x_{k-1} \equiv y_{k-1} \pmod{p} $. Then $ 2z_{k-1} \equiv -1 \pmod{p} $, so $ z_{k-1} \equiv -2^{-1} \pmod{p} $.

Now, since $ \gcd(x_{k-1}, y_{k-1}) = 1 $, and $ x_{k-1} \equiv y_{k-1} \pmod{p} $, then $ p \nmid x_{k-1} $, because if $ p \mid x_{k-1} $, then $ p \mid y_{k-1} $, contradiction.

So $ x_{k-1} \not\equiv 0 \pmod{p} $, and same for $ y_{k-1} $.

Now, look at the next step:

$$
a_{k+1} = 2x_k + 1, \quad b_{k+1} = 2y_k + 1, \quad \text{where } x_k = \frac{a_k}{g_k}, y_k = \frac{b_k}{g_k}
$$

But $ a_k = 2x_{k-1} + 1 $, $ b_k = 2y_{k-1} + 1 $, and $ g_k = \gcd(a_k, b_k) $, which is divisible by $ p $.

So $ x_k = \frac{2x_{k-1} + 1}{g_k} $, $ y_k = \frac{2y_{k-1} + 1}{g_k} $

Since $ p \mid g_k $, and $ p \mid 2x_{k-1} + 1 $, then $ x_k $ is an integer, and modulo $ p $:

$$
x_k = \frac{2x_{k-1} + 1}{g_k} \equiv \frac{0}{0} \pmod{p}? 
$$

Not helpful. Instead, think about the size.

---

## Step 3: Growth argument

Note that $ a_k = 2x_{k-1} + 1 $, and $ x_{k-1} = a_{k-1}/g_{k-1} \geq a_{k-1}/a_{k-1} = 1 $, but more importantly, since $ g_{k-1} \geq 1 $, we have $ x_{k-1} \leq a_{k-1} $, so $ a_k = 2x_{k-1} + 1 \leq 2a_{k-1} + 1 $.

But if $ g_{k-1} > 1 $, then $ x_{k-1} < a_{k-1} $, so $ a_k < 2a_{k-1} + 1 $, but still grows roughly exponentially if $ g_{k-1} = 1 $.

However, if $ g_k > 1 $ frequently, then $ a_k $ and $ b_k $ grow slower.

But here’s the crucial observation:

Each time $ g_k > 1 $, we are “removing” a common factor from $ a_{k-1}, b_{k-1} $, and then forming new values $ a_k = 2x_{k-1} + 1 $, $ b_k = 2y_{k-1} + 1 $, where $ x_{k-1}, y_{k-1} $ are coprime.

Now, suppose that for some $ k $, $ g_k = d > 1 $. Then $ d \mid a_k = 2x_{k-1} + 1 $, $ d \mid b_k = 2y_{k-1} + 1 $, and as shown, $ x_{k-1} \equiv y_{k-1} \pmod{d} $, and $ \gcd(x_{k-1}, y_{k-1}) = 1 $.

Now, consider the value $ |x_{k-1} - y_{k-1}| $. Since $ x_{k-1} \equiv y_{k-1} \pmod{d} $, we have $ d \mid |x_{k-1} - y_{k-1}| $.

But $ \gcd(x_{k-1}, y_{k-1}) = 1 $, so $ \gcd(x_{k-1}, x_{k-1} - y_{k-1}) = \gcd(x_{k-1}, y_{k-1}) = 1 $, similarly for $ y_{k-1} $.

Therefore, $ d $ must be coprime to both $ x_{k-1} $ and $ y_{k-1} $, and divides their difference.

Now, here’s the key: **the set of possible primes $ p $ that can divide any $ g_k $ is finite.**

Why? Because each such prime $ p $ must satisfy that for some $ k $, $ p \mid 2x_{k-1} + 1 $ and $ p \mid 2y_{k-1} + 1 $, with $ x_{k-1} \equiv y_{k-1} \pmod{p} $, and $ \gcd(x_{k-1}, y_{k-1}) = 1 $.

But $ x_{k-1} $ and $ y_{k-1} $ are determined by the initial $ m_0, n_0 $ through a deterministic process. In particular, the entire sequence $ (a_k, b_k) $ is determined by $ (m_0, n_0) $, and thus the set of primes that ever divide any $ g_k $ is contained in the set of prime divisors of numbers appearing in the sequence $ a_k, b_k $, which are generated from $ m_0, n_0 $ via linear fractional transformations.

But more concretely: suppose $ p \mid g_k $ for some $ k $. Then as above, $ p \mid 2x_{k-1} + 1 $, and $ x_{k-1} = a_{k-1}/g_{k-1} $, which is an integer derived from previous steps.

In fact, we can trace back: each $ x_j $ is of the form $ \frac{2x_{j-1} + 1}{g_j} $, starting from $ x_0 = m_0 $, $ y_0 = n_0 $.

So the values $ x_k, y_k $ are rational numbers that become integers after division by gcds, but ultimately, they are built from $ m_0, n_0 $ using operations like $ x \mapsto \frac{2x + 1}{d} $, where $ d $ divides $ 2x + 1 $ and the corresponding $ y $-value.

The important point is that **each time a prime $ p $ divides $ g_k $, it must divide $ 2x_{k-1} + 1 $, and $ x_{k-1} $ is a rational number whose numerator and denominator are bounded in terms of the initial data and the number of steps**.

But perhaps a simpler way:

---

## Final Argument: Only finitely many primes can divide any $ g_k $

Suppose that infinitely many $ k $ have $ g_k > 1 $. Then there is a prime $ p $ that divides $ g_k $ for infinitely many $ k $.

For each such $ k $, we have:

$$
p \mid 2x_{k-1} + 1, \quad p \mid 2y_{k-1} + 1, \quad x_{k-1} \equiv y_{k-1} \pmod{p}, \quad \gcd(x_{k-1}, y_{k-1}) = 1
$$

As established, this implies $ x_{k-1} \equiv y_{k-1} \equiv -2^{-1} \pmod{p} $.

Now, consider the sequence $ x_k, y_k $. They are defined recursively by:

$$
x_k = \frac{2x_{k-1} + 1}{g_k}, \quad y_k = \frac{2y_{k-1} + 1}{g_k}
$$

with $ g_k = \gcd(2x_{k-1} + 1, 2y_{k-1} + 1) $.

If $ p \mid g_k $, then $ x_k = \frac{2x_{k-1} + 1}{g_k} $, and since $ p \mid 2x_{k-1} + 1 $, and $ p \mid g_k $, then $ x_k $ is an integer, and modulo $ p $:

$$
x_k = \frac{2x_{k-1} + 1}{g_k} \equiv \frac{0}{0} \pmod{p}
$$

Not useful. But notice that $ x_k $ and $ y_k $ are getting smaller when $ g_k > 1 $, because we're dividing by $ g_k \geq p \geq 2 $.

Specifically, if $ g_k \geq 2 $, then $ x_k = \frac{2x_{k-1} + 1}{g_k} \leq \frac{2x_{k-1} + 1}{2} < x_{k-1} + \frac{1}{2} $, so if $ x_{k-1} \geq 1 $, then $ x_k \leq x_{k-1} $, and strictly less if $ g_k > 1 $.

Similarly for $ y_k $.

Therefore, the sequences $ x_k, y_k $ are non-increasing whenever $ g_k > 1 $, and since they are positive integers, they can decrease only finitely many times.

Hence, $ g_k > 1 $ can occur only finitely many times!

Because each time $ g_k > 1 $, we have $ x_k < x_{k-1} $ (since $ g_k \geq 2 $, and $ 2x_{k-1} + 1 \geq 3 $, so $ x_k \leq \lfloor (2x_{k-1} + 1)/2 \rfloor \leq x_{k-1} $, and equality only if $ 2x_{k-1} + 1 = 2x_{k-1} $, impossible; actually, $ x_k \leq x_{k-1} $, and strict inequality if $ g_k > 1 $).

More precisely:

$$
x_k = \frac{2x_{k-1} + 1}{g_k} \leq \frac{2x_{k-1} + 1}{2} = x_{k-1} + \frac{1}{2} - \frac{1}{2} + \frac{1}{2} wait no:

\frac{2x_{k-1} + 1}{2} = x_{k-1} + \frac{1}{2}

So if $ g_k \geq 2 $, then $ x_k \leq x_{k-1} + \frac{1}{2} $, but since $ x_k $ is integer, $ x_k \leq x_{k-1} $.

And equality holds only if $ \frac{2x_{k-1} + 1}{g_k} = x_{k-1} $, i.e., $ 2x_{k-1} + 1 = g_k x_{k-1} \Rightarrow g_k = 2 + \frac{1}{x_{k-1}} $, which is not integer unless $ x_{k-1} = 1 $, then $ g_k = 3 $.

So if $ x_{k-1} = 1 $, $ g_k = 3 $, then $ x_k = (2*1 + 1)/3 = 1 $, so stays the same.

Otherwise, if $ x_{k-1} > 1 $, and $ g_k \geq 2 $, then $ x_k \leq \frac{2x_{k-1} + 1}{2} < x_{k-1} + 0.5 $, so since integer, $ x_k \leq x_{k-1} $, and if $ g_k > 2 $, then $ x_k < x_{k-1} $.

Even if $ g_k = 2 $, $ x_k = \frac{2x_{k-1} + 1}{2} $, which is not integer unless $ 2x_{k-1} + 1 $ even, i.e., $ x_{k-1} $ half-integer, but $ x_{k-1} $ is integer, so $ 2x_{k-1} + 1 $ is odd, so $ g_k $ cannot be 2! Because $ a_k = 2x_{k-1} + 1 $ is always odd, so $ g_k = \gcd(a_k, b_k) $ is always odd.

Ah! Important point: $ a_k = 2m_k + 1 $ is always odd, similarly $ b_k $ is always odd, so $ g_k = \gcd(a_k, b_k) $ is always **odd**.

Therefore, $ g_k \geq 1 $, and if $ g_k > 1 $, then $ g_k \geq 3 $.

So if $ g_k \geq 3 $, then:

$$
x_k = \frac{2x_{k-1} + 1}{g_k} \leq \frac{2x_{k-1} + 1}{3} < x_{k-1} \quad \text{for } x_{k-1} \geq 1
$$

Check: $ \frac{2x + 1}{3} < x \iff 2x + 1 < 3x \iff 1 < x $, so for $ x_{k-1} \geq 2 $, we have $ x_k < x_{k-1} $.

If $ x_{k-1} = 1 $, then $ x_k = \frac{2*1 + 1}{g_k} = \frac{3}{g_k} $, and since $ g_k \geq 3 $, $ x_k \leq 1 $. If $ g_k = 3 $, $ x_k = 1 $; if $ g_k > 3 $, $ x_k < 1 $, impossible since $ x_k $ positive integer. So only possibility is $ g_k = 3 $, $ x_k = 1 $.

Similarly for $ y_k $.

Therefore, the only way $ x_k $ doesn't decrease is if $ x_{k-1} = 1 $ and $ g_k = 3 $, giving $ x_k = 1 $.

Same for $ y_k $.

But since $ \gcd(x_{k-1}, y_{k-1}) = 1 $, if $ x_{k-1} = 1 $, then $ y_{k-1} $ can be anything coprime to 1, i.e., any integer.

But if $ x_{k-1} = 1 $, $ y_{k-1} = c $, with $ \gcd(1,c)=1 $, then $ a_k = 2*1 + 1 = 3 $, $ b_k = 2c + 1 $, and $ g_k = \gcd(3, 2c+1) $.

This is 3 if $ 2c+1 \equiv 0 \pmod{3} $, i.e., $ c \equiv 1 \pmod{3} $, else 1.

So if $ c \equiv 1 \pmod{3} $, then $ g_k = 3 $, and $ x_k = 3/3 = 1 $, $ y_k = (2c+1)/3 $.

Then next step: $ x_k = 1 $, $ y_k = d = (2c+1)/3 $, and we repeat.

But now, $ y_k = d $, and if $ d > 1 $, and if later $ g_{k+1} > 1 $, then $ y_{k+1} = \frac{2d + 1}{g_{k+1}} \leq \frac{2d+1}{3} < d $ if $ d \geq 2 $.

So unless $ d = 1 $, it decreases.

Eventually, since $ x_k $ and $ y_k $ are positive integers, and they can stay constant only if they are 1 and the gcd is exactly 3, but even then, $ y_k $ may change.

In any case, the pair $ (x_k, y_k) $ can only take on finitely many values before either becoming (1,1) or decreasing further.

But if $ x_k = y_k = 1 $, then $ a_k = 3 $, $ b_k = 3 $, $ g_k = 3 $, then $ x_{k+1} = 3/3 = 1 $, $ y_{k+1} = 3/3 = 1 $, so it stabilizes at (1,1).

In this case, $ g_k = 3 $ for all subsequent $ k $, so $ 2m_k + 1 = a_k = 3 $, $ 2n_k + 1 = b_k = 3 $, so they are never relatively prime again.

But wait — the problem asks to prove that $ 2m_k + 1 $ and $ 2n_k + 1 $ are relatively prime for all but finitely many $ k $.

In this stabilization case, they are equal to 3 forever, so gcd is 3, not 1. So this would be a counterexample?

But the problem says "prove that ... for all but finitely many k", implying it's true.

What's wrong?

Ah! When $ x_k = y_k = 1 $, then $ m_k = x_k = 1 $, $ n_k = y_k = 1 $, but the problem states that $ m_0, n_0 $ are **distinct** positive integers.

Does the recurrence preserve distinctness?

Initially, $ m_0 \neq n_0 $.

At step 1: $ \frac{m_1}{n_1} = \frac{2m_0 + 1}{2n_0 + 1} $, reduced.

Could $ m_1 = n_1 $? Only if $ 2m_0 + 1 = 2n_0 + 1 $, i.e., $ m_0 = n_0 $, contradiction.

So $ m_1 \neq n_1 $.

Similarly, at each step, $ \frac{m_k}{n_k} = \frac{2m_{k-1} + 1}{2n_{k-1} + 1} $, and since $ m_{k-1} \neq n_{k-1} $, the fraction is not 1, so $ m_k \neq n_k $.

Therefore, $ x_k = m_k $, $ y_k = n_k $, and $ x_k \neq y_k $ for all k.

In particular, we can never have $ x_k = y_k = 1 $, because that would imply $ m_k = n_k = 1 $, contradiction.

So the stabilization at (1,1) is impossible.

Therefore, the sequences $ x_k, y_k $ are always distinct positive integers, and whenever $ g_k > 1 $, we have $ x_k < x_{k-1} $ or $ y_k < y_{k-1} $, and since they are positive integers, this can happen only finitely many times.

More precisely, define $ s_k = x_k + y_k $. Each time $ g_k > 1 $, since $ g_k \geq 3 $, and $ x_k = \frac{2x_{k-1} + 1}{g_k} \leq \frac{2x_{k-1} + 1}{3} $, similarly for $ y_k $, so:

$$
s_k = x_k + y_k \leq \frac{2x_{k-1} + 1}{3} + \frac{2y_{k-1} + 1}{3} = \frac{2(x_{k-1} + y_{k-1}) + 2}{3} = \frac{2s_{k-1} + 2}{3}
$$

Now, $ \frac{2s + 2}{3} < s $ when $ 2s + 2 < 3s \iff 2 < s $.

So if $ s_{k-1} > 2 $, then $ s_k < s_{k-1} $.

If $ s_{k-1} = 2 $, then $ x_{k-1} + y_{k-1} = 2 $, and since $ x_{k-1}, y_{k-1} \geq 1 $, and distinct (because $ m_{k-1} \neq n_{k-1} $), so possibilities: (1,1) but not allowed since not distinct, or (1,1) is the only solution to sum 2, but they must be distinct, so impossible. Minimum sum for distinct positive integers is 1+2=3.

So $ s_{k-1} \geq 3 $, and $ \frac{2s_{k-1} + 2}{3} < s_{k-1} $ for $ s_{k-1} > 2 $, which is always true.

Indeed, $ \frac{2s + 2}{3} < s \iff 2s + 2 < 3s \iff s > 2 $, which holds.

Moreover, $ s_k \leq \frac{2s_{k-1} + 2}{3} < s_{k-1} $, and since $ s_k $ is a positive integer, it decreases by at least 1 each time $ g_k > 1 $.

Therefore, $ g_k > 1 $ can occur only finitely many times, specifically, at most $ s_0 - 1 $ times, where $ s_0 = m_0 + n_0 $.

After that, for all larger $ k $, $ g_k = 1 $, meaning $ \gcd(2m_k + 1, 2n_k + 1) = 1 $.

---

## Conclusion

We have shown that the sum $ s_k = m_k + n_k $ (or rather $ x_k + y_k $, but since $ m_k = x_k $, $ n_k = y_k $ in our notation) decreases whenever $ g_k > 1 $, and since it starts at $ m_0 + n_0 \geq 1 + 2 = 3 $ (as distinct positives), and decreases by at least 1 each time $ g_k > 1 $, it can happen only finitely many times.

Therefore, for all but finitely many $ k $, $ g_k = 1 $, i.e., $ \gcd(2m_k + 1, 2n_k + 1) = 1 $.

✅ **Proved.**

---

**Final Answer:**

$$
\boxed{\text{For all but finitely many positive integers } k, \text{ the integers } 2m_k + 1 \text{ and } 2n_k + 1 \text{ are relatively prime.}}
$$


## Lucas's Theorem

Lucas's theorem, proved by Édouard Lucas in 1878, gives a way to compute a binomial coefficient modulo a prime $$p$$ using only the base-$$p$$ digits of the two numbers. [arxiv](https://arxiv.org/abs/1409.3820)

**Statement.** Let $$p$$ be prime, and let the base-$$p$$ expansions of $$m$$ and $$n$$ be

$$
m = m_k p^k + \cdots + m_1 p + m_0, \quad n = n_k p^k + \cdots + n_1 p + n_0.
$$

Then

$$
\binom{m}{n} \equiv \prod_{i=0}^{k} \binom{m_i}{n_i} \pmod{p},
$$

with the convention that $$\binom{a}{b}=0$$ when $$b>a$$ .

In words: to find $$\binom{m}{n} \bmod p$$, write $$m$$ and $$n$$ in base $$p$$, then multiply together the small binomial coefficients formed by corresponding digit pairs.

### Key Consequence

$$\binom{m}{n}$$ is divisible by $$p$$ **if and only if** at least one base-$$p$$ digit of $$n$$ is greater than the corresponding digit of $$m$$ . Equivalently (by Kummer's theorem), $$\binom{m}{n}$$ is *not* divisible by $$p$$ exactly when adding $$n$$ and $$m-n$$ in base $$p$$ produces no carries. [neelmishra.github](https://neelmishra.github.io/blog/cp/number-theory-2/lucas-theorem.html)

A useful corollary: in row $$m$$ of Pascal's triangle, the number of entries not divisible by $$p$$ equals $$\prod_{i=0}^{k}(m_i+1)$$. [math.hmc](https://math.hmc.edu/funfacts/lucas-theorem/)

### Why It Matters

- **Computation**: For large $$m,n$$ with small prime $$p$$, it reduces $$\binom{m}{n}\bmod p$$ to $$O(\log_p m)$$ small binomials, each computable in $$O(p)$$ time — a standard trick in competitive programming. [neelmishra.github](https://neelmishra.github.io/blog/cp/number-theory-2/lucas-theorem.html)
- **Combinatorics**: It reveals the fractal structure of Pascal's triangle modulo a prime (the basis of the Sierpiński triangle pattern).
- **Cryptography**: Useful for efficient modular arithmetic over prime fields. [medium](https://medium.com/@adrikapanwar2004/lucass-theorem-b587b47ef2af)

It also generalizes to prime powers via Granville's and Davis–Webb extensions, and has deep connections to $$p$$-adic analysis. [arxiv](https://arxiv.org/abs/1409.3820)

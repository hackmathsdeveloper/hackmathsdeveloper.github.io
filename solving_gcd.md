
Let $m_0$ and $n_0$ be distinct positive integers. For every positive integer $k$, define $m_k$ and $n_k$ to be the relatively prime positive integers such that

$$\frac{m_k}{n_k} = \frac{2m_{k-1} + 1}{2n_{k-1} + 1}.$$

Prove that $2m_k + 1$ and $2n_k + 1$ are relatively prime for all but finitely many positive integers $k$.

## Solution

For every $k \ge 0$, write
$$g_k := \gcd(2m_k+1,\; 2n_k+1).$$
We must show $g_k = 1$ for all but finitely many $k$.

**Claim 1: $m_k \neq n_k$ for all $k$.**
If $m_k = n_k$ for some $k \ge 1$, then $2m_{k-1}+1 = 2n_{k-1}+1$, hence $m_{k-1}=n_{k-1}$; descending step by step gives $m_0 = n_0$, contradicting the hypothesis. $\checkmark$

**Claim 2: For $k\ge 1$, $\;2m_{k-1}+1 = g_{k-1}m_k$ and $2n_{k-1}+1 = g_{k-1}n_k$.**
Let $A = 2m_{k-1}+1$, $B = 2n_{k-1}+1$, so $\gcd(A/g_{k-1},\, B/g_{k-1}) = 1$ and $\frac{m_k}{n_k} = \frac{A/g_{k-1}}{B/g_{k-1}}$. A positive rational has a **unique** representation as a fraction of coprime positive integers (if $mB' = nA'$ with both pairs coprime, then $A' \mid m$ and $B' \mid n$, forcing equality). Hence $m_k = A/g_{k-1}$, $n_k = B/g_{k-1}$. $\checkmark$

**Claim 3: Each $g_k$ is odd**, since it divides the odd number $2m_k+1$. $\checkmark$

## The key identity

Subtracting the two equations of Claim 2 gives, for all $k \ge 1$:
$$2(m_{k-1}-n_{k-1}) = g_{k-1}(m_k - n_k).$$
Iterating this relation yields, for every $k \ge 1$:
$$2^k (m_0 - n_0) = \big(g_0 g_1 \cdots g_{k-1}\big)(m_k - n_k). \qquad (\ast)$$

## Bounding the product of the $g_i$

Let $G_k := g_0 g_1 \cdots g_{k-1}$. By $(\ast)$ and Claim 1, $m_k - n_k$ is a **nonzero integer**, so
$$G_k \mid 2^k (m_0 - n_0).$$
By Claim 3, $G_k$ is odd; hence (Gauss's lemma, since $\gcd(G_k, 2^k)=1$)
$$G_k \mid m_0 - n_0 \qquad \Longrightarrow \qquad G_k \le |m_0 - n_0| \quad \text{for all } k. \qquad (\ast\ast)$$

## Conclusion

Each $g_i$ is an odd positive integer, so either $g_i = 1$ or $g_i \ge 3$. Suppose $g_i \ge 3$ for $r$ distinct indices $i < k$. Then by $(\ast\ast)$,
$$3^r \le G_k \le |m_0 - n_0| \qquad \Longrightarrow \qquad r \le \log_3 |m_0 - n_0|.$$

Thus $g_i > 1$ can happen for **at most** $\lfloor \log_3 |m_0-n_0| \rfloor$ indices $i$ — in particular, only finitely many. For every other positive integer $k$,
$$\gcd(2m_k+1,\; 2n_k+1) = g_k = 1,$$
which is exactly what we had to prove. $\blacksquare$

## Remark (the bound is sharp in spirit)

Exceptions really can occur, but only finitely many: e.g. $m_0 = 4$, $n_0 = 13$ gives $2m_0+1 = 9$, $2n_0+1 = 27$, so $g_0 = 9$; then $(m_1,n_1) = (1,3)$, and thereafter $(3,7),(7,15),(15,31),\dots$ with $g_k = 1$ for all $k \ge 1$. The mechanism of the proof is visible here: $m_0-n_0 = -9$ is exactly $G_1(m_1-n_1)/2 = 9\cdot(-2)/2$, and the odd part of $m_0-n_0$ is "used up" by the factors $g_i$, which forces $g_i=1$ eventually.



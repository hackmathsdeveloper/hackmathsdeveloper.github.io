
Here are 10 more useful properties relating $$\gcd$$ and $$\operatorname{lcm}$$:

1. **Divisibility order.**  
   $$
   \gcd(a,b)\mid a,\; \gcd(a,b)\mid b,\qquad a\mid \operatorname{lcm}(a,b),\; b\mid \operatorname{lcm}(a,b).
   $$

2. **Characterization by maximality/minimality.**  
   $$\gcd(a,b)$$ is the largest integer dividing both $$a$$ and $$b$$, while $$\operatorname{lcm}(a,b)$$ is the smallest integer divisible by both.

3. **Coprime criterion.**  
   $$
   \gcd(a,b)=1 \iff \operatorname{lcm}(a,b)=ab.
   $$

4. **Equality criterion.**  
   $$
   \gcd(a,b)=a \iff a\mid b,\qquad \operatorname{lcm}(a,b)=a \iff b\mid a.
   $$

5. **Bounds.**  
   $$
   \gcd(a,b)\le \min(a,b),\qquad \operatorname{lcm}(a,b)\ge \max(a,b).
   $$

6. **Product relation.**  
   $$
   \gcd(a,b)\operatorname{lcm}(a,b)=ab.
   $$

7. **Prime-power behavior.**  
   If $$a=p^\alpha$$ and $$b=p^\beta$$, then
   $$
   \gcd(a,b)=p^{\min(\alpha,\beta)},\qquad \operatorname{lcm}(a,b)=p^{\max(\alpha,\beta)}.
   $$

8. **Scaling law.**  
   For any positive integer $$k$$,
   $$
   \gcd(ka,kb)=k\gcd(a,b),\qquad \operatorname{lcm}(ka,kb)=k\operatorname{lcm}(a,b).
   $$

9. **Absorption identities.**  
   $$
   \gcd(a,\operatorname{lcm}(a,b))=a,\qquad \operatorname{lcm}(a,\gcd(a,b))=a.
   $$

10. **Monotonicity under divisibility.**  
   If $$a\mid c$$ and $$b\mid d$$, then
   $$
   \gcd(a,b)\mid \gcd(c,d),\qquad \operatorname{lcm}(a,b)\mid \operatorname{lcm}(c,d).
   $$


Based on the content of Henri Cohen's "Explicit Methods for Solving Diophantine Equations" lecture notes, here are 20 similar questions covering local methods, factorization, descent techniques, elliptic curves, and computational approaches.

### **Local Methods & Hensel’s Lemma**

1.  **Local Solubility of Fermat’s Quartic:** Determine the conditions on an integer $c$ such that the equation $x^4 + y^4 = c z^4$ has a non-trivial solution in $\mathbb{Q}_p$ for $p=2$ and for odd primes $p \nmid 2c$. Specifically, explain the role of Jacobi sums when $p \equiv 3 \pmod 4$.
2.  **Hensel’s Lemma Application:** Let $f(X) \in \mathbb{Z}_p[X]$. Suppose $\alpha \in \mathbb{Z}_p$ satisfies $v_p(f(\alpha)) \geq 1$ and $v_p(f'(\alpha)) = 0$. Prove that there exists a unique root $\alpha^* \in \mathbb{Z}_p$ such that $f(\alpha^*) = 0$ and $v_p(\alpha^* - \alpha) \geq 1$. How does this change if $v_p(f'(\alpha)) > 0$?
3.  **Strassmann’s Theorem:** Consider the power series $f(X) = \sum_{n \geq 0} a_n X^n$ with coefficients in $\mathbb{Q}_p$ converging for $|X|_p \leq 1$. If $N$ is the largest index such that $|a_N|_p = \max_n |a_n|_p$, prove that $f(X)$ has exactly $N$ zeros in $\mathbb{Z}_p$ (counting multiplicities). Apply this to show that $x^3 + 6y^3 = 1$ has only the trivial solution $(1,0)$ in integers by analyzing the expansion in $\mathbb{Q}_3$.
4.  **First Case of FLT:** State Wieferich’s criterion for the first case of Fermat’s Last Theorem. Show that if $2^{p-1} \not\equiv 1 \pmod{p^2}$, then FLT I holds for prime $p$. Verify this condition for $p=1093$ and $p=3511$.

### **Factorization & Classical Criteria**

5.  **Wendt’s Criterion:** Let $p$ be an odd prime and $q = kp + 1$ be a prime. Define the resultant $R(X^k - 1, (X+1)^k - 1)$. Prove that if $q \nmid R(X^k - 1, (X+1)^k - 1)$, then the first case of Fermat’s Last Theorem holds for $p$. Why is the condition $q \nmid xyz$ crucial in the proof?
6.  **Sophie Germain Primes:** Using Wendt’s criterion with $k=2$, show that if $q = 2p + 1$ is prime, then FLT I is true for $p$. Explain why this provides a simple infinite family of primes satisfying the first case of FLT.
7.  **Mordell Equations:** Consider the equation $y^2 = x^3 + t$. Prove that if $t = 8a^3 - b^2$ is squarefree and $3 \nmid b$, then the equation has no integral solutions. Apply this to show that $y^2 = x^3 + 7$ has no integer solutions.
8.  **Runge’s Method:** Explain the principle behind Runge’s method for solving Diophantine equations of the form $P(x,y)=0$ where the highest degree terms factor into coprime polynomials over $\mathbb{Q}$. Apply this to find all integer solutions to $y^2 = x^4 + x^3 + x^2 + x + 1$.

### **Catalan’s Equation & Baker’s Method**

9.  **Catalan’s Conjecture (Lebesgue’s Case):** Prove that the equation $x^m - y^n = 1$ has no solutions in positive integers for $m=2$ and $n > 2$ except for the known small cases. Use factorization in $\mathbb{Z}[i]$ or $\mathbb{Z}[\sqrt{-2}]$ as appropriate.
10. **Analytic Lemmas for Catalan:** Let $p$ and $q$ be distinct odd primes. Using the analytic lemma that $(a^q + 1)^p < (a^p + 1)^q$ for $a \geq 1$, show that if $x^p - y^q = 1$ with $p < q$, then $x-1$ must be a perfect $q$-th power. Derive a lower bound for $y$ in terms of $p$ and $q$.
11. **Lower Bounds via Linear Forms in Logarithms:** In the context of Catalan’s equation $x^p - y^q = 1$, explain how Baker’s theory of linear forms in logarithms provides an effective upper bound for the exponents $p$ and $q$. Why was this method insufficient to fully resolve Catalan’s conjecture before Mihăilescu’s proof?

### **Descent Methods on Elliptic Curves**

12. **2-Descent Setup:** Let $E: y^2 = x^3 + ax + b$ be an elliptic curve over $\mathbb{Q}$. Describe the 2-descent map $\alpha: E(\mathbb{Q})/2E(\mathbb{Q}) \to \mathbb{Q}^*/\mathbb{Q}^{*2}$. How does one compute the Selmer group $S_2(E)$ using the homogeneous spaces $y^2 = Q_i(x)$?
13. **Obstruction to Local Solubility:** In the context of 2-descent, explain the relationship between the Tate-Shafarevich group $\text{Ш}(E/\mathbb{Q})[2]$ and the failure of the local-global principle for the quartic equations arising from the descent. Give an example where a curve is everywhere locally soluble but has no rational points.
14. **3-Descent on Cubic Curves:** Consider the diagonal cubic curve $ax^3 + by^3 + cz^3 = 0$. Construct the 3-descent map $\alpha: E(\mathbb{Q}) \to \mathbb{Q}^*/\mathbb{Q}^{*3}$ associated with the isogeny defined by the point $T=(0, \sqrt[3]{abc})$. What condition on $a,b,c$ ensures that the image of $\alpha$ contains $b/c$?
15. **Computing Rational Points via Descent:** Given the curve $x^3 + 55y^3 + 66z^3 = 0$, use the 3-descent method to determine if it has non-trivial rational points. Specifically, calculate the images of the generators of $E(\mathbb{Q})/3E(\mathbb{Q})$ and check if $b/c$ lies in the span of these images modulo cubes.

### **L-functions & Heegner Points**

16. **Birch and Swinnerton-Dyer Conjecture:** State the BSD conjecture relating the rank of $E(\mathbb{Q})$ to the order of vanishing of $L(E,s)$ at $s=1$. If $L(E,1) \neq 0$, what does Kolyvagin-Rubin theory imply about the rank of $E(\mathbb{Q})$?
17. **Heegner Point Construction:** Let $E$ be an elliptic curve of conductor $N$ and $K = \mathbb{Q}(\sqrt{-D})$ be an imaginary quadratic field. Define a Heegner point of level $N$ and discriminant $-D$. Explain how the modular parametrization $\phi: X_0(N) \to E$ maps these points to $E(H)$, where $H$ is the Hilbert class field of $K$.
18. **Gross-Zagier Formula:** Explain the significance of the Gross-Zagier formula in computing the height of Heegner points. How does this formula allow one to construct a nontorsion rational point on $E(\mathbb{Q})$ when $L'(E,1) \neq 0$?
19. **Congruent Number Problem:** Relate the congruent number problem to the elliptic curve $E_n: y^2 = x^3 - n^2x$. Show that $n$ is a congruent number if and only if $E_n(\mathbb{Q})$ has positive rank. Use Tunnell’s theorem to give a criterion for determining if $n$ is congruent assuming the BSD conjecture.

### **Integral Points & Computational Techniques**

20. **Elliptic Logarithms and LLL:** Describe the method for computing all integral points on an elliptic curve $E(\mathbb{Z})$ using elliptic logarithms. How does one use David’s bounds to get an initial upper bound $H$ for the coefficients of the generators, and how is the LLL algorithm used to reduce this bound to a computationally feasible size? Illustrate with the curve $y^2 + y = x^3 - 7x + 6$.

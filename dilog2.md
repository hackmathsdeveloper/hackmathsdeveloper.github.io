
Given the series for the Dilogarithm function:

$$ \text{Li}_2(x) = x + \frac{x^2}{2^2} + \frac{x^3}{3^2} + \frac{x^4}{4^2} + \dots $$
*(where the left side is the integral of $\frac{-\ln(1-x)}{x}$)*

**Step 1: Divide both sides by $x$**

Dividing every term by $x$ shifts the powers down by one again:

$$ \frac{\text{Li}_2(x)}{x} = 1 + \frac{x}{2^2} + \frac{x^2}{3^2} + \frac{x^3}{4^2} + \dots $$

In summation notation:
$$ \frac{\text{Li}_2(x)}{x} = \sum_{n=0}^{\infty} \frac{x^n}{(n+1)^2} $$

**Step 2: Integrate both sides with respect to $x$ one more time**

**Left Side Integration:**
We need to find $\int \frac{\text{Li}_2(x)}{x} \, dx$. 
By the definition of polylogarithms, the integral of $\frac{\text{Li}_s(x)}{x}$ is $\text{Li}_{s+1}(x)$. Therefore, integrating the dilogarithm divided by $x$ gives us the **Trilogarithm**, denoted as $\text{Li}_3(x)$:
$$ \int \frac{\text{Li}_2(x)}{x} \, dx = \text{Li}_3(x) + C $$
*(Assuming $C=0$ so the sum is 0 at $x=0$)*.

**Right Side Integration (Term by Term):**
Using the power rule $\int x^n \, dx = \frac{x^{n+1}}{n+1}$ once more:

*   $\int 1 \, dx = x$
*   $\int \frac{x}{2^2} \, dx = \frac{x^2}{2^2 \cdot 2} = \frac{x^2}{2^3}$
*   $\int \frac{x^2}{3^2} \, dx = \frac{x^3}{3^2 \cdot 3} = \frac{x^3}{3^3}$
*   $\int \frac{x^3}{4^2} \, dx = \frac{x^4}{4^2 \cdot 4} = \frac{x^4}{4^3}$
*   ...and so on.

**The Resulting Series**

Equating the two sides gives us the series expansion for the Trilogarithm function:

$$ \text{Li}_3(x) = x + \frac{x^2}{2^3} + \frac{x^3}{3^3} + \frac{x^4}{4^3} + \dots $$

In summation notation:
$$ \text{Li}_3(x) = \sum_{n=1}^{\infty} \frac{x^n}{n^3} \quad \text{for } |x| < 1 $$

***

**The Pattern Emerges**
You can see a beautiful pattern forming from our repeated operations of integrating and dividing by $x$:

1.  **Start:** $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$
2.  **Integrate:** $-\ln(1-x) = \sum_{n=1}^{\infty} \frac{x^n}{n^1}$
3.  **Divide by $x$, Integrate:** $\text{Li}_2(x) = \sum_{n=1}^{\infty} \frac{x^n}{n^2}$
4.  **Divide by $x$, Integrate:** $\text{Li}_3(x) = \sum_{n=1}^{\infty} \frac{x^n}{n^3}$

If you were to continue this process $k$ times, you would generate the general **Polylogarithm** function of order $k$:
$$ \text{Li}_k(x) = \sum_{n=1}^{\infty} \frac{x^n}{n^k} $$

Just like the previous step, evaluating this at $x=1$ yields famous mathematical constants. For $k=3$, it gives Apéry's constant:
$$ \text{Li}_3(1) = 1 + \frac{1}{8} + \frac{1}{27} + \frac{1}{64} + \dots = \zeta(3) \approx 1.202 $$
*(where $\zeta$ is the Riemann zeta function).*

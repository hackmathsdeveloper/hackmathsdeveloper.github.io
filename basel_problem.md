
Based on the image provided, here is the detailed step-by-step derivation of the sum of the squares of the reciprocals of integers (also known as the solution to the Basel Problem), as solved by Leonhard Euler.

### Step 1: The Taylor Series Expansion
First, we start with the function $\sin(x)$. The Taylor series expansion for $\sin(x)$ around $x=0$ is:
$$ \sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots $$

To make this easier to work with, we divide the entire equation by $x$:
$$ \frac{\sin(x)}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!} + \dots $$

Recall that $3! = 3 \times 2 \times 1 = 6$. So, we can rewrite the equation as:
$$ \frac{\sin(x)}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \dots $$

### Step 2: Finding the Roots
Next, we look for the roots (zeros) of the function $\frac{\sin(x)}{x}$.
The function $\sin(x) = 0$ whenever $x$ is a multiple of $\pi$.
So, the roots are:
$$ x = \pm \pi, \pm 2\pi, \pm 3\pi, \dots $$

Note that at $x=0$, the limit of $\frac{\sin(x)}{x}$ is 1, so $x=0$ is not a root.

### Step 3: Factoring the Expression
Euler had a brilliant insight: he treated this infinite series like a giant polynomial.
According to the Fundamental Theorem of Algebra, if a polynomial $P(x)$ has roots $r_1, r_2, r_3 \dots$, it can be factored as:
$$ P(x) = k(x - r_1)(x - r_2)(x - r_3)\dots $$

Since our roots are $\pm \pi, \pm 2\pi, \pm 3\pi \dots$, we can pair the positive and negative roots together to form difference of squares terms: $(x - n\pi)(x + n\pi) = (x^2 - n^2\pi^2)$.

To match the constant term of "1" from our Taylor series in Step 1, we normalize the factors. The factored form looks like this:
$$ \frac{\sin(x)}{x} = \left(1 - \frac{x^2}{\pi^2}\right) \left(1 - \frac{x^2}{(2\pi)^2}\right) \left(1 - \frac{x^2}{(3\pi)^2}\right) \dots $$

Simplifying the denominators:
$$ \frac{\sin(x)}{x} = \left(1 - \frac{x^2}{\pi^2}\right) \left(1 - \frac{x^2}{4\pi^2}\right) \left(1 - \frac{x^2}{9\pi^2}\right) \dots $$

### Step 4: Comparing Coefficients
Now we have two different expressions for the exact same function $\frac{\sin(x)}{x}$.
1.  **The Series:** $1 - \frac{1}{6}x^2 + \dots$
2.  **The Factored Product:** $\left(1 - \frac{x^2}{\pi^2}\right) \left(1 - \frac{x^2}{4\pi^2}\right) \dots$

If we multiply out the factored product, we only care about the $x^2$ term. When you expand a product like $(1-a)(1-b)(1-c)\dots$, the term with the single power (in this case $x^2$) is simply the negative sum of the individual parts: $-(a + b + c + \dots)$.

So, the $x^2$ term from the factored side is:
$$ - \left( \frac{1}{\pi^2} + \frac{1}{4\pi^2} + \frac{1}{9\pi^2} + \dots \right) x^2 $$

We equate this to the $x^2$ coefficient from the Taylor series (Step 1), which was $-\frac{1}{6}$.

$$ -\frac{1}{6} = - \left( \frac{1}{\pi^2} + \frac{1}{4\pi^2} + \frac{1}{9\pi^2} + \dots \right) $$

### Step 5: Isolating the Sum
Now, we just do some algebra to solve for the sum.

1.  Multiply both sides by $-1$:
    $$ \frac{1}{6} = \frac{1}{\pi^2} + \frac{1}{4\pi^2} + \frac{1}{9\pi^2} + \dots $$

2.  Factor out $\frac{1}{\pi^2}$ on the right side:
    $$ \frac{1}{6} = \frac{1}{\pi^2} \left( 1 + \frac{1}{4} + \frac{1}{9} + \dots \right) $$

3.  Recognize that the terms inside the parenthesis are $\frac{1}{n^2}$:
    $$ \frac{1}{6} = \frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2} $$

4.  Multiply both sides by $\pi^2$ to isolate the sum:
    $$ \frac{\pi^2}{6} = \sum_{n=1}^{\infty} \frac{1}{n^2} $$

**Final Result:**
$$ 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots = \frac{\pi^2}{6} $$

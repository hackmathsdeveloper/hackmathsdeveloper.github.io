
Euler’s Gamma function is a solution to the problem “find a *continuous* function on \((0,\infty)\) that equals \((n-1)!\) at each positive integer \(n\) and satisfies the same recursion as the factorial.” In this precise sense it is a continuous (and in fact analytic) extension of the factorial, and Euler was the first to construct it in the 18th century. [britannica](https://www.britannica.com/science/gamma-function)

***

## The interpolation problem Euler was solving

The starting point is the discrete factorial function  
\[
n! = 1\cdot 2\cdot 3\cdots n,\quad n\in\mathbb{N}.
\]  
This is only defined on integers, but people (Goldbach, Bernoulli, Stirling) asked: can we find a function \(F(x)\) on positive real \(x\) such that \(F(n) = n!\) for all positive integers \(n\)? [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)

Euler’s version of the question is: find a “nice” function \(F(x)\) of a real (later complex) variable such that  

- \(F(n) = (n-1)!\) or \(F(n+1) = n!\) for all natural numbers \(n\), and  
- it satisfies the *same* recurrence as the factorial: \(F(x+1) = xF(x)\). [ms.uky](https://www.ms.uky.edu/~droyster/courses/fall06/PDFs/AppendixF.pdf)

This is an interpolation problem: extend a discrete sequence to a continuous function in a canonical way. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)

***

## Euler’s construction and modern definition

Euler ultimately arrived at the integral (for \(\text{Re}(z)>0\))  
\[
\Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t}\,dt,
\]  
now called Euler’s integral of the second kind. [britannica](https://www.britannica.com/science/gamma-function)

Two key facts link this to factorials:

1. **Functional equation** via integration by parts  
   Compute  
   \[
   \Gamma(z+1) = \int_0^\infty t^{z} e^{-t}dt.
   \]  
   Integrating by parts with \(u=t^z\), \(dv=e^{-t}dt\) gives  
   \[
   \Gamma(z+1) = z\Gamma(z),
   \]  
   exactly mirroring the factorial identity \((n+1)! = (n+1)\cdot n!\). [ms.uky](https://www.ms.uky.edu/~droyster/courses/fall06/PDFs/AppendixF.pdf)

2. **Agreement on integers**  
   Plugging \(z=1\) into the integral gives \(\Gamma(1)=1\). [britannica](https://www.britannica.com/science/gamma-function)
   Then apply the functional equation repeatedly:
   \[
   \Gamma(2) = 1\cdot \Gamma(1)=1!,\quad
   \Gamma(3) = 2\cdot \Gamma(2)=2!,\quad \dots
   \]  
   So in general \(\Gamma(n) = (n-1)!\) for \(n\in\mathbb{N}\). [ms.uky](https://www.ms.uky.edu/~droyster/courses/fall06/PDFs/AppendixF.pdf)

Thus, \(\Gamma\) is *by construction* a function on a continuous domain (initially \(z>0\), later \(\text{Re}(z)>0\), then all of \(\mathbb{C}\) minus poles) that coincides with factorials on integers and satisfies the same recursion. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)

***

## Why “continuous version” is more than just a slogan

Saying “Gamma is the continuous version of factorial” is not just heuristic; it can be made precise in several ways:

- **Exact interpolation:**  
  \(\Gamma\) is continuous (even analytic) on \((0,\infty)\) and matches \((n-1)!\) at every integer \(n\). This gives a unique smooth curve passing through all factorial values if you also require log-convexity and the standard normalization. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)

- **Bohr–Mollerup characterization:**  
  On \((0,\infty)\), \(\Gamma\) is the *only* function \(f\) such that  
  1. \(f(1)=1\),  
  2. \(f(x+1) = x f(x)\) for all \(x>0\), and  
  3. \(\log f(x)\) is convex. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)
  This uniqueness theorem explains why Gamma is the canonical extension: among all possible interpolants of the factorial sequence, Gamma is distinguished by a natural convexity property.

- **Analytic extension to complex plane:**  
  The integral defines an analytic function on \(\text{Re}(z)>0\); analytic continuation then extends \(\Gamma\) meromorphically to \(\mathbb{C}\) with simple poles at non-positive integers. [ms.uky](https://www.ms.uky.edu/~droyster/courses/fall06/PDFs/AppendixF.pdf)
  So “continuous” is actually an understatement: on its domain of holomorphy, Gamma is as smooth as one can ask—complex analytic.

- **Preserves factorial structure:**  
  Gamma respects all the algebraic structure of factorials (recurrence, multiplicative relationships, Stirling-type asymptotics), but now for non-integer and complex arguments. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)

***

## Euler’s role and historical context

Historically, the Gamma function emerged directly from attempts by Euler and others to interpolate the factorial. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)

- Euler discussed the factorial interpolation problem in correspondence, notably in a 1729 letter to Goldbach, and proposed expressions that effectively converge to what we now call the Gamma function. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/gamma-function)
- Euler initially gave a product form for what we now call \(\Gamma(z)\): a limit of expressions involving \(n! n^{z}/[z(z+1)\cdots(z+n)]\), and only later did the integral representation become standard. [ms.uky](https://www.ms.uky.edu/~droyster/courses/fall06/PDFs/AppendixF.pdf)
- The symbol \(\Gamma\) was introduced later by Legendre; Euler himself used other notations for these “Eulerian functions.” [dam.brown](https://www.dam.brown.edu/fractional_calculus/documents/TheEulerianFunctions.pdf)

So saying “Gamma function is the continuous version of the factorial, as invented by Euler” is historically accurate: Euler created a function that solved the factorial interpolation problem; later mathematicians formalized it into the modern Gamma function framework and notation. [britannica](https://www.britannica.com/science/gamma-function)

***

## Concrete example: non-integer factorial via Gamma

A nice illustration of “continuous factorial” is \((1/2)!\).  

Using the Gamma–factorial link, we interpret  
\[
\left(\tfrac{1}{2}\right)! := \Gamma\!\left(\tfrac{3}{2}\right).
\]  
Then  
\[
\Gamma\!\left(\tfrac{3}{2}\right) = \tfrac{1}{2}\Gamma\!\left(\tfrac{1}{2}\right) = \tfrac{1}{2}\sqrt{\pi},
\]  
so \((1/2)! = \sqrt{\pi}/2\). [britannica](https://www.britannica.com/science/gamma-function)

This gives a perfectly consistent meaning to factorial at a non-integer argument and fits smoothly with the entire “continuous curve” determined by Gamma.

***

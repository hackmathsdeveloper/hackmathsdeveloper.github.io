
A meromorphic function is, roughly, a complex function that is holomorphic everywhere except at isolated points where it is allowed to blow up like a pole (but not behave more wildly). [mathworld.wolfram](https://mathworld.wolfram.com/MeromorphicFunction.html)

***

## Core definition

Formally:

- Let \(U\subset\mathbb{C}\) be an open set.  
- A function \(f:U\to\mathbb{C}\) is **meromorphic on \(U\)** if:
  - \(f\) is holomorphic on \(U\setminus S\) for some discrete set \(S\subset U\), and  
  - Each point \(a\in S\) is a **pole** of finite order for \(f\) (no essential singularities). [math.libretexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/09:_Residue_Theorem/9.02:_Holomorphic_and_Meromorphic_Functions)

Equivalently, on one complex variable:

- Locally near every point (including poles), you can write \(f(z)=\dfrac{g(z)}{h(z)}\) where \(g,h\) are holomorphic and \(h\) is not identically zero. [sciencedirect](https://www.sciencedirect.com/topics/mathematics/meromorphic-function)
- Or: a meromorphic function on a Riemann surface is just a holomorphic map into the Riemann sphere \(\widehat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}\); poles are the points where the value is \(\infty\). [ncatlab](https://ncatlab.org/nlab/show/meromorphic+function)

***

## Intuitive picture

You can think of meromorphic functions as “holomorphic except for a controlled set of blow‑ups”:

- At ordinary points, they look like convergent power series.  
- At poles, they look like a finite principal part plus a regular part:
  \[
  f(z)=\frac{a_{-m}}{(z-a)^m}+\dots+\frac{a_{-1}}{z-a}+a_0+a_1(z-a)+\dots
  \]
  with \(a_{-m}\neq 0\). [en.wikipedia](https://en.wikipedia.org/wiki/Meromorphic_function)

In contrast, an essential singularity (like \(e^{1/z}\) at \(0\)) is not allowed for a meromorphic function; near such a point the behavior is too chaotic (Casorati–Weierstrass). [mathworld.wolfram](https://mathworld.wolfram.com/MeromorphicFunction.html)

***

## Examples

- \(f(z)=\dfrac{1}{z}\) is meromorphic on \(\mathbb{C}\) with a simple pole at \(0\). [en.wikipedia](https://en.wikipedia.org/wiki/Meromorphic_function)
- Any rational function \(f(z)=\dfrac{P(z)}{Q(z)}\) with polynomials \(P,Q\) is meromorphic on \(\mathbb{C}\), with poles at the zeros of \(Q\). [sciencedirect](https://www.sciencedirect.com/topics/mathematics/meromorphic-function)
- The gamma function \(\Gamma(z)\) is meromorphic on \(\mathbb{C}\) with simple poles at \(z=0,-1,-2,\dots\). [statisticshowto](https://www.statisticshowto.com/meromorphic-function-definition/)
- Elliptic functions (like Weierstrass \(\wp\)) are meromorphic and doubly periodic on \(\mathbb{C}\). [en.wikipedia](https://en.wikipedia.org/wiki/Elliptic_function)


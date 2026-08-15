
The video develops the prime–zeta connection from elementary prime counting to Riemann’s explicit formula and the Riemann Hypothesis. Below is an ordered transcription-based inventory of the equations and concepts, with standard mathematical notation used to make the spoken expressions precise. [youtube](https://www.youtube.com/watch?v=yCZgKep5iBc)

## 1. Primes and their density

| Order | Concept / equation |
|---|---|
| 1 | **Prime numbers:** integers \(>1\) with only \(1\) and themselves as positive divisors. |
| 2 | **Fundamental factorization idea:** every integer \(n>1\) factors into primes; examples: \(522=2\cdot3^2\cdot29\), \(7{,}761=3\cdot13\cdot199\). |
| 3 | **Sieve of Eratosthenes:** iteratively remove multiples of \(2,3,5,7,\ldots\); the survivors are primes. |
| 4 | **Prime-counting function:** \(\pi(x)=\#\{p\le x:p\text{ prime}\}\). Examples: \(\pi(10)=4\), \(\pi(100)=25\). |
| 5 | \(\pi(x)\) is a staircase: it jumps by \(1\) at each prime and is constant between primes. |
| 6 | **Prime density up to \(x\):** \(\pi(x)/x\). The falling ratio indicates that primes thin out. |
| 7 | **Average prime spacing:** \(x/\pi(x)\). This increases slowly with \(x\). |
| 8 | Heuristic observation: \(\frac{x}{\pi(x)}\approx\log x\), equivalently \(\pi(x)\approx\frac{x}{\log x}\). |
| 9 | **Prime Number Theorem:** \[\pi(x)\sim\frac{x}{\log x},\qquad\text{i.e.}\qquad\lim_{x\to\infty}\frac{\pi(x)}{x/\log x}=1.\] |
| 10 | **Logarithmic integral:** \[\operatorname{Li}(x)=\int_2^x\frac{dt}{\log t}.\] It is presented as a substantially better smooth approximation to \(\pi(x)\) than \(x/\log x\). |

The presentation emphasizes that these approximations describe the *average* distribution of primes but do not recover the individual jumps of the prime-counting staircase. [youtube](https://www.youtube.com/watch?v=yCZgKep5iBc)

## 2. Zeta function and Euler product

| Order | Concept / equation |
|---|---|
| 11 | **Riemann zeta function:** \[\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}=1+\frac1{2^s}+\frac1{3^s}+\cdots.\] |
| 12 | Special case—the Basel sum: \[\zeta(2)=\sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{6}.\] |
| 13 | Euler’s “sieving” of the zeta series: multiplying by \(1-2^{-s}\), then \(1-3^{-s}\), etc., removes terms whose denominators are divisible by the corresponding prime. |
| 14 | **Euler product formula:** \[\zeta(s)=\prod_{p}\left(1-\frac1{p^s}\right)^{-1},\] where the product runs over all primes \(p\). |
| 15 | The conceptual bridge: unique prime factorization is encoded analytically in \(\zeta(s)\). |
| 16 | Taking logarithms converts the product into a prime sum: \[\log\zeta(s)=-\sum_p\log(1-p^{-s}).\] |
| 17 | Logarithmic power series: \[-\log(1-u)=u+\frac{u^2}{2}+\frac{u^3}{3}+\cdots=\sum_{m\ge1}\frac{u^m}{m}.\] |
| 18 | With \(u=p^{-s}\): \[\log\zeta(s)=\sum_p\sum_{m\ge1}\frac{1}{m\,p^{ms}}.\] |
| 19 | Interpretation: the logarithm of \(\zeta\) sees not merely primes but all **prime powers** \(p^m\), with weight \(1/m\). |

This is the key transition: \(\zeta(s)\) encodes multiplicative prime factorization, while \(\log\zeta(s)\) exposes a weighted enumeration of prime powers. [youtube](https://www.youtube.com/watch?v=yCZgKep5iBc)

## 3. Weighted prime-power counting

| Order | Concept / equation |
|---|---|
| 20 | **Riemann’s weighted prime-power counting function:** \[J(x)=\sum_{\substack{p^m\le x\\m\ge1}}\frac1m.\] |
| 21 | Weight rule: \(p\) contributes \(1\), \(p^2\) contributes \(1/2\), \(p^3\) contributes \(1/3\), etc. |
| 22 | Example: \[J(10)=4+\frac12+\frac12+\frac13=\frac{16}{3}.\] The terms are \(2,3,5,7\), then \(4=2^2\), \(9=3^2\), and \(8=2^3\). |
| 23 | Example: \[J(100)=25+4\left(\frac12\right)+2\left(\frac13\right)+2\left(\frac14\right)+\frac15+\frac16=\frac{428}{15}.\] |
| 24 | \(J(x)\) is another staircase. Unlike \(\pi(x)\), it jumps at every prime power, and its jump heights decrease as \(1/m\). |
| 25 | Relation between the two counting functions: \[J(x)=\sum_{m\ge1}\frac1m\,\pi\!\left(x^{1/m}\right).\] |
| 26 | Expanded form: \[J(x)=\pi(x)+\frac12\pi(\sqrt{x})+\frac13\pi(x^{1/3})+\frac14\pi(x^{1/4})+\cdots.\] |

Thus \(J(x)\) is the prime staircase plus all of its weighted “prime-power layers.” [youtube](https://www.youtube.com/watch?v=yCZgKep5iBc)

## 4. Möbius inversion

| Order | Concept / equation |
|---|---|
| 27 | **Möbius function:** \[\mu(n)=\begin{cases}1,&n=1,\\(-1)^k,&n\text{ is a product of }k\text{ distinct primes},\\0,&n\text{ has a repeated prime factor}.\end{cases}\] |
| 28 | Examples: \(\mu(2)=\mu(3)=\mu(5)=-1\); \(\mu(6)=\mu(10)=1\); \(\mu(4)=\mu(8)=\mu(9)=0\). |
| 29 | **Möbius inversion recovers ordinary prime counting:** \[\pi(x)=\sum_{m\ge1}\frac{\mu(m)}{m}J\!\left(x^{1/m}\right).\] |
| 30 | Initial terms: \[\pi(x)=J(x)-\frac12J(x^{1/2})-\frac13J(x^{1/3})-\frac15J(x^{1/5})+\frac16J(x^{1/6})-\cdots.\] |
| 31 | The \(m=4\) correction is absent because \(\mu(4)=0\). |
| 32 | Worked check at \(x=100\): \[\pi(100)=J(100)-\frac12J(10)-\frac13J(100^{1/3})-\frac15J(100^{1/5})+\frac16J(100^{1/6})=25.\] |

The point is that determining \(J(x)\) is enough: Möbius inversion then reconstructs the exact prime-counting function \(\pi(x)\).  [youtube](https://www.youtube.com/watch?v=yCZgKep5iBc)

## 5. Analytic reconstruction and zeros

The remainder of the presentation makes the analytic connection explicit: the double sum for \(\log\zeta(s)\) is re-expressed using the jump data of \(J(x)\), leading schematically to a Mellin/Stieltjes-transform relation of the form

\[
\log\zeta(s)
=\int_{1^-}^{\infty}x^{-s}\,dJ(x)
=s\int_1^\infty J(x)x^{-s-1}\,dx.
\]

The inverse transform is then represented by a complex contour integral,

\[
J(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}
\frac{\log\zeta(s)}{s}\,x^s\,ds,
\qquad c>1.
\]

The central concepts that follow are:

- **Analytic continuation** of \(\zeta(s)\): extending the zeta function beyond the initial convergent series region \(\Re(s)>1\).
- The **pole at \(s=1\)**: its contribution yields the leading smooth term \(\operatorname{Li}(x)\).
- **Trivial zeros:** \(\zeta(-2)=\zeta(-4)=\zeta(-6)=\cdots=0\).
- **Non-trivial zeros:** zeros \(\rho\) in the critical strip \(0<\Re(\rho)<1\).
- **Riemann’s explicit formula:** in schematic form, the weighted staircase is reconstructed from the main logarithmic-integral term plus oscillatory contributions from all non-trivial zeros,
  \[
  J(x)
  =
  \operatorname{Li}(x)
  -
  \sum_{\rho}\operatorname{Li}(x^\rho)
  +\text{terms from the trivial zeros and constants}.
  \]
- **Conjugate pairing of zeros:** a zero \(\rho=\beta+i\gamma\) is paired with \(\bar\rho=\beta-i\gamma\), making their combined contribution real and oscillatory.
- **Why zeros locate primes:** adding more zero contributions progressively restores the discontinuous, prime-power staircase from its smooth approximation.
- **Riemann Hypothesis:** every non-trivial zero satisfies
  \[
  \Re(\rho)=\frac12.
  \]
  Equivalently, every non-trivial zero has the form \(\rho=\frac12+i\gamma\).

The video’s culminating idea is that primes can be viewed as an interference pattern generated by the non-trivial zeros of \(\zeta(s)\): \(\operatorname{Li}(x)\) provides the average trend, while the zeros provide the oscillatory corrections that resolve the individual prime jumps.  [youtube](https://www.youtube.com/watch?v=yCZgKep5iBc)


The Hardy–Littlewood circle method is an analytic number theory technique for counting additive representations of integers (e.g., as sums of powers or primes) by analyzing exponential sums over the unit circle and splitting it into “major” and “minor” arcs. At a high level, you encode your counting function in a generating function, write its coefficients as a contour integral integral over \(|z|=1\), and then asymptotically evaluate that integral by approximating the integrand near rational points \(a/q\) (major arcs) and showing the remaining region is negligible (minor arcs). [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)  

## Core setup and idea

- Typical context: You want the number \(r_s(n)\) of representations of a large integer \(n\) in an additive form, such as \(n = x_1^k + \cdots + x_s^k\) (Waring) or \(n = p_1 + p_2 + p_3\) (Goldbach-type problems). [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)
- Encoding via generating function: You form a generating series
  \[
  f(\alpha) = \sum_{m} a(m) e(m\alpha),
  \]
  where \(a(m)\) is an indicator/weight for \(m\) lying in your base set (e.g. \(a(m)=1\) if \(m\) is a \(k\)-th power, or a prime, etc.), and \(e(t) = e^{2\pi i t}\). [simonrs](https://simonrs.com/eulercircle/irpw2023/grace-circlemethod-paper.pdf)
- Representation count as integral:
  \[
  r_s(n) = \int_0^1 f(\alpha)^s e(-n\alpha)\, d\alpha,
  \]
  which follows by expanding \(f(\alpha)^s\), integrating termwise, and using orthogonality of \(e(m\alpha)\). [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)

The method is essentially about obtaining an asymptotic for this integral by detailed control of \(f(\alpha)\) on subintervals of \([0,1]\). [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)

## Major and minor arcs

The key structural step is to decompose the unit interval (circle) into regions where \(f(\alpha)\) is “structured” vs “pseudorandom”. [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)

- Major arcs \(\mathfrak{M}\): Neighbourhoods of rationals \(a/q\) with small denominator \(q\), say \(q \le Q\), around points \(\alpha = a/q + \beta\) with \(|\beta|\) very small relative to \(1/q\). [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)  
  - On major arcs, \(f(\alpha)\) can often be approximated by a product of local factors, leading to explicit main-term constants (singular series and singular integral). [simonrs](https://simonrs.com/eulercircle/irpw2023/grace-circlemethod-paper.pdf)
- Minor arcs \(\mathfrak{m}\): The complement of \(\mathfrak{M}\), where \(\alpha\) is badly approximable by rationals with small denominator. [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)
  - On minor arcs, one typically proves nontrivial bounds showing \(f(\alpha)\) is small on average, so \(\int_{\mathfrak{m}} f(\alpha)^s e(-n\alpha)\, d\alpha\) is of smaller order than the main term. [simonrs](https://simonrs.com/eulercircle/irpw2023/grace-circlemethod-paper.pdf)

Formally,
\[
r_s(n) = \int_{\mathfrak{M}} f(\alpha)^s e(-n\alpha)\, d\alpha + \int_{\mathfrak{m}} f(\alpha)^s e(-n\alpha)\, d\alpha,
\]
and one shows the first integral gives an explicit asymptotic main term while the second is \(o(\text{main term})\). [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)

## Typical application pattern

A standard “circle method” argument (e.g., for Waring’s problem) follows a fairly rigid template. [math.purdue](https://www.math.purdue.edu/~twooley/2023ant/2023antnotes.pdf)

1. **Construct the generating function.**  
   For Waring-type problems,
   \[
   f(\alpha) = \sum_{1 \le x \le X} e(x^k \alpha),
   \]
   so
   \[
   r_s(n) = \int_0^1 f(\alpha)^s e(-n\alpha)\, d\alpha
   \]
   counts solutions of \(x_1^k + \cdots + x_s^k = n\) with \(1 \le x_i \le X\). [math.purdue](https://www.math.purdue.edu/~twooley/2023ant/2023antnotes.pdf)

2. **Major arc approximation.**  
   Near \(\alpha = a/q + \beta\) with small \(q\), you approximate
   \[
   f\!\left(\frac{a}{q} + \beta\right) \approx q^{-1} S(q,a) I(\beta),
   \]
   where \(S(q,a)\) is a complete exponential sum modulo \(q\) and \(I(\beta)\) is a local integral (e.g., \(\int_0^X e(t^k \beta)\, dt\)). [math.purdue](https://www.math.purdue.edu/~twooley/2023ant/2023antnotes.pdf)
   Plugging this into the integral over major arcs produces a factorisation
   \[
   \int_{\mathfrak{M}} f(\alpha)^s e(-n\alpha)\, d\alpha \approx \mathfrak{S}(n) \cdot \mathfrak{J}(n),
   \]
   where:
   - \(\mathfrak{S}(n)\) is the **singular series**, an Euler-product-like factor encoding all local congruence obstructions. [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)
   - \(\mathfrak{J}(n)\) is the **singular integral**, a continuous local density term coming from integrals like \(\int_0^\infty e(t^k \beta)\, dt\). [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)

3. **Minor arc bounds.**  
   On \(\mathfrak{m}\), one uses Weyl-type exponential sum estimates, van der Corput differencing, or Vinogradov mean value theorems to show
   \[
   |f(\alpha)| \ll X^{1-\delta}
   \]
   for some \(\delta>0\), leading to
   \[
   \left|\int_{\mathfrak{m}} f(\alpha)^s e(-n\alpha)\, d\alpha\right| \ll X^{s(1-\delta)} = o(\text{main term}),
   \]
   when \(s\) is large enough relative to \(k\). [math.purdue](https://www.math.purdue.edu/~twooley/2023ant/2023antnotes.pdf)

4. **Conclude asymptotic formulae.**  
   Combining the two parts yields an asymptotic
   \[
   r_s(n) \sim \mathfrak{S}(n) \mathfrak{J}(n)
   \]
   for large \(n\), often with explicit exponents and effective lower bounds on \(s\). [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)

This is the template behind results like “every sufficiently large integer is a sum of \(s\) \(k\)-th powers” with explicit \(s(k)\), and Vinogradov’s theorem on sums of three primes. [old.maa](https://old.maa.org/press/maa-reviews/the-hardy-littlewood-method)

## Singluar series and singular integral

The singular series and singular integral are the central structural objects produced by the method. [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)

- **Singular series \(\mathfrak{S}(n)\).**  
  - Arises from the arithmetic of complete exponential sums near each major arc:
    \[
    \mathfrak{S}(n) = \sum_{q=1}^{\infty} \sum_{\substack{a \bmod q\\ (a,q)=1}} q^{-s} S(q,a)^s e(-na/q),
    \]
    for an appropriate exponential sum \(S(q,a)\). [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)
  - Often factorises as an Euler product over primes and converges if local solubility conditions are satisfied. [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)
  - Non-vanishing of \(\mathfrak{S}(n)\) is equivalent to the absence of congruence obstructions.  

- **Singular integral \(\mathfrak{J}(n)\).**  
  - Comes from the local continuous approximation at each major arc, e.g.
    \[
    \mathfrak{J}(n) = \int_{\mathbb{R}} \left(\int_0^\infty e(t^k \beta)\, dt\right)^s e(-n\beta)\, d\beta.
    \]
  - Captures the “real” geometric density of representations. [terrytao.wordpress](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/)

This separation cleanly splits global behaviour into infinite local \(p\)-adic pieces and a real-analytic piece, mirroring the structure of many conjectures in arithmetic geometry. [en.wikipedia](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method)

## Classic results and modern refinements

Historically and technically, the circle method sits at the core of additive number theory. [old.maa](https://old.maa.org/press/maa-reviews/the-hardy-littlewood-method)

- Early history:
  - Hardy and Ramanujan used a precursor of the method (1918) for the partition function \(p(n)\). [math.purdue](https://www.math.purdue.edu/~twooley/2023ant/2023antnotes.pdf)
  - Hardy and Littlewood then systematized it, applying it to Waring’s problem and sums of squares, leading to the classic “Hardy–Littlewood method”. [cirmath.hypotheses](https://cirmath.hypotheses.org/files/2018/06/2018-05-28-Cirmath-Americas-Adrian-Rice.pdf)
- Vinogradov’s variant:
  - Vinogradov replaced infinite series by finite exponential sums over primes and adapted the method to establish results like “every sufficiently large odd integer is a sum of three primes”. [web.williams](https://web.williams.edu/Mathematics/sjmiller/public_html/BrownClasses/1/circlemethod.pdf)
  - This involves heavy exponential sum technology and is a template for many results about primes in additive configurations.  
- Modern developments:
  - Refinements of minor arc estimates (e.g., efficient congruencing, decoupling) significantly improved thresholds on the number of variables needed in Waring-type problems. [math.purdue](https://www.math.purdue.edu/~twooley/2023ant/2023antnotes.pdf)
  - The method has been adapted to more geometric contexts, such as counting rational points on varieties via circle method style integrals. [lsa.umich](https://lsa.umich.edu/content/dam/math-assets/reu-su22/reu-2022/Wang-Xun-REU2022.pdf)

For a modern exposition, standard references include Davenport’s *The Hardy–Littlewood Method* and many lecture notes such as Vaughan’s and more concise sets like Wooley’s or Verstraëte’s notes. [mathweb.ucsd](https://mathweb.ucsd.edu/~jverstra/hardy.pdf)

***

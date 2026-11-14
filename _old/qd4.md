
Yes—quadratic forms show up very naturally inside infinite series/products, integrals, and even in functionals built from derivatives, but the *quadratic form itself* is still a degree‑2 polynomial (or bilinear form) in whatever variables you are feeding into it. The “infinite” or “differential” structure typically comes from how you *sum*, *integrate*, or *index* those quadratic forms, not from redefining “quadratic form” to mean something non‑polynomial. [arxiv](https://arxiv.org/html/2503.11445v1)

***

## Quadratic forms inside infinite series

Lots of q‑series and theta functions are sums indexed by \(\mathbb Z^n\) with exponents given by quadratic forms: [qseries](https://qseries.org/fgarvan/quadformsconf/abstracts.pdf)

- Classical theta series:
  \[
  \theta_Q(z) \;=\; \sum_{x\in\mathbb Z^n} e^{2\pi i\, Q(x)\, z},
  \]
  where \(Q(x)=x^\mathsf{T}Ax\) is an integral quadratic form. [arxiv](https://arxiv.org/html/2503.11445v1)
- “Extended” binary quadratic forms in infinite sums:
  \[
  \sum_{x\in\mathbb Z^n} q^{Q(x)},\quad Q(x)=x^\mathsf{T}Ax+ b^\mathsf{T}x + c,
  \]
  which appear in product identities, covering systems, and theta‑product factorisations. [arxiv](https://arxiv.org/html/2503.11445v1)

Here the quadratic form is finite and polynomial; the infinitude is in the *index set* and the resulting series.  

***

## Quadratic forms in infinite products

Quadratic forms also appear in exponents of infinite products, especially in the theory of theta functions and partition‑type identities: [qseries](https://qseries.org/fgarvan/quadformsconf/abstracts.pdf)

- Products such as
  \[
  \prod_{x \in \mathbb Z^n} \Bigl(1 - q^{Q(x)}\Bigr),
  \]
  where again \(Q(x)\) is a fixed quadratic form, show up in identities relating theta functions and modular forms. [qseries](https://qseries.org/fgarvan/quadformsconf/abstracts.pdf)

The product is infinite; the dependence on the discrete index \(x\) is via a quadratic form. You still have a perfectly classical quadratic form on \(\mathbb Z^n\); you’re just using it to weight an infinite product.  

***

## Quadratic forms under integrals

In analysis and probability, one routinely integrates expressions built from quadratic forms: [sites.lsa.umich](https://sites.lsa.umich.edu/barvinok/wp-content/uploads/sites/1434/2025/05/barr.pdf)

- Gaussian integrals:
  \[
  \int_{\mathbb R^n} e^{-Q(x)}\,dx,\quad Q(x) = x^\mathsf{T}Ax\ \text{positive definite},
  \]
  are basic objects; the value is proportional to \((\det A)^{-1/2}\). [sites.lsa.umich](https://sites.lsa.umich.edu/barvinok/wp-content/uploads/sites/1434/2025/05/barr.pdf)
- More complicated integrals involving products of quadratic forms:
  \[
  \int_{\mathbb R^n} (1 + \omega q_1(x))\cdots(1 + \omega q_m(x)) e^{-\|x\|^2/2} \,dx,
  \]
  where each \(q_k\) is a quadratic form. [sites.lsa.umich](https://sites.lsa.umich.edu/barvinok/wp-content/uploads/sites/1434/2025/05/barr.pdf)

Again, the quadratic forms themselves are finite polynomials; the integral is where infinite‑dimensional “summing” (over a continuum) happens.  

***

## Quadratic *differential* forms and functionals

On manifolds or function spaces, you can build quadratic expressions involving derivatives—these are usually called **quadratic differential forms** or quadratic functionals, not quadratic forms in the strict linear‑algebra sense: [mathweb.ucsd](https://mathweb.ucsd.edu/~helton/MTNSHISTORY/CONTENTS/2004LEUVEN/CDROM/papers/11.pdf)

- On a curve \(x(t)\) in \(\mathbb R^n\), a quadratic differential form might look like
  \[
  \Phi(x,\dot x)\,dt = \dot x(t)^\mathsf{T} A\, \dot x(t)\,dt,
  \]
  which is quadratic in \(\dot x\). [math.rug](https://www.math.rug.nl/~trentelman/psfiles/QDF.pdf)
- Functionals in calculus of variations:
  \[
  \mathcal Q(w) = \int_{t_0}^{t_1} \big( \dot w(t)^\mathsf{T}A\,\dot w(t) \big)\, dt,
  \]
  are *integrals of quadratic forms in derivatives*. [mathweb.ucsd](https://mathweb.ucsd.edu/~helton/MTNSHISTORY/CONTENTS/2004LEUVEN/CDROM/papers/11.pdf)

Here the *integrand* is a quadratic form in the variables \((w,\dot w, \dots)\), and you integrate it to get a scalar. The object \(\mathcal Q\) is sometimes called a quadratic functional; it’s quadratic in the function \(w\) (in a suitable Banach/Hilbert space sense) but defined via an integral.  

So you can absolutely have:

- Infinite matrices defining “quadratic differential forms,” with only finitely many nonzero entries in each row/column. [math.rug](https://www.math.rug.nl/~trentelman/psfiles/QDF.pdf)
- Path‑independent integrals of quadratic differential forms under certain conditions. [mathweb.ucsd](https://mathweb.ucsd.edu/~helton/MTNSHISTORY/CONTENTS/2004LEUVEN/CDROM/papers/11.pdf)

These generalize the finite‑dimensional \(x^\mathsf{T}Ax\) picture to spaces of functions and their derivatives.  

***

## Quadratics vs “quadratic forms” on function spaces

If you move to an infinite‑dimensional vector space \(V\) (e.g. a function space), you can still define a **quadratic form** \(Q:V\to\mathbb R\) satisfying
\[
Q(v+w) = Q(v)+Q(w)+B(v,w),
\]
with \(B\) bilinear, so \(Q\) is “quadratic” in the functional‑analytic sense. [gauss.math.yale](https://gauss.math.yale.edu/~sr2532/forms.pdf)

Examples:

- On \(L^2\), 
  \[
  Q(f) = \int |f(x)|^2\,dx
  \]
  is a quadratic form with associated bilinear form \(\langle f,g\rangle = \int f\overline g\). [gauss.math.yale](https://gauss.math.yale.edu/~sr2532/forms.pdf)
- On a Sobolev space,
  \[
  Q(u) = \int \left(|\nabla u|^2 + V(x)|u|^2\right)\,dx
  \]
  is quadratic in \(u\) and its derivatives; this is the standard Dirichlet form for an elliptic operator. [math.berkeley](https://math.berkeley.edu/~tb65536/QuadraticForms.pdf)

These involve integrals and derivatives, but algebraically they are still quadratic forms on a vector space—just an infinite‑dimensional one.  

***

## Infinite series involving quadratic forms in the index

Lastly, you also see **infinite series of quadratic forms** (or with quadratic forms in the exponent) in analytic number theory: [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/2412.03350)

- Series of the type
  \[
  \sum_{x\in \mathbb Z^n} F\big(Q(x)\big),
  \]
  where \(F\) is some analytic function and \(Q\) is a fixed integral quadratic form, arise when counting lattice points on quadratic surfaces or analyzing theta functions. [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/2412.03350)

The infinite nature is in the summation, not in changing what “quadratic form” means.  

***

### TL;DR

- **Core notion**: a quadratic form is (by definition) a homogeneous polynomial of degree 2 (or equivalent bilinear form) on a vector space.  
- **Yes**: you can build infinite series, infinite products, integrals, and functionals in which quadratic forms appear in the exponent, integrand, or as the basic building block. [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/2412.03350)
- **Yes**: in infinite‑dimensional settings (function spaces), “quadratic forms” are typically integrals of expressions quadratic in the function and its derivatives; they’re sometimes called quadratic functionals or quadratic differential forms. [math.berkeley](https://math.berkeley.edu/~tb65536/QuadraticForms.pdf)

If you tell me whether you’re more interested in the functional‑analytic (Dirichlet forms, quadratic forms of operators) or the number‑theoretic (theta functions, q‑series) side, I can zero in with concrete examples in that domain.

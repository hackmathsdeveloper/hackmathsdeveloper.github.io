
Assuming you mean **Carl Gustav Jacob Jacobi’s contributions to integration** (rather than a particular “Jacobi integration method”), his work falls into several connected areas:

## 1. Elliptic integrals → elliptic functions

Jacobi’s central achievement was to **invert elliptic integrals**. For example,

\[
u=\int_0^z \frac{dt}{\sqrt{(1-t^2)(1-k^2t^2)}}
\]

defines an elliptic integral; Jacobi treated its inverse as a new function:

\[
z=\operatorname{sn}(u,k).
\]

This led to the Jacobi elliptic functions \(\operatorname{sn}\), \(\operatorname{cn}\), and \(\operatorname{dn}\), which generalize \(\sin\), \(\cos\), and related circular functions for nonlinear problems. They provide closed-form descriptions for many integrals involving square roots of cubic or quartic polynomials. [encyclopediaofmath](https://encyclopediaofmath.org/wiki/Jacobi_elliptic_functions)

## 2. Theta functions and transformations

Jacobi developed theta-function machinery that gives series representations and transformation laws for elliptic functions and integrals. This made their periodicity, addition formulas, and changes of modulus systematic, rather than a collection of special substitutions. His 1829 *Fundamenta nova theoriae functionum ellipticarum* was foundational to this theory. [en.wikipedia](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi)

## 3. Hyperelliptic and Abelian integrals

He extended the program beyond single elliptic integrals toward multivariable integrals on algebraic curves—what became the theory of **Abelian integrals** and inversion problems. This is historically tied to the Abel–Jacobi theorem and later Riemann-surface theory. [en.wikipedia](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi)

## 4. Jacobi’s last multiplier

For a first-order system

\[
\dot{x}_i=a_i(x_1,\ldots,x_n),
\]

a **Jacobi last multiplier** \(M\) satisfies

\[
\sum_{i=1}^{n}\frac{\partial(Ma_i)}{\partial x_i}=0.
\]

It functions like an integrating factor in multiple dimensions. If enough first integrals are known, the multiplier lets the remaining solution be obtained by a quadrature; ratios of two last multipliers are first integrals. It also links differential equations with variational mechanics: for suitable second-order ODEs, it can be used to construct a Lagrangian. [arxiv](https://arxiv.org/pdf/0809.0022.pdf)

## 5. Hamilton–Jacobi integration of mechanics

Jacobi transformed the integration of Hamilton’s canonical equations into solving one first-order PDE for Hamilton’s principal function \(S(q,t)\):

\[
H\!\left(q,\frac{\partial S}{\partial q},t\right)
+\frac{\partial S}{\partial t}=0.
\]

If one finds a **complete integral** \(S(q,\alpha,t)\), depending on enough independent constants \(\alpha_i\), then the original \(2n\)-dimensional canonical system can be integrated by differentiating \(S\) with respect to those constants and solving the resulting relations. [ntrs.nasa](https://ntrs.nasa.gov/api/citations/19660001927/downloads/19660001927.pdf)

For a time-independent Hamiltonian, separation commonly takes the form

\[
S(q,t)=W(q;\alpha)-Et,
\]

reducing the Hamilton–Jacobi PDE to the characteristic equation

\[
H\!\left(q,\frac{\partial W}{\partial q}\right)=E.
\]

## 6. Separation of variables and integrability

Jacobi systematically used coordinate systems in which the Hamilton–Jacobi equation separates, turning a coupled PDE into independent one-variable integrals. For integrable systems, this produces action-like quadratures and exposes conserved quantities; his work on geodesics on an ellipsoid is a classic example of this approach. His broader contributions include differential equations, variational calculus, and classical dynamics. [en.wikipedia](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi)

In short: **Jacobi’s integration work is about converting hard integrals or dynamical systems into invertible special functions, integrating factors/multipliers, separated quadratures, or a single generating-function PDE.**

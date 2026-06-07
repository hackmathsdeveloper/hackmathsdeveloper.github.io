
There are infinitely many quadratic forms, so you can’t literally list all examples; instead we describe the general form and key families of examples. Any homogeneous degree‑2 polynomial in \(n\) variables over a field (e.g. \(\mathbb R\), \(\mathbb Q\)) is a quadratic form. [en.wikipedia](https://en.wikipedia.org/wiki/Quadratic_form)

***

## General definition

A (real) quadratic form in \(n\) variables is a map
\[
Q:\mathbb R^n\to\mathbb R,\quad Q(x)=\sum_{i,j} a_{ij} x_i x_j,
\]
with \(a_{ij}=a_{ji}\). Equivalently, choose a symmetric matrix \(A\in M_n(\mathbb R)\) and write [rmi.tsu](https://rmi.tsu.ge/~kade/LecturesT.Kadeishvili/MathEconomics/Term3/Week3QuadraticLEC.pdf)
\[
Q(x)=x^\mathsf{T} A x.
\] [en.wikipedia](https://en.wikipedia.org/wiki/Quadratic_form)  

Over a given field, every choice of symmetric matrix \(A\) gives a quadratic form, and different \(A\) can give equivalent forms up to change of basis (congruence).  

***

## Canonical small‑dimensional examples

For 1–2 variables, you can see the variety of behavior explicitly: [en.wikipedia](https://en.wikipedia.org/wiki/Quadratic_form)

- \(Q(x)=ax^2\) in 1 variable (any \(a\in\mathbb R\)).  
- \(Q(x,y)=x^2+y^2\) (positive definite).  
- \(Q(x,y)=-x^2-y^2\) (negative definite).  
- \(Q(x,y)=x^2-y^2\) (indefinite).  
- \(Q(x,y)=(x-y)^2\) (positive semidefinite).  
- More generally \(Q(x,y)=ax^2+2bxy+cy^2\) with arbitrary \(a,b,c\in\mathbb R\). [rmi.tsu](https://rmi.tsu.ge/~kade/LecturesT.Kadeishvili/MathEconomics/Term3/Week3QuadraticLEC.pdf)

Every 2‑variable quadratic form over \(\mathbb R\) is equivalent, via an invertible linear change of variables, to one of:
\[
\lambda_1 u^2 + \lambda_2 v^2,\quad\text{with }\lambda_i\in\mathbb R.
\] [en.wikipedia](https://en.wikipedia.org/wiki/Quadratic_form)  

***

## Matrix representation and higher dimensions

In \(n\) variables with symmetric \(A\), diagonalization yields an orthogonal change of basis \(x = P y\) such that
\[
Q(x)=y^\mathsf{T} D y = \sum_{i=1}^n \lambda_i y_i^2,
\]
where \(\lambda_i\) are eigenvalues of \(A\). So, up to orthogonal equivalence, examples in \(\mathbb R^n\) reduce to sums of squares with coefficients: [math.libretexts](https://math.libretexts.org/Bookshelves/Linear_Algebra/Understanding_Linear_Algebra_(Austin)/07:_The_Spectral_Theorem_and_singular_value_decompositions/7.02:_Quadratic_forms)

- Positive definite: all \(\lambda_i>0\), e.g. \(x_1^2+\cdots+x_n^2\). [math.libretexts](https://math.libretexts.org/Bookshelves/Linear_Algebra/Linear_Algebra_with_Applications_(Nicholson)/08:_Orthogonality/8.09:_An_Application_to_Quadratic_Forms)
- Negative definite: all \(\lambda_i<0\), e.g. \(-x_1^2-\cdots-x_n^2\).  
- Indefinite: a mix of positive and negative coefficients, e.g. \(x_1^2+\cdots+x_p^2 - x_{p+1}^2-\cdots-x_{p+q}^2\).  
- Semidefinite: some \(\lambda_i=0\), e.g. \(x_1^2+x_2^2\) in \(\mathbb R^3\) ignoring \(x_3\). [math.libretexts](https://math.libretexts.org/Bookshelves/Linear_Algebra/Linear_Algebra_with_Applications_(Nicholson)/08:_Orthogonality/8.09:_An_Application_to_Quadratic_Forms)

***

## Classification up to change of basis (real case)

Over \(\mathbb R\), Sylvester’s law of inertia says any real quadratic form is equivalent to
\[
x_1^2+\cdots+x_p^2 - x_{p+1}^2 -\cdots - x_{p+q}^2
\]
with \(p+q\le n\); the triple \((p,q,n-p-q)\) (positive, negative, zero directions) is an invariant. Thus, up to linear change of coordinates, all *real* quadratic forms are exhausted by these normal forms. [math.berkeley](https://math.berkeley.edu/~tb65536/QuadraticForms.pdf)

***

## Arithmetic examples over \(\mathbb Q\) or \(\mathbb Z\)

Over \(\mathbb Q\) or \(\mathbb Z\), the landscape is richer because integrality and local–global phenomena matter. [math.berkeley](https://math.berkeley.edu/~tb65536/QuadraticForms.pdf)

Typical examples:

- Binary: \(ax^2 + bxy + cy^2\) with \(a,b,c\in\mathbb Z\) (binary quadratic forms).  
- Ternary: \(x^2 + y^2 + z^2\), \(x^2 + y^2 - z^2\), etc.  
- Classical forms used in number theory:  
  - Sum of two squares: \(x^2 + y^2\).  
  - Sum of three squares: \(x^2 + y^2 + z^2\).  
  - Sum of four squares: \(x_1^2 + x_2^2 + x_3^2 + x_4^2\).  

Classification involves equivalence under GL\(_n(\mathbb Z)\), discriminants, genus, and spinor genus, and is highly nontrivial for \(n\ge 3\). [en.wikipedia](https://en.wikipedia.org/wiki/Quadratic_form)

***

## Why you can’t “list all” examples

- Each symmetric \(n\times n\) matrix over a field corresponds to a quadratic form, and there are infinitely many such matrices for any \(n\ge 1\). [rmi.tsu](https://rmi.tsu.ge/~kade/LecturesT.Kadeishvili/MathEconomics/Term3/Week3QuadraticLEC.pdf)
- Even up to linear equivalence (congruence), there are infinitely many inequivalent forms over \(\mathbb Q\) or \(\mathbb Z\). For instance, binary quadratic forms \(ax^2 + bxy + cy^2\) with varying discriminant \(b^2-4ac\) already give infinitely many classes. [math.berkeley](https://math.berkeley.edu/~tb65536/QuadraticForms.pdf)

So what one typically does is:

- Fix dimension and base field.  
- Classify quadratic forms *up to equivalence* by invariants (signature over \(\mathbb R\), discriminant and Hasse invariants over number fields, etc.). [en.wikipedia](https://en.wikipedia.org/wiki/Quadratic_form)

If you specify a field (e.g. \(\mathbb R\) vs \(\mathbb Q\)) and dimension, I can switch from these examples to a classification‑style answer (e.g., all real quadratic forms in \(n\) variables up to equivalence, or a quick tour of the arithmetic classification over \(\mathbb Q\)).

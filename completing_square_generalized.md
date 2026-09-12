
Yes—but not in quite the same clean, universal sense as completing the square.

“Completing the square” works exceptionally well because every quadratic can be rewritten as one shifted square plus a constant:

\[
x^2+bx+c=\left(x+\frac b2\right)^2+\left(c-\frac{b^2}{4}\right).
\]

For cubics and quartics, there are related methods, often informally called **completing the cube** and **completing the quartic**, but they require extra substitutions or parameters rather than a single direct identity.

## Cubics: a form of “completing the cube”

A general cubic

\[
x^3+ax^2+bx+c=0
\]

first undergoes a shift

\[
x=y-\frac a3,
\]

which removes the quadratic term. This produces a **depressed cubic**

\[
y^3+py+q=0.
\]

That shift is closely analogous to completing the square: it chooses a translation that eliminates the next-highest term. Cambridge’s discussion of cubic solving explicitly motivates this with the completion-of-square idea for quadratics. [dpmms.cam.ac](https://www.dpmms.cam.ac.uk/~wtg10/cubic.html)

Now rewrite it as

\[
y^3=-py-q.
\]

A tempting but generally unsuccessful idea is to add a constant so that the right side becomes a perfect cube. A cube has the expansion

\[
(u+v)^3=u^3+3u^2v+3uv^2+v^3,
\]

and the middle terms are the obstacle: the depressed cubic has just \(y^3\), \(y\), and a constant, not the full pattern needed for one obvious cube.

Cardano’s insight is to *represent* \(y\) as a sum:

\[
y=u+v.
\]

Then

\[
y^3=(u+v)^3=u^3+v^3+3uv(u+v).
\]

Substituting into \(y^3+py+q=0\) gives

\[
u^3+v^3+(3uv+p)(u+v)+q=0.
\]

Choose

\[
3uv+p=0
\qquad\Longrightarrow\qquad
uv=-\frac p3.
\]

The awkward linear term disappears, leaving

\[
u^3+v^3=-q.
\]

Let \(U=u^3\) and \(V=v^3\). Since

\[
UV=(uv)^3=-\frac{p^3}{27},
\]

the numbers \(U,V\) satisfy

\[
t^2+qt-\frac{p^3}{27}=0.
\]

That is only a **quadratic**. Solving it yields \(u^3\) and \(v^3\), then cube roots yield \(u,v\), and finally \(y=u+v\).

So “completing the cube” is a fair intuition for Cardano’s method, but the precise operation is:

> Turn a cubic into a structured cube expansion by introducing two quantities \(u\) and \(v\), then choose them so the unwanted cross term cancels.

### Small example

Solve

\[
x^3-6x-4=0.
\]

This is already depressed, so put \(x=u+v\). We need

\[
3uv=-6 \quad\Rightarrow\quad uv=-2,
\]

and

\[
u^3+v^3=4.
\]

Thus \(U=u^3\), \(V=v^3\) have

\[
U+V=4,\qquad UV=-8.
\]

Hence they are roots of

\[
t^2-4t-8=0,
\]

so

\[
U=2+2\sqrt3,\qquad V=2-2\sqrt3.
\]

Then one real solution is

\[
x=
\sqrt [en.wikipedia](https://en.wikipedia.org/wiki/Quartic_equation){2+2\sqrt3}
+
\sqrt [en.wikipedia](https://en.wikipedia.org/wiki/Quartic_equation){2-2\sqrt3}.
\]

Here, the “completed cube” is not a lone expression like \((x+a)^3\); it is the expansion of \((u+v)^3\).

## Quartics: completing squares is genuinely central

For a quartic

\[
x^4+ax^3+bx^2+cx+d=0,
\]

the first step is again a shift,

\[
x=y-\frac a4,
\]

to remove the cubic term. The result is a **depressed quartic**

\[
y^4+py^2+qy+r=0.
\]

Ferrari’s method then introduces a parameter in order to manufacture a square and ultimately a **difference of two squares**. This is explicitly a completion-of-the-square strategy. [masder.kfnl.gov](http://masder.kfnl.gov.sa/bitstream/123456789/12119/2/U01M02V02I01A06.pdf?locale=en)

A useful way to see the idea is to write

\[
y^4+py^2+qy+r
=
(y^2+m)^2-\left[(2m-p)y^2-qy+(m^2-r)\right].
\]

The first part is already a square. Ferrari chooses \(m\) so that the bracketed quadratic also becomes a perfect square:

\[
(2m-p)y^2-qy+(m^2-r)=(\alpha y+\beta)^2.
\]

If that succeeds, then the quartic becomes

\[
(y^2+m)^2-(\alpha y+\beta)^2=0.
\]

Factor it:

\[
\bigl(y^2+m-\alpha y-\beta\bigr)
\bigl(y^2+m+\alpha y+\beta\bigr)=0.
\]

So the quartic has been reduced to **two quadratic equations**.

The requirement that the second expression be a square creates a cubic equation for the parameter \(m\), called the **resolvent cubic**. Ferrari’s method therefore has this architecture:

1. Shift the variable to eliminate the cubic term.
2. Add/select a square involving a new parameter.
3. Solve a resolvent cubic to choose that parameter.
4. Factor the quartic as a difference of squares.
5. Solve two quadratics. [surya-teja](https://surya-teja.com/2008/10/04/quartic-equations/)

## Why the quadratic is special

The completion-of-square method is unusually direct because there is only one “middle” coefficient to manage:

\[
(x+h)^2=x^2+2hx+h^2.
\]

Choosing \(h=b/2\) immediately matches the \(x\)-coefficient.

For a cube,

\[
(x+h)^3=x^3+3hx^2+3h^2x+h^3,
\]

one parameter \(h\) would need to control both the \(x^2\) and \(x\) coefficients. In a generic cubic, that is impossible after matching just one of them.

For a fourth power,

\[
(x+h)^4=x^4+4hx^3+6h^2x^2+4h^3x+h^4,
\]

the coefficient constraints are even more restrictive. A general quartic is almost never “one translated fourth power plus a constant.”

For example,

\[
x^4+4x^3+6x^2+4x+9=(x+1)^4+8
\]

is directly “completable” to a fourth power. But a generic quartic such as

\[
x^4+x+1
\]

cannot be written as \((x+h)^4+k\): the latter necessarily has linked \(x^3\), \(x^2\), and \(x\) coefficients, whereas this polynomial does not.

## Bottom line

- **Completing the cube:** Yes, as an informal and sometimes formal description of the substitution behind Cardano’s cubic formula. It uses \(x=u+v\) and engineers the expansion of \((u+v)^3\), rather than simply adding a constant to form \((x+h)^3\).
- **Completing the quartic:** Yes, but the standard method is Ferrari’s: it deliberately completes a **square** inside the quartic problem, then forces a second expression to be a square and factors a difference of squares.
- **A direct analogue of completing the square:** Only for special cubics or quartics. The quadratic case is uniquely simple because a translation has exactly the right freedom to eliminate its linear term.

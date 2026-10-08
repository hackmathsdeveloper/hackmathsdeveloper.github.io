
We seek real polynomials satisfying the displayed identity
\[
p(p(x))-x=(p(x)-x)^2q(x).
\tag{1}
\]
 [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/13148127/78ce1d61-ef00-418b-a6d9-f8bbd6a6dbc5/image.jpg)

Set
\[
f(x)=p(x)-x,
\]
so that \(p(x)=x+f(x)\). Then
\[
p(p(x))-x=f(x)+f(x+f(x)).
\]

By the polynomial Taylor expansion, there is a polynomial \(R(x)\) such that
\[
f(x+f(x))=f(x)+f(x)f'(x)+f(x)^2R(x).
\]
Thus (1) becomes
\[
f(x)\bigl(2+f'(x)\bigr)=f(x)^2\bigl(q(x)-R(x)\bigr).
\]

If \(f\equiv0\), then \(p(x)=x\), which is already in our list. Otherwise, cancel \(f(x)\) to obtain
\[
\boxed{f\mid f'+2.}
\]

If \(f\) is nonconstant, then \(\deg(f'+2)<\deg f\), unless \(f'+2\) is identically zero. A nonzero polynomial cannot divide a nonzero polynomial of smaller degree, so necessarily
\[
f'(x)+2=0.
\]
Consequently,
\[
f(x)=-2x+c,\qquad p(x)=-x+c.
\]

If \(f\) is constant, say \(f(x)=c\), then
\[
p(x)=x+c.
\]
This proves that there are no other possibilities.

## Verification

- For \(p(x)=-x+c\), we have \(p(p(x))=x\), so \(q(x)=0\) works.
- For \(p(x)=x+c\) with \(c\ne0\), we have \(p(p(x))-x=2c\) and \((p(x)-x)^2=c^2\), so \(q(x)=2/c\) works.
- For \(p(x)=x\), both sides vanish, so any real polynomial \(q\) works.

The complete list is
\[
\boxed{p(x)=x+c\quad\text{or}\quad p(x)=-x+c,\qquad c\in\mathbb R.}
\]

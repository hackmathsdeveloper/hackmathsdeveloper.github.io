
A **torus knot** is defined by where its single strand lies: it winds around a torus. A **weaving knot** is defined by its diagram’s over–under pattern: it is an alternating knot with the same crossing projection as a torus knot. They often share the same picture, but they are generally different knots. [arxiv](https://arxiv.org/html/1506.04139v2)

## Torus knot \(T(p,q)\)

A \((p,q)\)-torus knot is a closed curve embedded on the surface of an unknotted torus. It winds \(p\) times around the torus’s meridian and \(q\) times around its longitude; when \(p\) and \(q\) are coprime, it has one component, otherwise \(T(p,q)\) is a multi-component torus link. [academic.oup](https://academic.oup.com/book/33813/chapter/288597576)

Its standard braid form is

\[
T(p,q)=\text{closure of }(\sigma_1\sigma_2\cdots\sigma_{p-1})^q.
\]

All crossings in that braid have the same handedness: every \(\sigma_i\) is, say, a positive crossing. [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/1704.03982)

For example, \(T(3,2)\) is the trefoil knot. [academic.oup](https://academic.oup.com/book/33813/chapter/288597576)

## Weaving knot \(W(p,q)\)

A weaving knot \(W(p,q)\) uses the **same underlying projection** as \(T(p,q)\), but changes the crossing signs so that the diagram is alternating: as you travel along each component, crossings alternate over, under, over, under. [arxiv](https://arxiv.org/html/1506.04139v2)

In braid notation:

\[
W(p,q)=\text{closure of }
(\sigma_1\sigma_2^{-1}\sigma_3\sigma_4^{-1}\cdots)^q.
\]

So the strands occupy the same projected positions as in the torus-knot braid, but the over–under choices are different. [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/1704.03982)

## The essential distinction

| Feature | Torus knot \(T(p,q)\) | Weaving knot \(W(p,q)\) |
|---|---|---|
| Defining property | Lies on a torus surface | Has an alternating diagram with a torus-knot projection |
| Crossing signs | All crossings in the standard braid have the same sign | Alternating positive and negative crossings |
| Diagram | Standard braid projection | Same braid projection, different over–under assignments |
| Usually alternating? | No | Yes, by construction |
| Number of components | \(\gcd(p,q)\) | \(\gcd(p,q)\) |
| Crossing number | \(\min((p-1)q,(q-1)p)\) | \(q(p-1)\) for the standard \(W(p,q)\) family |

A torus knot is generally **not alternating** in its standard projection, whereas a weaving knot is specifically built to be alternating. [arxiv](https://arxiv.org/html/1506.04139v2)

## Why they are different knots

Changing a crossing from over to under changes the knot type in general. Thus \(T(p,q)\) and \(W(p,q)\) can share the same shadow—same positions of arcs and crossings—but fail to be isotopic because their crossing data differ.

For example, \(T(5,4)\) and \(W(5,4)\) have the same standard projection, but \(W(5,4)\) is the alternating version. Its crossing number is

\[
c(W(5,4))=4(5-1)=16.
\]

This is the standard crossing count for the weaving-knot family, not necessarily the same as the torus-knot crossing number. [arxiv](https://arxiv.org/html/1506.04139v2)

## Connection to actual weaving

The name is apt because \(W(p,q)\) resembles a regular over–under lattice: successive strands alternate above and below one another, like the local structure of a woven textile.

However, a “weaving knot” in knot theory is not the same as a periodic fabric. A periodic weave is usually modeled as an infinite collection of threads, or equivalently as a link in a thickened torus. A weaving knot \(W(p,q)\) is a finite closed knot or link obtained by closing a finite braid-like patch. [arxiv](https://arxiv.org/html/1506.04139v2)

So:

\[
\text{torus knot: “where the curve sits”};
\]
\[
\text{weaving knot: “how the crossings alternate”}.
\]

They are related by projection, but their topology is normally distinct. [arxiv](https://arxiv.org/html/1506.04139v2)

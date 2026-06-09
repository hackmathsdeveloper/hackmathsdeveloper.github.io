
You can prove the cotangent partial fraction expansion by applying the residue theorem to a carefully chosen contour integral, and then letting the contour radius go to infinity. The key identity is
\[
\boxed{
\pi\cot(\pi z)
= \frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2}-n^{2}},\quad z\notin\mathbb{Z}.
}
\] [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function/Proof_1)

I’ll walk through a standard contour proof at a level that should be compatible with your complex analysis background.

***

## 1. Strategy and the function to integrate

We want a meromorphic function whose poles are at the integers with simple structure, and whose integral over a large contour we can control. A classical choice is
\[
f(w) = \pi\cot(\pi w)\,\frac{1}{w - z},
\]
where \(z\in\mathbb{C}\setminus\mathbb{Z}\) is fixed. [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function)

Properties:

- \(f(w)\) is meromorphic in \(\mathbb{C}\) with simple poles at each integer \(n\in\mathbb{Z}\) (coming from \(\cot(\pi w)\)) and an additional simple pole at \(w = z\) (from the factor \(1/(w-z)\)). [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function)
- We will integrate \(f(w)\) over a big circle \(|w| = R\) and send \(R\to\infty\). [math.nie.edu](https://math.nie.edu.sg/research/Maths2011/M2011-2.pdf)

The plan:

1. Use the residue theorem to express \(\displaystyle\oint_{|w|=R} f(w)\,dw\) as \(2\pi i\) times the sum of residues at the poles inside the circle.
2. Show that the integral over \(|w|=R\) tends to \(0\) as \(R\to\infty\).
3. Equate “0” to the sum of residues in the limit, and rearrange to get the desired partial fraction expansion.

***

## 2. Residues of \(f(w)\)

### Residue at \(w = z\)

At \(w=z\), \(f\) has a simple pole because of the \(1/(w-z)\) factor, while \(\pi\cot(\pi w)\) is holomorphic at \(w=z\) (since \(z\notin\mathbb{Z}\)). The residue is just the value of the holomorphic factor:
\[
\operatorname{Res}(f,w=z) = \pi\cot(\pi z).[][]

### Residues at \(w = n \in \mathbb{Z}\)

Near \(w = n\), write \(w = n + \epsilon\). We know
\[
\cot(\pi w) = \cot(\pi n + \pi\epsilon) = \cot(\pi\epsilon),
\]
and as \(\epsilon \to 0\),
\[
\cot(\pi\epsilon) \sim \frac{1}{\pi\epsilon} - \frac{\pi\epsilon}{3} + \cdots,
\]
so
\[
\pi\cot(\pi w) \sim \frac{1}{\epsilon} \quad \text{near } w=n. [math.nie.edu](https://math.nie.edu.sg/research/Maths2011/M2011-2.pdf)

Therefore the principal part is \(\dfrac{1}{w-n}\), and the residue at \(n\) of \(\pi\cot(\pi w)\) is \(1\). [math.nie.edu](https://math.nie.edu.sg/research/Maths2011/M2011-2.pdf)

Including the factor \(1/(w-z)\), we get
\[
\operatorname{Res}(f,w=n)
= \frac{1}{w-z}\Big|_{w=n}
= \frac{1}{n - z}.\] [proofwiki](https://proofwiki.org/wiki/Mittag-Leffler_Expansion_for_Cotangent_Function)

So, for any radius \(R>0\) not containing \(z\) on the circle and large enough that all integers with \(|n|<R\) are inside,
\[
\sum_{\text{poles inside }|w|=R}\operatorname{Res}(f,w)
= \pi\cot(\pi z) + \sum_{|n|<R} \frac{1}{n - z}.\] [math.nie.edu](https://math.nie.edu.sg/research/Maths2011/M2011-2.pdf)

***

## 3. Apply the residue theorem

By the residue theorem,
\[
\oint_{|w|=R} f(w)\,dw
= 2\pi i\left(\pi\cot(\pi z) + \sum_{|n|<R} \frac{1}{n - z}\right).[]

So if we can show the contour integral tends to 0 as \(R\to\infty\), we will get
\[
0 = 2\pi i\left(\pi\cot(\pi z) + \sum_{n\in\mathbb{Z}} \frac{1}{n - z}\right),
\]
and hence
\[
\pi\cot(\pi z) = - \sum_{n\in\mathbb{Z}} \frac{1}{n - z}.
\]

We’ll refine and symmetrize this in a moment. First we need to justify that the integral over \(|w|=R\) vanishes in the limit.

***

## 4. Show the contour integral tends to 0

Estimate \(f(w)\) on \(|w| = R\). For large \(|w|\), \(\cot(\pi w)\) is bounded on any horizontal strip (this uses that \(\cot\) is periodic and bounded on strips away from its poles), and in particular one can show
\[
|\pi\cot(\pi w)| = O(1)
\quad\text{as}\quad |w|\to\infty
\]
for \(w\) on the circle \(|w|=R\).[][]

Meanwhile,
\[
\left|\frac{1}{w - z}\right| \le \frac{1}{|w| - |z|} = \frac{1}{R-|z|}.
\]

Thus, on \(|w|=R\),
\[
|f(w)| = \left|\pi\cot(\pi w)\,\frac{1}{w - z}\right|
\le \frac{C}{R-|z|}
\]
for some constant \(C\) independent of \(R\).[][]

By the estimation lemma (ML inequality),
\[
\left|\oint_{|w|=R} f(w)\,dw\right|
\le (\text{max }|f(w)|)\cdot(\text{length of circle})
\le \frac{C}{R-|z|}\cdot 2\pi R
\to 0
\quad\text{as }R\to\infty. [math.utoronto](https://www.math.utoronto.ca/mnica/complex1.pdf)
\]

Therefore
\[
\lim_{R\to\infty}\oint_{|w|=R}f(w)\,dw = 0.
\]

Passing to the limit in the residue theorem identity gives
\[
0 = 2\pi i\left(\pi\cot(\pi z) + \sum_{n\in\mathbb{Z}} \frac{1}{n - z}\right),
\]
or
\[
\boxed{
\pi\cot(\pi z) = -\sum_{n\in\mathbb{Z}} \frac{1}{n - z}.
}
\][][]

***

## 5. Symmetrize to get the usual form

Write explicitly the sum over all integers:
\[
\sum_{n\in\mathbb{Z}} \frac{1}{n - z}
= \frac{1}{-z} + \sum_{n=1}^{\infty}\left(\frac{1}{n - z} + \frac{1}{-n - z}\right)
= -\frac{1}{z} + \sum_{n=1}^{\infty}\left(\frac{1}{n - z} + \frac{-1}{n + z}\right).
\]

So
\[
-\sum_{n\in\mathbb{Z}} \frac{1}{n - z}
= \frac{1}{z} + \sum_{n=1}^{\infty}\left(\frac{1}{z - n} + \frac{1}{z + n}\right). [ncatlab](https://ncatlab.org/nlab/show/product+formula+for+the+sine+function)

But the left-hand side is exactly \(\pi\cot(\pi z)\) from the previous step, hence
\[
\boxed{
\pi\cot(\pi z)
= \frac{1}{z} + \sum_{n=1}^{\infty}\left(\frac{1}{z - n} + \frac{1}{z + n}\right),\quad z\notin\mathbb{Z}.
}[][]

Combine the symmetric fractions in each pair:
\[
\frac{1}{z - n} + \frac{1}{z + n}
= \frac{2z}{z^{2}-n^{2}},
\]
giving
\[
\boxed{
\pi\cot(\pi z)
= \frac{1}{z} + 2\sum_{n=1}^{\infty}\frac{z}{z^{2}-n^{2}},\quad z\notin\mathbb{Z},
}
\][][]
which is the partial fraction (Mittag–Leffler) expansion we used earlier to derive the sine product.

***

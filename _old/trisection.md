
**Yes**—once you remove the compass-and-unmarked-straightedge restriction, both arbitrary angle trisection and squaring the circle have exact mathematical solutions. Some alternative methods have been known since antiquity. The crucial question is which additional operations you permit. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/HistTopics/Trisecting_an_angle/)

## 1. Trisecting any angle

An arbitrary angle can be trisected exactly using, for example:

- A marked ruler together with a compass. This allows a *neusis* construction: you slide and rotate the ruler until its marks simultaneously satisfy prescribed geometric conditions. An ordinary unmarked straightedge cannot perform that operation. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/HistTopics/Trisecting_an_angle/)
- Origami. Suitable paper folds can trisect an arbitrary angle exactly in the ideal mathematical model. [plus.maths](https://plus.maths.org/trisecting-angle-origami)
- Additional curves, such as a conchoid or suitable conic sections. These were already used in ancient solutions. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/HistTopics/Trisecting_an_angle/)

### Why do these succeed when straightedge and compass fail?

Let the given angle be \(\theta\), and put \(x=\cos(\theta/3)\). The triple-angle identity gives

\[
\cos\theta=4x^3-3x,
\]

so trisection requires finding an appropriate root of the cubic equation

\[
4x^3-3x-\cos\theta=0.
\]

Straightedge-and-compass constructions cannot solve this cubic in general. Origami and marked-ruler constructions allow operations powerful enough to overcome that obstruction. Thus, the impossibility is about the permitted operations—not about the existence of the trisected angle. [plus.maths](https://plus.maths.org/maths-three-minutes-trisecting-angle)

## 2. Squaring the circle

To square a circle means to construct a square having exactly the same area—not necessarily the same perimeter.

For a circle of radius \(r\), the square’s side \(s\) must satisfy

\[
s^2=\pi r^2,
\qquad\text{so}\qquad
s=r\sqrt{\pi}.
\]

That is already an exact mathematical specification of the answer. The construction question is whether your permitted tools can produce that length. With straightedge and compass alone, they cannot: Lindemann’s 1882 proof that \(\pi\) is transcendental establishes the obstruction. [uni-freiburg](https://uni-freiburg.de/en/squaring-the-circle/)

If you allow a suitable additional curve, however, an exact construction becomes possible. A classical example uses the quadratrix of Hippias. In a unit-coordinate setup, its equation is

\[
x=y\cot\left(\frac{\pi y}{2}\right).
\]

Its limiting intercept as \(y\to0\) is \(2/\pi\). If the curve and that intercept are available as part of the allowed construction, ordinary geometric operations can then produce \(\pi\), followed by \(\sqrt{\pi}\), and hence the required square. The important caveat is that providing the quadratrix and its limiting intercept supplies a capability unavailable to straightedge and compass alone. [cage.ugent](https://cage.ugent.be/~hs/quadratrix/quadratrix.html)

## 3. Removing the restriction does not make every alternative tool sufficient

The two problems have different levels of obstruction:

| Permitted method | Trisect any angle? | Square a circle exactly? |
|---|---|---|
| Compass and unmarked straightedge | No, in general | No |
| Standard mathematical origami | Yes | No |
| A suitable quadratrix, including its limiting intercept | Yes | Yes |

Origami overcomes the cubic-equation obstacle, but its standard construction rules still produce only algebraic lengths from a unit starting configuration. They therefore cannot produce the transcendental length \(\sqrt{\pi}\). The quadratrix supplies the stronger operation needed for circle squaring. [cage.ugent](https://cage.ugent.be/~hs/quadratrix/quadratrix.html)

So neither problem is an unresolved mystery once the classical restrictions are removed. What remains meaningful is specifying the replacement rules: a marked ruler, paper folding, special curves, numerical approximation, and exact symbolic formulas do not all provide the same capabilities. [mathshistory.st-andrews.ac](https://mathshistory.st-andrews.ac.uk/HistTopics/Trisecting_an_angle/)

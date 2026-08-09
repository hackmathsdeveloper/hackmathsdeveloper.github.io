
You can construct \(\sqrt n\) for **any positive integer \(n\)** using a straightedge and compass. The most compact general method uses a semicircle and the geometric-mean theorem. [geogebra](https://www.geogebra.org/m/edtecfcv)

## One construction for \(\sqrt n\)

Start with a chosen unit segment of length \(1\).

1. Draw a straight line and mark three consecutive points \(A,B,C\) so that  
   \[
   AB=n,\qquad BC=1.
   \]
   Thus \(AC=n+1\).

2. Construct the midpoint \(O\) of \(AC\).

3. Draw the circle (or just the upper semicircle) with diameter \(AC\).

4. At \(B\), construct a line perpendicular to \(AC\). Let it meet the semicircle at \(D\).

5. The segment
   \[
   BD=\sqrt n.
   \]

You may transfer \(BD\) with the compass onto a number line to mark the point representing \(\sqrt n\). [geogebra](https://www.geogebra.org/m/edtecfcv)

## Why it works

Because \(D\) lies on the circle with diameter \(AC\), \(\angle ADC=90^\circ\). In this right triangle, the altitude \(BD\) to the hypotenuse satisfies

\[
BD^2=AB\cdot BC.
\]

Since \(AB=n\) and \(BC=1\),

\[
BD^2=n\cdot1=n,
\qquad\text{therefore}\qquad
BD=\sqrt n.
\]

This is the geometric-mean theorem in action. [mathschallenge](https://mathschallenge.net/library/constructions/geometrical_square_root)

## Example: construct \(\sqrt7\)

- Mark \(AB=7\) unit lengths and then \(BC=1\) unit length.
- Draw the semicircle with \(AC=8\) as its diameter.
- Erect the perpendicular from \(B\) to meet the semicircle at \(D\).
- The perpendicular segment \(BD\) has length \(\sqrt7\).

## Repeated-triangle method

For many consecutive roots, use the **Spiral of Theodorus**:

- Make a right triangle whose legs are \(1\) and \(1\); its hypotenuse is \(\sqrt2\).
- At the endpoint of that hypotenuse, construct a new perpendicular leg of length \(1\); the next hypotenuse is \(\sqrt3\).
- Repeat: if the current hypotenuse is \(\sqrt k\), adding a perpendicular unit leg creates a hypotenuse
  \[
  \sqrt{(\sqrt k)^2+1^2}=\sqrt{k+1}.
  \]

So this produces \(\sqrt2,\sqrt3,\sqrt4,\sqrt5,\ldots\) one after another. [en.wikipedia](https://en.wikipedia.org/wiki/Square_root)

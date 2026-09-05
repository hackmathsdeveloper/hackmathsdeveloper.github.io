
François Viète's formula for $\frac{2}{\pi}$ is derived using repeated application of trigonometric half-angle identities, specifically working with the areas or perimeters of regular polygons inscribed in a circle.

**Core Trigonometric Identity**
The foundation of the derivation relies on the half-angle formula for the sine function:


$$\sin\left(\frac{\theta}{2}\right) = \sqrt{\frac{1 - \cos\theta}{2}}$$


Using the Pythagorean identity $\cos\theta = \sqrt{1 - \sin^2\theta}$, this can be expressed entirely in terms of sine:


$$\sin\left(\frac{\theta}{2}\right) = \frac{\sqrt{2 - \sqrt{4 - 4\sin^2\theta}}}{2} = \frac{\sqrt{2 - \sqrt{2^2 - (2\sin\theta)^2}}}{2}$$

**Applying to a Circle**
Viète considered a unit circle (radius $R = 1$) and inscribed regular polygons, starting with a square ($n = 4$ sides) and successively doubling the number of sides to an octagon ($n = 8$), 16-gon, and so on.

For a polygon with $2^k$ sides, the side length $s_k$ relative to the diameter can be related to angles. Specifically, setting $\theta = \frac{\pi}{2}$, the side length of an inscribed square yields a starting sine value.

1. **First Term ($n = 4$, Square):**
Starting with $\sin\left(\frac{\pi}{2}\right) = 1$, applying the half-angle substitution gives:

$$\sin\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2}$$


2. **Second Term ($n = 8$, Octagon):**
Applying the half-angle relation again for $\frac{\pi}{8}$:

$$\sin\left(\frac{\pi}{8}\right) = \frac{\sqrt{2 - \sqrt{2}}}{2}$$


3. **Subsequent Iterations:**
Continuing this process for $16$-gon, $32$-gon, and taking the limit as the number of sides approaches infinity ($n \to \infty$), the ratio of the polygon perimeters leads to the infinite product expression for $\frac{2}{\pi}$:

$$\frac{2}{\pi} = \prod_{n=1}^{\infty} a_n = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2 + \sqrt{2}}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt{2}}}}{2} \dots$$



**Limit Formulation**
Alternatively, using Archimedes' insight of bounding a circle by polygons, Viète expressed the ratio of areas. By evaluating the infinite product of nested radicals:


$$\lim_{k \to \infty} \frac{2^k}{\pi} \sin\left(\frac{\pi}{2^k}\right) = \frac{2}{\pi}$$


Expanding $\sin\left(\frac{\pi}{2^k}\right)$ via repeated half-angle expansions yields the exact product shown in the image.

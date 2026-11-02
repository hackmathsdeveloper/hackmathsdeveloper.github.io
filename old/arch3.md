
Archimedes’ proof that the surface area of a sphere of radius $R$ equals four times the area of its great circle ($A = 4\pi R^2$) is one of the crowning achievements of ancient geometry.

Because calculus was not available, Archimedes used the **Method of Exhaustion** combined with a **Proof by Contradiction** (a double *reductio ad absurdum*). He constructed regular polygons inscribed inside and circumscribed outside a circle, rotated them to form 3D solids, and squeezed the sphere's surface area between them.

---

### Step 1: Approximating the Circle via Inscribed and Circumscribed Polygons

Archimedes started with a 2D cross-section—a great circle of radius $R$—and constructed two regular polygons with $2n$ sides (e.g., 4, 8, 16, 32... sides):

1. **An Inscribed Polygon** lying entirely inside the circle.
2. **A Circumscribed Polygon** lying entirely outside the circle, touching the circle at the midpoints of its edges.

```
       Circumscribed Polygon (Outer)
             /---------\
            /   .---.   \
           /   /     \   \
          |   | Circle|   |   <-- Inscribed Polygon (Inner)
           \   \     /   /
            \   `---'   /
             \---------/

```

---

### Step 2: Revolution into 3D Geometric Solids

Archimedes rotated the entire figure around a central axis passing through opposite vertices:

* **Inscribed Solid:** Rotating the inner polygon creates a solid made of two right cones (at the poles) and several frustums of cones joined base-to-base inside the sphere.
* **Circumscribed Solid:** Rotating the outer polygon creates a similar solid made of cones and frustums enclosing the sphere entirely.

Because the sphere is contained entirely inside the circumscribed solid and entirely contains the inscribed solid, its surface area $A_{\text{sphere}}$ must lie between their surface areas:

$$S_{\text{inscribed}} < A_{\text{sphere}} < S_{\text{circumscribed}}$$

---

### Step 3: Area Formula for Frustums of Cones

Archimedes proved a key lemma: the lateral surface area of a frustum of a cone with slant height $s$ and base radii $r_1$ and $r_2$ is equal to:

$$\text{Area} = 2\pi \cdot r_{\text{mid}} \cdot s$$

where $r_{\text{mid}} = \frac{r_1 + r_2}{2}$ is the distance from the midpoint of the slant side to the axis of rotation.

When summing the lateral areas of all the frustums and cones forming the **inscribed solid**, the total surface area simplifies precisely to:

$$S_{\text{inscribed}} = 2\pi \cdot h \cdot a_n$$

* $h = 2R$ is the diameter along the rotation axis.
* $a_n$ is the apothem (the perpendicular distance from the center of the circle to a side of the inscribed polygon).

As the number of sides $n$ increases, the apothem $a_n$ gets arbitrarily close to the radius $R$:

$$\lim_{n \to \infty} S_{\text{inscribed}} = 2\pi (2R) R = 4\pi R^2$$

---

### Step 4: Double Proof by Contradiction (*Reductio ad Absurdum*)

Let $C = 4\pi R^2$ be four times the area of the great circle. Archimedes proved that $A_{\text{sphere}} = C$ by showing that both $A_{\text{sphere}} > C$ and $A_{\text{sphere}} < C$ lead to logical impossibilities.

#### Part A: Assume $A_{\text{sphere}} > C$

1. If $A_{\text{sphere}} > C$, there exists a circumscribed solid whose surface area $S_{\text{circumscribed}}$ is smaller than $A_{\text{sphere}}$ by increasing the number of polygon sides $n$.
2. But the circumscribed solid completely encloses the sphere, so geometrically its surface area **must** be strictly greater than that of the sphere ($S_{\text{circumscribed}} > A_{\text{sphere}}$).
3. Contradiction! Therefore, $A_{\text{sphere}}$ cannot be strictly greater than $C$.

#### Part B: Assume $A_{\text{sphere}} < C$

1. If $A_{\text{sphere}} < C$, we can choose an inscribed solid with enough sides $n$ such that its surface area $S_{\text{inscribed}} > A_{\text{sphere}}$.
2. But the inscribed solid lies entirely inside the sphere, so its surface area **must** be strictly less than that of the sphere ($S_{\text{inscribed}} < A_{\text{sphere}}$).
3. Contradiction! Therefore, $A_{\text{sphere}}$ cannot be strictly less than $C$.

---

### Conclusion

Since $A_{\text{sphere}}$ can neither be greater than nor less than four times the area of its great circle $C$, it must be exactly equal to it:

$$A_{\text{sphere}} = 4\pi R^2$$

* Would you like to explore the proof for the volume of the sphere ($V = \frac{4}{3}\pi R^3$) using a similar exhaustion approach?
* Would you like to see how Archimedes used conic sections to solve the cubic equation in Proposition 4 of Book II?

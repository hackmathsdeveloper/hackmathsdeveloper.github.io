
***On the Sphere and Cylinder*** (*Περὶ σφαίρας καὶ κυλίνδρου*) is a masterwork written by Archimedes of Syracuse around 225 BC, published in two books. In this treatise, Archimedes established fundamental formulas for the surface areas and volumes of spheres, spherical segments, cones, and cylinders using his rigorous method of exhaustion.

Below is a comprehensive list of the main results, theorems, and propositions established across both books.

---

### Key Formulas & Fundamental Relations

Let $r$ be the radius of the sphere, $d = 2r$ its diameter, and consider a right circular cylinder circumscribing the sphere (height $h = 2r$ and base radius $r$).

| Geometric Quantity | Formula | Ratio (Sphere to Cylinder) |
| --- | --- | --- |
| **Surface Area of Sphere** | $A = 4\pi r^2$ | $\frac{2}{3}$ of cylinder total area ($6\pi r^2$) |
| **Volume of Sphere** | $V = \frac{4}{3}\pi r^3$ | $\frac{2}{3}$ of cylinder volume ($2\pi r^3$) |
| **Curved Surface Area** | $A_{\text{curved}} = 4\pi r^2$ | Equal to cylinder lateral area ($2\pi r \cdot 2r = 4\pi r^2$) |

---

### Book I: Main Results and Propositions

Book I begins with core axioms concerning convex surfaces and curves, followed by 44 propositions establishing surface areas and volumes.

#### 1. Surface Area and Area Theorems

* **Proposition 13 & 14:** The lateral surface area of any right circular cylinder is equal to the area of a circle whose radius is the mean proportional between the side (height) of the cylinder and the diameter of its base ($A = 2\pi r h$).
* **Proposition 33 (The Surface Area of a Sphere):** The surface area of any sphere is equal to four times the area of its greatest circle:

$$A = 4\pi r^2$$


* **Proposition 35–37:** The surface area of any spherical segment/cap equals the area of a circle whose radius is equal to the straight line drawn from the vertex of the segment to the base perimeter:

$$A_{\text{cap}} = 2\pi r h$$



#### 2. Volume Theorems

* **Proposition 34 (The Volume of a Sphere):** Any sphere is equal in volume to four times the cone whose base is equal to the greatest circle of the sphere and whose height is equal to the radius of the sphere:

$$V = 4 \cdot \left(\frac{1}{3} \pi r^2 \cdot r\right) = \frac{4}{3}\pi r^3$$


* **Proposition 42 & 43 (Volume of a Spherical Sector):** The volume of a spherical sector (a cone-like shape with a spherical base) is equal to a cone whose base is equal to the surface area of the spherical segment and whose height is the radius of the sphere:

$$V_{\text{sector}} = \frac{1}{3} (2\pi r h) r = \frac{2}{3}\pi r^2 h$$



#### 3. The Grand Ratio (Archimedes' Proudest Discovery)

* **Propositions 44:** A sphere has two-thirds the volume and two-thirds the total surface area of the circumscribing cylinder.

$$\frac{V_{\text{sphere}}}{V_{\text{cylinder}}} = \frac{\frac{4}{3}\pi r^3}{2\pi r^3} = \frac{2}{3}$$


$$\frac{A_{\text{sphere}}}{A_{\text{cylinder}}} = \frac{4\pi r^2}{6\pi r^2} = \frac{2}{3}$$



---

### Book II: Cutting and Segmenting Spheres

Book II contains 9 propositions applying the results of Book I to problems involving planes intersecting spheres.

#### 1. Volume of Spherical Segments

* **Proposition 2:** The volume of a spherical segment of height $h$ cut from a sphere of radius $r$ is equivalent to a cone with the same base and a modified height:

$$V_{\text{segment}} = \pi h^2 \left(r - \frac{h}{3}\right)$$



#### 2. Division of Spheres by Planes

* **Proposition 3 & 4:** Given a sphere, to cut it by a plane so that:
1. The surface areas of the two resulting spherical segments have a given ratio.
2. The volumes of the two resulting spherical segments have a given ratio.
*(Proposition 4 requires solving a cubic equation of the form $x^3 - ax^2 + b = 0$, which Archimedes solved geometrically using the intersection of conic sections).*



#### 3. Similar Spherical Segments

* **Proposition 8 & 9:** Similar spherical segments (segments subtending equal angles at the center) have surface areas proportional to the squares of their base radii or heights, and volumes proportional to the cubes of their base radii or heights:

$$\frac{A_1}{A_2} = \left(\frac{h_1}{h_2}\right)^2, \quad \frac{V_1}{V_2} = \left(\frac{h_1}{h_2}\right)^3$$



* Would you like a step-by-step breakdown of Archimedes' **method of exhaustion** proof for $A = 4\pi r^2$?
* Should we examine the geometric conic-section solution Archimedes used for **Proposition 4** (the cubic equation)?
* Would you like detailed calculations for specific spherical segment dimensions?

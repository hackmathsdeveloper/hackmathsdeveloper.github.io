
The possibility of a regular tessellation depends entirely on how the interior angles of the regular polygons fit around a single vertex.
The {8,4} tessellation is possible on the hyperbolic plane but impossible on the Euclidean plane because of the sum of interior angles around a vertex, which is dictated by the curvature of the space. Conformality is not a property of the space itself that decides if a tiling is possible; rather, it is a property of the mapping projections used to draw hyperbolic space on a flat screen.
Here is the mathematical breakdown of why this happens and the relevant calculations.

The Fundamental Property: Vertex Angle Deficit/Surplus

To form a perfect, gapless regular tessellation where \(q\) regular \(p\)-sided polygons meet at every vertex (a {p,q} tiling), the total angle around that vertex must equal exactly 360° (\(2\pi\) radians).
1. Interior Angle of a Regular Polygon (\(A\)):
In flat Euclidean geometry, the interior angle of a regular \(p\)-sided polygon is:
\(A=\frac{(p-2)\times 180^{\circ }}{p}\text{\ or\ }A=\pi \left(1-\frac{2}{p}\right)\)
2. Total Angle Sum Around a Vertex (\(S\)):
When \(q\) of these polygons meet at a single vertex, their combined angles sum to:
\(S=q\times A=q\times \pi \left(1-\frac{2}{p}\right)\)
The geometry of the plane required for the tiling is determined by how \(S\) compares to \(2\pi\):
• Euclidean Plane (Flat): \(S = 2\pi \implies \frac{1}{p} + \frac{1}{q} = \frac{1}{2}\)
• Spherical Plane (Positive Curvature): \(S < 2\pi \implies \frac{1}{p} + \frac{1}{q} > \frac{1}{2}\)
• Hyperbolic Plane (Negative Curvature): \(S > 2\pi \implies \frac{1}{p} + \frac{1}{q} < \frac{1}{2}\)

Calculating the {8,4} Tessellation

Let's plug \(p = 8\) (octagons) and \(q = 4\) (four meeting at a vertex) into the criteria.

1. Why it is Impossible in the Euclidean Plane

If we tried to construct a flat, Euclidean regular octagon, its interior angle would be:
\(A=\frac{(8-2)\times 180^{\circ }}{8}=135^{\circ }\)
If 4 octagons meet at a vertex in the Euclidean plane, the total angle sum is:
\(S=4\times 135^{\circ }=540^{\circ }\)
Because \(540^\circ > 360^\circ\), the tiles overlap heavily. There is a total angle surplus of 180° (\(540^\circ - 360^\circ\)). You cannot physically squeeze four flat 135° angles around a single point on a flat sheet of paper without the paper buckling or overlapping.

2. Why it is Possible in the Hyperbolic Plane

In hyperbolic geometry, the interior angles of a polygon are not fixed by the number of sides; they shrink as the area of the polygon grows.
To make the {8,4} tiling possible, we need the 4 octagons to meet perfectly around a vertex with no overlap (\(S = 360^\circ\)). This means each hyperbolic octagon must have an interior angle of exactly:
\(A_{\text{hyperbolic}}=\frac{360^{\circ }}{4}=90^{\circ }\)
Because a hyperbolic octagon's angles can be compressed down to \(90^{\circ }\) (a right-angled octagon), 4 of them fit perfectly around a vertex, creating a stable, infinite tessellation across a negatively curved space.

Conformality and Hyperbolic Projections

Conformality means angle-preserving. Because humans cannot perfectly perceive a natively curved hyperbolic plane, mathematicians project it onto Euclidean maps.
The Poincaré Disk Model is a conformal projection of the hyperbolic plane.
• What it does: It maps the entire infinite hyperbolic plane inside a finite circle.
• Conformality Property: Because it is conformal, every intersection angle in the model perfectly matches the true hyperbolic angle. When you look at a graphic of the {8,4} tiling on a Poincaré Disk, the octagons appear to warp and get smaller near the boundary, but every vertex cleanly shows four lines crossing at exactly 90° angles.
To visualize how these compressed angles fit together perfectly without Euclidean overlapping, you can interact with the hyperbolic grid generator below.
AI-generated. Don't enter sensitive personal info.
Would you like to calculate the exact hyperbolic area of one of these regular {8,4} octagons using the Gauss-Bonnet theorem?


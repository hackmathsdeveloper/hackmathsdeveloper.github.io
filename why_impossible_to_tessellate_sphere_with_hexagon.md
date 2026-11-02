
**No**—not in the usual sense of a finite, edge-to-edge tiling in which each hexagon has six genuine corners and at least three tiles meet at every vertex. This remains impossible even if the hexagons are irregular or distorted: the obstruction is topological, not just geometric. [math.stackexchange](https://math.stackexchange.com/questions/1065040/hexagonal-tessellation-on-a-sphere)

## Why it is impossible

A tiling of the sphere must satisfy Euler’s formula:

\[
V-E+F=2,
\]

where \(V,E,F\) count vertices, edges, and faces.

Suppose all \(F\) faces are hexagons:

- Each face has six edges, and each edge belongs to two faces, so \(E=3F\).
- There are \(6F\) face-corner incidences. If at least three faces meet at every vertex, then \(3V\le 6F\), so \(V\le 2F\).

Consequently,

\[
V-E+F\le 2F-3F+F=0,
\]

contradicting Euler’s required value of \(2\). Allowing more than three hexagons to meet at some vertices does not fix the problem. [math.stackexchange](https://math.stackexchange.com/questions/1065040/hexagonal-tessellation-on-a-sphere)

## Why pentagons solve the problem

If exactly three faces meet at every vertex, the same counting argument gives the general identity

\[
\sum_{k}(6-k)F_k=12,
\]

where \(F_k\) is the number of \(k\)-sided faces. Hexagons contribute zero, pentagons contribute \(+1\), and heptagons contribute \(-1\). Thus, if you use only pentagons and hexagons, you need exactly twelve pentagons, regardless of the number of hexagons. A familiar example is the classic football pattern: twelve pentagons and twenty hexagons. [math.stackexchange](https://math.stackexchange.com/questions/1065040/hexagonal-tessellation-on-a-sphere)

This is also why practical “hexagonal” globe grids contain nonhexagonal cells; common icosahedron-based constructions have twelve pentagonal cells. [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9015668/)

## A theoretical loophole

If you relax what counts as a hexagon, there is a degenerate construction: divide the equator into six arcs and call each hemisphere a “hexagon.” The two faces then have six labeled edges each, but their “corners” have straight \(180^\circ\) interior angles, and only two faces meet at each vertex. This is a valid broad cell decomposition, but not a genuine hexagonal mesh in the usual geometric sense. [math.stackexchange](https://math.stackexchange.com/questions/1065040/hexagonal-tessellation-on-a-sphere)

So the precise answer is: an ordinary all-hexagon spherical tessellation is impossible; only by relaxing the usual requirements can you obtain an all-“hexagon” construction. [math.stackexchange](https://math.stackexchange.com/questions/1065040/hexagonal-tessellation-on-a-sphere)

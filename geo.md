
One explicit configuration with 12 touching spheres is given by putting the contact points at the 12 vertices of a regular icosahedron on the unit sphere; in that configuration every outer sphere touches the central one and exactly 5 outer neighbors, so in particular it is possible to realize 12 mutually tangent spheres around 1. [en.wikipedia](https://en.wikipedia.org/wiki/Kissing_number)
## What the statement is actually about
The statement you quoted is exactly the theorem “12 Identical Spheres can touch One Other Sphere” on ProofWiki. [proofwiki](https://proofwiki.org/wiki/12_Identical_Spheres_can_touch_One_Other_Sphere)
The usual geometric translation is:

- Take a central sphere of radius \(R\).  
- Place other spheres of the same radius so that each outer sphere is tangent to the central sphere.  
- Equivalently, normalize so the central sphere is the unit sphere and the centers of the outer spheres lie on the unit sphere at pairwise chordal distance at least \(1\) (to avoid overlap). [en.wikipedia](https://en.wikipedia.org/wiki/Kissing_number)

Then:

1. There exists a configuration of 12 outer spheres touching the central one (this is “kissing number in 3D is at least 12”). [en.wikipedia](https://en.wikipedia.org/wiki/Kissing_number)
2. In the particular configuration ProofWiki is after, each outer sphere also touches exactly 3 outer spheres; this is a specific combinatorial realization of 12 contact points on the central sphere. [proofwiki](https://proofwiki.org/wiki/12_Identical_Spheres_can_touch_One_Other_Sphere)

Note that there are many 12‑around‑1 configurations; the icosahedral one has each outer sphere touching 5 neighbors, not 3. [math.hkust.edu](https://www.math.hkust.edu.hk/~yangwang/Course/2016FSMath4999/Wing%20Lung%20Lee/lect1.pdf)
So what you’re being asked to prove is not the uniqueness or optimality of any arrangement, just existence of at least one arrangement with that adjacency pattern.
## Constructing 12 touching spheres
Normalize the radius of the central sphere to 1.  
If the outer spheres also have radius 1, then their centers must lie at distance \(2\) from the central center, so after scaling by \(1/2\) we can equivalently work with:

- A central unit sphere \(S^2\).  
- 12 points on \(S^2\) where each point is at spherical distance strictly greater than 0 from others (no overlap) and we are free to choose adjacency so that each one has degree 3 in the contact graph. [en.wikipedia](https://en.wikipedia.org/wiki/Kissing_number)

An extremely clean way to get a 12‑vertex, 3‑regular contact graph on the sphere is to use the graph of a regular dodecahedron (12 vertices, 3 edges incident at each vertex). [math.hkust.edu](https://www.math.hkust.edu.hk/~yangwang/Course/2016FSMath4999/Wing%20Lung%20Lee/lect1.pdf)
You can realize the 20 vertices of a regular dodecahedron on a sphere, and you can similarly realize a 12‑vertex, 3‑regular graph as a convex polyhedron whose vertices lie on a sphere. [en.wikipedia](https://en.wikipedia.org/wiki/Kissing_number)

ProofWiki’s construction proceeds more directly: it gives explicit coordinates for 12 unit vectors on \(S^2\) whose pairwise inner products are large enough (for non‑adjacent vertices) to avoid unwanted tangencies, and equal to a specific value for adjacent vertices, so that the contact graph is a 3‑regular graph on 12 vertices. [proofwiki](https://proofwiki.org/wiki/12_Identical_Spheres_can_touch_One_Other_Sphere)
These 12 directions are then used as directions of centers of the outer spheres around the central one.

Concretely, if \(v_1,\dots,v_{12}\) are unit vectors on \(S^2\) such that

- \(\lVert v_i - v_j\rVert = d_0\) whenever vertices \(i\) and \(j\) are adjacent in the chosen 3‑regular graph,  
- \(\lVert v_i - v_j\rVert > d_0\) otherwise,

then by taking outer sphere radius \(r\) small enough and placing the center of the \(i\)-th outer sphere at \(c_i = (1+r)\,v_i\), we have:

- \(\lVert c_i\rVert = 1+r\), so each outer sphere is tangent to the central sphere of radius 1.  
- \(\lVert c_i - c_j\rVert = (1+r)\,\lVert v_i - v_j\rVert\).  

Choosing \(r\) so that \((1+r)d_0 = 2r\) gives tangency exactly along edges of the graph; non‑edges have larger separation and thus are not tangent. [proofwiki](https://proofwiki.org/wiki/12_Identical_Spheres_can_touch_One_Other_Sphere)
Since there are 3 edges incident at each vertex of the graph, each outer sphere will touch exactly 3 other outer spheres.

This solves the existence problem: it shows you can engineer 12 identical spheres around a central one so that each touches the center and precisely 3 neighbors.
## Why 12 is the right number in 3D
Historically, this is the 3‑dimensional “kissing number” problem: what is the maximum number of equal spheres that can all touch a given sphere without overlaps. [en.wikipedia](https://en.wikipedia.org/wiki/Kissing_number)
Newton believed the maximum in 3D was 12; Gregory thought maybe 13 was possible. [plus.maths](https://plus.maths.org/content/newton-and-kissing-problem)
The question stayed open until a nontrivial geometric‑combinatorial proof in the 20th century, where it was finally shown that 12 is indeed maximal. [math.hkust.edu](https://www.math.hkust.edu.hk/~yangwang/Course/2016FSMath4999/Wing%20Lung%20Lee/lect1.pdf)

Fejes Tóth, Leech, Hsiang and others developed methods based on:

- Projecting the centers of the outer spheres radially onto the unit sphere to get a finite set of points.  
- Studying spherical caps (geodesic disks) around these points and using area and angle inequalities plus Euler’s formula \(V-E+F=2\) for planar graphs embedded on the sphere. [ams](https://www.ams.org/journals/bull/1989-21-01/S0273-0979-1989-15795-9/S0273-0979-1989-15795-9.pdf)
- Showing that any hypothetical 13‑point configuration with minimum pairwise angle corresponding to tangency of unit spheres leads to contradictions in these inequalities. [math.hkust.edu](https://www.math.hkust.edu.hk/~yangwang/Course/2016FSMath4999/Wing%20Lung%20Lee/lect1.pdf)

The upshot is:

- Kissing number in 3D is exactly 12, so “a total of 12 identical spheres can touch one other such sphere” is sharp. [proofwiki](https://proofwiki.org/wiki/12_Identical_Spheres_can_touch_One_Other_Sphere)
- There are many non‑congruent 12‑sphere configurations; one family has each sphere touching 3 neighbors as in your statement, another is the icosahedral one where each sphere touches 5 neighbors. [arxiv](https://arxiv.org/abs/1611.10297)

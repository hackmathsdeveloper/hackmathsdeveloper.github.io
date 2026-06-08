
A topograph is Conway’s combinatorial-geometric way of drawing all primitive values of a binary quadratic form on the plane at once, so that arithmetic properties become visible as “terrain features” like rivers and basins. [math.utah](http://www.math.utah.edu/vigre/ugrad/reu/sgp/ibqf.pdf)

***

## Core idea

Given an integral binary quadratic form \(Q(x,y)=Ax^2+Bxy+Cy^2\), the topograph is a planar graph whose regions are labeled by primitive integer directions \((x:y)\) and annotated with the integer value \(Q(x,y)\) at that direction. The construction is set up so that local adjacency in the graph reflects simple relations between the pairs \((x,y)\) (e.g. Farey neighbors), and global structures in the graph encode arithmetic behavior of \(Q\). [webhomes.maths.ed.ac](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/conwaysens.pdf)

Intuitively, the topograph is a “map” of the values of \(Q\) over primitive lattice points, drawn in a highly structured way rather than just as a scatter plot.

***

## Combinatorial structure

Conway’s original construction starts from the *Farey tessellation* of the hyperbolic plane (or, combinatorially, the Farey tree) and uses its edges and vertices to organize primitive integer pairs. [londmathsoc.onlinelibrary.wiley](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70042)

- Each *region* (face) corresponds to a primitive lattice vector \((x,y)\) up to sign. [math.utah](http://www.math.utah.edu/vigre/ugrad/reu/sgp/ibqf.pdf)
- Neighboring regions correspond to “adjacent” primitive vectors related by unimodular transformations such as \((x,y)\mapsto(x\pm y,y)\) or \((x,x\pm y)\). [webhomes.maths.ed.ac](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/conwaysens.pdf)
- The whole structure is a tree-like planar graph (no cycles) with a highly regular local pattern.

This combinatorial graph is independent of the particular form; the form enters via the labels you assign to the regions.

***

## Labels: encoding the values of Q

To turn this combinatorial skeleton into the topograph of a specific form \(Q\), you label each region by the value of \(Q\) on its direction:

- Choose a representative primitive pair \((x,y)\) for each region.
- Attach the integer \(Q(x,y)\) to that region. [math.utah](http://www.math.utah.edu/vigre/ugrad/reu/sgp/ibqf.pdf)

Because each primitive direction appears exactly once, the topograph shows **all primitive values** of \(Q\) simultaneously. The action of \(\mathrm{SL}_2(\mathbb{Z})\) on forms corresponds to symmetries or re-embeddings of this labeled graph, which is why the topograph can also be used to represent an entire equivalence class of forms rather than a single form. [londmathsoc.onlinelibrary.wiley](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70042)

***

## Rivers, basins, and qualitative features

The real power of the concept comes from the global patterns that arise in these labels. [webhomes.maths.ed.ac](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/conwaysens.pdf)

- For indefinite forms (mixed signs), there is typically a **river**: an infinite path in the graph along which the values change sign on opposite sides, separating regions with positive values from regions with negative values. [math.utah](http://www.math.utah.edu/vigre/ugrad/reu/sgp/ibqf.pdf)
- For positive definite forms, you see **basins** or “lakes”: regions of small positive values surrounded by larger positive values, which visually encapsulate minima and reduction phenomena. [webhomes.maths.ed.ac](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/conwaysens.pdf)

These features are not arbitrary metaphors; they encode precise arithmetic data, such as:

- The minimal positive value represented by the form.
- How many times a given integer is represented.
- The structure of reduced forms and their relation to continued fractions (via the shape of the river). [londmathsoc.onlinelibrary.wiley](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70042)

***

## Relation to equivalence and reduction

The topograph interacts cleanly with Gauss’s equivalence of forms and reduction theory. [londmathsoc.onlinelibrary.wiley](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70042)

- Forms in the same equivalence class correspond to different ways of choosing “coordinates” on the same underlying labeled graph, or to re-labelings related by \(\mathrm{SL}_2(\mathbb{Z})\) symmetries. [londmathsoc.onlinelibrary.wiley](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70042)
- Reduction procedures (e.g. moving to a reduced form) correspond to traversing the topograph along certain canonical paths (typically following the river), which mirrors the continued-fraction interpretation of quadratic forms. [webhomes.maths.ed.ac](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/conwaysens.pdf)

From this perspective, the statement you quoted previously—“a number \(a\) appears on the topograph of \(Q\) iff it is the leading coefficient of some form equivalent to \(Q\)”—is the claim that:

- every primitive representation \(Q(x,y)=a\) shows up as a region label; and
- by taking \((x,y)\) as a new basis, you get an equivalent form with leading coefficient \(a\).

So “appears in the topograph” = “is a primitive value of some representative in the equivalence class”.

***

## Why this is useful

Compared to working only algebraically with triples \([A,B,C]\), the topograph gives a geometric/combinatorial handle on:

- solving representation problems (which integers are represented, and how often?),
- understanding reduction as movement in a tree,
- visualizing the effect of \(\mathrm{SL}_2(\mathbb{Z})\) on forms, and
- connecting quadratic forms to geodesics and tessellations in the hyperbolic plane. [londmathsoc.onlinelibrary.wiley](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70042)

In practice, for explicit low-discriminant forms, you can literally draw part of the topograph and read off small represented values and their multiplicities by inspection.

***

Would it be most helpful next to walk through a concrete example (say \(x^2+xy+y^2\) or \(x^2 - 2y^2\)) and sketch how a small patch of its topograph looks, or are you more interested in the hyperbolic-plane interpretation and relation to continued fractions?

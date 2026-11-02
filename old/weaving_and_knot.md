
Knot theory applies to weaving by treating the yarns as **curves in 3D space** and the over–under crossings as the data that determine their entanglement. A periodic weave becomes a **link diagram on a torus**, which lets you distinguish fabrics that may look similar locally but are topologically different globally. [arxiv](https://arxiv.org/abs/0806.2824v1)

## From weave to knot diagram

A knot diagram is a 2D projection with gaps showing which strand passes over at each crossing.  A woven fabric supplies exactly that information: at every warp–weft intersection, one thread is over and the other is under. [arxiv](https://arxiv.org/html/2604.09005v1)

For a small piece of plain weave, draw:

```text
vertical thread: over, under, over, under
horizontal thread: under, over, under, over
```

The drawing is a crossing diagram. If you connect the loose ends of the threads, you obtain a knot or link; with multiple yarns, it is generally a **link**, meaning several closed curves. [link.springer](https://link.springer.com/article/10.1007/s44217-025-01060-x?error=cookies_not_supported&code=33568e33-aae2-4114-9dd5-db87ec92ccb4)

The crucial point is that the actual fabric is not just the flat diagram: the yarns occupy a thin layer of 3D space. Two diagrams that differ by a Reidemeister move can represent the same underlying entanglement. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

## Periodicity gives a torus

A real woven fabric repeats in two directions. Take one repeating cell and identify:

- its left edge with its right edge;
- its top edge with its bottom edge.

The plane becomes a torus \(T^2\), and the yarns become curves in the **thickened torus** \(T^2 \times [0,1]\). This is the standard topological model for doubly periodic textile structures. [arxiv](https://arxiv.org/abs/0806.2824v1)

Schematically:

\[
\text{infinite periodic weave}
\quad\longrightarrow\quad
\text{finite repeat cell}
\quad\longrightarrow\quad
\text{link diagram on }T^2.
\]

This removes the artificial distinction between “inside” and “outside” a small sample: a yarn leaving the right edge re-enters from the left, just as it does in the physical fabric.

## Plain weave as a link

Consider a \(2\times2\) plain-weave cell:

\[
\begin{array}{c|c}
\text{warp over} & \text{warp under}\\
\hline
\text{warp under} & \text{warp over}
\end{array}
\]

Draw two vertical yarns and two horizontal yarns, mark the four crossings, then glue opposite sides. The result is a link in the thickened torus, not merely four separate crossings on a square.

For the common biaxial weaves, the topology can be represented using four curves: two yarn components plus two curves representing the two fundamental directions around the torus. A Kagome weave requires five. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

## What knot theory can distinguish

Knot theory is useful because it ignores incidental geometry—exact yarn thickness, slight curvature, or how tightly the cloth is drawn—and focuses on the invariant structure of the entanglement. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

It can distinguish questions such as:

| Question | Knot-theoretic formulation |
|---|---|
| Are two weave patterns fundamentally the same? | Are their torus links equivalent under allowed deformations? |
| How complex is a pattern? | How many crossings are needed in an irreducible diagram? |
| Are threads genuinely interlaced? | What are the linking and knotting properties of the components? |
| Does a larger repeat contain a smaller structural repeat? | Can its link invariant be recovered from a subgroup or covering? |
| What happens if one crossing is reversed? | Does the link invariant change? |

A crossing change reverses an over–under relationship. In ordinary knot theory, such changes can alter the knot type; in weaving, reversing selected crossings is precisely how one moves from plain weave to twill, satin, or another structural family. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

## Alexander polynomial: an algebraic fingerprint

One important invariant is the multivariable Alexander polynomial. For a textile, researchers construct an associated “kernel” link in ordinary 3-space and compute a normalized multivariable Alexander polynomial. This polynomial acts like a structural fingerprint of the weave. [arxiv](https://arxiv.org/abs/0806.2824v1)

It can reveal:

- whether the structure contains closed curves;
- how the pattern behaves under changes of scale;
- whether two fabrics with different-sized repeat cells share underlying topology;
- information about the arrangement of yarn components in the periodic structure. [arxiv](https://arxiv.org/abs/0806.2824v1)

The “multi-variable” part matters because a fabric has several meaningful directions or components: warp, weft, and the two periodic directions of the torus. A single-variable knot invariant would lose some of that structure.

## Weaving knots

There is also a technical class called **weaving knots**: alternating knots or links whose projection matches the standard projection of a torus knot. For \(W(p,q)\), the crossing number is

\[
c(W(p,q))=q(p-1).
\]

These are not necessarily literal cloth patterns, but they formalize the idea of an alternating, highly regular over–under arrangement resembling a woven grid. [wpi-aimr.tohoku.ac](https://www.wpi-aimr.tohoku.ac.jp/GTF2021/speaker-details.html)

For example, a finite patch of square weave can be closed into a weaving knot. Its hyperbolic geometry and diagrammatic complexity can then be studied through quantities such as volume density and determinant density. [arxiv](https://arxiv.org/html/2504.01747v2)

## A concrete experiment

Take a \(3\times3\) grid and assign crossings by

\[
A_{ij}=(i+j)\bmod 2.
\]

This gives a checkerboard/plain-weave pattern. Now change one entry from \(0\) to \(1\). Visually, you have changed one local over–under choice; topologically, you may have changed the associated torus link.

Ask:

1. Can the new diagram be simplified back to the original using Reidemeister moves?
2. Do the two patterns have the same Alexander polynomial?
3. Is the changed crossing essential, or can it be removed by choosing a different repeat cell?

That is knot theory applied directly to weaving: not “what does the cloth look like?” but “what entanglement does the cloth encode?” [arxiv](https://arxiv.org/abs/0806.2824v1)

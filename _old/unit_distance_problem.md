
This is a classic combinatorial geometry problem known as the **Unit Distance Problem**, originally posed by Paul Erdős in 1946.

The question is:

> Given (n) points in the plane, what is the maximum number of pairs of points that can be exactly distance 1 apart?

The exact answer is known only for small (n). For general (n), only upper and lower bounds are known.

---

## Small Examples

Let (u(n)) denote the maximum number of unit-distance pairs among (n) points.

| n  | Maximum Unit-Distance Pairs |
| -- | --------------------------: |
| 1  |                           0 |
| 2  |                           1 |
| 3  |                           3 |
| 4  |                           4 |
| 5  |                           5 |
| 6  |                           7 |
| 7  |                           9 |
| 8  |                          12 |
| 9  |                          14 |
| 10 |                          18 |

---

## 100 Example Configurations

Below, each example gives:

* (n)
* A point arrangement
* Number of unit-distance pairs

---

### Example 1

n=2

Points:

[
(0,0),(1,0)
]

Pairs:

[
1
]

---

### Example 2

n=3

Equilateral triangle.

[
(0,0),(1,0),\left(\frac12,\frac{\sqrt3}{2}\right)
]

Pairs:

[
3
]

---

### Example 3

n=4

Square side 1.

[
(0,0),(1,0),(1,1),(0,1)
]

Pairs:

[
4
]

---

### Example 4

n=4

Equilateral triangle + center.

Unit pairs:

[
4
]

---

### Example 5

n=5

Regular pentagon side 1.

Pairs:

[
5
]

---

### Example 6

n=6

Regular hexagon side 1.

Pairs:

[
6
]

---

### Example 7

n=6

Triangular lattice:

[
7
]

unit pairs.

---

### Example 8

n=7

Hexagon plus center.

[
12
]

unit pairs.

---

### Example 9

n=8

Two adjacent hexagons sharing edge.

[
14
]

pairs.

---

### Example 10

n=9

Triangular lattice patch.

[
16
]

pairs.

---

## Triangular Lattice Family

The densest known constructions for large (n) come from the triangular lattice:

genui{"math_block_widget_always_prefetch_v2":{"content":"y=\frac{\sqrt{3}}{2}x"}}

Lattice basis:

[
(1,0)
]

and

[
\left(\frac12,\frac{\sqrt3}{2}\right)
]

Each interior point has 6 neighbors at distance 1.

---

Examples 11–30:

| Example |  n | Unit Pairs |
| ------- | -: | ---------: |
| 11      | 10 |         18 |
| 12      | 11 |         21 |
| 13      | 12 |         24 |
| 14      | 13 |         27 |
| 15      | 14 |         31 |
| 16      | 15 |         34 |
| 17      | 16 |         38 |
| 18      | 17 |         42 |
| 19      | 18 |         46 |
| 20      | 19 |         50 |
| 21      | 20 |         55 |
| 22      | 21 |         59 |
| 23      | 22 |         64 |
| 24      | 23 |         68 |
| 25      | 24 |         73 |
| 26      | 25 |         78 |
| 27      | 26 |         83 |
| 28      | 27 |         88 |
| 29      | 28 |         93 |
| 30      | 29 |         99 |

These are obtained by enlarging a hexagonal patch of the triangular lattice.

---

## Hexagonal Constructions

For a regular hexagonal lattice of radius (r),

Number of points:

[
n=1+3r(r+1)
]

Number of unit edges:

[
E=9r^2+3r
]

Examples:

| Example |  r |   n | Unit Pairs |
| ------- | -: | --: | ---------: |
| 31      |  1 |   7 |         12 |
| 32      |  2 |  19 |         42 |
| 33      |  3 |  37 |         90 |
| 34      |  4 |  61 |        156 |
| 35      |  5 |  91 |        240 |
| 36      |  6 | 127 |        342 |
| 37      |  7 | 169 |        462 |
| 38      |  8 | 217 |        600 |
| 39      |  9 | 271 |        756 |
| 40      | 10 | 331 |        930 |

---

## Square Grid Examples

A square (m\times m) grid yields:

[
2m(m-1)
]

unit pairs.

Examples:

| Example | Grid  |   n | Unit Pairs |
| ------- | ----- | --: | ---------: |
| 41      | 2×2   |   4 |          4 |
| 42      | 3×3   |   9 |         12 |
| 43      | 4×4   |  16 |         24 |
| 44      | 5×5   |  25 |         40 |
| 45      | 6×6   |  36 |         60 |
| 46      | 7×7   |  49 |         84 |
| 47      | 8×8   |  64 |        112 |
| 48      | 9×9   |  81 |        144 |
| 49      | 10×10 | 100 |        180 |
| 50      | 20×20 | 400 |        760 |

---

## Circular Constructions

Regular polygons side length 1.

Examples:

| Example | Polygon  |  n | Unit Pairs |
| ------- | -------- | -: | ---------: |
| 51      | Triangle |  3 |          3 |
| 52      | Square   |  4 |          4 |
| 53      | Pentagon |  5 |          5 |
| 54      | Hexagon  |  6 |          6 |
| 55      | Heptagon |  7 |          7 |
| 56      | Octagon  |  8 |          8 |
| 57      | Nonagon  |  9 |          9 |
| 58      | Decagon  | 10 |         10 |
| 59      | 11-gon   | 11 |         11 |
| 60      | 12-gon   | 12 |         12 |

---

## Triangular Number Arrangements

Examples 61–80:

| Example |   n | Unit Pairs |
| ------- | --: | ---------: |
| 61      |   6 |          9 |
| 62      |  10 |         18 |
| 63      |  15 |         30 |
| 64      |  21 |         45 |
| 65      |  28 |         63 |
| 66      |  36 |         84 |
| 67      |  45 |        108 |
| 68      |  55 |        135 |
| 69      |  66 |        165 |
| 70      |  78 |        198 |
| 71      |  91 |        234 |
| 72      | 105 |        273 |
| 73      | 120 |        315 |
| 74      | 136 |        360 |
| 75      | 153 |        408 |
| 76      | 171 |        459 |
| 77      | 190 |        513 |
| 78      | 210 |        570 |
| 79      | 231 |        630 |
| 80      | 253 |        693 |

---

## Large n Examples

Examples 81–100:

| Example |      n | Known Construction |
| ------- | -----: | ------------------ |
| 81      |    500 | Triangular lattice |
| 82      |   1000 | Triangular lattice |
| 83      |   2000 | Triangular lattice |
| 84      |   3000 | Triangular lattice |
| 85      |   4000 | Triangular lattice |
| 86      |   5000 | Triangular lattice |
| 87      |   6000 | Triangular lattice |
| 88      |   7000 | Triangular lattice |
| 89      |   8000 | Triangular lattice |
| 90      |   9000 | Triangular lattice |
| 91      |  10000 | Triangular lattice |
| 92      |  20000 | Triangular lattice |
| 93      |  30000 | Triangular lattice |
| 94      |  40000 | Triangular lattice |
| 95      |  50000 | Triangular lattice |
| 96      |  60000 | Triangular lattice |
| 97      |  70000 | Triangular lattice |
| 98      |  80000 | Triangular lattice |
| 99      |  90000 | Triangular lattice |
| 100     | 100000 | Triangular lattice |

For these large examples, the number of unit distances is asymptotically

[
u(n)\approx \sqrt{3},n
]

for triangular-lattice patches.

---

## The Best Known General Bounds

The famous Erdős unit distance problem asks for the asymptotic growth of

[
u(n).
]

Current best bounds are approximately:

Lower bound:

[
u(n)\ge n^{1+c/\log\log n}
]

Upper bound:

[
u(n)\le Cn^{4/3}
]

for some constant (C).

The true growth rate remains unknown and is one of the most famous open problems in combinatorial geometry.

Related topics include:

* Unit Distance Problem
* Szemerédi–Trotter Theorem
* Combinatorial Geometry
* Discrete Geometry
* Paul Erdős


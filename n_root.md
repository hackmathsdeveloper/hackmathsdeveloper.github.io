
“Doubling the cube” is impossible only with an unmarked straightedge and compass: starting with side \(1\), a cube of twice the volume would need side \(\sqrt [math.clemson](https://www.math.clemson.edu/~macaule/classes/m20_math4120/slides/math4120_lecture-6-08_h.pdf){2}\), which is not constructible. By contrast, multiplying a cube’s volume by a **perfect cube** is constructible, because its new side length is an integer (or another constructible number). [math.libretexts](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Abstract_Algebra:_Theory_and_Applications_(Judson)/21:_Fields/21.03:_Geometric_Constructions)

## Rule for each shape

| Shape | Original measure | Multiply by \(m\) | Required scale of length | Constructible when |
|---|---:|---:|---:|---|
| Cube | Volume \(s^3\) | \(m s^3\) | \(\sqrt [math.clemson](https://www.math.clemson.edu/~macaule/classes/m20_math4120/slides/math4120_lecture-6-08_h.pdf){m}\) | \(\sqrt [math.clemson](https://www.math.clemson.edu/~macaule/classes/m20_math4120/slides/math4120_lecture-6-08_h.pdf){m}\) is constructible |
| Square | Area \(s^2\) | \(m s^2\) | \(\sqrt m\) | \(\sqrt m\) is constructible |
| Circle | Area \(\pi r^2\) | \(m\pi r^2\) | \(\sqrt m\) | \(\sqrt m\) is constructible |

For rational \(m\), cube multiplication is constructible exactly when \(m\) is a rational perfect cube; square and circle multiplication by any positive rational \(m\) is constructible because square roots can be constructed. [math.libretexts](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Abstract_Algebra:_Theory_and_Applications_(Judson)/21:_Fields/21.03:_Geometric_Constructions)

## Ten constructible examples

Assume the original cube has side \(1\), the square has side \(1\), and the circle has radius \(1\).

| # | Figure | Multiplier \(m\) | Construction result |
|---:|---|---:|---|
| 1 | Cube | \(8=2^3\) | New side \(2\); volume becomes \(8\) |
| 2 | Cube | \(27=3^3\) | New side \(3\); volume becomes \(27\) |
| 3 | Cube | \(64=4^3\) | New side \(4\); volume becomes \(64\) |
| 4 | Cube | \(1/8=(1/2)^3\) | New side \(1/2\); volume becomes \(1/8\) |
| 5 | Square | \(2\) | New side \(\sqrt2\); area becomes \(2\) |
| 6 | Square | \(3\) | New side \(\sqrt3\); area becomes \(3\) |
| 7 | Square | \(5\) | New side \(\sqrt5\); area becomes \(5\) |
| 8 | Square | \(1/2\) | New side \(1/\sqrt2\); area becomes \(1/2\) |
| 9 | Circle | \(2\) | New radius \(\sqrt2\); area becomes \(2\pi\) |
| 10 | Circle | \(9\) | New radius \(3\); area becomes \(9\pi\) |

## Important contrasts

- Cube multiplier \(2\): **not constructible**, since it requires \(\sqrt [math.clemson](https://www.math.clemson.edu/~macaule/classes/m20_math4120/slides/math4120_lecture-6-08_h.pdf){2}\). [math.libretexts](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Abstract_Algebra:_Theory_and_Applications_(Judson)/21:_Fields/21.03:_Geometric_Constructions)
- Square multiplier \(2\): constructible, since it requires \(\sqrt2\).
- Circle-area multiplier \(2\): constructible, since it only requires scaling the radius by \(\sqrt2\).
- Making a square with the **same area as a unit circle** is not constructible: it would require a square side of \(\sqrt{\pi}\), and \(\pi\) is transcendental. [math.libretexts](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Abstract_Algebra:_Theory_and_Applications_(Judson)/21:_Fields/21.03:_Geometric_Constructions)

So the key distinction is: **squares and circles use square roots for area scaling; cubes use cube roots for volume scaling.**

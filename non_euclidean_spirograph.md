
# Non-Euclidean Hyperbolic Spirographs: When Rolling Circles Enter Curved Space

*What happens when the rules of Spirograph are applied to a universe with negative curvature? Discover how hypotrochoids, epitrochoids, and rotating geometric systems can be transformed into intricate patterns inside the Poincaré disk.*

## 1. From familiar spirographs to an unfamiliar universe

A Spirograph is a deceptively simple mathematical machine. A circle rolls around another circle, a point attached to the moving circle traces a path, and a small collection of radii and rotation rates produces an astonishing variety of flowers, loops, stars, and interlocking curves.

In the [Mathematical Art gallery](https://tthtlc.github.io/index_gallery.html), the Spirographs & Rolling Curves collection brings together 62 visualizations, including hypotrochoids, epitrochoids, cardioids, rotating circles, and combinations of moving geometric objects. The wider gallery also explores lemniscates, polygon-chasing systems, fractals, and three-dimensional surfaces.

But there is a deeper question waiting beyond these Euclidean constructions:

**What happens if the rolling circles inhabit a space where the geometry itself is curved?**

Imagine replacing the flat drawing surface with a hyperbolic plane. The familiar circular motions now have to obey a different distance metric. Paths that seem ordinary near the centre may become dramatically distorted in the disk representation. A curve can sweep through the interior while its repeated structures become increasingly fine near the circular boundary.

The result is a new family of mathematical-art experiments: **non-Euclidean hyperbolic spirographs**.

The aim is not merely to decorate an ordinary spirograph with a circular frame. It is to investigate what happens when the geometry governing the curve is changed.

## 2. The Euclidean engine: hypotrochoids and epitrochoids

Before changing the geometry, let us understand the mechanism that generates the original curves.

### Hypotrochoids: rolling on the inside

Consider a fixed circle of radius \(R\). A smaller circle of radius \(r\) rolls along its interior. Attach a drawing point at distance \(d\) from the centre of the moving circle.

One standard parametrisation of the resulting hypotrochoid is

\[
\begin{aligned}
x(t)&=(R-r)\cos t\\
&\quad+d\cos\left(\frac{R-r}{r}t\right),\\[5pt]
y(t)&=(R-r)\sin t\\
&\quad-d\sin\left(\frac{R-r}{r}t\right).
\end{aligned}
\]

The two terms in each coordinate encode two motions: the movement of the small circle's centre around the larger circle and the rotation of the drawing point relative to that centre.

Changing the radius ratio \(R/r\) changes the relative angular frequencies. Changing \(d\) moves the pen point closer to or farther from the wheel's centre, creating cusps, rounded petals, or self-intersecting loops.

Explore the existing [interactive hypotrochoid and hypocycloid visualization](https://tthtlc.github.io/hypocycloid_explore.html) to see how the radii and drawing-point offset alter the shape.

### Epitrochoids: rolling on the outside

Now let the small circle roll around the exterior of the fixed circle. A corresponding parametrisation is

\[
\begin{aligned}
x(t)&=(R+r)\cos t\\
&\quad-d\cos\left(\frac{R+r}{r}t\right),\\[5pt]
y(t)&=(R+r)\sin t\\
&\quad-d\sin\left(\frac{R+r}{r}t\right).
\end{aligned}
\]

The difference between \(R-r\) and \(R+r\) changes the relationship between the orbital and rotational motions. That simple change produces a different family of curves.

These equations work beautifully in ordinary Euclidean geometry. However, both the circular paths and the rolling relationships rely on the geometry of a flat plane.

To create a genuinely hyperbolic spirograph, we need to reconsider the geometry behind the mechanism itself.

## 3. Welcome to the Poincaré disk

The Poincaré disk is one of the most visually compelling models of hyperbolic geometry.

Represent the hyperbolic plane by the interior of a unit circle:

\[
\mathbb D=\{(x,y):x^2+y^2<1\}.
\]

Every point lies strictly inside the disk. Its circular boundary represents points at infinity rather than an ordinary edge that an object can reach.

The important change is the metric. Instead of measuring infinitesimal distances using the familiar Euclidean expression \(dx^2+dy^2\), we use

\[
\boxed{
ds^2=
\frac{4(dx^2+dy^2)}
{(1-x^2-y^2)^2}
}
\]

This is the Poincaré disk metric for constant curvature \(-1\). It is the mathematical foundation of the model; see the reference on the [Poincaré disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model).

Notice the denominator. As a point approaches the unit circle, \(x^2+y^2\) approaches \(1\), causing the metric factor to grow without bound.

A small Euclidean movement close to the boundary can therefore represent a much larger hyperbolic distance than an equally small movement near the centre.

This is the central visual idea behind hyperbolic spirographs.

### Why the boundary creates infinite detail

Let \(\rho=\sqrt{x^2+y^2}\) be the ordinary Euclidean distance from the centre of the displayed disk. The hyperbolic distance \(s\) from the origin to that point is

\[
s=2\,\operatorname{artanh}(\rho)
=\ln\left(\frac{1+\rho}{1-\rho}\right).
\]

Consider two locations:

- At \(\rho=0.9\), the hyperbolic distance is approximately \(2.94\).
- At \(\rho=0.99\), the hyperbolic distance is approximately \(5.29\).

Although the displayed Euclidean radii differ by only \(0.09\), their hyperbolic distances from the centre differ by more than \(2.35\) units.

As \(s\) increases, the corresponding displayed radius satisfies

\[
\rho=\tanh\left(\frac{s}{2}\right).
\]

For large \(s\),

\[
1-\rho\approx 2e^{-s}.
\]

In other words, equal increments of hyperbolic distance become exponentially compressed toward the edge of the diagram.

This explains the signature visual effect: repeated structures can become progressively finer near the boundary, while comparable structures appear larger and more open toward the centre.

The boundary is not physically squeezing a wheel. It is the way the model represents an infinite hyperbolic plane inside a finite Euclidean drawing.

## 4. What makes a spirograph genuinely hyperbolic?

Here we must distinguish two related but different constructions.

**A hyperbolically warped spirograph** starts with an ordinary Euclidean curve and transforms its coordinates to create a Poincaré-disk-like appearance. This is relatively straightforward and can produce beautiful artwork.

**A true hyperbolic rolling curve** defines the circles, distances, and rolling motion using hyperbolic geometry from the beginning. This is a more demanding mathematical construction.

Why does the distinction matter?

In Euclidean geometry, a circle of radius \(r\) has circumference

\[
C_{\mathrm E}=2\pi r.
\]

In the hyperbolic plane of curvature \(-1\), a circle of hyperbolic radius \(r\) has circumference

\[
C_{\mathrm H}=2\pi\sinh(r).
\]

The latter grows faster than the Euclidean circumference as \(r\) increases. Consequently, the familiar ratios between rolling-circle radii cannot simply be carried over unchanged.

A hyperbolic circle is defined by a fixed hyperbolic distance from its centre. A point rolling on that circle must follow motion consistent with the hyperbolic metric, including the way directions and distances behave across the curved space.

The Euclidean hypotrochoid formula is therefore a useful starting point, but it is not, by itself, a formula for hyperbolic rolling.

For mathematical-art development, it is worthwhile to explore both constructions and label them clearly. The first offers immediate artistic flexibility; the second explores the geometry more faithfully.

## 5. Designing the visual signature

The proposed visual identity of a Non-Euclidean Hyperbolic Spirograph is a circular field filled with increasingly fine geometric detail.

Picture a curve beginning as delicate, densely packed arcs near the circular boundary. As the trajectory moves inward, the loops become larger and more widely separated. Several families of curves cross and recross one another, creating a radial web around the central region.

The design may combine several effects.

**Boundary compression.** Repeated loops appear smaller near the rim because equal hyperbolic distances occupy less Euclidean display space there.

**Radial expansion.** Moving inward reveals larger apparent features and broader loops.

**Curvature-driven distortion.** A curve that resembles a familiar circular pattern near the centre may look strongly warped farther away.

**Interference between motions.** Combining different angular frequencies or multiple rolling systems produces intersections, petal structures, and dense networks of lines.

One important qualification: this appearance is a design goal, not a universal theorem about every hyperbolic curve. The metric explains the compression of hyperbolic distances in the disk, but the final pattern also depends on the curve, its parameters, the transformation, and the rendering choices.

This is where mathematical constraints and artistic exploration meet. The equations determine which patterns are possible; the visualization reveals which ones are compelling.

## 6. A first implementation: compressing a Euclidean curve into the disk

A simple prototype can use any existing hypotrochoid generator and then map its points radially into the Poincaré disk.

Suppose a point on the original curve has Euclidean coordinates \((x,y)\), and let

\[
r_{\mathrm E}=\sqrt{x^2+y^2}.
\]

Treat the scaled radial coordinate \(\lambda r_{\mathrm E}\) as a chosen hyperbolic radial distance. Map it to the displayed radius

\[
\rho=\tanh\left(\frac{\lambda r_{\mathrm E}}{2}\right).
\]

The resulting coordinates are

\[
x_{\mathbb D}=\rho\frac{x}{r_{\mathrm E}},
\qquad
y_{\mathbb D}=\rho\frac{y}{r_{\mathrm E}},
\]

with the origin mapped to itself. Here, \(\lambda\) controls the scale of the artistic transformation.

A JavaScript implementation is short:

```javascript
function mapToDisk(x, y, scale = 0.01) {
  const r = Math.hypot(x, y);

  if (r < 1e-12) {
    return { x: 0, y: 0 };
  }

  const rho = Math.tanh(0.5 * scale * r);

  return {
    x: rho * x / r,
    y: rho * y / r
  };
}
```

Feed each point generated by a hypotrochoid or epitrochoid into `mapToDisk()`, then connect the transformed points in their original parametric order.

The output always lies inside the unit disk, because \(\tanh(u)<1\) for finite positive \(u\).

The `scale` parameter determines how quickly the transformed curve approaches the boundary. Larger values produce stronger radial compression for the same input coordinates.

**This is a radial artistic mapping, not a simulation of hyperbolic rolling.** In particular, the input radii are Euclidean coordinates, and the transformation does not enforce hyperbolic no-slip contact between moving circles. It is an effective first experiment for studying the visual language of disk-based spirographs.

A more faithful implementation would generate the rolling motion directly from hyperbolic distances and circle geometry, then render the resulting trajectory in the disk model.

## 7. Möbius transformations: moving the pattern without changing its geometry

The Poincaré disk has another useful mathematical feature: its distance-preserving transformations can move and rotate patterns without changing their hyperbolic geometry.

In complex coordinates \(z=x+iy\), an orientation-preserving disk isometry can be written as

\[
f(z)=e^{i\theta}
\frac{z-a}{1-\overline{a}z},
\qquad |a|<1.
\]

Here, \(a\) determines a displacement within the disk and \(\theta\) controls rotation. The overline denotes complex conjugation.

Unlike ordinary Euclidean translation, this transformation preserves hyperbolic distances and angles within the model. It also keeps the disk mapped onto itself.

This makes Möbius transformations useful for creating families of related pictures. A hyperbolic rolling curve can be generated once and then repositioned through disk isometries to produce a collection of geometrically equivalent variants.

For more on the mathematical basis, see these [university lecture notes on hyperbolic geometry and disk isometries](https://www.math.uci.edu/~ndonalds/math161/hyper.pdf).

## 8. An Escher-inspired universe of curves

The visual comparison with M. C. Escher is particularly appropriate.

His *Circle Limit* works show figures arranged in the Poincaré disk, with repeated motifs becoming progressively smaller near the circular edge. These images use hyperbolic tessellation rather than spirograph motion, but they demonstrate how negative curvature can transform a geometric construction into an apparently endless pattern.

See the [Escher in the Palace Museum's discussion of *Circle Limit IV*](https://escherinhetpaleis.nl/en/about/escher-today/circle-limit-iv-heaven-and-hell).

A hyperbolic spirograph could create a related sense of infinity using continuously traced curves rather than repeated tiled figures.

Imagine combining several hypotrochoid-like trajectories, each with a slightly different frequency ratio, then adding selected disk isometries and contrasting colours. The central region might reveal large, almost floral structures, while the outer region develops delicate rings, crossings, and fine filaments.

Unlike a conventional rosette, its complexity would be shaped not just by the ratios of the rotating components but also by how the underlying geometry is represented.

The result would not be an illustration of Escher's work. It would be another route to the same mathematical fascination: discovering an enormous visual world inside a bounded circular frame.

## 9. Experiments for an interactive hyperbolic spirograph

The existing [Mathematical Art gallery](https://tthtlc.github.io/index_gallery.html) already provides a natural starting point for a new interactive visualization.

A dedicated explorer could expose several groups of parameters:

| Control | Mathematical or visual effect |
|---|---|
| Fixed radius \(R\) | Changes the large-scale circular structure |
| Rolling radius \(r\) | Changes the ratio of orbital and rotational motion |
| Drawing offset \(d\) | Changes cusps, petals, and self-intersections |
| Curvature scale | Controls the scale of hyperbolic distances and the disk mapping |
| Angular frequencies | Changes periodicity and rotational symmetry |
| Number of curve families | Controls the density of the geometric web |
| Phase offsets | Rotates or displaces the relationship between trajectories |
| Line density and colour | Reveals overlaps and emphasizes boundary detail |

Two rendering modes would be especially valuable.

In **Artistic Disk Mode**, existing Euclidean spirographs are transformed into the disk. This mode is fast, suitable for experimentation, and compatible with the current collection of JavaScript curve generators.

In **Hyperbolic Geometry Mode**, circles and trajectories are defined using the hyperbolic metric, with rolling constraints derived from the curved geometry. This mode is more mathematically demanding, but it allows experiments to reveal how negative curvature changes the motion itself.

The comparison between the two modes would teach an important lesson: an image can resemble hyperbolic geometry without every operation used to generate it being hyperbolic.

## 10. A new direction for mathematical art

Non-Euclidean Hyperbolic Spirographs sit at the intersection of geometry, dynamical systems, complex analysis, and computer graphics.

They begin with the familiar question of how rotating circles combine to draw a curve. Then they replace the flat geometric setting with one in which distance increases dramatically toward the boundary and the ordinary relationships between lengths no longer apply.

From that change comes a different visual language: sweeping loops in the interior, densely compressed details at the rim, and radial webs that suggest structures extending far beyond the limits of the image.

The most interesting results will come from moving between mathematical modes rather than treating every disk-shaped picture as the same construction. A radial transformation can give us an immediate artistic playground, while metric-based rolling can reveal the deeper consequences of negative curvature.

The challenge is to make both approaches explorable: to let a reader alter the radii and rotation rates, observe the geometry unfold, and discover how much a seemingly small change in the underlying rules can transform the entire picture.

**What happens when Spirograph rules enter curved space?** The answer is a new family of geometric experiments in which familiar circles become the starting point for exploring a space of seemingly endless patterns.

### Further reading and exploration

- [Mathematical Art — interactive gallery](https://tthtlc.github.io/index_gallery.html)
- [Existing hypotrochoid explorer](https://tthtlc.github.io/hypocycloid_explore.html)
- [Epicycles: One Arm, Two Arms, Three Arms](https://tthtlc.github.io/blog/2026/09/13/epicycles-one-two-three-arms/)
- [Poincaré disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model)
- [Hyperbolic geometry and disk isometries — university lecture notes](https://www.math.uci.edu/~ndonalds/math161/hyper.pdf)
- [Escher in the Palace — *Circle Limit IV*](https://escherinhetpaleis.nl/en/about/escher-today/circle-limit-iv-heaven-and-hell)


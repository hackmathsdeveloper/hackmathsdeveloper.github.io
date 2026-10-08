# Recursive branching curves: a mathematical gallery

The screenshot is best described as a **fractal tree**, specifically a curved recursive branching tree. It does not uniquely determine a named construction or generating equation. This gallery explains the six illustrative constructions from the earlier webpage, rather than claiming to recover the original video's algorithm.

Markdown is static: the sliders become parameters, and the live previews are replaced with schematic diagrams, equations, and recursion rules. Diagrams show branching topology only, not exact angles or curvature.

## Shared notation and recursion

Work in mathematical coordinates with positive y pointing upward. Define

\[
u(\theta)=(\cos\theta,\sin\theta).
\]

A branch state is \((P,\theta,L,n)\): starting point, direction, length parameter, and remaining depth. Start with \(P=(0,0)\), \(\theta=\pi/2\), \(L=L_0>0\), and \(n=D\).

The shared parameters are:

| Parameter | Meaning | Earlier webpage default |
|---|---|---|
| \(D\) | Number of branch generations drawn | 8 |
| \(\alpha\) | Branching angle | \(28^\circ\) |
| \(r\) | Child-to-parent length-parameter ratio | 0.68 |
| \(\beta\) | Curved-branch turning parameter | 0.22 radians |

Convert angles to radians before using trigonometric functions. Stop when \(n=0\); an optional minimum-length threshold is useful in a renderer.

For two children per branch and a root counted as generation zero, depth \(D\) draws

\[
N(D)=1+2+\cdots+2^{D-1}=2^D-1
\]

branches. The drawing cost is \(O(2^D)\); a depth-first implementation uses \(O(D)\) stack space, excluding any stored geometry.

For equal scaling, a generation-k branch has length parameter

\[
L_k=L_0r^k.
\]

Along one descendant path, the sum of these length parameters is bounded by \(L_0/(1-r)\) when \(0<r<1\). This is different from the sum over all branches: for straight equal-scale binary trees, the latter is \(L_0\sum_{k=0}^{D-1}(2r)^k\), which converges as depth increases only when \(2r<1\).

## 1. Curved recursive tree

Closest visual match to the supplied image. This is a descriptive label, not a uniquely named curve.

```text
             smaller curved subtrees
                    ↖   ↗
                     \ /
              ↖       )       ↗
               \     /       /
                curved parent
                      |
```

### Branch geometry: quadratic Bézier curve

The earlier webpage used a quadratic Bézier curve with start point \(P\), control point \(C\), and endpoint \(Q\):

\[
C=P+0.52L\,u(\theta),\qquad
Q=P+L\,u(\theta+\beta/2),
\]

\[
B(t)=(1-t)^2P+2(1-t)tC+t^2Q,
\qquad 0\le t\le1.
\]

Thus \(L\) is the endpoint chord length, not the exact arc length. Its actual arc length is \(\int_0^1\|B'(t)\|\,dt\).

### Recursive rule

After drawing \(B\), spawn two children at \(Q\):

\[
T(P,\theta,L,n)\longrightarrow
\begin{cases}
T(Q,\theta+\beta-\alpha,rL,n-1),\\
T(Q,\theta+\beta+\alpha,rL,n-1).
\end{cases}
\]

The same signed bend on every branch introduces a directional bias, so this curved construction is not exactly mirror symmetric.

The webpage's \(\theta+\beta\) is a nominal end direction. It is not guaranteed to equal the actual Bézier end-tangent direction, which is

\[
\theta_{\rm end}=\operatorname{atan2}(Q_y-C_y,Q_x-C_x),
\qquad B'(1)=2(Q-C).
\]

For tangent-relative branching, replace \(\theta+\beta\) with \(\theta_{\rm end}\). Children at angles \(\theta_{\rm end}\pm\alpha\) still form intentional junction angles; this does not make both child paths smoothly tangent to the parent.

## 2. Binary fractal tree

The basic two-child recursive model. “Binary” specifies the number of children, not a particular angle or ratio.

```text
        /\       /\
       /  \     /  \
          \     /
           \   /
            \ /
             |
```

### Branch geometry and recursion

Draw the segment from \(P\) to

\[
Q=P+L\,u(\theta).
\]

Then recurse:

\[
T(P,\theta,L,n)\longrightarrow
\begin{cases}
T(Q,\theta-\alpha,rL,n-1),\\
T(Q,\theta+\alpha,rL,n-1).
\end{cases}
\]

For a path encoded by signs \(\sigma_j\in\{-1,+1\}\),

\[
\theta_k=\theta_0+\alpha\sum_{j=1}^k\sigma_j,
\qquad
P_{k+1}=P_k+L_0r^k u(\theta_k).
\]

These equations construct any root-to-descendant path directly.

### Pseudocode

```text
TREE(P, theta, L, n):
    if n == 0: return
    Q = P + L * (cos(theta), sin(theta))
    draw_segment(P, Q)
    TREE(Q, theta - alpha, r * L, n - 1)
    TREE(Q, theta + alpha, r * L, n - 1)
```

## 3. Symmetric fractal canopy

A standard symmetric instance of a binary fractal tree: both children use the same ratio and opposite branching angles. Its geometry is therefore the same as entry 2 with equal left/right parameters. The earlier webpage intentionally displayed the same construction under these related labels; they are not two independent curve families.

```text
       left subtree | right subtree
              \     |     /
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
```

### Self-similarity as a set equation

Normalize the root to the segment

\[
S=\{(0,t):0\le t\le1\},\qquad A=(0,1).
\]

Let

\[
R_\phi=
\begin{pmatrix}
\cos\phi&-\sin\phi\\
\sin\phi&\cos\phi
\end{pmatrix},
\qquad
f_\pm(X)=A+rR_{\pm\alpha}X.
\]

Finite-depth sets satisfy

\[
K_0=\varnothing,\qquad
K_D=S\cup f_-(K_{D-1})\cup f_+(K_{D-1}).
\]

The ideal limiting tree obeys

\[
K=S\cup f_-(K)\cup f_+(K).
\]

The explicit trunk \(S\) matters: omitting it describes a different self-similar set, generally the endpoint attractor rather than the full branch skeleton.

### Dimension caveat

The similarity-dimension equation for the associated two-map endpoint attractor is

\[
2r^s=1,\qquad s=\frac{\log 2}{\log(1/r)}.
\]

This equals its Hausdorff dimension only under suitable separation conditions, such as the open set condition. It is not an unconditional dimension formula for an overlapping canopy or the full tree. For the closure of the branch skeleton in a nondegenerate separated case, the segments contribute dimension 1 and the endpoint set contributes s, giving \(\max(1,s)\). Overlaps require separate analysis, and any planar set has Hausdorff dimension at most 2. A finite drawing is only a finite union of segments or smooth arcs.

## 4. Asymmetric fractal tree

Unequal child angles or scaling factors break the mirror symmetry while retaining a repeated rule.

```text
          /\
         /  \       /\
        /    \     /  \
              \   /
               \ /
                |
```

### General recurrence

Draw \(P\to Q=P+Lu(\theta)\), then use

\[
T(P,\theta,L,n)\longrightarrow
\begin{cases}
T(Q,\theta-\alpha_L,r_LL,n-1),\\
T(Q,\theta+\alpha_R,r_RL,n-1).
\end{cases}
\]

The earlier webpage chose

\[
\alpha_L=\alpha,\quad\alpha_R=1.4\alpha,
\qquad r_L=r,\quad r_R=0.82r.
\]

A descendant reached by choices \(b_1,\ldots,b_k\in\{L,R\}\) has

\[
L_k=L_0\prod_{j=1}^k r_{b_j}.
\]

For the associated endpoint attractor with suitable separation, the similarity dimension solves

\[
r_L^s+r_R^s=1.
\]

Usually this equation is solved numerically. As with the symmetric canopy, it is not automatically the dimension of the full branch skeleton.

## 5. Fern-like recursive tree

A descriptive construction with a continuing stem and a smaller side subtree. It is not the Barnsley fern algorithm, which is a different affine-IFS construction.

```text
            )
       ----)
           )
      ----)
          )
     ----)
         |
```

### Branch and attachment geometry

Draw the same Bézier branch \(B(t)\) as entry 1. Let \(\theta_e=\theta+\beta\) denote the webpage's nominal end direction, and choose

\[
\lambda=0.62,\qquad c=0.57,\qquad\delta=0.06.
\]

The earlier webpage attached the side branch at

\[
A=P+\lambda(Q-P).
\]

Then it spawned

\[
\begin{aligned}
\text{continuation: }&T(Q,\theta_e-\delta,rL,n-1),\\
\text{side subtree: }&T(A,\theta_e+1.9\alpha,crL,n-1).
\end{aligned}
\]

Both children repeat this same rule. The side child is shorter, but it is itself a branching subtree, not just one leaf stroke.

### More geometrically faithful attachment

The original attachment point lies on the chord \(PQ\), not generally on the curved branch. To attach directly to the drawn stem, use

\[
A=B(\lambda),\qquad
\theta_A=\operatorname{atan2}(B'_y(\lambda),B'_x(\lambda)),
\]

\[
B'(t)=2(1-t)(C-P)+2t(Q-C).
\]

Then define the side direction relative to \(\theta_A\), for example \(\theta_A+1.9\alpha\). Note that \(t=0.62\) is a Bézier parameter, not necessarily 62% of the arc length. Alternating the sign of the side angle can produce foliage on both sides, but that would be a modification of the earlier preview.

## 6. Radial branching tree

Several recursive trees share one center. This is a descriptive arrangement rather than a separate standard named fractal curve.

```text
            tree
             |
     tree -- center -- tree
            /     \
         tree     tree
```

### Multiple initial directions

Choose \(m\) initial directions

\[
\theta_j=\theta_0+\frac{2\pi j}{m},
\qquad j=0,\ldots,m-1.
\]

Then run the symmetric binary-tree recursion independently for each:

\[
\mathcal R_D=\bigcup_{j=0}^{m-1}
T(P_0,\theta_j,\kappa L_0,D).
\]

The webpage used \(m=5\) and \(\kappa=0.47\), reducing the initial length to fit the drawing area. Its nominal branch count, before coincident geometry is merged, is

\[
N_{\rm radial}(D)=m(2^D-1).
\]

Equal spacing gives rotational symmetry of order m when each initial tree uses the same rule. Taking finitely many rotated copies of a set does not change its Hausdorff dimension, although overlaps can change its visible appearance.

## Implementation notes

- Browser canvas coordinates have y increasing downward. Use initial angle \(-\pi/2\), or transform mathematical coordinates by \((x,y)\mapsto(x_0+x,y_0-y)\).
- A consistent positive bend appears clockwise in ordinary canvas coordinates, but counterclockwise in the mathematical convention used here.
- Keep geometry separate from styling. The earlier webpage decreased stroke width approximately as \(3.7(0.73)^k\), with a minimum width, and changed color by generation. These choices do not change the mathematical branch set.
- Depth, ratio, and angle control different properties: amount of detail, scale decay, and spread. Increasing depth alone does not change the recursive rule.
- Not every self-similar branching construction has a noninteger dimension. Dimension depends on which set is measured and on overlap and separation.

## Sources and further exploration

- [Processing: recursive tree example](https://processing.org/examples/tree.html)
- [Yale: dimensions of fractal trees](https://gauss.math.yale.edu/fractals/FracTrees/welcome.html)
- [Fractal canopy: standard binary construction](https://en.wikipedia.org/wiki/Fractal_canopy)
- [Smooth Fractal Trees: Analytic Generators and Discrete Equivalence — preprint](https://arxiv.org/pdf/2601.17490v1.pdf)

The specific Bézier constants, asymmetric ratios, fern attachment rule, and radial arrangement above document the earlier generated webpage. They are illustrative design choices, not formulas attributed to these sources.

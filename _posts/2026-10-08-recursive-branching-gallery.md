---
title: "One Recursion, Six Forests — the Branching Secret Behind Every Fractal Tree"
date: 2026-10-08
categories:
  - Fractals
  - Mathematics
tags:
  - fractal-trees
  - recursive-branching
  - bezier-curves
  - self-similarity
  - iterated-function-systems
  - hausdorff-dimension
share: true
read_time: true
excerpt: "Six branching constructions — curved trees, canopies, fern-like stems, and radial forests — all emerge from one recursive rule. We write down the exact recursions, the Bézier geometry, and the similarity-dimension equations, and show why finite drawings only approximate the ideal fractal tree."
---

**Challenge to the reader:** A recursive tree draws two children per branch, each shrunk by a factor $r=0.68$, stopping after depth $D=8$. Before reading on, predict: how many segments does it draw, and does the total length of everything it draws stay finite as $D$ grows? Verify both predictions against the formulas in Sections 1–3.

The screenshot is best described as a **fractal tree**, specifically a curved recursive branching tree. It does not uniquely determine a named construction or generating equation. This gallery explains the six illustrative constructions from the earlier webpage, rather than claiming to recover the original video's algorithm.

The drawings below are not static: the canvas code from the gallery is embedded in this page, so every figure is drawn live by the recursion rule written out beside it. The sliders use the gallery's defaults (depth 8, angle $28^\circ$, ratio 0.68) and redraw all six figures at once.

**Why it matters.** One recursive rule — two children per branch, each shrunk and rotated — generates every picture in this gallery. Writing that rule down is what turns a pretty picture into mathematics, and the honest part is the interesting part: a picture alone never determines its rule.

---

## Shared notation and recursion

Work in mathematical coordinates with positive y pointing upward. Define

$$
u(\theta)=(\cos\theta,\sin\theta).
$$

A branch state is $(P,\theta,L,n)$: starting point, direction, length parameter, and remaining depth. Start with $P=(0,0)$, $\theta=\pi/2$, $L=L_0>0$, and $n=D$.

The shared parameters are:

| Parameter | Meaning | Earlier webpage default |
|---|---|---|
| $D$ | Number of branch generations drawn | 8 |
| $\alpha$ | Branching angle | $28^\circ$ |
| $r$ | Child-to-parent length-parameter ratio | 0.68 |
| $\beta$ | Curved-branch turning parameter | 0.22 radians |

<div class="controls-row">
  <label>Depth <input id="depth" type="range" min="3" max="10" value="8"> <output id="dv">8</output></label>
  <label>Angle <input id="angle" type="range" min="12" max="55" value="28"> <output id="av">28°</output></label>
  <label>Length ratio <input id="ratio" type="range" min="50" max="78" value="68"> <output id="rv">0.68</output></label>
  <button id="reset" type="button">Reset</button>
</div>

Convert angles to radians before using trigonometric functions. Stop when $n=0$; an optional minimum-length threshold is useful in a renderer.

For two children per branch and a root counted as generation zero, depth $D$ draws

$$
N(D)=1+2+\cdots+2^{D-1}=2^D-1
$$

branches. The drawing cost is $O(2^D)$; a depth-first implementation uses $O(D)$ stack space, excluding any stored geometry.

For equal scaling, a generation-$k$ branch has length parameter

$$
L_k=L_0r^k.
$$

Along one descendant path, the sum of these length parameters is bounded by $L_0/(1-r)$ when $0<r<1$. This is different from the sum over all branches: for straight equal-scale binary trees, the latter is $L_0\sum_{k=0}^{D-1}(2r)^k$, which converges as depth increases only when $2r<1$.

---

## 1. Curved recursive tree

Closest visual match to the supplied image. This is a descriptive label, not a uniquely named curve.

<canvas class="tree-canvas" data-type="curved" aria-label="Curved recursive tree, drawn live by the recursion in this section"></canvas>

### Branch geometry: quadratic Bézier curve

The earlier webpage used a quadratic Bézier curve with start point $P$, control point $C$, and endpoint $Q$:

$$
C=P+0.52L\,u(\theta),\qquad
Q=P+L\,u(\theta+\beta/2),
$$

$$
B(t)=(1-t)^2P+2(1-t)tC+t^2Q,
\qquad 0\le t\le1.
$$

Thus $L$ is the endpoint chord length, not the exact arc length. Its actual arc length is $\int_0^1\lVert B'(t)\rVert\,dt$.

### Recursive rule

After drawing $B$, spawn two children at $Q$:

$$
T(P,\theta,L,n)\longrightarrow
\begin{cases}
T(Q,\theta+\beta-\alpha,rL,n-1),\\
T(Q,\theta+\beta+\alpha,rL,n-1).
\end{cases}
$$

The same signed bend on every branch introduces a directional bias, so this curved construction is not exactly mirror symmetric.

The webpage's $\theta+\beta$ is a nominal end direction. It is not guaranteed to equal the actual Bézier end-tangent direction, which is

$$
\theta_{\rm end}=\operatorname{atan2}(Q_y-C_y,Q_x-C_x),
\qquad B'(1)=2(Q-C).
$$

For tangent-relative branching, replace $\theta+\beta$ with $\theta_{\rm end}$. Children at angles $\theta_{\rm end}\pm\alpha$ still form intentional junction angles; this does not make both child paths smoothly tangent to the parent.

## 2. Binary fractal tree

The basic two-child recursive model. “Binary” specifies the number of children, not a particular angle or ratio.

<canvas class="tree-canvas" data-type="binary" aria-label="Binary fractal tree, drawn live by the recursion in this section"></canvas>

### Branch geometry and recursion

Draw the segment from $P$ to

$$
Q=P+L\,u(\theta).
$$

Then recurse:

$$
T(P,\theta,L,n)\longrightarrow
\begin{cases}
T(Q,\theta-\alpha,rL,n-1),\\
T(Q,\theta+\alpha,rL,n-1).
\end{cases}
$$

For a path encoded by signs $\sigma_j\in\lbrace-1,+1\rbrace$,

$$
\theta_k=\theta_0+\alpha\sum_{j=1}^k\sigma_j,
\qquad
P_{k+1}=P_k+L_0r^k u(\theta_k).
$$

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

**Mid-post challenge:** The root's four grandchildren correspond to the sign sequences $(+,+),(+,-),(-,+),(-,-)$. Using $\theta_k=\theta_0+\alpha\sum_{j=1}^k\sigma_j$ with $\theta_0=\pi/2$, $\alpha=28^\circ$, $L_0=1$, $r=0.68$, compute the two endpoints $P_2$ reached via $(+,-)$ and $(-,+)$, and show they have the same direction $\theta_2=\theta_0$ but different positions.

---

## 3. Symmetric fractal canopy

A standard symmetric instance of a binary fractal tree: both children use the same ratio and opposite branching angles. Its geometry is therefore the same as entry 2 with equal left/right parameters. The earlier webpage intentionally displayed the same construction under these related labels; they are not two independent curve families.

<canvas class="tree-canvas" data-type="canopy" aria-label="Symmetric fractal canopy, drawn live by the recursion in this section"></canvas>

### Self-similarity as a set equation

Normalize the root to the segment

$$
S=\{(0,t):0\le t\le1\},\qquad A=(0,1).
$$

Let

$$
R_\phi=
\begin{pmatrix}
\cos\phi&-\sin\phi\\
\sin\phi&\cos\phi
\end{pmatrix},
\qquad
f_\pm(X)=A+rR_{\pm\alpha}X.
$$

Finite-depth sets satisfy

$$
K_0=\varnothing,\qquad
K_D=S\cup f_-(K_{D-1})\cup f_+(K_{D-1}).
$$

The ideal limiting tree obeys

$$
K=S\cup f_-(K)\cup f_+(K).
$$

The explicit trunk $S$ matters: omitting it describes a different self-similar set, generally the endpoint attractor rather than the full branch skeleton.

### Dimension caveat

The similarity-dimension equation for the associated two-map endpoint attractor is

$$
2r^s=1,\qquad s=\frac{\log 2}{\log(1/r)}.
$$

This equals its Hausdorff dimension only under suitable separation conditions, such as the open set condition. It is not an unconditional dimension formula for an overlapping canopy or the full tree. For the closure of the branch skeleton in a nondegenerate separated case, the segments contribute dimension 1 and the endpoint set contributes $s$, giving $\max(1,s)$. Overlaps require separate analysis, and any planar set has Hausdorff dimension at most 2. A finite drawing is only a finite union of segments or smooth arcs.

**Mid-post challenge:** For $r=0.68$, compute $s=\log 2/\log(1/r)$ and confirm $s>1$. Then explain, using $L_0\sum_{k=0}^{D-1}(2r)^k$ from the notation section, why the divergence of total length and $s>1$ tell the same story.

---

## 4. Asymmetric fractal tree

Unequal child angles or scaling factors break the mirror symmetry while retaining a repeated rule.

<canvas class="tree-canvas" data-type="asymmetric" aria-label="Asymmetric fractal tree, drawn live by the recursion in this section"></canvas>

### General recurrence

Draw $P\to Q=P+Lu(\theta)$, then use

$$
T(P,\theta,L,n)\longrightarrow
\begin{cases}
T(Q,\theta-\alpha_L,r_LL,n-1),\\
T(Q,\theta+\alpha_R,r_RL,n-1).
\end{cases}
$$

The earlier webpage chose

$$
\alpha_L=\alpha,\quad\alpha_R=1.4\alpha,
\qquad r_L=r,\quad r_R=0.82r.
$$

A descendant reached by choices $b_1,\ldots,b_k\in\lbrace L,R\rbrace$ has

$$
L_k=L_0\prod_{j=1}^k r_{b_j}.
$$

For the associated endpoint attractor with suitable separation, the similarity dimension solves

$$
r_L^s+r_R^s=1.
$$

Usually this equation is solved numerically. As with the symmetric canopy, it is not automatically the dimension of the full branch skeleton.

**Mid-post challenge:** The webpage's asymmetric tree has $r_L=0.68$ and $r_R=0.82\cdot0.68=0.5576$. Show that $r_L^s+r_R^s=1$ has a solution with $1<s<2$ by evaluating the left-hand side at $s=1$ and $s=2$ — no numerical root-finding required.

---

## 5. Fern-like recursive tree

A descriptive construction with a continuing stem and a smaller side subtree. It is not the Barnsley fern algorithm, which is a different affine-IFS construction.

<canvas class="tree-canvas" data-type="fern" aria-label="Fern-like recursive tree, drawn live by the recursion in this section"></canvas>

### Branch and attachment geometry

Draw the same Bézier branch $B(t)$ as entry 1. Let $\theta_e=\theta+\beta$ denote the webpage's nominal end direction, and choose

$$
\lambda=0.62,\qquad c=0.57,\qquad \delta=0.06.
$$

The earlier webpage attached the side branch at

$$
A=P+\lambda(Q-P).
$$

Then it spawned

$$
\begin{aligned}
\text{continuation: }&T(Q,\theta_e-\delta,rL,n-1),\\
\text{side subtree: }&T(A,\theta_e+1.9\alpha,crL,n-1).
\end{aligned}
$$

Both children repeat this same rule. The side child is shorter, but it is itself a branching subtree, not just one leaf stroke.

### More geometrically faithful attachment

The original attachment point lies on the chord $PQ$, not generally on the curved branch. To attach directly to the drawn stem, use

$$
A=B(\lambda),\qquad
\theta_A=\operatorname{atan2}(B'_y(\lambda),B'_x(\lambda)),
$$

$$
B'(t)=2(1-t)(C-P)+2t(Q-C).
$$

Then define the side direction relative to $\theta_A$, for example $\theta_A+1.9\alpha$. Note that $t=0.62$ is a Bézier parameter, not necessarily 62% of the arc length. Alternating the sign of the side angle can produce foliage on both sides, but that would be a modification of the earlier preview.

## 6. Radial branching tree

Several recursive trees share one center. This is a descriptive arrangement rather than a separate standard named fractal curve.

<canvas class="tree-canvas" data-type="radial" aria-label="Radial branching tree, drawn live by the recursion in this section"></canvas>

### Multiple initial directions

Choose $m$ initial directions

$$
\theta_j=\theta_0+\frac{2\pi j}{m},
\qquad j=0,\ldots,m-1.
$$

Then run the symmetric binary-tree recursion independently for each:

$$
\mathcal R_D=\bigcup_{j=0}^{m-1}
T(P_0,\theta_j,\kappa L_0,D).
$$

The webpage used $m=5$ and $\kappa=0.47$, reducing the initial length to fit the drawing area. Its nominal branch count, before coincident geometry is merged, is

$$
N_{\rm radial}(D)=m(2^D-1).
$$

Equal spacing gives rotational symmetry of order $m$ when each initial tree uses the same rule. Taking finitely many rotated copies of a set does not change its Hausdorff dimension, although overlaps can change its visible appearance.

---

## The six constructions at a glance

| Construction | Branch shape | Children | Distinctive parameters |
|---|---|---|---|
| Curved recursive tree | Quadratic Bézier | 2, at nominal angles $\theta+\beta\pm\alpha$ | bend $\beta=0.22$ |
| Binary fractal tree | Straight segment | 2, at $\theta\pm\alpha$ | symmetric, equal scales |
| Symmetric fractal canopy | Straight segment | 2, at $\pm\alpha$ from the trunk | IFS maps $f_\pm$, trunk $S$ |
| Asymmetric fractal tree | Straight segment | 2, unequal | $\alpha_R=1.4\alpha$, $r_R=0.82r$ |
| Fern-like recursive tree | Bézier stem + side child | continuation + side subtree | $\lambda=0.62$, $c=0.57$, $\delta=0.06$ |
| Radial branching tree | Rotated copies of a tree | $m$ independent roots | $m=5$, $\kappa=0.47$ |

## Implementation notes

- Browser canvas coordinates have y increasing downward. Use initial angle $-\pi/2$, or transform mathematical coordinates by $(x,y)\mapsto(x_0+x,y_0-y)$.
- A consistent positive bend appears clockwise in ordinary canvas coordinates, but counterclockwise in the mathematical convention used here.
- Keep geometry separate from styling. The earlier webpage decreased stroke width approximately as $3.7(0.73)^k$, with a minimum width, and changed color by generation. These choices do not change the mathematical branch set.
- Depth, ratio, and angle control different properties: amount of detail, scale decay, and spread. Increasing depth alone does not change the recursive rule.
- Not every self-similar branching construction has a noninteger dimension. Dimension depends on which set is measured and on overlap and separation.

---

## Deeper significance

The deepest lesson of this gallery is negative in the best way: a picture does not determine its mathematics. The curved tree, the canopy, and the fern-like construction are finite truncations of different limit objects, and infinitely many rules approximate any one picture. The inverse problem of fractal geometry — reconstruct the rule from the drawing — is ill-posed, which is why the gallery labels these constructions descriptively rather than by name.

What survives the limit is the set equation $K=S\cup f_-(K)\cup f_+(K)$ of Section 3. Finite depth draws a finite union of segments; the limit object is the fixed point of an iterated function system. The two natural limit objects — the branch skeleton and the endpoint attractor — can have different dimensions, which is why $2r^s=1$ must be read with the open set condition in mind. The Barnsley fern, often confused with these constructions, is a different affine IFS with probabilities: it samples its attractor, it does not recursively draw every branch.

Recursive branching is a language — L-systems, IFSs, turtle graphics — in which the same sentence can mean many things. Reading the sentence precisely is what the six sections above are for.

---

## Final challenge

**Final challenge:** Using only Section 1, find the bend $\beta$ for which the nominal end direction $\theta+\beta$ actually equals the Bézier end-tangent direction. Hint: $B'(1)=2(Q-C)$, two vectors are parallel exactly when their cross product vanishes, and $u(a)\times u(b)=\sin(b-a)$. Then confirm that the gallery's $\beta=0.22$ fails the condition you found.

---

## Sources and further exploration

- [Processing: recursive tree example](https://processing.org/examples/tree.html)
- [Yale: dimensions of fractal trees](https://gauss.math.yale.edu/fractals/FracTrees/welcome.html)
- [Fractal canopy: standard binary construction](https://en.wikipedia.org/wiki/Fractal_canopy)
- [Smooth Fractal Trees: Analytic Generators and Discrete Equivalence — preprint](https://arxiv.org/pdf/2601.17490v1.pdf)

The specific Bézier constants, asymmetric ratios, fern attachment rule, and radial arrangement above document the earlier generated webpage. They are illustrative design choices, not formulas attributed to these sources.

<style>
.controls-row{display:flex;gap:14px 22px;flex-wrap:wrap;align-items:center;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:12px 16px;margin:14px 0 8px}
.controls-row label{font-size:14px;white-space:nowrap}
.controls-row output{min-width:34px;display:inline-block;text-align:right;font-size:13px}
.tree-canvas{width:100%;max-width:620px;height:300px;background:#f6faf7;border:1px solid #d8e2ee;border-radius:10px;display:block;margin:10px auto}
</style>

<script>
function draw(c){
  const w=c.clientWidth,h=300,dpr=window.devicePixelRatio||1;
  c.width=w*dpr;c.height=h*dpr;
  const ctx=c.getContext('2d');ctx.scale(dpr,dpr);
  const type=c.dataset.type,depth=+document.getElementById('depth').value,ang=+document.getElementById('angle').value*Math.PI/180,r=+document.getElementById('ratio').value/100;
  function branch(x,y,a,len,n,level){
    if(n===0)return;
    const bend=(type==='curved'||type==='fern')?0.22:0;
    const endA=a+bend;
    const ex=x+len*Math.cos(a+bend/2),ey=y+len*Math.sin(a+bend/2);
    ctx.strokeStyle=`hsl(${205-level*13},60%,${38+level*2}%)`;
    ctx.lineWidth=Math.max(0.55,3.7*Math.pow(0.73,level));
    ctx.beginPath();ctx.moveTo(x,y);
    if(bend)ctx.quadraticCurveTo(x+len*.52*Math.cos(a),y+len*.52*Math.sin(a),ex,ey);else ctx.lineTo(ex,ey);
    ctx.stroke();
    if(type==='fern'){branch(ex,ey,endA-0.06,len*r,n-1,level+1);branch(x+(ex-x)*.62,y+(ey-y)*.62,endA+ang*1.9,len*r*.57,n-1,level+1)}
    else{branch(ex,ey,endA-ang,len*r,n-1,level+1);branch(ex,ey,endA+ang*(type==='asymmetric'?1.4:1),len*r*(type==='asymmetric'?.82:1),n-1,level+1)}
  }
  const len=Math.min(w*.23,68)*(1-r)/.32;
  if(type==='radial'){for(let i=0;i<5;i++)branch(w/2,h/2,-Math.PI/2+i*2*Math.PI/5,len*.47,depth,0)}
  else branch(w/2,h-12,-Math.PI/2,len,depth,0)
}
function render(){
  document.getElementById('dv').value=document.getElementById('depth').value;
  document.getElementById('av').value=document.getElementById('angle').value+'°';
  document.getElementById('rv').value=(+document.getElementById('ratio').value/100).toFixed(2);
  document.querySelectorAll('.tree-canvas').forEach(draw)
}
['depth','angle','ratio'].forEach(id=>document.getElementById(id).addEventListener('input',render));
document.getElementById('reset').onclick=()=>{document.getElementById('depth').value=8;document.getElementById('angle').value=28;document.getElementById('ratio').value=68;render()};
window.addEventListener('resize',render);
render();
</script>

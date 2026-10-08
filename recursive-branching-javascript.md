# Recursive branching curves — JavaScript line drawings

The ASCII diagrams have been removed. Each entry now contains a JavaScript implementation that produces actual Canvas line drawings, with its mathematical rule explained below it.

Ordinary Markdown displays fenced JavaScript as source code; it does not execute it. The companion HTML demo runs the same code and displays all six drawings with depth, angle, and ratio sliders. A live drawing inside a Markdown page requires a renderer that explicitly supports interactive components or scripts.

## Shared parameters

Use mathematical y-up coordinates and u(theta)=(cos(theta),sin(theta)). Start at P=(0,0), theta=pi/2 and length L=1. Depth D=8, angle alpha=28 degrees, length ratio r=0.68, and curved-branch bend beta=0.22 radians are the defaults. Each visited branch decreases remaining depth by one. A two-child tree draws 2^D-1 branches. Drawing costs O(2^D), so keep depth modest (1–10). Use 0<r<1 for shrinking branches.

## Shared Canvas drawing engine

Load these helpers before the entry generators. The renderer fits the entire tree to the canvas, flips mathematical y-up coordinates into Canvas y-down coordinates, and draws straight segments with `lineTo` or quadratic Bézier branches with `quadraticCurveTo`. Control-point bounds conservatively enclose the curved branches.

```javascript
const TAU = 2 * Math.PI;
const rad = degrees => degrees * Math.PI / 180;
const move = (p, angle, length) => ({
  x: p.x + length * Math.cos(angle),
  y: p.y + length * Math.sin(angle)
});

function segment(p, q, level) {
  return { p, q, level };
}
function curvedBranch(p, angle, length, bend, level) {
  return {
    p,
    c: move(p, angle, 0.52 * length),
    q: move(p, angle + bend / 2, length),
    level
  };
}
function bezierPoint(b, t) {
  const s = 1 - t;
  return {
    x: s*s*b.p.x + 2*s*t*b.c.x + t*t*b.q.x,
    y: s*s*b.p.y + 2*s*t*b.c.y + t*t*b.q.y
  };
}
function tangentAngle(b, t) {
  const dx = (1-t)*(b.c.x-b.p.x) + t*(b.q.x-b.c.x);
  const dy = (1-t)*(b.c.y-b.p.y) + t*(b.q.y-b.c.y);
  return Math.atan2(dy, dx);
}
const defaults = { depth: 8, angle: rad(28), ratio: 0.68,
                   length: 1, bend: 0.22 };

// Fit the entire tree to the canvas, using mathematical y-up coordinates.
function paint(canvas, branches) {
  const width = canvas.clientWidth || 600;
  const height = canvas.clientHeight || 400;
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.round(width * dpr);
  canvas.height = Math.round(height * dpr);
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.fillStyle = '#f5faf7';
  ctx.fillRect(0, 0, width, height);
  if (!branches.length) return;
  let xmin=Infinity, ymin=Infinity, xmax=-Infinity, ymax=-Infinity;
  for (const b of branches) {
    for (const p of [b.p, b.q, ...(b.c ? [b.c] : [])]) {
      xmin=Math.min(xmin,p.x); xmax=Math.max(xmax,p.x);
      ymin=Math.min(ymin,p.y); ymax=Math.max(ymax,p.y);
    }
  }
  const padding=24;
  const scale=Math.min((width-2*padding)/Math.max(xmax-xmin,1e-9),
                       (height-2*padding)/Math.max(ymax-ymin,1e-9));
  const project=p => ({x:width/2+(p.x-(xmin+xmax)/2)*scale,
                        y:height/2-(p.y-(ymin+ymax)/2)*scale});
  ctx.lineCap='round'; ctx.lineJoin='round';
  for (const b of branches) {
    const p=project(b.p), q=project(b.q);
    ctx.strokeStyle=`hsl(${205-13*b.level}, 60%, 40%)`;
    ctx.lineWidth=Math.max(0.6, 4*Math.pow(0.73,b.level));
    ctx.beginPath(); ctx.moveTo(p.x,p.y);
    if (b.c) {
      const c=project(b.c);
      ctx.quadraticCurveTo(c.x,c.y,q.x,q.y);
    } else ctx.lineTo(q.x,q.y);
    ctx.stroke();
  }
}
```

## Curved recursive tree

```javascript
function curvedTree(options = {}) {
  const o={...defaults,...options}, result=[];
  function visit(p, angle, length, n, level) {
    if (n <= 0) return;
    const b=curvedBranch(p,angle,length,o.bend,level);
    result.push(b);
    const end=angle+o.bend;
    visit(b.q,end-o.angle,length*o.ratio,n-1,level+1);
    visit(b.q,end+o.angle,length*o.ratio,n-1,level+1);
  }
  visit({x:0,y:0},Math.PI/2,o.length,o.depth,0);
  return result;
}
```

### Recursive rule

Use a quadratic Bézier branch:
\[
C=P+0.52L u(\theta),\quad Q=P+Lu(\theta+\beta/2),
\quad B(t)=(1-t)^2P+2t(1-t)C+t^2Q.
\]
The children start at Q with length rL and directions \(\theta+\beta\pm\alpha\). L measures chord length, not arc length. The nominal end direction \(\theta+\beta\) need not equal the actual end tangent. This retains the original webpage's rule. Set `end=tangentAngle(b,1)` if child directions should be relative to the actual tangent. Branch junctions still have intentional angles.

## Binary fractal tree

```javascript
function binaryTree(options = {}) {
  const o={...defaults,...options}, result=[];
  function visit(p, angle, length, n, level) {
    if (n <= 0) return;
    const q=move(p,angle,length);
    result.push(segment(p,q,level));
    visit(q,angle-o.angle,length*o.ratio,n-1,level+1);
    visit(q,angle+o.angle,length*o.ratio,n-1,level+1);
  }
  visit({x:0,y:0},Math.PI/2,o.length,o.depth,0);
  return result;
}
```

### Recursive rule

Draw from P to \(Q=P+Lu(\theta)\). Recurse at Q with directions \(\theta-\alpha\) and \(\theta+\alpha\), scaling both lengths by r. At generation k the length is \(L_0r^k\). Stop at depth zero.

## Symmetric fractal canopy

```javascript
function symmetricCanopy(options = {}) {
  // This is the symmetric special case of the binary tree, not a new rule.
  return binaryTree(options);
}
```

### Recursive rule

This is the same equal-angle, equal-ratio binary construction as entry 2, not a separate geometry. With root segment S from (0,0) to (0,1), define \(f_\pm(X)=(0,1)+rR_{\pm\alpha}X\). Then \(K_0=\varnothing\) and \(K_D=S\cup f_-(K_{D-1})\cup f_+(K_{D-1})\). R denotes the usual planar rotation matrix.

## Asymmetric fractal tree

```javascript
function asymmetricTree(options = {}) {
  const o={...defaults,...options}, result=[];
  const leftAngle=o.leftAngle ?? o.angle;
  const rightAngle=o.rightAngle ?? 1.4*o.angle;
  const leftRatio=o.leftRatio ?? o.ratio;
  const rightRatio=o.rightRatio ?? 0.82*o.ratio;
  function visit(p, angle, length, n, level) {
    if (n <= 0) return;
    const q=move(p,angle,length);
    result.push(segment(p,q,level));
    visit(q,angle-leftAngle,length*leftRatio,n-1,level+1);
    visit(q,angle+rightAngle,length*rightRatio,n-1,level+1);
  }
  visit({x:0,y:0},Math.PI/2,o.length,o.depth,0);
  return result;
}
```

### Recursive rule

Children start at \(Q=P+Lu(\theta)\) with independent parameters:
\[
(\theta-\alpha_L,r_LL),\qquad(\theta+\alpha_R,r_RL).
\]
Defaults reproduce the earlier webpage: \(\alpha_L=\alpha\), \(\alpha_R=1.4\alpha\), \(r_L=r\), \(r_R=0.82r\). A path's length is \(L_0\prod_j r_{b_j}\), where each choice is left or right.

## Fern-like recursive tree

```javascript
function fernTree(options = {}) {
  const o={...defaults,attachToCurve:true,...options}, result=[];
  function visit(p, angle, length, n, level) {
    if (n <= 0) return;
    const b=curvedBranch(p,angle,length,o.bend,level);
    result.push(b);
    const end=angle+o.bend;
    const a=o.attachToCurve ? bezierPoint(b,0.62) : {
      x:p.x+0.62*(b.q.x-p.x), y:p.y+0.62*(b.q.y-p.y)
    };
    const sideDirection=o.attachToCurve ? tangentAngle(b,0.62) : end;
    visit(b.q,end-0.06,length*o.ratio,n-1,level+1);
    visit(a,sideDirection+1.9*o.angle,
          length*o.ratio*0.57,n-1,level+1);
  }
  visit({x:0,y:0},Math.PI/2,o.length,o.depth,0);
  return result;
}
```

### Recursive rule

Draw the same Bézier branch as entry 1. The continuation starts at Q, has direction \(\theta+\beta-0.06\), and length rL. The side subtree has length 0.57rL and attaches at \(A=B(0.62)\). Its direction is the local tangent angle plus \(1.9\alpha\), using
\[
B'(t)=2(1-t)(C-P)+2t(Q-C).
\]
This improves the earlier chord-based attachment. Set `attachToCurve:false` to reproduce that earlier rule: \(A=P+0.62(Q-P)\) with side direction \(\theta+\beta+1.9\alpha\). The Bézier parameter 0.62 is not necessarily 62% of arc length. This is a fern-like recursive tree, not the Barnsley fern.

## Radial branching tree

```javascript
function radialTree(options = {}) {
  const o={...defaults,arms:5,...options}, result=[];
  function visit(p, angle, length, n, level) {
    if (n <= 0) return;
    const q=move(p,angle,length);
    result.push(segment(p,q,level));
    visit(q,angle-o.angle,length*o.ratio,n-1,level+1);
    visit(q,angle+o.angle,length*o.ratio,n-1,level+1);
  }
  for (let j=0;j<o.arms;j++) {
    visit({x:0,y:0},Math.PI/2+TAU*j/o.arms,
          0.47*o.length,o.depth,0);
  }
  return result;
}
```

### Recursive rule

Start m trees from the same origin at directions
\[
\theta_j=\pi/2+2\pi j/m,\qquad 0\le j<m.
\]
Each uses entry 2's recursion and initial length 0.47L. Defaults use m=5. The nominal branch count is \(m(2^D-1)\), before any coincident geometry is merged. This is a radial arrangement, not a separate standard named curve.

## Run a drawing

Create a canvas in your HTML host:

```html
<canvas id="tree" style="width:100%;height:420px;display:block"></canvas>
```

Load the shared helpers and desired generator, then run:

```javascript
const canvas = document.getElementById('tree');
function redraw() {
  paint(canvas, curvedTree({depth: 8, angle: rad(28), ratio: 0.68}));
}
window.addEventListener('resize', redraw);
redraw();
```

Replace `curvedTree` with `binaryTree`, `symmetricCanopy`, `asymmetricTree`, `fernTree`, or `radialTree`. The canopy alias also requires `binaryTree` to be loaded. To implement sliders, read their values and call `paint` again. All six implementations and shared helpers are included in the companion standalone HTML demo; no external dependencies or network requests are required.

## Mathematical cautions

These are illustrative constructions, not an identification of the original video's generating algorithm. Binary fractal trees and fractal canopies are established terms; curved, fern-like, and radial labels here describe variations. The symmetric binary and canopy previews intentionally share the same geometry.

An infinite recursive construction and a finite browser drawing are different objects. A finite drawing is a finite union of segments or smooth arcs. Self-similarity alone does not establish noninteger dimension. Endpoint attractors and full branch skeletons must be distinguished; overlapping constructions need separate dimension analysis.

## Further reading

- [GitHub Docs: fenced code blocks display and highlight source](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)
- [Processing recursive tree example](https://processing.org/examples/tree.html)
- [Yale: dimensions of fractal trees](https://gauss.math.yale.edu/fractals/FracTrees/welcome.html)

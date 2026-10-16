---
title: "From Fabric to Knot Theory: A Weave Is a Link on a Torus"
date: 2026-10-17
categories:
  - Knot Theory
  - Mathematics
tags:
  - knot-theory
  - link-theory
  - alexander-polynomial
  - torus
  - weaving
  - textiles
share: true
read_time: true
excerpt: "Identify the opposite edges of a repeat cell and a piece of cloth becomes a link in a thickened torus. Part 2 of the series turns the binary matrix of Part 1 into knot diagrams — with a live 3D viewer that renders warp and weft yarns as curves on an actual torus, over–under crossings included."
---

**Challenge to the reader:** Take a $3\times 3$ plain-weave cell and identify opposite edges. Count the components of the resulting link, its crossings, and identify each component's winding type on the torus — before reading the answer in Section 3.

*Part 2 of five in the series **From Weaving Mathematics to Torus Knots**: [Part 1 — The Mathematics Hidden in a Weave]({% post_url 2026-10-16-weaving-mathematics %}) · Part 2 — From Fabric to Knot Theory: A Weave Is a Link on a Torus (this page) · [Part 3 — Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement]({% post_url 2026-10-18-torus-knots-versus-weaving-knots %}) · [Part 4 — Constructing the Torus Knot: Two Circular Motions, One Equation]({% post_url 2026-10-19-torus-knot-construction %}) · [Part 5 — The Torus Knot Laboratory: An Interactive Playground]({% post_url 2026-10-20-torus-knot-laboratory %}).*

Knot theory applies to weaving by treating the yarns as **curves in 3D space** and the over–under crossings as the data that determine their entanglement. A periodic weave becomes a **link diagram on a torus**, which lets you distinguish fabrics that may look similar locally but are topologically different globally. [arxiv](https://arxiv.org/abs/0806.2824)

## From weave to knot diagram

A knot diagram is a 2D projection with gaps showing which strand passes over at each crossing. A woven fabric supplies exactly that information: at every warp–weft intersection, one thread is over and the other is under. [arxiv](https://arxiv.org/html/2604.09005v1)

For a small piece of plain weave, draw:

```text
vertical thread: over, under, over, under
horizontal thread: under, over, under, over
```

The drawing is a crossing diagram. If you connect the loose ends of the threads, you obtain a knot or link; with multiple yarns, it is generally a **link**, meaning several closed curves. [link.springer](https://link.springer.com/article/10.1007/s44217-025-01060-x)

The crucial point is that the actual fabric is not just the flat diagram: the yarns occupy a thin layer of 3D space. Two diagrams that differ by a Reidemeister move can represent the same underlying entanglement. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

**Why it matters.** The binary matrix $A_{ij}$ of Part 1 was a *choice of crossings*. Knot theory is the machinery that asks which of those choices are genuinely different once the threads may slide and bend — but not pass through one another.

## Periodicity gives a torus

A real woven fabric repeats in two directions. Take one repeating cell and identify:

- its left edge with its right edge;
- its top edge with its bottom edge.

The plane becomes a torus $T^2$, and the yarns become curves in the **thickened torus** $T^2\times[0,1]$. This is the standard topological model for doubly periodic textile structures. [arxiv](https://arxiv.org/abs/0806.2824)

Schematically:

$$
\text{infinite periodic weave}
\quad\longrightarrow\quad
\text{finite repeat cell}
\quad\longrightarrow\quad
\text{link diagram on }T^2.
$$

This removes the artificial distinction between "inside" and "outside" a small sample: a yarn leaving the right edge re-enters from the left, just as it does in the physical fabric.

## Plain weave as a link

Consider a $2\times 2$ plain-weave cell:

$$
\begin{array}{c|c}
\text{warp over} & \text{warp under}\\
\hline
\text{warp under} & \text{warp over}
\end{array}
$$

Draw two vertical yarns and two horizontal yarns, mark the four crossings, then glue opposite sides. The result is a link in the thickened torus, not merely four separate crossings on a square.

For the common biaxial weaves, the topology can be represented using four curves: two yarn components plus two curves representing the two fundamental directions around the torus. A Kagome weave requires five. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

**Figure 1 — the identification, rendered honestly.** The left panel shows an $n\times n$ plain-weave cell with the identification arrows on its boundary. The right panel carries out the identification: the same yarns are drawn as tubes on a real torus. The key equation is the radial offset

$$
\rho(u)=r+\varepsilon\,\sigma(i,j),
\qquad
\sigma(i,j)=
\begin{cases}
+1,&(i+j)\bmod 2=0 \text{ (warp over)},\\
-1,&(i+j)\bmod 2=1 \text{ (weft over)},
\end{cases}
$$

smoothly interpolated between crossings — that is the third direction of the thickened torus $T^2\times[0,1]$, i.e. *exactly the over–under data of $A_{ij}$*. The rendering has no hand-drawn gaps: over and under are real depth, computed by the painter's algorithm. Drag to rotate; press **Flip crossing (1,1)** to change one entry of the matrix, and watch both panels.

<div class="torus-controls">
  <label>n <input id="tn" type="range" min="2" max="6" value="3"> <output id="tnv">3</output></label>
  <label>yarn offset ε <input id="teps" type="range" min="0.05" max="0.5" step="0.01" value="0.28"> <output id="tepsv">0.28</output></label>
  <label><input id="tguide" type="checkbox" checked> guide torus</label>
  <label><input id="tspin" type="checkbox" checked> auto-rotate</label>
  <button id="tflip" type="button">Flip crossing (1,1)</button>
  <button id="treset" type="button">Reset</button>
</div>
<div class="torus-panels">
  <div><canvas id="flat-cell" width="300" height="300" aria-label="Flat repeat cell with opposite-edge identification arrows"></canvas><div class="panel-cap">repeat cell → torus</div></div>
  <div><canvas id="torus-view" width="560" height="420" aria-label="Warp and weft yarns as tubes on a torus, with true over-under depth"></canvas><div class="panel-cap">the same weave in T² × [0,1]</div></div>
</div>
<div id="torus-stats" role="status"></div>

Here is the arithmetic behind Figure 1. Warp yarn $j$ lies at longitudinal angle $v_j=2\pi j/n$ and winds once meridionally: it is a $(1,0)$-curve. Weft yarn $i$ lies at meridional angle $u_i=2\pi i/n$ and winds once longitudinally: it is a $(0,1)$-curve. A meridian and a longitude on a torus meet exactly once, so warp $j$ and weft $i$ cross at exactly the single point $(u_i,v_j)$ — there are $n^2$ crossings in total, and each warp–weft pair has linking number $\pm 1$. The full link therefore has $2n$ components and $n^2$ crossings, and its entire entanglement is encoded by which sign $\sigma(i,j)$ sits at each of the $n^2$ points.

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

One important invariant is the multivariable Alexander polynomial. For a textile, researchers construct an associated "kernel" link in ordinary 3-space and compute a normalized multivariable Alexander polynomial. This polynomial acts like a structural fingerprint of the weave. [arxiv](https://arxiv.org/abs/0806.2824)

It can reveal:

- whether the structure contains closed curves;
- how the pattern behaves under changes of scale;
- whether two fabrics with different-sized repeat cells share underlying topology;
- information about the arrangement of yarn components in the periodic structure. [arxiv](https://arxiv.org/abs/0806.2824)

The "multi-variable" part matters because a fabric has several meaningful directions or components: warp, weft, and the two periodic directions of the torus. A single-variable knot invariant would lose some of that structure.

## Weaving knots

There is also a technical class called **weaving knots**: alternating knots or links whose projection matches the standard projection of a torus knot. For $W(p,q)$, the crossing number is

$$
c(W(p,q))=q(p-1).
$$

These are not necessarily literal cloth patterns, but they formalize the idea of an alternating, highly regular over–under arrangement resembling a woven grid. [arxiv](https://arxiv.org/html/1506.04139v2)

For example, a finite patch of square weave can be closed into a weaving knot. Its hyperbolic geometry and diagrammatic complexity can then be studied through quantities such as volume density and determinant density. [arxiv](https://arxiv.org/html/1506.04139v2)

## A concrete experiment

Take a $3\times3$ grid and assign crossings by

$$
A_{ij}=(i+j)\bmod 2.
$$

This gives a checkerboard/plain-weave pattern. Now change one entry from $0$ to $1$. Visually, you have changed one local over–under choice; topologically, you may have changed the associated torus link.

Ask:

1. Can the new diagram be simplified back to the original using Reidemeister moves?
2. Do the two patterns have the same Alexander polynomial?
3. Is the changed crossing essential, or can it be removed by choosing a different repeat cell?

That is knot theory applied directly to weaving: not "what does the cloth look like?" but "what entanglement does the cloth encode?" [arxiv](https://arxiv.org/abs/0806.2824)

---

**Final challenge:** In Figure 1, set $n=3$ and flip crossing $(1,1)$. Each warp–weft pair still links once, so the *pairwise* linking numbers cannot see the flip. Which invariant of the whole link — not of its pairs — could? (Hint: it is the one in Section 5.)

*Next: [Part 3 — Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement]({% post_url 2026-10-18-torus-knots-versus-weaving-knots %}), which zooms in on the two knots that share the torus-knot projection but differ in their crossing signs.*

*References for the curious reader: Doubly periodic textile patterns ([arXiv:0806.2824](https://arxiv.org/abs/0806.2824)); Textiles: from twisted yarn to topology and mechanics ([arXiv:2604.09005](https://arxiv.org/abs/2604.09005)); Volume bounds for weaving knots ([arXiv:1506.04139](https://arxiv.org/abs/1506.04139)).*

<style>
.torus-controls{display:flex;gap:14px 22px;flex-wrap:wrap;align-items:center;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:12px 16px;margin:14px 0 8px}
.torus-controls label{font-size:14px;white-space:nowrap}
.torus-controls output{min-width:34px;display:inline-block;text-align:right;font-size:13px}
.torus-controls button{font-size:13px;background:#dbe6f4;border:1px solid #b9cbe0;border-radius:7px;padding:6px 10px;cursor:pointer}
.torus-controls button.on{background:#f4d3de;border-color:#d79bb1}
.torus-panels{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin:10px 0}
.torus-panels>div{flex:0 1 auto}
#flat-cell{width:280px;height:280px;background:#f6faf7;border:1px solid #d8e2ee;border-radius:10px;display:block}
#torus-view{width:min(560px,100%);height:420px;background:#0f1626;border:1px solid #2b3857;border-radius:10px;display:block;touch-action:none;cursor:grab}
.panel-cap{font-size:13px;color:#667;text-align:center;margin-top:6px}
#torus-stats{font-size:14px;line-height:1.7;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:10px 16px;margin:10px 0;color:#334}
</style>

<script>
(function () {
  var cflat = document.getElementById('flat-cell');
  var c3d = document.getElementById('torus-view');
  var state = { n: 3, eps: 0.28, flip: false, yaw: 0.9, pitch: 0.85, spin: true, guide: true };
  var mesh = [], torus = [], buildVersion = -1;
  var dragging = false, lastX = 0, lastY = 0;
  var R = 2.2, r0 = 1.0;

  function g(id) { return document.getElementById(id); }
  function sigma(i, j) {
    var a = ((i + j) % 2 + 2) % 2 === 0 ? 1 : -1;
    if (state.flip && i === 1 && j === 1) a = -a;
    return a;
  }
  function smooth(x) { return x * x * (3 - 2 * x); }
  function add(a, b) { return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]; }
  function sub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function mul(a, s) { return [a[0] * s, a[1] * s, a[2] * s]; }
  function dot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function cross(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
  function norm(a) { var l = Math.sqrt(dot(a, a)) || 1; return [a[0] / l, a[1] / l, a[2] / l]; }

  function curve(ui, vi, offAt) {
    // ui, vi: constants for the fixed angle (null means this angle varies); offAt(t): signed offset
    var N = 110, out = [];
    for (var i = 0; i <= N; i++) {
      var t = i / N;
      var u = ui === null ? 2 * Math.PI * t : ui;
      var v = vi === null ? 2 * Math.PI * t : vi;
      var rho = r0 + offAt(t);
      var cu = Math.cos(u), su = Math.sin(u), cv = Math.cos(v), sv = Math.sin(v);
      out.push({ p: [(R + rho * cu) * cv, (R + rho * cu) * sv, rho * su], n: [cu * cv, cu * sv, su] });
    }
    return out;
  }
  function buildWeave() {
    var n = state.n, eps = state.eps, out = [];
    var M = 6, a = Math.min(eps * 0.42, (Math.PI * r0 / n) * 0.42);
    function pushTube(pts, col) {
      var rings = [];
      for (var i = 0; i < pts.length; i++) {
        var prev = pts[Math.max(0, i - 1)], next = pts[Math.min(pts.length - 1, i + 1)];
        var tan = norm(sub(next.p, prev.p));
        var b = norm(cross(tan, pts[i].n));
        var ring = [];
        for (var k = 0; k < M; k++) {
          var th = 2 * Math.PI * k / M;
          var nn = add(mul(pts[i].n, Math.cos(th)), mul(b, Math.sin(th)));
          ring.push({ p: add(pts[i].p, mul(nn, a)), n: nn, c: col });
        }
        rings.push(ring);
      }
      for (var i = 0; i < rings.length - 1; i++) {
        for (var k = 0; k < M; k++) {
          var p0 = rings[i][k], p1 = rings[i + 1][k], p2 = rings[i + 1][(k + 1) % M], p3 = rings[i][(k + 1) % M];
          out.push([p0, p1, p2], [p0, p2, p3]);
        }
      }
    }
    for (var j = 0; j < n; j++) {
      (function (j) {
        var vj = 2 * Math.PI * j / n;
        pushTube(curve(null, vj, function (t) {
          var idx = Math.floor(t * n), f = t * n - idx;
          var s0 = sigma(idx % n, j), s1 = sigma((idx + 1) % n, j);
          return (s0 + (s1 - s0) * smooth(f)) * eps;
        }), 0);
      })(j);
    }
    for (var i = 0; i < n; i++) {
      (function (i) {
        var ui = 2 * Math.PI * i / n;
        pushTube(curve(ui, null, function (t) {
          var idx = Math.floor(t * n), f = t * n - idx;
          var s0 = sigma(i, idx % n), s1 = sigma(i, (idx + 1) % n);
          return -(s0 + (s1 - s0) * smooth(f)) * eps;
        }), 1);
      })(i);
    }
    return out;
  }
  function buildTorus() {
    var out = [], N = 40, M = 18;
    function vert(i, j) {
      var u = 2 * Math.PI * j / M, v = 2 * Math.PI * i / N;
      var cu = Math.cos(u), su = Math.sin(u), cv = Math.cos(v), sv = Math.sin(v);
      return { p: [(R + r0 * cu) * cv, (R + r0 * cu) * sv, r0 * su], n: [cu * cv, cu * sv, su], c: 2 };
    }
    for (var i = 0; i < N; i++) for (var j = 0; j < M; j++) {
      var a = vert(i, j), b = vert(i + 1, j), c = vert(i + 1, j + 1), d = vert(i, j + 1);
      out.push([a, b, c], [a, c, d]);
    }
    return out;
  }
  function rotate(p, y, x) {
    var a = Math.cos(y) * p[0] - Math.sin(y) * p[1];
    var b = Math.sin(y) * p[0] + Math.cos(y) * p[1];
    return [a, Math.cos(x) * b - Math.sin(x) * p[2], Math.sin(x) * b + Math.cos(x) * p[2]];
  }
  function draw3d() {
    var w = c3d.clientWidth, h = c3d.clientHeight, dpr = Math.min(window.devicePixelRatio || 1, 1.6);
    if (c3d.width !== Math.round(w * dpr) || c3d.height !== Math.round(h * dpr)) {
      c3d.width = Math.round(w * dpr); c3d.height = Math.round(h * dpr);
    }
    var ctx = c3d.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.fillStyle = '#0f1626'; ctx.fillRect(0, 0, w, h);
    var scale = Math.min(w, h) * 0.55, faces = [];
    function push(tris) {
      for (var f = 0; f < tris.length; f++) {
        var tri = tris[f];
        var vs = [rotate(tri[0].p, state.yaw, state.pitch), rotate(tri[1].p, state.yaw, state.pitch), rotate(tri[2].p, state.yaw, state.pitch)];
        var depth = (vs[0][2] + vs[1][2] + vs[2][2]) / 3;
        var pts = vs.map(function (v) { return [w / 2 + v[0] * scale / (9 - v[2]), h / 2 - v[1] * scale / (9 - v[2])]; });
        var nrm = norm(rotate(add(add(tri[0].n, tri[1].n), tri[2].n), state.yaw, state.pitch));
        var light = 0.27 + 0.73 * Math.max(0, dot(nrm, norm([-0.4, 0.65, 1])));
        var col = tri[0].c;
        var color = col === 2 ? 'rgba(115,181,255,0.06)'
          : col === 0 ? 'hsl(215 78% ' + Math.round(20 + light * 52) + '%)'
          : 'hsl(32 85% ' + Math.round(22 + light * 52) + '%)';
        faces.push({ pts: pts, depth: depth, color: color });
      }
    }
    push(mesh);
    if (state.guide) push(torus);
    faces.sort(function (a, b) { return a.depth - b.depth; });
    for (var f = 0; f < faces.length; f++) {
      var face = faces[f];
      ctx.beginPath();
      ctx.moveTo(face.pts[0][0], face.pts[0][1]);
      ctx.lineTo(face.pts[1][0], face.pts[1][1]);
      ctx.lineTo(face.pts[2][0], face.pts[2][1]);
      ctx.closePath();
      ctx.fillStyle = face.color; ctx.fill();
    }
  }
  function drawFlat() {
    var n = state.n;
    var w = cflat.clientWidth, h = cflat.clientHeight, dpr = window.devicePixelRatio || 1;
    cflat.width = Math.round(w * dpr); cflat.height = Math.round(h * dpr);
    var ctx = cflat.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var mx = 26, my = 26, cw = (w - 2 * mx) / n, ch = (h - 2 * my) / n;
    ctx.fillStyle = '#f6faf7'; ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = 'rgba(51,68,85,0.15)'; ctx.lineWidth = 1;
    var i, j;
    for (i = 0; i <= n; i++) { ctx.beginPath(); ctx.moveTo(mx, my + i * ch); ctx.lineTo(w - mx, my + i * ch); ctx.stroke(); }
    for (j = 0; j <= n; j++) { ctx.beginPath(); ctx.moveTo(mx + j * cw, my); ctx.lineTo(mx + j * cw, my + n * ch); ctx.stroke(); }
    ctx.lineCap = 'round';
    for (i = 0; i < n; i++) {
      ctx.strokeStyle = '#d17f3f'; ctx.lineWidth = ch * 0.40;
      ctx.beginPath(); ctx.moveTo(mx, my + (i + 0.5) * ch); ctx.lineTo(w - mx, my + (i + 0.5) * ch); ctx.stroke();
    }
    for (j = 0; j < n; j++) {
      ctx.strokeStyle = '#3f6fd1'; ctx.lineWidth = cw * 0.40;
      ctx.beginPath(); ctx.moveTo(mx + (j + 0.5) * cw, my); ctx.lineTo(mx + (j + 0.5) * cw, my + n * ch); ctx.stroke();
    }
    for (i = 0; i < n; i++) for (j = 0; j < n; j++) {
      var x = mx + (j + 0.5) * cw, y = my + (i + 0.5) * ch;
      if (sigma(i, j) === 1) {
        ctx.fillStyle = '#f6faf7';
        ctx.fillRect(x - cw * 0.26, y - ch * 0.24, cw * 0.52, ch * 0.48);
        ctx.strokeStyle = '#d17f3f'; ctx.lineWidth = ch * 0.40;
        ctx.beginPath(); ctx.moveTo(x - cw * 0.26, y); ctx.lineTo(x + cw * 0.26, y); ctx.stroke();
      } else {
        ctx.fillStyle = '#f6faf7';
        ctx.fillRect(x - cw * 0.24, y - ch * 0.26, cw * 0.48, ch * 0.52);
        ctx.strokeStyle = '#3f6fd1'; ctx.lineWidth = cw * 0.40;
        ctx.beginPath(); ctx.moveTo(x, y - ch * 0.26); ctx.lineTo(x, y + ch * 0.26); ctx.stroke();
      }
      if (state.flip && i === 1 && j === 1) {
        ctx.strokeStyle = '#b03a5b'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.arc(x, y, cw * 0.38, 0, 2 * Math.PI); ctx.stroke();
      }
    }
    // identification arrows
    ctx.fillStyle = '#3f6fd1';
    for (j = 0; j < n; j++) arrow(ctx, mx + (j + 0.5) * cw, my - 14, 0, -1, 6);
    ctx.fillStyle = '#d17f3f';
    for (j = 0; j < n; j++) arrow(ctx, mx + (j + 0.5) * cw, h - my + 14, 0, 1, 6);
    for (i = 0; i < n; i++) arrow(ctx, mx - 14, my + (i + 0.5) * ch, -1, 0, 6);
    for (i = 0; i < n; i++) arrow(ctx, w - mx + 14, my + (i + 0.5) * ch, 1, 0, 6);
  }
  function arrow(ctx, x, y, dx, dy, s) {
    var px = dx === 0 ? -dy : dx, py = dx === 0 ? dx : dy;
    ctx.beginPath();
    ctx.moveTo(x + (dx - px) * s, y + (dy - py) * s);
    ctx.lineTo(x + dx * s, y + dy * s);
    ctx.lineTo(x + (dx + px) * s, y + (dy + py) * s);
    ctx.closePath(); ctx.fill();
  }
  function rebuild() {
    mesh = buildWeave(); torus = buildTorus();
  }
  function stats() {
    var n = state.n;
    var html = 'Components: 2n = ' + (2 * n) + ' &nbsp;·&nbsp; crossings: n² = ' + (n * n) +
      ' &nbsp;·&nbsp; warp yarn = (1,0)-curve (meridian), weft yarn = (0,1)-curve (longitude)' +
      ' &nbsp;·&nbsp; each warp–weft pair crosses once, linking number ±1';
    if (state.flip) html += '<br>σ(1,1) flipped: one entry of the matrix changed. The pairwise linking numbers are unchanged — the difference lives in the whole link, not its pairs.';
    g('torus-stats').innerHTML = html;
  }
  function refresh() { drawFlat(); draw3d(); stats(); }
  g('tn').addEventListener('input', function () { state.n = +g('tn').value; g('tnv').textContent = state.n; rebuild(); refresh(); });
  g('teps').addEventListener('input', function () { state.eps = +g('teps').value; g('tepsv').textContent = state.eps.toFixed(2); rebuild(); refresh(); });
  g('tguide').addEventListener('change', function () { state.guide = g('tguide').checked; refresh(); });
  g('tspin').addEventListener('change', function () { state.spin = g('tspin').checked; });
  g('tflip').addEventListener('click', function () {
    state.flip = !state.flip;
    g('tflip').classList.toggle('on', state.flip);
    rebuild(); refresh();
  });
  g('treset').addEventListener('click', function () {
    state.n = 3; state.eps = 0.28; state.flip = false; state.yaw = 0.9; state.pitch = 0.85;
    g('tn').value = 3; g('tnv').textContent = 3;
    g('teps').value = 0.28; g('tepsv').textContent = '0.28';
    g('tflip').classList.remove('on');
    rebuild(); refresh();
  });
  c3d.addEventListener('pointerdown', function (e) {
    dragging = true; lastX = e.clientX; lastY = e.clientY;
    c3d.setPointerCapture(e.pointerId);
  });
  c3d.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    state.yaw += (e.clientX - lastX) * 0.008;
    state.pitch += (e.clientY - lastY) * 0.008;
    lastX = e.clientX; lastY = e.clientY;
  });
  ['pointerup', 'pointercancel'].forEach(function (ev) {
    c3d.addEventListener(ev, function () { dragging = false; });
  });
  window.addEventListener('resize', refresh);
  rebuild();
  refresh();
  var last = 0;
  function frame(t) {
    if (t - last > 32) {
      if (state.spin && !dragging) state.yaw += Math.min(t - last, 60) * 0.0004;
      draw3d();
      last = t;
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
</script>

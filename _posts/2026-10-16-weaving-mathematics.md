---
title: "The Mathematics Hidden in a Weave: Binary Matrices, Modular Arithmetic, and Symmetry"
date: 2026-10-16
categories:
  - Knot Theory
  - Mathematics
tags:
  - weaving
  - binary-matrices
  - modular-arithmetic
  - combinatorics
  - group-theory
  - symmetry
  - textiles
share: true
read_time: true
excerpt: "A weave is simultaneously a picture, a binary matrix, and a system of entangled curves. Part 1 of the series unpacks the over–under matrix: 2^(mn) possible patterns, modular repeat lengths n/gcd(n,s), symmetry groups, and the topology waiting one identification away — with a live weave simulator drawn by the very rules in the equations."
---

**Challenge to the reader:** Plain weave has the repeating block $\begin{pmatrix}1&0\\0&1\end{pmatrix}$. For the diagonal rule $(j-si)\bmod n\in S$ with $n=4$, $s=1$, $S=\{0,1\}$, write out the first four rows, then verify that the pattern repeats after exactly $r=n/\gcd(n,s)=4$ rows — and predict what happens to $r$ when $s=2$.

*Part 1 of five in the series **From Weaving Mathematics to Torus Knots**: Part 1 — The Mathematics Hidden in a Weave (this page) · [Part 2 — From Fabric to Knot Theory: A Weave Is a Link on a Torus]({% post_url 2026-10-17-weaving-and-knots %}) · [Part 3 — Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement]({% post_url 2026-10-18-torus-knots-versus-weaving-knots %}) · [Part 4 — Constructing the Torus Knot: Two Circular Motions, One Equation]({% post_url 2026-10-19-torus-knot-construction %}) · [Part 5 — The Torus Knot Laboratory: An Interactive Playground]({% post_url 2026-10-20-torus-knot-laboratory %}).*

A weaving pattern can lead to **mathematics** ranging from elementary counting to group theory, number theory, topology, algorithms, and the mechanics of materials. The key is that a weave is simultaneously a picture, a system of discrete over–under choices, and a three-dimensional arrangement of interacting threads. Research on weaving explicitly identifies arithmetic, geometric transformations, and interconnected patterns as overlapping mathematical activities. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

For an ordinary warp–weft weave, here is a useful way to develop these connections.

## 1. Start with a binary matrix

Let vertical threads be the warp and horizontal threads the weft. At each crossing, record

$$
A_{ij}=
\begin{cases}
1,&\text{warp thread }j\text{ passes over weft thread }i,\\
0,&\text{warp thread }j\text{ passes under weft thread }i.
\end{cases}
$$

A plain weave has the repeating block

$$
A=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
$$

and its infinite extension satisfies

$$
A_{ij}=(i+j+1)\bmod 2.
$$

This separates the structural pattern from thread colours: two cloths can have the same over–under matrix but look different because their yarn colours differ. Binary matrices and equivalence relations between them are established mathematical tools for studying weave design. [arxiv](https://arxiv.org/html/1201.1465v1)

**Figure 1 — the rule draws itself.** The simulator below contains no picture: it computes $A_{ij}$ from the equation beside it and draws warp over weft exactly when $A_{ij}=1$. Choose the *diagonal* rule and move the shift $s$: the dashed repeat block shrinks to exactly $r=n/\gcd(n,s)$ rows, computed live by the same number-theoretic formula derived in Section 3.

<div class="weave-controls">
  <label>Rule
    <select id="wmode">
      <option value="plain">plain: (i+j+1) mod 2</option>
      <option value="diagonal" selected>diagonal: (j−s·i) mod n ∈ S</option>
    </select>
  </label>
  <label>n <input id="wn" type="range" min="3" max="12" value="4"> <output id="wnv">4</output></label>
  <label>shift s <input id="ws" type="range" min="0" max="11" value="1"> <output id="wsv">1</output></label>
  <label>S = {<span id="sboxes" class="s-toggles"></span>}</label>
  <button id="wreset" type="button">Reset</button>
</div>
<canvas id="weave-canvas" width="640" height="400" aria-label="Live weave pattern, computed from the binary matrix rule"></canvas>
<div id="weave-stats" role="status"></div>

From this representation, several branches unfold naturally.

## 2. Combinatorics: how many patterns are possible?

An $m\times n$ crossing grid has $mn$ binary choices, so there are

$$
2^{mn}
$$

possible crossing assignments before imposing constraints.

But "different binary matrices" is not necessarily the same as "different useful weaves." You might require:

- Every thread to pass both over and under other threads.
- No excessively long uninterrupted over- or under-runs.
- A specified proportion of warp-visible crossings.
- A pattern compatible with the loom.
- Patterns related by translation or rotation to count as equivalent.

This turns weaving into a constrained enumeration problem: count binary arrays, then identify equivalent arrays or discard those that violate design requirements. Mathematical work on weave structures explicitly studies this kind of matrix equivalence. [arxiv](https://arxiv.org/html/1201.1465v1)

A subtle question is whether a local condition, such as limiting uninterrupted runs, guarantees a satisfactory whole fabric. Local appearance and global structure are different problems.

## 3. Number theory: modular arithmetic, divisibility, and repeat lengths

You can generate diagonal patterns by defining

$$
A_{ij}=1
\quad\Longleftrightarrow\quad
(j-si)\bmod n\in S,
$$

where:

- $n$ is the horizontal repeat length;
- $s$ is the shift between successive rows;
- $S$ specifies which positions are warp-over crossings.

For example, choose $n=4$, $s=1$, and $S=\{0,1\}$:

```text
1100
0110
0011
1001
```

Each row shifts the preceding row by one position.

The shifts return to their starting position after the smallest positive $r$ satisfying

$$
rs\equiv0\pmod n,
$$

namely

$$
r=\frac{n}{\gcd(n,s)}.
$$

Thus coprimality determines whether the shift visits every position. A motif with additional internal symmetry can repeat even sooner.

This provides concrete investigations into parity, congruences, greatest common divisors, and least common multiples—connections also used in weaving-based mathematics activities. [mathingaround](https://mathingaround.com/curriculum/weaving-and-coding-mathematical-connections/)

## 4. Geometry and group theory: which transformations preserve the weave?

A pattern might be unchanged under translations, rotations, reflections, or glide reflections. Weaving research identifies these geometric transformations as part of the design process. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

The interesting distinction is:

- A transformation may preserve the visible colour design.
- It may preserve the over–under structure.
- It may preserve the structure only after exchanging warp and weft, or reversing which thread lies on top.

These are not necessarily the same symmetry.

For a periodic matrix, translation symmetry means

$$
A_{i+p,j+q}=A_{ij}.
$$

The set of preserving transformations forms a group. Classification then asks: which patterns have the same symmetry group, and which apparently similar patterns have different structural symmetries?

## 5. Topology: how are the threads actually entangled?

Geometry studies positions and shapes. Topology asks what remains unchanged when threads deform without passing through one another.

A crossing diagram contains over–under information, so it leads naturally to knot and link theory. For doubly periodic textiles, identifying opposite edges of a repeat cell turns the planar repeat into a torus; the threads become curves in a thickened torus. Researchers use link constructions and Alexander-polynomial invariants to analyse and compare these structures. [arxiv](https://arxiv.org/abs/0806.2824)

This raises deeper questions:

- Can one arrangement be continuously deformed into another?
- Are there genuinely entangled components?
- What is the smallest number of crossings needed in a repeat cell?
- Which features survive a change in the chosen repeat cell?

Crossing-number classification is an active mathematical approach to periodic weaves. [arxiv](https://arxiv.org/html/2202.01755v1)

Ordinary weaving is more naturally connected to periodic link theory than automatically to braid groups; braid theory becomes especially relevant when strands exchange positions along a common direction. **This is the exact turn we take in Part 2, and again in Part 3.**

## 6. Graph theory: represent the relationships, not just the picture

One graph model takes crossing points as vertices and thread segments between crossings as edges. To reconstruct a weave, that graph must also record which edges continue along the same thread and which thread passes over at each crossing.

Another model takes entire threads as vertices and their crossings as edges.

These are modelling choices rather than a single universal "weaving graph." They expose different questions: connectivity, crossing incidence, thread families, and repeat-cell structure. Formal weave descriptions likewise distinguish thread organisation from crossing sequences. [arxiv](https://arxiv.org/html/2202.01755v1)

## 7. Algorithms and logic: turn a pattern into instructions

A binary crossing rule is already a small program:

```text
for each weft row i:
    for each warp thread j:
        choose over or under using A(i, j)
```

The harder problem is translating the desired matrix into operations supported by a particular loom. This is analogous to compiling a high-level specification into machine instructions. Weaving education explicitly connects pattern generation with coding and computational thinking. [mathingaround](https://mathingaround.com/curriculum/weaving-and-coding-mathematical-connections/)

Possible computational problems include:

- Generate every pattern satisfying a maximum-run constraint.
- Test whether two repeat blocks differ only by a cyclic shift.
- Find the smallest repeat cell.
- Search for a pattern meeting several structural and visual requirements.

The underlying matrix-equivalence problem supplies a rigorous starting point for such algorithms. [arxiv](https://arxiv.org/html/1201.1465v1)

## 8. Mechanics and differential geometry: why does the cloth behave that way?

The binary matrix describes crossing order, but not yarn thickness, curvature, friction, tension, or material properties.

To predict physical behaviour, the threads become three-dimensional curves and the fabric becomes a deformable surface. Mathematical models then involve elasticity, energy minimisation, numerical simulation, and homogenisation: deriving large-scale fabric behaviour from a small repeating yarn structure. These approaches are used for both cloth and woven composites. [link.springer](https://link.springer.com/article/10.1007/s11029-013-9316-8)

One schematic formulation is

$$
W_{\mathrm{eff}}(F)
=
\frac{1}{\lvert\Omega\rvert}
\min_{\text{admissible yarn configurations}}
E_{\mathrm{yarn}}(F),
$$

where $F$ describes an imposed macroscopic deformation and $\Omega$ is a repeat cell.

This connects the pattern to questions about stretching, shear, bending, and direction-dependent stiffness—not merely appearance. Yarn-level models have been used to fit shell models with distinct warp, weft, and coupled responses. [arxiv](https://arxiv.org/html/2401.15169v1)

## A compact mathematical investigation

The shifted-row construction from Section 3 makes a good starting point because one simple rule exposes several different questions:

| Investigation | Mathematical connection |
|---|---|
| Change $n$ and $s$; determine when rows repeat | Number theory |
| Count allowable choices of $S$ | Combinatorics |
| Identify translations and reflections | Group theory |
| Track uninterrupted over–under runs | Discrete algorithms |
| Glue opposite edges of the repeat cell | Topology |
| Add yarn geometry and material properties | Mechanics |

The central distinction is between studying the visible motif, the crossing structure, and the physical fabric. Each layer has its own mathematics, and the most interesting problems often arise where those layers interact. [link.springer](https://link.springer.com/article/10.1007/s11423-023-10316-y)

---

**Final challenge:** For the diagonal rule with $n=6$, $s=2$, $S=\{0,1,3\}$, write down one full repeat block (it has $r=3$ rows), then identify a symmetry of the *visible* pattern that is *not* a symmetry of the over–under matrix — or argue that none exists.

*Next: [Part 2 — From Fabric to Knot Theory: A Weave Is a Link on a Torus]({% post_url 2026-10-17-weaving-and-knots %}), where the binary matrix becomes a link diagram and the repeat cell becomes a torus.*

*References for the curious reader: the papers cited inline — doubly periodic textile patterns ([arXiv:0806.2824](https://arxiv.org/abs/0806.2824)), modeling of weaving structure design ([arXiv:1201.1465](https://arxiv.org/abs/1201.1465)), and the classification of doubly periodic weaves by crossing number ([arXiv:2202.01755](https://arxiv.org/abs/2202.01755)).*

<style>
.weave-controls{display:flex;gap:14px 22px;flex-wrap:wrap;align-items:center;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:12px 16px;margin:14px 0 8px}
.weave-controls label{font-size:14px;white-space:nowrap}
.weave-controls output{min-width:30px;display:inline-block;text-align:right;font-size:13px}
.weave-controls select{font-size:13px}
.s-toggles{display:inline-flex;flex-wrap:wrap;gap:2px 6px;align-items:center}
.s-toggles label{font-size:13px;display:inline-flex;gap:3px;align-items:center}
#weave-canvas{width:100%;max-width:660px;height:400px;background:#f6faf7;border:1px solid #d8e2ee;border-radius:10px;display:block;margin:10px auto}
#weave-stats{font-size:14px;line-height:1.7;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:10px 16px;margin:10px 0;color:#334}
</style>

<script>
(function () {
  var canvas = document.getElementById('weave-canvas');
  var ctx = canvas.getContext('2d');
  var nPrev = -1;
  var forceDefault = false;
  function g(id) { return document.getElementById(id); }
  function gcd(a, b) { return b ? gcd(b, a % b) : a; }
  function mod(a, m) { return ((a % m) + m) % m; }

  function getS(n) {
    var out = [];
    var boxes = g('sboxes').querySelectorAll('input');
    for (var j = 0; j < boxes.length && j < n; j++) if (boxes[j].checked) out.push(j);
    if (!out.length) out.push(0);
    return out;
  }

  function rebuildS(n) {
    var keep = forceDefault ? [0, 1] : getS(n);
    g('sboxes').innerHTML = '';
    for (var j = 0; j < n; j++) {
      var lab = document.createElement('label');
      var cb = document.createElement('input');
      cb.type = 'checkbox';
      cb.checked = keep.indexOf(j) >= 0;
      cb.addEventListener('change', render);
      lab.appendChild(cb);
      lab.appendChild(document.createTextNode(String(j)));
      g('sboxes').appendChild(lab);
    }
    forceDefault = false;
  }

  function A(mode, i, j, n, s, S) {
    if (mode === 'plain') return (i + j + 1) % 2;
    return S.indexOf(mod(j - s * i, n)) >= 0 ? 1 : 0;
  }

  function render() {
    var mode = g('wmode').value;
    var n = Math.round(+g('wn').value);
    var s = Math.round(+g('ws').value);
    s = Math.min(s, n - 1);
    g('wnv').textContent = n; g('wsv').textContent = s;
    if (n !== nPrev) { rebuildS(n); nPrev = n; }
    var boxes = g('sboxes').querySelectorAll('input');
    for (var b = 0; b < boxes.length; b++) boxes[b].disabled = (mode !== 'diagonal');
    g('sboxes').style.opacity = mode === 'diagonal' ? 1 : 0.35;
    var S = getS(n);
    var r = mode === 'diagonal' ? n / gcd(n, s) : 2;
    var m = mode === 'diagonal' ? r : 8;

    var W = canvas.clientWidth, H = canvas.clientHeight, dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var mx = 34, my = 28, cw = (W - 2 * mx) / n, ch = (H - 2 * my) / m;
    ctx.fillStyle = '#f6faf7'; ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = 'rgba(51,68,85,0.15)'; ctx.lineWidth = 1;
    var i, j;
    for (i = 0; i <= m; i++) { ctx.beginPath(); ctx.moveTo(mx, my + i * ch); ctx.lineTo(W - mx, my + i * ch); ctx.stroke(); }
    for (j = 0; j <= n; j++) { ctx.beginPath(); ctx.moveTo(mx + j * cw, my); ctx.lineTo(mx + j * cw, my + m * ch); ctx.stroke(); }
    // weft (horizontal) threads
    ctx.strokeStyle = '#d17f3f'; ctx.lineCap = 'round';
    for (i = 0; i < m; i++) {
      ctx.lineWidth = ch * 0.40;
      ctx.beginPath(); ctx.moveTo(mx - 10, my + (i + 0.5) * ch); ctx.lineTo(W - mx + 10, my + (i + 0.5) * ch); ctx.stroke();
    }
    // warp (vertical) threads
    ctx.strokeStyle = '#3f6fd1';
    for (j = 0; j < n; j++) {
      ctx.lineWidth = cw * 0.40;
      ctx.beginPath(); ctx.moveTo(mx + (j + 0.5) * cw, my - 10); ctx.lineTo(mx + (j + 0.5) * cw, H - my + 10); ctx.stroke();
    }
    // over-under gaps
    for (i = 0; i < m; i++) for (j = 0; j < n; j++) {
      var x = mx + (j + 0.5) * cw, y = my + (i + 0.5) * ch;
      if (A(mode, i, j, n, s, S) === 1) {
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
    }
    // repeat-cell outline
    var rh = mode === 'diagonal' ? r : 2, rw = mode === 'diagonal' ? n : 2;
    ctx.strokeStyle = '#b03a5b'; ctx.lineWidth = 2; ctx.setLineDash([6, 4]);
    ctx.strokeRect(mx, my, rw * cw, rh * ch);
    ctx.setLineDash([]);

    var html;
    if (mode === 'plain') {
      html = 'Rule: A(i, j) = (i + j + 1) mod 2 &nbsp;·&nbsp; repeat block: [[1,0],[0,1]] &nbsp;·&nbsp; warp-over share: 1/2';
    } else {
      html = 'Rule: A(i, j) = 1 ⟺ (j − ' + s + '·i) mod ' + n + ' ∈ S, &nbsp; S = {' + S.join(', ') + '}';
      html += '<br>Rows before the pattern repeats: r = n / gcd(n, s) = ' + n + ' / ' + gcd(n, s) + ' = ' + r;
      html += ' &nbsp;·&nbsp; gcd(' + n + ', ' + s + ') = ' + gcd(n, s) + (gcd(n, s) === 1 ? ' (coprime — the shift visits every position)' : '');
      html += ' &nbsp;·&nbsp; warp-over crossings per row: |S| = ' + S.length;
    }
    html += '<br>Unconstrained ' + n + '×' + n + ' crossing grid: 2<sup>mn</sup> = 2<sup>' + (n * n) + '</sup> possible over–under matrices';
    g('weave-stats').innerHTML = html;
  }

  ['wn', 'ws'].forEach(function (id) { g(id).addEventListener('input', render); });
  g('wmode').addEventListener('change', render);
  g('wreset').addEventListener('click', function () {
    g('wn').value = 4; g('ws').value = 1; g('wmode').value = 'diagonal';
    nPrev = -1; forceDefault = true; render();
  });
  window.addEventListener('resize', render);
  render();
})();
</script>

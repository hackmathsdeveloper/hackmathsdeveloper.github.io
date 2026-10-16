---
title: "Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement"
date: 2026-10-18
categories:
  - Knot Theory
  - Mathematics
tags:
  - torus-knots
  - weaving-knots
  - braids
  - crossing-number
  - alternation
share: true
read_time: true
excerpt: "A torus knot is defined by where its strand lives; a weaving knot by how its crossings alternate. Part 3 of the series draws both families side by side from their braid words — the same shadow, opposite handedness patterns — and explains why identical projections are different knots."
---

**Challenge to the reader:** Compute $c(W(5,4))=q(p-1)=16$ and $c(T(5,4))=\min((p-1)q,(q-1)p)=12$. The standard braid diagram of $T(5,4)$ has $16$ crossings — explain why a diagram can have more crossings than its knot's crossing number.

*Part 3 of five in the series **From Weaving Mathematics to Torus Knots**: [Part 1 — The Mathematics Hidden in a Weave]({% post_url 2026-10-16-weaving-mathematics %}) · [Part 2 — From Fabric to Knot Theory: A Weave Is a Link on a Torus]({% post_url 2026-10-17-weaving-and-knots %}) · Part 3 — Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement (this page) · [Part 4 — Constructing the Torus Knot: Two Circular Motions, One Equation]({% post_url 2026-10-19-torus-knot-construction %}) · [Part 5 — The Torus Knot Laboratory: An Interactive Playground]({% post_url 2026-10-20-torus-knot-laboratory %}).*

A **torus knot** is defined by where its single strand lies: it winds around a torus. A **weaving knot** is defined by its diagram's over–under pattern: it is an alternating knot with the same crossing projection as a torus knot. They often share the same picture, but they are generally different knots. [arxiv](https://arxiv.org/html/1506.04139v2)

**Why it matters.** This is the purest version of the lesson of Part 2: the *shadow* (where the strands lie) does not determine the knot — the signs of the crossings do. The same matrix of positions $A_{ij}$ with different signs is a different entanglement.

## Torus knot $T(p,q)$

A $(p,q)$-torus knot is a closed curve embedded on the surface of an unknotted torus. It winds $p$ times around the torus's meridian and $q$ times around its longitude; when $p$ and $q$ are coprime, it has one component, otherwise $T(p,q)$ is a multi-component torus link. [academic.oup](https://academic.oup.com/book/33813/chapter/288597576)

Its standard braid form is

$$
T(p,q)=\text{closure of }(\sigma_1\sigma_2\cdots\sigma_{p-1})^q.
$$

All crossings in that braid have the same handedness: every $\sigma_i$ is, say, a positive crossing. [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/1704.03982)

For example, $T(3,2)$ is the trefoil knot. [academic.oup](https://academic.oup.com/book/33813/chapter/288597576)

## Weaving knot $W(p,q)$

A weaving knot $W(p,q)$ uses the **same underlying projection** as $T(p,q)$, but changes the crossing signs so that the diagram is alternating: as you travel along each component, crossings alternate over, under, over, under. [arxiv](https://arxiv.org/html/1506.04139v2)

In braid notation:

$$
W(p,q)=\text{closure of }
(\sigma_1\sigma_2^{-1}\sigma_3\sigma_4^{-1}\cdots)^q.
$$

So the strands occupy the same projected positions as in the torus-knot braid, but the over–under choices are different. [ar5iv.labs.arxiv](https://ar5iv.labs.arxiv.org/html/1704.03982)

**Figure 1 — two knots, one shadow.** Both panels draw the closure of a braid on $p$ strands with $q$ waves of $p-1$ crossings; the strand positions are identical. The only difference is the sign rule: positive everywhere on the left, alternating $\sigma_1\sigma_2^{-1}\sigma_3\sigma_4^{-1}\cdots$ on the right. Positive crossings are drawn green ($+$), negative red ($−$); the closure arcs pass behind the page. Watch the over–under sequence along any single strand in each panel.

<div class="braid-controls">
  <label>p <input id="bp" type="range" min="2" max="6" value="3"> <output id="bpv">3</output></label>
  <label>q <input id="bq" type="range" min="1" max="6" value="3"> <output id="bqv">3</output></label>
</div>
<div class="braid-panels">
  <div>
    <div class="braid-label">T(p,q): <span id="word-t">(σ₁σ₂)<sup>3</sup></span> — all crossings positive</div>
    <canvas id="braid-t" width="340" height="430" aria-label="Braid diagram of the torus knot with all positive crossings"></canvas>
  </div>
  <div>
    <div class="braid-label">W(p,q): <span id="word-w">(σ₁σ₂⁻¹)<sup>3</sup></span> — signs alternate</div>
    <canvas id="braid-w" width="340" height="430" aria-label="Braid diagram of the weaving knot with alternating crossing signs"></canvas>
  </div>
</div>
<div id="braid-stats" role="status"></div>

## The essential distinction

| Feature | Torus knot $T(p,q)$ | Weaving knot $W(p,q)$ |
|---|---|---|
| Defining property | Lies on a torus surface | Has an alternating diagram with a torus-knot projection |
| Crossing signs | All crossings in the standard braid have the same sign | Alternating positive and negative crossings |
| Diagram | Standard braid projection | Same braid projection, different over–under assignments |
| Usually alternating? | No | Yes, by construction |
| Number of components | $\gcd(p,q)$ | $\gcd(p,q)$ |
| Crossing number | $\min((p-1)q,(q-1)p)$ | $q(p-1)$ for the standard $W(p,q)$ family |

A torus knot is generally **not alternating** in its standard projection, whereas a weaving knot is specifically built to be alternating. [arxiv](https://arxiv.org/html/1506.04139v2)

## Why they are different knots

Changing a crossing from over to under changes the knot type in general. Thus $T(p,q)$ and $W(p,q)$ can share the same shadow—same positions of arcs and crossings—but fail to be isotopic because their crossing data differ.

For example, $T(5,4)$ and $W(5,4)$ have the same standard projection, but $W(5,4)$ is the alternating version. Its crossing number is

$$
c(W(5,4))=4(5-1)=16.
$$

This is the standard crossing count for the weaving-knot family, not necessarily the same as the torus-knot crossing number. [arxiv](https://arxiv.org/html/1506.04139v2)

The smallest example is memorable: $T(3,2)$ is the trefoil knot ($3$ crossings), while $W(3,2)$ is the figure-eight knot $4_1$ ($4$ crossings) — the two simplest nontrivial knots, born from the same shadow.

## Connection to actual weaving

The name is apt because $W(p,q)$ resembles a regular over–under lattice: successive strands alternate above and below one another, like the local structure of a woven textile.

However, a "weaving knot" in knot theory is not the same as a periodic fabric. A periodic weave is usually modeled as an infinite collection of threads, or equivalently as a link in a thickened torus. A weaving knot $W(p,q)$ is a finite closed knot or link obtained by closing a finite braid-like patch. [arxiv](https://arxiv.org/html/1506.04139v2)

So:

$$
\text{torus knot: "where the curve sits"};
$$

$$
\text{weaving knot: "how the crossings alternate"}.
$$

They are related by projection, but their topology is normally distinct. [arxiv](https://arxiv.org/html/1506.04139v2)

---

**Final challenge:** In Figure 1 set $p=3$, $q=2$. The left panel is the trefoil, the right is the figure-eight. Give one invariant that separates them — tricolorability, the Alexander polynomial, or the crossing number — and state its value for each.

*Next: [Part 4 — Constructing the Torus Knot: Two Circular Motions, One Equation]({% post_url 2026-10-19-torus-knot-construction %}), which builds $T(p,q)$ explicitly from a parametric equation and computes its crossing number and genus.*

*References for the curious reader: Volume bounds for weaving knots ([arXiv:1506.04139](https://arxiv.org/abs/1506.04139)); The Jones polynomial and Khovanov homology of weaving knots $W(3,n)$ ([arXiv:1704.03982](https://arxiv.org/abs/1704.03982)); the torus knot entry on [Wikipedia](https://en.wikipedia.org/wiki/Torus_knot).*

<style>
.braid-controls{display:flex;gap:14px 22px;flex-wrap:wrap;align-items:center;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:12px 16px;margin:14px 0 8px}
.braid-controls label{font-size:14px;white-space:nowrap}
.braid-controls output{min-width:30px;display:inline-block;text-align:right;font-size:13px}
.braid-panels{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin:10px 0}
.braid-label{font-size:14px;color:#334;text-align:center;margin-bottom:6px;line-height:1.5}
.braid-label span{font-family:Georgia,serif}
.braid-panels canvas{background:#f6faf7;border:1px solid #d8e2ee;border-radius:10px;display:block}
#braid-stats{font-size:14px;line-height:1.7;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:10px 16px;margin:10px 0;color:#334}
</style>

<script>
(function () {
  var ct = document.getElementById('braid-t');
  var cw = document.getElementById('braid-w');
  function g(id) { return document.getElementById(id); }
  function gcd(a, b) { return b ? gcd(b, a % b) : a; }
  function wordHTML(p, q, alternating) {
    var s = '';
    for (var i = 1; i <= p - 1; i++) {
      s += 'σ<sub>' + i + '</sub>';
      if (alternating && i % 2 === 0) s += '<sup>−1</sup>';
    }
    return '(' + s + ')<sup>' + q + '</sup>';
  }
  function drawBraid(canvas, p, q, alternating) {
    var w = canvas.clientWidth, h = canvas.clientHeight, dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    var ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var bg = '#f6faf7';
    ctx.fillStyle = bg; ctx.fillRect(0, 0, w, h);
    var L = q * (p - 1);
    var x0 = 26, x1 = w - 44, top = 26, bot = h - 64;
    var rowH = p > 1 ? (bot - top) / (p - 1) : 1;
    var cols = [], paths = [], crosses = [];
    var j, k;
    for (j = 0; j < p; j++) { cols.push(j); paths.push([{ x: x0, y: top + j * rowH }]); }
    for (k = 0; k < L; k++) {
      var i = k % (p - 1);
      var xk = x0 + (k + 1) * (x1 - x0) / (L + 1);
      var ym = top + (i + 0.5) * rowH;
      var s = alternating ? (i % 2 === 0 ? 1 : -1) : 1;
      var overJ = -1;
      for (j = 0; j < p; j++) {
        if (cols[j] === i) { paths[j].push({ x: xk, y: ym }); cols[j] = i + 1; if (s === 1) overJ = j; }
        else if (cols[j] === i + 1) { paths[j].push({ x: xk, y: ym }); cols[j] = i; if (s === -1) overJ = j; }
        else paths[j].push({ x: xk, y: top + cols[j] * rowH });
      }
      crosses.push({ x: xk, y: ym, s: s, overJ: overJ, idx: paths[overJ].length - 1 });
    }
    for (j = 0; j < p; j++) paths[j].push({ x: x1, y: top + cols[j] * rowH });
    // closure arcs (behind the page), connecting end position to start position
    ctx.strokeStyle = 'rgba(51,68,85,0.45)'; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
    for (j = 0; j < p; j++) {
      ctx.beginPath();
      ctx.moveTo(x1, top + j * rowH);
      ctx.quadraticCurveTo((x0 + x1) / 2, bot + 22 + j * 5, x0, top + j * rowH);
      ctx.stroke();
    }
    ctx.setLineDash([]);
    ctx.fillStyle = 'rgba(51,68,85,0.55)'; ctx.font = '11px system-ui';
    ctx.fillText('closure (behind)', (x0 + x1) / 2 - 40, bot + 40);
    // strands
    ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    for (j = 0; j < p; j++) {
      ctx.strokeStyle = 'hsl(' + Math.round(30 + j * 360 / p) + ' 62% 42%)';
      ctx.lineWidth = Math.min(7, rowH * 0.42);
      ctx.beginPath();
      ctx.moveTo(paths[j][0].x, paths[j][0].y);
      for (k = 1; k < paths[j].length; k++) ctx.lineTo(paths[j][k].x, paths[j][k].y);
      ctx.stroke();
    }
    // crossing gaps and over-strand redraw
    var rr = Math.max(8, Math.min(12, rowH * 0.42));
    for (k = 0; k < crosses.length; k++) {
      var c = crosses[k];
      ctx.fillStyle = bg;
      ctx.beginPath(); ctx.arc(c.x, c.y, rr, 0, 2 * Math.PI); ctx.fill();
      var jj = c.overJ, m = c.idx;
      ctx.strokeStyle = 'hsl(' + Math.round(30 + jj * 360 / p) + ' 62% 42%)';
      ctx.lineWidth = Math.min(7, rowH * 0.42);
      ctx.beginPath();
      ctx.moveTo(paths[jj][m - 1].x, paths[jj][m - 1].y);
      ctx.lineTo(paths[jj][m].x, paths[jj][m].y);
      ctx.lineTo(paths[jj][m + 1].x, paths[jj][m + 1].y);
      ctx.stroke();
      ctx.fillStyle = c.s === 1 ? '#2a7f6a' : '#b03a5b';
      ctx.font = 'bold 12px system-ui';
      ctx.fillText(c.s === 1 ? '+' : '−', c.x + rr + 2, c.y - rr - 2);
    }
  }
  function render() {
    var p = +g('bp').value, q = +g('bq').value;
    g('bpv').textContent = p; g('bqv').textContent = q;
    g('word-t').innerHTML = wordHTML(p, q, false);
    g('word-w').innerHTML = wordHTML(p, q, true);
    drawBraid(ct, p, q, false);
    drawBraid(cw, p, q, true);
    var d = gcd(p, q);
    var drawn = q * (p - 1);
    var cT = Math.min((p - 1) * q, (q - 1) * p);
    var html = 'Both diagrams: ' + drawn + ' crossings in the standard braid &nbsp;·&nbsp; components: gcd(p, q) = ' + d;
    html += '<br>Crossing numbers: c(T(p,q)) = min((p−1)q, (q−1)p) = ' + cT + ' &nbsp;·&nbsp; c(W(p,q)) = q(p−1) = ' + drawn;
    if (drawn > cT) html += ' &nbsp;— the standard torus-braid diagram is not minimal (it contains a nugatory crossing); the reduced alternating weaving diagram is.';
    if (p === 2) html += '<br>p = 2: the sign pattern is trivial, so W(2,q) = T(2,q) — every torus knot T(2,q) is alternating.';
    if (p === 1 || q === 1) html += '<br>p = 1 or q = 1: both close to the unknot.';
    g('braid-stats').innerHTML = html;
  }
  g('bp').addEventListener('input', render);
  g('bq').addEventListener('input', render);
  window.addEventListener('resize', render);
  render();
})();
</script>

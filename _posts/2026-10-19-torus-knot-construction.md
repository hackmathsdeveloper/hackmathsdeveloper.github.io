---
title: "Constructing the Torus Knot: Two Circular Motions, One Equation"
date: 2026-10-19
categories:
  - Knot Theory
  - Mathematics
tags:
  - torus-knots
  - parametrization
  - knot-genus
  - crossing-number
  - coprime
share: true
read_time: true
excerpt: "One parametric equation — a circle around a circle, at two synchronized angular speeds — builds every torus knot. Part 4 of the series derives the parametrization, proves the curve lies on a torus, explains why gcd(p,q) counts components, and computes crossing numbers and genera — with live visuals for each step."
---

**Challenge to the reader:** $\gcd(8,5)=1$ but $\gcd(8,6)=2$. Before reading Section 2, predict how many components the curve of Section 1 closes into for $(p,q)=(8,5)$ and for $(p,q)=(8,6)$.

*Part 4 of five in the series **From Weaving Mathematics to Torus Knots**: [Part 1 — The Mathematics Hidden in a Weave]({% post_url 2026-10-16-weaving-mathematics %}) · [Part 2 — From Fabric to Knot Theory: A Weave Is a Link on a Torus]({% post_url 2026-10-17-weaving-and-knots %}) · [Part 3 — Torus Knots versus Weaving Knots: Same Shadow, Different Entanglement]({% post_url 2026-10-18-torus-knots-versus-weaving-knots %}) · Part 4 — Constructing the Torus Knot: Two Circular Motions, One Equation (this page) · [Part 5 — The Torus Knot Laboratory: An Interactive Playground]({% post_url 2026-10-20-torus-knot-laboratory %}).*

Parts 1–3 built knots out of *matrices and signs*. This part builds the torus knot $T(p,q)$ out of a **single parametric equation** — the same equation that drives the interactive laboratory of Part 5.

The page uses the parameterization

$$
\boxed{
\begin{aligned}
x(t)&=\bigl(R+r\cos(pt)\bigr)\cos(qt),\\
y(t)&=\bigl(R+r\cos(pt)\bigr)\sin(qt),\\
z(t)&=r\sin(pt),
\end{aligned}
\qquad 0\le t\le 2\pi
}
$$

where $R>r>0$. This is the standard torus-knot construction, with the winding-number labels chosen so that $p$ controls the small-circle oscillations and $q$ controls revolutions around the central axis. Some references interchange $p$ and $q$, so the explicit equations matter more than the naming convention. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

**Figure 1 — the equation, plotted.** The dark canvas below evaluates the boxed formula at 640 values of $t$ and draws the curve, one segment at a time, with color moving along $t$. The sliders change the equation itself; drag to rotate. Notice that changing $R$ or $r$ changes the *shape* while the knot type stays fixed — this is the theme of Section 3.

<div class="tk-controls">
  <label>p <input id="kp" type="range" min="1" max="10" value="3"> <output id="kpv">3</output></label>
  <label>q <input id="kq" type="range" min="1" max="10" value="2"> <output id="kqv">2</output></label>
  <label>R <input id="kR" type="range" min="1.5" max="3.2" step="0.01" value="2.2"> <output id="kRv">2.20</output></label>
  <label>r <input id="kr" type="range" min="0.4" max="1.4" step="0.01" value="1"> <output id="krv">1.00</output></label>
  <label><input id="kspin" type="checkbox" checked> auto-rotate</label>
</div>
<canvas id="knot-preview" width="560" height="400" aria-label="The torus knot curve, drawn live from the parametric equation"></canvas>
<div class="panel-cap">x(t) = (R + r cos(pt)) cos(qt), &nbsp; y(t) = (R + r cos(pt)) sin(qt), &nbsp; z(t) = r sin(pt)</div>
<div id="knot-stats" role="status"></div>

## 1. Two synchronized circular motions

The equations combine two angles:

$$
u=pt,\qquad v=qt.
$$

- $u$ moves around the torus's circular cross-section.
- $v$ moves around its central axis.
- $R$ sets the major radius.
- $r$ sets the radius of the supporting torus's cross-section—not the visible strand thickness. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

Substituting the parameterization gives

$$
\left(\sqrt{x^2+y^2}-R\right)^2+z^2=r^2,
$$

so the centerline lies exactly on a torus. This is the same identification machinery as Part 2: $u$ and $v$ are precisely the coordinates of the flat repeat cell, and the equation is the *inverse* of gluing opposite edges.

## 2. Coprimality determines knot versus link

For positive integer winding numbers,

$$
d=\gcd(p,q)
$$

is the number of components of the corresponding torus link. All nine pairs in the preset table below are coprime, so each represents one closed knot. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

**Figure 2 — where the components come from.** Think of $u$ and $v$ as coordinates on a square $[0,2\pi)^2$ whose opposite edges are identified — that square *is* the torus (Part 2 again). A closed curve is a solution of

$$
q u-p v\equiv 0 \pmod{2\pi},
$$

parametrized component-by-component as

$$
u=\frac{p}{d}t+\frac{2\pi k}{q},\qquad v=\frac{q}{d}t,\qquad k=0,\dots,d-1.
$$

These are $d$ parallel lines of slope $q/p$ wrapping the square: a line leaving through the top edge re-enters through the bottom. Count the lines — that is $\gcd(p,q)$, visible as pure geometry.

<div class="tk-controls">
  <label>p (shared) <input id="kp2" type="range" min="1" max="10" value="3"> <output id="kp2v">3</output></label>
  <label>q (shared) <input id="kq2" type="range" min="1" max="10" value="2"> <output id="kq2v">2</output></label>
</div>
<div class="tk-panels">
  <canvas id="param-square" width="420" height="420" aria-label="The parameter square with the lines qu minus pv congruent to 0 modulo 2 pi, one line per component"></canvas>
</div>
<div class="panel-cap">the parameter square [0, 2π)² with its opposite edges identified: qu − pv ≡ 0 (mod 2π)</div>

There is an important implementation subtlety: if $d>1$, merely inserting $p,q$ into the single-curve formula retraces one component $d$ times; it does not draw all components. Both figures on this page explicitly generate the distinct components instead.

## 3. Shape and topology are different

Changing $R$ and $r$, while maintaining $R>r>0$, changes the geometric appearance without changing the knot type. Also, $T(p,q)$ and $T(q,p)$ are equivalent knots, despite generally looking different in their standard torus embeddings. Reflecting the curve produces its mirror image. [arxiv](https://arxiv.org/html/1201.0214v1)

Test this in Figure 1: set $(p,q)=(5,2)$, then $(2,5)$ — two different embeddings of the same knot.

## 4. Complexity can be calculated directly

For coprime positive integers $p,q>1$, the minimal crossing number and knot genus are

$$
c=\min\bigl((p-1)q,\,(q-1)p\bigr),
\qquad
g=\frac{(p-1)(q-1)}{2}.
$$

The crossing number is minimized over all knot diagrams; it is not necessarily the number of overlaps visible from the current camera. Genus means the minimum genus of an orientable surface bounded by the knot—not the genus of the supporting torus. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

Applying those formulas to the preset collection:

| Knot | Minimal crossings $c$ | Genus $g$ |
|---|---:|---:|
| $T(3,2)$ | 3 | 1 |
| $T(4,3)$ | 8 | 3 |
| $T(5,2)$ | 5 | 2 |
| $T(5,3)$ | 10 | 4 |
| $T(5,4)$ | 15 | 6 |
| $T(7,2)$ | 7 | 3 |
| $T(7,4)$ | 21 | 9 |
| $T(8,5)$ | 32 | 14 |
| $T(8,7)$ | 48 | 21 |

These values follow directly from the torus-knot crossing and genus formulas above. [en.wikipedia](https://en.wikipedia.org/wiki/Torus_knot)

---

**Final challenge:** Derive the implicit torus equation by eliminating $t$ from the boxed parametrization — that is, verify $\left(\sqrt{x^2+y^2}-R\right)^2+z^2=r^2$ by direct substitution, and say exactly where the two factors $R$ and $r$ reappear in the final expression.

*Next: [Part 5 — The Torus Knot Laboratory: An Interactive Playground]({% post_url 2026-10-20-torus-knot-laboratory %}), where the same equation is rendered as shaded 3D tubes you can rotate, mirror, and export.*

*References for the curious reader: the [torus knot](https://en.wikipedia.org/wiki/Torus_knot) article on Wikipedia; [Wolfram MathWorld](https://mathworld.wolfram.com/TorusKnot.html) on torus knots; Lorenz knots ([arXiv:1201.0214](https://arxiv.org/abs/1201.0214)) for the equivalence $T(p,q)\cong T(q,p)$ and mirror images.*

<style>
.tk-controls{display:flex;gap:14px 22px;flex-wrap:wrap;align-items:center;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:12px 16px;margin:14px 0 8px}
.tk-controls label{font-size:14px;white-space:nowrap}
.tk-controls output{min-width:34px;display:inline-block;text-align:right;font-size:13px}
.tk-panels{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin:10px 0}
#knot-preview{width:min(560px,100%);height:400px;background:#0f1626;border:1px solid #2b3857;border-radius:10px;display:block;touch-action:none;cursor:grab;margin:0 auto}
#param-square{width:min(420px,100%);height:420px;background:#f6faf7;border:1px solid #d8e2ee;border-radius:10px;display:block;margin:0 auto}
.panel-cap{font-size:13px;color:#667;text-align:center;margin-top:6px;font-family:Georgia,serif}
#knot-stats{font-size:14px;line-height:1.7;background:#eef3f9;border:1px solid #d8e2ee;border-radius:10px;padding:10px 16px;margin:10px 0;color:#334}
</style>

<script>
(function () {
  var cp = document.getElementById('knot-preview');
  var cs = document.getElementById('param-square');
  var state = { p: 3, q: 2, R: 2.2, r: 1, yaw: 0.9, pitch: 0.7, spin: true };
  var dragging = false, lastX = 0, lastY = 0;
  function g(id) { return document.getElementById(id); }
  function gcd(a, b) { return b ? gcd(b, a % b) : a; }

  function curvePoints(p, q, R, r, N) {
    var d = gcd(p, q), out = [];
    for (var k = 0; k < d; k++) {
      var pts = [];
      for (var i = 0; i <= N; i++) {
        var t = 2 * Math.PI * i / N;
        var u = (p / d) * t + 2 * Math.PI * k / q;
        var v = (q / d) * t;
        var cu = Math.cos(u), cv = Math.cos(v), sv = Math.sin(v);
        var h = R + r * cu;
        pts.push({ x: h * cv, y: h * sv, z: r * Math.sin(u), t: i / N, k: k });
      }
      out.push(pts);
    }
    return out;
  }
  function rotate(pt, y, x) {
    var a = Math.cos(y) * pt.x - Math.sin(y) * pt.y;
    var b = Math.sin(y) * pt.x + Math.cos(y) * pt.y;
    return { x: a, y: Math.cos(x) * b - Math.sin(x) * pt.z, z: Math.sin(x) * b + Math.cos(x) * pt.z };
  }
  function draw3d() {
    var w = cp.clientWidth, h = cp.clientHeight, dpr = Math.min(window.devicePixelRatio || 1, 1.6);
    if (cp.width !== Math.round(w * dpr) || cp.height !== Math.round(h * dpr)) {
      cp.width = Math.round(w * dpr); cp.height = Math.round(h * dpr);
    }
    var ctx = cp.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.fillStyle = '#0f1626'; ctx.fillRect(0, 0, w, h);
    var comps = curvePoints(state.p, state.q, state.R, state.r, 640);
    var scale = Math.min(w, h) * 0.98 / (2 * (state.R + state.r) * 1.06), segs = [];
    for (var c = 0; c < comps.length; c++) {
      var pts = comps[c];
      for (var i = 0; i < pts.length - 1; i++) {
        var a = rotate(pts[i], state.yaw, state.pitch), b = rotate(pts[i + 1], state.yaw, state.pitch);
        var depth = (a.z + b.z) / 2;
        segs.push({
          ax: w / 2 + a.x * scale / (9 - a.z), ay: h / 2 - a.y * scale / (9 - a.z),
          bx: w / 2 + b.x * scale / (9 - b.z), by: h / 2 - b.y * scale / (9 - b.z),
          depth: depth,
          hue: Math.round((205 + 145 * pts[i].t) % 360),
          alpha: 0.30 + 0.65 * (depth + state.R + state.r) / (2 * (state.R + state.r))
        });
      }
    }
    segs.sort(function (s1, s2) { return s1.depth - s2.depth; });
    ctx.lineCap = 'round'; ctx.lineWidth = 2.4;
    for (var s = 0; s < segs.length; s++) {
      var e = segs[s];
      ctx.strokeStyle = 'hsla(' + e.hue + ' 72% 58% / ' + e.alpha.toFixed(3) + ')';
      ctx.beginPath(); ctx.moveTo(e.ax, e.ay); ctx.lineTo(e.bx, e.by); ctx.stroke();
    }
  }
  function drawSquare() {
    var p = state.p, q = state.q, d = gcd(p, q);
    var w = cs.clientWidth, h = cs.clientHeight, dpr = window.devicePixelRatio || 1;
    cs.width = Math.round(w * dpr); cs.height = Math.round(h * dpr);
    var ctx = cs.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var mx = 40, my = 34, bw = w - mx - 26, bh = h - my - 26;
    ctx.fillStyle = '#f6faf7'; ctx.fillRect(0, 0, w, h);
    // grid at multiples of pi/2
    ctx.strokeStyle = 'rgba(51,68,85,0.16)'; ctx.lineWidth = 1;
    for (var i = 0; i <= 4; i++) {
      var gx = mx + (i / 4) * bw, gy = my + (i / 4) * bh;
      ctx.beginPath(); ctx.moveTo(gx, my); ctx.lineTo(gx, my + bh); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(mx, gy); ctx.lineTo(mx + bw, gy); ctx.stroke();
    }
    ctx.strokeStyle = 'rgba(51,68,85,0.6)';
    ctx.strokeRect(mx, my, bw, bh);
    ctx.fillStyle = '#445'; ctx.font = '12px system-ui';
    ctx.fillText('u: 0', mx, h - 8); ctx.fillText('2π', mx + bw - 16, h - 8);
    ctx.fillText('v: 0', 4, my + 4); ctx.fillText('2π', 8, my + bh + 4);
    // component lines
    for (var k = 0; k < d; k++) {
      ctx.strokeStyle = 'hsl(' + Math.round(205 + k * 65 % 360) + ' 70% 46%)';
      ctx.lineWidth = 2.4;
      ctx.beginPath();
      var started = false, px = 0, pv = 0;
      for (var i = 0; i <= 1000; i++) {
        var t = 2 * Math.PI * i / 1000;
        var u = ((p / d) * t + 2 * Math.PI * k / q) % (2 * Math.PI);
        var v = ((q / d) * t) % (2 * Math.PI);
        var X = mx + u / (2 * Math.PI) * bw, Y = my + bh - v / (2 * Math.PI) * bh;
        if (!started) { ctx.moveTo(X, Y); started = true; }
        else if (Math.abs(X - px) > bw * 0.9 || Math.abs(Y - pv) > bh * 0.9) ctx.moveTo(X, Y);
        else ctx.lineTo(X, Y);
        px = X; pv = Y;
      }
      ctx.stroke();
      // start dot
      var u0 = (2 * Math.PI * k / q) % (2 * Math.PI);
      ctx.fillStyle = 'hsl(' + Math.round(205 + k * 65 % 360) + ' 70% 46%)';
      ctx.beginPath();
      ctx.arc(mx + u0 / (2 * Math.PI) * bw, my + bh, 4, 0, 2 * Math.PI);
      ctx.fill();
    }
  }
  function stats() {
    var p = state.p, q = state.q, d = gcd(p, q);
    var html = 'gcd(p, q) = ' + d + ' &nbsp;→&nbsp; ' + (d === 1 ? 'one closed knot' : d + '-component torus link');
    if (d === 1) {
      var c = Math.min((p - 1) * q, (q - 1) * p);
      html += ' &nbsp;·&nbsp; minimal crossings: c = min((p−1)q, (q−1)p) = ' + c;
      if (p > 1 && q > 1) html += ' &nbsp;·&nbsp; genus: g = (p−1)(q−1)/2 = ' + ((p - 1) * (q - 1) / 2);
    } else {
      html += ' &nbsp;·&nbsp; each component is T(' + (p / d) + ', ' + (q / d) + ')';
    }
    if (p === 1 || q === 1) html += ' &nbsp;·&nbsp; unknot (one of the windings is trivial)';
    html += '<br>R = ' + state.R.toFixed(2) + ', r = ' + state.r.toFixed(2) + ' — these change the shape only, never the knot type (while R &gt; r &gt; 0).';
    g('knot-stats').innerHTML = html;
  }
  function refresh() { draw3d(); drawSquare(); stats(); }
  function syncSliders() {
    g('kp2').value = state.p; g('kq2').value = state.q;
    g('kp2v').textContent = state.p; g('kq2v').textContent = state.q;
    g('kpv').textContent = state.p; g('kqv').textContent = state.q;
    g('kRv').textContent = state.R.toFixed(2); g('krv').textContent = state.r.toFixed(2);
  }
  g('kp').addEventListener('input', function () { state.p = +g('kp').value; syncSliders(); refresh(); });
  g('kq').addEventListener('input', function () { state.q = +g('kq').value; syncSliders(); refresh(); });
  g('kR').addEventListener('input', function () { state.R = +g('kR').value; syncSliders(); refresh(); });
  g('kr').addEventListener('input', function () { state.r = +g('kr').value; syncSliders(); refresh(); });
  g('kp2').addEventListener('input', function () { state.p = +g('kp2').value; syncSliders(); refresh(); });
  g('kq2').addEventListener('input', function () { state.q = +g('kq2').value; syncSliders(); refresh(); });
  g('kspin').addEventListener('change', function () { state.spin = g('kspin').checked; });
  cp.addEventListener('pointerdown', function (e) {
    dragging = true; lastX = e.clientX; lastY = e.clientY;
    cp.setPointerCapture(e.pointerId);
  });
  cp.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    state.yaw += (e.clientX - lastX) * 0.008;
    state.pitch += (e.clientY - lastY) * 0.008;
    lastX = e.clientX; lastY = e.clientY;
  });
  ['pointerup', 'pointercancel'].forEach(function (ev) {
    cp.addEventListener(ev, function () { dragging = false; });
  });
  window.addEventListener('resize', refresh);
  syncSliders();
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

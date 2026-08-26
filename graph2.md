

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Secret Inside the Cosine Wave</title>
<style>
  :root { color-scheme: dark; }
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; background: #020204; color: #f6f3ff; font-family: Georgia, 'Times New Roman', serif; }
  body { display: grid; place-items: center; overflow: hidden; }
  main { width: min(1000px, 96vw); }
  h1 { margin: 0 0 19px; text-align: center; font-weight: 500; font-size: clamp(28px, 4.2vw, 56px); letter-spacing: .02em; background: linear-gradient(90deg,#ff7f7f,#ffd76b,#71ddc8,#7caaff,#b479ff); -webkit-background-clip: text; color: transparent; }
  .bar { display: flex; gap: 0; width: 100%; margin-bottom: 18px; }
  button { flex: 1; color: #fff; background: #08090f; border: 1px solid #d7d7df; padding: 10px 7px; font: 600 clamp(13px,2vw,23px)/1 Georgia,serif; cursor: pointer; transition: .2s; }
  button:first-child { background: linear-gradient(100deg,#7f2428,#15151d 62%); }
  button:hover, button.active { background: linear-gradient(105deg,#6e3042,#1a1c38 65%); }
  canvas { display: block; width: 100%; height: min(68vh, 630px); background: #020204; }
  .caption { text-align: center; color: #9ca0b3; margin: 10px 0 0; font: 15px/1.4 ui-sans-serif,system-ui,sans-serif; }
</style>
</head>
<body>
<main>
  <h1>Secret Inside the Cosine Wave</h1>
  <div class="bar">
    <button data-count="50" class="active">50 balls</button>
    <button data-count="500">500 balls</button>
    <button data-count="5000">5000 balls</button>
  </div>
  <canvas id="c"></canvas>
  <p class="caption">Particles fall vertically, bounce from \(y=-\cos x\), then trace reflected trajectories.</p>
</main>
<script>
const canvas = document.querySelector('#c');
const ctx = canvas.getContext('2d');
let W, H, dpr, count = 50, particles = [], start = performance.now();

function resize() {
  dpr = Math.min(devicePixelRatio || 1, 2);
  const rect = canvas.getBoundingClientRect();
  W = rect.width; H = rect.height;
  canvas.width = W * dpr; canvas.height = H * dpr;
  ctx.setTransform(dpr,0,0,dpr,0,0);
  makeParticles();
}
function waveY(x) { return H * 0.60 - H * 0.23 * Math.cos((x / W) * Math.PI * 2); }
function slope(x) { return H * 0.23 * (Math.PI * 2 / W) * Math.sin((x / W) * Math.PI * 2); }
function hue(x) { return 355 - 225 * (x / W); }
function makeParticles() {
  particles = Array.from({length: count}, (_, i) => {
    const x = W * 0.035 + (W * 0.93) * (i + 0.5) / count;
    return { x, y: 0, vx: 0, vy: 0, state: 'fall', delay: i / count * 1.25, trail: [] };
  });
}
function resetParticle(p) {
  p.y = 5; p.vx = 0; p.vy = 135; p.state = 'fall'; p.trail.length = 0;
}
function drawWave() {
  ctx.beginPath();
  for (let x = 0; x <= W; x += 2) {
    const y = waveY(x);
    if (!x) ctx.moveTo(x,y); else ctx.lineTo(x,y);
  }
  const grad = ctx.createLinearGradient(0,0,W,0);
  grad.addColorStop(0,'#ff7a73'); grad.addColorStop(.27,'#fff274'); grad.addColorStop(.53,'#62dfc7'); grad.addColorStop(.77,'#6ba7ff'); grad.addColorStop(1,'#aa77ff');
  ctx.strokeStyle = grad; ctx.lineWidth = 3.2; ctx.shadowBlur = 11; ctx.shadowColor = '#81cbff'; ctx.stroke(); ctx.shadowBlur = 0;
}
function drawGuides() {
  ctx.lineWidth = 1;
  for (let x = W*.035; x <= W*.965; x += Math.max(7, W/count)) {
    ctx.strokeStyle = 'rgba(119,137,176,.13)';
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, waveY(x)); ctx.stroke();
  }
}
function drawParticle(p) {
  if (p.trail.length > 1) {
    ctx.beginPath();
    p.trail.forEach((v,i) => i ? ctx.lineTo(v[0],v[1]) : ctx.moveTo(v[0],v[1]));
    ctx.strokeStyle = `hsla(${hue(p.x)},90%,70%,.22)`; ctx.lineWidth = 1; ctx.stroke();
  }
  ctx.beginPath(); ctx.arc(p.x,p.y, count > 1000 ? 1 : 2.2, 0, Math.PI*2);
  ctx.fillStyle = `hsl(${hue(p.x)},90%,72%)`; ctx.shadowBlur = 7; ctx.shadowColor = ctx.fillStyle; ctx.fill(); ctx.shadowBlur = 0;
}
function step(time) {
  const t = (time - start) / 1000;
  ctx.clearRect(0,0,W,H);
  drawGuides();
  const dt = 1/60;
  for (const p of particles) {
    if (t < p.delay) continue;
    if (p.state === 'fall' && p.y === 0) resetParticle(p);
    if (p.state === 'fall') {
      p.y += p.vy * dt;
      const surface = waveY(p.x);
      if (p.y >= surface) {
        p.y = surface;
        const m = slope(p.x), nx = -m, ny = 1, inv = 1 / Math.hypot(nx,ny);
        const ux = nx*inv, uy = ny*inv;
        const dot = p.vx*ux + p.vy*uy;
        p.vx = (p.vx - 2*dot*ux) * 0.86;
        p.vy = (p.vy - 2*dot*uy) * 0.86;
        p.state = 'bounce';
      }
    } else {
      p.vy += 145 * dt;
      p.x += p.vx * dt; p.y += p.vy * dt;
      p.trail.push([p.x,p.y]); if (p.trail.length > 22) p.trail.shift();
      if (p.y > H + 15 || p.x < -20 || p.x > W + 20) resetParticle(p);
    }
    drawParticle(p);
  }
  drawWave();
  requestAnimationFrame(step);
}
document.querySelectorAll('button').forEach(b => b.onclick = () => {
  document.querySelector('.active').classList.remove('active'); b.classList.add('active');
  count = +b.dataset.count; start = performance.now(); makeParticles();
});
addEventListener('resize', resize); resize(); requestAnimationFrame(step);
</script>
</body>
</html>



I created the second interactive HTML animation: particles fall from above, collide with the cosine surface \(y=-\cos x\), reflect according to the local surface normal, and continue their trajectories with fading trails.

It includes the 50 / 500 / 5000 particle controls and a color gradient matching the supplied reference.

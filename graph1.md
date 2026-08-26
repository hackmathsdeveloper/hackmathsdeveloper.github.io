
https://www.perplexity.ai/search/59c778c7-ace2-4fa3-85be-8dd394e3c3a5?preview=1

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Animated Parametric Surface</title>
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; overflow: hidden; background: #05070c; color: #eaf2ff; font-family: ui-sans-serif, system-ui, sans-serif; }
  #hud { position: fixed; z-index: 2; left: 18px; top: 16px; padding: 13px 15px; border: 1px solid #2d426b; background: rgba(5, 8, 16, .74); border-radius: 10px; backdrop-filter: blur(8px); max-width: 345px; }
  #hud h1 { margin: 0 0 7px; font-size: 15px; font-weight: 650; }
  #hud code { color: #ffd496; font-size: 14px; line-height: 1.55; }
  #hud p { margin: 8px 0 0; color: #aebbd2; font-size: 12px; line-height: 1.45; }
  #controls { position: fixed; z-index: 2; right: 18px; bottom: 17px; display: flex; gap: 10px; align-items: center; padding: 10px; background: rgba(5, 8, 16, .74); border: 1px solid #2d426b; border-radius: 10px; backdrop-filter: blur(8px); }
  button { border: 1px solid #5877ac; background: #11203b; color: #eef5ff; padding: 8px 10px; border-radius: 7px; cursor: pointer; font-weight: 600; }
  button:hover { background: #1b3158; }
  label { font-size: 12px; color: #c2cde1; display: flex; gap: 7px; align-items: center; }
  input { width: 112px; accent-color: #77b6ff; }
  canvas { display: block; }
</style>
</head>
<body>
<div id="hud">
  <h1>Animated parametric surface</h1>
  <code>x = p sin(p) cos(q)<br>y = p sin²(p)<br>z = p cos(p)</code>
  <p>The surface is traced progressively as q sweeps around the vertical axis. Drag to orbit; scroll to zoom.</p>
</div>
<div id="controls">
  <button id="toggle">Pause</button>
  <button id="reset">Reset</button>
  <label>Speed <input id="speed" type="range" min="0.1" max="2.5" step="0.1" value="0.8"></label>
</div>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.161.0/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.161.0/examples/jsm/controls/OrbitControls.js';

const scene = new THREE.Scene();
scene.fog = new THREE.Fog(0x05070c, 20, 67);
const camera = new THREE.PerspectiveCamera(48, innerWidth / innerHeight, 0.1, 200);
camera.position.set(12, 9, 15);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.setAnimationLoop(animate);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.target.set(0, 0, 0);

scene.add(new THREE.HemisphereLight(0x9dc7ff, 0x101321, 2.2));
const light = new THREE.DirectionalLight(0xffffff, 2.2);
light.position.set(7, 11, 10);
scene.add(light);

const grid = new THREE.GridHelper(32, 24, 0x294166, 0x16243e);
grid.position.y = -7.1;
scene.add(grid);

const axes = new THREE.AxesHelper(5);
scene.add(axes);

const pMin = 0, pMax = Math.PI * 4.5, pSteps = 310, qSteps = 360;
const positions = new Float32Array((pSteps + 1) * (qSteps + 1) * 3);
const colors = new Float32Array((pSteps + 1) * (qSteps + 1) * 3);
let k = 0;
const color = new THREE.Color();
for (let i = 0; i <= pSteps; i++) {
  const p = pMin + (pMax - pMin) * i / pSteps;
  for (let j = 0; j <= qSteps; j++) {
    const q = Math.PI * 2 * j / qSteps;
    positions[k] = p * Math.sin(p) * Math.cos(q);
    positions[k + 1] = p * Math.sin(p) * Math.sin(p);
    positions[k + 2] = p * Math.cos(p);
    color.setHSL(0.55 + 0.18 * Math.sin(p * 0.65), 0.82, 0.55);
    colors[k] = color.r; colors[k + 1] = color.g; colors[k + 2] = color.b;
    k += 3;
  }
}
const geometry = new THREE.BufferGeometry();
geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
const material = new THREE.PointsMaterial({ size: 0.045, vertexColors: true, transparent: true, opacity: 0.9, depthWrite: false });
const points = new THREE.Points(geometry, material);
scene.add(points);

const ringMaterial = new THREE.LineBasicMaterial({ color: 0xffc06a, transparent: true, opacity: 0.9 });
const traceGeometry = new THREE.BufferGeometry();
const tracePositions = new Float32Array((pSteps + 1) * 3);
traceGeometry.setAttribute('position', new THREE.BufferAttribute(tracePositions, 3));
traceGeometry.setDrawRange(0, pSteps + 1);
const trace = new THREE.Line(traceGeometry, ringMaterial);
scene.add(trace);

let running = true, phase = 0, speed = 0.8;
function updateTrace(q) {
  const a = traceGeometry.attributes.position.array;
  for (let i = 0; i <= pSteps; i++) {
    const p = pMin + (pMax - pMin) * i / pSteps;
    a[3*i] = p * Math.sin(p) * Math.cos(q);
    a[3*i+1] = p * Math.sin(p) * Math.sin(p);
    a[3*i+2] = p * Math.cos(p);
  }
  traceGeometry.attributes.position.needsUpdate = true;
}

let previous = performance.now();
function animate(now) {
  const dt = Math.min((now - previous) / 1000, 0.05); previous = now;
  if (running) phase += dt * speed;
  const q = phase * Math.PI * 0.6;
  updateTrace(q);
  points.rotation.y = q * 0.18;
  controls.update();
  renderer.render(scene, camera);
}

const toggle = document.querySelector('#toggle');
toggle.onclick = () => { running = !running; toggle.textContent = running ? 'Pause' : 'Play'; };
document.querySelector('#reset').onclick = () => { phase = 0; camera.position.set(12, 9, 15); controls.target.set(0,0,0); controls.update(); };
document.querySelector('#speed').oninput = e => { speed = Number(e.target.value); };
addEventListener('resize', () => { camera.aspect = innerWidth / innerHeight; camera.updateProjectionMatrix(); renderer.setSize(innerWidth, innerHeight); });
</script>
</body>
</html>

I created an interactive WebGL animation of the parametric surface

\[
x=p\sin(p)\cos(q),\qquad y=p\sin^2(p),\qquad z=p\cos(p).
\]

It includes an animated tracing curve, rotation, orbit/zoom controls, plus pause, reset, and speed controls. Open the HTML file in a modern browser.

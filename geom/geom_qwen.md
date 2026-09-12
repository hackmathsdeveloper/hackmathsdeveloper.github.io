
# 10 Intermediate Geometry Problems: Triangles & Circles

Below are 10 problems with SVG diagrams. Solutions are provided at the end.

---

## Problem 1 — Incircle of a Triangle

A triangle has sides 13, 14, and 15. Find the radius $r$ of its inscribed circle.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,280 340,280 240,40" fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="220" cy="200" r="80" fill="rgba(220,38,38,0.08)" stroke="#dc2626" stroke-width="2"/>
  <circle cx="220" cy="200" r="3" fill="#dc2626"/>
  <line x1="220" y1="200" x2="220" y2="280" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="50" y="295" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="345" y="295" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="240" y="32" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="225" y="198" font-size="13" font-family="serif" font-style="italic">I</text>
  <text x="225" y="245" font-size="12" font-family="serif" fill="#dc2626">r</text>
  <text x="130" y="170" font-size="12" font-family="serif">15</text>
  <text x="290" y="170" font-size="12" font-family="serif">13</text>
  <text x="190" y="300" font-size="12" font-family="serif">14</text>
</svg>
```

---

## Problem 2 — Circumcircle of a Right Triangle

A right triangle has legs 5 and 12. Find the radius $R$ of its circumscribed circle.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <circle cx="200" cy="200" r="130" fill="rgba(220,38,38,0.06)" stroke="#dc2626" stroke-width="2"/>
  <polygon points="80,260 80,60 320,260" fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="2"/>
  <rect x="80" y="245" width="15" height="15" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="200" cy="200" r="3" fill="#dc2626"/>
  <line x1="200" y1="200" x2="320" y2="260" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="65" y="275" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="65" y="55" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="325" y="275" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="205" y="195" font-size="13" font-family="serif" font-style="italic">O</text>
  <text x="255" y="240" font-size="12" font-family="serif" fill="#dc2626">R</text>
  <text x="55" y="165" font-size="12" font-family="serif">5</text>
  <text x="190" y="280" font-size="12" font-family="serif">12</text>
  <text x="210" y="150" font-size="12" font-family="serif">13</text>
</svg>
```

---

## Problem 3 — Tangent from an External Point

Point $P$ is 13 units from the center $O$ of a circle. The tangent from $P$ to the circle has length 12. Find the radius $r$.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <circle cx="120" cy="180" r="75" fill="rgba(220,38,38,0.06)" stroke="#dc2626" stroke-width="2"/>
  <circle cx="120" cy="180" r="3" fill="#dc2626"/>
  <circle cx="320" cy="180" r="3" fill="#2563eb"/>
  <circle cx="165" cy="120" r="3" fill="#16a34a"/>
  <line x1="120" y1="180" x2="320" y2="180" stroke="#64748b" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="320" y1="180" x2="165" y2="120" stroke="#16a34a" stroke-width="2"/>
  <line x1="120" y1="180" x2="165" y2="120" stroke="#dc2626" stroke-width="1.5"/>
  <rect x="158" y="120" width="10" height="10" fill="none" stroke="#16a34a" stroke-width="1" transform="rotate(-30 163 125)"/>
  <text x="105" y="175" font-size="14" font-family="serif" font-style="italic">O</text>
  <text x="325" y="175" font-size="14" font-family="serif" font-style="italic">P</text>
  <text x="160" y="110" font-size="14" font-family="serif" font-style="italic">T</text>
  <text x="210" y="170" font-size="12" font-family="serif">13</text>
  <text x="240" y="145" font-size="12" font-family="serif" fill="#16a34a">12</text>
  <text x="135" y="150" font-size="12" font-family="serif" fill="#dc2626">r</text>
</svg>
```

---

## Problem 4 — Two Tangent Circles and a Common Tangent

Two circles with radii 4 and 9 are externally tangent. A common external tangent touches them at $A$ and $B$. Find the length $AB$.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <line x1="60" y1="260" x2="360" y2="260" stroke="#16a34a" stroke-width="2"/>
  <circle cx="120" cy="200" r="60" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="300" cy="125" r="135" fill="rgba(220,38,38,0.06)" stroke="#dc2626" stroke-width="2"/>
  <circle cx="120" cy="200" r="3" fill="#2563eb"/>
  <circle cx="300" cy="125" r="3" fill="#dc2626"/>
  <circle cx="120" cy="260" r="3" fill="#16a34a"/>
  <circle cx="300" cy="260" r="3" fill="#16a34a"/>
  <line x1="120" y1="200" x2="120" y2="260" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="300" y1="125" x2="300" y2="260" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="120" y1="200" x2="300" y2="125" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="105" y="195" font-size="13" font-family="serif" font-style="italic">O₁</text>
  <text x="305" y="120" font-size="13" font-family="serif" font-style="italic">O₂</text>
  <text x="105" y="278" font-size="13" font-family="serif" font-style="italic">A</text>
  <text x="305" y="278" font-size="13" font-family="serif" font-style="italic">B</text>
  <text x="125" y="235" font-size="11" font-family="serif">4</text>
  <text x="305" y="200" font-size="11" font-family="serif">9</text>
  <text x="200" y="155" font-size="11" font-family="serif">13</text>
</svg>
```

---

## Problem 5 — Power of a Point

From a point $P$ outside a circle, a tangent $PT = 8$ and a secant through the center are drawn. The secant intersects the circle at $A$ and $B$, with $PA = 4$. Find $PB$.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <circle cx="140" cy="180" r="100" fill="rgba(220,38,38,0.06)" stroke="#dc2626" stroke-width="2"/>
  <circle cx="140" cy="180" r="3" fill="#dc2626"/>
  <circle cx="340" cy="180" r="3" fill="#2563eb"/>
  <circle cx="240" cy="180" r="3" fill="#16a34a"/>
  <circle cx="40" cy="180" r="3" fill="#16a34a"/>
  <circle cx="200" cy="100" r="3" fill="#9333ea"/>
  <line x1="140" y1="180" x2="340" y2="180" stroke="#64748b" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="40" y1="180" x2="340" y2="180" stroke="#2563eb" stroke-width="1.5"/>
  <line x1="340" y1="180" x2="200" y2="100" stroke="#9333ea" stroke-width="2"/>
  <line x1="140" y1="180" x2="200" y2="100" stroke="#dc2626" stroke-width="1.5"/>
  <text x="125" y="175" font-size="13" font-family="serif" font-style="italic">O</text>
  <text x="345" y="175" font-size="13" font-family="serif" font-style="italic">P</text>
  <text x="240" y="172" font-size="13" font-family="serif" font-style="italic">A</text>
  <text x="25" y="175" font-size="13" font-family="serif" font-style="italic">B</text>
  <text x="200" y="92" font-size="13" font-family="serif" font-style="italic">T</text>
  <text x="275" y="145" font-size="12" font-family="serif" fill="#9333ea">8</text>
  <text x="285" y="200" font-size="12" font-family="serif">4</text>
  <text x="130" y="200" font-size="12" font-family="serif" fill="#dc2626">r</text>
</svg>
```

---

## Problem 6 — Incircle of a Right Triangle

A right triangle has legs 5 and 12 and hypotenuse 13. Find the radius $r$ of its inscribed circle.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <polygon points="80,280 80,80 320,280" fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="120" cy="240" r="40" fill="rgba(220,38,38,0.08)" stroke="#dc2626" stroke-width="2"/>
  <circle cx="120" cy="240" r="3" fill="#dc2626"/>
  <rect x="80" y="265" width="15" height="15" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <line x1="120" y1="240" x2="120" y2="280" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="65" y="295" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="65" y="75" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="325" y="295" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="125" y="238" font-size="13" font-family="serif" font-style="italic">I</text>
  <text x="125" y="265" font-size="12" font-family="serif" fill="#dc2626">r</text>
  <text x="55" y="185" font-size="12" font-family="serif">5</text>
  <text x="190" y="300" font-size="12" font-family="serif">12</text>
  <text x="210" y="170" font-size="12" font-family="serif">13</text>
</svg>
```

---

## Problem 7 — Equilateral Triangle: Ratio of Radii

An equilateral triangle has side length $s$. Let $R$ be the circumradius and $r$ the inradius. Find the ratio $R/r$.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <polygon points="200,40 60,280 340,280" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="200" cy="200" r="160" fill="none" stroke="#dc2626" stroke-width="2"/>
  <circle cx="200" cy="200" r="80" fill="rgba(234,179,8,0.08)" stroke="#ca8a04" stroke-width="2"/>
  <circle cx="200" cy="200" r="3" fill="#64748b"/>
  <line x1="200" y1="200" x2="200" y2="40" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="200" y1="200" x2="200" y2="280" stroke="#ca8a04" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="205" y="35" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="40" y="295" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="345" y="295" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="205" y="195" font-size="13" font-family="serif" font-style="italic">O</text>
  <text x="205" y="125" font-size="12" font-family="serif" fill="#dc2626">R</text>
  <text x="205" y="245" font-size="12" font-family="serif" fill="#ca8a04">r</text>
  <text x="115" y="170" font-size="12" font-family="serif">s</text>
</svg>
```

---

## Problem 8 — Circle on the Base of an Isosceles Triangle

An isosceles triangle has $AB = AC = 10$ and base $BC = 12$. A circle has its center on $BC$ and is tangent to both $AB$ and $AC$. Find its radius $r$.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,280 340,280 200,40" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="200" cy="280" r="96" fill="rgba(220,38,38,0.06)" stroke="#dc2626" stroke-width="2"/>
  <circle cx="200" cy="280" r="3" fill="#dc2626"/>
  <line x1="200" y1="280" x2="152" y2="208" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="45" y="295" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="345" y="295" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="205" y="35" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="205" y="275" font-size="13" font-family="serif" font-style="italic">O</text>
  <text x="165" y="245" font-size="12" font-family="serif" fill="#dc2626">r</text>
  <text x="110" y="170" font-size="12" font-family="serif">10</text>
  <text x="280" y="170" font-size="12" font-family="serif">10</text>
  <text x="190" y="300" font-size="12" font-family="serif">12</text>
</svg>
```

---

## Problem 9 — Circumradius of a Triangle

A triangle has sides 7, 8, and 9. Find the radius $R$ of its circumscribed circle.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <circle cx="200" cy="170" r="130" fill="rgba(220,38,38,0.05)" stroke="#dc2626" stroke-width="2"/>
  <polygon points="90,240 310,240 220,50" fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="200" cy="170" r="3" fill="#dc2626"/>
  <line x1="200" y1="170" x2="310" y2="240" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="75" y="255" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="315" y="255" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="225" y="45" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="205" y="165" font-size="13" font-family="serif" font-style="italic">O</text>
  <text x="255" y="215" font-size="12" font-family="serif" fill="#dc2626">R</text>
  <text x="140" y="155" font-size="12" font-family="serif">9</text>
  <text x="275" y="155" font-size="12" font-family="serif">8</text>
  <text x="190" y="260" font-size="12" font-family="serif">7</text>
</svg>
```

---

## Problem 10 — Altitude and a Circle Through Three Points

In right triangle $ABC$, $\angle C = 90°$, $AC = 6$, $BC = 8$. The altitude from $C$ meets $AB$ at $D$. A circle passes through $C$, $D$, and $B$. Find its radius $R$.

```svg
<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
  <polygon points="80,260 80,60 320,260" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2"/>
  <line x1="80" y1="260" x2="195" y2="122" stroke="#16a34a" stroke-width="2"/>
  <circle cx="200" cy="260" r="120" fill="rgba(220,38,38,0.05)" stroke="#dc2626" stroke-width="2"/>
  <rect x="80" y="245" width="15" height="15" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="195" cy="122" r="3" fill="#16a34a"/>
  <circle cx="80" cy="260" r="3" fill="#2563eb"/>
  <circle cx="80" cy="60" r="3" fill="#2563eb"/>
  <circle cx="320" cy="260" r="3" fill="#2563eb"/>
  <text x="65" y="275" font-size="14" font-family="serif" font-style="italic">C</text>
  <text x="65" y="55" font-size="14" font-family="serif" font-style="italic">A</text>
  <text x="325" y="275" font-size="14" font-family="serif" font-style="italic">B</text>
  <text x="200" y="115" font-size="14" font-family="serif" font-style="italic">D</text>
  <text x="55" y="165" font-size="12" font-family="serif">6</text>
  <text x="190" y="280" font-size="12" font-family="serif">8</text>
  <text x="210" y="150" font-size="12" font-family="serif">10</text>
</svg>
```

---

## Solutions

**1.** Semi-perimeter $s = \frac{13+14+15}{2} = 21$. Area by Heron's formula: $K = \sqrt{21 \cdot 8 \cdot 7 \cdot 6} = 84$. Then $r = \frac{K}{s} = \frac{84}{21} = \boxed{4}$.

**2.** For a right triangle, the hypotenuse is the diameter of the circumcircle. $R = \frac{13}{2} = \boxed{6.5}$.

**3.** Since $OT \perp PT$, triangle $OTP$ is right-angled at $T$. $r = \sqrt{OP^2 - PT^2} = \sqrt{169 - 144} = \sqrt{25} = \boxed{5}$.

**4.** Drop a perpendicular from $O_1$ to $O_2B$, meeting it at $C$. Then $O_2C = 9 - 4 = 5$ and $O_1O_2 = 13$. By Pythagoras, $AB = O_1C = \sqrt{13^2 - 5^2} = \sqrt{144} = \boxed{12}$.

**5.** By the Power of a Point theorem: $PT^2 = PA \cdot PB \implies 64 = 4 \cdot PB \implies PB = \boxed{16}$.

**6.** For a right triangle, $r = \frac{a + b - c}{2} = \frac{5 + 12 - 13}{2} = \boxed{2}$.

**7.** For an equilateral triangle, $R = \frac{s}{\sqrt{3}}$ and $r = \frac{s}{2\sqrt{3}}$. Therefore $\frac{R}{r} = \boxed{2}$.

**8.** Place $B=(0,0)$, $C=(12,0)$, $A=(6,8)$. The center $O=(x,0)$ lies on $BC$. Equating distances from $O$ to lines $AB$ and $AC$ gives $x = 6$, and $r = \frac{4 \cdot 6}{5} = \boxed{\dfrac{24}{5}}$.

**9.** Semi-perimeter $s = 12$. Area $K = \sqrt{12 \cdot 5 \cdot 4 \cdot 3} = 12\sqrt{5}$. Then $R = \frac{abc}{4K} = \frac{7 \cdot 8 \cdot 9}{48\sqrt{5}} = \frac{504}{48\sqrt{5}} = \boxed{\dfrac{21\sqrt{5}}{10}}$.

**10.** Since $CD \perp AB$, angle $\angle CDB = 90°$. A circle through $C, D, B$ with a right angle at $D$ means $CB$ is a diameter. Thus $R = \frac{CB}{2} = \frac{8}{2} = \boxed{4}$.

#!/usr/bin/env python3
"""Generate the exact SVG figures for the Archimedes Project series.

Every curve is sampled from its equation; every label length is computed.
Run from the repository root:

    python3 _tools/archimedes_figures.py

Output: assets/archimedes/*.svg
"""

import math
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "archimedes")

# ---------------------------------------------------------------- palette
BG      = "#252a34"
PANEL   = "#1f2430"
GRID    = "#3a455c"
AXIS    = "#7c89a6"
TEXT    = "#eaeaea"
MUTED   = "#b9c4d8"
TEAL    = "#00adb5"
ORANGE  = "#f78c6c"
YELLOW  = "#ffcb6b"
BLUE    = "#82aaff"
PURPLE  = "#c792ea"
GREEN   = "#c3e88d"
RED     = "#f07178"
WHITE   = "#ffffff"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def head(title, desc, w=900, h=560):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="ttl dsc">
<title id="ttl">{esc(title)}</title>
<desc id="dsc">{esc(desc)}</desc>
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 Z" fill="{MUTED}"/></marker>
  <marker id="arrow-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 Z" fill="{TEAL}"/></marker>
  <marker id="arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 Z" fill="{RED}"/></marker>
  <marker id="dim" viewBox="0 0 8 8" refX="4" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M1,4 L7,4" stroke="{MUTED}" stroke-width="1.4"/></marker>
  <pattern id="hatch" width="9" height="9" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="0" y2="9" stroke="{RED}" stroke-width="2.2" opacity="0.55"/>
  </pattern>
  <style>
    text {{ font-family: 'Source Sans Pro','Helvetica Neue',Arial,sans-serif; fill: {TEXT}; }}
    .ttl {{ font-size: 20px; font-weight: 600; fill: {WHITE}; }}
    .sub {{ font-size: 14px; fill: {MUTED}; }}
    .lbl {{ font-size: 17px; fill: {TEXT}; }}
    .sml {{ font-size: 14px; fill: {MUTED}; }}
    .eq  {{ font-size: 17px; fill: {YELLOW}; }}
    .axis {{ stroke: {AXIS}; stroke-width: 1.5; fill: none; }}
    .grid {{ stroke: {GRID}; stroke-width: 1; fill: none; }}
    .curve {{ stroke: {TEAL}; stroke-width: 2.8; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
    .curve2 {{ stroke: {ORANGE}; stroke-width: 2.4; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
    .curve3 {{ stroke: {BLUE}; stroke-width: 2.2; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
    .thin {{ stroke: {TEXT}; stroke-width: 1.5; fill: none; stroke-linejoin: round; }}
    .thin2 {{ stroke: {MUTED}; stroke-width: 1.2; fill: none; }}
    .dash {{ stroke-dasharray: 7 6; }}
    .dotdash {{ stroke-dasharray: 2 6; }}
    .fill-teal {{ fill: {TEAL}; fill-opacity: 0.16; }}
    .fill-orange {{ fill: {ORANGE}; fill-opacity: 0.15; }}
    .fill-blue {{ fill: {BLUE}; fill-opacity: 0.12; }}
    .fill-purple {{ fill: {PURPLE}; fill-opacity: 0.14; }}
    .fill-green {{ fill: {GREEN}; fill-opacity: 0.12; }}
    .fill-red {{ fill: {RED}; fill-opacity: 0.12; }}
    .pt {{ fill: {TEXT}; }}
    .pt-teal {{ fill: {TEAL}; }}
    .pt-orange {{ fill: {ORANGE}; }}
    .box {{ fill: {PANEL}; stroke: {GRID}; stroke-width: 1.2; }}
  </style>
</defs>
<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="{BG}"/>
'''


def tail():
    return "</svg>\n"


def txt(x, y, s, cls="lbl", anchor="start", fill=None, size=None, weight=None,
        style=None, opacity=None):
    a = f' x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"'
    if fill:
        a += f' fill="{fill}"'
    if size:
        a += f' font-size="{size}"'
    if weight:
        a += f' font-weight="{weight}"'
    if style:
        a += f' font-style="{style}"'
    if opacity is not None:
        a += f' opacity="{opacity}"'
    return f"<text{a}>{esc(s)}</text>\n"


def line(x1, y1, x2, y2, cls="thin", marker=None):
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"{m}/>\n'


def path(d, cls="curve", marker=None):
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<path d="{d}" class="{cls}"{m}/>\n'


def circ(cx, cy, r, cls="thin"):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" class="{cls}"/>\n'


def dot(x, y, cls="pt", r=4.2):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>\n'


def rect(x, y, w, h, cls="box", rx=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" class="{cls}"/>\n'


def linspace(a, b, n):
    if n == 1:
        return [a]
    return [a + (b - a) * i / (n - 1) for i in range(n)]


class Frame:
    """Map mathematical coordinates to a screen box, optionally equal-aspect."""
    def __init__(self, box, xr, yr, equal=True):
        x0, y0, x1, y1 = box
        xmin, xmax = xr
        ymin, ymax = yr
        if equal:
            s = min((x1 - x0) / (xmax - xmin), (y1 - y0) / (ymax - ymin))
            self.sx = self.sy = s
            self.ox = x0 + ((x1 - x0) - (xmax - xmin) * s) / 2 - xmin * s
            self.oy = y0 + ((y1 - y0) - (ymax - ymin) * s) / 2 + ymax * s
        else:
            self.sx = (x1 - x0) / (xmax - xmin)
            self.sy = (y1 - y0) / (ymax - ymin)
            self.ox = x0 - xmin * self.sx
            self.oy = y0 + ymax * self.sy

    def p(self, x, y):
        return (self.ox + x * self.sx, self.oy - y * self.sy)

    def pts(self, pairs):
        return [self.p(x, y) for x, y in pairs]

    def poly(self, pairs, cls="curve", closed=False):
        pp = self.pts(pairs)
        if not pp:
            return ""
        d = "M " + " L ".join(f"{x:.2f},{y:.2f}" for x, y in pp)
        if closed:
            d += " Z"
        return path(d, cls)

    def seg(self, a, b, cls="thin", marker=None):
        p1 = self.p(*a)
        p2 = self.p(*b)
        return line(p1[0], p1[1], p2[0], p2[1], cls, marker)

    def dot(self, xy, cls="pt", r=4.2):
        p = self.p(*xy)
        return dot(p[0], p[1], cls, r)

    def label(self, xy, s, dx=10, dy=-10, anchor="start", cls="lbl",
              fill=None, size=None, style=None):
        p = self.p(*xy)
        return txt(p[0] + dx, p[1] + dy, s, cls=cls, anchor=anchor,
                   fill=fill, size=size, style=style)

    def arrow(self, a, b, cls="thin2", marker="arrow"):
        return self.seg(a, b, cls, marker)

    def dim(self, a, b, off=0.0, cls="thin2", label=None, lab_off=0.0):
        """Dimension line between two world points with a perpendicular offset."""
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        if L == 0:
            return ""
        nx, ny = -dy / L, dx / L
        a2 = (ax + nx * off, ay + ny * off)
        b2 = (bx + nx * off, by + ny * off)
        out = self.seg(a2, b2, cls)
        out += self.seg(a, a2, "thin2 dash")
        out += self.seg(b, b2, "thin2 dash")
        if label:
            mx, my = (a2[0] + b2[0]) / 2, (a2[1] + b2[1]) / 2
            p = self.p(mx, my)
            out += txt(p[0], p[1] - 8 + lab_off, label, cls="sml", anchor="middle")
        return out


def save(name, body, title, desc, w=900, h=560):
    svg = head(title, desc, w, h) + body + tail()
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name)


# ======================================================================
# PART 1 — Quadrature of the Parabola, proposition by proposition
# ======================================================================

def p1_segment():
    w, h = 900, 560
    fr = Frame((60, 60, 840, 500), (-1.7, 1.4), (-0.45, 1.85))
    A = (-1.2, 1.44)
    B = (0.8, 0.64)
    P = (-0.2, 0.04)
    out = []
    # segment fill
    arc = [(x, x * x) for x in linspace(-1.2, 0.8, 320)]
    seg_pts = [A, B] + list(reversed(arc))
    out.append(fr.poly(seg_pts, "fill-teal", closed=True))
    # triangle APB
    out.append(fr.poly([A, P, B], "fill-blue", closed=True))
    # parabola
    curve = [(x, x * x) for x in linspace(-1.55, 1.25, 500)]
    out.append(fr.poly(curve, "curve"))
    # chord and tangent
    out.append(fr.seg(A, B, "thin"))
    m = 2 * P[0]
    t1 = (-1.65, m * (-1.65 - P[0]) + P[1])
    t2 = (1.25, m * (1.25 - P[0]) + P[1])
    out.append(fr.seg(t1, t2, "thin2 dash"))
    # height foot
    vx, vy = B[0] - A[0], B[1] - A[1]
    t = ((P[0] - A[0]) * vx + (P[1] - A[1]) * vy) / (vx * vx + vy * vy)
    F = (A[0] + t * vx, A[1] + t * vy)
    out.append(fr.seg(P, F, "thin2 dash"))
    # right-angle mark at F
    out.append(fr.dot(P))
    out.append(fr.dot(A))
    out.append(fr.dot(B))
    out.append(fr.dot(F, "pt", 3.2))
    out += [
        fr.label(A, "A", -26, -8, "end"),
        fr.label(B, "B", 10, -8),
        fr.label(P, "P", 4, 26, "middle", cls="lbl"),
        fr.label(F, "h", 10, 5, "start", cls="sml"),
        fr.label((0.25, 1.18), "chord AB", 0, 0, "start", cls="sml"),
        fr.label(t2, "tangent at P  ∥  AB", 8, -10, "end", cls="sml"),
    ]
    # segment label
    pos = fr.p(-1.0, 1.0)
    out.append(txt(pos[0], pos[1], "parabolic segment", cls="sml", anchor="start"))
    # triangle label
    pos = fr.p(0.3, 0.15)
    out.append(txt(pos[0], pos[1], "triangle APB", cls="sml", anchor="start", fill=BLUE))
    # axis hint
    out.append(fr.seg((0, -0.3), (0, 1.7), "thin2 dotdash"))
    pos = fr.p(0, 1.66)
    out.append(txt(pos[0] + 8, pos[1], "axis", cls="sml", anchor="start"))
    # title
    out.insert(0, txt(32, 40, "A parabolic segment and its vertex triangle", cls="ttl"))
    save("p1-segment.svg", "".join(out),
         "Parabolic segment and vertex triangle",
         "A parabola with an oblique chord AB, the segment vertex P where the tangent is parallel to AB, and the inscribed triangle APB.", w, h)


def p1_prop1():
    fr = Frame((80, 80, 820, 500), (-1.5, 1.5), (-0.45, 1.55))
    A, B = (-1, 1), (1, 1)
    P, M = (0, 0), (0, 1)
    out = []
    out.append(fr.poly([(x, x * x) for x in linspace(-1.45, 1.45, 500)], "curve"))
    out.append(fr.seg(A, B, "thin"))
    out.append(fr.seg(P, M, "thin2 dash"))
    out.append(fr.seg((-1.45, 0), (1.45, 0), "thin2 dash"))
    # midpoint ticks
    for x in (-0.5, 0.5):
        out.append(fr.seg((x, 0.92), (x, 1.08), "thin2"))
    out += [fr.dot(A), fr.dot(B), fr.dot(P), fr.dot(M, "pt", 3.4)]
    out += [
        fr.label(A, "A", -24, -8, "end"),
        fr.label(B, "B", 10, -8),
        fr.label(P, "P", -22, 6, "end"),
        fr.label(M, "M  (midpoint of AB)", 12, 26, "start"),
        fr.label((-0.5, 1.08), "AM", 0, -6, "middle", cls="sml"),
        fr.label((0.5, 1.08), "MB", 0, -6, "middle", cls="sml"),
        fr.label((0.08, 0.5), "diameter through M", 8, 0, "start", cls="sml", style="italic"),
        fr.label((-1.42, 0.0), "tangent at P", 4, -8, "start", cls="sml"),
    ]
    out.append(txt(32, 40, "Proposition 1 — the midpoint fixes the vertex", cls="ttl"))
    out.append(txt(32, 66, "The axis-parallel line through the chord midpoint meets the parabola at P; the tangent at P is parallel to AB.", cls="sub"))
    save("p1-prop1.svg", "".join(out),
         "Proposition 1: chord midpoint and parallel tangent",
         "The midpoint M of chord AB, the axis-parallel line through M meeting the parabola at P, and the tangent at P parallel to AB.")


def p1_prop2():
    fr = Frame((90, 90, 810, 500), (-1.5, 1.5), (-1.5, 1.55))
    A, B = (-1, 1), (1, 1)
    P, M, E = (0, 0), (0, 1), (0, -1)
    out = []
    out.append(fr.poly([(x, x * x) for x in linspace(-1.42, 1.42, 500)], "curve"))
    out.append(fr.poly([A, B, E], "fill-orange", closed=True))
    out.append(fr.seg(A, B, "thin"))
    out.append(fr.seg((-1.45, 0), (1.45, 0), "thin2 dash"))
    # tangents
    out.append(fr.seg(A, E, "thin2"))
    out.append(fr.seg(B, E, "thin2"))
    # vertical diameter P-M-E
    out.append(fr.seg((0, -1.35), (0, 1.4), "thin2 dash"))
    # equal ticks PM and PE
    for y in (0.5, -0.5):
        out.append(fr.seg((-0.08, y), (0.08, y), "thin"))
    out += [fr.dot(A), fr.dot(B), fr.dot(P), fr.dot(M, "pt", 3.4), fr.dot(E, "pt", 3.4)]
    out += [
        fr.label(A, "A", -24, -8, "end"),
        fr.label(B, "B", 10, -8),
        fr.label(P, "P", 10, 6),
        fr.label(M, "M", -10, -10, "end"),
        fr.label(E, "E", 10, 5),
        fr.label((0.06, 0.5), "PM", 10, 0),
        fr.label((0.06, -0.5), "PE", 10, 0),
        fr.label((0.58, -0.3), "tangent at B", 6, -6, "start", cls="sml"),
    ]
    out.append(txt(32, 40, "Proposition 2 — the tangent cuts the diameter symmetrically", cls="ttl"))
    out.append(txt(32, 66, "The tangent at B meets the diameter PM at E, and P is the midpoint of EM:  PE = PM.", cls="sub"))
    save("p1-prop2.svg", "".join(out),
         "Proposition 2: tangent intercept bisected by the vertex",
         "The tangents at A and B meet at E on the segment diameter, with PM equal to PE.")


def p1_prop5():
    fr = Frame((100, 120, 800, 670), (-1.45, 1.4), (-3.3, 1.5))
    A, B = (-1, 1), (1, 1)
    D = (-1, -3)
    k = 0.4
    K = (k, 1)
    Q = (k, k * k)
    L = (k, 2 * k - 1)
    out = []
    out.append(fr.poly([(x, x * x) for x in linspace(-1.35, 1.3, 500)], "curve"))
    out.append(fr.poly([A, D, B], "fill-blue", closed=True))
    out.append(fr.seg(A, B, "thin"))
    out.append(fr.seg(A, D, "thin2"))
    out.append(fr.seg(B, D, "thin2"))
    out.append(fr.seg(K, L, "thin"))
    out += [fr.dot(A), fr.dot(B), fr.dot(D), fr.dot(K, "pt", 3.6), fr.dot(Q, "pt-teal"), fr.dot(L, "pt", 3.4)]
    out += [
        fr.label(A, "A", -24, -8, "end"),
        fr.label(B, "B", 10, -8),
        fr.label(D, "D", -24, 8, "end"),
        fr.label(K, "K", 10, -8),
        fr.label(Q, "Q", 10, 0),
        fr.label(L, "L", 10, 5),
        fr.label((-0.55, 0.6), "AK", 0, -8, "middle", cls="sml"),
        fr.label((0.55, 0.6), "KB", 0, -8, "middle", cls="sml"),
        fr.label((k - 0.08, 0.58), "QK", 0, 0, "end", cls="sml"),
        fr.label((k + 0.08, 0.08), "LQ", 0, 0, "start", cls="sml"),
    ]
    out.append(txt(32, 40, "Proposition 5 — a transverse line through the enclosing triangle", cls="ttl"))
    out.append(txt(32, 66, "The parabola divides the axis-parallel section QL in the same ratio as the chord is divided at K.", cls="sub"))
    out.append(txt(32, 90, "For this K:  AK/KB = QK/LQ = 7/3.", cls="eq", size=16))
    save("p1-prop5.svg", "".join(out),
         "Proposition 5: QK is to LQ as AK is to KB",
         "The enclosing triangle ADB, a chord division at K, and the parabola point Q dividing the parallel section QL in the ratio AK to KB.",
         w=900, h=700)


def p1_children():
    fr = Frame((70, 90, 700, 500), (-1.18, 1.18), (-0.12, 1.16))
    A, B, P = (-1, 1), (1, 1), (0, 0)
    Ql, Qr = (-0.5, 0.25), (0.5, 0.25)
    R1, R2, R3, R4 = (-0.75, 0.5625), (-0.25, 0.0625), (0.25, 0.0625), (0.75, 0.5625)
    out = []
    arc = [(x, x * x) for x in linspace(-1, 1, 400)]
    out.append(fr.poly([A, P, B], "fill-teal", closed=True))
    out.append(fr.poly([A, Ql, P], "fill-orange", closed=True))
    out.append(fr.poly([P, Qr, B], "fill-orange", closed=True))
    for tri in ([A, R1, Ql], [Ql, R2, P], [P, R3, Qr], [Qr, R4, B]):
        out.append(fr.poly(tri, "fill-blue", closed=True))
    out.append(fr.poly(arc, "curve"))
    out.append(fr.seg(A, B, "thin"))
    out += [fr.dot(A), fr.dot(B), fr.dot(P), fr.dot(Ql, "pt-teal", 3.4), fr.dot(Qr, "pt-teal", 3.4)]
    out += [
        fr.label(A, "A", -22, -8, "end"),
        fr.label(B, "B", 10, -8),
        fr.label(P, "P", -8, 20, "end"),
        fr.label(Ql, "Q", -10, -8, "end", fill=ORANGE),
        fr.label(Qr, "Q′", 10, -8, fill=ORANGE),
    ]
    # legend
    lx = 700
    out.append(rect(lx, 120, 170, 150, "box", 10))
    out.append(rect(lx + 14, 138, 16, 16, "fill-teal", 2))
    out.append(txt(lx + 40, 152, "generation 0", cls="sml"))
    out.append(txt(lx + 40, 174, "area T", cls="eq", size=15))
    out.append(rect(lx + 14, 194, 16, 16, "fill-orange", 2))
    out.append(txt(lx + 40, 208, "generation 1", cls="sml"))
    out.append(txt(lx + 40, 230, "2 × T/8 = T/4", cls="eq", size=15))
    out.append(rect(lx + 14, 250, 16, 16, "fill-blue", 2))
    out.append(txt(lx + 40, 264, "generation 2", cls="sml"))
    out.append(txt(lx + 40, 286, "4 × T/64 = T/16", cls="eq", size=15))
    out.append(txt(32, 40, "The generation law — each child is one eighth of its parent", cls="ttl"))
    out.append(txt(32, 66, "Each new triangle has area T/8; the two children together contribute T/4, so generation n contributes T/4ⁿ.", cls="sub"))
    save("p1-children.svg", "".join(out),
         "Nested triangles in a parabolic segment",
         "Three generations of inscribed triangles in the segment bounded by y = x squared and y = 1, with generation areas T, T/4, T/16.")


def p1_series():
    w, h = 1000, 470
    out = []
    x0, x1 = 80, 940
    unit = (x1 - x0) / (4 / 3)
    y, bh = 130, 70
    bounds = [0, 1, 1.25, 1.3125, 1.328125, 4 / 3]
    colors = [TEAL, ORANGE, BLUE, PURPLE, None]
    # main bar
    for i in range(5):
        xa = x0 + bounds[i] * unit
        xb = x0 + bounds[i + 1] * unit
        if i == 4:
            out.append(f'<rect x="{xa:.2f}" y="{y}" width="{xb-xa:.2f}" height="{bh}" fill="url(#hatch)" stroke="{RED}" stroke-width="1.2"/>\n')
        else:
            out.append(f'<rect x="{xa:.2f}" y="{y}" width="{xb-xa:.2f}" height="{bh}" fill="{colors[i]}" fill-opacity="0.78"/>\n')
            out.append(f'<rect x="{xa:.2f}" y="{y}" width="{xb-xa:.2f}" height="{bh}" fill="none" stroke="{BG}" stroke-width="2"/>\n')
    out.append(txt(x0 + 0.5 * unit, y - 18, "T", cls="eq", anchor="middle", size=19))
    out.append(txt(x0 + 1.125 * unit, y - 18, "T/4", cls="eq", anchor="middle", size=17))
    out.append(txt(x0 + 1.28125 * unit, y - 18, "T/16", cls="eq", anchor="middle", size=15))
    out.append(txt(x0 + 1.3203125 * unit, y - 18, "T/64", cls="eq", anchor="middle", size=14))
    out.append(txt((x0 + x1) / 2, y + bh + 28, "total length  4T/3", cls="sml", anchor="middle", fill=YELLOW))
    # inset: tail from 1.25 to 4/3
    iy, ih = 300, 62
    ix0, ix1 = 80, 940
    lo, hi = 1.25, 4 / 3
    iunit = (ix1 - ix0) / (hi - lo)
    ib = [1.25, 1.3125, 1.328125, 1.33203125, 4 / 3]
    ic = [ORANGE, BLUE, PURPLE, None]
    for i in range(4):
        xa = ix0 + (ib[i] - lo) * iunit
        xb = ix0 + (ib[i + 1] - lo) * iunit
        if i == 3:
            out.append(f'<rect x="{xa:.2f}" y="{iy}" width="{max(xb-xa,2):.2f}" height="{ih}" fill="url(#hatch)" stroke="{RED}" stroke-width="1.2"/>\n')
        else:
            out.append(f'<rect x="{xa:.2f}" y="{iy}" width="{xb-xa:.2f}" height="{ih}" fill="{ic[i]}" fill-opacity="0.78"/>\n')
            out.append(f'<rect x="{xa:.2f}" y="{iy}" width="{xb-xa:.2f}" height="{ih}" fill="none" stroke="{BG}" stroke-width="2"/>\n')
    # ticks
    for v, lab in [(1.25, "1.25"), (1.3125, "1.3125"), (1.328125, "1.328125"), (4/3, "4/3")]:
        xx = ix0 + (v - lo) * iunit
        out.append(line(xx, iy + ih, xx, iy + ih + 8, "thin2"))
        out.append(txt(xx, iy + ih + 24, lab, cls="sml", anchor="middle"))
    out.append(txt(ix0, iy - 16, "tail magnified 16×", cls="sml", anchor="start", fill=MUTED))
    out.append(txt(ix0 + 0.03125 * iunit, iy - 44, "T/16", cls="eq", anchor="middle", size=16))
    out.append(txt(ix0 + 0.0703125 * iunit, iy - 16, "T/64", cls="eq", anchor="middle", size=15))
    # leader for T/256 and remainder
    x256 = ix0 + (1.330078125 - lo) * iunit
    out.append(line(x256, iy - 4, x256 + 40, iy - 34, "thin2"))
    out.append(txt(x256 + 44, iy - 38, "T/256", cls="eq", anchor="start", size=14))
    xr = ix0 + (4 / 3 - lo) * iunit
    out.append(line(x256 + 8, iy + ih + 40, xr, iy + ih + 40, "thin2"))
    out.append(txt(xr, iy + ih + 60, "remainder T/768", cls="sml", anchor="end", fill=RED))
    # title and equation
    out.append(txt(32, 44, "The finite sum plus one third of the last term equals 4T/3", cls="ttl"))
    out.append(txt(32, 72, "For every n,  T + T/4 + … + T/4ⁿ + (1/3)(T/4ⁿ) = 4T/3.  The main bar shows n = 4; the inset magnifies its tail 16×.", cls="sub"))
    out.append(txt(500, 448, "S∞ = 4T/3", cls="eq", anchor="middle", size=21))
    save("p1-series.svg", "".join(out),
         "Geometric series bar for the quadrature",
         "A true-scale bar of total length four thirds of T, with the tail from 1.25 to 4/3 magnified sixteen times to show T/16, T/64, T/256 and the exact remainder T/768.",
         w, h)


# ======================================================================
# PART 2 — the two proofs
# ======================================================================

def p2_auxiliary():
    fr = Frame((90, 100, 810, 640), (-1.35, 1.35), (-3.25, 1.45))
    A, B, D, P = (-1, 1), (1, 1), (-1, -3), (0, 0)
    out = []
    out.append(fr.poly([(x, x * x) for x in linspace(-1.3, 1.3, 500)], "curve"))
    out.append(fr.poly([A, D, B], "fill-orange", closed=True))
    out.append(fr.poly([A, P, B], "fill-teal", closed=True))
    out.append(fr.seg(A, B, "thin"))
    out.append(fr.seg(A, D, "thin2"))
    out.append(fr.seg(D, B, "thin2"))
    out.append(fr.seg(A, P, "thin"))
    out.append(fr.seg(P, B, "thin"))
    out += [fr.dot(A), fr.dot(B), fr.dot(D), fr.dot(P)]
    out += [
        fr.label(A, "A", -22, -8, "end"),
        fr.label(B, "B", 10, -8),
        fr.label(D, "D", -22, 8, "end"),
        fr.label(P, "P", 8, 8),
        fr.label((-0.72, 0.55), "T", 0, 0, "middle", fill=TEAL, size=20),
    ]
    p_lab = fr.p(-0.1, -2.75)
    out.append(txt(p_lab[0], p_lab[1], "area ADB = 4T", cls="lbl", anchor="middle", fill=ORANGE))
    p_to = fr.p(0.1, -1.35)
    out.append(line(p_lab[0], p_lab[1] - 10, p_to[0], p_to[1], "thin2", "arrow-red"))
    # right angle mark at A
    out.append(fr.seg((-1, 0.8), (-0.8, 0.8), "thin2"))
    out.append(fr.seg((-0.8, 0.8), (-0.8, 1), "thin2"))
    out.append(txt(32, 44, "The auxiliary triangle has four times the inscribed triangle", cls="ttl"))
    out.append(txt(32, 72, "AD is parallel to the axis, DB is tangent at B, AB is the chord.  [ADB] = 4[APB].", cls="sub"))
    save("p2-auxiliary.svg", "".join(out),
         "Auxiliary triangle four times the inscribed triangle",
         "The triangle ADB formed by the chord, the axis-parallel through A, and the tangent at B, containing four copies of the area of triangle APB.",
         w=900, h=720)


def p2_parallelogram():
    fr = Frame((110, 100, 790, 500), (-1.2, 1.2), (-0.15, 1.22))
    A, B, P = (-1, 0), (1, 0), (0, 1)
    out = []
    arc = [(x, 1 - x * x) for x in linspace(-1, 1, 300)]
    out.append(fr.poly([(-1, 0), (-1, 1), (1, 1), (1, 0)], "fill-orange", closed=True))
    out.append(fr.poly(arc + [(1, 0), (-1, 0)], "fill-teal", closed=True))
    out.append(fr.poly(arc, "curve"))
    out.append(fr.seg((-1, 0), (1, 0), "thin"))
    out.append(fr.seg((-1, 1), (1, 1), "thin2"))
    out.append(fr.seg((-1, 0), (-1, 1), "thin2"))
    out.append(fr.seg((1, 0), (1, 1), "thin2"))
    out.append(fr.poly([A, P, B], "thin"))
    out += [fr.dot(A), fr.dot(B), fr.dot(P)]
    out += [
        fr.label(A, "A", -22, 8, "end"),
        fr.label(B, "B", 10, 8),
        fr.label(P, "P", 8, -8),
        fr.label((0, 0.58), "segment S", 0, 0, "middle", fill=TEAL, size=18),
        fr.label((-0.98, 1.04), "enclosing rectangle, area 2T", 4, -8, "start", cls="sml", fill=ORANGE),
        fr.label((0.38, 0.22), "triangle T", 0, 0, "middle", fill=BLUE, size=16),
    ]
    out.append(txt(32, 44, "Why the first triangle removes more than half", cls="ttl"))
    out.append(txt(32, 72, "The segment sits strictly inside a rectangle of area 2T, so S < 2T and the triangle T exceeds half the segment.", cls="sub"))
    out.append(txt(450, 536, "S < 2T   ⇒   T > S/2", cls="eq", anchor="middle", size=20))
    save("p2-parallelogram.svg", "".join(out),
         "Parallelogram bound on the parabolic segment",
         "The parabola segment inside the rectangle of area twice the inscribed triangle, proving T greater than S over 2.")


def p2_intervals():
    w, h = 1000, 520
    out = []
    x0, x1 = 160, 690
    xmin, xmax = 0.95, 1.36
    def X(v):
        return x0 + (v - xmin) / (xmax - xmin) * (x1 - x0)
    K = 4 / 3
    rows = 6
    ytop, ystep = 165, 48
    # axis
    out.append(line(x0, ytop - 34, x1, ytop - 34, "axis"))
    for t in [1.0, 1.1, 1.2, 1.3]:
        xx = X(t)
        out.append(line(xx, ytop - 40, xx, ytop - 28, "axis"))
        out.append(txt(xx, ytop - 50, f"{t:g}", cls="sml", anchor="middle"))
    out.append(line(X(K), ytop - 44, X(K), ytop + (rows - 1) * ystep + 20, "thin2 dash"))
    out.append(txt(X(K) + 8, ytop - 50, "K = 4/3", cls="eq", anchor="start"))
    labels = ["n = 0", "n = 1", "n = 2", "n = 3", "n = 4", "n = 5"]
    fracs = ["1", "5/4", "21/16", "85/64", "341/256", "1365/1024"]
    gaps = ["1/3", "1/12", "1/48", "1/192", "1/768", "1/3072"]
    for n in range(rows):
        S = K - 1 / (3 * 4 ** n)
        y = ytop + n * ystep
        out.append(txt(52, y + 5, labels[n], cls="lbl"))
        out.append(f'<rect x="{X(S):.2f}" y="{y-11}" width="{X(K)-X(S):.2f}" height="22" fill="{TEAL}" fill-opacity="0.55" stroke="{TEAL}" stroke-width="1"/>\n')
        out.append(f'<rect x="{X(S):.2f}" y="{y-11}" width="4" height="22" fill="{WHITE}"/>\n')
        out.append(txt(720, y + 5, f"Sₙ = {fracs[n]}", cls="sml", anchor="start"))
        out.append(txt(850, y + 5, f"gap = {gaps[n]}", cls="sml", anchor="start", fill=YELLOW))
    out.append(txt(32, 42, "The squeeze, from below", cls="ttl"))
    out.append(txt(32, 70, "Every finite inscribed sum Sₙ lies below K = 4T/3, and the gap is exactly T/(3·4ⁿ).", cls="sub"))
    save("p2-intervals.svg", "".join(out),
         "Nested intervals converging to four thirds",
         "Six rows showing the inscribed sums 1, 5/4, 21/16, 85/64, 341/256, 1365/1024 approaching 4/3 with exact gaps.", w, h)


def p2_lever():
    fr = Frame((80, 80, 820, 400), (-7.5, 7.5), (-1.6, 2.6))
    out = []
    # beam
    out.append(fr.seg((-7, 0), (7, 0), "thin"))
    # fulcrum
    out.append(fr.poly([(-0.7, 0), (0.7, 0), (0, -1.1)], "fill-orange", closed=True))
    out.append(fr.poly([(-0.7, 0), (0.7, 0), (0, -1.1)], "thin", closed=True))
    # triangle on right: vertices (0,0),(0,4)-> scale? use (0,0),(0,4),(6,0) but y max 2.6
    # use base 6, height 2.4, centroid x = 2
    tri = [(0, 0.02), (0, 2.2), (6, 0.02)]
    out.append(fr.poly(tri, "fill-teal", closed=True))
    out.append(fr.poly(tri, "thin", closed=True))
    G = ((0 + 0 + 6) / 3, (0.02 + 2.2 + 0.02) / 3)
    out.append(fr.dot(G, "pt-orange"))
    out.append(fr.label(G, "centroid", 10, 4, "start", cls="sml", fill=ORANGE))
    # counterweight: area T/3 -> square side sqrt(1/3)*? draw square side 1.15 at -6
    sq = 1.15
    x_sq = fr.p(-6 - sq / 2, 0)[0]
    y_sq = fr.p(-6, sq)[1]
    w_sq = fr.p(sq, 0)[0] - fr.p(0, 0)[0]
    h_sq = abs(fr.p(0, sq)[1] - fr.p(0, 0)[1])
    out.append(f'<rect x="{x_sq:.2f}" y="{y_sq:.2f}" width="{w_sq:.2f}" height="{h_sq:.2f}" fill="{ORANGE}" fill-opacity="0.7" stroke="{ORANGE}" stroke-width="1.5"/>\n')
    out.append(fr.label((-6, sq / 2), "Z = T/3", 0, 5, "middle", cls="sml", fill=WHITE))
    out.append(fr.label((3.0, 0.55), "T", 0, 0, "middle", cls="lbl", fill=WHITE, size=20))
    # distance dimensions
    out.append(fr.dim((0, -0.55), (6, -0.55), 0, label="L"))
    out.append(fr.dim((0, -1.05), (2, -1.05), 0, label="L/3"))
    # vertical dashed through centroid
    out.append(fr.seg((2, 0), (2, 2.2 * 0 + 0.02), "thin2 dash"))
    out.append(txt(32, 44, "The balance lemma behind the mechanical proof", cls="ttl"))
    out.append(txt(32, 72, "A triangle whose centroid is L/3 from the fulcrum is balanced at distance L by one third of its area:  Z·L = T·(L/3).", cls="sub"))
    save("p2-lever.svg", "".join(out),
         "The triangle balance lemma",
         "A triangle on a lever arm with centroid at one third of the arm, balanced by a counterweight of one third its area at the full arm length.",
         w=900, h=430)


def p2_two_proofs():
    w, h = 900, 440
    out = []
    # panel 1
    out.append(rect(40, 80, 360, 290, "box", 14))
    out.append(txt(220, 112, "Mechanical proof", cls="lbl", anchor="middle", fill=TEAL))
    out.append(line(80, 280, 360, 280, "thin"))
    out.append(f'<polygon points="220,280 200,320 240,320" fill="{ORANGE}" fill-opacity="0.8"/>\n')
    out.append(line(220, 280, 220, 180, "thin2 dash"))
    out.append(f'<rect x="90" y="230" width="44" height="50" fill="{TEAL}" fill-opacity="0.7" stroke="{TEAL}"/>\n')
    out.append(f'<rect x="300" y="210" width="34" height="70" fill="{ORANGE}" fill-opacity="0.6" stroke="{ORANGE}"/>\n')
    out.append(txt(112, 222, "W₁", cls="sml", anchor="middle"))
    out.append(txt(317, 202, "W₂", cls="sml", anchor="middle"))
    out.append(txt(220, 348, "finite triangles, trapezoids, balance bounds", cls="sml", anchor="middle"))
    # panel 2
    out.append(rect(500, 80, 360, 290, "box", 14))
    out.append(txt(680, 112, "Geometric proof", cls="lbl", anchor="middle", fill=ORANGE))
    # small parabola
    def px(t): return 680 + 120 * t
    def py(t): return 300 - 150 * (1 - t * t)
    arc = [(px(t), py(t)) for t in linspace(-1, 1, 200)]
    out.append(path("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in arc), "curve"))
    out.append(line(px(-1), py(-1), px(1), py(-1), "thin"))
    out.append(f'<polygon points="{px(-1):.1f},{py(-1):.1f} {px(0):.1f},{py(1):.1f} {px(1):.1f},{py(-1):.1f}" fill="{TEAL}" fill-opacity="0.18" stroke="{TEAL}"/>\n')
    out.append(f'<polygon points="{px(-1):.1f},{py(-1):.1f} {px(-0.5):.1f},{py(0.25):.1f} {px(0):.1f},{py(0):.1f}" fill="none" stroke="{ORANGE}"/>\n')
    out.append(f'<polygon points="{px(0):.1f},{py(0):.1f} {px(0.5):.1f},{py(0.25):.1f} {px(1):.1f},{py(-1):.1f}" fill="none" stroke="{ORANGE}"/>\n')
    out.append(txt(680, 348, "inscribed triangles, finite sums, exhaustion", cls="sml", anchor="middle"))
    # arrows to centre
    out.append(line(390, 225, 406, 225, "thin2", "arrow"))
    out.append(line(494, 225, 510, 225, "thin2", "arrow"))
    # central result
    out.append(rect(408, 155, 84, 140, "box", 10))
    out.append(txt(450, 190, "S =", cls="eq", anchor="middle", size=18))
    out.append(txt(450, 220, "4T", cls="eq", anchor="middle", size=20))
    out.append(line(426, 231, 474, 231, "thin2"))
    out.append(txt(450, 260, "3", cls="eq", anchor="middle", size=20))
    out.append(txt(450, 46, "Two proofs, one number", cls="ttl", anchor="middle"))
    save("p2-two-proofs.svg", "".join(out),
         "Two proofs of the parabolic area",
         "A schematic comparison: the mechanical proof through balances and the geometric proof through nested triangles, both yielding S equals four thirds T.", w, h)


# ======================================================================
# PART 3 — the surface of the sphere
# ======================================================================

def p3_polygons():
    fr = Frame((80, 100, 620, 500), (-1.55, 1.55), (-1.42, 1.42))
    out = []
    # inscribed hexagon fill first
    ins = [(math.cos(k * math.pi / 3), math.sin(k * math.pi / 3)) for k in range(7)]
    out.append(fr.poly(ins, "fill-teal", closed=True))
    # circle
    out.append(fr.poly([(math.cos(t), math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "curve3"))
    out.append(fr.poly(ins, "thin"))
    # circumscribed hexagon
    sec = 1 / math.cos(math.pi / 6)
    cir = [(sec * math.cos(math.pi / 6 + k * math.pi / 3), sec * math.sin(math.pi / 6 + k * math.pi / 3)) for k in range(7)]
    out.append(fr.poly(cir, "curve2"))
    # axis
    out.append(fr.seg((-1.45, 0), (1.45, 0), "thin2 dotdash"))
    # radius and apothem
    out.append(fr.seg((0, 0), (1, 0), "thin"))
    am = math.cos(math.pi / 6)
    out.append(fr.seg((0, 0), (am * math.cos(math.pi / 6), am * math.sin(math.pi / 6)), "thin2 dash"))
    out.append(fr.dot((0, 0)))
    out.append(fr.label((0.5, 0), "R", 0, -10, "middle", cls="sml", fill=YELLOW))
    out.append(fr.label((0.38, 0.22), "aₙ", 8, 0, "start", cls="sml", fill=MUTED))
    out.append(fr.label((0.0, 0.0), "O", 8, 16, "start", cls="sml"))
    out.append(txt(32, 44, "Trapping the circle between two polygons", cls="ttl"))
    out.append(txt(32, 72, "The inscribed polygon lies inside; the circumscribed polygon lies outside and touches at the side midpoints.", cls="sub"))
    lx, ly = 650, 110
    out.append(rect(lx, ly, 230, 100, "box", 10))
    out.append(rect(lx + 14, ly + 16, 18, 18, "fill-teal", 3))
    out.append(txt(lx + 42, ly + 31, "inscribed", cls="sml"))
    out.append(line(lx + 14, ly + 52, lx + 32, ly + 52, "curve2"))
    out.append(txt(lx + 42, ly + 58, "circumscribed", cls="sml"))
    out.append(txt(lx + 14, ly + 82, "shown: 6 sides", cls="sml", fill=MUTED))
    save("p3-polygons.svg", "".join(out),
         "Circle with inscribed and circumscribed polygons",
         "A circle of radius R, an inscribed regular hexagon, a circumscribed regular hexagon, the radius R, and the apothem a_n.")


def p3_frustum():
    fr = Frame((80, 160, 620, 500), (-0.6, 5.1), (-1.9, 1.9))
    out = []
    x1, r1 = 0.0, 1.6
    x2, r2 = 4.2, 0.9
    # full axial section (both halves)
    full = [(x1, -r1), (x1, r1), (x2, r2), (x2, -r2)]
    out.append(fr.poly(full, "fill-teal", closed=True))
    out.append(fr.poly(full, "thin", closed=True))
    # axis
    out.append(fr.seg((-0.4, 0), (4.9, 0), "thin2 dotdash"))
    # radii
    out.append(fr.seg((x1, 0), (x1, r1), "thin"))
    out.append(fr.seg((x2, 0), (x2, r2), "thin"))
    # slant midpoint
    mx, my = (x1 + x2) / 2, (r1 + r2) / 2
    out.append(fr.dot((mx, my), "pt-orange", 4.2))
    out.append(fr.seg((mx, my), (mx, 0), "thin2 dash"))
    out.append(fr.seg((x1, r1), (x2, r2), "curve2"))
    out += [
        fr.label((x1, r1), "r₁", -10, -8, "end", cls="sml", fill=YELLOW),
        fr.label((x2, r2), "r₂", 10, -8, "start", cls="sml", fill=YELLOW),
        fr.label((mx, my), "midpoint", 10, -8, "start", cls="sml", fill=ORANGE),
        fr.label((mx, 0), "r_mid = (r₁+r₂)/2", 8, 20, "start", cls="sml"),
        fr.label(((x1 + x2) / 2 + 0.25, (r1 + r2) / 2 + 0.38), "slant s", 0, 0, "middle", cls="sml"),
    ]
    # formula box
    out.append(rect(640, 120, 240, 110, "box", 10))
    out.append(txt(760, 152, "lateral area", cls="eq", anchor="middle", size=17))
    out.append(txt(760, 180, "=  2π · r_mid · s", cls="eq", anchor="middle", size=17))
    out.append(txt(760, 210, "the frustum lemma", cls="sml", anchor="middle"))
    out.append(txt(32, 44, "The frustum lemma", cls="ttl"))
    out.append(txt(32, 72, "A frustum's lateral area equals 2π times the midpoint radius times the slant height.", cls="sub"))
    save("p3-frustum.svg", "".join(out),
         "Lateral area of a conical frustum",
         "An axial cross-section of a conical frustum with radii r1 and r2, slant s, and midpoint radius r_mid, illustrating the lemma area equals 2 pi r_mid s.")


def p3_zones():
    fr = Frame((120, 100, 780, 500), (-1.32, 1.32), (-1.32, 1.32))
    out = []
    zs = [-1, -0.6, -0.2, 0.2, 0.6, 1]
    cols = ["fill-teal", "fill-blue", "fill-purple", "fill-blue", "fill-teal"]
    for i in range(5):
        z0, z1 = zs[i], zs[i + 1]
        p0, p1 = math.asin(z0), math.asin(z1)
        right = [(math.cos(t), math.sin(t)) for t in linspace(p0, p1, 60)]
        left = [(math.cos(t), math.sin(t)) for t in linspace(math.pi - p1, math.pi - p0, 60)]
        pts = right + left
        out.append(fr.poly(pts, cols[i], closed=True))
    out.append(fr.poly([(math.cos(t), math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "curve"))
    for z in zs:
        x = math.sqrt(max(0, 1 - z * z))
        out.append(fr.seg((-x, z), (x, z), "thin2"))
    out.append(fr.seg((0, -1.2), (0, 1.2), "thin2 dotdash"))
    out.append(fr.dot((0, 0), "pt", 3.2))
    out.append(fr.label((0, 0), "O", 8, 16, "start", cls="sml"))
    # dimension for one band on the right
    zz0, zz1 = 0.2, 0.6
    xd = 1.12
    out.append(fr.seg((xd, zz0), (xd, zz1), "thin2"))
    out.append(fr.seg((xd - 0.05, zz0), (xd + 0.05, zz0), "thin2"))
    out.append(fr.seg((xd - 0.05, zz1), (xd + 0.05, zz1), "thin2"))
    out.append(fr.label((xd, (zz0 + zz1) / 2), "Δz", 12, 0, "start", cls="sml", fill=YELLOW))
    out.append(fr.label((0.0, 1.16), "R", 8, 0, "start", cls="sml", fill=YELLOW))
    out.append(txt(32, 44, "Equal heights, equal areas", cls="ttl"))
    out.append(txt(32, 72, "Each horizontal band of the sphere has area 2πRΔz, independent of where it sits.", cls="sub"))
    out.append(txt(450, 540, "area(band) = 2πR · Δz", cls="eq", anchor="middle", size=20))
    save("p3-zones.svg", "".join(out),
         "Sphere divided into equal-height bands",
         "A sphere cut by equally spaced horizontal planes, with alternating shaded bands, showing that each band of height delta z has area 2 pi R delta z.")


def p3_squeeze():
    w, h = 900, 520
    out = []
    x0, y0, x1, y1 = 120, 100, 830, 430
    nmin, nmax = 2, 12
    ymin, ymax = 0.6, 1.45
    def X(n): return x0 + (n - nmin) / (nmax - nmin) * (x1 - x0)
    def Y(v): return y1 - (v - ymin) / (ymax - ymin) * (y1 - y0)
    def sinc(n): return math.cos(math.pi / (2 * n))
    def scirc(n):
        d = math.pi / (2 * n)
        return (1 / math.cos(d) ** 2) * math.sin((n - 1) * d)
    ns = [nmin + i * 0.05 for i in range(int((nmax - nmin) / 0.05) + 1)]
    ins = [(X(n), Y(sinc(n))) for n in ns]
    cir = [(X(n), Y(scirc(n))) for n in ns]
    # shade between
    band = ins + list(reversed(cir))
    out.append(path("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in band) + " Z", "fill-teal"))
    out.append(path("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in ins), "curve"))
    out.append(path("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in cir), "curve2"))
    # limit line
    out.append(line(x0, Y(1), x1, Y(1), "thin2 dash"))
    out.append(txt(x1 + 6, Y(1) + 5, "1", cls="sml", anchor="start"))
    # axes
    out.append(line(x0, y1, x1, y1, "axis"))
    out.append(line(x0, y0, x0, y1, "axis"))
    for n in range(2, 13, 2):
        out.append(line(X(n), y1, X(n), y1 + 7, "axis"))
        out.append(txt(X(n), y1 + 24, str(2 * n), cls="sml", anchor="middle"))
    for v in [0.6, 0.8, 1.0, 1.2, 1.4]:
        out.append(line(x0 - 7, Y(v), x0, Y(v), "axis"))
        out.append(txt(x0 - 12, Y(v) + 5, f"{v:g}", cls="sml", anchor="end"))
    out.append(txt((x0 + x1) / 2, y1 + 52, "number of sides of the polygon  (2n)", cls="sml", anchor="middle"))
    out.append(txt(44, (y0 + y1) / 2, "area / (4πR²)", cls="sml", anchor="middle", style="italic"))
    # curve labels
    out.append(txt(X(6.2), Y(scirc(6.2)) - 12, "circumscribed", cls="sml", fill=ORANGE, anchor="middle"))
    out.append(txt(X(6.2), Y(sinc(6.2)) + 24, "inscribed", cls="sml", fill=TEAL, anchor="middle"))
    out.append(txt(32, 44, "The squeeze that produces 4πR²", cls="ttl"))
    out.append(txt(32, 72, "Both polygonal surface areas approach the same limit; the gap can be made smaller than any prescribed area.", cls="sub"))
    out.append(txt(450, 495, "inscribed  <  sphere  <  circumscribed   →   4πR²", cls="eq", anchor="middle", size=19))
    save("p3-squeeze.svg", "".join(out),
         "Inscribed and circumscribed surface areas approaching four pi R squared",
         "Two curves plotting the inscribed and circumscribed polygonal surface areas divided by 4 pi R squared against the number of polygon sides; both converge to 1.", w, h)


# ======================================================================
# PART 4 — On the Sphere and Cylinder
# ======================================================================

def p4_sphere_cylinder():
    fr = Frame((70, 100, 600, 500), (-1.45, 1.45), (-1.45, 1.45))
    out = []
    out.append(fr.poly([(-1, -1), (1, -1), (1, 1), (-1, 1)], "fill-orange", closed=True))
    out.append(fr.poly([(-1, -1), (1, -1), (1, 1), (-1, 1)], "thin", closed=True))
    out.append(fr.poly([(math.cos(t), math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "curve"))
    out.append(fr.poly([(math.cos(t), math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "fill-teal", closed=True))
    out.append(fr.seg((-1, 0), (1, 0), "thin2 dotdash"))
    out.append(fr.seg((0, -1), (0, 1), "thin2 dotdash"))
    out.append(fr.dot((0, 0)))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((0, 1), "r", 8, -8, "start", cls="sml", fill=YELLOW),
        fr.label((1, 0.0), "r", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((0.0, -1.0), "2r", -10, 8, "end", cls="sml", fill=YELLOW),
    ]
    # dimension height
    out.append(fr.dim((1.22, -1), (1.22, 1), 0, label="2r"))
    # result box
    out.append(rect(630, 110, 250, 190, "box", 12))
    out.append(txt(755, 145, "V_sphere / V_cylinder", cls="eq", anchor="middle", size=16))
    out.append(txt(755, 168, "= 2/3", cls="eq", anchor="middle", size=17))
    out.append(txt(755, 198, "A_sphere / A_cylinder", cls="eq", anchor="middle", size=16))
    out.append(txt(755, 221, "= 2/3", cls="eq", anchor="middle", size=17))
    out.append(txt(755, 250, "sphere area = lateral area", cls="sml", anchor="middle"))
    out.append(txt(755, 272, "4πr² = 2πr · 2r", cls="sml", anchor="middle", fill=TEAL))
    out.append(txt(755, 291, "the tombstone ratio", cls="sml", anchor="middle", fill=MUTED))
    out.append(txt(32, 44, "The sphere inside its cylinder", cls="ttl"))
    out.append(txt(32, 72, "A sphere of radius r exactly fits a cylinder of radius r and height 2r; both volume and total surface stand in the ratio 2:3.", cls="sub"))
    save("p4-sphere-cylinder.svg", "".join(out),
         "Sphere inscribed in a cylinder",
         "A circle of radius r inside the square of side 2r, representing the sphere inside its circumscribing cylinder, with the 2 to 3 ratios.")


def p4_cap():
    fr = Frame((70, 100, 600, 500), (-1.35, 1.35), (-1.35, 1.35))
    out = []
    r = 1.0
    hcap = 0.65
    zc = r - hcap
    xb = math.sqrt(r * r - zc * zc)
    # cap fill: arc from left base to right base over the top
    phi = math.asin(zc)
    arc = [(math.cos(t), math.sin(t)) for t in linspace(phi, math.pi - phi, 120)]
    out.append(fr.poly([(xb, zc)] + arc + [(-xb, zc)], "fill-teal", closed=True))
    out.append(fr.poly([(math.cos(t), math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "curve"))
    out.append(fr.seg((-xb, zc), (xb, zc), "thin"))
    out.append(fr.seg((0, zc), (0, r), "thin2 dash"))
    out.append(fr.seg((0, zc), (xb, zc), "thin2 dash"))
    out.append(fr.seg((0, 0), (xb, zc), "thin2 dash"))
    out.append(fr.dot((0, 0), "pt", 3.2))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((0, (zc + r) / 2), "h", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((xb / 2, zc), "base radius", 0, 22, "middle", cls="sml"),
        fr.label((xb / 2, zc / 2), "r", -10, 0, "end", cls="sml", fill=YELLOW),
        fr.label((0, r), "vertex", 10, -8, "start", cls="sml"),
    ]
    out.append(rect(630, 100, 250, 160, "box", 12))
    out.append(txt(755, 136, "A_cap = 2πrh", cls="eq", anchor="middle", size=19))
    out.append(txt(755, 174, "V_cap = πh²(r − h/3)", cls="eq", anchor="middle", size=18))
    out.append(txt(755, 210, "h = height of the cap", cls="sml", anchor="middle"))
    out.append(txt(755, 234, "base radius = √(2rh − h²)", cls="sml", anchor="middle", fill=TEAL))
    out.append(txt(32, 44, "A spherical cap", cls="ttl"))
    out.append(txt(32, 72, "The cap's area depends only on its height h, not on where it is cut from the sphere.", cls="sub"))
    save("p4-cap.svg", "".join(out),
         "Spherical cap with height h",
         "A sphere with a cap of height h shaded above a horizontal chord, showing the base radius and the formulas for cap area and volume.")


def p4_sector():
    fr = Frame((70, 100, 600, 500), (-1.35, 1.35), (-1.35, 1.35))
    out = []
    r = 1.0
    hcap = 0.6
    zc = r - hcap
    alpha = math.acos(zc)
    # circular sector from pi/2-alpha to pi/2+alpha
    a0, a1 = math.pi / 2 - alpha, math.pi / 2 + alpha
    pts = [(0, 0)] + [(math.cos(t), math.sin(t)) for t in linspace(a0, a1, 160)]
    out.append(fr.poly(pts, "fill-teal", closed=True))
    out.append(fr.poly([(math.cos(t), math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "curve"))
    out.append(fr.seg((0, 0), (math.cos(a0), math.sin(a0)), "thin"))
    out.append(fr.seg((0, 0), (math.cos(a1), math.sin(a1)), "thin"))
    xb = math.sqrt(r * r - zc * zc)
    out.append(fr.seg((-xb, zc), (xb, zc), "thin2 dash"))
    out.append(fr.dot((0, 0)))
    # angle arc
    out.append(fr.poly([(0.28 * math.cos(t), 0.28 * math.sin(t)) for t in linspace(math.pi / 2 - alpha, math.pi / 2 + alpha, 60)], "thin2"))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((0.0, 0.32), "α", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((0, (zc + r) / 2), "h", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((0.55, zc + 0.1), "cap", 0, 0, "middle", cls="sml", fill=TEAL),
    ]
    out.append(rect(630, 100, 250, 160, "box", 12))
    out.append(txt(755, 136, "V_sector = (2/3)πr²h", cls="eq", anchor="middle", size=18))
    out.append(txt(755, 174, "A_cap = 2πrh", cls="eq", anchor="middle", size=19))
    out.append(txt(755, 210, "the sector is a cone plus the cap", cls="sml", anchor="middle"))
    out.append(txt(755, 234, "apex at the sphere's centre", cls="sml", anchor="middle", fill=TEAL))
    out.append(txt(32, 44, "A spherical sector", cls="ttl"))
    out.append(txt(32, 72, "The sector generated by a circular sector of the sphere: a cone from the centre plus the spherical cap.", cls="sub"))
    save("p4-sector.svg", "".join(out),
         "Spherical sector generated by a circular sector",
         "A circle with a shaded circular sector of half-angle alpha about the vertical axis, its chord, and the cap it generates, with the sector volume formula.")


# ======================================================================
# PART 5 — On Spirals
# ======================================================================

A_SPIRAL = 1 / (2 * math.pi)


def spiral_pts(t0, t1, n=500, a=A_SPIRAL):
    return [(a * t * math.cos(t), a * t * math.sin(t)) for t in linspace(t0, t1, n)]


def p5_spiral():
    fr = Frame((110, 100, 790, 500), (-2.2, 2.2), (-2.2, 2.2))
    out = []
    # circles
    for rr in (1, 2):
        out.append(fr.poly([(rr * math.cos(t), rr * math.sin(t)) for t in linspace(0, 2 * math.pi, 300)], "thin2 dash"))
    # first turn region
    first = spiral_pts(0, 2 * math.pi)
    out.append(fr.poly(first + [(0, 0)], "fill-teal", closed=True))
    # second ring
    outer = spiral_pts(2 * math.pi, 4 * math.pi)
    inner_rev = list(reversed(spiral_pts(0, 2 * math.pi)))
    ring = outer + [(1, 0)] + inner_rev
    out.append(fr.poly(ring, "fill-orange", closed=True))
    # spiral
    out.append(fr.poly(spiral_pts(0, 4 * math.pi), "curve"))
    out.append(fr.seg((-2.1, 0), (2.1, 0), "axis"))
    out.append(fr.dot((0, 0)))
    out.append(fr.dot((1, 0), "pt-teal", 4.2))
    out.append(fr.dot((2, 0), "pt-orange", 4.2))
    out += [
        fr.label((0, 0), "O", 8, 18, "start", cls="sml"),
        fr.label((1, 0), "P₁", 6, 22, "start", cls="sml", fill=TEAL),
        fr.label((2, 0), "P₂", 6, 22, "start", cls="sml", fill=ORANGE),
        fr.label((-1.45, 1.05), "first turn:  A₁ = πd²/3", 0, 0, "middle", cls="sml", fill=TEAL),
        fr.label((0.1, -1.35), "second-ring shell:  R₂ = 6A₁", 0, 0, "middle", cls="sml", fill=ORANGE),
        fr.label((1.5, 1.5), "radius d", 10, -6, "start", cls="sml"),
        fr.label((1.75, 0.35), "radius 2d", 8, -8, "start", cls="sml"),
    ]
    out.append(txt(32, 44, "Two turns of the Archimedean spiral", cls="ttl"))
    out.append(txt(32, 72, "r = aθ.  The first turn encloses A₁ = πd²/3; the shell added by the second turn has area 6A₁.", cls="sub"))
    save("p5-spiral.svg", "".join(out),
         "Two turns of an Archimedean spiral with shaded areas",
         "The spiral r equals a theta over two turns, with the first-turn region shaded teal and the second-turn shell shaded orange, the circles of radius d and 2d shown dashed.")


def p5_tangent():
    w, h = 900, 560
    out = []
    # left panel: exact right triangle, OP = 50 px, OT = 2*pi*50
    O = (100, 515)
    P = (150, 515)
    T = (100, 515 - 2 * math.pi * 50)
    out.append(line(O[0], O[1], P[0], P[1], "thin"))
    out.append(line(O[0], O[1], T[0], T[1], "thin"))
    out.append(line(P[0], P[1], T[0], T[1], "curve2"))
    out.append(f'<path d="M {O[0]+18:.1f},{O[1]:.1f} L {O[0]+18:.1f},{O[1]-18:.1f} L {O[0]:.1f},{O[1]-18:.1f}" class="thin2"/>\n')
    out.append(dot(P[0], P[1], "pt-teal"))
    out.append(dot(T[0], T[1], "pt-orange"))
    out.append(dot(O[0], O[1]))
    out.append(txt(O[0] - 10, O[1] + 20, "O", cls="lbl", anchor="end"))
    out.append(txt(P[0] + 8, P[1] + 20, "P", cls="lbl", fill=TEAL))
    out.append(txt(T[0] + 8, T[1] - 4, "T", cls="lbl", fill=ORANGE))
    out.append(txt((O[0] + P[0]) / 2, O[1] + 24, "d", cls="eq", anchor="middle"))
    out.append(txt(O[0] - 8, (O[1] + T[1]) / 2, "OT = 2πd", cls="eq", anchor="end", fill=YELLOW))
    out.append(txt(P[0] + 74, (P[1] + T[1]) / 2, "tangent", cls="sml", anchor="start", fill=ORANGE))
    out.append(txt(240, 120, "tan ψ = OT/OP = 2π", cls="eq", anchor="middle", size=18))
    out.append(txt(240, 148, "ψ is the angle between OP and the tangent", cls="sml", anchor="middle"))
    # right panel: spiral near P
    cx, cy, sc = 650, 330, 120
    def sp(t): return (cx + sc * A_SPIRAL * t * math.cos(t), cy - sc * A_SPIRAL * t * math.sin(t))
    pts = [sp(t) for t in linspace(0, 2 * math.pi, 400)]
    out.append(path("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts), "curve"))
    # tangent short segment at P: y = 2pi(x-1) in world, scale
    xp, yp = sp(2 * math.pi)
    def tang(x):
        yw = 2 * math.pi * (x - 1)
        return (cx + sc * x, cy - sc * yw)
    a = tang(0.82)
    b = tang(1.10)
    out.append(line(a[0], a[1], b[0], b[1], "curve2"))
    out.append(line(cx, cy, xp, yp, "thin2 dash"))
    out.append(dot(cx, cy))
    out.append(dot(xp, yp, "pt-teal"))
    out.append(txt(cx - 8, cy + 20, "O", cls="lbl", anchor="end"))
    out.append(txt(xp + 8, yp + 20, "P", cls="lbl", fill=TEAL))
    out.append(txt(xp + 40, yp - 40, "slope 2π", cls="sml", fill=ORANGE))
    out.append(txt(650, 110, "First turn, with the tangent at P", cls="lbl", anchor="middle"))
    out.append(txt(650, 136, "P is the end of the first complete turn", cls="sml", anchor="middle", fill=MUTED))
    out.append(txt(32, 44, "Proposition 18 — unwinding the circumference", cls="ttl"))
    out.append(txt(32, 72, "The tangent at the end of the first turn meets the perpendicular through O at T, with OT equal to the first circle's circumference.", cls="sub"))
    save("p5-tangent.svg", "".join(out),
         "Tangent construction giving a straight segment equal to the circumference",
         "Left: a right triangle OPT with OP equal to d and OT equal to 2 pi d. Right: the first turn of the spiral with the tangent at P.", w, h)


def p5_trisection():
    a = 1.8 / math.pi
    fr = Frame((120, 90, 780, 520), (-0.08, 0.82), (-0.08, 0.72))
    out = []
    pts = [(a * t * math.cos(t), a * t * math.sin(t)) for t in linspace(0, 1.2, 400)]
    out.append(fr.poly(pts, "curve"))
    # rays
    for ang, lab, L in [(0, "0°", 0.62), (math.pi / 9, "20°", 0.38), (math.pi / 3, "60°", 0.38)]:
        out.append(fr.seg((0, 0), (L * math.cos(ang), L * math.sin(ang)), "thin2"))
        out.append(fr.label((L * math.cos(ang), L * math.sin(ang)), lab, 8, 0, "start", cls="sml"))
    # target P at 60 deg, r=0.6
    th = math.pi / 3
    r = a * th
    P = (r * math.cos(th), r * math.sin(th))
    Q = ((r / 3) * math.cos(th / 3), (r / 3) * math.sin(th / 3))
    out.append(fr.seg((0, 0), P, "thin"))
    out.append(fr.poly([((r / 3) * math.cos(t), (r / 3) * math.sin(t)) for t in linspace(0, 2 * math.pi, 200)], "thin2 dash"))
    # equal marks on OP
    for k in (1, 2):
        rr = r * k / 3
        # small perpendicular tick
        dx, dy = -math.sin(th), math.cos(th)
        c = (rr * math.cos(th), rr * math.sin(th))
        out.append(fr.seg((c[0] - 0.012 * dx, c[1] - 0.012 * dy), (c[0] + 0.012 * dx, c[1] + 0.012 * dy), "thin"))
    out.append(fr.dot(P, "pt-teal"))
    out.append(fr.dot(Q, "pt-orange"))
    out += [
        fr.label(P, "P", 8, -8, "start", cls="lbl", fill=TEAL),
        fr.label(Q, "Q", 8, -8, "start", cls="lbl", fill=ORANGE),
        fr.label((r / 2 * math.cos(th), r / 2 * math.sin(th)), "r", 8, -8, "start", cls="sml"),
        fr.label((r / 6 * math.cos(th), r / 6 * math.sin(th)), "r/3", 8, 12, "start", cls="sml"),
    ]
    # angle arc 20 and 60
    out.append(fr.poly([(0.12 * math.cos(t), 0.12 * math.sin(t)) for t in linspace(0, th, 60)], "thin2"))
    out.append(txt(32, 44, "Trisecting 60° with a spiral", cls="ttl"))
    out.append(txt(32, 72, "Divide OP into three equal parts, draw the circle of radius r/3, and meet the spiral: the ray to Q is at 20°.", cls="sub"))
    out.append(txt(450, 545, "60° = 3 × 20°", cls="eq", anchor="middle", size=20))
    save("p5-trisection.svg", "".join(out),
         "Trisecting a sixty degree angle with an Archimedean spiral",
         "An Archimedean spiral with rays at zero, twenty, and sixty degrees, the radius OP divided into three equal parts, and the circle of radius r over three meeting the spiral at twenty degrees.")


def p5_area_ratio():
    a = 1.0
    t1, t2 = math.pi / 6, 2 * math.pi / 3
    fr = Frame((110, 100, 790, 500), (-0.4, 2.4), (-0.55, 2.2))
    out = []
    r1, r2 = a * t1, a * t2
    # sector of radius r2
    sec = [(0, 0)] + [(r2 * math.cos(t), r2 * math.sin(t)) for t in linspace(t1, t2, 160)]
    out.append(fr.poly(sec, "fill-orange", closed=True))
    # spiral region
    arc = [(a * t * math.cos(t), a * t * math.sin(t)) for t in linspace(t1, t2, 240)]
    region = [(0, 0)] + arc
    out.append(fr.poly(region, "fill-teal", closed=True))
    # boundaries
    out.append(fr.poly([(r2 * math.cos(t), r2 * math.sin(t)) for t in linspace(t1, t2, 160)], "curve2"))
    out.append(fr.poly(arc, "curve"))
    out.append(fr.seg((0, 0), (r1 * math.cos(t1), r1 * math.sin(t1)), "thin"))
    out.append(fr.seg((0, 0), (r2 * math.cos(t2), r2 * math.sin(t2)), "thin"))
    out.append(fr.dot((0, 0)))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((r1 * math.cos(t1), r1 * math.sin(t1)), "r₁", 8, -6, "start", cls="sml"),
        fr.label((r2 * math.cos(t2), r2 * math.sin(t2)), "r₂", 8, -6, "start", cls="sml"),
        fr.label((0.85, 0.95), "spiral area", 0, 0, "middle", cls="sml", fill=TEAL),
        fr.label((1.65, 0.35), "comparison sector", 0, 0, "middle", cls="sml", fill=ORANGE),
    ]
    # angle arc
    out.append(fr.poly([(0.25 * math.cos(t), 0.25 * math.sin(t)) for t in linspace(t1, t2, 80)], "thin2"))
    out.append(fr.label((0.27, 0.27), "Δθ", 8, 0, "start", cls="sml", fill=YELLOW))
    out.append(rect(100, 520, 700, 60, "box", 10))
    out.append(txt(450, 558, "A = (Δθ/6)(r₁² + r₁r₂ + r₂²)", cls="eq", anchor="middle", size=20))
    out.append(txt(32, 44, "Proposition 26 — the area of a spiral portion", cls="ttl"))
    out.append(txt(32, 72, "The region between two radii and one turn of the spiral, compared with the circular sector of radius r₂.", cls="sub"))
    save("p5-area-ratio.svg", "".join(out),
         "Area of a spiral portion compared with a circular sector",
         "A spiral arc from angle theta one to theta two with its two radii, shaded teal, inside the dashed circular sector of radius r2 shaded orange, illustrating the area formula.")


def p5_shell_ratio():
    a = 1.0
    r1, r2 = 1.0, 2.0
    t1, t2 = r1 / a, r2 / a
    fr = Frame((70, 120, 600, 500), (-2.4, 2.4), (-0.45, 2.45))
    out = []
    # annular sector outline
    inner = [(r1 * math.cos(t), r1 * math.sin(t)) for t in linspace(t1, t2, 120)]
    outer = [(r2 * math.cos(t), r2 * math.sin(t)) for t in linspace(t1, t2, 120)]
    # L region: inner arc + radial at t2 + spiral back
    spiral = [(a * t * math.cos(t), a * t * math.sin(t)) for t in linspace(t1, t2, 160)]
    Lpts = inner + [(r2 * math.cos(t2), r2 * math.sin(t2))] + list(reversed(spiral))
    out.append(fr.poly(Lpts, "fill-teal", closed=True))
    # U region: radial at t1 + outer arc + spiral back
    Upts = [(r1 * math.cos(t1), r1 * math.sin(t1)), (r2 * math.cos(t1), r2 * math.sin(t1))] + outer + list(reversed(spiral))
    out.append(fr.poly(Upts, "fill-orange", closed=True))
    # boundaries
    out.append(fr.poly(inner, "curve3"))
    out.append(fr.poly(outer, "curve3"))
    out.append(fr.poly(spiral, "curve"))
    out.append(fr.seg((r1 * math.cos(t1), r1 * math.sin(t1)), (r2 * math.cos(t1), r2 * math.sin(t1)), "thin"))
    out.append(fr.seg((r1 * math.cos(t2), r1 * math.sin(t2)), (r2 * math.cos(t2), r2 * math.sin(t2)), "thin"))
    out.append(fr.dot((0, 0)))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((0.40, 1.03), "L", 0, 0, "middle", cls="lbl", fill=TEAL, size=20),
        fr.label((0.58, 1.49), "U", 0, 0, "middle", cls="lbl", fill=ORANGE, size=20),
        fr.label((r1 * math.cos(t1), r1 * math.sin(t1)), "r₁", -8, -8, "end", cls="sml"),
        fr.label((r2 * math.cos(t1), r2 * math.sin(t1)), "r₂", 8, 8, "start", cls="sml"),
        fr.label((r2 * math.cos(t2), r2 * math.sin(t2)), "r₂", 8, -6, "start", cls="sml"),
    ]
    out.append(rect(630, 110, 250, 110, "box", 12))
    out.append(txt(755, 146, "U / L", cls="eq", anchor="middle", size=18))
    out.append(txt(755, 174, "= (r₁ + 2r₂)/(2r₁ + r₂)", cls="eq", anchor="middle", size=16))
    out.append(txt(755, 202, "here = 5/4", cls="sml", anchor="middle"))
    out.append(txt(32, 44, "Proposition 28 — the spiral splits an annular sector", cls="ttl"))
    out.append(txt(32, 72, "The spiral divides the region between two circles into L (inside) and U (outside), in a ratio fixed by r₁ and r₂.", cls="sub"))
    save("p5-shell-ratio.svg", "".join(out),
         "Spiral dividing an annular sector into two regions",
         "An annular sector between radii r1 and r2 shaded teal below the spiral and orange above it, with the ratio U over L equal to r1 plus 2 r2 over 2 r1 plus r2.")


# ======================================================================
# PART 6 — On the Equilibrium of Planes, Book I
# ======================================================================

def p6_lever():
    fr = Frame((70, 100, 830, 390), (-7.5, 7.5), (-1.5, 2.7))
    out = []
    out.append(fr.seg((-7, 0), (7, 0), "thin"))
    out.append(fr.poly([(-0.7, 0), (0.7, 0), (0, -1.05)], "fill-orange", closed=True))
    out.append(fr.poly([(-0.7, 0), (0.7, 0), (0, -1.05)], "thin", closed=True))
    # weights as squares of side sqrt(W)
    for x, W, lab, col in [(-3, 2, "W₁ = 2", TEAL), (2, 3, "W₂ = 3", ORANGE)]:
        s = math.sqrt(W)
        p0 = fr.p(x - s / 2, 0)
        p1 = fr.p(x + s / 2, s)
        out.append(f'<rect x="{p0[0]:.2f}" y="{p1[1]:.2f}" width="{p1[0]-p0[0]:.2f}" height="{p0[1]-p1[1]:.2f}" fill="{col}" fill-opacity="0.72" stroke="{col}" stroke-width="1.5"/>\n')
        out.append(fr.label((x, s / 2), lab, 0, 5, "middle", cls="sml", fill=WHITE))
    out += [fr.dot((-3, 0), "pt-teal", 3.2), fr.dot((2, 0), "pt-orange", 3.2)]
    # dimensions
    out.append(fr.seg((-3, -0.35), (-3, 0.0), "thin2 dash"))
    out.append(fr.seg((2, -0.35), (2, 0.0), "thin2 dash"))
    out.append(fr.dim((-3, -0.45), (0, -0.45), 0, label="d₁ = 3"))
    out.append(fr.dim((0, -1.15), (2, -1.15), 0, label="d₂ = 2"))
    out.append(txt(450, 490, "W₁ d₁  =  W₂ d₂     2 · 3  =  3 · 2", cls="eq", anchor="middle", size=21))
    out.append(txt(32, 44, "The law of the lever", cls="ttl"))
    out.append(txt(32, 72, "Equal moments balance: the heavier weight sits at the shorter distance.", cls="sub"))
    save("p6-lever.svg", "".join(out),
         "Law of the lever with two weights",
         "A beam with a fulcrum, a weight of two at distance three on the left and a weight of three at distance two on the right, illustrating W1 d1 equals W2 d2.",
         w=900, h=520)


def p6_triangle():
    fr = Frame((80, 100, 820, 500), (-0.5, 6.5), (-0.5, 5.5))
    A, B, C = (0, 0), (6, 0), (2, 5)
    MAB = (3, 0)
    MBC = (4, 2.5)
    MCA = (1, 2.5)
    G = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    out = []
    out.append(fr.poly([A, B, C], "fill-teal", closed=True))
    out.append(fr.poly([A, B, C], "thin", closed=True))
    out.append(fr.seg(C, MAB, "curve2"))
    out.append(fr.seg(A, MBC, "thin2 dash"))
    out.append(fr.seg(B, MCA, "thin2 dash"))
    out.append(fr.dot(G, "pt-orange", 4.6))
    for P, lab, dx, dy, anc in [(A, "A", -10, 16, "end"), (B, "B", 10, 16, "start"), (C, "C", 0, -12, "middle"),
                                (MAB, "M", 8, 18, "start"), (G, "G", 10, -8, "start")]:
        out.append(fr.label(P, lab, dx, dy, anc, cls="lbl"))
    # ratio labels on median C-M
    out.append(fr.label(((C[0] + G[0]) / 2, (C[1] + G[1]) / 2), "2", 10, 0, "start", cls="eq", fill=ORANGE))
    out.append(fr.label(((G[0] + MAB[0]) / 2, (G[1] + MAB[1]) / 2), "1", 10, 0, "start", cls="eq", fill=TEAL))
    out.append(txt(450, 545, "CG : GM = 2 : 1", cls="eq", anchor="middle", size=20))
    out.append(txt(32, 44, "The centre of gravity of a triangle", cls="ttl"))
    out.append(txt(32, 72, "The three medians meet at G, and G divides each median in the ratio 2:1 from the vertex.", cls="sub"))
    save("p6-triangle.svg", "".join(out),
         "Triangle centroid at the intersection of the medians",
         "A triangle with all three medians drawn, their intersection G, and the labels showing CG to GM equals 2 to 1.",
         w=900, h=580)


def p6_trapezoid():
    fr = Frame((100, 100, 800, 500), (-3.6, 3.6), (-0.5, 4.5))
    B, b, hgt = 6.0, 3.0, 4.0
    A, Bp, Cp, D = (-B / 2, 0), (B / 2, 0), (b / 2, hgt), (-b / 2, hgt)
    MB, Mb = (0, 0), (0, hgt)
    yG = hgt * (B + 2 * b) / (3 * (B + b))
    G = (0, yG)
    out = []
    out.append(fr.poly([A, Bp, Cp, D], "fill-teal", closed=True))
    out.append(fr.poly([A, Bp, Cp, D], "thin", closed=True))
    out.append(fr.seg(MB, Mb, "curve2"))
    out.append(fr.dot(MB, "pt", 3.4))
    out.append(fr.dot(Mb, "pt", 3.4))
    out.append(fr.dot(G, "pt-orange", 4.6))
    out += [
        fr.label(A, "A", -10, 18, "end", cls="sml"),
        fr.label(Bp, "B", 10, 18, "start", cls="sml"),
        fr.label(Cp, "C", 10, -8, "start", cls="sml"),
        fr.label(D, "D", -10, -8, "end", cls="sml"),
        fr.label(MB, "M_B", 8, 18, "start", cls="sml"),
        fr.label(Mb, "M_b", 8, -8, "start", cls="sml"),
        fr.label(G, "G", 10, 5, "start", cls="lbl", fill=ORANGE),
        fr.label((0, hgt / 2), "5", 10, -14, "start", cls="eq", fill=ORANGE),
        fr.label((0, yG / 2), "4", 10, 5, "start", cls="eq", fill=TEAL),
    ]
    out.append(fr.dim((-B / 2, -0.25), (B / 2, -0.25), 0, label="B = 6"))
    out.append(fr.dim((-b / 2, hgt + 0.3), (b / 2, hgt + 0.3), 0, label="b = 3"))
    out.append(txt(450, 545, "M_bG : GM_B = 5 : 4", cls="eq", anchor="middle", size=20))
    out.append(txt(32, 44, "The centre of gravity of a trapezium", cls="ttl"))
    out.append(txt(32, 72, "The centroid lies on the midline joining the parallel sides, closer to the larger base.", cls="sub"))
    save("p6-trapezoid.svg", "".join(out),
         "Trapezium centroid on the midline",
         "A trapezium with parallel sides 6 and 3 and height 4, its midline, and the centroid dividing the midline in the ratio 5 to 4.",
         w=900, h=580)


def p6_parabola_centroid():
    fr = Frame((120, 100, 780, 500), (-1.3, 1.3), (-0.2, 1.2))
    out = []
    arc = [(x, 1 - x * x) for x in linspace(-1, 1, 320)]
    out.append(fr.poly(arc + [(1, 0), (-1, 0)], "fill-teal", closed=True))
    out.append(fr.poly(arc, "curve"))
    out.append(fr.seg((-1, 0), (1, 0), "thin"))
    out.append(fr.seg((0, 0), (0, 1), "thin2 dash"))
    V, M, G = (0, 1), (0, 0), (0, 0.4)
    out += [fr.dot(V, "pt", 3.4), fr.dot(M, "pt", 3.4), fr.dot(G, "pt-orange", 4.6)]
    out += [
        fr.label(V, "V", 10, -8, "start", cls="lbl"),
        fr.label(M, "M", 10, 18, "start", cls="sml"),
        fr.label(G, "G", 10, 5, "start", cls="lbl", fill=ORANGE),
        fr.label((0.08, 0.72), "VG = 3/5", 0, 0, "start", cls="eq", fill=ORANGE),
        fr.label((0.08, 0.2), "GM = 2/5", 0, 0, "start", cls="eq", fill=TEAL),
    ]
    out.append(txt(450, 545, "VG : GM = 3 : 2", cls="eq", anchor="middle", size=20))
    out.append(txt(32, 44, "The centre of gravity of a parabolic segment", cls="ttl"))
    out.append(txt(32, 72, "The centroid lies on the diameter, three fifths of the way from the vertex to the base.", cls="sub"))
    save("p6-parabola-centroid.svg", "".join(out),
         "Centroid of a parabolic segment",
         "The segment bounded by y equals one minus x squared and the x-axis, its diameter VM, and the centroid G with VG to GM equal to 3 to 2.",
         w=900, h=580)


def p6_subtraction():
    fr = Frame((70, 120, 560, 500), (-0.4, 6.4), (-0.4, 4.4))
    out = []
    # remainder L-shape
    L = [(0, 0), (4, 0), (4, 2), (6, 2), (6, 4), (0, 4)]
    out.append(fr.poly(L, "fill-teal", closed=True))
    out.append(fr.poly(L, "thin", closed=True))
    # removed square
    out.append(fr.poly([(4, 0), (6, 0), (6, 2), (4, 2)], "fill-red", closed=True))
    out.append(fr.poly([(4, 0), (6, 0), (6, 2), (4, 2)], "thin", closed=True))
    # whole rectangle outline on top
    out.append(fr.poly([(0, 0), (6, 0), (6, 4), (0, 4)], "thin2 dash", closed=True))
    G, P, R = (3, 2), (5, 1), (2.6, 2.2)
    out.append(fr.seg((5, 1), (2.6, 2.2), "thin2 dash"))
    out += [fr.dot(G, "pt", 4.2), fr.dot(P, "pt-orange", 4.2), fr.dot(R, "pt-teal", 4.6)]
    out += [
        fr.label(G, "G", 10, -8, "start", cls="lbl"),
        fr.label(P, "P", 10, -8, "start", cls="lbl", fill=ORANGE),
        fr.label(R, "R", 10, 12, "start", cls="lbl", fill=TEAL),
        fr.label((3.0, 3.1), "whole: W = 24", 0, 0, "middle", cls="sml"),
        fr.label((5.0, 0.55), "removed: w = 4", 0, 0, "middle", cls="sml", fill=RED),
    ]
    out.append(rect(600, 100, 270, 100, "box", 12))
    out.append(txt(735, 134, "GR / GP", cls="eq", anchor="middle", size=18))
    out.append(txt(735, 162, "= w / (W − w)", cls="eq", anchor="middle", size=16))
    out.append(txt(735, 188, "= 4/20 = 1/5", cls="sml", anchor="middle"))
    out.append(txt(32, 44, "Proposition I.8 — removing a part", cls="ttl"))
    out.append(txt(32, 72, "If a part is removed, the remainder's centre lies on the line of the two centres, beyond the whole's centre.", cls="sub"))
    save("p6-subtraction.svg", "".join(out),
         "Centroid after removing a part",
         "An L-shaped remainder of a rectangle with the removed square shaded, showing the centroid R on the line through the whole centroid G and the removed part's centroid P.",
         w=900, h=560)


# ======================================================================
# PART 7 — Book II, parabolic centroids
# ======================================================================

def p7_polygon():
    fr = Frame((120, 100, 780, 520), (-1.22, 1.22), (-0.14, 1.16))
    out = []
    xs = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
    chain = [(x, 1 - x * x) for x in xs]
    poly = [(-1, 0), (1, 0)] + list(reversed(chain))
    out.append(fr.poly(poly, "fill-teal", closed=True))
    out.append(fr.poly(chain, "curve"))
    out.append(fr.seg((-1, 0), (1, 0), "thin"))
    out.append(fr.seg((0, 0), (0, 1), "thin2 dash"))
    # horizontal chords
    for x, z in [(0.75, 7 / 16), (0.5, 3 / 4), (0.25, 15 / 16)]:
        out.append(fr.seg((-x, z), (x, z), "thin2"))
        out.append(fr.dot((0, z), "pt", 3.2))
    # interval labels on diameter
    levels = [0, 7 / 16, 3 / 4, 15 / 16, 1]
    labels = ["7", "5", "3", "1"]
    for i in range(4):
        zc = (levels[i] + levels[i + 1]) / 2
        out.append(fr.label((0, zc), labels[i], 12, 5, "start", cls="eq", fill=YELLOW))
    # annotate odd ratios
    out.append(txt(640, 130, "diameter intervals", cls="sml", anchor="middle"))
    out.append(txt(640, 154, "7 : 5 : 3 : 1", cls="eq", anchor="middle", size=18))
    out.append(txt(640, 180, "from base to vertex", cls="sml", anchor="middle", fill=MUTED))
    out.append(txt(32, 44, "The inscribed polygon ladder", cls="ttl"))
    out.append(txt(32, 72, "Chords parallel to the base are bisected by the diameter; the successive diameter intervals are in odd-number ratios.", cls="sub"))
    save("p7-polygon.svg", "".join(out),
         "Inscribed polygon with odd-number diameter intervals",
         "A parabolic segment with an inscribed polygon whose vertices lie on the parabola, horizontal chords, and diameter intervals in the ratios 7 to 5 to 3 to 1.")


def polygon_centroid(pts):
    A = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        cr = x0 * y1 - x1 * y0
        A += cr
        cx += (x0 + x1) * cr
        cy += (y0 + y1) * cr
    A *= 0.5
    return (cx / (6 * A), cy / (6 * A))


def p7_centroid_limit():
    fr = Frame((120, 100, 780, 520), (-1.22, 1.22), (-0.14, 1.16))
    out = []
    # segment fill first
    arc = [(x, 1 - x * x) for x in linspace(-1, 1, 300)]
    out.append(fr.poly(arc + [(1, 0), (-1, 0)], "fill-teal", closed=True))
    gens = [
        ([-1, 0, 1], ORANGE, "curve2"),
        ([-1, -0.5, 0, 0.5, 1], BLUE, "curve3"),
        ([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1], TEAL, "curve"),
    ]
    Gs = []
    for xs, col, cls in gens:
        chain = [(x, 1 - x * x) for x in xs]
        poly = [(-1, 0), (1, 0)] + list(reversed(chain))
        out.append(fr.poly(chain, cls))
        G = polygon_centroid(poly)
        Gs.append((G, col))
    out.append(fr.seg((-1, 0), (1, 0), "thin"))
    out.append(fr.seg((0, 0), (0, 1), "thin2 dash"))
    Gseg = (0, 0.4)
    out.append(f'<circle cx="{fr.p(0,0.4)[0]:.1f}" cy="{fr.p(0,0.4)[1]:.1f}" r="5" fill="{YELLOW}" stroke="{BG}" stroke-width="1.2"/>\n')
    out.append(fr.label(Gseg, "G (segment)", 12, -8, "start", cls="lbl", fill=YELLOW))
    offs = [(-12, 12, "end"), (12, 12, "start"), (-12, -8, "end")]
    for (G, col), n, (dx, dy, anc) in zip(Gs, [0, 1, 2], offs):
        out.append(fr.dot(G, "pt", 4.0))
        out.append(fr.label(G, f"G{n}", dx, dy, anc, cls="sml", fill=col))
    # approach arrow
    out.append(fr.seg((0.0, Gs[0][0][1] + 0.02), (0.0, Gseg[1] - 0.03), "thin2", "arrow"))
    out.append(txt(32, 44, "Centres of gravity climb toward the curve's centre", cls="ttl"))
    out.append(txt(32, 72, "Every inscribed polygon's centroid lies on the diameter, below G; the polygons approach G as the construction refines.", cls="sub"))
    save("p7-centroid-limit.svg", "".join(out),
         "Polygon centroids approaching the segment centroid",
         "A parabolic segment with three generations of inscribed polygons and their centroids G0, G1, G2 on the diameter, approaching the segment centroid G at two fifths of the height.")


def p7_portion():
    fr = Frame((90, 120, 600, 520), (-2.4, 2.4), (-0.4, 4.4))
    out = []
    # region between y=1 and y=4 around the parabola y=x^2
    lower = [(x, x * x) for x in linspace(1, 2, 120)]
    upper = [(x, x * x) for x in linspace(-2, -1, 120)]
    region = [(-1, 1), (1, 1)] + lower + [(2, 4), (-2, 4)] + upper
    out.append(fr.poly(region, "fill-teal", closed=True))
    out.append(fr.poly([(x, x * x) for x in linspace(-2.35, 2.35, 400)], "curve"))
    out.append(fr.seg((-2.4, 1), (2.4, 1), "thin2"))
    out.append(fr.seg((-2.4, 4), (2.4, 4), "thin2"))
    out.append(fr.seg((0, 0), (0, 4.2), "thin2 dash"))
    Ms, ML = (0, 1), (0, 4)
    P, Q = (0, 2.2), (0, 2.8)
    # exact G: PG/GQ = 16/5, with P at 2.2, Q at 2.8
    ratio = 16 / 5
    PG = ratio / (ratio + 1) * 0.6
    G = (0, 2.2 + PG)
    out += [fr.dot(Ms, "pt", 3.4), fr.dot(ML, "pt", 3.4), fr.dot(P, "pt", 3.4), fr.dot(Q, "pt", 3.4), fr.dot(G, "pt-orange", 4.6)]
    out += [
        fr.label(Ms, "M_s", 8, 16, "start", cls="sml"),
        fr.label(ML, "M_L", 8, -8, "start", cls="sml"),
        fr.label(P, "P", 12, 4, "start", cls="sml", fill=YELLOW),
        fr.label(Q, "Q", 12, -6, "start", cls="sml", fill=YELLOW),
        fr.label(G, "G", -12, 6, "end", cls="lbl", fill=ORANGE),
        fr.label((0.35, 2.5), "middle fifth", 0, 0, "start", cls="sml"),
        fr.label((-0.8, 1.12), "s = 2", 0, 0, "middle", cls="sml"),
        fr.label((-1.45, 4.12), "L = 4", 0, 0, "middle", cls="sml"),
    ]
    out.append(rect(630, 120, 250, 100, "box", 12))
    out.append(txt(755, 154, "PG / GQ = 16/5", cls="eq", anchor="middle", size=18))
    out.append(txt(755, 186, "= L²(2s+L) / s²(2L+s)", cls="sml", anchor="middle"))
    out.append(txt(32, 44, "The portion between two parallel chords", cls="ttl"))
    out.append(txt(32, 72, "The centre of gravity lies inside the middle fifth of the diameter, in a ratio fixed by the two chord lengths.", cls="sub"))
    save("p7-portion.svg", "".join(out),
         "Centroid of a parabolic portion between parallel chords",
         "A parabolic region cut between the chords y equals 1 and y equals 4, with the diameter, the middle fifth between P and Q, and the centroid G dividing it in the ratio 16 to 5.")


# ======================================================================
# PART 8 — On Conoids and Spheroids
# ======================================================================

def p8_ellipse():
    fr = Frame((80, 100, 600, 500), (-2.35, 2.35), (-2.35, 2.35))
    out = []
    a, b = 2.0, 1.2
    out.append(fr.poly([(a * math.cos(t), a * math.sin(t)) for t in linspace(0, 2 * math.pi, 400)], "thin2 dash"))
    ell = [(a * math.cos(t), b * math.sin(t)) for t in linspace(0, 2 * math.pi, 400)]
    out.append(fr.poly(ell, "fill-teal", closed=True))
    out.append(fr.poly(ell, "curve"))
    out.append(fr.seg((-2.25, 0), (2.25, 0), "axis"))
    out.append(fr.seg((0, -2.25), (0, 2.25), "axis"))
    out.append(fr.seg((0, 0), (a, 0), "thin"))
    out.append(fr.seg((0, 0), (0, b), "thin"))
    out.append(fr.dot((0, 0)))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((a / 2, 0), "a", 0, 18, "middle", cls="sml", fill=YELLOW),
        fr.label((0, b / 2), "b", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((1.25, 0.45), "ellipse", 0, 0, "middle", cls="sml", fill=TEAL),
        fr.label((-1.45, 1.55), "auxiliary circle", 0, 0, "middle", cls="sml"),
    ]
    out.append(rect(630, 110, 250, 150, "box", 12))
    out.append(txt(755, 146, "A_ellipse / A_circle", cls="eq", anchor="middle", size=17))
    out.append(txt(755, 174, "= b / a", cls="eq", anchor="middle", size=18))
    out.append(txt(755, 206, "A_ellipse = πab", cls="eq", anchor="middle", size=19))
    out.append(txt(755, 234, "a = semimajor, b = semiminor", cls="sml", anchor="middle", fill=MUTED))
    out.append(txt(32, 44, "The ellipse and its auxiliary circle", cls="ttl"))
    out.append(txt(32, 72, "Squashing the circle vertically by b/a scales every area by the same factor.", cls="sub"))
    save("p8-ellipse.svg", "".join(out),
         "Ellipse and auxiliary circle",
         "An ellipse with semimajor axis a and semiminor axis b inside its auxiliary circle of radius a, with the area ratio b over a and area pi a b.")


def p8_paraboloid():
    fr = Frame((100, 100, 650, 520), (-2.5, 2.5), (-0.4, 4.5))
    out = []
    R, H = 2.0, 4.0
    par = [(x, x * x) for x in linspace(-R, R, 300)]
    region = [(-R, H), (R, H)] + list(reversed(par))
    out.append(fr.poly(region, "fill-teal", closed=True))
    out.append(fr.poly(par, "curve"))
    # cone
    out.append(fr.poly([(-R, H), (0, 0), (R, H)], "curve2"))
    # cutting plane and axis
    out.append(fr.seg((-2.4, H), (2.4, H), "thin"))
    out.append(fr.seg((0, -0.3), (0, 4.4), "thin2 dash"))
    out += [fr.dot((0, 0)), fr.dot((0, H), "pt", 3.4)]
    out += [
        fr.label((0, 0), "vertex", 10, 16, "start", cls="sml"),
        fr.label((0, H), "axis H", 10, -8, "start", cls="sml"),
        fr.label((R, H), "R", 10, -8, "start", cls="sml", fill=YELLOW),
        fr.label((0.7, 1.6), "paraboloid", 0, 0, "start", cls="sml", fill=TEAL),
        fr.label((1.15, 2.8), "comparison cone", 0, 0, "start", cls="sml", fill=ORANGE),
    ]
    out.append(txt(450, 560, "V = (1/2) B H = (3/2) V(cone)", cls="eq", anchor="middle", size=21))
    out.append(txt(32, 44, "A paraboloid segment and its comparison cone", cls="ttl"))
    out.append(txt(32, 72, "The paraboloid z = r² cut at height H has half the volume of the cylinder on the same base.", cls="sub"))
    save("p8-paraboloid.svg", "".join(out),
         "Paraboloid segment compared with a cone",
         "The cross-section z equals r squared cut at height H, with the comparison cone drawn dashed and the segment shaded, illustrating volume equals half base times height.",
         w=900, h=600)


def p8_hyperboloid():
    fr = Frame((100, 100, 650, 520), (-3.4, 3.4), (0.0, 3.35))
    out = []
    a, h = 1.0, 2.0
    zs = [a + (h) * i / 200 for i in range(201)]
    right = [(math.sqrt(z * z - a * a), z) for z in zs]
    left = [(-math.sqrt(z * z - a * a), z) for z in zs]
    region = left + list(reversed(right))
    out.append(fr.poly(region, "fill-teal", closed=True))
    out.append(fr.poly(right, "curve"))
    out.append(fr.poly(left, "curve"))
    # asymptotes
    out.append(fr.seg((-3.3, 3.3), (3.3, -3.3), "thin2 dash"))
    out.append(fr.seg((3.3, 3.3), (-3.3, -3.3), "thin2 dash"))
    # cone with same base and axis
    Rb = math.sqrt((a + h) ** 2 - a * a)
    out.append(fr.seg((0, a), (Rb, a + h), "curve2"))
    out.append(fr.seg((0, a), (-Rb, a + h), "curve2"))
    # cutting planes
    out.append(fr.seg((-3.3, a), (3.3, a), "thin2"))
    out.append(fr.seg((-3.3, a + h), (3.3, a + h), "thin"))
    out.append(fr.seg((0, 0), (0, 3.3), "thin2 dash"))
    out += [fr.dot((0, 0)), fr.dot((0, a), "pt", 3.4), fr.dot((0, a + h), "pt", 3.4)]
    out += [
        fr.label((0, 0), "C", 10, 16, "start", cls="sml"),
        fr.label((0, a), "A", 10, 16, "start", cls="sml"),
        fr.label((0, a + h), "D", 10, -8, "start", cls="sml"),
        fr.label((0, a / 2), "a", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((0, a + h / 2), "h", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((Rb, a + h), "base", 10, -8, "start", cls="sml"),
        fr.label((1.4, 1.75), "hyperboloid", 0, 0, "start", cls="sml", fill=TEAL),
        fr.label((2.1, 2.4), "cone", 0, 0, "start", cls="sml", fill=ORANGE),
    ]
    out.append(txt(450, 560, "V(segment) / V(cone) = (h + 3a) / (h + 2a)", cls="eq", anchor="middle", size=20))
    out.append(txt(32, 44, "A hyperboloid segment", cls="ttl"))
    out.append(txt(32, 72, "Unlike the paraboloid, the ratio to the comparison cone depends on the segment's size relative to a.", cls="sub"))
    save("p8-hyperboloid.svg", "".join(out),
         "Hyperboloid segment and comparison cone",
         "The cross-section of a hyperboloid of revolution from vertex A to cutting plane D, with center C, axial semidiameter a, height h, asymptotes dashed, and the comparison cone in orange.",
         w=900, h=600)


def p8_spheroid():
    w, h = 900, 520
    out = []
    a, b = 2.0, 1.5
    # left cap
    fr = Frame((60, 110, 430, 470), (-b - 0.3, b + 0.3), (-a - 0.3, a + 0.3))
    hcap = 1.2
    zc = a - hcap
    xb = b * math.sqrt(1 - (zc / a) ** 2)
    phi = math.asin(zc / a)
    arc = [(b * math.cos(t), a * math.sin(t)) for t in linspace(phi, math.pi - phi, 160)]
    cap = [(xb, zc)] + arc + [(-xb, zc)]
    out.append(fr.poly(cap, "fill-teal", closed=True))
    ell = [(b * math.cos(t), a * math.sin(t)) for t in linspace(0, 2 * math.pi, 400)]
    out.append(fr.poly(ell, "curve"))
    out.append(fr.seg((-xb, zc), (xb, zc), "thin"))
    out.append(fr.seg((0, zc), (0, a), "thin2 dash"))
    out.append(fr.seg((0, zc), (xb, zc), "thin2 dash"))
    out.append(fr.dot((0, 0), "pt", 3.4))
    out += [
        fr.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr.label((0, (zc + a) / 2), "h", 10, 0, "start", cls="sml", fill=YELLOW),
        fr.label((0, a), "pole", 10, -6, "start", cls="sml"),
        fr.label((xb / 2, zc), "base", 0, 20, "middle", cls="sml"),
    ]
    out.append(txt(245, 90, "cap, h ≤ a", cls="lbl", anchor="middle", fill=TEAL))
    out.append(txt(245, 505, "V = (Bh/3)(3a−h)/(2a−h)", cls="sml", anchor="middle", fill=YELLOW))
    # right half
    fr2 = Frame((470, 110, 840, 470), (-b - 0.3, b + 0.3), (-a - 0.3, a + 0.3))
    ell2 = [(b * math.cos(t), a * math.sin(t)) for t in linspace(0, 2 * math.pi, 400)]
    out.append(fr2.poly(ell2, "curve"))
    half = [(b * math.cos(t), a * math.sin(t)) for t in linspace(0, math.pi, 200)] + [(-b, 0)]
    out.append(fr2.poly(half, "fill-teal", closed=True))
    out.append(fr2.poly([(b, 0), (0, a), (-b, 0)], "curve2"))
    out.append(fr2.seg((-b, 0), (b, 0), "thin"))
    out += [
        fr2.label((0, 0), "O", 8, 16, "start", cls="sml"),
        fr2.label((0, a), "pole", 10, -6, "start", cls="sml"),
        fr2.label((0, a / 2), "a", 10, 0, "start", cls="sml", fill=YELLOW),
        fr2.label((b / 2, 0), "b", 0, 18, "middle", cls="sml", fill=YELLOW),
    ]
    out.append(txt(655, 90, "half-spheroid", cls="lbl", anchor="middle", fill=TEAL))
    out.append(txt(655, 505, "V = 2 V(cone)", cls="sml", anchor="middle", fill=YELLOW))
    out.append(txt(32, 44, "Spheroidal caps and the half-spheroid", cls="ttl"))
    out.append(txt(32, 72, "A cap's volume is a fixed multiple of its comparison cone; at the centre cut the multiple is exactly 2.", cls="sub"))
    save("p8-spheroid.svg", "".join(out),
         "Spheroidal cap and half-spheroid",
         "Left: an ellipse with a cap of height h shaded and its base chord. Right: half an ellipse compared with a cone from the centre to the equator.",
         w, h)


# ======================================================================
# PART 9 — the reader's guide
# ======================================================================

def node(x, y, label, sub, color=TEAL, dashed=False, w=170, h=66):
    stroke = color
    dash = ' stroke-dasharray="6 5"' if dashed else ""
    out = f'<rect x="{x-w/2:.1f}" y="{y-h/2:.1f}" width="{w}" height="{h}" rx="10" fill="{PANEL}" stroke="{stroke}" stroke-width="1.6"{dash}/>\n'
    out += txt(x, y - 4, label, cls="lbl", anchor="middle", size=16, fill=WHITE)
    out += txt(x, y + 18, sub, cls="sml", anchor="middle")
    return out


def p9_dependency_map():
    w, h = 1000, 640
    out = []
    # nodes
    out.append(node(150, 120, "Equilibrium I", "lever + centroids"))
    out.append(node(450, 120, "Quadrature", "parabolic area 4T/3"))
    out.append(node(790, 120, "Equilibrium II", "parabolic centroids"))
    out.append(node(150, 330, "On Spirals", "tangents + spiral areas"))
    out.append(node(450, 330, "Measurement", "of a Circle", GREEN, True))
    out.append(node(790, 330, "Sphere & Cylinder", "surfaces + volumes"))
    out.append(node(620, 500, "Conoids & Spheroids", "curved-solid volumes"))
    # edges
    def edge(a, b, label, lx, ly, dashed=False, color=MUTED):
        x1, y1 = a
        x2, y2 = b
        cls = "thin2"
        dash = " stroke-dasharray='6 5'" if dashed else ""
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.4" marker-end="url(#arrow)"{dash}/>\n')
        out.append(txt(lx, ly, label, cls="sml", anchor="middle", fill=MUTED))
    edge((240, 120), (360, 120), "lever + centroid", 300, 108)
    edge((540, 120), (700, 120), "segment area", 620, 108)
    edge((505, 155), (735, 295), "exhaustion template", 650, 225)
    edge((200, 295), (405, 155), "finite sums", 280, 215)
    edge((240, 330), (360, 330), "circumference", 300, 318)
    edge((540, 330), (700, 330), "circle area", 620, 318)
    edge((750, 360), (660, 465), "volume methods", 745, 425)
    # legend
    out.append(rect(60, 560, 420, 60, "box", 10))
    out.append(line(78, 584, 118, 584, "thin2"))
    out.append(txt(130, 589, "a treatise with its own post", cls="sml"))
    out.append(line(290, 584, 330, 584, "thin2 dash"))
    out.append(txt(342, 589, "related work", cls="sml"))
    out.append(txt(500, 44, "How the works feed one another", cls="ttl", anchor="middle"))
    out.append(txt(500, 72, "Conceptual dependencies reconstructed from the arguments, not a chronology.", cls="sub", anchor="middle"))
    save("p9-dependency-map.svg", "".join(out),
         "Dependency map of the Archimedean treatises",
         "A graph connecting Equilibrium of Planes I, Quadrature of the Parabola, Equilibrium of Planes II, On Spirals, Measurement of a Circle, On the Sphere and Cylinder, and On Conoids and Spheroids, with labelled dependency arrows.", w, h)


def p9_three_tools():
    w, h = 900, 500
    out = []
    # triangle of tools
    G = (450, 110)
    M = (210, 400)
    E = (690, 400)
    C = (450, 300)
    out.append(line(G[0], G[1], M[0], M[1], "thin2"))
    out.append(line(G[0], G[1], E[0], E[1], "thin2"))
    out.append(line(M[0], M[1], E[0], E[1], "thin2"))
    # central result
    out.append(f'<polygon points="450,250 500,275 500,325 450,350 400,325 400,275" fill="{PANEL}" stroke="{YELLOW}" stroke-width="1.8"/>\n')
    out.append(txt(450, 292, "exact", cls="eq", anchor="middle", size=18))
    out.append(txt(450, 316, "result", cls="eq", anchor="middle", size=18))
    # cards
    out.append(node(450, 110, "Geometry", "conic sections + ratios", TEAL))
    out.append(node(210, 400, "Mechanics", "lever + centre of gravity", ORANGE))
    out.append(node(690, 400, "Exhaustion", "finite bounds + contradiction", BLUE))
    # arrows to centre
    out.append(line(450, 144, 450, 244, "thin2", "arrow"))
    out.append(line(255, 380, 410, 325, "thin2", "arrow"))
    out.append(line(645, 380, 490, 325, "thin2", "arrow"))
    out.append(txt(465, 195, "conic ratios", cls="sml", anchor="start", fill=TEAL))
    out.append(txt(300, 340, "moments", cls="sml", anchor="middle", fill=ORANGE))
    out.append(txt(610, 340, "squeeze", cls="sml", anchor="middle", fill=BLUE))
    out.append(txt(450, 44, "Three tools, one answer", cls="ttl", anchor="middle"))
    out.append(txt(450, 72, "Every result in the series is built by combining these three kinds of reasoning.", cls="sub", anchor="middle"))
    save("p9-three-tools.svg", "".join(out),
         "The three tools of Archimedean proof",
         "A triangle connecting geometry, mechanics, and exhaustion, each pointing to a central exact result.", w, h)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    p1_segment()
    p1_prop1()
    p1_prop2()
    p1_prop5()
    p1_children()
    p1_series()
    p2_auxiliary()
    p2_parallelogram()
    p2_intervals()
    p2_lever()
    p2_two_proofs()
    p3_polygons()
    p3_frustum()
    p3_zones()
    p3_squeeze()
    p4_sphere_cylinder()
    p4_cap()
    p4_sector()
    p5_spiral()
    p5_tangent()
    p5_trisection()
    p5_area_ratio()
    p5_shell_ratio()
    p6_lever()
    p6_triangle()
    p6_trapezoid()
    p6_parabola_centroid()
    p6_subtraction()
    p7_polygon()
    p7_centroid_limit()
    p7_portion()
    p8_ellipse()
    p8_paraboloid()
    p8_hyperboloid()
    p8_spheroid()
    p9_dependency_map()
    p9_three_tools()

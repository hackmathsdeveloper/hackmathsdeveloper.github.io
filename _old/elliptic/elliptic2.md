
To add two points on an elliptic curve over a field, we use the **Chord-and-Tangent method**. The curve equation is:

$$y^2 = x^3 + ax + b$$

Let $P = (x_1, y_1)$ and $Q = (x_2, y_2)$ be two distinct points on the curve. We construct a line passing through both points, find its third intersection point $R' = (x_3, y_3')$ with the curve, and reflect it across the $x$-axis to obtain $R = P + Q = (x_3, y_3)$.

---

## 1. Point Addition ($P \neq Q$)

Assuming $x_1 \neq x_2$ (if $x_1 = x_2$ and $y_1 = -y_2$, then $P + Q = \mathcal{O}$, the point at infinity):

### Step 1: Slope of the Secant Line

The slope $m$ of the line passing through $P(x_1, y_1)$ and $Q(x_2, y_2)$ is:

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

The equation of this line is given by $y = m(x - x_1) + y_1$.

### Step 2: Intersecting with the Curve

Substitute $y = m(x - x_1) + y_1$ into the curve equation $y^2 = x^3 + ax + b$:

$$(m(x - x_1) + y_1)^2 = x^3 + ax + b$$

Expanding and rearranging terms into standard cubic polynomial form:

$$x^3 - m^2 x^2 + (a - 2m^2 x_1 + 2m y_1)x + (b - m^2 x_1^2 + 2m x_1 y_1 - y_1^2) = 0$$

### Step 3: Finding $x_3$ and $y_3$

By Vieta’s formulas, the sum of the roots of a monic cubic polynomial $x^3 + c_2 x^2 + c_1 x + c_0 = 0$ equals $-c_2$. Since $x_1, x_2, x_3$ are the three roots of this equation:

$$x_1 + x_2 + x_3 = m^2 \implies x_3 = m^2 - x_1 - x_2$$

The $y$-coordinate on the secant line is $y_3' = m(x_3 - x_1) + y_1$. Reflecting across the $x$-axis gives $y_3 = -y_3'$:

$$y_3 = m(x_1 - x_3) - y_1$$

---

## 2. Point Doubling ($P = Q$)

When doubling a point $P(x_1, y_1)$ (assuming $y_1 \neq 0$), the line is the **tangent line** to the curve at $P$.

### Step 1: Slope of the Tangent Line

Using implicit differentiation on $y^2 = x^3 + ax + b$:

$$2y \frac{dy}{dx} = 3x^2 + a \implies m = \frac{dy}{dx} = \frac{3x_1^2 + a}{2y_1}$$

### Step 2: Finding $x_3$ and $y_3$

Using the same intersection logic, the root $x_1$ now has a multiplicity of 2 (since the line is tangent at $P$). Thus:

$$x_1 + x_1 + x_3 = m^2 \implies x_3 = m^2 - 2x_1$$

Reflecting the $y$-coordinate across the $x$-axis gives:

$$y_3 = m(x_1 - x_3) - y_1$$

---

## Summary Table

| Operation | Slope ($m$) | Output Point $(x_3, y_3)$ |
| --- | --- | --- |
| **Point Addition** ($P \neq Q$) | $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ | $x_3 = m^2 - x_1 - x_2$<br>

<br>$y_3 = m(x_1 - x_3) - y_1$ |
| **Point Doubling** ($P = Q$) | $m = \dfrac{3x_1^2 + a}{2y_1}$ | $x_3 = m^2 - 2x_1$<br>

<br>$y_3 = m(x_1 - x_3) - y_1$ |

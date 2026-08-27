
# Double Pendulum — Lagrangian Analysis

## 1. Setup & Coordinates

We use two standard simplifications: **equal masses** ($m_1 = m_2 = m$) and **equal lengths** ($L_1 = L_2 = L$).

| | Position |
|---|---|
| Mass 1 | $x_1 = L\sin\theta_1,\quad y_1 = -L\cos\theta_1$ |
| Mass 2 | $x_2 = L\sin\theta_1 + L\sin\theta_2,\quad y_2 = -L\cos\theta_1 - L\cos\theta_2$ |

---

## 2. Energies

**Kinetic Energy** $T = T_1 + T_2$:

$$T = \frac{1}{2}mL^2\Big[2\dot\theta_1^2 + \dot\theta_2^2 + 2\dot\theta_1\dot\theta_2\cos(\theta_1 - \theta_2)\Big]$$

**Potential Energy** $V = V_1 + V_2$ (taking pivot as reference):

$$V = -mgL\big(2\cos\theta_1 + \cos\theta_2\big)$$

**Lagrangian** $\mathcal{L} = T - V$:

$$\boxed{\mathcal{L} = \frac{1}{2}mL^2\Big[2\dot\theta_1^2 + \dot\theta_2^2 + 2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2)\Big] + mgL\big(2\cos\theta_1 + \cos\theta_2\big)}$$

---

## 3. Full Nonlinear Equations of Motion

Applying the Euler–Lagrange equations $\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot\theta_i} - \frac{\partial \mathcal{L}}{\partial \theta_i} = 0$:

$$2\ddot\theta_1 + \ddot\theta_2\cos(\theta_1-\theta_2) + \dot\theta_2^2\sin(\theta_1-\theta_2) + \frac{2g}{L}\sin\theta_1 = 0$$

$$\ddot\theta_1\cos(\theta_1-\theta_2) + \ddot\theta_2 - \dot\theta_1^2\sin(\theta_1-\theta_2) + \frac{g}{L}\sin\theta_2 = 0$$

> These coupled nonlinear ODEs exhibit **chaotic behavior** for large angles.

---

## 4. Small-Angle Linearization

We now apply the standard simplification: $\theta_1, \theta_2 \ll 1$, so

$$\sin\theta \approx \theta,\quad \cos(\theta_1-\theta_2)\approx 1,\quad \dot\theta^2\text{ terms} \approx 0$$

Letting $\omega_0^2 = g/L$, the system becomes:

$$2\ddot\theta_1 + \ddot\theta_2 + 2\omega_0^2\,\theta_1 = 0 \tag{I}$$
$$\ddot\theta_1 + \ddot\theta_2 + \omega_0^2\,\theta_2 = 0 \tag{II}$$

---

## 5. Normal Modes

Assume $\theta_i(t) = A_i\,e^{i\omega t}$. Substituting:

$$\begin{pmatrix} 2(\omega_0^2 - \omega^2) & -\omega^2 \\ -\omega^2 & \omega_0^2 - \omega^2 \end{pmatrix} \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = 0$$

Setting the determinant to zero:

$$2(\omega_0^2 - \omega^2)^2 - \omega^4 = 0 \;\;\Longrightarrow\;\; \omega^4 - 4\omega_0^2\omega^2 + 2\omega_0^4 = 0$$

Solving the quadratic in $\omega^2$:

$$\boxed{\omega_1^2 = (2-\sqrt{2})\,\omega_0^2, \qquad \omega_2^2 = (2+\sqrt{2})\,\omega_0^2}$$

**Amplitude ratios** $A_1/A_2 = (\omega_0^2 - \omega^2)/\omega^2$:

| Mode | Frequency | Ratio $A_1/A_2$ | Physical picture |
|------|-----------|-----------------|------------------|
| 1 (slow) | $\omega_1 = \omega_0\sqrt{2-\sqrt{2}} \approx 0.765\,\omega_0$ | $+1/\sqrt{2}$ | Both swing **in phase** |
| 2 (fast) | $\omega_2 = \omega_0\sqrt{2+\sqrt{2}} \approx 1.848\,\omega_0$ | $-1/\sqrt{2}$ | Swing **out of phase** |

---

## 6. Solution with Standard Initial Conditions

Take the classic initial condition: both pendulums displaced equally and released from rest:

$$\theta_1(0) = \theta_0,\quad \theta_2(0) = \theta_0,\quad \dot\theta_1(0) = 0,\quad \dot\theta_2(0) = 0$$

The general solution is a superposition of both modes. Applying the ICs:

$$\boxed{\theta_1(t) = \frac{\theta_0}{4}\Big[(2+\sqrt{2})\cos\omega_1 t + (2-\sqrt{2})\cos\omega_2 t\Big]}$$

$$\boxed{\theta_2(t) = \frac{\theta_0}{2}\Big[(\sqrt{2}+1)\cos\omega_1 t - (\sqrt{2}-1)\cos\omega_2 t\Big]}$$

### Physical interpretation — beats

The two frequencies are **incommensurate** ($\omega_2/\omega_1 \approx 2.414$), so the motion is quasi-periodic. The energy sloshes back and forth between the two pendulums in a **beat** pattern with envelope frequency:

$$\omega_{\text{beat}} = \frac{\omega_2 - \omega_1}{2} \approx 0.541\,\omega_0$$

> At certain times, mass 1 nearly stops while mass 2 swings wildly, then the roles reverse — a hallmark of weakly coupled oscillator dynamics.

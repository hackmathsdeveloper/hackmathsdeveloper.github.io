
To solve the double pendulum using the **Lagrange method**, we'll go step-by-step.  
We’ll use **standard simplifying assumptions**:

- Two point masses \( m_1, m_2 \)
- Massless rods of lengths \( l_1, l_2 \)
- Motion in a vertical plane
- No friction at pivots
- Gravity \( g \) acts downward

---

## 1. Choose Generalized Coordinates
Since it’s a 2-DOF system, we use:

\[
\theta_1, \theta_2
\]

where:
- \( \theta_1 \): angle of rod 1 from vertical
- \( \theta_2 \): angle of rod 2 from vertical

---

## 2. Positions of Masses

**Mass 1:**
\[
x_1 = l_1 \sin\theta_1, \quad y_1 = -l_1 \cos\theta_1
\]

**Mass 2:**
\[
x_2 = l_1 \sin\theta_1 + l_2 \sin\theta_2
\]
\[
y_2 = -l_1 \cos\theta_1 - l_2 \cos\theta_2
\]

---

## 3. Velocities (squared)

**For mass 1:**
\[
\dot{x}_1^2 + \dot{y}_1^2 = l_1^2 \dot{\theta}_1^2
\]

**For mass 2:**
\[
\dot{x}_2^2 + \dot{y}_2^2 = l_1^2 \dot{\theta}_1^2 + l_2^2 \dot{\theta}_2^2 + 2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)
\]

---

## 4. Kinetic Energy \( T \)

\[
T = \frac12 m_1 l_1^2 \dot{\theta}_1^2 + \frac12 m_2 \left[ l_1^2 \dot{\theta}_1^2 + l_2^2 \dot{\theta}_2^2 + 2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2) \right]
\]

---

## 5. Potential Energy \( V \) (zero at pivot)

\[
V = -m_1 g l_1 \cos\theta_1 - m_2 g (l_1 \cos\theta_1 + l_2 \cos\theta_2)
\]

---

## 6. Lagrangian \( L = T - V \)

\[
L = \frac12 (m_1 + m_2) l_1^2 \dot{\theta}_1^2 + \frac12 m_2 l_2^2 \dot{\theta}_2^2 + m_2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)
\]
\[
+ (m_1 + m_2) g l_1 \cos\theta_1 + m_2 g l_2 \cos\theta_2
\]

---

## 7. Euler–Lagrange Equations

For each coordinate \( q_i \):
\[
\frac{d}{dt} \frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
\]

---

### For \( \theta_1 \):

\[
\frac{\partial L}{\partial \dot{\theta}_1} = (m_1 + m_2) l_1^2 \dot{\theta}_1 + m_2 l_1 l_2 \dot{\theta}_2 \cos(\theta_1 - \theta_2)
\]

\[
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}_1}\right) = (m_1 + m_2) l_1^2 \ddot{\theta}_1 + m_2 l_1 l_2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) - m_2 l_1 l_2 \dot{\theta}_2 (\dot{\theta}_1 - \dot{\theta}_2) \sin(\theta_1 - \theta_2)
\]

\[
\frac{\partial L}{\partial \theta_1} = -m_2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \sin(\theta_1 - \theta_2) - (m_1 + m_2) g l_1 \sin\theta_1
\]

---

**Equation for \( \theta_1 \):**
\[
(m_1 + m_2) l_1^2 \ddot{\theta}_1 + m_2 l_1 l_2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l_1 l_2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) + (m_1 + m_2) g l_1 \sin\theta_1 = 0
\]

---

### For \( \theta_2 \):

\[
\frac{\partial L}{\partial \dot{\theta}_2} = m_2 l_2^2 \dot{\theta}_2 + m_2 l_1 l_2 \dot{\theta}_1 \cos(\theta_1 - \theta_2)
\]

\[
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}_2}\right) = m_2 l_2^2 \ddot{\theta}_2 + m_2 l_1 l_2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l_1 l_2 \dot{\theta}_1 (\dot{\theta}_1 - \dot{\theta}_2) \sin(\theta_1 - \theta_2)
\]

\[
\frac{\partial L}{\partial \theta_2} = m_2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \sin(\theta_1 - \theta_2) - m_2 g l_2 \sin\theta_2
\]

---

**Equation for \( \theta_2 \):**
\[
m_2 l_2^2 \ddot{\theta}_2 + m_2 l_1 l_2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l_1 l_2 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) + m_2 g l_2 \sin\theta_2 = 0
\]

---

## 8. Simplified Form (divide common masses)

Divide first by \( l_1 \), second by \( l_2 \):

\[
(m_1 + m_2) l_1 \ddot{\theta}_1 + m_2 l_2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l_2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) + (m_1 + m_2) g \sin\theta_1 = 0
\]

\[
l_2 \ddot{\theta}_2 + l_1 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - l_1 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) + g \sin\theta_2 = 0
\]

---

## 9. Matrix Form (for numerical solution)

\[
\begin{bmatrix}
(m_1 + m_2) l_1 & m_2 l_2 \cos(\theta_1 - \theta_2) \\
l_1 \cos(\theta_1 - \theta_2) & l_2
\end{bmatrix}
\begin{bmatrix}
\ddot{\theta}_1 \\ \ddot{\theta}_2
\end{bmatrix}
=
\begin{bmatrix}
- m_2 l_2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) - (m_1 + m_2) g \sin\theta_1 \\
l_1 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) - g \sin\theta_2
\end{bmatrix}
\]

This can be inverted numerically at each time step.

---

## 10. Standard Initial Conditions (simplifying)

A common simplifying choice:

\[
\theta_1(0) = \frac{\pi}{2}, \quad \theta_2(0) = \frac{\pi}{2}
\]
\[
\dot{\theta}_1(0) = 0, \quad \dot{\theta}_2(0) = 0
\]

This means:
- Both rods start horizontal
- Released from rest

**Even simpler (symmetric):**
\[
m_1 = m_2 = m, \quad l_1 = l_2 = l
\]

Then the equations reduce to:

\[
2l \ddot{\theta}_1 + l \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + l \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) + 2g \sin\theta_1 = 0
\]
\[
l \ddot{\theta}_2 + l \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - l \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) + g \sin\theta_2 = 0
\]

These are the **standard simplified double pendulum equations**.

---

## 11. Resulting Motion
With the above initial conditions, the system shows **chaotic behavior** for most energies — sensitive dependence on initial conditions.

---

If you want, I can now:
- Give you the **numerical integration code** (Python/Runge-Kutta)
- Derive the **small-angle linearized solution**
- Show the **Hamiltonian** form

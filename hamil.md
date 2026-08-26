
To derive the **Hamiltonian form** of the double pendulum, we start from the Lagrangian we already have and perform a **Legendre transformation**. 

We'll keep the **standard simplifications**:
- \( m_1 = m_2 = m \)
- \( l_1 = l_2 = l \)

This keeps the algebra clean while still showing the full nonlinear Hamiltonian structure.

---

## 1. Generalized Momenta

The canonical momenta are:

\[
p_1 = \frac{\partial L}{\partial \dot{\theta}_1}, \quad p_2 = \frac{\partial L}{\partial \dot{\theta}_2}
\]

From our simplified Lagrangian:

\[
L = \frac12 m l^2 (2\dot{\theta}_1^2 + \dot{\theta}_2^2 + 2\dot{\theta}_1\dot{\theta}_2 \cos\Delta) + mgl(2\cos\theta_1 + \cos\theta_2)
\]
where \( \Delta = \theta_1 - \theta_2 \).

So:

\[
p_1 = m l^2 (2\dot{\theta}_1 + \dot{\theta}_2 \cos\Delta)
\]
\[
p_2 = m l^2 (\dot{\theta}_2 + \dot{\theta}_1 \cos\Delta)
\]

---

## 2. Invert to get velocities in terms of momenta

This is the tricky part. Write in matrix form:

\[
\begin{bmatrix} p_1 \\ p_2 \end{bmatrix}
= m l^2
\begin{bmatrix}
2 & \cos\Delta \\
\cos\Delta & 1
\end{bmatrix}
\begin{bmatrix} \dot{\theta}_1 \\ \dot{\theta}_2 \end{bmatrix}
\]

The determinant of the mass matrix:

\[
D = 2 - \cos^2\Delta = 1 + \sin^2\Delta
\]

Inverse of the mass matrix:

\[
\frac{1}{m l^2 D}
\begin{bmatrix}
1 & -\cos\Delta \\
-\cos\Delta & 2
\end{bmatrix}
\]

Thus:

\[
\dot{\theta}_1 = \frac{1}{m l^2 D} \left( p_1 - p_2 \cos\Delta \right)
\]
\[
\dot{\theta}_2 = \frac{1}{m l^2 D} \left( -p_1 \cos\Delta + 2 p_2 \right)
\]

---

## 3. Hamiltonian \( H = p_1\dot{\theta}_1 + p_2\dot{\theta}_2 - L \)

First, compute the kinetic part in terms of momenta:

\[
T = \frac12 
\begin{bmatrix} \dot{\theta}_1 & \dot{\theta}_2 \end{bmatrix}
\begin{bmatrix}
2 & \cos\Delta \\
\cos\Delta & 1
\end{bmatrix}
\begin{bmatrix} \dot{\theta}_1 \\ \dot{\theta}_2 \end{bmatrix} m l^2
\]

Substituting velocities gives:

\[
T = \frac{1}{2 m l^2 D} \left( p_1^2 - 2 p_1 p_2 \cos\Delta + 2 p_2^2 \right)
\]

And the potential energy:

\[
V = -mgl(2\cos\theta_1 + \cos\theta_2)
\]

Therefore:

---

## 4. Final Hamiltonian

\[
\boxed{
H(\theta_1, \theta_2, p_1, p_2) = 
\frac{ p_1^2 - 2 p_1 p_2 \cos(\theta_1 - \theta_2) + 2 p_2^2 }{2 m l^2 \left[ 1 + \sin^2(\theta_1 - \theta_2) \right] }
- mgl(2\cos\theta_1 + \cos\theta_2)
}
\]

---

## 5. Hamilton’s Equations of Motion

\[
\dot{\theta}_1 = \frac{\partial H}{\partial p_1} = \frac{p_1 - p_2 \cos\Delta}{m l^2 (1 + \sin^2\Delta)}
\]

\[
\dot{\theta}_2 = \frac{\partial H}{\partial p_2} = \frac{-p_1 \cos\Delta + 2 p_2}{m l^2 (1 + \sin^2\Delta)}
\]

\[
\dot{p}_1 = -\frac{\partial H}{\partial \theta_1} = -2mgl \sin\theta_1 - \frac{\partial}{\partial \theta_1} \left( \frac{ p_1^2 - 2 p_1 p_2 \cos\Delta + 2 p_2^2 }{2 m l^2 (1 + \sin^2\Delta)} \right)
\]

\[
\dot{p}_2 = -\frac{\partial H}{\partial \theta_2} = -mgl \sin\theta_2 - \frac{\partial}{\partial \theta_2} \left( \frac{ p_1^2 - 2 p_1 p_2 \cos\Delta + 2 p_2^2 }{2 m l^2 (1 + \sin^2\Delta)} \right)
\]

---

## 6. Expanded \( \dot{p}_1, \dot{p}_2 \) (explicit form)

Let \( K = p_1^2 - 2p_1 p_2 \cos\Delta + 2p_2^2 \) and \( S = 1 + \sin^2\Delta \).

Since \( \partial \Delta / \partial \theta_1 = 1 \), \( \partial \Delta / \partial \theta_2 = -1 \):

\[
\frac{\partial K}{\partial \theta_1} = 2 p_1 p_2 \sin\Delta
\]
\[
\frac{\partial S}{\partial \theta_1} = 2 \sin\Delta \cos\Delta = \sin 2\Delta
\]
\[
\frac{\partial K}{\partial \theta_2} = -2 p_1 p_2 \sin\Delta
\]
\[
\frac{\partial S}{\partial \theta_2} = -\sin 2\Delta
\]

So:

\[
\dot{p}_1 = -2mgl \sin\theta_1 - \frac{1}{2 m l^2} \left( \frac{2 p_1 p_2 \sin\Delta}{S} - \frac{K \sin 2\Delta}{S^2} \right)
\]

\[
\dot{p}_2 = -mgl \sin\theta_2 - \frac{1}{2 m l^2} \left( \frac{-2 p_1 p_2 \sin\Delta}{S} + \frac{K \sin 2\Delta}{S^2} \right)
\]

---

## 7. Summary: Hamiltonian System

\[
\boxed{
\begin{aligned}
\dot{\theta}_1 &= \frac{p_1 - p_2 \cos\Delta}{m l^2 (1 + \sin^2\Delta)} \\
\dot{\theta}_2 &= \frac{-p_1 \cos\Delta + 2 p_2}{m l^2 (1 + \sin^2\Delta)} \\
\dot{p}_1 &= -2mgl \sin\theta_1 - \frac{p_1 p_2 \sin\Delta}{m l^2 S} + \frac{K \sin 2\Delta}{2 m l^2 S^2} \\
\dot{p}_2 &= -mgl \sin\theta_2 + \frac{p_1 p_2 \sin\Delta}{m l^2 S} - \frac{K \sin 2\Delta}{2 m l^2 S^2}
\end{aligned}
}
\]

with  
\( \Delta = \theta_1 - \theta_2 \),  
\( S = 1 + \sin^2\Delta \),  
\( K = p_1^2 - 2p_1 p_2 \cos\Delta + 2p_2^2 \).

---

## 8. Advantages of Hamiltonian Form

- **Conserves energy** exactly (useful for numerical integrators like symplectic Euler or Verlet)
- **Phase-space structure** reveals chaos via Poincaré sections
- **Canonical transformations** (e.g., action-angle) are possible for near-integrable limits

---

## 9. Standard Initial Conditions in Hamiltonian Form

For the horizontal release:

\[
\theta_1(0) = \frac{\pi}{2}, \quad \theta_2(0) = \frac{\pi}{2}, \quad p_1(0) = 0, \quad p_2(0) = 0
\]

Then the Hamiltonian initially equals:

\[
H(0) = -mgl(0 + 0) = 0
\]

So total energy is zero (all potential relative to the pivot — the rods start horizontal).  
This is a common chaotic regime.

---

Would you like me to:
- Derive the **Poincaré sections** for this Hamiltonian?
- Show the **small-angle approximation** (normal modes)?
- Provide a **Python code** to integrate these Hamilton equations using a symplectic method?


A “wobbling plate” is most cleanly modeled as a **torque-free, axisymmetric rigid disk**: a thin circular plate whose symmetry axis is not aligned with its conserved angular-momentum vector. Its motion follows Euler’s rigid-body equations.

## Model and notation

Let body-fixed principal axes be \((\mathbf e_1,\mathbf e_2,\mathbf e_3)\), with \(\mathbf e_3\) normal to the plate. For an axisymmetric plate,

\[
I_1=I_2\equiv I_\perp,\qquad I_3\equiv I_\parallel .
\]

For a uniform thin circular plate of mass \(M\) and radius \(R\),

\[
I_\perp=\frac14 MR^2,\qquad
I_\parallel=\frac12 MR^2=2I_\perp.
\]

Write the angular velocity in the body frame as

\[
\boldsymbol\omega=\omega_1\mathbf e_1+\omega_2\mathbf e_2+\omega_3\mathbf e_3.
\]

Here \(\omega_3\) is the spin about the plate normal, while \(\omega_1,\omega_2\) describe the wobble/tilt motion.

## Equations of motion

With no external torque about the centre of mass,

\[
\boldsymbol{\tau}=0,
\]

Euler’s equations become

\[
I_\perp \dot\omega_1+(I_\parallel-I_\perp)\omega_2\omega_3=0,
\]

\[
I_\perp \dot\omega_2+(I_\perp-I_\parallel)\omega_3\omega_1=0,
\]

\[
I_\parallel\dot\omega_3=0.
\]

Equivalently,

\[
\boxed{
\begin{aligned}
\dot\omega_1 &=-\frac{I_\parallel-I_\perp}{I_\perp}\,\omega_2\omega_3,\\[4pt]
\dot\omega_2 &=\phantom{-}\frac{I_\parallel-I_\perp}{I_\perp}\,\omega_1\omega_3,\\[4pt]
\dot\omega_3 &=0.
\end{aligned}}
\]

Thus the axial spin is constant:

\[
\omega_3=s=\text{constant}.
\]

These are the equations of motion for the idealized free wobbling plate. They are the torque-free Euler equations specialized to \(I_1=I_2\). [lehman](https://www.lehman.edu/faculty/anchordoqui/CM07_12.pdf)

## Wobble solution

Define

\[
\Omega=\frac{I_\parallel-I_\perp}{I_\perp}\,\omega_3.
\]

Then \(\omega_1,\omega_2\) obey harmonic-oscillator equations,

\[
\ddot\omega_1+\Omega^2\omega_1=0,
\qquad
\ddot\omega_2+\Omega^2\omega_2=0.
\]

A convenient solution is

\[
\boxed{
\begin{aligned}
\omega_1(t)&=A\cos(\Omega t+\delta),\\
\omega_2(t)&=A\sin(\Omega t+\delta),\\
\omega_3(t)&=s.
\end{aligned}}
\]

So the transverse angular-velocity vector \((\omega_1,\omega_2)\) rotates uniformly in the body frame. This rotation is the intrinsic wobble.

For a thin uniform disk, \(I_\parallel=2I_\perp\), hence

\[
\boxed{\Omega=\omega_3.}
\]

That is, the body-frame transverse angular velocity circulates at the same magnitude as the spin rate for an ideal thin plate. [physics.stackexchange](https://physics.stackexchange.com/questions/340505/feynmans-wobbling-plate)

## Euler-angle form

Use Euler angles \((\phi,\theta,\psi)\):

- \(\theta\): angle between the plate normal \(\mathbf e_3\) and the fixed angular-momentum direction;
- \(\phi\): precession of the plate normal about that fixed direction;
- \(\psi\): rotation of the plate around its own normal.

With the standard convention,

\[
\begin{aligned}
\omega_1 &= \dot\phi\sin\theta\sin\psi+\dot\theta\cos\psi,\\
\omega_2 &= \dot\phi\sin\theta\cos\psi-\dot\theta\sin\psi,\\
\omega_3 &= \dot\phi\cos\theta+\dot\psi.
\end{aligned}
\]

For a free axisymmetric plate, the nutation angle is constant:

\[
\boxed{\dot\theta=0.}
\]

Let \(L=|\mathbf L|\) be the conserved angular momentum. Then

\[
L\cos\theta=I_\parallel\omega_3,
\]

and the precession rate is

\[
\boxed{
\dot\phi=\frac{L}{I_\perp}
=\frac{I_\parallel}{I_\perp}\frac{\omega_3}{\cos\theta}.
}
\]

The body-spin Euler angle evolves as

\[
\boxed{
\dot\psi
=
\omega_3-\dot\phi\cos\theta
=
-\frac{I_\parallel-I_\perp}{I_\perp}\omega_3
=
-\Omega.
}
\]

Therefore, for a thin plate,

\[
\boxed{
\dot\phi=\frac{2\omega_3}{\cos\theta},
\qquad
\dot\psi=-\omega_3,
\qquad
\dot\theta=0.
}
\]

For a small wobble angle \(\theta\ll1\),

\[
\dot\phi\simeq 2\omega_3.
\]

So the normal of a freely spinning thin plate precesses in space at approximately **twice** its axial spin rate when the wobble is small. The Euler-angle angular-velocity relations used here are standard rigid-body kinematics. [galileoandeinstein.phys.virginia](https://galileoandeinstein.phys.virginia.edu/7010/CM_26_Euler_Angles.html)

## Conserved quantities

The motion can also be checked from two invariants:

\[
\boxed{
T=
\frac12 I_\perp(\omega_1^2+\omega_2^2)
+\frac12 I_\parallel\omega_3^2
=
\text{constant},
}
\]

and

\[
\boxed{
L^2=
I_\perp^2(\omega_1^2+\omega_2^2)
+I_\parallel^2\omega_3^2
=
\text{constant}.
}
\]

Since \(\omega_3\) is constant, these imply

\[
\omega_1^2+\omega_2^2=A^2=\text{constant}.
\]

Hence the angular-velocity tip traces a circle in the body-frame \((\omega_1,\omega_2)\)-plane.

## Important distinction

These equations describe a plate wobbling freely in the air or effectively torque-free about its centre of mass. If you mean an **Euler’s disk** or a plate rolling on a table, gravity, normal contact force, friction, and a non-slip or slipping contact constraint must be included. Then the equations are no longer the three torque-free Euler equations above; one must use

\[
m\ddot{\mathbf r}_{\rm CM}
=
m\mathbf g+\mathbf N+\mathbf F,
\]

\[
\frac{d\mathbf L_{\rm CM}}{dt}
=
\mathbf r_{\rm contact/CM}\times(\mathbf N+\mathbf F),
\]

supplemented by either the rolling-without-slip constraint

\[
\mathbf v_{\rm contact}=0,
\]

or a specified friction law for slipping. Contacting-disk analyses use precisely linear and angular momentum balances of this form. [juen.ac](https://www.juen.ac.jp/lab/takano/ND_CRED.pdf)

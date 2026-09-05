
For a freely rotating **thin uniform disk**, the intrinsic wobble frequency is

\[
\boxed{\Omega_{\rm body}
=
\frac{I_3-I_1}{I_1}\,\omega_3}
\]

where \(I_1=I_2\) is the diameter-axis moment of inertia, \(I_3\) is the moment about the disk normal, and \(\omega_3\) is the component of angular velocity along the disk normal.

Because a thin uniform disk has \(I_3=2I_1\),

\[
\boxed{\Omega_{\rm body}=\omega_3.}
\]

This is the frequency with which the transverse components of \(\boldsymbol\omega\) rotate in the **body frame**. What you visually see—the disk’s normal precessing around the fixed angular-momentum direction—has a different frequency, approximately \(2\omega_3\) for a small wobble. [damtp.cam.ac](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S3.html)

## Start from Euler’s equations

Let \((\mathbf e_1,\mathbf e_2,\mathbf e_3)\) be principal axes fixed in the disk, with \(\mathbf e_3\) perpendicular to the disk. For an axisymmetric body,

\[
I_1=I_2\equiv I_\perp,
\qquad
I_3\equiv I_\parallel.
\]

For torque-free motion, Euler’s equations are

\[
I_\perp\dot\omega_1+(I_\parallel-I_\perp)\omega_2\omega_3=0,
\]

\[
I_\perp\dot\omega_2-(I_\parallel-I_\perp)\omega_1\omega_3=0,
\]

\[
I_\parallel\dot\omega_3=0.
\]

The last equation gives

\[
\omega_3=\text{constant}.
\]

Define

\[
\Omega_{\rm body}
=
\frac{I_\parallel-I_\perp}{I_\perp}\omega_3.
\]

Then, up to the choice of signs and orientation of \(\mathbf e_1,\mathbf e_2\),

\[
\dot\omega_1=-\Omega_{\rm body}\omega_2,
\qquad
\dot\omega_2=\Omega_{\rm body}\omega_1.
\]

Differentiate the first equation:

\[
\ddot\omega_1
=
-\Omega_{\rm body}\dot\omega_2
=
-\Omega_{\rm body}^2\omega_1.
\]

Therefore,

\[
\boxed{
\ddot\omega_1+\Omega_{\rm body}^2\omega_1=0,
}
\]

and likewise,

\[
\boxed{
\ddot\omega_2+\Omega_{\rm body}^2\omega_2=0.
}
\]

So the solution is

\[
\omega_1=A\cos(\Omega_{\rm body}t+\delta),
\]

\[
\omega_2=A\sin(\Omega_{\rm body}t+\delta),
\]

\[
\omega_3=\text{constant}.
\]

The transverse angular velocity rotates in a circle in the disk’s body frame. This is the torque-free wobble. [phys.libretexts](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline)/13:_Rigid-body_Rotation/13.20:_Torque-free_rotation_of_an_inertially-symmetric_rigid_rotor)

## Insert the thin-disk moments

For a uniform thin disk of mass \(M\) and radius \(R\),

\[
I_\perp=\frac14MR^2,
\qquad
I_\parallel=\frac12MR^2.
\]

Hence

\[
\frac{I_\parallel-I_\perp}{I_\perp}
=
\frac{\frac12MR^2-\frac14MR^2}{\frac14MR^2}
=1.
\]

Therefore,

\[
\boxed{
\Omega_{\rm body}=\omega_3.
}
\]

In ordinary frequencies in hertz,

\[
\boxed{
f_{\rm body}=\frac{\Omega_{\rm body}}{2\pi}
=\frac{\omega_3}{2\pi}
=f_3.
}
\]

Thus, if the disk’s axial component of rotation is \(10\ \text{Hz}\), its body-frame wobble frequency is also \(10\ \text{Hz}\).

## What “wobble frequency” means

There are two commonly confused angular frequencies.

| Quantity | Symbol | Exact result for a thin free disk | What it describes |
|---|---:|---:|---|
| Body-frame wobble | \(\Omega_{\rm body}\) | \(\omega_3\) | Rotation of \((\omega_1,\omega_2)\), or equivalently the angular-momentum direction, around the disk normal in the disk frame |
| Space-frame precession | \(\dot\phi\) | \(\frac{2\omega_3}{\cos\theta}\) | Motion of the disk normal around the fixed angular-momentum vector |
| Euler-angle body spin | \(\dot\psi\) | \(-\omega_3\) | Rotation of the body axes relative to the precessing line of nodes |

Here \(\theta\) is the constant tilt angle between the disk normal \(\mathbf e_3\) and \(\mathbf L\).

For small \(\theta\),

\[
\cos\theta\simeq 1,
\]

so the visible precession frequency is

\[
\boxed{
\dot\phi\simeq2\omega_3,
\qquad
f_{\rm visible}\simeq2f_3.
}
\]

This factor of two is the classic result for a torque-free round plate: the body-frame motion occurs at \(\omega_3\), while the plate normal’s space-frame precession is approximately \(2\omega_3\) for small tilt. [damtp.cam.ac](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S3.html)

## Deriving the visible precession rate

The angular momentum components in the disk frame are

\[
\mathbf L
=
I_\perp\omega_1\mathbf e_1
+
I_\perp\omega_2\mathbf e_2
+
I_\parallel\omega_3\mathbf e_3.
\]

Since \(\mathbf L\) is fixed in inertial space,

\[
L\cos\theta=I_\parallel\omega_3.
\]

The disk symmetry axis precesses around \(\mathbf L\) at rate

\[
\dot\phi=\frac{L}{I_\perp}.
\]

Substitute

\[
L=\frac{I_\parallel\omega_3}{\cos\theta},
\]

to obtain

\[
\boxed{
\dot\phi
=
\frac{I_\parallel}{I_\perp}
\frac{\omega_3}{\cos\theta}.
}
\]

For a thin disk, \(I_\parallel/I_\perp=2\), so

\[
\boxed{
\dot\phi=\frac{2\omega_3}{\cos\theta}.
}
\]

For example, if a disk has \(\omega_3=60\ \text{rad s}^{-1}\) and tilts by \(\theta=10^\circ\),

\[
\Omega_{\rm body}=60\ \text{rad s}^{-1},
\]

while

\[
\dot\phi
=
\frac{120}{\cos10^\circ}
\approx121.85\ \text{rad s}^{-1}.
\]

Thus,

\[
f_{\rm body}\approx9.55\ \text{Hz},
\qquad
f_{\rm visible}\approx19.39\ \text{Hz}.
\]

## Scope of this result

This derivation assumes:

- A rigid, uniform, very thin circular disk.
- Rotation about its centre of mass.
- No external torque.
- Constant wobble angle \(\theta\).
- No aerodynamic drag, gravity torque, surface contact, or friction.

A disk spinning and wobbling on a table—Euler’s disk—is a different problem. Its frequency varies strongly in time as its inclination decreases, and contact forces, gravity, rolling/slipping, and dissipation determine the observed accelerating wobble. The \(\Omega_{\rm body}=\omega_3\) and \(\dot\phi\simeq2\omega_3\) results apply to the free, torque-free plate rather than the final-stage tabletop Euler’s-disk motion.

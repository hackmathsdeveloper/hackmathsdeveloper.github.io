
**Methods for solving the Schrödinger equation** fall into analytical (exact or approximate), numerical, and hybrid categories. They differ significantly between the **time-independent Schrödinger equation (TISE)** and the **time-dependent Schrödinger equation (TDSE)**.

### Time-Independent Schrödinger Equation (TISE)
The TISE is the eigenvalue problem
\[
\hat{H}\psi = E\psi, \qquad
\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r}).
\]
It is solved for bound states (discrete spectrum) or scattering states (continuous spectrum).

#### Exact Analytical Methods
- **Separation of variables**: When \(V\) is time-independent, the full TDSE separates into a spatial TISE and a simple time equation \(\phi(t) \propto e^{-iEt/\hbar}\). In multiple dimensions, further separation is possible if the potential separates in Cartesian, spherical, cylindrical, or other coordinates (e.g., hydrogen atom in spherical coordinates).
- **Exact closed-form solutions** for special potentials:
  - Infinite square well (trigonometric functions).
  - Finite square well (matching transcendental equations).
  - Harmonic oscillator (Hermite polynomials × Gaussian).
  - Hydrogen atom / Coulomb potential (associated Laguerre polynomials × spherical harmonics).
  - Morse potential, Pöschl–Teller potential, etc.
- **Series solutions / Frobenius method**: Power-series expansions about regular singular points (used for hydrogen radial equation, Bessel, Legendre, etc.).
- **Transformation to known equations**: Mapping the TISE onto hypergeometric, confluent hypergeometric, or other classical special-function equations.

#### Approximate Analytical Methods
- **Time-independent perturbation theory**:
  - Non-degenerate: Expand energies and wavefunctions in powers of a small perturbation \(H'\).
  - Degenerate: Diagonalize the perturbation within the degenerate subspace first.
- **Variational method (Rayleigh–Ritz)**: Choose a trial function with adjustable parameters; minimize \(\langle\psi|\hat{H}|\psi\rangle/\langle\psi|\psi\rangle\). Gives upper bounds to the ground-state (and, with orthogonalization, excited-state) energies. Extends to basis-set expansions leading to a matrix eigenvalue problem \(\mathbf{Hc}=E\mathbf{Sc}\).
- **WKB (Wentzel–Kramers–Brillouin) / semiclassical approximation**: Valid for slowly varying potentials. Uses local de Broglie wavelength and connection formulas across turning points; yields quantization conditions and tunneling rates.
- **Adiabatic approximation** (Born–Oppenheimer for molecules): Separate fast and slow degrees of freedom.
- Other specialized approximations: Airy-function matching near linear turning points, effective-mass approximations in solids, etc.

#### Numerical Methods for TISE
- **Shooting method**: Integrate the ordinary differential equation outward (or inward) from a boundary, adjusting the energy \(E\) until the wavefunction satisfies the far-side boundary condition (often combined with bisection or Newton root-finding).
- **Numerov method**: High-order (error \(\sim(\Delta x)^6\)) finite-difference integrator specialized for equations of the form \(\psi''=f(x)\psi\). Frequently paired with shooting.
- **Finite-difference / finite-element discretizations**: Convert the differential operator into a matrix on a spatial grid; solve the resulting algebraic eigenvalue problem.
- **Discrete Variable Representation (DVR)**: Represent the wavefunction on a grid of quadrature points; kinetic-energy matrix elements are known analytically (often Fourier-based).
- **Basis-set expansion + matrix diagonalization**: Expand \(\psi=\sum c_k\phi_k\) in a convenient complete set (harmonic-oscillator functions, Gaussians, plane waves, finite-element bases, etc.) and diagonalize the Hamiltonian matrix. Sparse-matrix techniques such as the Lanczos algorithm efficiently extract the lowest eigenvalues.
- **Other techniques**: Finite-element methods in higher dimensions, spectral methods, quantum Monte Carlo (for many-body ground states).

### Time-Dependent Schrödinger Equation (TDSE)
The TDSE is
\[
i\hbar\frac{\partial\Psi}{\partial t}=\hat{H}(t)\Psi.
\]
When \(\hat{H}\) is time-independent the formal solution is \(\Psi(t)=e^{-i\hat{H}t/\hbar}\Psi(0)\).

#### Exact / Semi-Analytical Approaches
- **Expansion in stationary states**: If the eigenfunctions \(\psi_n\) and eigenvalues \(E_n\) of the time-independent Hamiltonian are known,
  \[
  \Psi(\mathbf{r},t)=\sum_n c_n\psi_n(\mathbf{r})e^{-iE_nt/\hbar},
  \]
  with coefficients fixed by the initial condition. This is exact for time-independent \(H\).
- **Time-dependent perturbation theory**: Expand in powers of a weak time-dependent interaction (Fermi’s golden rule, multiphoton transitions, etc.).
- **Sudden approximation**: Instantaneous change of Hamiltonian; wavefunction is continuous, coefficients are overlaps with the new eigenbasis.
- **Adiabatic approximation**: Slow variation of parameters; system stays in the instantaneous eigenstate (Berry phase appears in the geometric phase).
- **Exact solvable models**: Driven harmonic oscillator, certain two-level systems (Rabi model), etc.

#### Numerical Propagators for TDSE
Most practical methods approximate the unitary time-evolution operator \(U(t,t_0)\).

- **Short-time propagation** (most common): Assume \(H\) is constant over a small interval \(\Delta t\) and apply \(e^{-iH\Delta t/\hbar}\).
  - **Crank–Nicolson** (implicit, unitary, second-order): Cayley form
    \[
    U\approx\frac{1-iH\Delta t/2}{1+iH\Delta t/2}.
    \]
  - **Split-operator / Fourier methods**: Factor kinetic and potential pieces (Trotter or higher-order decompositions) and evaluate the kinetic part in momentum space via FFT.
  - **Chebyshev polynomial expansion**: Global expansion of the exponential in Chebyshev polynomials of the Hamiltonian; very accurate for long times when the spectrum is bounded.
  - **Lanczos / Krylov-subspace methods**: Project onto a small Krylov space generated by repeated application of \(H\) and exponentiate the resulting tridiagonal matrix.
  - **Magnus expansion**: Systematic expansion that preserves unitarity for time-dependent \(H\).
  - **Explicit multistep or Runge–Kutta-type schemes**: Higher-order explicit integrators (some preserve norm approximately or exactly after stabilization).
  - **Polynomial methods** and other exponential integrators.
- **Global / larger-step methods**: Double DVR (space–time basis), iterative Volterra integral formulations, etc., that treat longer intervals at once.
- **Path-integral methods**: Feynman path integrals (Monte-Carlo or semiclassical approximations).
- **Other specialized techniques**: Absorbing potentials or complex scaling for continuum problems, time-dependent density-functional theory (TDDFT) for many-electron systems, quantum Monte Carlo for imaginary-time propagation (ground-state projection).

### Practical Considerations and Hierarchy
- **Exact analytic solutions** exist only for a handful of potentials; they serve as benchmarks and pedagogical tools.
- **Approximate analytic methods** (perturbation, variational, WKB) give insight and are often sufficient for weak interactions or semiclassical regimes.
- **Numerical methods** are the workhorses for realistic potentials. Choice depends on dimensionality, whether the spectrum is discrete or continuous, time-independence of \(H\), required accuracy, and available computational resources.
- In higher dimensions or for many-body systems the exponential growth of Hilbert-space dimension forces further approximations (mean-field, DFT, configuration interaction, tensor networks, etc.).

In summary, the TISE is most often attacked by separation of variables + exact special-function solutions, shooting/Numerov, variational/basis-set diagonalization, perturbation theory, or WKB. The TDSE is typically solved by expanding in the stationary eigenbasis (when available) or by unitary numerical propagators such as Crank–Nicolson, split-operator, Chebyshev, or Lanczos methods. Hybrid analytic–numeric strategies are common in practice.

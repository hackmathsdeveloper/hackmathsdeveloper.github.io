
The closest answer is the **compressible Navier–Stokes equations**, extended to include chemical reactions and heat transfer. They describe the gas flowing through the intake, compressor, combustor, turbine, and nozzle. However, no single differential equation describes every phenomenon in a jet engine: a complete model couples fluid-flow equations to combustion, heat conduction, and mechanical dynamics. NASA describes the core fluid system as conservation equations for mass, momentum, and energy. [grc.nasa](https://www.grc.nasa.gov/WWW/k-12/airplane/nseqs.html)

## 1. The central equations: reacting, compressible fluid flow

For a conventional gas-turbine jet engine, the main unknowns are fields that vary with position and time:

- Density \(\rho(\mathbf{x},t)\).
- Velocity \(\mathbf{u}(\mathbf{x},t)\).
- Pressure \(p(\mathbf{x},t)\).
- Temperature \(T(\mathbf{x},t)\).
- Chemical-species mass fractions \(Y_k(\mathbf{x},t)\).

The governing equations express conservation of mass, momentum, energy, and chemical species. Compressibility matters because the gas changes density as it is compressed, heated, and expanded. [grc.nasa](https://www.grc.nasa.gov/WWW/k-12/airplane/nseqs.html)

### A. Conservation of mass

\[
\boxed{
\frac{\partial \rho}{\partial t}
+\nabla\cdot(\rho\mathbf{u})=0
}
\]

This says that mass cannot disappear: any accumulation of gas in a region must result from a net inflow. It applies throughout the engine, including the compression and expansion regions. [grc.nasa](https://www.grc.nasa.gov/WWW/k-12/airplane/nseqs.html)

### B. Conservation of momentum

\[
\boxed{
\frac{\partial(\rho\mathbf{u})}{\partial t}
+\nabla\cdot(\rho\mathbf{u}\otimes\mathbf{u})
=
-\nabla p+\nabla\cdot\boldsymbol{\tau}
+\rho\mathbf{b}
}
\]

Here:

- \(\mathbf{u}\otimes\mathbf{u}\) represents transport of momentum by the moving gas.
- \(-\nabla p\) is the force due to pressure gradients.
- \(\nabla\cdot\boldsymbol{\tau}\) represents viscous forces.
- \(\mathbf{b}\) is body force per unit mass.

This is Newton’s second law applied locally to the gas. Together with moving blade boundaries, it describes how compressor and turbine blades exchange momentum with the flow. [en.wikipedia](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations)

### C. Conservation of total energy

One useful conservative form is

\[
\boxed{
\frac{\partial(\rho E)}{\partial t}
+\nabla\cdot\left[(\rho E+p)\mathbf{u}\right]
=
\nabla\cdot(\boldsymbol{\tau}\cdot\mathbf{u})
-\nabla\cdot\mathbf{q}
+\rho\mathbf{b}\cdot\mathbf{u}
+\dot Q_{\mathrm{ext}}
}
\]

where

\[
E=e+\frac12|\mathbf{u}|^2.
\]

Here \(e\) is specific internal energy, \(\mathbf{q}\) is heat flux—including conductive and species-diffusion contributions—and \(\dot Q_{\mathrm{ext}}\) represents any separately modeled volumetric energy input. This equation tracks the exchange between internal energy, kinetic energy, pressure work, viscous work, and heat transfer. [grc.nasa](https://www.grc.nasa.gov/WWW/k-12/airplane/nseqs.html)

An important bookkeeping detail: if \(e\) includes the chemical formation energies of the species, combustion does not need a separate “heat-release” source in this total-energy equation. Reactions change composition, and the temperature changes consistently with the mixture’s energy. Adding the same chemical energy again as a source would double-count it. [charlesreid1](https://charlesreid1.com/wiki/Cantera/Reactor_Equations)

### D. Conservation of each chemical species

For species \(k\),

\[
\boxed{
\frac{\partial(\rho Y_k)}{\partial t}
+\nabla\cdot(\rho Y_k\mathbf{u})
=
-\nabla\cdot\mathbf{J}_k+\dot\omega_k
}
\]

where:

- \(\mathbf{J}_k\) is the diffusive mass flux of species \(k\).
- \(\dot\omega_k\) is its chemical production rate per unit volume.

This extends the fluid model to combustion: fuel and oxygen are transported, mixed, and converted into reaction products. Chemical-reactor models likewise couple species balances to energy balances, often producing stiff systems of differential equations because reaction timescales differ greatly. [cantera](https://cantera.org/stable/reference/reactors/index.html)

## 2. Why those equations still need additional relationships

Conservation laws alone do not determine every unknown. You also need constitutive and thermodynamic relationships—for example, an ideal-gas-mixture equation of state,

\[
p=\rho R_{\mathrm{mix}}T,
\]

a model for viscous stress, thermal conductivity, species diffusion, and chemical reaction rates. The equation of state closes the relationship among pressure, temperature, density, and composition. [cantera](https://cantera.org/stable/reference/reactors/index.html)

Turbulence introduces another modeling choice. When engineers solve averaged rather than fully resolved flow equations, extra turbulent stresses and energy transport appear, requiring closure models. NASA’s compressible-flow work, for example, uses Favre-averaged conservation equations together with additional turbulence transport equations. [ntrs.nasa](https://ntrs.nasa.gov/search.jsp?R=19920016133)

Thus, “Navier–Stokes” is the foundation—not a complete engine model by itself.

## 3. What must be coupled in to describe the whole engine?

The gas is only one part of the engine. Blade temperatures, deformation, vibration, and shaft acceleration require additional equations.

| Phenomenon | Representative equation | What it adds |
|---|---|---|
| Heat conduction in blades and casing | \(\displaystyle \rho_s c_s\frac{\partial T_s}{\partial t}=\nabla\cdot(k_s\nabla T_s)+\dot q_s\) | Temperature distribution inside solid parts |
| Structural deformation and vibration | \(\displaystyle \rho_s\frac{\partial^2\mathbf d}{\partial t^2}=\nabla\cdot\boldsymbol{\sigma}+\mathbf f_s\) | Blade displacement, stress, and vibration |
| Shaft acceleration, for constant rotational inertia | \(\displaystyle I\frac{d\Omega}{dt}=\mathcal T_{\mathrm{turbine}}-\mathcal T_{\mathrm{compressor}}-\mathcal T_{\mathrm{load}}-\mathcal T_{\mathrm{loss}}\) | How rotor speed changes during startup or throttle changes |

These are representative continuum and rotational-dynamics forms; their detailed implementation depends on the materials, geometry, and modeling assumptions. Gas-turbine simulations couple fluid and thermal calculations to capture blade cooling, and transfer aerodynamic and thermal loads into structural models. Reduced engine-dynamics models also connect fuel delivery to rotational speed. [nas.nasa](https://www.nas.nasa.gov/assets/nas/pdf/ams/2021/AMS_20211110_Krishnan.pdf)

The coupling goes both ways: the gas heats and loads the blades, while blade motion and temperature influence the flow and heat transfer. This is why an all-phenomena model is a multiphysics problem. [nas.nasa](https://www.nas.nasa.gov/assets/nas/pdf/ams/2021/AMS_20211110_Krishnan.pdf)

## 4. Which model is “best” depends on what you want to predict

There is a useful hierarchy:

- For thrust at a known operating condition, an integral momentum balance may be sufficient. Thrust is principally the change in flow momentum, with a pressure correction. [web.mit](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node78.html)
- For startup, throttle response, or speed regulation, reduced differential-equation models of the engine and fuel system are more appropriate. [epj-conferences](https://www.epj-conferences.org/articles/epjconf/pdf/2015/11/epjconf_efm2014_02034.pdf)
- For compressor surge and rotating stall, specialized models such as the Moore–Greitzer system capture the relevant instability dynamics without resolving the entire engine. [web.math.ucsb](https://web.math.ucsb.edu/~birnir/research/outline.html)
- For detailed internal flow and blade cooling, compressible CFD and coupled heat-transfer models are needed. [ntrs.nasa](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20020073073.pdf)
- For blade stress and deformation, the fluid solution must be coupled to thermal and structural calculations. [nas.nasa](https://www.nas.nasa.gov/assets/nas/pdf/ams/2021/AMS_20211110_Krishnan.pdf)

For example, a simplified single-stream thrust equation is

\[
F
=
\dot m_e V_e-\dot m_a V_a
+(p_e-p_a)A_e,
\]

under the usual steady, approximately uniform inlet/exit assumptions and ambient-pressure inlet condition. This is an integrated consequence of momentum conservation—not a differential equation that describes combustion, cooling, or vibration. [web.mit](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node78.html)

So, if you want the name of the fundamental governing system, it is the reacting compressible Navier–Stokes system. If you literally want all phenomena occurring in a jet engine, the appropriate object is a coupled system of fluid, chemical, thermal, and mechanical differential equations, supplied with material laws, geometry, and initial and boundary conditions.

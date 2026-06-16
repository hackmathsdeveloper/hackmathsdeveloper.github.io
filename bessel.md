
https://www.perplexity.ai/search/f446aae2-51df-4615-b3ab-e4d5393f4e90


elaborate on this with lots of actual examples and original equations:

Bessel functions also appear in other fields, such as [signal processing](https://en.wikipedia.org/wiki/Signal_processing "Signal processing") (e.g., see [FM audio synthesis](https://en.wikipedia.org/wiki/Frequency_modulation_synthesis "Frequency modulation synthesis"), [Kaiser window](https://en.wikipedia.org/wiki/Kaiser_window "Kaiser window"), or [Bessel filter](https://en.wikipedia.org/wiki/Bessel_filter "Bessel filter")). They also appear in pure mathematics as part of the Fourier expansion of [Maass forms](https://en.wikipedia.org/wiki/Maass_forms "Maass forms").


# elaborate on this with lots of actual examples and original equations:

Bessel functions also appear in other fields, such as [signal processing](https://en.wikipedia.org/wiki/Signal_processing) (e.g., see [FM audio synthesis](https://en.wikipedia.org/wiki/Frequency_modulation_synthesis), [Kaiser window](https://en.wikipedia.org/wiki/Kaiser_window), or [Bessel filter](https://en.wikipedia.org/wiki/Bessel_filter)). They also appear in pure mathematics as part of the Fourier expansion of [Maass forms](https://en.wikipedia.org/wiki/Maass_forms).

Bessel functions enter signal processing and Maass forms in very concrete, computational ways: they literally show up as the coefficients of Fourier expansions or as closed‑form expressions for design parameters. Below are several worked examples and explicit equations.

***

## 1. FM synthesis: sidebands as Bessel coefficients

Consider a single‑tone FM signal with carrier frequency $\omega_c$, modulation frequency $\omega_m$, and modulation index $\beta$:

$$
s(t) = \sin\!\bigl(\omega_c t + \beta \sin(\omega_m t)\bigr).
$$

A classical identity expresses this as a Fourier series in harmonics of the modulating tone with weights $J_k(\beta)$, the Bessel functions of the first kind:[^1][^2][^3]

$$
\sin\!\bigl(\omega_c t + \beta \sin(\omega_m t)\bigr)
= \sum_{k=-\infty}^{\infty} J_k(\beta)\,\sin\bigl((\omega_c + k\omega_m)t\bigr).
$$

So:

- Each sideband at frequency $\omega_c + k\omega_m$ has amplitude $J_k(\beta)$.
- Changing $\beta$ redistributes energy across sidebands in a highly structured way.


### Example: explicit expansion for small $\beta$

For small $\beta$, we have the approximations[^4][^3]

$$
J_0(\beta) \approx 1 - \frac{\beta^2}{4},\quad
J_1(\beta) \approx \frac{\beta}{2},\quad
J_n(\beta) \approx 0\text{ for }n\ge 2.
$$

Plugging these into the FM signal and keeping only $k=-1,0,1$:

$$
\begin{aligned}
s(t)
&\approx J_0(\beta)\sin(\omega_c t)
+ J_1(\beta)\sin((\omega_c + \omega_m)t)
+ J_{-1}(\beta)\sin((\omega_c - \omega_m)t) \\
&\text{and }J_{-1}(\beta)= -J_1(\beta),
\end{aligned}
$$

so

$$
s(t) \approx \left(1-\frac{\beta^2}{4}\right)\sin(\omega_c t)
+ \frac{\beta}{2}\sin((\omega_c + \omega_m)t)
- \frac{\beta}{2}\sin((\omega_c - \omega_m)t).
$$

This is the standard narrowband‑FM approximation: a slightly reduced carrier plus two symmetric sidebands. The Bessel functions give the exact correction at higher orders.

### Example: zeroing the carrier in FM

At specific $\beta$, $J_0(\beta)=0$. Let $\beta_0\approx 2.4048255577$ be the first positive zero of $J_0$. Then[^3]

$$
s(t) = \sin\!\bigl(\omega_c t + \beta_0 \sin(\omega_m t)\bigr)
$$

has no carrier component: the $\omega_c$ term vanishes because its coefficient $J_0(\beta_0)$ is zero. The spectrum is purely sidebands at $\omega_c \pm k\omega_m$, $k\ge 1$.

This is exploited in FM synthesis to design “hollow” or bell‑like timbres: pick $\beta$ so that $J_0(\beta)$ is small or zero, forcing most energy into higher harmonics.

### Example: power identity and FM bandwidth

Bessel functions satisfy the Parseval‑like identity[^4][^3]

$$
\sum_{n=-\infty}^{\infty} J_n(\beta)^2 = 1.
$$

Interpreting this in FM:

- Total normalized power of the FM signal is 1 (for unit carrier amplitude).
- The fraction of power in sideband $n$ is $J_n(\beta)^2$.
- “Significant” sidebands are those with $|J_n(\beta)|$ above some threshold (e.g., $0.02$), which is used in communication texts to compute the effective occupied bandwidth from tables of $J_n(\beta)$. [^4]

***

## 2. Kaiser (Kaiser–Bessel) window: FIR design and Bessel ratios

The (discrete) Kaiser window of length $N$ is defined by[^5][^6][^7][^8]

$$
w[k] = 
\frac{I_0\!\Bigl(\pi\alpha\sqrt{1-\Bigl(\frac{2k}{N-1}-1\Bigr)^2}\Bigr)}
     {I_0(\pi\alpha)},\quad k=0,\dots,N-1,
$$

where $I_0$ is the modified Bessel function of the first kind of order zero and $\alpha$ controls the trade‑off between main‑lobe width and side‑lobe level.[^7][^5]

The underlying Bessel function is defined by its series:[^7]

$$
I_\nu(x) = \sum_{n=0}^{\infty}
\frac{1}{n!\,\Gamma(n+\nu+1)}\left(\frac{x}{2}\right)^{2n+\nu},
$$

and in particular

$$
I_0(x) = \sum_{n=0}^{\infty} \frac{1}{(n!)^2}\left(\frac{x}{2}\right)^{2n}.
$$

### Example: explicit Kaiser window values

Take $N=5$ and $\alpha=3$. Then $k=0,1,2,3,4$, and

$$
\frac{2k}{N-1}-1 = \frac{2k}{4}-1 = \frac{k}{2} - 1.
$$

Compute the argument factor

$$
r_k = \sqrt{1-\left(\frac{k}{2}-1\right)^2}.
$$

This gives

- $k=0$: $r_0 = \sqrt{1-(-1)^2} = 0$.
- $k=1$: $r_1 = \sqrt{1-( -0.5)^2} = \sqrt{1-0.25} = \sqrt{0.75}$.
- $k=2$: $r_2 = \sqrt{1-0^2} = 1$.
- $k=3$: symmetric with $k=1$: $r_3 = \sqrt{0.75}$.
- $k=4$: symmetric with $k=0$: $r_4 = 0$.

So the Kaiser window becomes

$$
w = w[^9] = \frac{I_0(0)}{I_0(3\pi)},\quad
w[^10] = w[^5] = \frac{I_0(3\pi\sqrt{0.75})}{I_0(3\pi)},\quad
w[^11] = \frac{I_0(3\pi)}{I_0(3\pi)} = 1.
$$

Using the series truncated at, say, $n=3$,

$$
I_0(x) \approx 1 + \frac{x^2}{4} + \frac{x^4}{64} + \frac{x^6}{2304}.
$$

Plugging $x=3\pi$ gives a large denominator, while for $x=0$ the numerator is 1. Hence $w$ and $w[^9]$ become small, giving a smoothly tapered window with maximum at the center tap. This explicit expression shows how the Bessel function controls the taper.

### Example: approximate design formulas

In FIR design, one often parametrizes the Kaiser window by desired stopband attenuation $A$ (in dB) and transition width $\Delta\omega$. A standard set of empirical yet widely used design equations is[^6][^8]

$$
\beta = 
\begin{cases}
0, & A \le 21,\\
0.5842(A-21)^{0.4} + 0.07886(A-21), & 21 < A < 50,\\
0.1102(A-8.7), & A \ge 50,
\end{cases}
$$

and the required filter length is approximately

$$
N \approx \frac{A - 8}{2.285\Delta\omega} + 1.
$$

These formulas encode the complicated relationship between the Bessel‑controlled time‑domain shape and frequency‑domain side lobe level into two simple algebraic expressions. The $\beta$ that appears here is precisely the same parameter as the $\alpha$ (up to scaling conventions) that enters $I_0$ in the window definition.[^5][^6]

***

## 3. Bessel filters: Bessel polynomials and maximally flat group delay

The analog low‑pass Bessel filter has transfer function[^11][^12]

$$
H(s) = \frac{1}{B_N(s)},
$$

where $B_N(s)$ is the $N$th‑order Bessel polynomial satisfying the recursion[^12]

$$
B_N(s) = (2N-1)\,B_{N-1}(s) + s^2 B_{N-2}(s),\quad B_0(s) = 1,\ B_1(s) = s+1.
$$

The first few polynomials are[^11][^12]

$$
\begin{aligned}
B_0(s) &= 1,\\
B_1(s) &= s + 1,\\
B_2(s) &= s^2 + 3s + 3,\\
B_3(s) &= s^3 + 6s^2 + 15s + 15,\\
B_4(s) &= s^4 + 10s^3 + 45s^2 + 105s + 105.
\end{aligned}
$$

These polynomials are intimately related to Bessel functions of half‑integer order; their coefficients come from truncated series expansions of Bessel functions and are chosen to make the group delay maximally flat at $\omega=0$.[^12]

### Example: explicit second‑order Bessel low‑pass

Take $N=2$. The unnormalized transfer function is

$$
H(s) = \frac{1}{s^2 + 3s + 3}.
$$

To set a desired cutoff frequency $\omega_c$, you apply frequency scaling $s \mapsto s/\omega_c$:

$$
H(s) = \frac{1}{(s/\omega_c)^2 + 3(s/\omega_c) + 3}
= \frac{\omega_c^2}{s^2 + 3\omega_c s + 3\omega_c^2}.
$$

So a realizable 2nd‑order analog Bessel low‑pass with DC gain 1 and (approximate) cutoff $\omega_c$ has

$$
H(s) = \frac{\omega_c^2}{s^2 + 3\omega_c s + 3\omega_c^2}.
$$

Compare this with a Butterworth of order 2:

$$
H_B(s)=\frac{\omega_c^2}{s^2+\sqrt{2}\,\omega_c s+\omega_c^2}.
$$

Both have unity gain at DC, but the Bessel filter’s denominator coefficients (3, 3) give a much flatter group delay near DC at the cost of a slower magnitude roll‑off. The coefficients themselves arise from matching the Taylor expansion of the phase (or equivalently the group delay) to as high an order as possible, which is where the underlying Bessel function structure enters.[^12]

### Example: group delay matching via Taylor expansion

Let the phase response near $\omega=0$ have series

$$
\phi(\omega) = -\tau_0 \omega + c_3 \omega^3 + c_5 \omega^5 + \dots
$$

Maximally flat group delay means that as many higher‑order coefficients as possible vanish:

$$
c_3 = c_5 = \dots = 0,
$$

so the group delay

$$
\tau_g(\omega) = -\frac{d\phi}{d\omega}
$$

is constant to higher order in $\omega$. Solving the resulting polynomial constraints on the denominator coefficients yields, in closed form, the Bessel polynomials above. Those polynomially defined filters can be equivalently described using spherical Bessel functions of the first kind evaluated at imaginary arguments; that representation is what ties them back to “true” Bessel functions.

***

## 4. FM in communication systems: precise spectral expressions

Communication‑theory texts derive the exact spectrum of an FM wave driven by a sinusoidal modulating signal using the integral representation of $J_n$:[^2][^13]

$$
J_n(\beta) 
= \frac{1}{2\pi}\int_{-\pi}^{\pi}
\exp\!\bigl(j(\beta \sin x - nx)\bigr)\,dx.
$$

Starting from

$$
s(t) = A_c \cos\!\bigl(\omega_c t + \beta\sin(\omega_m t)\bigr),
$$

you can write

$$
\exp\!\bigl(j\beta\sin(\omega_m t)\bigr)
= \sum_{n=-\infty}^{\infty} J_n(\beta) e^{jn\omega_m t},
$$

so

$$
\begin{aligned}
s(t)
&= \Re\Bigl\{
A_c e^{j\omega_c t}
\sum_{n=-\infty}^{\infty} J_n(\beta) e^{jn\omega_m t}
\Bigr\}\\
&= A_c \sum_{n=-\infty}^{\infty} J_n(\beta)
\cos\bigl((\omega_c+n\omega_m)t\bigr).
\end{aligned}
$$

This derivation shows exactly why Bessel functions are unavoidable: they arise as the Fourier series coefficients of the periodic function $e^{j\beta\sin x}$.[^14][^2]

***

## 5. Maass forms: Fourier–Bessel (K‑Bessel) expansion

A Maass form $f$ of eigenvalue $1/4+\nu^2$ on the upper half‑plane typically has a Fourier expansion of the form[^15][^16][^17][^18]

$$
f(z)=f(x+iy) = \sum_{n\in\mathbb{Z}} a_n\,\sqrt{y}\,K_{i\nu}(2\pi |n| y)\,e^{2\pi i n x},
$$

or, for cusp forms (no constant term),

$$
f(z) = \sum_{n\ne 0} a_n\,\sqrt{y}\,K_{i\nu}(2\pi |n| y)\,e^{2\pi i n x}.
$$

Here $K_{i\nu}$ is the K‑Bessel (modified Bessel of the second kind) with imaginary order.[^17][^15]

This is the exact analog of the usual Fourier expansion of a holomorphic modular form

$$
g(z) = \sum_{n\ge 0} b_n e^{2\pi i n z},
$$

but with an extra radial factor $\sqrt{y}\,K_{i\nu}(2\pi|n|y)$ because Maass forms are eigenfunctions of the Laplace–Beltrami operator, not holomorphic functions.

### Example: Bessel solution of the eigenvalue ODE

If you separate variables in the eigenvalue equation for the hyperbolic Laplacian,

$$
\Delta f = \left(-y^2\bigl(\partial_x^2+\partial_y^2\bigr)\right)f = \left(\frac{1}{4}+\nu^2\right)f,
$$

and write $f(x,y) = e^{2\pi i n x} u_n(y)$, you find that $u_n(y)$ satisfies[^15][^17]

$$
y^2 u_n''(y) - y u_n'(y) 
+ \Bigl((2\pi n y)^2 - \bigl(\tfrac{1}{4} + \nu^2\bigr)\Bigr)u_n(y) = 0.
$$

With the change of variables $t=2\pi |n| y$ and $u_n(y)=\sqrt{y}\,v(t)$, this becomes the modified Bessel equation

$$
t^2 v''(t) + t v'(t) - \bigl(t^2+\nu^2\bigr)v(t)=0,
$$

whose independent solutions are $I_{i\nu}(t)$ and $K_{i\nu}(t)$. The Maass cusp form condition (square integrability and decay at the cusp) forces you to select the $K$-Bessel solution because $K_{i\nu}(t)$ decays exponentially as $t\to\infty$, whereas $I_{i\nu}(t)$ grows.[^16][^17][^15]

Thus

$$
u_n(y) = c_n \sqrt{y}\,K_{i\nu}(2\pi |n| y),
$$

giving the stated Fourier–Bessel expansion.

### Example: asymptotic behavior and cusp decay

The K‑Bessel function has asymptotic behaviors [standard Bessel theory; used in Maass form analysis as in ][^16][^17]

$$
K_{i\nu}(t) \sim \sqrt{\frac{\pi}{2t}}\,e^{-t}\quad\text{as }t\to\infty,
$$

and

$$
K_{i\nu}(t) \sim 
\begin{cases}
-\log t, & \nu = 0,\\[4pt]
\frac{1}{2}\Gamma(|\nu|)\left(\frac{t}{2}\right)^{-|\nu|}, & \nu\ne 0,
\end{cases}
\quad\text{as }t\to 0.
$$

Thus each Fourier coefficient term in a Maass cusp form behaves, for large $y$, like

$$
\sqrt{y}\,K_{i\nu}(2\pi |n| y) \sim \sqrt{y}\sqrt{\frac{\pi}{4\pi |n| y}}\,e^{-2\pi|n|y}
= \frac{1}{\sqrt{2|n|}} e^{-2\pi|n|y}.
$$

So the Maass form decays exponentially in the cusp $y\to\infty$, with decay rate determined by the smallest nonzero $|n|$ in the Fourier expansion. This property is essential in analytic number theory—for example, in bounding contributions from cuspidal parts in the spectral expansion of automorphic kernels. [][]

### Example: heuristic link to “radial” expansions

From a representation‑theoretic viewpoint, the appearance of Bessel functions is not accidental: they are the radial eigenfunctions of the Laplacian in symmetric spaces. For ordinary Euclidean Fourier analysis, you get exponentials $e^{2\pi i n x}$ in the “flat” direction $x$. In the hyperbolic radial direction $y$, the analogous radial eigenfunctions are Bessel‑type functions (here $K_{i\nu}$), giving a Fourier–Bessel expansion rather than a pure Fourier series.

***

## 6. Other signal‑processing appearances (brief)

Just to round out the picture, a few more places where Bessel functions show up in concrete, computable ways:

- **Jakes fading model**: the autocorrelation function of a Rayleigh fading process in Clarke–Jakes channel models is $R(\tau)=J_0(2\pi f_D \tau)$, with $f_D$ the Doppler frequency. [][]
- **Timing recovery**: modified Bessel functions $I_0(\cdot)$ appear in non‑data‑aided timing estimators in AWGN channels because the likelihood ratio involves integrals of complex Gaussians over phase, yielding $I_0$. []
- **Window families for MDCT**: the Kaiser–Bessel‑derived (KBD) window used in audio coding (e.g., AAC) is literally built by cumulative sums of a discrete Kaiser window, whose samples are defined by $I_0$ as in section 2. []

All of these are essentially “Fourier‑adjacent” roles: Bessel functions arise either as Fourier coefficients of nontrivial periodic functions, as solutions of radial eigenvalue equations, or as analytic evaluations of integrals in likelihoods and correlation functions.

***

To dive deeper in a direction that’s most useful to you, would you prefer a more detailed derivation of the FM/Bessel identity from the Jacobi–Anger expansion, or a more representation‑theoretic viewpoint on Maass forms and their K‑Bessel expansions?
<span style="display:none">[^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29]</span>

<div align="center">⁂</div>

[^1]: https://www.dafx.de/paper-archive/2004/P_339.PDF

[^2]: https://es.slideshare.net/slideshow/tele3113-wk5wed/8210989

[^3]: http://www2.ensc.sfu.ca/people/faculty/ho/ENSC327/Pre_10_Bessel.pdf

[^4]: https://www.mmmut.ac.in/News_content/10301tpnews_10162020.pdf

[^5]: https://en.wikipedia.org/wiki/Kaiser_window

[^6]: https://www.dsprelated.com/freebooks/sasp/Kaiser_Window.html

[^7]: https://www.recordingblogs.com/wiki/kaiser-window

[^8]: https://2021.help.altair.com/2021/hwdesktop/hwd/topics/reference/math/kaiser.htm

[^9]: https://id.scribd.com/document/412502837/10-1-1-224-9222-pdf

[^10]: https://www.oreilly.com/library/view/digital-communication-systems/9780471647355/AppendixC.html

[^11]: https://www.ech-vzw.be/filters/LowPassFilterDesignBessel.pdf

[^12]: https://de.scribd.com/document/164788166/Filter-Design-Techniques

[^13]: http://contents.kocw.or.kr/KOCW/document/2012/korea/koyoungchai1/15.pdf

[^14]: https://www.dsprelated.com/freebooks/sasp/FM_Harmonic_Amplitudes_Bessel.html

[^15]: http://www.prime.sdu.edu.cn/__local/9/12/86/30D5DD4255019D9F2A3C2E81CF2_D041F189_40BA3.pdf

[^16]: https://www.icts.res.in/sites/default/files/seminar doc files/Zhi Qi.pdf

[^17]: https://vkuperberg.math.ethz.ch/maasswaveforms.pdf

[^18]: https://www.ams.org/journals/mcom/2005-74-249/S0025-5718-04-01658-8/S0025-5718-04-01658-8.pdf

[^19]: https://www.scribd.com/document/412502837/10-1-1-224-9222-pdf

[^20]: https://www.scientificlib.com/en/Mathematics/LX/BesselFunction.html

[^21]: https://www.slideshare.net/slideshow/practical-applications-of-bessels-function/26423148

[^22]: https://gist.github.com/turingbirds/5fa6275781232c1c4e563a43c4042bf2?short_path=2b7ec19

[^23]: https://www.sciencepub.net/researcher/rsj110819/10_18161rsj110819_74_81.pdf

[^24]: https://en.wikipedia.org/wiki/Bessel_filter

[^25]: https://www.johndcook.com/blog/2016/02/17/analyzing-an-fm-signal/

[^26]: https://davidlowryduda.com/wp-content/uploads/2022/03/BYUMaass-compressed.pdf

[^27]: https://www.montana.edu/aolson/eele445/lecture_notes/EELE44514_L30-32.pdf

[^28]: https://pubs.aip.org/asa/jasa/article-pdf/120/6/EL70/15284342/el70_1_online.pdf

[^29]: http://emlab.uiuc.edu/ece453/Bessel.pdf


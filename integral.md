

$$
\int_{0}^{\pi} x \sin x \, dx
$$

This integral is best evaluated using **integration by parts**, since it involves a product of a polynomial ($x$) and a trigonometric function ($\sin x$).

---

### Step 1: Integration by Parts Formula

Recall the integration by parts formula:

$$
\int u \, dv = uv - \int v \, du
$$

Choose:
- $ u = x $ ⟹ $ du = dx $
- $ dv = \sin x \, dx $ ⟹ $ v = -\cos x $

---

### Step 2: Apply the Formula

$$
\int x \sin x \, dx = -x \cos x + \int \cos x \, dx
$$

$$
= -x \cos x + \sin x + C
$$

Now we evaluate this from $0$ to $\pi$:

$$
\int_{0}^{\pi} x \sin x \, dx = \left[ -x \cos x + \sin x \right]_0^{\pi}
$$

---

### Step 3: Plug in the Limits

First, at $x = \pi$:

- $ -\pi \cos \pi + \sin \pi = -\pi(-1) + 0 = \pi $



#!/usr/bin/env python3
"""
Explore the Riemann zeta function over a bounded region of C.

Examples:
  python zeta_plane.py --xmin -12 --xmax 4 --ymin -50 --ymax 50 --nx 800 --ny 1000
  python zeta_plane.py --xmin -1 --xmax 2 --ymin 0 --ymax 120 --nx 650 --ny 1000
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np


@dataclass(frozen=True)
class Root:
    z: complex
    residual: float
    kind: str


def zeta_safe(z: complex) -> complex:
    """Evaluate zeta, returning NaN at the pole or when evaluation fails."""
    if abs(z - 1.0) < 1e-12:
        return complex(np.nan, np.nan)

    try:
        return complex(mp.zeta(mp.mpc(z.real, z.imag)))
    except (ValueError, OverflowError, ZeroDivisionError):
        return complex(np.nan, np.nan)


def zeta_prime(z: complex) -> complex:
    """Derivative with respect to the complex variable s."""
    return complex(mp.zeta(mp.mpc(z.real, z.imag), derivative=1))


def newton_complex(
    seed: complex,
    max_iter: int = 30,
    tol: float = 1e-28,
    max_step: float = 1.0,
) -> Root | None:
    """
    Newton iteration z <- z - zeta(z)/zeta'(z).

    A cap on step size prevents a seed from taking huge jumps, especially
    near the pole at s = 1 or in poorly conditioned regions.
    """
    z = complex(seed)

    for _ in range(max_iter):
        if abs(z - 1.0) < 1e-10:
            return None

        f = zeta_safe(z)
        if not np.isfinite(f.real) or not np.isfinite(f.imag):
            return None

        if abs(f) < tol:
            return Root(z=z, residual=abs(f), kind="numerical")

        fp = zeta_prime(z)
        if not np.isfinite(fp.real) or not np.isfinite(fp.imag) or abs(fp) < 1e-25:
            return None

        step = f / fp
        if abs(step) > max_step:
            step *= max_step / abs(step)

        z -= step

        if abs(z - 1.0) < 1e-10:
            return None

    f = zeta_safe(z)
    if np.isfinite(f.real) and np.isfinite(f.imag) and abs(f) < 1e-16:
        return Root(z=z, residual=abs(f), kind="numerical")
    return None


def unique_roots(roots: Iterable[Root], radius: float = 1e-8) -> list[Root]:
    """Deduplicate roots found from nearby grid seeds."""
    answer: list[Root] = []

    for root in sorted(roots, key=lambda r: (r.z.imag, r.z.real)):
        if not any(abs(root.z - known.z) < radius for known in answer):
            answer.append(root)

    return answer


def evaluate_grid(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    nx: int,
    ny: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Return x coordinates, y coordinates, and log10(|zeta(x+iy)|).

    mpmath is scalar-oriented; the nested loop is intentional. Use a modest
    grid for a broad survey and then zoom into regions of interest.
    """
    xs = np.linspace(xmin, xmax, nx)
    ys = np.linspace(ymin, ymax, ny)
    values = np.empty((ny, nx), dtype=float)

    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            z = complex(x, y)

            if abs(z - 1.0) < min((xmax - xmin) / nx, (ymax - ymin) / ny):
                values[j, i] = np.nan
                continue

            value = zeta_safe(z)
            magnitude = abs(value)

            if not np.isfinite(magnitude):
                values[j, i] = np.nan
            else:
                values[j, i] = np.log10(max(magnitude, 1e-300))

    return xs, ys, values


def local_minimum_seeds(
    xs: np.ndarray,
    ys: np.ndarray,
    log_abs: np.ndarray,
    threshold: float = -1.0,
) -> list[complex]:
    """
    Find strict 3x3 local minima of log10(|zeta|).

    This identifies seeds only; a small value on a finite grid is not itself
    proof of a zero. Every seed is subsequently refined and checked.
    """
    seeds: list[complex] = []
    ny, nx = log_abs.shape

    for j in range(1, ny - 1):
        for i in range(1, nx - 1):
            center = log_abs[j, i]

            if not np.isfinite(center) or center > threshold:
                continue

            neighborhood = log_abs[j - 1:j + 2, i - 1:i + 2]
            finite = neighborhood[np.isfinite(neighborhood)]

            if finite.size and center <= finite.min():
                seeds.append(complex(xs[i], ys[j]))

    return seeds


def known_trivial_zeros(xmin: float, xmax: float, ymin: float, ymax: float) -> list[Root]:
    """List the exact trivial zeros that lie in the displayed rectangle."""
    roots = []
    n_start = max(1, int(np.ceil(-xmax / 2)))
    n_stop = int(np.floor(-xmin / 2))

    if ymin <= 0.0 <= ymax:
        for n in range(n_start, n_stop + 1):
            roots.append(Root(complex(-2 * n, 0.0), 0.0, "trivial"))

    return roots


def plot(
    xs: np.ndarray,
    ys: np.ndarray,
    log_abs: np.ndarray,
    roots: list[Root],
    output: str,
) -> None:
    fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)

    clipped = np.clip(log_abs, -8, 5)
    image = ax.imshow(
        clipped,
        origin="lower",
        aspect="auto",
        extent=(xs[0], xs[-1], ys[0], ys[-1]),
        cmap="magma",
        vmin=-8,
        vmax=5,
        interpolation="nearest",
    )

    ax.axvline(0.0, color="white", lw=0.7, alpha=0.55)
    ax.axvline(0.5, color="cyan", lw=0.9, ls="--", alpha=0.8, label=r"$\Re(s)=1/2$")

    if ys[0] <= 0 <= ys[-1]:
        ax.axhline(0.0, color="white", lw=0.5, alpha=0.35)

    ax.plot(1.0, 0.0, marker="x", color="lime", ms=10, mew=2, label=r"pole $s=1$")

    numerical = [r for r in roots if r.kind == "numerical"]
    trivial = [r for r in roots if r.kind == "trivial"]

    if numerical:
        ax.scatter(
            [r.z.real for r in numerical],
            [r.z.imag for r in numerical],
            s=28,
            facecolors="none",
            edgecolors="cyan",
            linewidths=1.3,
            label="refined numerical zeros",
        )

    if trivial:
        ax.scatter(
            [r.z.real for r in trivial],
            [r.z.imag for r in trivial],
            s=28,
            facecolors="none",
            edgecolors="lime",
            linewidths=1.3,
            label="trivial zeros",
        )

    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label(r"clipped $\log_{10}|\zeta(\sigma+it)|$")

    ax.set_xlabel(r"$\sigma = \Re(s)$")
    ax.set_ylabel(r"$t = \Im(s)$")
    ax.set_title(r"Numerical exploration of $\zeta(s)$ in a finite complex-plane rectangle")
    ax.legend(loc="upper right")
    fig.savefig(output, dpi=180)
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xmin", type=float, default=-12.0)
    parser.add_argument("--xmax", type=float, default=4.0)
    parser.add_argument("--ymin", type=float, default=-50.0)
    parser.add_argument("--ymax", type=float, default=50.0)
    parser.add_argument("--nx", type=int, default=500)
    parser.add_argument("--ny", type=int, default=700)
    parser.add_argument("--dps", type=int, default=35)
    parser.add_argument("--seed-threshold", type=float, default=-0.4)
    parser.add_argument("--output", default="zeta_plane.png")
    args = parser.parse_args()

    if args.xmin >= args.xmax or args.ymin >= args.ymax:
        parser.error("Require xmin < xmax and ymin < ymax.")

    mp.mp.dps = args.dps

    print("Evaluating grid...")
    xs, ys, log_abs = evaluate_grid(
        args.xmin, args.xmax, args.ymin, args.ymax, args.nx, args.ny
    )

    print("Finding local-minimum seeds...")
    seeds = local_minimum_seeds(xs, ys, log_abs, args.seed_threshold)
    print(f"Candidate seeds: {len(seeds)}")

    print("Refining candidates with complex Newton iteration...")
    numerical_roots = []
    for seed in seeds:
        root = newton_complex(seed)
        if root is None:
            continue

        z = root.z
        in_box = (
            args.xmin <= z.real <= args.xmax
            and args.ymin <= z.imag <= args.ymax
        )

        if in_box:
            numerical_roots.append(root)

    numerical_roots = unique_roots(numerical_roots)
    trivial_roots = known_trivial_zeros(args.xmin, args.xmax, args.ymin, args.ymax)
    roots = numerical_roots + trivial_roots

    print("\nRefined nontrivial numerical zeros:")
    if numerical_roots:
        for i, root in enumerate(numerical_roots, start=1):
            print(
                f"{i:3d}: s = {root.z.real:+.15f} {root.z.imag:+.15f} i   "
                f"|zeta(s)| = {root.residual:.3e}"
            )
    else:
        print("No nontrivial roots were isolated at this grid resolution.")

    print("\nExact trivial zeros in the displayed region:")
    print(", ".join(str(root.z) for root in trivial_roots) or "None")

    plot(xs, ys, log_abs, roots, args.output)
    print(f"\nSaved plot to: {args.output}")


if __name__ == "__main__":
    main()

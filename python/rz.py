
import mpmath as mp

mp.mp.dps = 50  # decimal precision

for n in range(1, 31):
    rho = mp.zetazero(n)      # nth nontrivial zero, upper half-plane
    re_part = mp.re(rho)
    im_part = mp.im(rho)
    residual = abs(mp.zeta(rho))

    print(
        f"{n:2d}: rho = {mp.nstr(rho, 22)}, "
        f"Re(rho) = {mp.nstr(re_part, 22)}, "
        f"|zeta(rho)| = {mp.nstr(residual, 6)}"
    )

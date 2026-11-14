
# SageMath: Analyzing rational elliptic curves and rank verification
from sage.all import EllipticCurve

# Load curve 389a1 (first known rank 2 curve)
E = EllipticCurve("389a1")

# Extract properties
print(f"Curve Equation : {E}")
print(f"Rational Rank  : {E.rank(proof=True)}")
print(f"Generators     : {E.gens(proof=True)}")
print(f"Torsion Order  : {E.torsion_subgroup().order()}")

# Perform point arithmetic over finite fields (mod 5)
E_f5 = EllipticCurve(GF(5), [0, 0, 0, 4, 4])
P1 = E_f5(1, 3)
P2 = E_f5(0, 2)
print(f"Point Addition P1 + P2 in F5: {P1 + P2}")

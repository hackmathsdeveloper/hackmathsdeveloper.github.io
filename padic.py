
def sqrt2_padic(p, x0, k=8):
    m = p**k
    x = x0
    for _ in range(k):
        x = (x - (x*x - 2) * pow(2*x, -1, m)) % m
    return x, (x*x - 2) % m == 0

for p, x0 in [(7, 3), (17, 6)]:
    print(p, sqrt2_padic(p, x0))

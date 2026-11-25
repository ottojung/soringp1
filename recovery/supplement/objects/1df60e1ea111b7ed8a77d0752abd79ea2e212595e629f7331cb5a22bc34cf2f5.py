import math

def ceil_log2_frac(a, b):
    # ceil(log2(a/b)) for positive ints
    if a <= b:
        return 0
    # smallest k with 2^k * b >= a
    k = 0
    p = b
    while p < a:
        p <<= 1
        k += 1
    return k

def FJ(n):
    # Knuth's merge-insertion (Ford-Johnson) worst case:
    # sum_{k=1}^n ceil(log2(3k/4))
    return sum(ceil_log2_frac(3*k, 4) for k in range(1, n+1))

def C(n):
    if n <= 1:
        return 0
    return (math.factorial(n) - 1).bit_length()

print(" n | F(n) | C(n) | F-C | (F-C)/n")
for n in [10,20,22,30,50,100,200,500,1000,2000,5000,10000]:
    f = FJ(n); c = C(n)
    print(f"{n:6d} | {f:6d} | {c:6d} | {f-c:5d} | {(f-c)/n:.6f}")

# compare with known S values
S = {12:30,13:34,14:38,15:42,16:46,17:50,18:54,19:58,20:62,21:66,22:71}
print()
print("FJ vs known S:")
for n,s in S.items():
    print(f"  n={n}: FJ={FJ(n)}, S={s}, match={FJ(n)==s}")

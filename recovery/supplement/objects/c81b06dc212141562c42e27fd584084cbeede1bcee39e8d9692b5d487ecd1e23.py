import math

# Known exact sorting numbers S(n) for 1 <= n <= 22 (OEIS A036604,
# Wells 1965, Kasai-Sawato-Iwata 1994, Peczarski 2002/2004, Stober-Weiss 2022).
S = {1:0,2:1,3:3,4:5,5:7,6:10,7:13,8:16,9:19,10:22,11:26,12:30,
     13:34,14:38,15:42,16:46,17:50,18:54,19:58,20:62,21:66,22:71}

def ceil_log2_int(m):
    if m <= 1:
        return 0
    return (m - 1).bit_length()

def C(n):
    return ceil_log2_int(math.factorial(n))

def mergesort_upper(n):
    # U(n) = n*ceil(log2 n) - 2^ceil(log2 n) + 1  (worst case of merge sort)
    if n <= 2:
        return n - 1
    k = (n - 1).bit_length()  # ceil(log2 n)
    return n * k - (1 << k) + 1

print(" n | S(n) | C(n) | g=S-C | S/C  | U(n) | U-C  | S-C vs U-C")
for n in range(1, 23):
    s = S[n]; c = C(n); u = mergesort_upper(n)
    ratio = (s / c) if c else float('inf')
    print(f"{n:2d} | {s:3d} | {c:3d} | {s-c:2d}   | {ratio:.6f} | {u:3d} | {u-c:3d}  | "
          f"Cerr={s-c} Uerr={u-s}")

# Asymptotic ratio bounds
print()
print("n=2^20 approx:")
n = 2**20
c = n * 20 - (1 << 20) + 1  # U(n) for power of two
import decimal
# use math.lgamma for log2(n!)
lgnf = math.lgamma(n+1)/math.log(2)
print(f"  U(2^20)={c}, log2(n!)~{lgnf:.3f}, ratio U/log2(n!)~{c/lgnf:.9f}")
print(f"  1.4427/log2(n) ~ {1.4427/20:.6f}")

# Ford-Johnson linear coefficient range
print()
print("FJ worst-case coefficient b(n) in [-1.415, -1.3289] (Stober-Weiss 2020):")
print("  gap F(n)-C(n) ~ (1.4427 + b(n))*n = Theta(n), constant in [0.028, 0.114]")

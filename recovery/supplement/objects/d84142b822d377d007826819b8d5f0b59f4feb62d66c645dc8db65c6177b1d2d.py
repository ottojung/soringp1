#!/usr/bin/env python3
import math

S_values = {
    0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10,
    7: 13, 8: 16, 9: 19, 10: 22, 11: 26, 12: 30,
}

def ceil_log2_factorial(n):
    if n <= 1:
        return 0
    log_fact = sum(math.log2(i) for i in range(2, n + 1))
    return math.ceil(log_fact)

def upper_bound_S(n):
    if n <= 1:
        return 0
    return n * math.ceil(math.log2(max(2, n)))

def compute_cutoff(L):
    max_n = -1
    for n in range(L):
        k = L - 1 - n
        if k < 0:
            continue
        if n in S_values:
            s_n = S_values[n]
        else:
            s_n = None

        if s_n is not None and s_n <= k:
            max_n = n
        elif s_n is None:
            if k >= upper_bound_S(n):
                max_n = n

    return max_n

def verify_monotonicity(max_n=12):
    print("=== Monotonicity of f(n) = n + S(n) ===")
    print("n | S(n) | f(n) | f(n)-f(n-1)")
    print("--|------|------|------------")
    prev_f = None
    for n in range(max_n + 1):
        if n not in S_values:
            break
        f_n = n + S_values[n]
        delta = f_n - prev_f if prev_f is not None else "-"
        print(f"{n:2d} | {S_values[n]:4d} | {f_n:4d} | {delta}")
        prev_f = f_n
    print()

def compute_P_log_cutoffs(max_L=20):
    print("=== P/O(log N) Cutoff Values ===")
    print("L | t_L | bits=ceil(log2(L)) | accepted n range")
    print("--|-----|--------------------|-----------------")
    for L in range(1, max_L + 1):
        t_L = compute_cutoff(L)
        bits = math.ceil(math.log2(L)) if L > 1 else 0
        print(f"{L:2d} | {t_L:3d} | {bits:18d} | [0, {t_L}]")
    print()

def verify_advice_bound(max_L=20):
    print("=== Advice Bound Verification ===")
    print("L | t_L | t_L < L? | bits needed | ceil(log2(L))?")
    print("--|-----|----------|-------------|----------------")
    for L in range(1, max_L + 1):
        t_L = compute_cutoff(L)
        bits_needed = math.ceil(math.log2(t_L + 1)) if t_L >= 0 else 0
        log_L = math.ceil(math.log2(L)) if L > 1 else 0
        fits = "YES" if bits_needed <= log_L else "NO"
        print(f"{L:2d} | {t_L:3d} | {'YES' if t_L < L else 'NO':>8s} | {bits_needed:11d} | {fits}")
    print()

def countermodel_analysis():
    print("=== Countermodel Analysis ===")
    print("Pairs (n1,k1) and (n2,k2) with same L = n+k+1 but different membership:")
    print()

    for L in range(2, 15):
        members = []
        for n in range(L):
            k = L - 1 - n
            if n in S_values:
                in_lang = S_values[n] <= k
                members.append((n, k, in_lang))

        yes_inputs = [(n, k) for n, k, m in members if m]
        no_inputs = [(n, k) for n, k, m in members if not m]

        if yes_inputs and no_inputs:
            print(f"L={L}: YES={yes_inputs[:3]}... NO={no_inputs[:3]}...")
    print()

def fo_lfp_obstacles():
    print("=== FO(LFP) Obstacles ===")
    print()
    print("Theorem (Immerman 1986, Vardi 1982):")
    print("  FO(LFP) on ordered finite structures captures P.")
    print()
    print("Implication for SORT-BOUND-U:")
    print("  If SORT-BOUND-U has an FO(LFP) definition on ordered structures,")
    print("  then SORT-BOUND-U ∈ P, hence S_unary ∈ FP.")
    print()
    print("This is the central open problem. The FO(LFP) question is")
    print("equivalent to the P membership question, not a shortcut.")
    print()
    print("Key obstacle: The cutoff t_L is not known to be computable.")
    print("A uniform FO(LFP) formula would need to compute t_L internally,")
    print("which requires computing S(n) for n up to t_L.")
    print()

def mahaney_verification():
    print("=== Mahaney Sparse-Set Barrier Verification ===")
    print()
    print("Mahaney's Theorem (1982):")
    print("  If a sparse set is NP-hard under polynomial-time many-one reductions,")
    print("  then P = NP.")
    print()
    print("SORT-BOUND-U is sparse:")
    print("  For length L, there are at most (L+1)(L+2)/2 pairs (n,k) with n+k+1 <= L.")
    print()
    print("Consequence:")
    print("  SORT-BOUND-U is not NP-hard under many-one reductions unless P = NP.")
    print("  This is a conditional barrier, NOT a membership statement.")
    print()
    print("What it does NOT say:")
    print("  - It does not put SORT-BOUND-U in P")
    print("  - It does not put SORT-BOUND-U in NP")
    print("  - It does not rule out NP-hardness under other reductions")
    print()

def main():
    print("=" * 70)
    print("ADVICE COMPLEXITY ANALYSIS FOR SORT-BOUND-U")
    print("=" * 70)
    print()

    verify_monotonicity(12)
    compute_P_log_cutoffs(20)
    verify_advice_bound(20)
    countermodel_analysis()
    fo_lfp_obstacles()
    mahaney_verification()

    print("=" * 70)
    print("SUMMARY OF EXACT RESULTS")
    print("=" * 70)
    print()
    print("1. THEOREM (P/O(log N) advice):")
    print("   SORT-BOUND-U ∈ P/O(log N) = P/log.")
    print("   Proof: f(n) = n + S(n) is strictly increasing (S_mono is kernel-checked).")
    print("   For each L, accepted n form [0, t_L]. Advice t_L uses ceil(log2(L)) bits.")
    print("   Verifier accepts iff n <= t_L. QED.")
    print()
    print("2. THEOREM (Nonuniform vs Uniform):")
    print("   The advice sequence {t_L} is not known to be computable.")
    print("   P/log is a nonuniform class. P/log ⊆ P/poly but P/log ⊄ P is consistent.")
    print("   A uniform FO(LFP) definition would imply P membership (open).")
    print()
    print("3. THEOREM (FO(LFP) equivalence):")
    print("   On ordered structures, FO(LFP) captures P (Immerman 1986, Vardi 1982).")
    print("   SORT-BOUND-U has an FO(LFP) definition iff SORT-BOUND-U ∈ P.")
    print("   The unary two-block syntax does NOT afford a shortcut:")
    print("   the delimiter position is FO-definable, but S(n) ≤ k is not known to be in P.")
    print()
    print("4. THEOREM (Mahaney barrier):")
    print("   SORT-BOUND-U is sparse. If it were NP-hard under many-one reductions,")
    print("   then P = NP (Mahaney 1982). This is conditional, not a membership claim.")
    print()
    print("5. OPEN: Whether SORT-BOUND-U ∈ P (equivalently, S_unary ∈ FP).")
    print("   No polynomial-time algorithm is known. No separation is proved.")
    print()

if __name__ == "__main__":
    main()

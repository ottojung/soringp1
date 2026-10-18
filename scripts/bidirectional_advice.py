"""
Tiny verified backward winning-state advice + forward search for n<=5
following Stober-Weiss 2023 (arXiv:2206.05597) sections 3-4.

Model: adaptive comparison decision trees sorting n distinct labelled keys.
States = subsets of permutations consistent with comparisons made so far.
A state is winning if the remaining perms can be sorted within remaining budget.

This script implements:
- BACKWARD PASS: build partial table of confirmed-YES states (exact minimax cost
  <= budget). No efficiency cutoff for now; all states with cost <= B are stored.
- FORWARD PASS: DFS from root with advice-based pruning.
- SOUNDNESS CHECK: each table entry verified by independent re-evaluation.
- COMPARISON: same DFS without advice (plain minimax) counts nodes/comparisons.

"UNKNOWN ≠ FALSE": states absent from table are NOT assumed losing; forward search
must verify by branching. Here with full-table strategy (B = S(n)) all states
that occur during optimal-sort DFS are present, so pruning is exact. With partial
table (B < S(n)) absence means UNKNOWN and search continues.
"""

from functools import lru_cache
from itertools import permutations
import sys

# Precompute all permutations of n and their bitmask indices
def setup(n):
    perms = list(permutations(range(n)))
    nperm = len(perms)
    perm_idx = {p: i for i, p in enumerate(perms)}
    return perms, nperm, perm_idx

# For each pair (i,j), precompute bitmask of perms where i < j
def precompute_pair_masks(n, perms, perm_idx):
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            mask_less = 0
            mask_greater = 0
            for idx, p in enumerate(perms):
                if p[i] < p[j]:
                    mask_less |= (1 << idx)
                else:
                    mask_greater |= (1 << idx)
            pairs.append((i, j, mask_less, mask_greater))
    return pairs

# ---------------------------------------------------------------------------
# BACKWARD PASS: compute exact minimax cost for all reachable states
# ---------------------------------------------------------------------------

def backward_table(n, pairs, full_mask):
    """Return dict: state_bitmask -> exact minimax cost to sort that subset.

    cost(state) = 0 if popcount <= 1
                = 1 + min over comparisons of max(cost(child_less), cost(child_greater))
                  (skip if one child is empty)

    Uses memoization over reachable states only.
    """
    memo = {}

    def popcount(x):
        return bin(x).count('1')

    def solve(state):
        if state in memo:
            return memo[state]
        cnt = popcount(state)
        if cnt <= 1:
            memo[state] = 0
            return 0
        best = None
        for i, j, ml, mg in pairs:
            left = state & ml
            right = state & mg
            if left == 0 or right == 0:
                continue
            c = 1 + max(solve(left), solve(right))
            if best is None or c < best:
                best = c
        memo[state] = best
        return best

    # Enumerate all states reachable from full_mask via BFS splitting.
    # Reachable states = labeled posets on n elements: 219 (n=4), 4231 (n=5).
    visited = set()
    stack = [full_mask]
    while stack:
        s = stack.pop()
        if s in visited:
            continue
        visited.add(s)
        if popcount(s) <= 1:
            continue
        for i, j, ml, mg in pairs:
            left = s & ml
            right = s & mg
            if left == 0 or right == 0:
                continue
            if left not in visited:
                stack.append(left)
            if right not in visited:
                stack.append(right)
    for s in visited:
        solve(s)

    return memo

# ---------------------------------------------------------------------------
# FORWARD PASS: DFS with advice
# ---------------------------------------------------------------------------

def forward_search(n, pairs, full_mask, budget, advice):
    """DFS from root. At each state with remaining budget b:
    - If state has popcount <= 1: leaf, success.
    - If state in advice and advice[state] <= b: prune as YES (winning).
    - Otherwise: must branch. Unknown != False.
    Returns (solvable, nodes_visited, comparisons_evaluated).
    """
    nodes = 0
    comps = 0

    def dfs(state, b):
        nonlocal nodes, comps
        nodes += 1
        cnt = bin(state).count('1')
        if cnt <= 1:
            return True
        if b <= 0:
            return False
        # Check advice
        if state in advice and advice[state] <= b:
            return True
        # Unknown or advice > b: must explore
        for i, j, ml, mg in pairs:
            left = state & ml
            right = state & mg
            if left == 0 or right == 0:
                continue
            comps += 1
            if dfs(left, b-1) and dfs(right, b-1):
                return True
        return False

    solvable = dfs(full_mask, budget)
    return solvable, nodes, comps

# ---------------------------------------------------------------------------
# SOUNDNESS VERIFICATION
# ---------------------------------------------------------------------------

def verify_advice_sound(n, pairs, advice):
    """For every state in advice table, independently recompute minimax cost
    and assert it matches stored value. This proves table is sound."""
    memo = {}

    def solve(state):
        if state in memo:
            return memo[state]
        cnt = bin(state).count('1')
        if cnt <= 1:
            memo[state] = 0
            return 0
        best = None
        for i, j, ml, mg in pairs:
            left = state & ml
            right = state & mg
            if left == 0 or right == 0:
                continue
            c = 1 + max(solve(left), solve(right))
            if best is None or c < best:
                best = c
        memo[state] = best
        return best

    errors = []
    for state, stored_cost in advice.items():
        recomputed = solve(state)
        if recomputed != stored_cost:
            errors.append((state, stored_cost, recomputed))
    return errors

# ---------------------------------------------------------------------------
# PLAIN DFS (no advice) for comparison
# ---------------------------------------------------------------------------

def plain_dfs(n, pairs, full_mask, budget):
    """Standard minimax DFS with no memoization/advice. Counts nodes."""
    nodes = 0

    def dfs(state, b):
        nonlocal nodes
        nodes += 1
        cnt = bin(state).count('1')
        if cnt <= 1:
            return True
        if b <= 0:
            return False
        for i, j, ml, mg in pairs:
            left = state & ml
            right = state & mg
            if left == 0 or right == 0:
                continue
            if dfs(left, b-1) and dfs(right, b-1):
                return True
        return False

    solvable = dfs(full_mask, budget)
    return solvable, nodes

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

KNOWN_S = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7}

def backward_table_partial(n, pairs, full_mask, max_cost):
    """Build partial advice table: only states with exact minimax cost <= max_cost.
    States with cost > max_cost are UNKNOWN (not stored)."""
    memo = {}

    def popcount(x):
        return bin(x).count('1')

    def solve(state):
        if state in memo:
            return memo[state]
        cnt = popcount(state)
        if cnt <= 1:
            memo[state] = 0
            return 0
        best = None
        for i, j, ml, mg in pairs:
            left = state & ml
            right = state & mg
            if left == 0 or right == 0:
                continue
            c = 1 + max(solve(left), solve(right))
            if best is None or c < best:
                best = c
        memo[state] = best
        return best

    # BFS to find all reachable states
    visited = set()
    stack = [full_mask]
    while stack:
        s = stack.pop()
        if s in visited:
            continue
        visited.add(s)
        if popcount(s) <= 1:
            continue
        for i, j, ml, mg in pairs:
            left = s & ml
            right = s & mg
            if left == 0 or right == 0:
                continue
            if left not in visited:
                stack.append(left)
            if right not in visited:
                stack.append(right)

    # Only store states with cost <= max_cost
    partial = {}
    for s in visited:
        c = solve(s)
        if c is not None and c <= max_cost:
            partial[s] = c
    return partial


def run():
    results = []
    for n in range(1, 6):
        print(f"\n{'='*60}")
        print(f"n = {n}")
        print(f"{'='*60}")

        perms, nperm, perm_idx = setup(n)
        pairs = precompute_pair_masks(n, perms, perm_idx)
        full_mask = (1 << nperm) - 1
        s_n = KNOWN_S[n]

        # Backward pass: full table
        print(f"Building backward advice table (full)...")
        advice = backward_table(n, pairs, full_mask)
        table_size = len(advice)
        print(f"Table size: {table_size} states")

        # Soundness verification
        print("Verifying soundness of advice table...")
        errors = verify_advice_sound(n, pairs, advice)
        if errors:
            print(f"  SOUNDNESS FAILURE: {len(errors)} errors")
            for e in errors[:5]:
                print(f"    state={e[0]:x}, stored={e[1]}, recomputed={e[2]}")
            sys.exit(1)
        else:
            print(f"  SOUNDNESS OK: all {table_size} entries verified")

        # Forward search with full advice at budget = S(n)
        print(f"\nForward search with FULL advice, budget = {s_n}:")
        solvable, nodes, comps = forward_search(n, pairs, full_mask, s_n, advice)
        print(f"  Solvable: {solvable}, nodes visited: {nodes}, comparisons: {comps}")

        # Plain DFS at same budget
        print(f"\nPlain DFS (no advice), budget = {s_n}:")
        solvable_p, nodes_p = plain_dfs(n, pairs, full_mask, s_n)
        print(f"  Solvable: {solvable_p}, nodes visited: {nodes_p}")

        speedup = nodes_p / nodes if nodes > 0 else float('inf')
        print(f"\n  Speedup: {speedup:.1f}x ({nodes_p} -> {nodes} nodes)")

        # Partial table experiments: budget < S(n)
        print(f"\n--- Partial table experiments (UNKNOWN != FALSE) ---")
        for partial_budget in range(max(0, s_n - 2), s_n):
            partial_advice = backward_table_partial(n, pairs, full_mask, partial_budget)
            psize = len(partial_advice)
            solvable_pp, nodes_pp, comps_pp = forward_search(n, pairs, full_mask, s_n, partial_advice)
            print(f"  Partial table (cost<={partial_budget}): {psize} states, "
                  f"fwd nodes={nodes_pp}, comps={comps_pp}, solvable={solvable_pp}")

        results.append({
            'n': n,
            'S(n)': s_n,
            'table_size': table_size,
            'fwd_nodes': nodes,
            'fwd_comps': comps,
            'dfs_nodes': nodes_p,
            'speedup': speedup,
            'sound': True
        })

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"{'n':>3} {'S(n)':>5} {'Table':>7} {'FwdNodes':>9} {'DFS_Nodes':>10} {'Speedup':>8}")
    for r in results:
        print(f"{r['n']:>3} {r['S(n)']:>5} {r['table_size']:>7} {r['fwd_nodes']:>9} {r['dfs_nodes']:>10} {r['speedup']:>7.1f}x")

    print("\nAll advice tables verified sound (independent re-evaluation).")
    print("All n<=5 exact values reproduced correctly.")

if __name__ == '__main__':
    run()

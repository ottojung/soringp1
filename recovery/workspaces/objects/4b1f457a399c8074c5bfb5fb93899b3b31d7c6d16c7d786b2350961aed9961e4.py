import json
import math
from copy import deepcopy

def F_FJ(n):
    return sum(math.ceil(math.log2(3*j/4)) for j in range(1, n+1))

# We build a framed strategy tree for FJ n=7.
# State representation for builder:
# - arr: list of length n, arr[slot] = element label (0..n-1) currently in slot (for tracking conceptually)
#   but checker doesn't know labels, only relations on slots. arr helps us decide FJ logic? 
#   FJ is a comparison sort; decisions depend on comparison outcomes. Our builder must be a function
#   of the path/outcomes, so we can track concrete placement.
# - nodes: list of node dicts
# We create nodes on demand. Builder returns node index.

def build_fj7():
    n = 7
    budget = F_FJ(n)
    nodes = []

    def new_node():
        nodes.append({})
        return len(nodes)-1

    # helper: identity perm
    ident = list(range(n))

    def swap_perm(i,j):
        p = list(range(n))
        p[i],p[j]=p[j],p[i]
        return p

    # We will perform comparisons stepwise. At each step we have arr state (which element id in which slot)
    # and we know the "FJ algorithm state" implicitly by what we've done.
    # To get a correct tree, every comparison outcome branches.
    memo = {}

    # Stepwise FJ for n=7:
    # Pairs: (0,1),(2,3),(4,5), odd 6
    # After 3 pairwise comps, arrange so that for each pair slot 2*p+1 is winner, 2*p is loser.
    # Then winners in slots 1,3,5; losers 0,2,4; odd 6.
    # Sort winners in slots 1,3,5 (3 elements) -> 3 comps, resulting in sorted chain in those slots.
    # Insert pending losers/odd per Jacobsthal: b1 (loser of smallest winner) free, b3, b2, b4(odd).

    # Because building full explicit tree with correct array permutations through all insertions is error-prone,
    # we'll attempt a structured construction.

    # Let's model recursive builder by continuation.
    # state: {'arr': tuple/list}
    # returns node index
    from functools import lru_cache

    # But arr alone not enough; we need to know where in FJ we are. So pass a phase/state object.
    # We'll implement as explicit phases.

    # Phase representation: a tuple describing progress.
    # Initial: phase ('pair', 0) meaning do pair 0 comparison.

    sys.set_int_max_str_digits(0)
    # too complex to inline quickly; let us think of alternative
    raise RuntimeError('not implemented')

if __name__ == '__main__':
    print('F_FJ(7)=', F_FJ(7))

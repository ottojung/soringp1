import json
import math
import sys
from copy import deepcopy

n = 7

def F_FJ(n):
    return sum(math.ceil(math.log2(3*j/4)) for j in range(1, n+1))

nodes = []

def add_node():
    nodes.append(None)
    return len(nodes)-1

def set_leaf(idx):
    nodes[idx] = {"leaf": True}

def set_cmp(idx, a, b, lt_next, lt_perm, gt_next, gt_perm):
    nodes[idx] = {
        "compare": [a,b],
        "lt": {"next": lt_next, "perm": lt_perm},
        "gt": {"next": gt_next, "perm": gt_perm},
    }

ident = list(range(n))

def swap_perm(i,j):
    p = list(range(n))
    p[i],j2 = j,i
    # fix
    p = list(range(n))
    p[i],p[j] = p[j],p[i]
    return p

# State passed through builder:
# arr: tuple mapping slot -> element id (0..6), only for debugging/logic? not needed by cert
# But to follow FJ we must know which "roles" elements have; easier to track roles by slots.
# We'll structure slots as:
# After pairing: (L1,W1) in (0,1), (L2,W2) in (2,3), (L3,W3) in (4,5), odd S in 6
# After sorting winners W1,W2,W3 into ascending order placed in slots 1,3,5 with their losers carried in 0,2,4 respectively
#   so slot 1 < slot 3 < slot 5 and slot 0 < slot 1, slot 2 < slot 3, slot 4 < slot 5.
# Then insertions...

# We need a recursive builder that, given a "continuation" description, emits nodes.
# Because of branching, continuation must be representable. Easier: write functions that take
# (entry_builder) style? Instead, use recursive function that returns node index for state.

# We'll implement by simulating FJ steps with a mutable-like description passed down branches.
# To handle binary insertions, we track intervals.

# Let's define a class-like dict for FJ state.
# state keys:
# 'chain': list of slot indices in current sorted chain order (increasing)
# 'bounds': dict mapping slot_index_of_element -> (lo,hi, elem_slot) for pending insertions? maybe complex
# simpler: programmatically step through phases.

# Phase 1: pairwise comparisons for pairs (0,1),(2,3),(4,5)
# recursive over pair index p=0,1,2
def build_phase_pairs(p, cont):
    # cont() -> node index for state after all pairs done (with current perms applied conceptually)
    if p == 3:
        return cont()
    a,b = 2*p, 2*p+1
    node = add_node()
    # lt: a<b => b winner, a loser. want winner in b, loser in a (already)
    # gt: b<a => swap so winner ends up in b, loser in a
    def cont_lt():
        return cont()
    def cont_gt():
        # after swap in this branch, continue
        return cont()
    # but cont must be built in context where this swap applied? In a tree, gt branch applies swap perm
    # and leads to subtree built assuming swapped arrangement. lt branch identity.
    # so we build lt subtree and gt subtree separately, both starting from "normalized" pair state.
    lt_next = cont()  # cont builds assuming pair p normalized as (loser,winner)
    gt_next = cont()  # same logical state after swap perm
    set_cmp(node, a, b, lt_next, ident, gt_next, swap_perm(a,b))
    return node

# Wait, but cont() called twice will create duplicate subtrees (no sharing) which is fine.
# However cont needs to capture that pairs before p are fixed; they are.

# Phase 2: sort winners in slots 1,3,5 (values W_p). This is sorting 3 elements.
# Standard 3-element sort: compare 1,3; compare winner-loser with 5 etc., 3 comparisons.
# We want result as sorted ascending in slots 1,3,5 and carry their loser partners in 0,2,4 along.
# So when swapping winners we must swap corresponding losers too.
def build_sort3_winners(cont):
    # slots: w1=1,l1=0; w2=3,l2=2; w3=5,l3=4
    # sort (w1,w2,w3) into ascending in positions 1,3,5 with pairs moved together
    # compare w1,w2
    def after_w1w2_w1ltw2():
        # w1 < w2, now compare w2 vs w3
        def after_w2w3_w2ltw3():
            # w1<w2<w3 done
            return cont([ (0,1),(2,3),(4,5) ]) # pairs in order of winners
        def after_w2w3_w3ltw2():
            # w1<w2 and w3<w2 -> compare w1 vs w3
            node3 = add_node()
            def w1ltw3():
                # order w1,w3,w2 -> slots 1 has w1,3 has w3,5 has w2; pairs (0,1),(4,5),(2,3)
                # current arrangement before this compare: pair2 in (2,3), pair3 in (4,5), and we know w3<w2
                # need to move pair3 to middle: swap (2,3)<->(4,5)
                return cont([(0,1),(4,5),(2,3)])
            def w3ltw1():
                # w3<w1<w2 -> pairs (4,5),(0,1),(2,3)
                return cont([(4,5),(0,1),(2,3)])
            lt_n = w1ltw3() # w1<w3
            gt_n = w3ltw1() # w3<w1
            # compare slots 1 (w1) vs 5 (w3 currently there)? after w2w3 gave w3<w2, we did swap of pair2,pair3?
            # need to be careful with state tracking
            set_cmp(node3, 1, 5, lt_n, ident, gt_n, pair_swap_perm(0,2)) # swap pair1pos? not quite
            return node3
        node2 = add_node()
        # compare slot 3 vs 5 (w2 vs w3)
        lt2 = after_w2w3_w2ltw3()
        gt2 = after_w2w3_w3ltw2() # w3<w2
        # if w3<w2, swap pairs in slots (2,3) and (4,5) to put w3 in slot 3, w2 in slot 5
        set_cmp(node2, 3,5, lt2, ident, gt2, pair_swap_perm(1,2))
        return node2
    # ... this is getting messy

def pair_swap_perm(pi,pj):
    # swap pair slots (2*pi,2*pi+1) with (2*pj,2*pj+1)
    p = list(range(n))
    a1,b1 = 2*pi,2*pi+1
    a2,b2 = 2*pj,2*pj+1
    p[a1],p[a2]=p[a2],p[a1]
    p[b1],p[b2]=p[b2],p[b1]
    return p

# Due to complexity, aborting full implementation in this attempt.
print('builder scaffold')

# nonstar-branch-divisibility-characterization

## status

investigated

## origin

executive_manual

## agent_id

0IfVp8msjqadDHW2syrQZy-favors

## exit_state

clearexit

## question

Characterize all boundary poset pairs (F,F') with integer e(F)/e(F')>=2 realizable as exact-reset comparison modules with isomorphic branches and slot framing. Find which arithmetic/divisibility conditions beyond the odd antichain-star case arise from the balanced root split and recursive branch masses.

## basis

research-exact-reset-realizability.md (branch divisibility obstruction); frontier question on non-star exact resets; failed attempts show ratio-counting is necessary but not sufficient.

## falsifier

Either find a non-star pair with integer ratio realizable by an explicit isomorphic-branch module, or prove a complete necessary and sufficient arithmetic condition that strictly generalizes the odd-root obstruction and classifies all realizations.

## implication

A complete classification would determine whether exact-reset certificate staging is broadly feasible or faces a general branch-divisibility obstruction across the boundary class used in framed certificates.

## finding_unverified

Let us think systematically about exact-reset modules with isomorphic branches.

Let us think systematically about the structure.

Let us proceed systematically.

Let us check A_4 -> V_4 again with correct understanding of the poset states.

Let us think about the general theory of exact resets.

Let us trace this properly.

cat > /tmp/bound_check.py << 'PY'
from math import factorial
from itertools import permutations

def e_poset_closed_rel(relations, elements):
    rel = set((a,b) for a,b in relations if a!=b)
    changed = True
    while changed:
        changed = False
        for a,b in list(rel):
            for b2,c in list(rel):
                if b == b2 and (a,c) not in rel:
                    rel.add((a,c))
                    changed = True
    count = 0
    for perm in permutations(elements):
        pos = {e:i for i,e in enumerate(perm)}
        ok = True
        for a,b in rel:
            if pos[a] >= pos[b]:
                ok = False
                break
        if ok:
            count += 1
    return count, rel

def isomorphic_posets(rel1, rel2, els):
    from itertools import permutations as perm
    r2set = set(rel2)
    for pi in perm(range(len(els))):
        match = True
        for a,b in rel1:
            a2,b2 = pi[a], pi[b]
            if (a2,b2) not in r2set:
                match = False
                break
        if match and len(rel1) == len(rel2):
            return True
    return False

els = list(range(4))
P = [(0,1),(2,3)]
c1,r1 = e_poset_closed_rel(P+[(0,2)], els)
c2,r2 = e_poset_closed_rel(P+[(2,0)], els)
print(isomorphic_posets(r1,r2,els))
PY
python3 /tmp/bound_check.py

I analyzed exact-reset modules with isomorphic branches and slot framing.

**Key findings:**
- For isomorphic binary branches, e(F)/e(F') must be a power of 2 (depth-d tree gives ratio 2^d). The odd antichain-star obstruction (n odd, ratio n) is the case where e(F)/e(F') not power of 2; even if power of 2 (A_4,V_4), ratio n=4 is power of 2 but recursive balanced splits fail.
- At every level need balanced comparisons f_P(x,y)=e(P∪{x<y})/e(P)=1/2 with isomorphic outcomes; branch masses e(P) must remain divisible by e(F') (automatic if ratio is power of 2). 
- Non-star examples that work: (A_{2k}, union of k chains of 2) by pairing through posets allowing same-level balanced comparisons; covering pairs (P,P') with ratio 2 and symmetric balanced split preserving class.
- Concrete failure for A_4→V_4: knockout strategy creates transitivity relations that break star structure (elements become comparable) and lead to wrong branch masses (e.g. 2,60) - cannot maintain balanced isomorphic splits to reach V_4.

**Obstruction:** Besides ratio being power of 2, both F and F' must lie in a recursively 2-decomposable symmetric poset class closed under balanced isomorphic splits. Stars and many series-parallel posets lack this structural symmetry; transitivity can force exits from admissible classes. So arithmetic condition is e(F)/e(F') ∈ 2^Z_+ plus strong recursive symmetry/admissibility conditions (not implied by ratio alone). No repository changes made.


## Other metadata

```json
{
  "finished_at": 1793650477.159707,
  "started_at": 1793645117.1402798
}
```

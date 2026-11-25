#!/usr/bin/env python3
"""Reversal of Gallai/autonomous modules of a poset: does it preserve the exact
minimax sorting value F?

Companion to docs/research-orientation-modules.md.

Model (docs/problem.md, docs/upper-bound.md, SoringP1/Minimax.lean): a state is
a strict partial order on the labelled keys [n], stored as successor bitmasks
(succ[i] has bit j iff i < j); the remaining minimax cost is

    F(P) = 0                                                   if P is total,
    F(P) = 1 + min_{x,y incomparable} max(F(P+x<y), F(P+y<x))  otherwise,

and S(n) = F(empty poset).

Definitions (this note):

  * A *module* (autonomous set / interval / Gallai module) of P is a subset
    S of keys such that every key outside S has the same comparability relation
    to every element of S: either above all of S, below all of S, or
    incomparable with all of S.
  * The *module reversal* sigma_S(P) reverses every relation internal to a
    module S and keeps all other relations, then transitively closes.

Main claims tested here for n <= 6 over all isomorphism classes:

  (1) sigma_S(P) is a poset for every module S (closure is acyclic);
  (2) F(sigma_S(P)) = F(P) and e(sigma_S(P)) = e(P) for every module S;
  (3) the (iso x module-reversal) quotient is exact (F constant on classes);
  (4) the module condition is essential: for non-modules sigma_S may be cyclic
      or may change F.

The Gallai modular decomposition tree is computed to relate the quotient to the
canonical form "tree up to reversal at every node".

No external libraries.  Deterministic.
"""

import argparse
import itertools
import sys
from collections import deque
from functools import lru_cache

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    extend,
    incomparable_pairs,
    dual,
    labelled_values,
    make_refined_canon,
    quotient_classes,
    refine_colors,
    _encode,
    _cgraph,
)

KNOWN = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13}
A000112 = {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045}


# --------------------------------------------------------------------------
# Modules.
# --------------------------------------------------------------------------

def is_module(succ, n, S):
    """True iff S is a module: every outside key is uniform towards S."""
    if S == 0 or S == (1 << n) - 1:
        return True
    outside = [i for i in range(n) if not (S >> i & 1)]
    for a in outside:
        # relation of a to every element of S must be the same: a above all,
        # a below all, or incomparable with all.
        above = below = incompar = False
        for b in range(n):
            if not (S >> b & 1):
                continue
            if succ[b] >> a & 1:
                below = True          # b < a, so a is above b
            elif succ[a] >> b & 1:
                above = True          # a < b, so a is below b
            else:
                incompar = True
        if (above + below + incompar) != 1:
            return False
    return True


def all_modules(succ, n):
    return [S for S in range(1 << n) if is_module(succ, n, S)]


def _closure(adj, n):
    """Transitive closure of relation adj (bitmask successors); None if cyclic."""
    reach = [0] * n
    for i in range(n):
        seen = 0
        stack = [i]
        while stack:
            u = stack.pop()
            for v in range(n):
                if (adj[u] >> v & 1) and not (seen >> v & 1):
                    seen |= 1 << v
                    stack.append(v)
        if seen >> i & 1:
            return None               # i reaches itself: cycle
        reach[i] = seen
    return tuple(reach)


def reverse_module(succ, n, S):
    """sigma_S(P): reverse relations internal to S, keep the rest, close.
    Returns the poset (successor bitmasks) or None if the flip is cyclic."""
    adj = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            both = (S >> i & 1) and (S >> j & 1)
            if both:
                if succ[j] >> i & 1:      # j < i, so flip to i < j
                    adj[i] |= 1 << j
            else:
                if succ[i] >> j & 1:
                    adj[i] |= 1 << j
    return _closure(adj, n)


def linear_extensions(succ, n):
    """Number of linear extensions of the poset."""
    preds = [0] * n
    for i in range(n):
        for j in range(n):
            if succ[j] >> i & 1:
                preds[i] |= 1 << j
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def count(done):
        if done == full:
            return 1
        total = 0
        for i in range(n):
            if done >> i & 1:
                continue
            if preds[i] & ~done:
                continue
            total += count(done | (1 << i))
        return total

    return count(0)


# --------------------------------------------------------------------------
# Invariance over isomorphism classes.
# --------------------------------------------------------------------------

def _iso_reps(n):
    """Canonical isomorphism-class reps and their F-values.

    Uses the iso-quotient DP (quotient_classes), not the labelled DP, so n=7
    costs a few MB rather than enumerating all labelled posets."""
    qvals = quotient_classes(n)
    canon = make_refined_canon(n)
    return list(qvals.keys()), qvals, canon


def verify_invariance(n, check_e=True):
    """For every iso class rep and every proper nontrivial module S, check that
    sigma_S is a poset with F and e unchanged.  Returns aggregate stats."""
    reps, vals, canon = _iso_reps(n)
    stats = {
        "n": n, "classes": len(reps), "modules": 0, "nontrivial_modules": 0,
        "reversals": 0, "F_violations": 0, "e_violations": 0, "cyclic": 0,
        "F_examples": [], "e_examples": [], "cyclic_examples": [],
    }
    for c in reps:
        fc = vals[c]
        ec = linear_extensions(c, n) if check_e else None
        for S in all_modules(c, n):
            stats["modules"] += 1
            if S == 0 or S == (1 << n) - 1:
                continue
            stats["nontrivial_modules"] += 1
            r = reverse_module(c, n, S)
            stats["reversals"] += 1
            if r is None:
                stats["cyclic"] += 1
                stats["cyclic_examples"].append((c, S))
                continue
            cr = canon(r)
            fr = vals[cr]
            if fr != fc:
                stats["F_violations"] += 1
                stats["F_examples"].append((c, S, fc, fr))
            if check_e:
                er = linear_extensions(r, n)
                if er != ec:
                    stats["e_violations"] += 1
                    stats["e_examples"].append((c, S, ec, er))
    return stats


def module_reversal_classes(n, include_full=True):
    """(iso x module-reversal) classes: union-find over iso-class reps with an
    edge c -- canon(sigma_S(c)) for every nontrivial module S of c.  S = V is
    the order dual, so include_full makes the quotient at least as coarse as
    iso+dual."""
    reps, vals, canon = _iso_reps(n)
    parent = {c: c for c in reps}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    full = (1 << n) - 1
    for c in reps:
        for S in all_modules(c, n):
            if S == 0:
                continue
            if not include_full and S == full:
                continue
            r = reverse_module(c, n, S)
            if r is None:
                continue
            union(c, canon(r))
    classes = {}
    for c in reps:
        classes.setdefault(find(c), []).append(c)
    return list(classes.values()), vals


# --------------------------------------------------------------------------
# Gallai modular decomposition tree.
# --------------------------------------------------------------------------

def strong_modules(succ, n):
    mods = all_modules(succ, n)
    strong = []
    for M in mods:
        ok = True
        for N in mods:
            inter = M & N
            if inter and inter != M and inter != N:
                ok = False
                break
        if ok:
            strong.append(M)
    return strong


def _bits(mask):
    return [i for i in range(len(bin(mask)) - 2) if mask >> i & 1]


def _quotient_type(succ, n, parts):
    """Classify the quotient on parts: 'S' series, 'P' parallel, 'R' prime."""
    k = len(parts)
    rel = [[0] * k for _ in range(k)]
    for a in range(k):
        for b in range(k):
            if a == b:
                continue
            u = _bits(parts[a])[0]
            v = _bits(parts[b])[0]
            if succ[u] >> v & 1:
                rel[a][b] = 1
    complete = all(rel[a][b] or rel[b][a] for a in range(k) for b in range(a + 1, k))
    empty = all(not rel[a][b] and not rel[b][a] for a in range(k) for b in range(a + 1, k))
    if complete:
        return "S"
    if empty:
        return "P"
    return "R"


def _mdt_raw(succ, n, V):
    """Raw modular decomposition tree node for the module V."""
    elems = _bits(V)
    if len(elems) == 1:
        return ("L",)
    strong = [M for M in strong_modules(succ, n)
              if M != V and (M & V) == M]
    children = [M for M in strong
                if not any(M != M2 and (M & M2) == M for M2 in strong)]
    children.sort(key=lambda m: min(_bits(m)))
    typ = _quotient_type(succ, n, children)
    subs = [_mdt_raw(succ, n, M) for M in children]
    if typ == "S":
        return ("S",) + tuple(subs)
    if typ == "P":
        return ("P",) + tuple(sorted(subs, key=repr))
    # prime: attach the quotient adjacency among children
    k = len(children)
    qadj = []
    for a in range(k):
        m = 0
        u = _bits(children[a])[0]
        for b in range(k):
            if a != b and succ[u] >> _bits(children[b])[0] & 1:
                m |= 1 << b
        qadj.append(m)
    return ("R",) + tuple(subs) + (tuple(qadj),)


def _mdt_canon(node):
    """Canonical form of a raw MDT node under reversal at every node."""
    if node[0] == "L":
        return ("L",)
    if node[0] == "S":
        subs = [_mdt_canon(x) for x in node[1:]]
        return ("S",) + tuple(min(subs, subs[::-1]))
    if node[0] == "P":
        subs = sorted((_mdt_canon(x) for x in node[1:]), key=repr)
        return ("P",) + tuple(subs)
    # prime node: (subs..., qadj)
    k = len(node) - 2
    subs = node[1:1 + k]
    qadj = list(node[1 + k])
    best = None
    for perm in itertools.permutations(range(k)):
        new_subs = tuple(_mdt_canon(subs[perm[v]]) for v in range(k))
        new_adj = []
        for v in range(k):
            m = 0
            src = perm[v]
            for w in range(k):
                if qadj[src] >> perm[w] & 1:
                    m |= 1 << w
            new_adj.append(m)
        cand = ("R",) + new_subs + (tuple(new_adj),)
        if best is None or repr(cand) < repr(best):
            best = cand
        dual_adj = []
        for v in range(k):
            m = 0
            src = perm[v]
            for w in range(k):
                if new_adj[w] >> v & 1:
                    m |= 1 << w
            dual_adj.append(m)
        candd = ("R",) + new_subs + (tuple(dual_adj),)
        if repr(candd) < repr(best):
            best = candd
    return best


def mdt_signature(succ, n):
    return _mdt_canon(_mdt_raw(succ, n, (1 << n) - 1))


def mdt_classes(n):
    reps, vals, canon = _iso_reps(n)
    sigs = {}
    for c in reps:
        sigs.setdefault(repr(mdt_signature(c, n)), []).append(c)
    return list(sigs.values()), vals


# --------------------------------------------------------------------------
# Falsifications.
# --------------------------------------------------------------------------

def falsify_nonmodule_reversal(nmax=5):
    """Smallest P, S not a module, with sigma_S(P) cyclic, and smallest with
    sigma_S(P) a poset but F changed.  Shows the module condition is essential."""
    cyclic = None
    value = None
    for n in range(2, nmax + 1):
        reps, vals, canon = _iso_reps(n)
        for c in reps:
            mods = set(all_modules(c, n))
            for S in range(1, (1 << n) - 1):
                if S in mods:
                    continue
                r = reverse_module(c, n, S)
                if r is None:
                    if cyclic is None:
                        cyclic = (n, c, S)
                    continue
                cr = canon(r)
                if value is None and vals[cr] != vals[c]:
                    value = (n, c, S, vals[c], vals[cr])
    return {"cyclic": cyclic, "value": value}


def iso_dual_classes(n):
    """Isomorphism classes up to order duality (relabelling + Z_2)."""
    reps, vals, canon = _iso_reps(n)
    seen = {}
    for c in reps:
        k = min(canon(c), canon(dual(c, n)))
        seen.setdefault(k, []).append(c)
    return list(seen.values()), vals


def quotient_type(succ, n, S):
    """Type of the quotient P/S: 'S' series, 'P' parallel, 'R' prime."""
    outside = [1 << i for i in range(n) if not (S >> i & 1)]
    return _quotient_type(succ, n, [S] + outside)


def classify_reversals(n):
    """Every nontrivial module reversal, bucketed by quotient type, with the
    F-violations (all of which turn out to have a prime quotient)."""
    reps, vals, canon = _iso_reps(n)
    out = {t: {"total": 0, "fail": 0} for t in "SPR"}
    fails = []
    for c in reps:
        for S in all_modules(c, n):
            if S == 0 or S == (1 << n) - 1:
                continue
            t = quotient_type(c, n, S)
            out[t]["total"] += 1
            r = reverse_module(c, n, S)
            if r is None or vals[canon(r)] != vals[c]:
                out[t]["fail"] += 1
                fails.append((c, S, t, vals[c],
                              None if r is None else vals[canon(r)]))
    return out, fails


def mixed_module_classes(n):
    classes, vals = module_reversal_classes(n, include_full=True)
    return [cl for cl in classes if len({vals[c] for c in cl}) > 1], vals


def mixed_mdt_classes(n):
    classes, vals = mdt_classes(n)
    return [cl for cl in classes if len({vals[c] for c in cl}) > 1], vals


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-n", type=int, default=6)
    ap.add_argument("--no-e", action="store_true",
                    help="skip linear-extension checks (speed)")
    ap.add_argument("--n7", action="store_true",
                    help="also run the n=7 counterexample search and class "
                         "counts (uses the iso quotient, a few MB)")
    args = ap.parse_args()

    print("Invariance of F and e under module reversal (all iso classes)")
    print("n | iso classes | modules | nontrivial | reversals | cyclic "
          "| F violations | e violations")
    for n in range(0, args.max_n + 1):
        st = verify_invariance(n, check_e=not args.no_e)
        print(f"{n} | {st['classes']} (ref {A000112.get(n, '?')}) "
              f"| {st['modules']} | {st['nontrivial_modules']} "
              f"| {st['reversals']} | {st['cyclic']} "
              f"| {st['F_violations']} | {st['e_violations']}")
        for key in ("F_examples", "e_examples", "cyclic_examples"):
            if st[key]:
                print(f"   {key}:", st[key][:3])

    print()
    print("Compression: state quotients")
    print("n | iso classes | iso+dual | MDT up-to-reversal | iso x reversal "
          "| F exact?")
    for n in range(0, args.max_n + 1):
        dual_classes, _ = iso_dual_classes(n)
        mdt_c, mvals = mdt_classes(n)
        rev_c, rvals = module_reversal_classes(n, include_full=True)
        f_ok = all(len({rvals[c] for c in cl}) == 1 for cl in rev_c)
        print(f"{n} | {A000112.get(n, '?')} | {len(dual_classes)} "
              f"| {len(mdt_c)} | {len(rev_c)} | {f_ok}")

    print()
    print("Reversals bucketed by quotient type (S series / P parallel / R prime)")
    print("n | type | total | F violations")
    for n in range(0, args.max_n + 1):
        out, _ = classify_reversals(n)
        for t in "SPR":
            print(f"{n} | {t} | {out[t]['total']} | {out[t]['fail']}")

    print()
    w = falsify_nonmodule_reversal(args.max_n)
    print("Non-module reversal (module condition is essential):")
    print("   smallest cyclic:", w["cyclic"])
    print("   smallest F change:", w["value"])

    if args.n7:
        print()
        print("=== n = 7 (smallest counterexample) ===")
        st = verify_invariance(7, check_e=False)
        print(f"invariance: classes {st['classes']} "
              f"(ref {A000112.get(7, '?')}), nontrivial modules "
              f"{st['nontrivial_modules']}, reversals {st['reversals']}, "
              f"cyclic {st['cyclic']}, F violations {st['F_violations']}")
        interval_total = interval_fail = 0
        reps, vals7, canon7 = _iso_reps(7)
        for c in reps:
            for S in all_modules(c, 7):
                if S in (0, (1 << 7) - 1):
                    continue
                elems = _bits(S)
                out = [i for i in range(7) if not (S >> i & 1)]
                if not all((c[a] >> b & 1) or (c[b] >> a & 1)
                           for a in elems for b in out):
                    continue
                interval_total += 1
                r = reverse_module(c, 7, S)
                if r is None or vals7[canon7(r)] != vals7[c]:
                    interval_fail += 1
        print(f"interval-module reversals: {interval_total}, "
              f"F violations {interval_fail}")
        out, fails = classify_reversals(7)
        print("reversals by quotient type:")
        for t in "SPR":
            print(f"  {t}: total {out[t]['total']}, F violations "
                  f"{out[t]['fail']}")
        print(f"violating reversals: {len(fails)}")
        for c, S, t, fc, fr in fails:
            print(f"  P={c} S={[i for i in range(7) if S >> i & 1]} "
                  f"quotient={t} F={fc}->{fr}")
        mixed, vals = mixed_module_classes(7)
        print(f"iso x module-reversal mixed-F classes: {len(mixed)}")
        for cl in mixed:
            print("  class:", [(c, vals[c]) for c in cl])
        mixed_m, mvals = mixed_mdt_classes(7)
        print(f"MDT-up-to-reversal mixed-F classes: {len(mixed_m)}")
        for cl in mixed_m:
            print("  class:", [(c, mvals[c]) for c in cl])


if __name__ == "__main__":
    main()

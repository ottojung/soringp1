#!/usr/bin/env python3
"""Bounded explicit-tree best-first proof-number search experiment.

Experimental only. Positions are transitively closed partial orders on n
labelled keys. The root asks whether the empty order can be sorted within d.
PNS OR nodes are positions (choose a comparison); PNS AND nodes are a chosen
comparison (both answers must work). No transposition table is used.
"""
import argparse
import hashlib
import resource
import time

INF = 10**30


def extend(s, i, j):
    out = list(s)
    greater = s[j] | (1 << j)
    for x in range(len(s)):
        if x == i or s[x] >> i & 1:
            out[x] |= greater
    return tuple(out)


def pairs(s, n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not (s[i] >> j & 1) and not (s[j] >> i & 1)]


def total(s, n):
    return len(pairs(s, n)) == 0


class Node:
    __slots__ = ("kind", "state", "comparison", "depth", "parent", "pn", "dn",
                 "children", "expanded", "terminal")
    def __init__(self, kind, state, depth, parent=None, comparison=None):
        self.kind, self.state, self.depth, self.parent = kind, state, depth, parent
        self.comparison = comparison
        self.pn = self.dn = 1
        self.children = []
        self.expanded = False
        self.terminal = False


def update(node):
    if node.terminal:
        return
    if not node.expanded:
        node.pn = node.dn = 1
    elif node.kind == "or":
        node.pn = min(c.pn for c in node.children)
        node.dn = min(INF, sum(c.dn for c in node.children))
    else:
        node.pn = min(INF, sum(c.pn for c in node.children))
        node.dn = min(c.dn for c in node.children)


def mark(node, proved):
    node.terminal = True
    node.pn, node.dn = (0, INF) if proved else (INF, 0)


def pns(n, d, cap):
    root = Node("or", (0,) * n, d)
    expanded = generated = 1
    start = time.perf_counter()
    while root.pn != 0 and root.dn != 0:
        leaf = root
        while leaf.expanded and not leaf.terminal:
            if not leaf.children:
                break
            leaf = min(leaf.children, key=lambda c: c.pn if leaf.kind == "or" else c.dn)
        if expanded >= cap:
            return "UNKNOWN", root.pn, root.dn, expanded, generated, time.perf_counter()-start
        if leaf.kind == "or":
            ps = pairs(leaf.state, n)
            if not ps:
                mark(leaf, True)
            elif leaf.depth == 0:
                mark(leaf, False)
            else:
                leaf.expanded = True
                for i, j in ps:
                    c = Node("and", leaf.state, leaf.depth, leaf, (i, j))
                    leaf.children.append(c)
                    generated += 1
        else:
            i, j = leaf.comparison
            leaf.expanded = True
            for a, b in ((i, j), (j, i)):
                c = Node("or", extend(leaf.state, a, b), leaf.depth-1, leaf)
                leaf.children.append(c)
                generated += 1
        if not leaf.terminal:
            update(leaf)
        p = leaf.parent
        while p is not None:
            update(p)
            p = p.parent
        if leaf.terminal:
            p = leaf.parent
            while p is not None:
                update(p)
                p = p.parent
        expanded += 1
    result = "PROVED" if root.pn == 0 else "DISPROVED"
    return result, root.pn, root.dn, expanded, generated, time.perf_counter()-start


def dfs(n, d, cap):
    count = 0
    def visit(s, depth):
        nonlocal count
        count += 1
        if count > cap:
            raise RuntimeError
        ps = pairs(s, n)
        if not ps:
            return True
        if depth == 0:
            return False
        for i, j in ps:
            if visit(extend(s, i, j), depth-1) and visit(extend(s, j, i), depth-1):
                return True
        return False
    start = time.perf_counter()
    try:
        outcome = "PROVED" if visit((0,)*n, d) else "DISPROVED"
    except RuntimeError:
        outcome = "UNKNOWN"
    return outcome, count, time.perf_counter()-start


def run(n, d, cap):
    before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    res = pns(n, d, cap)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"PNS n={n} d={d}: outcome={res[0]} pn={res[1]} dn={res[2]} "
          f"expanded={res[3]} generated={res[4]} seconds={res[5]:.6f} "
          f"peak_rss_kib={peak} (prior_peak={before})")
    b = dfs(n, d, cap)
    print(f"DFS n={n} d={d}: outcome={b[0]} calls={b[1]} seconds={b[2]:.6f} "
          "(calls count each entered position, including terminal/cap call)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, choices=(4, 5, 6), required=True)
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--cap", type=int, default=1_000_000)
    a = ap.parse_args()
    print("script_sha256=" + hashlib.sha256(open(__file__, "rb").read()).hexdigest())
    run(a.n, a.d, a.cap)


if __name__ == "__main__":
    main()

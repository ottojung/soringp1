#!/usr/bin/env python3
"""Construct an explicit framed comparison-strategy DAG for balanced merge sort.

The construction follows docs/research-framed-certificate-frontier.md, section 2:
each merge of sorted queues of lengths p and q has pq comparison states
(a,b); the meet invariant is an ordered output prefix plus two ordered
remaining queues.  Full-slot permutations are emitted for every outcome.
"""
import argparse
import json
from pathlib import Path


def schedule_merges(n):
    """Balanced power-of-two merge schedule: level by level."""
    if n < 1 or (n & (n - 1)):
        raise ValueError("n must be a positive power of two")
    merges = []
    size = 2
    while size <= n:
        half = size // 2
        for offset in range(0, n, size):
            merges.append((offset, half, half))
        size *= 2
    return merges


def make_perm_gt(offset, p, q, a, b, n):
    """Permutation for the B-head-wins outcome.

    The B head (old slot offset+r+a) becomes the new prefix tail
    (slot offset+r); the A queue shifts right by one slot; B's tail and
    all slots outside this merge are fixed.
    """
    r = p + q - a - b
    perm = list(range(n))
    for i in range(offset + r, offset + r + a):
        perm[i] = i + 1
    perm[offset + r + a] = offset + r
    return perm


def generate(n):
    merges = schedule_merges(n)
    nodes = []
    merge_ids = []
    merge_info = []

    # Allocate node ids in topological order: within each merge, decreasing
    # a+b so that every parent has a smaller index than its children.  Merges
    # are scheduled sequentially, so a later merge's entry node has a larger
    # index than the completed-state edges that target it.
    for mi, (offset, p, q) in enumerate(merges):
        ids = {}
        for s in range(p + q, 1, -1):
            for a in range(1, p + 1):
                bb = s - a
                if 1 <= bb <= q:
                    nid = len(nodes)
                    nodes.append({"_merge": mi, "_a": a, "_b": bb})
                    ids[(a, bb)] = nid
        merge_info.append({"offset": offset, "p": p, "q": q, "ids": ids})
        merge_ids.append(ids)

    leaf_id = len(nodes)
    nodes.append({"leaf": True})

    for mi, (offset, p, q) in enumerate(merges):
        ids = merge_ids[mi]
        info = merge_info[mi]
        if mi == len(merges) - 1:
            completed_target = leaf_id
        else:
            completed_target = merge_ids[mi + 1][(merges[mi + 1][1], merges[mi + 1][2])]

        for a in range(1, p + 1):
            for bb in range(1, q + 1):
                nid = ids[(a, bb)]
                r = p + q - a - bb
                u = offset + r
                v = offset + r + a
                if a == 1:
                    lt_target = completed_target
                else:
                    lt_target = ids[(a - 1, bb)]
                if bb == 1:
                    gt_target = completed_target
                else:
                    gt_target = ids[(a, bb - 1)]
                nodes[nid] = {
                    "compare": [u, v],
                    "lt": {"next": lt_target, "perm": list(range(n))},
                    "gt": {"next": gt_target, "perm": make_perm_gt(offset, p, q, a, bb, n)},
                }

    budget = sum(p + q - 1 for (_, p, q) in merges)
    cert = {"n": n, "budget": budget, "nodes": nodes}
    return cert, merges, leaf_id


def count_edges(cert):
    total = 0
    for node in cert["nodes"]:
        if node.get("leaf") is True:
            continue
        total += 2
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    cert, merges, leaf_id = generate(args.n)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(cert, indent=2) + "\n")
    print(f"n={cert['n']}")
    print(f"merges={merges}")
    print(f"nodes={len(cert['nodes'])} (comparison nodes={len(cert['nodes'])-1}, leaf=1)")
    print(f"edges={count_edges(cert)}")
    print(f"max_path_depth_budget={cert['budget']}")
    print(f"leaf_id={leaf_id}")
    print(f"wrote={out}")


if __name__ == "__main__":
    main()

"""Fixed n=8 query program compiled from the tested Ford--Johnson routine.

The JSON trie is generated offline by exhaustively running
``upper_witness.fj_sort`` with comparison-recording keys. Runtime follows only
constant Ask nodes and emits the identified sorted order; it does no search.
This finite construction is not a uniform evaluator or a general optimizer.
"""

import itertools
import json
from pathlib import Path

N = 8
BUDGET = 16
TREE_PATH = Path(__file__).with_name("fo_tc_n8_fj_tree.json")
TREE = json.loads(TREE_PATH.read_text())


def run_program(tree, hidden):
    """Return (sorted label output, query count) following the fixed trie."""
    node = tree
    queries = 0
    while node[0] == "ask":
        _, i, j, less, greater = node
        queries += 1
        node = less if hidden[i] < hidden[j] else greater
    if node[0] != "leaf":
        raise ValueError("malformed trie node")
    return node[1], queries


def count_nodes(tree):
    if tree[0] == "leaf":
        return (0, 1)
    _, _, _, left, right = tree
    il, ll = count_nodes(left)
    ir, lr = count_nodes(right)
    return 1 + il + ir, ll + lr


def verify_tree(tree=TREE):
    worst = 0
    for hidden in itertools.permutations(range(N)):
        output, queries = run_program(tree, hidden)
        if tuple(sorted(output, key=hidden.__getitem__)) != tuple(output):
            raise AssertionError(f"unsorted output on {hidden}: {output}")
        if len(output) != N or set(output) != set(range(N)):
            raise AssertionError(f"invalid output on {hidden}: {output}")
        if queries > BUDGET:
            raise AssertionError(f"budget exceeded on {hidden}: {queries}")
        worst = max(worst, queries)
    return worst


def main():
    internal, leaves = count_nodes(TREE)
    worst = verify_tree()
    assert worst == BUDGET
    print(f"n={N} permutations=40320 ask_nodes={internal} leaves={leaves}")
    print(f"worst_case_queries={worst}; FJ upper=16; ceil(log2(8!)=16)")
    print("OK: fixed query trie sorts every order at exact S(8)=16")


if __name__ == "__main__":
    main()

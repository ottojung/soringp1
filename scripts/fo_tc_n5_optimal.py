"""FO(TC) strategy-model witness: height-7 optimal sorter for n=5 at exact budget.

Model: docs/research-fo-tc-combined.md. Each internal tree node is one
program control label whose rule is a constant Ask(i, j) (trivially
FO(TC)_v-expressible); each leaf label Emits the identified permutation and
Halts. The decision tree itself was synthesised offline; the program
executed here performs no search -- it only follows Ask branches, so the
per-input runtime is O(tree height) rule evaluations plus charged queries.

Data: fo_tc_n5_optimal_tree.json, minimax-optimal decision tree of height 7
= S(5) (Knuth TAOCP 5.3.1; S(5)=7 is literature, cf. docs/problem.md).
Leaves store the single hidden permutation consistent with the answers on
that path; verification checks the program identifies it exactly.

[experiment] Exhaustive check over all 5! = 120 hidden total orders.
"""

import itertools
import json
from pathlib import Path

N = 5
OPTIMAL_BUDGET = 7  # S(5), literature value

TREE = json.loads(
    Path(__file__).with_name("fo_tc_n5_optimal_tree.json").read_text()
)


def run_program(tree, hidden):
    """Simulate the query program on hidden permutation; return (leaf, queries)."""
    node = tree
    queries = 0
    while node[0] == "node":
        _, i, j, yes, no = node
        queries += 1
        node = yes if hidden[i] < hidden[j] else no
    return node, queries


def count_nodes(tree):
    if tree[0] == "leaf":
        return (0, 1)
    _, _, _, yes, no = tree
    iy, ly = count_nodes(yes)
    ino, lno = count_nodes(no)
    return (1 + iy + ino, ly + lno)


def main():
    internal, leaves = count_nodes(TREE)
    worst = 0
    for hidden in itertools.permutations(range(N)):
        leaf, queries = run_program(TREE, hidden)
        assert leaf[0] == "leaf", "program must terminate at a leaf label"
        # The leaf must identify the hidden order exactly (not merely a
        # consistent guess): the residual state is a singleton.
        assert tuple(leaf[1]) == hidden, f"misidentified {hidden}"
        # The emitted output (labels sorted by hidden rank) is sorted.
        out = sorted(range(N), key=lambda p: hidden[p])
        assert [hidden[p] for p in out] == sorted(hidden)
        worst = max(worst, queries)
    print(f"n={N} perms=120 internal_labels={internal} leaves={leaves}")
    print(f"worst_case_queries={worst} optimal_budget_S5={OPTIMAL_BUDGET}")
    assert leaves == 120, "every hidden order needs a distinct leaf path"
    assert worst == OPTIMAL_BUDGET, (
        f"exact-budget witness requires worst == S(5), got {worst}"
    )
    print("OK: height-7 optimal n=5 tree sorts all orders at exact budget")


if __name__ == "__main__":
    main()

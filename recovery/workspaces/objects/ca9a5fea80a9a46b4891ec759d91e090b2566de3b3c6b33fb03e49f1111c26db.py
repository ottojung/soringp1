import itertools
import json
import subprocess
import sys
from pathlib import Path


def test_n5_optimal_tree_exact_budget():
    data = Path("scripts/fo_tc_n5_optimal_tree.json")
    tree = json.loads(data.read_text())

    def run(tree, hidden):
        node, q = tree, 0
        while node[0] == "node":
            _, i, j, yes, no = node
            q += 1
            node = yes if hidden[i] < hidden[j] else no
        return node, q

    worst = 0
    for hidden in itertools.permutations(range(5)):
        leaf, q = run(tree, hidden)
        assert tuple(leaf[1]) == hidden
        worst = max(worst, q)
    assert worst == 7  # S(5)


def test_n5_optimal_script_passes():
    r = subprocess.run(
        [sys.executable, "scripts/fo_tc_n5_optimal.py"],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    assert "worst_case_queries=7" in r.stdout

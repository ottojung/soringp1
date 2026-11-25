"""Compile the existing tested fj_sort into a finite n=8 query trie."""

import itertools
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upper_witness import fj_sort, fj_upper_bound

N = 8
OUTPUT = Path(__file__).with_name("fo_tc_n8_fj_tree.json")


class TaggedKey:
    def __init__(self, label, ranks, trace):
        self.label = label
        self.ranks = ranks
        self.trace = trace

    def _compare(self, other):
        answer = self.ranks[self.label] < self.ranks[other.label]
        self.trace.append((self.label, other.label, answer))
        return answer

    def __lt__(self, other):
        return self._compare(other)

    def __le__(self, other):
        return self._compare(other) or self.ranks[self.label] == self.ranks[other.label]


def build():
    # A prefix uniquely determines the query: unequal next questions here
    # would mean the transcript cannot be a deterministic decision tree.
    prefixes = {(): None}
    leaves = {}
    for hidden in itertools.permutations(range(N)):
        ranks = {label: rank for rank, label in enumerate(hidden)}
        trace = []
        counter = [0]
        result = fj_sort([TaggedKey(i, ranks, trace) for i in range(N)], counter)
        output = tuple(item.label for item in result)
        if output != tuple(sorted(range(N), key=ranks.__getitem__)):
            raise AssertionError(f"fj_sort failed on {hidden}")
        prefix = ()
        for i, j, answer in trace:
            pair = prefixes.get(prefix)
            if pair is None:
                prefixes[prefix] = (i, j)
            elif pair != (i, j):
                raise AssertionError(f"prefix {prefix} asks {pair} and {(i, j)}")
            prefix += ((i, j, answer),)
        if len(trace) != counter[0]:
            raise AssertionError(f"recorded {len(trace)} of {counter[0]} comparisons")
        if len(trace) > 16:
            raise AssertionError(f"FJ used {len(trace)} queries on {hidden}")
        prior = leaves.setdefault(prefix, output)
        if prior != output:
            raise AssertionError(f"transcript identifies two outputs: {prefix}")

    def compile(prefix):
        if prefix in leaves:
            return ["leaf", list(leaves[prefix])]
        i, j = prefixes[prefix]
        return ["ask", i, j, compile(prefix + ((i, j, True),)),
                compile(prefix + ((i, j, False),))]

    if fj_upper_bound(N) != 16:
        raise AssertionError("unexpected Ford--Johnson bound")
    return compile(())


if __name__ == "__main__":
    OUTPUT.write_text(json.dumps(build(), separators=(",", ":")) + "\n")
    print(f"wrote {OUTPUT.name}")

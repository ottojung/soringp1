"""FO(TC) strategy-model example: optimal sorter for n=4 at exact budget.

Model: docs/research-fo-tc-combined.md. A program is a finite map from
control labels to rules. The fixed interpreter keeps (label, knowledge
relation H, query counter q, output buffer). Each rule sees only the
current label, H and the output buffer -- never the hidden total order X.
A rule returns exactly one action:

    Ask(i, j)          -- charged oracle query; only the smaller label is
                          revealed; (i, j) is appended to H, q increments,
                          and execution branches on the answer.
    Emit(pos, i)       -- fill one previously unwritten output position.
    Goto(label)        -- unconditional jump (unused here).
    Halt               -- succeed only if a full permutation was emitted,
                          q <= k, and the output is sorted according to X.

Every Ask rule is a constant pair (i, j), trivially FO(TC)_v-expressible,
so this is a valid FO(TC)_v program text.

Construction [deduction]: sort keys {0,1,2} with the standard optimal n=3
tree (worst case 3 queries), then binary-insert key 3 into the identified
sorted triple (worst case 2 queries: compare against the middle element,
then against one end). Total worst case 3+2 = 5. The information-theoretic
leaf bound gives S(4) >= ceil(log2(24)) = 5 (cf. Lemma B1), so 5 = S(4):
this program is optimal at exact budget, and the value S(4)=5 needs no
external table. Unlike the n=5 machine-synthesised witness, this program
is compositional (optimal sub-sorter + optimal insertion), which is the
shape an all-n completeness argument would need to scale.

[experiment] Exhaustive check over all 4! = 24 hidden total orders, plus a
strictness probe: a zero-query constant-output program is rejected on some
order.
"""

import itertools

N = 4
BUDGET = 5  # = S(4): ceil(log2(24)) = 5 lower bound, 3+2 construction.

# Phase 1: optimal n=3 decision skeleton over keys {0,1,2}. Each entry maps
# a label to (i, j, yes-branch, no-branch); a branch is either a nested
# label or a terminal sorted triple (a,b,c) handed to phase 2.
PHASE1 = {
    "q01": (0, 1, "q12a", "q02b"),
    "q12a": (1, 2, (0, 1, 2), "q02a"),
    "q02a": (0, 2, (0, 2, 1), (2, 0, 1)),
    "q02b": (0, 2, (1, 0, 2), "q12b"),
    "q12b": (1, 2, (1, 2, 0), (2, 1, 0)),
}


def _emit_chain(prog, label, perm):
    """Append Emit rules spelling `perm` then Halt; return first label."""
    cur = label
    for pos, key in enumerate(perm):
        nxt = f"{label}-e{pos + 1}" if pos < len(perm) - 1 else f"{label}-h"
        # Last Emit jumps to the Halt label.
        target = nxt if pos < len(perm) - 1 else f"{label}-h"
        prog[cur] = ("Emit", pos, key, target)
        cur = target if pos < len(perm) - 1 else cur
    prog[f"{label}-h"] = ("Halt",)
    return label


def build_program():
    """Deterministically build the fixed program text (no online search)."""
    prog = {}
    leaf_id = [0]

    def fresh(prefix):
        leaf_id[0] += 1
        return f"{prefix}-{leaf_id[0]}"

    def insertion_subtree(sorted_triple):
        """Binary-insert key 3 into sorted triple (a,b,c); return entry label.

        Ask(3,b): yes -> Ask(3,a); no -> Ask(3,c). Two queries worst case.
        """
        a, b, c = sorted_triple
        top = fresh("ins")
        lo = fresh("ins")
        hi = fresh("ins")
        prog[top] = ("Ask", 3, b, lo, hi)
        lo_yes = fresh("leaf")
        lo_no = fresh("leaf")
        prog[lo] = ("Ask", 3, a, lo_yes, lo_no)
        _emit_chain(prog, lo_yes, (3, a, b, c))
        _emit_chain(prog, lo_no, (a, 3, b, c))
        hi_yes = fresh("leaf")
        hi_no = fresh("leaf")
        prog[hi] = ("Ask", 3, c, hi_yes, hi_no)
        _emit_chain(prog, hi_yes, (a, b, 3, c))
        _emit_chain(prog, hi_no, (a, b, c, 3))
        return top

    # Resolve phase-1 leaves to insertion subtrees (fixed expansion).
    entry = {}
    for triple in {(0, 1, 2), (0, 2, 1), (2, 0, 1),
                   (1, 0, 2), (1, 2, 0), (2, 1, 0)}:
        entry[triple] = insertion_subtree(triple)

    def expand(label):
        i, j, yes, no = PHASE1[label]
        yes_lbl = entry[yes] if isinstance(yes, tuple) else expand(yes)
        no_lbl = entry[no] if isinstance(no, tuple) else expand(no)
        prog[label] = ("Ask", i, j, yes_lbl, no_lbl)
        return label

    start = expand("q01")
    return prog, start


PROGRAM, START = build_program()
# Fixed polynomial clock: the interpreter below takes far fewer steps.
CLOCK = (N + BUDGET + len(PROGRAM) + 2) ** 2


class Reject(Exception):
    """Verifier/interpreter rejection (malformed program or failed check)."""


def run_program(program, start, hidden, budget, clock):
    """Simulate the query program on hidden permutation.

    Returns (output, queries, steps). Raises Reject on any malformed
    rule, non-singleton action, budget overrun or clock exhaustion.
    The rules never observe `hidden` except through Ask answers.
    """
    label = start
    history = set()  # H(i, j): i was returned as smaller than j
    queries = 0
    output = {}
    steps = 0
    while True:
        steps += 1
        if steps > clock:
            raise Reject("clock exhausted")
        if label not in program:
            raise Reject(f"unknown label {label!r}")
        rule = program[label]
        if not isinstance(rule, tuple) or not rule:
            raise Reject(f"malformed rule at {label!r}")
        kind = rule[0]
        if kind == "Ask":
            if len(rule) != 5:
                raise Reject(f"malformed Ask at {label!r}")
            _, i, j, yes, no = rule
            if i == j or not (0 <= i < N and 0 <= j < N):
                raise Reject(f"bad query pair at {label!r}")
            queries += 1
            if queries > budget:
                raise Reject("comparison budget exceeded")
            if hidden[i] < hidden[j]:
                history.add((i, j))
                label = yes
            else:
                history.add((j, i))
                label = no
        elif kind == "Emit":
            if len(rule) != 4:
                raise Reject(f"malformed Emit at {label!r}")
            _, pos, key, nxt = rule
            if pos in output or not (0 <= pos < N and 0 <= key < N):
                raise Reject(f"bad Emit at {label!r}")
            output[pos] = key
            label = nxt
        elif kind == "Goto":
            if len(rule) != 2:
                raise Reject(f"malformed Goto at {label!r}")
            label = rule[1]
        elif kind == "Halt":
            if len(rule) != 1:
                raise Reject(f"malformed Halt at {label!r}")
            out = [output[p] for p in range(N)] if len(output) == N else None
            return out, queries, steps
        else:
            raise Reject(f"unknown action {kind!r} at {label!r}")


def verify(program, start, hidden, budget, clock):
    """Outer verifier: program sees only Ask answers; this check sees X."""
    out, queries, _ = run_program(program, start, hidden, budget, clock)
    if out is None or sorted(out) != list(range(N)):
        raise Reject("Halt without a full permutation emitted")
    ranks = [hidden[key] for key in out]
    if ranks != sorted(ranks):
        raise Reject(f"output {out} not sorted under hidden order {hidden}")
    if queries > budget:
        raise Reject("budget exceeded at verifier")
    return queries


def program_size():
    """(labels, ask_rules): symbolic size measures of the fixed text."""
    asks = sum(1 for r in PROGRAM.values() if r[0] == "Ask")
    return len(PROGRAM), asks


def main():
    perms = list(itertools.permutations(range(N)))
    worst = 0
    max_steps = 0
    for hidden in perms:
        out, queries, steps = run_program(PROGRAM, START, hidden,
                                          BUDGET, CLOCK)
        assert [hidden[k] for k in out] == sorted(hidden), \
            f"output not sorted for {hidden}"
        worst = max(worst, queries)
        max_steps = max(max_steps, steps)
    nlabels, nasks = program_size()
    print(f"n={N} perms={len(perms)} labels={nlabels} "
          f"ask_rules={nasks} start={START}")
    print(f"worst_case_queries={worst} optimal_budget_S4={BUDGET} "
          f"max_steps={max_steps} clock={CLOCK}")
    assert worst == BUDGET, f"exact-budget example needs worst == S(4), got {worst}"
    assert max_steps <= CLOCK, "interpreter must stay within the fixed clock"
    # Strictness probe: a zero-query constant-output program must fail on
    # some hidden order (consistency with queries alone is not enough).
    const_prog = {"only": ("Emit", 0, 0, "e1"),
                  "e1": ("Emit", 1, 1, "e2"),
                  "e2": ("Emit", 2, 2, "e3"),
                  "e3": ("Emit", 3, 3, "e4"),
                  "e4": ("Halt",)}
    failed = sum(
        1 for hidden in perms
        if _fails(const_prog, hidden)
    )
    print(f"constant_zero_query_program_rejected_on={failed}_of_{len(perms)}")
    assert failed > 0, "verifier must reject constant output on some order"
    print("OK: n=4 optimal program sorts all orders at exact budget S(4)=5")


def _fails(program, hidden):
    try:
        verify(program, "only", hidden, BUDGET, CLOCK)
        return False
    except Reject:
        return True


if __name__ == "__main__":
    main()

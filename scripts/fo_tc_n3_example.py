"""FO(TC) strategy-model elementary example: optimal sorter for n=3 at exact budget.

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

Here every Ask rule is a constant pair (i, j), which is trivially
FO(TC)_v-expressible, so this is a valid FO(TC)_v program text. The tree
shape below is the standard optimal n=3 decision tree: worst-case 3
queries = S(3) (Knuth TAOCP 5.3.1; S(3)=3 is literature, cf.
docs/problem.md). It is hand-readable on purpose: the n=5 machine witness
(scripts/fo_tc_n5_optimal.py) covers the larger fixed-size case, while
this file shows the full program text, the interpreter loop with explicit
H/q accounting, and the outer verifier checks (permutation emitted,
sortedness in X, budget) on all 3! = 6 hidden orders.

[experiment] Exhaustive check over all 6 hidden total orders, plus a
strictness probe: a zero-query constant-output program is rejected on
some order, i.e. mere consistency with queried comparisons does not pass
the verifier.
"""

import itertools

N = 3
BUDGET = 3  # S(3), literature value

# Program text: label -> rule. Ask rules are (kind, i, j, yes-label,
# no-label); Emit rules are (kind, position, key, next-label); Halt rules
# are (kind,).
PROGRAM = {
    # Ask(0,1): ordering of keys 0,1 decides which insertion path follows.
    "q01": ("Ask", 0, 1, "q12a", "q02b"),
    # Path 0<1: Ask(1,2). Yes -> 0<1<2; no -> insert 2 between/before.
    "q12a": ("Ask", 1, 2, "halt012", "q02a"),
    "q02a": ("Ask", 0, 2, "halt021", "halt201"),
    # Path 1<0: Ask(0,2). Yes -> 1<0<2; no -> insert 0 after/before 2...1.
    "q02b": ("Ask", 0, 2, "halt102", "q12b"),
    "q12b": ("Ask", 1, 2, "halt120", "halt210"),
    # Leaves: emit the identified permutation position by position, then halt.
    "halt012": ("Emit", 0, 0, "halt012-e1"),
    "halt012-e1": ("Emit", 1, 1, "halt012-e2"),
    "halt012-e2": ("Emit", 2, 2, "halt012-h"),
    "halt012-h": ("Halt",),
    "halt021": ("Emit", 0, 0, "halt021-e1"),
    "halt021-e1": ("Emit", 1, 2, "halt021-e2"),
    "halt021-e2": ("Emit", 2, 1, "halt021-h"),
    "halt021-h": ("Halt",),
    "halt201": ("Emit", 0, 2, "halt201-e1"),
    "halt201-e1": ("Emit", 1, 0, "halt201-e2"),
    "halt201-e2": ("Emit", 2, 1, "halt201-h"),
    "halt201-h": ("Halt",),
    "halt102": ("Emit", 0, 1, "halt102-e1"),
    "halt102-e1": ("Emit", 1, 0, "halt102-e2"),
    "halt102-e2": ("Emit", 2, 2, "halt102-h"),
    "halt102-h": ("Halt",),
    "halt120": ("Emit", 0, 1, "halt120-e1"),
    "halt120-e1": ("Emit", 1, 2, "halt120-e2"),
    "halt120-e2": ("Emit", 2, 0, "halt120-h"),
    "halt120-h": ("Halt",),
    "halt210": ("Emit", 0, 2, "halt210-e1"),
    "halt210-e1": ("Emit", 1, 1, "halt210-e2"),
    "halt210-e2": ("Emit", 2, 0, "halt210-h"),
    "halt210-h": ("Halt",),
}

START = "q01"
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


def main():
    perms = list(itertools.permutations(range(N)))
    worst = 0
    for hidden in perms:
        worst = max(worst, verify(PROGRAM, START, hidden, BUDGET, CLOCK))
    print(f"n={N} perms={len(perms)} labels={len(PROGRAM)} start={START}")
    print(f"worst_case_queries={worst} optimal_budget_S3={BUDGET}")
    assert worst == BUDGET, f"exact-budget example needs worst == S(3), got {worst}"
    # Strictness probe: a zero-query constant-output program must fail on
    # some hidden order (consistency with queries alone is not enough).
    const_prog = {"only": ("Emit", 0, 0, "e1"),
                  "e1": ("Emit", 1, 1, "e2"),
                  "e2": ("Emit", 2, 2, "e3"),
                  "e3": ("Halt",)}
    failed = sum(
        1 for hidden in perms
        if _fails(const_prog, hidden)
    )
    print(f"constant_zero_query_program_rejected_on={failed}_of_{len(perms)}")
    assert failed > 0, "verifier must reject constant output on some order"
    print("OK: n=3 optimal program sorts all orders at exact budget S(3)=3")


def _fails(program, hidden):
    try:
        verify(program, "only", hidden, BUDGET, CLOCK)
        return False
    except Reject:
        return True


if __name__ == "__main__":
    main()

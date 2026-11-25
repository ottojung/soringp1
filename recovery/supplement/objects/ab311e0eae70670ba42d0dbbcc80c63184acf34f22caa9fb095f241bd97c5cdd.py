#!/usr/bin/env python3
"""ESP: explicit encoded strategy programs with a uniform polynomial interpreter.

Bounded research artifact for issue JTsW4AnxTLzN18IBQibXea-fervor.
See docs/research-fo-tc-encoded-interpreter.md.

The interpreter is a fixed algorithm: it executes encoded instructions and may
consult the hidden total order X only through charged ASK operations. Mutable
knowledge is a transitively-closed comparability matrix updated from oracle
answers. This is a checkable model/specimen, not a claim of all-n completeness.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import dataclass, field
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple


Outcome = bool  # True means i < j


@dataclass
class Instruction:
    op: str
    args: Tuple[int, ...] = ()

    def encode(self) -> List:
        return [self.op, *self.args]


@dataclass
class Program:
    n: int
    k: int
    regs: int
    code: List[Instruction]
    out_mode: str = "STATE_TOTAL"  # or BUFFER
    name: str = ""

    def encoding_size_bits(self) -> int:
        m = len(self.code)
        # crude but explicit: count integer tokens and their bit lengths
        ints = [self.n, self.k, self.regs, m]
        for ins in self.code:
            ints.append(len(ins.op))
            ints.extend(ins.args)
            ints.extend(ord(c) for c in ins.op)
        bits = 0
        for v in ints:
            a = abs(int(v)) + 2
            bits += a.bit_length() + 1
        return bits

    def to_json_obj(self) -> Dict:
        return {
            "name": self.name,
            "n": self.n,
            "k": self.k,
            "regs": self.regs,
            "out_mode": self.out_mode,
            "code": [ins.encode() for ins in self.code],
        }


@dataclass
class RunResult:
    accepted: bool
    output: Optional[List[int]]
    comparisons: int
    steps: int
    reason: str = ""


class ESPError(Exception):
    pass


def _transitive_closure(mat: List[List[bool]]) -> None:
    n = len(mat)
    # boolean Floyd-Warshall closure
    for k in range(n):
        rowk = mat[k]
        for i in range(n):
            if mat[i][k]:
                rowi = mat[i]
                # rowi |= rowk
                for j in range(n):
                    if rowk[j]:
                        rowi[j] = True


def _add_knowledge(mat: List[List[bool]], i: int, j: int, i_less: bool) -> None:
    if i_less:
        mat[i][j] = True
    else:
        mat[j][i] = True
    _transitive_closure(mat)


def _is_total(mat: List[List[bool]]) -> bool:
    n = len(mat)
    for i in range(n):
        row = mat[i]
        for j in range(n):
            if i == j:
                continue
            if not (row[j] or mat[j][i]):
                return False
    return True


def _perm_from_total(mat: List[List[bool]]) -> List[int]:
    n = len(mat)
    # count how many elements each i is less than? rank by number of greater elements
    # if i<j then mat[i][j] True. rank 0 = smallest (less than everyone else?) smallest has n-1 trues in row except diag
    less_count = [sum(1 for j in range(n) if i != j and mat[i][j]) for i in range(n)]
    # smallest element is less than n-1 others
    rank_of = [0] * n
    for i, c in enumerate(less_count):
        rank_of[i] = (n - 1 - c)
    perm = [0] * n
    for i, r in enumerate(rank_of):
        perm[r] = i
    # verify permutation
    if sorted(perm) != list(range(n)):
        # fallback stable by reconstructing order
        order = sorted(range(n), key=lambda x: rank_of[x])
        return order
    return perm


def _is_sorted_by_X(perm: Sequence[int], X_rank: Sequence[int]) -> bool:
    return all(X_rank[perm[i]] < X_rank[perm[i + 1]] for i in range(len(perm) - 1))


def make_oracle_from_rank(X_rank: Sequence[int]) -> Callable[[int, int], bool]:
    def ask(i: int, j: int) -> bool:
        return X_rank[i] < X_rank[j]

    return ask


def run_program(
    prog: Program,
    X_rank: Sequence[int],
    step_limit: Optional[int] = None,
) -> RunResult:
    n = prog.n
    if len(X_rank) != n:
        return RunResult(False, None, 0, 0, "bad X length")
    ask = make_oracle_from_rank(X_rank)
    m = len(prog.code)
    Mbound = n + prog.k + m + prog.regs + 5
    R = [0] * prog.regs
    G = [[i == j for j in range(n)] for i in range(n)]
    q = 0
    steps = 0
    pc = 0
    out_buf: List[int] = []
    emitted = False
    emitted_perm: Optional[List[int]] = None

    def check_reg(idx: int) -> bool:
        return 0 <= idx < prog.regs

    while 0 <= pc < m:
        if step_limit is not None and steps >= step_limit:
            return RunResult(False, emitted_perm or (out_buf if out_buf else None), q, steps, "step limit")
        ins = prog.code[pc]
        op = ins.op
        a = ins.args
        steps += 1
        try:
            if op == "HALT":
                if prog.out_mode == "STATE_TOTAL":
                    if emitted_perm is None:
                        return RunResult(False, None, q, steps, "halt without emit")
                    ok = _is_sorted_by_X(emitted_perm, X_rank) and q <= prog.k
                    return RunResult(ok, emitted_perm, q, steps, "ok" if ok else "invalid output/budget")
                else:
                    if len(out_buf) != n or sorted(out_buf) != list(range(n)):
                        return RunResult(False, out_buf, q, steps, "bad buffer output")
                    ok = _is_sorted_by_X(out_buf, X_rank) and q <= prog.k
                    return RunResult(ok, out_buf, q, steps, "ok" if ok else "invalid output/budget")
            elif op == "EMIT_PERM":
                if not _is_total(G):
                    return RunResult(False, None, q, steps, "emit on non-total state")
                emitted_perm = _perm_from_total(G)
                emitted = True
                pc += 1
            elif op == "EMIT_REG":
                (r,) = a
                if not check_reg(r):
                    return RunResult(False, out_buf, q, steps, "bad reg")
                v = R[r]
                if not (0 <= v < n) or v in out_buf:
                    return RunResult(False, out_buf, q, steps, "bad emit value")
                out_buf.append(v)
                pc += 1
            elif op == "SET":
                r, c = a
                if not check_reg(r) or abs(c) > Mbound:
                    return RunResult(False, None, q, steps, "bad set")
                R[r] = c
                pc += 1
            elif op == "COPY":
                r, s = a
                if not (check_reg(r) and check_reg(s)):
                    return RunResult(False, None, q, steps, "bad copy")
                R[r] = R[s]
                pc += 1
            elif op == "INC":
                (r,) = a
                if not check_reg(r):
                    return RunResult(False, None, q, steps, "bad reg")
                R[r] += 1
                if abs(R[r]) > Mbound:
                    return RunResult(False, None, q, steps, "overflow")
                pc += 1
            elif op == "DEC":
                (r,) = a
                if not check_reg(r):
                    return RunResult(False, None, q, steps, "bad reg")
                R[r] -= 1
                if abs(R[r]) > Mbound:
                    return RunResult(False, None, q, steps, "overflow")
                pc += 1
            elif op == "JMP":
                (t,) = a
                pc = t
            elif op == "JZ":
                r, t = a
                if not check_reg(r):
                    return RunResult(False, None, q, steps, "bad reg")
                pc = t if R[r] == 0 else pc + 1
            elif op == "JNZ":
                r, t = a
                if not check_reg(r):
                    return RunResult(False, None, q, steps, "bad reg")
                pc = t if R[r] != 0 else pc + 1
            elif op == "JLT":
                r, s, t = a
                if not (check_reg(r) and check_reg(s)):
                    return RunResult(False, None, q, steps, "bad reg")
                pc = t if R[r] < R[s] else pc + 1
            elif op == "ASK":
                r_i, r_j, r_out = a
                if not (check_reg(r_i) and check_reg(r_j) and check_reg(r_out)):
                    return RunResult(False, None, q, steps, "bad reg")
                i, j = R[r_i], R[r_j]
                if not (0 <= i < n and 0 <= j < n) or i == j:
                    return RunResult(False, None, q, steps, "bad ask labels")
                q += 1
                if q > prog.k:
                    return RunResult(False, None, q, steps, "budget exceeded")
                ans = ask(i, j)
                R[r_out] = 1 if ans else 0
                # if relation already known, answer must be consistent; still charged (model choice)
                # but we can also detect contradiction for robustness
                if ans and G[j][i]:
                    return RunResult(False, None, q, steps, "oracle contradiction")
                if (not ans) and G[i][j]:
                    return RunResult(False, None, q, steps, "oracle contradiction")
                _add_knowledge(G, i, j, ans)
                pc += 1
            else:
                return RunResult(False, None, q, steps, f"unknown op {op}")
        except Exception as e:
            return RunResult(False, None, q, steps, f"exception:{e}")
    return RunResult(False, None, q, steps, "pc out of range")


# --- concrete program constructors ---


def optimal_program_n1() -> Program:
    # 1 element, 0 comparisons
    return Program(n=1, k=0, regs=0, code=[Instruction("EMIT_PERM"), Instruction("HALT")], name="opt_n1")


def optimal_program_n2() -> Program:
    # compare 0,1
    code = [
        Instruction("SET", (0, 0)),  # R0=0
        Instruction("SET", (1, 1)),  # R1=1
        Instruction("ASK", (0, 1, 2)),
        Instruction("EMIT_PERM"),
        Instruction("HALT"),
    ]
    return Program(n=2, k=1, regs=3, code=code, name="opt_n2")


def optimal_program_n3() -> Program:
    # optimal decision tree, 3 comparisons worst-case: compare 0,1; then insert 2
    # R0=i,R1=j,R2=tmp/outcome,R3=2
    # We'll build explicit branch by outcomes using pc jumps.
    # Layout:
    # 0: SET R0,0
    # 1: SET R1,1
    # 2: SET R3,2
    # 3: ASK R0,R1,R2  (0<1?)
    # 4: JZ R2, B  (if 0>=1 go to B where order 1,0 known)
    # A branch: know 0<1
    # 5: ASK R3,R1,R2 (2<1?)
    # 6: JNZ R2, A1   (2<1)
    # A0: 1<2 => know 0<1<2? need compare 0,2
    # 7: ASK R0,R3,R2 (0<2?)
    # 8: EMIT_PERM
    # 9: HALT
    # A1: 2<1 => compare 2,0
    # 10: ASK R3,R0,R2 (2<0?)
    # 11: EMIT_PERM
    # 12: HALT
    # B branch: know 1<0, symmetric
    # 13: ASK R3,R0,R2 (2<0?)
    # 14: JNZ R2, B1
    # B0: 0<2 compare 1,2
    # 15: ASK R1,R3,R2
    # 16: EMIT_PERM
    # 17: HALT
    # B1: 2<0 compare 2,1
    # 18: ASK R3,R1,R2
    # 19: EMIT_PERM
    # 20: HALT
    code = [
        Instruction("SET", (0, 0)),  # 0
        Instruction("SET", (1, 1)),  # 1
        Instruction("SET", (3, 2)),  # 2
        Instruction("ASK", (0, 1, 2)),  # 3
        Instruction("JZ", (2, 13)),  # 4 -> B
        # A: 0<1
        Instruction("ASK", (3, 1, 2)),  # 5 2<1?
        Instruction("JNZ", (2, 10)),  # 6 -> A1
        # A0: 1<2
        Instruction("ASK", (0, 3, 2)),  # 7 0<2?
        Instruction("EMIT_PERM"),  # 8
        Instruction("HALT"),  # 9
        # A1: 2<1
        Instruction("ASK", (3, 0, 2)),  # 10 2<0?
        Instruction("EMIT_PERM"),  # 11
        Instruction("HALT"),  # 12
        # B: 1<0
        Instruction("ASK", (3, 0, 2)),  # 13 2<0?
        Instruction("JNZ", (2, 18)),  # 14 -> B1
        # B0: 0<2
        Instruction("ASK", (1, 3, 2)),  # 15 1<2?
        Instruction("EMIT_PERM"),  # 16
        Instruction("HALT"),  # 17
        # B1: 2<0
        Instruction("ASK", (3, 1, 2)),  # 18 2<1?
        Instruction("EMIT_PERM"),  # 19
        Instruction("HALT"),  # 20
    ]
    return Program(n=3, k=3, regs=4, code=code, name="opt_n3")


def optimal_program_n4() -> Program:
    # Known S(4)=5. Use explicit decision strategy (Ford-Johnson equivalent for n=4)
    # encoded as an ASK-branch tree. Registers: R0=a,R1=b,R2=c,R3=d,R4=ans/tmp
    # We'll construct by a small manual tree:
    # 1. compare a,b (0,1); 2. compare c,d (2,3)
    # assume wlog a<b,c<d after relabel in knowledge? but labels are fixed elements.
    # easier: just perform fixed comparisons with branching to always resolve total in <=5.
    # Decision tree (one standard optimal): 
    # (0,1),(2,3), if 0<1 and 2<3 compare 1,3 else handle symmetric; then insert remaining.
    # To keep encoding explicit and obviously correct, we implement full tree by states.
    # For brevity/correctness, generate via recursive emit of decision structure? simpler: hardcode.
    R0,R1,R2,R3,R4 = 0,1,2,3,4
    code: List[Instruction] = []
    labels: Dict[str,int] = {}

    def mark(name: str) -> None:
        labels[name] = len(code)

    def ref(name: str) -> int:
        # placeholder resolved later
        return name  # type: ignore

    # We'll append and then patch
    def emit(ins: Instruction) -> int:
        code.append(ins)
        return len(code)-1

    # Patching helpers store (index,argpos,label)
    patches: List[Tuple[int,int,str]] = []
    def emit_jump(op: str, r: int, target: str) -> None:
        idx = emit(Instruction(op, (r, -1)))
        patches.append((idx, 1, target))
    def emit_jmp(target: str) -> None:
        idx = emit(Instruction("JMP", (-1,)))
        patches.append((idx, 0, target))
    def emit_jlt(rs: int, rt: int, target: str) -> None:
        idx = emit(Instruction("JLT", (rs, rt, -1)))
        patches.append((idx, 2, target))

    emit(Instruction("SET", (R0,0)))
    emit(Instruction("SET", (R1,1)))
    emit(Instruction("SET", (R2,2)))
    emit(Instruction("SET", (R3,3)))
    # c1: 0 vs 1
    emit(Instruction("ASK", (R0,R1,R4)))
    emit_jump("JZ", R4, "c1_ge")  # 0>1
    # c1_lt: 0<1
    # c2: 2 vs 3
    emit(Instruction("ASK", (R2,R3,R4)))
    emit_jump("JZ", R4, "c1lt_c2ge")
    # 0<1 and 2<3
    emit(Instruction("ASK", (R1,R3,R4))) # 1 vs 3
    emit_jump("JZ", R4, "A_1ge3")
    # A: 0<1<3 and 2<3 => compare 0,2 and 1,2
    emit(Instruction("ASK", (R0,R2,R4))) # 0 vs 2
    emit_jump("JZ", R4, "A_0ge2")
    # 0<2 and 1<3,2? know 0<1<3,2<3,0<2 => compare 1,2
    emit(Instruction("ASK", (R1,R2,R4)))
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("A_0ge2") # 2<0 => 2<0<1<3
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("A_1ge3") # 3<1 => 0<1 and 2<3<1
    emit(Instruction("ASK", (R0,R2,R4))) # 0 vs 2
    emit_jump("JZ", R4, "A2_0ge2")
    emit(Instruction("ASK", (R1,R2,R4))) # 1 vs 2? know 0<2? 0<2 and 2<3 => 0<2<3<1
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("A2_0ge2") # 2<0 => 2<0<1 and 2<3<1 => compare 0,3
    emit(Instruction("ASK", (R0,R3,R4)))
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))

    mark("c1lt_c2ge") # 0<1 and 3<2
    emit(Instruction("ASK", (R1,R2,R4))) # 1 vs 2
    emit_jump("JZ", R4, "B_1ge2")
    # 0<1<2 and 3<2
    emit(Instruction("ASK", (R0,R3,R4))) # 0 vs 3
    emit_jump("JZ", R4, "B_0ge3")
    emit(Instruction("ASK", (R1,R3,R4))) # 1 vs 3
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("B_0ge3") # 3<0
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("B_1ge2") # 2<1 => 0<1 and 3<2<1
    emit(Instruction("ASK", (R0,R3,R4)))
    emit_jump("JZ", R4, "B2_0ge3")
    emit(Instruction("ASK", (R1,R3,R4))) # 1 vs 3? 0<3 and 3<2 => 0<3<2<1
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("B2_0ge3") # 3<0
    emit(Instruction("ASK", (R0,R2,R4)))
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))

    mark("c1_ge") # 1<0
    emit(Instruction("ASK", (R2,R3,R4))) # 2 vs 3
    emit_jump("JZ", R4, "c1ge_c2ge")
    # 1<0 and 2<3
    emit(Instruction("ASK", (R0,R3,R4))) # 0 vs 3
    emit_jump("JZ", R4, "C_0ge3")
    emit(Instruction("ASK", (R1,R2,R4))) # 1 vs 2
    emit_jump("JZ", R4, "C_1ge2")
    emit(Instruction("ASK", (R0,R2,R4))) # 0 vs 2
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("C_1ge2") # 2<1
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("C_0ge3") # 3<0 => 1<0 and 2<3<0
    emit(Instruction("ASK", (R1,R2,R4)))
    emit_jump("JZ", R4, "C2_1ge2")
    emit(Instruction("ASK", (R0,R2,R4))) # 0 vs 2? 1<2 and 2<3
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("C2_1ge2") # 2<1
    emit(Instruction("ASK", (R1,R3,R4)))
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))

    mark("c1ge_c2ge") # 1<0 and 3<2
    emit(Instruction("ASK", (R0,R2,R4))) # 0 vs 2
    emit_jump("JZ", R4, "D_0ge2")
    emit(Instruction("ASK", (R1,R3,R4))) # 1 vs 3
    emit_jump("JZ", R4, "D_1ge3")
    emit(Instruction("ASK", (R0,R3,R4))) # 0 vs 3
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("D_1ge3") # 3<1
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("D_0ge2") # 2<0 => 1<0 and 3<2<0
    emit(Instruction("ASK", (R1,R3,R4)))
    emit_jump("JZ", R4, "D2_1ge3")
    emit(Instruction("ASK", (R0,R3,R4)))
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))
    mark("D2_1ge3") # 3<1
    emit(Instruction("ASK", (R1,R2,R4)))
    emit(Instruction("EMIT_PERM")); emit(Instruction("HALT"))

    # patch
    for idx, argpos, name in patches:
        target = labels[name]
        args = list(code[idx].args)
        args[argpos] = target
        code[idx] = Instruction(code[idx].op, tuple(args))

    return Program(n=4, k=5, regs=5, code=code, name="opt_n4")


# --- parametric binary insertion family (explicit for given n) ---

def binary_insertion_sort_explicit(n: int) -> Tuple[Program, int]:
    """Return an explicit straight-line-control ESP program for binary insertion.

    This is an explicit unfolded encoding for a fixed n: it realizes binary
    insertion comparisons in a deterministic schedule (a standard adaptive
    strategy). Program size is O(B(n)*log n) (one block per comparison/merge step
    in this simple unfolding), which is polynomial in n; it is a restricted-family
    witness at budget B(n), not an exact-S(n) completeness witness in general.
    """
    # We generate code that maintains a sorted prefix in an array encoded into regs?
    # Registers are integers; easier: we simulate by tracking permutation via state
    # only through ASKs on label pairs determined by the usual binary insertion
    # positions over the current sorted sequence. Since control flow in this simple
    # static encoding must not read X except ASK, we implement the textbook
    # decision procedure: to insert element v = i, binary search over current sorted
    # list L of length i by comparing v with L[mid] at each step - but L's identity
    # depends on prior outcomes. Therefore full explicit static unfolding would be a
    # decision tree of size related to i!. Instead, we provide a compact interpreted
    # driver using a small fixed instruction set extension is not allowed; so we
    # realize binary insertion as: for each new element, do linear scan? no, want
    # binary insertion budget.
    # Alternative: encode the standard binary-insertion decision tree for given n by
    # recursive construction over all possible sorted prefixes? that's exponential in n.
    # So for "explicit ESP code" in this ISA, binary insertion's adaptive choices
    # require either (a) registers holding the current sorted sequence and computed
    # indices (then ASK takes register-indirect labels - supported) and comparisons
    # determine branches (supported) -> this is a fixed-size control program with
    # runtime O(n^2 log n) steps manipulating an array stored in registers/memory.
    # Our ISA has no memory array, only fixed regs. For a true polynomial-size fixed
    # control program for all n we would need RAM/array addressing; that's a standard
    # uniform model extension. To stay fully explicit and checkable, we implement a
    # *RAM-extended* variant in the interpreter? No, must match spec.

    # Practical checkable compromise: build the exact decision tree for n<=8 by
    # exploring all X? but tree is huge. Better: construct program as a driver that
    # is correct by simulating binary insertion logic against X via the oracle calls
    # in the mathematically prescribed order for the concrete X? but program cannot
    # see X. However, given current knowledge G and previous answers, the next binary
    # insertion comparison is determined by outcomes - which is exactly a decision
    # tree. So explicit ESP code IS that tree. For small n we can construct it by
    # state-compressed exploration over all orders (states are possible partial orders)
    # deduplicating identical knowledge states - this is like the framed DAG/program
    # idea; size can be polynomial? no, not guaranteed.

    # Given scope, provide: (1) optimal small-n explicit programs, (2) a direct
    # verification function that the binary-insertion *strategy* (as an adaptive
    # algorithm class) achieves B(n) with poly runtime, and (3) mark parametric
    # fixed-control encoding as requiring array addressing (noted in doc §5.2).
    # We'll implement a strategy runner for binary insertion to supply the experiment.
    raise NotImplementedError("explicit unfolded ESP for general n not generated here")


import math


def binary_insertion_comparison_count(n: int) -> int:
    """Worst-case charged comparisons B(n) = sum_{i=1}^{n-1} ceil(log2(i+1))."""
    return sum(math.ceil(math.log2(i + 1)) for i in range(1, n))


def run_binary_insertion_strategy(X_rank: Sequence[int]) -> Tuple[List[int], int, int]:
    """Run textbook binary insertion sort as an adaptive charged-oracle strategy.

    Returns (output permutation, comparisons, logical_steps). The algorithm's
    control decisions depend only on previous comparison outcomes; X is consulted
    only via comparisons (counted). Steps are O(n^2 log n) in a simple accounting.
    """
    n = len(X_rank)
    order: List[int] = [0] if n else []
    comps = 0
    steps = 0

    def less(i: int, j: int) -> bool:
        nonlocal comps, steps
        comps += 1
        steps += 1
        return X_rank[i] < X_rank[j]

    for v in range(1, n):
        lo, hi = 0, len(order)
        while lo < hi:
            mid = (lo + hi) // 2
            steps += 1
            # compare v with order[mid]
            if less(v, order[mid]):
                hi = mid
            else:
                lo = mid + 1
        order.insert(lo, v)
        steps += len(order)  # insertion bookkeeping
    return order, comps, steps


def merge_sort_comparison_count(n: int) -> int:
    """Worst-case comparisons M(n) for standard top-down merge sort.

    Split: left = first floor(n/2), right = rest. Merge of p,q sorted lists
    uses at most p+q-1 charged comparisons.
    """
    if n <= 1:
        return 0
    left = n // 2
    right = n - left
    return (
        merge_sort_comparison_count(left)
        + merge_sort_comparison_count(right)
        + (n - 1)
    )


def run_merge_sort_strategy(X_rank: Sequence[int]) -> Tuple[List[int], int, int]:
    """Run standard top-down merge sort as an adaptive charged-oracle strategy.

    Returns (output permutation, comparisons, logical_steps). The program
    observes the unknown order X only through charged ASK outcomes less(i,j);
    recursive split points and merge-front choices depend only on previous
    outcomes and the fixed label partition, never on X_rank values directly.
    Split: indices[:n//2], indices[n//2:]. Steps are O(n log n) comparisons
    plus O(n log n) bookkeeping in this accounting.
    """
    n = len(X_rank)
    comps = 0
    steps = 0

    def less(i: int, j: int) -> bool:
        nonlocal comps, steps
        comps += 1
        steps += 1
        return X_rank[i] < X_rank[j]

    def merge(left: List[int], right: List[int]) -> List[int]:
        nonlocal steps
        out: List[int] = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            steps += 1
            # charged oracle query: only outcome is observed
            if less(left[i], right[j]):
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        if i < len(left):
            out.extend(left[i:])
            steps += len(left) - i
        if j < len(right):
            out.extend(right[j:])
            steps += len(right) - j
        return out

    def msort(indices: List[int]) -> List[int]:
        nonlocal steps
        steps += 1
        if len(indices) <= 1:
            return list(indices)
        mid = len(indices) // 2
        left = msort(indices[:mid])
        right = msort(indices[mid:])
        return merge(left, right)

    out = msort(list(range(n)))
    return out, comps, steps


# --- verification helpers ---

def all_total_orders(n: int) -> Iterable[List[int]]:
    for perm in itertools.permutations(range(n)):
        # perm is the list in increasing X order? easier: X_rank such that element perm[r] has rank r
        rank = [0] * n
        for r, elem in enumerate(perm):
            rank[elem] = r
        yield rank


def check_program_on_all_orders(prog: Program, step_limit: Optional[int] = None) -> Dict:
    worst_q = -1
    worst_steps = -1
    bad = None
    count = 0
    for rank in all_total_orders(prog.n):
        res = run_program(prog, rank, step_limit=step_limit)
        count += 1
        if not res.accepted:
            bad = (rank, res)
            break
        worst_q = max(worst_q, res.comparisons)
        worst_steps = max(worst_steps, res.steps)
    return {
        "ok": bad is None,
        "orders": count,
        "worst_q": worst_q,
        "worst_steps": worst_steps,
        "bad": None if bad is None else {"rank": bad[0], "reason": bad[1].reason, "q": bad[1].comparisons, "steps": bad[1].steps},
    }


def check_binary_insertion_family(max_n: int = 8) -> Dict:
    results = {}
    for n in range(1, max_n + 1):
        worst_q = -1
        worst_steps = -1
        ok = True
        budget = binary_insertion_comparison_count(n)
        for rank in all_total_orders(n):
            out, q, steps = run_binary_insertion_strategy(rank)
            if not _is_sorted_by_X(out, rank) or q > budget:
                ok = False
            worst_q = max(worst_q, q)
            worst_steps = max(worst_steps, steps)
        # standard binary insertion achieves the worst-case bound B(n)
        if worst_q != budget:
            ok = False
        results[n] = {"ok": ok, "budget": budget, "worst_q": worst_q, "worst_steps": worst_steps}
    return results


def check_merge_sort_family(max_n: int = 8) -> Dict:
    """Exhaustively check standard top-down merge sort as a charged-oracle strategy.

    For each n, runs on all n! total orders X (given as rank functions) and
    records correctness, the exact worst-case charged comparison count, and
    logical steps. The algorithm observes X only through ASK outcomes.
    """
    results = {}
    for n in range(1, max_n + 1):
        worst_q = -1
        worst_steps = -1
        ok = True
        budget = merge_sort_comparison_count(n)
        for rank in all_total_orders(n):
            out, q, steps = run_merge_sort_strategy(rank)
            if not _is_sorted_by_X(out, rank) or q > budget:
                ok = False
            worst_q = max(worst_q, q)
            worst_steps = max(worst_steps, steps)
        # worst case over all orders attains the standard merge-sort bound M(n)
        if worst_q != budget:
            ok = False
        results[n] = {
            "ok": ok,
            "budget": budget,
            "worst_q": worst_q,
            "worst_steps": worst_steps,
        }
    return results


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-small", action="store_true")
    ap.add_argument("--check-insertion", type=int, default=0)
    ap.add_argument("--check-merge", type=int, default=0)
    args = ap.parse_args()
    if args.check_small:
        for ctor in [optimal_program_n1, optimal_program_n2, optimal_program_n3, optimal_program_n4]:
            p = ctor()
            r = check_program_on_all_orders(p)
            print(p.name, p.encoding_size_bits(), r)
    if args.check_insertion:
        print(json.dumps(check_binary_insertion_family(args.check_insertion), indent=2, sort_keys=True))
    if args.check_merge:
        print(json.dumps(check_merge_sort_family(args.check_merge), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

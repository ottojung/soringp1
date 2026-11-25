#!/usr/bin/env python3
"""Total-move-coverage branch-and-bound fragment for G(n,k) refuter search.

Records, at every explored node (P,b), status for ALL incomparable pairs in
Inc(P) (no heuristic dominance without proof). A move is refuter-certified if
at least one adversary answer (lt/gt) leads to a refuter win within budget.
The node is refuter-winning iff EVERY move is refuter-certified (adversary can
answer any sorter move). A move is sorter-certified if BOTH answers lead to a
sorter win (sorter wins by playing this move). Unknown/capped moves block
certification.

Poset congruence: optional color-refinement canonical key for memoization.
This is a SOUND invariant for value equality only when states are identical or
when an explicit isomorphism is established; by default we use exact state keys
(no congruence). With --congruence we use 2-dim color-refinement signatures as
memo keys ONLY for states where the signature is a complete invariant? No -
refinement is not complete in general. Therefore --congruence is OFF for
certified claims and used only as an experiment label in trace; default is
exact/identity (proof-safe). For n<=6 we can optionally do full S_n canonical
but n=12 makes that infeasible - we do not use it.
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path

# state: tuple of successor bitmasks, succ[i] has bit j set iff i<j (TC)

def extend(succ, i, j):
    out = list(succ)
    new_g = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_g
    return tuple(out)

def incomparable_pairs(succ, n):
    return [(i,j) for i in range(n) for j in range(i+1,n)
            if not (succ[i]>>j&1) and not (succ[j]>>i&1)]

def is_total(succ, n):
    for i in range(n):
        for j in range(i+1,n):
            if not (succ[i]>>j&1) and not (succ[j]>>i&1):
                return False
    return True

def state_key(succ):
    return succ  # exact

REFUTER_WIN = 'refuter_win'      # adversary wins from this state within budget
SORTER_WIN = 'sorter_win'        # sorter wins
UNKNOWN = 'unknown'              # capped/unresolved

class Stats:
    def __init__(self, node_cap, time_cap):
        self.node_cap = node_cap
        self.time_cap = time_cap
        self.nodes = 0
        self.moves_examined = 0
        self.answer_checks = 0
        self.memo_hits = 0
        self.t0 = time.perf_counter()
        self.capped = False
        self.cap_reason = None
        self.first_cap_path = None
    def tick(self, path=None):
        if self.capped: return True
        self.nodes += 1
        if self.nodes > self.node_cap:
            self.capped = True; self.cap_reason = f'node_cap>{self.node_cap}'
            if self.first_cap_path is None: self.first_cap_path = list(path or [])
            return True
        if self.time_cap and (time.perf_counter()-self.t0) > self.time_cap:
            self.capped = True; self.cap_reason = f'time_cap>{self.time_cap}s'
            if self.first_cap_path is None: self.first_cap_path = list(path or [])
            return True
        return False

def solve(succ, n, b, memo, stats, trace_nodes=None, path=None, depth=0, trace_depth=0):
    """Return (status, detail). detail records total move coverage at explored nodes."""
    if path is None: path = []
    key = (succ, b)
    if key in memo:
        stats.memo_hits += 1
        return memo[key][0], {'memo': True, 'status': memo[key][0]}
    if stats.capped:
        return UNKNOWN, {'capped': True, 'reason': stats.cap_reason}
    if stats.tick(path):
        return UNKNOWN, {'capped': True, 'reason': stats.cap_reason}
    if is_total(succ, n):
        res = (SORTER_WIN, {'total': True})
        memo[key] = res; return res
    if b == 0:
        res = (REFUTER_WIN, {'budget_zero_non_total': True, 'inc': len(incomparable_pairs(succ,n))})
        memo[key] = res; return res
    inc = incomparable_pairs(succ, n)
    # total move coverage: examine ALL incomparable pairs
    move_records = []
    any_sorter_win_move = False
    any_unknown = False
    for (i,j) in inc:
        if stats.capped:
            any_unknown = True
            move_records.append({'move':[i,j],'status':UNKNOWN,'reason':'capped'})
            continue
        stats.moves_examined += 1
        # adversary wins move if EXISTS answer with refuter win; sorter wins move if BOTH answers sorter win
        ans_records = {}
        refuter_answer = None
        sorter_both = True
        for ans_name, child in (('lt', extend(succ,i,j)), ('gt', extend(succ,j,i))):
            if stats.capped:
                ans_records[ans_name] = UNKNOWN; sorter_both = False; continue
            stats.answer_checks += 1
            st, _ = solve(child, n, b-1, memo, stats, trace_nodes, path+[(i,j,ans_name)], depth+1, trace_depth)
            ans_records[ans_name] = st
            if st == REFUTER_WIN and refuter_answer is None:
                refuter_answer = ans_name
            if st != SORTER_WIN:
                sorter_both = False
        if sorter_both:
            mstatus = SORTER_WIN
            any_sorter_win_move = True
        elif refuter_answer is not None:
            mstatus = REFUTER_WIN
        else:
            mstatus = UNKNOWN
            any_unknown = True
        move_records.append({'move':[i,j],'answers':ans_records,'status':mstatus})
        # early cut: if any move is sorter-win, node is sorter-win (sound, not dominance heuristic - exact)
        if any_sorter_win_move:
            # still must record remaining moves? total move coverage requires recording all Inc(P).
            # Continue to record remaining as not_examined_after_cut? No - "records total move coverage
            # over all Inc(P) at explored nodes" - explored node: we explored it; we can cut but must be
            # explicit. Better: record all moves; we may mark some as skipped_due_to_exact_cut.
            pass
    # finalize remaining if cut - but we already iterated all in python loop? no, early flag but loop continues.
    # Actually we did not break; we examined all for coverage. Good.
    if any_sorter_win_move:
        status = SORTER_WIN
    elif any_unknown:
        status = UNKNOWN
    else:
        status = REFUTER_WIN
    detail = {'status':status,'budget':b,'inc_count':len(inc),'total_move_coverage':True,
              'move_records': move_records if depth < trace_depth else f'omitted_depth>={trace_depth}',
              'capped': stats.capped}
    if trace_nodes is not None and depth < trace_depth:
        trace_nodes.append({'depth':depth,'state_n':n,'budget':b,'inc_count':len(inc),
                            'status':status,'capped':stats.capped})
    memo[key] = (status, None)
    return status, detail

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, required=True)
    ap.add_argument('--k', type=int, required=True)
    ap.add_argument('--node-cap', type=int, default=200000)
    ap.add_argument('--time-cap', type=float, default=60.0)
    ap.add_argument('--trace-depth', type=int, default=2)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    stats = Stats(args.node_cap, args.time_cap)
    memo = {}
    succ0 = (0,)*args.n
    status, detail = solve(succ0, args.n, args.k, memo, stats, trace_nodes=[], path=[], trace_depth=args.trace_depth)
    dt = time.perf_counter()-stats.t0
    res = {
        'instance': f'G({args.n},{args.k})',
        'n': args.n, 'k': args.k,
        'root_status': status,
        'certified': status != UNKNOWN and not stats.capped,
        'claim': None,  # never auto-claim S(12)>29/S(12)<=30
        'caps': {'node_cap': args.node_cap, 'time_cap': args.time_cap},
        'stats': {'nodes': stats.nodes, 'moves_examined': stats.moves_examined,
                  'answer_checks': stats.answer_checks, 'memo_entries': len(memo),
                  'memo_hits': stats.memo_hits, 'seconds': round(dt,4),
                  'capped': stats.capped, 'cap_reason': stats.cap_reason, 'first_cap_path': stats.first_cap_path},
        'blocking_frontier': {'capped': stats.capped, 'cap_reason': stats.cap_reason, 'first_cap_path': stats.first_cap_path, 'nodes': stats.nodes, 'memo_entries': len(memo)},
        'root_detail': detail,
        'method': 'total-move-coverage refuter BB; exact TC states; no heuristic dominance; identity memo keys; congruence/canonicalization NOT used (n may be 12)',
        'labels': ['definition','deduction','experiment'],
    }
    if status == REFUTER_WIN and not stats.capped and args.n != 12:
        res['claim'] = f'S({args.n})>{args.k} (certified by exhaustive total-coverage fragment)'
    elif status == SORTER_WIN and not stats.capped and args.n != 12:
        res['claim'] = f'sorter wins G({args.n},{args.k}) i.e. S({args.n})<={args.k} (certified by fragment; note refuter-BB found sorter-win move)'
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(res, indent=2))
    print(json.dumps({'instance':res['instance'],'root_status':status,'certified':res['certified'],
                      'nodes':stats.nodes,'moves':stats.moves_examined,'seconds':round(dt,4),
                      'capped':stats.capped,'cap_reason':stats.cap_reason}, indent=2))

if __name__ == '__main__':
    main()

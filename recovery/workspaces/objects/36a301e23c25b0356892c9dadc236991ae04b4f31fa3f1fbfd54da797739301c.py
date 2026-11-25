#!/usr/bin/env python3
"""Exact Wells heavier-child, congruence-quotiented admissibility for n=13, C(13)=33, depth 7.

Finite, reproducible computation. NOT a proof of S(13)>33 or S(13)<=33. No separation claim.

Extends the verified depth-6 frontier (62 orbit classes, 928 heavier states, 4339
incomparable moves, cap 67,108,864 at depth 7 children) to depth 7 with explicit caps
and a saved JSON artifact.

Model: docs/problem.md. n=13 distinct labelled keys, adaptive worst-case pairwise
comparisons, no ties. States are transitively closed strict partial orders.
e(P) is the exact number of linear extensions (order-ideal/downset DP over 2^13 ideals).
Target height C=33.

Wells one-sided heavier-child admissibility:
- S_0={antichain_13}, e=13!, L0=33.
- At depth c, move (u,v) from P in S_c is admissible iff both children satisfy
  e(child) <= 2^(C-c-1). Depth-7 children use cap 2^(33-7)=67,108,864.
- S_{c+1} contains heavier child max(e1,e2) of every admissible move, quotiented by
  labelled-poset isomorphism of the transitive-closed successor DAG (networkx).

Soundness/caveats (same as depth-6 analysis):
- A complete empty one-sided Wells level, under an audited sound discipline, would
  be an obstruction candidate for S(13)>33; but for n>=13 the literature discipline may
  require second children/bidirectional treatment. This computation is INCONCLUSIVE.
- Non-empty levels and resource exhaustion are INCONCLUSIVE. NEVER claim S(13)>33 or
  S(13)<=33 unless certified.

Assumptions A1-A5: adaptive pairwise comparisons/13 keys/no ties; exact e(P) downset DP;
admissibility cap 2^(C-c-1); exhaustion/caps inconclusive; quotient via networkx
DiGraphMatcher.is_isomorphic on transitive-closed successor DAG.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from one_ply_obstruction import add_relation, linear_extensions, incomparable_pairs, ceil_log2

import networkx as nx

N = 13
C = 33
FACT13 = math.factorial(N)


def succ_to_dag(succ):
    G = nx.DiGraph()
    G.add_nodes_from(range(N))
    for i in range(N):
        m = succ[i]
        while m:
            j = (m & -m).bit_length() - 1
            m &= m - 1
            G.add_edge(i, j)
    return G


def quotient_heavy_states(items, progress_every=50, t0=None):
    classes = []
    for idx, (e_heavy, succ) in enumerate(items, 1):
        G = succ_to_dag(succ)
        found = None
        for c in classes:
            if nx.is_isomorphic(G, c['graph']):
                found = c
                break
        if found is None:
            classes.append({'graph': G, 'succ': succ, 'e': e_heavy, 'count': 1,
                            'pairs': len(incomparable_pairs(succ)),
                            'L0': ceil_log2(e_heavy)})
        else:
            found['count'] += 1
        if progress_every and idx % progress_every == 0:
            dt = time.perf_counter() - t0 if t0 else 0
            print(f"  quotient {idx}/{len(items)} classes={len(classes)} elapsed={dt:.1f}s", flush=True)
    for c in classes:
        del c['graph']
    return classes


def load_depth6_frontier(path):
    with open(path) as f:
        d = json.load(f)
    lv = next(x for x in d['levels'] if x['depth'] == 6)
    # s13-wells-depth6.json stores classes without succ in some forms? check
    if lv['classes'] and 'succ' in lv['classes'][0]:
        return d, lv['classes']
    raise ValueError(f"depth-6 JSON {path} has no succ representatives; regenerate with succ")


def run_depth7_from_s6(max_time_s, max_moves, max_state_expansions, progress_every):
    t0 = time.perf_counter()
    deadline = t0 + max_time_s
    depth = 6  # expanding S_6 -> S_7
    cap = 1 << (C - depth - 1)  # 67,108,864

    # Build S_6 representatives from depth-6 computation by replay? No, depth6 json lacks succ.
    # Recompute S_0..S_6 quickly? depth 6 took 110s; affordable and deterministic.
    print("Recomputing S_0..S_6 to obtain S_6 succ representatives...", flush=True)
    A = (0,) * N
    current = [{'succ': A, 'e': FACT13, 'count': 1, 'pairs': N*(N-1)//2, 'L0': ceil_log2(FACT13)}]
    prior_levels = []
    for d in range(6):
        if time.perf_counter() > deadline:
            return {'status': 'INCONCLUSIVE: time cap during S_0..S_6 recompute', 'elapsed_s': time.perf_counter()-t0}
        cap_d = 1 << (C - d - 1)
        heavy = []
        moves = adm = inad = 0
        for st in current:
            for (i, j) in incomparable_pairs(st['succ']):
                moves += 1
                c1 = add_relation(st['succ'], i, j); c2 = add_relation(st['succ'], j, i)
                e1 = linear_extensions(c1); e2 = linear_extensions(c2)
                if e1 <= cap_d and e2 <= cap_d:
                    adm += 1
                    hv = c1 if e1 >= e2 else c2
                    heavy.append((max(e1, e2), hv))
                else:
                    inad += 1
        classes = quotient_heavy_states(heavy, progress_every=0)
        prior_levels.append({'depth': d+1, 'cap_children': cap_d, 'moves_tested': moves,
                             'admissible_both': adm, 'inadmissible': inad,
                             'orbit_classes': len(classes),
                             'total_heavy_states': sum(c['count'] for c in classes),
                             'classes': [{k: v for k, v in c.items() if k != 'succ'} for c in
                                         sorted(classes, key=lambda c: (-c['e'], -c['count']))]})
        print(f"  S_{d+1}: moves={moves} adm={adm} classes={len(classes)} states={sum(c['count'] for c in classes)} elapsed={time.perf_counter()-t0:.1f}s", flush=True)
        current = classes
        if not classes:
            return {'status': f'OBSTRUCTION_CANDIDATE at S_{d+1} during recompute (audit required)', 'levels_through_6': prior_levels}

    s6 = current
    total_pairs = sum(c['pairs'] * c['count'] for c in s6)  # states * pairs
    # Actually moves tested = sum pairs over class representatives? No, each representative stands for count states but moves from representative? No: Wells level has all states in class; quotient means test representative and each orbit state has isomorphic moves. Standard: test representative once per orbit class, multiply? Depth-6 script tested per representative class in its loop over states list (which were orbit classes with succ+count). It did `for st in states: pairs=incomparable_pairs(st['succ']); for pair in pairs: test` — so it tests ONE representative per class, not per count. Counts are heavier-child occurrences.
    rep_pairs = sum(c['pairs'] for c in s6)
    print(f"S_6 ready: {len(s6)} classes, {sum(c['count'] for c in s6)} states, {rep_pairs} representative moves, depth-7 cap={cap}", flush=True)

    info = {
        'depth_from': 6, 'depth_to': 7, 'state_classes': len(s6),
        'total_states_represented': sum(c['count'] for c in s6),
        'representative_pairs_to_test': rep_pairs,
        'cap_children': cap, 'moves_tested': 0, 'admissible_both': 0, 'inadmissible': 0,
        'expansions': 0, 'stopped': None, 'elapsed_s': 0.0,
        'max_time_s': max_time_s, 'max_moves': max_moves, 'max_state_expansions': max_state_expansions,
    }
    heavy = []
    t7 = time.perf_counter()
    for sidx, st in enumerate(s6):
        if info['stopped']:
            break
        if time.perf_counter() > deadline:
            info['stopped'] = f'time_cap after class {sidx}/{len(s6)} moves {info["moves_tested"]}/{rep_pairs}'
            break
        if max_state_expansions is not None and info['expansions'] >= max_state_expansions:
            info['stopped'] = f'max_state_expansions={max_state_expansions} at class {sidx}'
            break
        info['expansions'] += 1
        pairs = incomparable_pairs(st['succ'])
        for (i, j) in pairs:
            if max_moves is not None and info['moves_tested'] >= max_moves:
                info['stopped'] = f'max_moves={max_moves} at class {sidx} move {info["moves_tested"]}'
                break
            if time.perf_counter() > deadline:
                info['stopped'] = f'time_cap at class {sidx} move {info["moves_tested"]}/{rep_pairs}'
                break
            info['moves_tested'] += 1
            c1 = add_relation(st['succ'], i, j)
            c2 = add_relation(st['succ'], j, i)
            e1 = linear_extensions(c1)
            e2 = linear_extensions(c2)
            if e1 <= cap and e2 <= cap:
                info['admissible_both'] += 1
                hv = c1 if e1 >= e2 else c2
                heavy.append((max(e1, e2), hv))
            else:
                info['inadmissible'] += 1
            if progress_every and info['moves_tested'] % progress_every == 0:
                dt = time.perf_counter() - t7
                rate = info['moves_tested'] / dt if dt else 0
                eta = (rep_pairs - info['moves_tested']) / rate if rate else None
                print(f"  depth7 {info['moves_tested']}/{rep_pairs} adm={info['admissible_both']} inad={info['inadmissible']} heavy={len(heavy)} {rate:.1f} moves/s eta={eta:.0f}s" if eta else f"  depth7 {info['moves_tested']}/{rep_pairs}", flush=True)
    info['elapsed_s'] = round(time.perf_counter() - t7, 3)

    result = {
        'model': 'Wells heavier-child admissible forward search, poset-isomorphism quotient, n=13 C=33 depth 7',
        'n': N, 'C': C, 'target_budget': C, 'fact_n': FACT13,
        'caps': {'max_time_s': max_time_s, 'max_moves': max_moves, 'max_state_expansions': max_state_expansions},
        'caveats': [
            'NOT a proof of S(13)>33. NOT a proof of S(13)<=33. No separation claim.',
            'One-sided Wells heavier-child admissibility; for n>=13 complete refutation may require both children/bidirectional discipline (literature context, not audited).',
            'Resource exhaustion, non-empty levels, or stopped runs are INCONCLUSIVE.',
            'Orbit quotient by networkx DiGraphMatcher.is_isomorphic on transitive-closed successor DAG.',
            'Exact e(P) by downset DP over 2^13 ideals, integer arithmetic.',
        ],
        's6_frontier': {
            'orbit_classes': len(s6), 'total_states': sum(c['count'] for c in s6),
            'representative_pairs': rep_pairs,
            'classes': [{k: v for k, v in c.items() if k != 'succ'} for c in sorted(s6, key=lambda c: (-c['e'], -c['count']))],
        },
        'depth7_analysis': info,
        'prior_levels_summary': prior_levels,
    }

    if info['stopped']:
        result['status'] = f"INCONCLUSIVE: {info['stopped']}"
        result['s7'] = None
        result['elapsed_s'] = round(time.perf_counter() - t0, 3)
        return result

    print(f"Quotienting {len(heavy)} admissible heavier children...", flush=True)
    classes7 = quotient_heavy_states(heavy, progress_every=100, t0=t0)
    classes7.sort(key=lambda c: (-c['e'], -c['count']))
    result['s7'] = {
        'orbit_classes': len(classes7),
        'total_heavy_states': sum(c['count'] for c in classes7),
        'classes': [{k: v for k, v in c.items() if k != 'succ'} for c in classes7],
    }
    if not classes7:
        result['status'] = 'OBSTRUCTION_CANDIDATE: S_7 empty under complete depth-7 enumeration of S_6 (audit required; not a certified S(13)>33 claim)'
    else:
        result['status'] = 'INCONCLUSIVE: S_7 non-empty (no obstruction at depth 7 under one-sided Wells heavier-child quotient; not evidence for S(13)<=33)'
    result['elapsed_s'] = round(time.perf_counter() - t0, 3)
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--time-cap', type=float, default=7200, help='wall seconds, explicit cap')
    ap.add_argument('--max-moves', type=int, default=None, help='cap representative moves tested at depth 7')
    ap.add_argument('--max-state-expansions', type=int, default=None, help='cap S_6 orbit classes expanded')
    ap.add_argument('--progress-every', type=int, default=250)
    ap.add_argument('--json', default=str(ROOT / 'data' / 's13_wells_depth7.json'))
    args = ap.parse_args()
    r = run_depth7_from_s6(args.time_cap, args.max_moves, args.max_state_expansions, args.progress_every)
    print('\nSTATUS:', r['status'])
    if r.get('depth7_analysis'):
        a = r['depth7_analysis']
        print(f"depth7: moves={a['moves_tested']}/{a['representative_pairs_to_test']} adm={a['admissible_both']} inad={a['inadmissible']} cap={a['cap_children']}")
        if a.get('stopped'): print('STOPPED:', a['stopped'])
    if r.get('s7'):
        s7 = r['s7']
        print(f"S_7: classes={s7['orbit_classes']} total={s7['total_heavy_states']}")
        for c in s7['classes'][:20]:
            print(f"  e={c['e']} L0={c['L0']} pairs={c['pairs']} count={c['count']}")
        if len(s7['classes']) > 20: print(f"  ... {len(s7['classes'])-20} more")
    out = Path(args.json)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w') as f:
        json.dump(r, f, indent=2)
    print('wrote', out)
    print('elapsed', r['elapsed_s'], 's')

if __name__ == '__main__':
    main()

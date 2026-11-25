#!/usr/bin/env python3
"""Exact Wells heavier-child, congruence-quotiented admissibility analysis for n=13, C(13)=33.

Finite, reproducible computation. NOT a proof of S(13)>33. No separation claim.

Model (docs/problem.md): n=13 distinct labelled keys, adaptive worst-case pairwise
comparisons. A state P is a transitively closed strict partial order (successor
bitmasks on {0..12}). e(P) = number of linear extensions (exact order-ideal DP).
S(n)=F(antichain_n) is the minimax remaining-comparison value.

Target: test the Wells admissible heavier-child forward search for height C=33.
- S_0 = {antichain_13}.
- At depth c (0-based comparisons made to reach a level-c state), a move (u,v)
  from P in S_c is admissible iff both children satisfy e <= 2^(C-c-1).
- S_{c+1} collects the heavier child (max e; tie broken canonically by poset
  isomorphism key is irrelevant) of every admissible move from every P in S_c.
- States are quotiented by poset isomorphism (congruence quotient) using networkx
  DiGraph isomorphism on the transitively-closed successor DAG.

Soundness (deduction, docs/research-n12-nontightness.md §4): if any S_c is empty,
no height-C sorting tree exists, hence S(13)>C. An empty level found by this
complete enumeration of S_c is a finite obstruction certificate (subject to audit).
Non-empty levels within resource caps are INCONCLUSIVE and do NOT support S(13)<=33.

Caveat (literature, Stober-Weiss/Peczarski context as summarized in prior notes):
for n>=13 one-sided heavier-child forward search may be insufficient for a complete
refutation strategy; a full proof of S(13)>33 may require inspecting second children
or a bidirectional/complete discipline. This script reports the one-sided
Wells/heavier-child admissible levels actually computed.

Assumptions:
A1. Adaptive worst-case pairwise comparisons, 13 distinct keys, no ties.
A2. Exact e(P) by downset DP over 2^13 ideals.
A3. Admissibility cap at depth c+1 children: 2^(C-c-1).
A4. Resource exhaustion (depth, time, state, class caps) is INCONCLUSIVE.
A5. Poset isomorphism is tested by networkx DiGraphMatcher.is_isomorphic on the
    successor DAG (transitively closed); equality of all reported orbit counts is
    up to this quotient.

Reproduce:
  python3 scripts/s13_wells_depth3_cong.py
  python3 scripts/s13_wells_depth3_cong.py --max-depth 4 --time-cap 300
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
try:
    from one_ply_obstruction import add_relation, linear_extensions, incomparable_pairs, ceil_log2
except Exception:  # fallback to local path
    from pathlib import Path as _P
    sys.path.insert(0, str(_P('/home/lubko/soring-fronts/s13-wells-depth3-cong-20261105/scripts')))
    from one_ply_obstruction import add_relation, linear_extensions, incomparable_pairs, ceil_log2

import networkx as nx

N = 13
C = 33
FACT13 = math.factorial(N)


def succ_to_dag(succ):
    n = len(succ)
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    for i in range(n):
        m = succ[i]
        while m:
            j = (m & -m).bit_length() - 1
            m &= m - 1
            G.add_edge(i, j)
    return G


def quotient_heavy_states(items):
    """items: list of (e_heavy, succ). Return list of orbit dicts."""
    classes = []
    for e_heavy, succ in items:
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
    for c in classes:
        del c['graph']
    return classes


def analyze_level(states, depth, max_expansions=None, deadline=None):
    """Expand level `depth` states to produce heavier children for depth+1.

    depth is number of comparisons already made for states in `states`.
    Children are at depth+1, admissible if e <= 2^(C - depth - 1).
    """
    cap = 1 << (C - depth - 1)
    info = {
        'depth_from': depth,
        'depth_to': depth + 1,
        'state_classes': len(states),
        'cap_children': cap,
        'moves_tested': 0,
        'admissible_both': 0,
        'inadmissible': 0,
        'expansions': 0,
        'stopped': None,
    }
    heavy = []
    for sidx, st in enumerate(states):
        succ = st['succ']
        pairs = incomparable_pairs(succ)
        info['moves_tested'] += len(pairs)
        info['expansions'] += 1
        if max_expansions is not None and info['expansions'] > max_expansions:
            info['stopped'] = f'max_expansions={max_expansions}'
            break
        if deadline is not None and time.perf_counter() > deadline:
            info['stopped'] = f'time_cap deadline after state {sidx}'
            break
        for (i, j) in pairs:
            c1 = add_relation(succ, i, j)
            c2 = add_relation(succ, j, i)
            e1 = linear_extensions(c1)
            e2 = linear_extensions(c2)
            if e1 <= cap and e2 <= cap:
                info['admissible_both'] += 1
                hv = c1 if e1 >= e2 else c2
                heavy.append((max(e1, e2), hv))
            else:
                info['inadmissible'] += 1
    return info, heavy


def run(max_depth=4, time_cap=300, max_state_expansions=None):
    t0 = time.perf_counter()
    deadline = t0 + time_cap
    result = {
        'model': 'Wells heavier-child admissible forward search, poset-isomorphism quotient',
        'n': N, 'C': C, 'target_budget': C, 'fact_n': FACT13,
        'max_depth_requested': max_depth, 'time_cap_s': time_cap,
        'caveats': [
            'NOT a proof of S(13)>33. No separation claim.',
            'One-sided heavier-child search; for n>=13 complete refutation may require both children/bidirectional discipline (literature context).',
            'Resource exhaustion is INCONCLUSIVE.',
            'Quotient by networkx DiGraph isomorphism on transitive-closed successor DAG.',
        ],
        'levels': [],
        'status': 'running',
    }

    A = (0,) * N
    # S_0
    s0 = [{'succ': A, 'e': FACT13, 'count': 1, 'pairs': N*(N-1)//2, 'L0': ceil_log2(FACT13),
           'desc': 'antichain'}]
    result['levels'].append({'depth': 0, 'orbit_classes': 1, 'classes': [
        {'e': FACT13, 'count': 1, 'pairs': N*(N-1)//2, 'L0': ceil_log2(FACT13), 'desc': 'antichain'}]})

    current = s0
    for depth in range(max_depth):
        if time.perf_counter() > deadline:
            result['status'] = f'INCONCLUSIVE: time_cap reached before depth {depth}->{depth+1}'
            break
        info, heavy = analyze_level(current, depth, max_expansions=max_state_expansions, deadline=deadline)
        level_rec = {'depth': depth + 1, 'analysis': info}
        if info['stopped']:
            level_rec['orbit_classes'] = None
            level_rec['classes'] = None
            result['levels'].append(level_rec)
            result['status'] = f"INCONCLUSIVE: {info['stopped']}"
            break
        classes = quotient_heavy_states(heavy)
        classes.sort(key=lambda c: (-c['e'], -c['count']))
        level_rec['orbit_classes'] = len(classes)
        level_rec['total_heavy_states'] = sum(c['count'] for c in classes)
        level_rec['classes'] = [{k: v for k, v in c.items() if k != 'succ'} for c in classes]
        result['levels'].append(level_rec)
        if not classes:
            result['status'] = f'OBSTRUCTION_CANDIDATE: S_{depth+1} empty under complete enumeration of S_{depth} with assumptions A1-A5; audit required before claiming S(13)>33'
            break
        current = classes
        if time.perf_counter() > deadline:
            result['status'] = f'INCONCLUSIVE: time_cap reached after depth {depth+1}'
            break
    else:
        result['status'] = f'INCONCLUSIVE: no empty level through depth {max_depth} (not evidence for S(13)<=33)'

    result['elapsed_s'] = round(time.perf_counter() - t0, 3)
    return result


def print_report(r):
    print(f"n={r['n']} C={r['C']} 13!={r['fact_n']} max_depth={r['max_depth_requested']} time_cap={r['time_cap_s']}s")
    print('STATUS:', r['status'])
    for c in r['caveats']:
        print('  -', c)
    for lv in r['levels']:
        d = lv['depth']
        if d == 0:
            print(f"\nS_{d}: 1 orbit class, e={lv['classes'][0]['e']}, L0={lv['classes'][0]['L0']}, pairs={lv['classes'][0]['pairs']}")
            continue
        a = lv['analysis']
        print(f"\nS_{d} (from S_{d-1}): cap e(child)<={a['cap_children']} moves_tested={a['moves_tested']} admissible_both={a['admissible_both']} inadmissible={a['inadmissible']}")
        if a.get('stopped'):
            print('  STOPPED:', a['stopped'])
        if lv.get('orbit_classes') is not None:
            print(f"  heavier-child orbit classes={lv['orbit_classes']} total_heavy_states={lv['total_heavy_states']}")
            for c in lv['classes']:
                print(f"    e={c['e']} (13!/2^{round(math.log2(FACT13/c['e']))} approx? 13!/x={FACT13/c['e']:.6g}) "
                      f"L0={c['L0']} pairs={c['pairs']} count={c['count']}")
    print(f"\nelapsed {r['elapsed_s']}s")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--max-depth', type=int, default=4)
    ap.add_argument('--time-cap', type=float, default=300)
    ap.add_argument('--max-state-expansions', type=int, default=None)
    ap.add_argument('--json', default=None, help='optional JSON output path')
    args = ap.parse_args()
    r = run(max_depth=args.max_depth, time_cap=args.time_cap,
            max_state_expansions=args.max_state_expansions)
    print_report(r)
    if args.json:
        with open(args.json, 'w') as f:
            json.dump(r, f, indent=2)
        print('wrote', args.json)


if __name__ == '__main__':
    main()

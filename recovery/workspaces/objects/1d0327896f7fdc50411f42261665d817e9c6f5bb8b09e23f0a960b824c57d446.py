#!/usr/bin/env python3
import sys, time, math, itertools
sys.path.insert(0, '/home/lubko/soring-fronts/fibonacci-threshold-20261111')
from solve_fib import (
    transitive_closure, extend, incomparable_pairs, is_total,
    count_linear_extensions, m_poset_state, enumerate_all_classes,
    make_refined_canon, A000112, fib_upto, fence_W
)

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    time_limit = float(sys.argv[2]) if len(sys.argv) > 2 else 7200.0
    t0 = time.time()
    F = fib_upto(n + 20)
    print(f'Fibonacci threshold n={n} time_limit={time_limit}s', flush=True)
    print(f'A000112[{n}]={A000112.get(n)}', flush=True)

    # enumerate
    te = time.time()
    classes = enumerate_all_classes(n)
    enum_t = time.time() - te
    count_ok = (A000112.get(n) == len(classes))
    print(f'ENUM n={n} classes={len(classes)} expected={A000112.get(n)} ok={count_ok} time={enum_t:.3f}s', flush=True)

    viol = []
    min_slack = None
    tight = 0
    done = 0
    total = len(classes)
    for idx, c in enumerate(classes):
        if time.time() - t0 > time_limit:
            print(f'TIMEOUT after {done}/{total} classes elapsed={time.time()-t0:.3f}s', flush=True)
            break
        e = count_linear_extensions(c, n)
        mp = m_poset_state(c, n)
        bound = F[mp+2]
        slack = e - bound
        if min_slack is None or slack < min_slack:
            min_slack = slack
        if slack < 0:
            viol.append((n,e,mp,bound,slack,c))
            print(f'VIOLATOR n={n} e={e} m={mp} F={bound} slack={slack} rep={c}', flush=True)
        if slack == 0:
            tight += 1
        done += 1
        if done % 500 == 0 or done == total:
            print(f'PROGRESS {done}/{total} viol={len(viol)} min_slack={min_slack} tight={tight} elapsed={time.time()-t0:.3f}s', flush=True)
    complete = (done == total)
    print(f'RESULT complete={complete} done={done} total={total} count_ok={count_ok} violations={len(viol)} min_slack={min_slack} tight={tight} time={time.time()-t0:.3f}s enum_time={enum_t:.3f}s', flush=True)
    if viol:
        for v in viol[:20]:
            print('  V', v, flush=True)
    # fence n
    w = fence_W(n)
    ew = count_linear_extensions(w,n); mw = m_poset_state(w,n)
    print(f'FENCE W_{n}: e={ew} m={mw} F={F[mw+2]} slack={ew-F[mw+2]}', flush=True)

if __name__ == '__main__':
    main()

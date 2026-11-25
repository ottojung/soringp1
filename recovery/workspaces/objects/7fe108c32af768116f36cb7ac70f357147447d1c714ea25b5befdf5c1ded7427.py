#!/usr/bin/env python3
import sys, os, time, json, argparse, multiprocessing as mp
sys.path.insert(0, '/home/lubko/soring-fronts/fibonacci-threshold-20261111')
from solve_fib import (
    count_linear_extensions, m_poset_state, m_extension_set,
    enumerate_all_classes, fib_upto, A000112
)

N = 8
FIB = fib_upto(N + 20)

def compute_one(args):
    idx, rep = args
    t0 = time.time()
    e = count_linear_extensions(rep, N)
    m = m_poset_state(rep, N)
    bound = FIB[m+2]
    slack = e - bound
    dt = time.time() - t0
    return {'idx': idx, 'e': e, 'm': m, 'bound': bound, 'slack': slack, 'dt': dt, 'rep': rep}

def load_done(checkpoint_path):
    done = {}
    if not os.path.exists(checkpoint_path):
        return done
    with open(checkpoint_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            if 'idx' in r:
                done[int(r['idx'])] = r
    return done

def append_result(checkpoint_path, rec):
    with open(checkpoint_path, 'a') as f:
        f.write(json.dumps({k: rec[k] for k in ('idx','e','m','bound','slack','dt')}, separators=(',',':')) + '\n')
        f.flush()
        os.fsync(f.fileno())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2)-1))
    ap.add_argument('--time-limit', type=float, default=5*3600)
    ap.add_argument('--checkpoint', default='checkpoint_n8.jsonl')
    ap.add_argument('--enum-cache', default='classes_n8.json')
    ap.add_argument('--crosscheck', type=int, default=30, help='target number of extension-set cross-check samples')
    ap.add_argument('--crosscheck-max-e', type=int, default=4000)
    args = ap.parse_args()

    t0 = time.time()
    print(f'START n={N} workers={args.workers} time_limit={args.time_limit}s pid={os.getpid()}', flush=True)

    # enumerate
    if os.path.exists(args.enum_cache):
        with open(args.enum_cache) as f:
            classes = [tuple(x) for x in json.load(f)]
        enum_t = 0.0
        print(f'ENUM loaded cache classes={len(classes)}', flush=True)
    else:
        te = time.time()
        classes = enumerate_all_classes(N)
        enum_t = time.time() - te
        with open(args.enum_cache, 'w') as f:
            json.dump([list(c) for c in classes], f)
        print(f'ENUM computed classes={len(classes)} expected={A000112.get(N)} ok={len(classes)==A000112.get(N)} time={enum_t:.3f}s', flush=True)
    total = len(classes)
    count_ok = (total == A000112.get(N))

    done_map = load_done(args.checkpoint)
    done_count = len(done_map)
    min_slack = None
    tight = 0
    viol = None
    # recompute stats from checkpoint
    for r in done_map.values():
        s = int(r['slack'])
        if min_slack is None or s < min_slack: min_slack = s
        if s == 0: tight += 1
        if s < 0 and viol is None:
            viol = r
    print(f'CHECKPOINT loaded done={done_count}/{total} min_slack={min_slack} tight={tight} viol={viol is not None}', flush=True)

    if viol is not None:
        print(f'VIOLATOR_FROM_CHECKPOINT idx={viol.get("idx")} e={viol.get("e")} m={viol.get("m")} bound={viol.get("bound")} slack={viol.get("slack")}', flush=True)
        return 0

    remaining = [(i, classes[i]) for i in range(total) if i not in done_map]
    print(f'REMAINING {len(remaining)}', flush=True)

    cross_agree = 0
    cross_total = 0
    cross_samples = []  # (idx, e, m_state)
    # gather candidates from checkpoint for cross-check first
    for i,r in done_map.items():
        if len(cross_samples) >= args.crosscheck: break
        if int(r['e']) <= args.crosscheck_max_e:
            cross_samples.append((i, int(r['e']), int(r['m'])))
    # run cross-checks on checkpoint samples
    for idx,e,m_state in cross_samples:
        m_ext = m_extension_set(classes[idx], N)
        cross_total += 1
        if m_ext == m_state:
            cross_agree += 1
        else:
            print(f'CROSSCHECK_MISMATCH idx={idx} e={e} m_state={m_state} m_ext={m_ext}', flush=True)
    if cross_total:
        print(f'CROSSCHECK checkpoint_samples={cross_total} agree={cross_agree}', flush=True)

    t_eval_start = time.time()
    completed_this_run = 0
    # chunk size
    chunksize = 1
    pool = mp.Pool(processes=args.workers)
    try:
        it = pool.imap_unordered(compute_one, remaining, chunksize=chunksize)
        while True:
            if time.time() - t0 > args.time_limit:
                print(f'TIMEBOX elapsed={time.time()-t0:.3f}s', flush=True)
                break
            try:
                rec = it.next(timeout=30)
            except StopIteration:
                break
            except mp.TimeoutError:
                # no result yet, check time
                continue
            idx = rec['idx']
            if idx in done_map:
                continue
            append_result(args.checkpoint, rec)
            done_map[idx] = rec
            done_count += 1
            completed_this_run += 1
            s = rec['slack']
            if min_slack is None or s < min_slack: min_slack = s
            if s == 0: tight += 1
            # cross-check sample
            if cross_total < args.crosscheck and rec['e'] <= args.crosscheck_max_e:
                m_ext = m_extension_set(classes[idx], N)
                cross_total += 1
                if m_ext == rec['m']:
                    cross_agree += 1
                else:
                    print(f'CROSSCHECK_MISMATCH idx={idx} e={rec["e"]} m_state={rec["m"]} m_ext={m_ext}', flush=True)
                print(f'CROSSCHECK progress {cross_agree}/{cross_total}', flush=True)
            if s < 0:
                viol = rec
                print(f'VIOLATOR idx={idx} e={rec["e"]} m={rec["m"]} bound={rec["bound"]} slack={s} rep={classes[idx]}', flush=True)
                break
            if completed_this_run % 50 == 0 or done_count == total:
                elapsed = time.time() - t0
                eval_elapsed = time.time() - t_eval_start
                rate = (completed_this_run / eval_elapsed) if eval_elapsed > 0 else 0.0
                print(f'PROGRESS done={done_count}/{total} this_run={completed_this_run} min_slack={min_slack} tight={tight} cross={cross_agree}/{cross_total} rate={rate:.4f}c/s elapsed={elapsed:.3f}s', flush=True)
    finally:
        pool.terminate()
        pool.join()

    elapsed = time.time() - t0
    eval_elapsed = time.time() - t_eval_start
    rate = (completed_this_run / eval_elapsed) if eval_elapsed > 0 else 0.0
    complete = (done_count == total and viol is None)
    status = 'violator' if viol is not None else ('boundary' if complete else 'incomplete')
    print(f'FINAL status={status} done={done_count}/{total} complete={complete} count_ok={count_ok} min_slack={min_slack} tight={tight} violations={1 if viol else 0} cross_agree={cross_agree} cross_total={cross_total} rate={rate:.6f}c/s elapsed={elapsed:.3f}s enum_time={enum_t:.3f}s workers={args.workers}', flush=True)
    if viol:
        print(f'WITNESS idx={viol["idx"]} e={viol["e"]} m={viol["m"]} bound={viol["bound"]} slack={viol["slack"]} rep={classes[viol["idx"]]}', flush=True)
    # write summary
    summary = {
        'status': status, 'n': N, 'done': done_count, 'total': total, 'complete': complete,
        'count_ok': count_ok, 'min_slack': min_slack, 'tight': tight,
        'violator': viol, 'cross_agree': cross_agree, 'cross_total': cross_total,
        'rate_cps': rate, 'elapsed_s': elapsed, 'enum_time_s': enum_t, 'workers': args.workers,
    }
    with open('summary_n8.json','w') as f:
        json.dump(summary, f, indent=2)
    print('SUMMARY_WRITTEN summary_n8.json', flush=True)

if __name__ == '__main__':
    main()

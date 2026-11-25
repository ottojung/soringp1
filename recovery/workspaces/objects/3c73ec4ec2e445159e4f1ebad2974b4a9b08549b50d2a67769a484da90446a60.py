#!/usr/bin/env python3
import sys, os, time, json, argparse, multiprocessing as mp

sys.path.insert(0, '/home/lubko/soring-fronts/fibonacci-threshold-20261111')
from solve_fib import (
    count_linear_extensions, m_poset_state, m_extension_set,
    enumerate_all_classes, fib_upto, A000112
)

N = 8
FIB = fib_upto(N + 40)

def compute_m(args):
    idx, rep, e = args
    t0 = time.time()
    m = m_poset_state(rep, N)
    bound = FIB[m+2]
    slack = e - bound
    dt = time.time() - t0
    return {'idx': int(idx), 'e': int(e), 'm': int(m), 'bound': int(bound), 'slack': int(slack), 'dt': float(dt)}

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

def write_summary(path, summary):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(summary, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2)-1))
    ap.add_argument('--time-limit', type=float, default=5*3600)
    ap.add_argument('--checkpoint', default='checkpoint_n8_ordered.jsonl')
    ap.add_argument('--enum-cache', default='classes_n8.json')
    ap.add_argument('--e-cache', default='e_values_n8.json')
    ap.add_argument('--crosscheck', type=int, default=30)
    ap.add_argument('--crosscheck-max-e', type=int, default=5000)
    ap.add_argument('--progress-every', type=int, default=100)
    args = ap.parse_args()

    t0 = time.time()
    print(f'START n={N} workers={args.workers} time_limit={args.time_limit}s pid={os.getpid()}', flush=True)

    # enumerate classes (canonical reps)
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
    print(f'CLASS_COUNT total={total} A000112_{N}={A000112.get(N)} ok={count_ok}', flush=True)

    # compute exact e(P) for all classes (cheap DP)
    if os.path.exists(args.e_cache):
        with open(args.e_cache) as f:
            e_list = json.load(f)
        e_t = 0.0
        print(f'E loaded cache count={len(e_list)}', flush=True)
    else:
        te = time.time()
        e_list = [None] * total
        for i, rep in enumerate(classes):
            e_list[i] = int(count_linear_extensions(rep, N))
            if (i+1) % 2000 == 0 or i+1 == total:
                print(f'E_PROGRESS {i+1}/{total} elapsed={time.time()-te:.3f}s', flush=True)
        e_t = time.time() - te
        with open(args.e_cache, 'w') as f:
            json.dump(e_list, f)
        print(f'E computed count={len(e_list)} time={e_t:.3f}s min_e={min(e_list)} max_e={max(e_list)}', flush=True)

    # difficulty order: by e ascending, tie-break by idx for determinism
    order = sorted(range(total), key=lambda i: (e_list[i], i))
    e_by_idx = e_list

    # load checkpoint
    done_map = load_done(args.checkpoint)
    done_count = len(done_map)
    min_slack = None
    tight = 0
    viol = None
    max_done_e = None
    for r in done_map.values():
        s = int(r['slack'])
        e = int(r['e'])
        if min_slack is None or s < min_slack: min_slack = s
        if s == 0: tight += 1
        if max_done_e is None or e > max_done_e: max_done_e = e
        if s < 0 and viol is None:
            viol = r
    print(f'CHECKPOINT loaded done={done_count}/{total} min_slack={min_slack} tight={tight} viol={viol is not None} max_done_e={max_done_e}', flush=True)

    if viol is not None:
        print(f'VIOLATOR_FROM_CHECKPOINT idx={viol.get("idx")} e={viol.get("e")} m={viol.get("m")} bound={viol.get("bound")} slack={viol.get("slack")} rep={classes[int(viol["idx"])]}', flush=True)

    # cross-check samples from checkpoint (independent extension-set minimax)
    cross_agree = 0
    cross_total = 0
    cross_mismatches = []
    # prefer diverse/smaller-e completed samples
    ck_samples = [(int(i), int(r['e']), int(r['m'])) for i, r in done_map.items() if int(r['e']) <= args.crosscheck_max_e]
    ck_samples.sort(key=lambda x: (x[1], x[0]))
    for idx,e,m_state in ck_samples[:args.crosscheck]:
        rep = classes[idx]
        try:
            m_ext = m_extension_set(rep, N)
        except Exception as ex:
            print(f'CROSSCHECK_ERROR idx={idx} e={e} err={ex}', flush=True)
            continue
        cross_total += 1
        if int(m_ext) == int(m_state):
            cross_agree += 1
        else:
            cross_mismatches.append({'idx': idx, 'e': e, 'm_state': m_state, 'm_ext': int(m_ext)})
            print(f'CROSSCHECK_MISMATCH idx={idx} e={e} m_state={m_state} m_ext={m_ext}', flush=True)
    if cross_total:
        print(f'CROSSCHECK checkpoint done={cross_agree}/{cross_total} mismatches={len(cross_mismatches)}', flush=True)

    remaining = [(i, classes[i], e_by_idx[i]) for i in order if i not in done_map]
    if remaining:
        next_e = remaining[0][2]
        print(f'REMAINING {len(remaining)} next_e={next_e} max_remaining_e={remaining[-1][2]}', flush=True)
    else:
        print('REMAINING 0', flush=True)

    t_eval_start = time.time()
    completed_this_run = 0
    status_note = None

    if viol is None and remaining:
        pool = mp.Pool(processes=args.workers)
        try:
            it = pool.imap_unordered(compute_m, remaining, chunksize=1)
            while True:
                if time.time() - t0 > args.time_limit:
                    status_note = 'timebox'
                    print(f'TIMEBOX elapsed={time.time()-t0:.3f}s', flush=True)
                    break
                try:
                    rec = it.next(timeout=30)
                except StopIteration:
                    status_note = 'exhausted'
                    break
                except mp.TimeoutError:
                    continue
                idx = rec['idx']
                if idx in done_map:
                    continue
                append_result(args.checkpoint, rec)
                done_map[idx] = rec
                done_count += 1
                completed_this_run += 1
                s = rec['slack']
                e = rec['e']
                if min_slack is None or s < min_slack: min_slack = s
                if s == 0: tight += 1
                if max_done_e is None or e > max_done_e: max_done_e = e
                # cross-check on-the-fly from easy completed ones
                if cross_total < args.crosscheck and rec['e'] <= args.crosscheck_max_e:
                    try:
                        m_ext = m_extension_set(classes[idx], N)
                        cross_total += 1
                        if int(m_ext) == rec['m']:
                            cross_agree += 1
                        else:
                            cross_mismatches.append({'idx': idx, 'e': rec['e'], 'm_state': rec['m'], 'm_ext': int(m_ext)})
                            print(f'CROSSCHECK_MISMATCH idx={idx} e={rec["e"]} m_state={rec["m"]} m_ext={m_ext}', flush=True)
                        print(f'CROSSCHECK progress {cross_agree}/{cross_total}', flush=True)
                    except Exception as ex:
                        print(f'CROSSCHECK_ERROR idx={idx} e={rec["e"]} err={ex}', flush=True)
                if s < 0:
                    viol = rec
                    print(f'VIOLATOR idx={idx} e={rec["e"]} m={rec["m"]} bound={rec["bound"]} slack={s} rep={classes[idx]}', flush=True)
                    break
                if completed_this_run % args.progress_every == 0 or done_count == total:
                    elapsed = time.time() - t0
                    eval_elapsed = time.time() - t_eval_start
                    rate = (completed_this_run / eval_elapsed) if eval_elapsed > 0 else 0.0
                    print(f'PROGRESS done={done_count}/{total} this_run={completed_this_run} min_slack={min_slack} tight={tight} max_done_e={max_done_e} cross={cross_agree}/{cross_total} rate={rate:.6f}c/s elapsed={elapsed:.3f}s', flush=True)
        finally:
            pool.terminate()
            pool.join()

    elapsed = time.time() - t0
    eval_elapsed = time.time() - t_eval_start
    rate = (completed_this_run / eval_elapsed) if eval_elapsed > 0 else 0.0
    if viol is None and done_count == total:
        status = 'boundary'
    elif viol is not None:
        status = 'violator'
    else:
        status = 'incomplete'

    # stalled difficulty band estimate (next pending in difficulty order)
    stalled = None
    pending = [i for i in order if i not in done_map]
    if pending:
        stalled = {
            'next_idx': int(pending[0]),
            'next_e': int(e_by_idx[pending[0]]),
            'done_up_to_max_e': int(max_done_e) if max_done_e is not None else None,
            'pending_count': len(pending),
        }

    summary = {
        'status': status, 'n': N, 'done': done_count, 'total': total,
        'complete': (done_count == total and viol is None), 'count_ok': count_ok,
        'min_slack': min_slack, 'tight': tight,
        'violator': ({k: viol[k] for k in ('idx','e','m','bound','slack','dt')} | {'rep': list(classes[int(viol['idx'])])}) if viol else None,
        'cross_agree': cross_agree, 'cross_total': cross_total, 'cross_mismatches': cross_mismatches,
        'rate_cps_this_run': rate, 'completed_this_run': completed_this_run,
        'elapsed_s': elapsed, 'enum_time_s': enum_t, 'e_time_s': e_t,
        'workers': args.workers, 'stalled_band': stalled, 'status_note': status_note,
        'e_min': min(e_by_idx), 'e_max': max(e_by_idx),
    }
    write_summary('summary_n8_ordered.json', summary)

    print(f'FINAL status={status} done={done_count}/{total} complete={summary["complete"]} count_ok={count_ok} min_slack={min_slack} tight={tight} violations={1 if viol else 0} cross={cross_agree}/{cross_total} rate={rate:.6f}c/s elapsed={elapsed:.3f}s workers={args.workers}', flush=True)
    if stalled:
        print(f'STALLED {json.dumps(stalled, separators=(",",":"))}', flush=True)
    if viol:
        print(f'WITNESS idx={viol["idx"]} e={viol["e"]} m={viol["m"]} bound={viol["bound"]} slack={viol["slack"]} rep={classes[int(viol["idx"])]}', flush=True)
    print('SUMMARY_WRITTEN summary_n8_ordered.json', flush=True)

if __name__ == '__main__':
    mp.freeze_support()
    main()

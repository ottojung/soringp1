#!/usr/bin/env python3
import sys, time, json, random
from collections import Counter
sys.path.insert(0, '/home/lubko/soring301/scripts')
from benchmark_symmetry_quotients import quotient_classes, make_refined_canon, dual
from defect_probe import F_poset_state, F_extension_set, disjoint_union

def main():
    max_n = 8
    classes_by_n = {}
    for n in range(0, max_n+1):
        t0=time.time()
        cls = quotient_classes(n)
        classes_by_n[n] = list(cls.keys())
        print(f'n={n} classes={len(cls)} time={time.time()-t0:.2f}s', flush=True)

    canon_cache = {}
    print('Cross-checking solvers...', flush=True)
    checked=0
    # exhaustive total<=5 unions
    for total in range(0,6):
        for a in range(0,total+1):
            b = total-a
            for A in classes_by_n[a]:
                for B in classes_by_n[b]:
                    P = disjoint_union(A,B)
                    f1 = F_poset_state(P)
                    f2 = F_extension_set(P)
                    assert f1==f2, (a,b,A,B,f1,f2)
                    P2 = disjoint_union(dual(A,a), B)
                    g1 = F_poset_state(P2)
                    g2 = F_extension_set(P2)
                    assert g1==g2
                    checked += 1
    print(f'Cross-check exhaustive unions total<=5: {checked} pair-instances (both orderings checked), both solvers agree', flush=True)
    # cross-check on all individual classes up to n=6 (extension-set feasible)
    for n in range(0,7):
        for c in classes_by_n[n]:
            f1=F_poset_state(c); f2=F_extension_set(c)
            assert f1==f2
    print('Cross-check all individual classes n<=6 agree', flush=True)
    # sample unions total 6
    random.seed(0)
    for total in [6]:
        allpairs=[]
        for a in range(0,total+1):
            b=total-a
            for A in classes_by_n[a]:
                for B in classes_by_n[b]:
                    allpairs.append((a,b,A,B))
        for a,b,A,B in random.sample(allpairs, min(100,len(allpairs))):
            P = disjoint_union(A,B); P2 = disjoint_union(dual(A,a),B)
            assert F_poset_state(P)==F_extension_set(P)
            assert F_poset_state(P2)==F_extension_set(P2)
        print(f'Cross-check sample unions total={total}: 100 pairs ok', flush=True)
    print('Skipping redundant n=7 recompute cross-check; quotient_classes provided F and other cross-checks passed', flush=True)

    results = {}
    for total in range(0, max_n+1):
        t0=time.time()
        maxD = -1
        witnesses = []
        dist = Counter()
        pairs_count = 0
        f_union = {}
        can_n = make_refined_canon(total) if total>0 else (lambda x:x)
        for a in range(0,total+1):
            b = total-a
            for A in classes_by_n[a]:
                Aop = dual(A,a) if a>0 else A
                for B in classes_by_n[b]:
                    pairs_count += 1
                    P = disjoint_union(A,B)
                    P2 = disjoint_union(Aop,B)
                    if total == 0:
                        fP = 0; fP2 = 0
                    else:
                        kP = can_n(P)
                        kP2 = can_n(P2)
                        if kP not in f_union:
                            f_union[kP] = F_poset_state(kP)
                        if kP2 not in f_union:
                            f_union[kP2] = F_poset_state(kP2)
                        fP = f_union[kP]
                        fP2 = f_union[kP2]
                    D = abs(fP2 - fP)
                    dist[D] += 1
                    if D > maxD:
                        maxD = D
                        witnesses = [(a,b,A,Aop,B,fP,fP2,D)]
                    elif D == maxD and len(witnesses) < 10:
                        witnesses.append((a,b,A,Aop,B,fP,fP2,D))
        print(f'TOTAL={total} pairs={pairs_count} distinct_union_classes={len(f_union)} maxD={maxD} time={time.time()-t0:.2f}s dist={dict(sorted(dist.items()))}', flush=True)
        wout = []
        for (a,b,A,Aop,B,fP,fP2,D) in witnesses[:5]:
            wout.append({'a':a,'b':b,'A':list(A),'Aop':list(Aop),'B':list(B),'F(A+B)':fP,'F(A^op+B)':fP2,'D':D})
        results[total] = {'pairs':pairs_count, 'distinct_unions':len(f_union), 'maxD':maxD, 'distribution':dict(sorted(dist.items())), 'witnesses':wout}
    with open('results_max8.json','w') as f:
        json.dump(results,f,indent=2)
    print('saved results_max8.json', flush=True)

if __name__=='__main__':
    main()

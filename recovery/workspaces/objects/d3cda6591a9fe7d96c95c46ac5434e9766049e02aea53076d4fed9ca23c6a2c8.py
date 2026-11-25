import sys, time, json
from collections import Counter
sys.path.insert(0, '/home/lubko/soring301/scripts')
from benchmark_symmetry_quotients import quotient_classes, make_refined_canon, dual
from defect_probe import F_poset_state, disjoint_union

print('loading classes', flush=True)
classes_by_n = {n: list(quotient_classes(n).keys()) for n in range(8)}
print('classes loaded', flush=True)
total=7
t0=time.time()
maxD = -1
witnesses = []
dist = Counter()
pairs_count = 0
f_union = {}
can_n = make_refined_canon(total)
for a in range(0,total+1):
    b = total-a
    print(f'  a={a},b={b}', flush=True)
    for A in classes_by_n[a]:
        Aop = dual(A,a) if a>0 else A
        for B in classes_by_n[b]:
            pairs_count += 1
            P = disjoint_union(A,B); P2 = disjoint_union(Aop,B)
            kP = can_n(P); kP2 = can_n(P2)
            if kP not in f_union: f_union[kP]=F_poset_state(kP)
            if kP2 not in f_union: f_union[kP2]=F_poset_state(kP2)
            fP=f_union[kP]; fP2=f_union[kP2]
            D=abs(fP2-fP)
            dist[D]+=1
            if D>maxD:
                maxD=D; witnesses=[(a,b,list(A),list(Aop),list(B),fP,fP2)]
            elif D==maxD and len(witnesses)<5:
                witnesses.append((a,b,list(A),list(Aop),list(B),fP,fP2))
out={'pairs':pairs_count,'distinct_unions':len(f_union),'maxD':maxD,'distribution':dict(sorted(dist.items())),'witnesses':[{'a':w[0],'b':w[1],'A':w[2],'Aop':w[3],'B':w[4],'F(A+B)':w[5],'F(A^op+B)':w[6],'D':abs(w[6]-w[5])} for w in witnesses]}
print(f'TOTAL={total} pairs={pairs_count} distinct={len(f_union)} maxD={maxD} time={time.time()-t0:.2f}s dist={dict(sorted(dist.items()))}', flush=True)
with open('n7.json','w') as f: json.dump(out,f,indent=2)
print('saved n7.json', flush=True)
PY

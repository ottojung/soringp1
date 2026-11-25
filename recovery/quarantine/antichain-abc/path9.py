import sys
sys.path.insert(0,'/home/lubko/soring-fronts/antichain-reachable-abc-tree-completeness/scripts')
from benchmark_symmetry_quotients import make_refined_canon

def add_rel(up,x,y):
    n=len(up)
    if up[x]>>y&1: return up
    if up[y]>>x&1: return None
    belowx=1<<x
    for a in range(n):
        if up[a]>>x&1: belowx|=1<<a
    gain=(1<<y)|up[y]
    out=list(up)
    for a in range(n):
        if belowx>>a&1: out[a]|=gain
    return tuple(out)
def inc(up):
    n=len(up)
    return [(i,j) for i in range(n) for j in range(i+1,n) if not(up[i]>>j&1) and not(up[j]>>i&1)]
rows={}; F={}; H={}
for line in open('/home/lubko/soring-scratch/antichain-abc/all9.out'):
    if not line.startswith('ROW'): continue
    p=line.split(); r=int(p[1]); F[r]=int(p[2]); H[r]=int(p[3]); rows[r]=tuple(int(x) for x in p[4].split('=',1)[1].split(','))
canon=make_refined_canon(9)
# first bad path
for line in open('/home/lubko/soring-scratch/antichain-abc/reach9.out'):
    if line.startswith('PATH'):
        print(line.strip()); seq=[int(x.split('(')[0]) for x in line.split()[1:]]; break
cur=rows[seq[0]]; moves=[]
for t in seq[1:]:
    target=canon(rows[t]); found=False
    for x,y in inc(cur):
        for u,v in ((x,y),(y,x)):
            ch=add_rel(cur,u,v)
            if ch is None: continue
            if canon(ch)==target:
                print('compare',u,v,'-> class',t,'F',F[t]); moves.append((u,v)); cur=ch; found=True; break
        if found: break
    if not found: print('NO MOVE',t); break
print('final class',seq[-1],'F,H',F[seq[-1]],H[seq[-1]],'actual up',cur)
print('moves',moves)

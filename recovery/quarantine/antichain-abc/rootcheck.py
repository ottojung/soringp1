import sys,functools
sys.path.insert(0,'/home/lubko/soring-fronts/antichain-reachable-abc-tree-completeness/scripts')
from benchmark_symmetry_quotients import make_refined_canon
from path8 import add_rel, inc

def ext_counts(up):
    n=len(up); down=[0]*n
    for i in range(n):
        for j in range(n):
            if up[i]>>j&1: down[j]|=1<<i
    full=(1<<n)-1; dp=[0]*(full+1); dp[0]=1
    for mask in range(1,full+1):
        s=0
        for v in range(n):
            if mask>>v&1 and not(down[v]&~mask): s+=dp[mask^(1<<v)]
        dp[mask]=s
    return dp[full],down

def E(up): return ext_counts(up)[0]

def certinfo(up):
    n=len(up); total,down=ext_counts(up)
    pairs=[(x,y) for x in range(n) for y in range(x+1,n) if not(up[x]>>y&1) and not(up[y]>>x&1)]
    out={}
    for x,y in pairs:
        a=E(add_rel(up,x,y)); b=total-a; wit=[]
        def slaves(u,v):
            freeY=~(up[v] if False else up[v]|down[v]|(1<<v))
            freeX=~(up[u]|down[u]|(1<<u))
            return (up[u]&freeY).bit_count()+(down[v]&freeX).bit_count()
        for u,v,eu in ((x,y,a),(y,x,b)):
            sl=slaves(u,v)
            if sl<=1 and 2*eu>=total: wit.append(('A',u,v,eu,sl))
            if 2*eu==total: wit.append(('B',u,v,eu,sl))
        if not wit:
            for u,v in ((x,y),(y,x)):
                evu=b if u==x else a
                for z in range(n):
                    if z in (x,y): continue
                    t1=add_rel(up,u,v); t2=add_rel(t1,v,z)
                    a1=0 if t2 is None else E(t2)
                    tz=add_rel(up,z,v); ezv=0 if tz is None else E(tz)
                    bound=max(evu,ezv)
                    if 2*bound<=total and a1<=bound:
                        wit.append(('C',u,v,z,a1,bound)); break
                if wit: break
        out[(x,y)]=(a,b,wit)
    return out,total
up=(10,8,72,0,32,0,0,10)
info,total=certinfo(up)
print('up',up,'e',total)
# F values from all8
rows={}; F={}; H={}
for line in open('/home/lubko/soring-scratch/antichain-abc/all8.out'):
    if not line.startswith('ROW'): continue
    p=line.split(); r=int(p[1]); F[r]=int(p[2]); H[r]=int(p[3]); rows[r]=tuple(int(x) for x in p[4].split('=',1)[1].split(','))
canon=make_refined_canon(8); key={canon(v):r for r,v in rows.items()}
print('class',key[canon(up)],'F,H',F[key[canon(up)]],H[key[canon(up)]])
for (x,y),(a,b,wit) in info.items():
    c1=add_rel(up,x,y); c2=add_rel(up,y,x)
    f1=F[key[canon(c1)]]; f2=F[key[canon(c2)]]
    print('pair',x,y,'branches e',a,b,'child F',f1,f2,'optimal',max(f1,f2)==F[key[canon(up)]]-1,'cert',wit)

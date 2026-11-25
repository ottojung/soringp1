import sys,functools,time
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
@functools.lru_cache(None)
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
@functools.lru_cache(None)
def certs(up):
    n=len(up); total,down=ext_counts(up)
    pairs=[(x,y) for x in range(n) for y in range(x+1,n) if not(up[x]>>y&1) and not(up[y]>>x&1)]
    out={}
    for x,y in pairs:
        a=E(add_rel(up,x,y)); b=total-a; wit=[]
        def slaves(u,v):
            freeY=~(up[v]|down[v]|(1<<v)); freeX=~(up[u]|down[u]|(1<<u))
            return (up[u]&freeY).bit_count()+(down[v]&freeX).bit_count()
        for u,v,eu in ((x,y,a),(y,x,b)):
            sl=slaves(u,v)
            if sl<=1 and 2*eu>=total: wit.append('A')
            if 2*eu==total: wit.append('B')
        if not wit:
            for u,v in ((x,y),(y,x)):
                evu=b if u==x else a
                for z in range(n):
                    if z in (x,y): continue
                    t1=add_rel(up,u,v); t2=add_rel(t1,v,z)
                    a1=0 if t2 is None else E(t2)
                    tz=add_rel(up,z,v); ezv=0 if tz is None else E(tz)
                    bound=max(evu,ezv)
                    if 2*bound<=total and a1<=bound: wit.append('C'); break
                if wit: break
        out[(x,y)]=bool(wit)
    return out
rows={}; F={}; H={}
for line in open('/home/lubko/soring-scratch/antichain-abc/all8.out'):
    if not line.startswith('ROW'): continue
    p=line.split(); r=int(p[1]); F[r]=int(p[2]); H[r]=int(p[3]); rows[r]=tuple(int(x) for x in p[4].split('=',1)[1].split(','))
canon=make_refined_canon(8); key={canon(v):r for r,v in rows.items()}
@functools.lru_cache(None)
def Hrec(up):
    c=key[canon(up)]; f=F[c]
    cs=certs(up); best=10**9; n=len(up)
    for (x,y),ok in cs.items():
        if not ok: continue
        c1=add_rel(up,x,y); c2=add_rel(up,y,x)
        r1=key[canon(c1)]; r2=key[canon(c2)]
        if max(F[r1],F[r2])!=f-1: continue
        best=min(best,1+max(Hrec(c1),Hrec(c2)))
    return best
up=(10,8,72,0,32,0,0,10)
t=time.time(); print('H=',Hrec(up),'time',time.time()-t,'cache',Hrec.cache_info())

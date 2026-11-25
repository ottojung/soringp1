import functools,time,sys
sys.setrecursionlimit(1000000)

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

@functools.lru_cache(None)
def e(up): return ext_counts(up)[0]

def classify(up):
    n=len(up); total,down=ext_counts(up)
    pairs=[(x,y) for x in range(n) for y in range(x+1,n) if not(up[x]>>y&1) and not(up[y]>>x&1)]
    cert={p:False for p in pairs}
    def slaves(x,y):
        freeY=~(up[y]|down[y]|(1<<y)); freeX=~(up[x]|down[x]|(1<<x))
        return (up[x]&freeY).bit_count()+(down[y]&freeX).bit_count()
    for x,y in pairs:
        a=e(add_rel(up,x,y)); b=total-a
        for u,v,eu in ((x,y,a),(y,x,b)):
            if slaves(u,v)<=1 and 2*eu>=total: cert[(x,y)]=True
            if 2*eu==total: cert[(x,y)]=True
            if cert[(x,y)]: break
        if cert[(x,y)]: continue
        for u,v in ((x,y),(y,x)):
            evu=b if u==x else a
            for z in range(n):
                if z in (x,y): continue
                t1=add_rel(up,u,v); t2=add_rel(t1,v,z)
                a1=0 if t2 is None else e(t2)
                tz=add_rel(up,z,v); ezv=0 if tz is None else e(tz)
                bound=max(evu,ezv)
                if 2*bound<=total and a1<=bound:
                    cert[(x,y)]=True; break
            if cert[(x,y)]: break
    return cert,pairs,total

@functools.lru_cache(None)
def F(up):
    cert,pairs,total=classify(up)
    if not pairs: return 0
    return 1+min(max(F(add_rel(up,x,y)),F(add_rel(up,y,x))) for x,y in pairs)

@functools.lru_cache(None)
def H(up):
    cert,pairs,total=classify(up)
    if not pairs: return 0
    vals=[]
    for x,y in pairs:
        if cert[(x,y)]:
            vals.append(1+max(H(add_rel(up,x,y)),H(add_rel(up,y,x))))
    return min(vals) if vals else 10**9

path=[(0,0,0,0,0,0,0,0),
(2,0,0,0,0,0,0,0),
(2,0,8,0,0,0,0,0),
(2,0,8,0,32,0,0,0),
(10,8,8,0,32,0,0,0),
(10,8,72,0,32,0,0,0),
(10,8,72,0,32,0,0,10)]
for k,up in enumerate(path):
    t=time.time(); print('path',k,'e',e(up),'F',F(up),'H',H(up),'t',round(time.time()-t,2),flush=True)
print('cache F',F.cache_info(),'H',H.cache_info())

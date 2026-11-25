import subprocess, sys, time, os
n=int(sys.argv[1]); out=sys.argv[2]; nshards=int(sys.argv[3]) if len(sys.argv)>3 else 4
base='/home/lubko/soring-scratch/antichain-abc'
gen=f'{base}/nauty2_8_8/genposetg'
procs=[]
for s in range(nshards):
    procs.append(subprocess.Popen([gen,str(n),'t','q','m',str(s),str(nshards)],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1<<20))
def parse(line,n):
    line=line.strip()
    if not line or not line.startswith('&'): return None
    s=line[2:]
    bits=[]
    for ch in s:
        v=ord(ch)-63
        for k in range(5,-1,-1): bits.append((v>>k)&1)
    up=[]
    for i in range(n):
        m=0
        for j in range(n):
            if bits[i*n+j]: m|=1<<j
        up.append(m)
    for k in range(n):
        bit=1<<k
        for i in range(n):
            if up[i]&bit: up[i]|=up[k]
    return up
t=time.time()
with open(out,'w') as g:
    g.write(f'{n}\n')
    cnt=0
    for p in procs:
        for line in p.stdout:
            up=parse(line,n)
            if up is None: continue
            g.write(' '.join(map(str,up))+'\n'); cnt+=1
        p.wait()
print('rows',cnt,'time',time.time()-t)

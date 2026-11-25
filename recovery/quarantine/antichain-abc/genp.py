import subprocess, sys, time
n=int(sys.argv[1]); out=sys.argv[2]
t=time.time(); cnt=0
p=subprocess.Popen(['/home/lubko/soring-scratch/antichain-abc/nauty2_8_8/genposetg',str(n),'t'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1<<20)
with open(out,'w') as g:
    g.write(f'{n}\n')
    for line in p.stdout:
        line=line.strip()
        if not line or not line.startswith('&'): continue
        s=line[2:]  # skip & and N(n), valid for n<=62
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
        g.write(' '.join(map(str,up))+'\n'); cnt+=1
p.wait()
print('rows',cnt,'time',time.time()-t)

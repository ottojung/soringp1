import sys
sys.path.insert(0,'/home/lubko/soring-scratch/antichain-abc')
from rootcheck import add_rel, E, certinfo
from benchmark_symmetry_quotients import make_refined_canon
rows={}; F={}; H={}
for line in open('/home/lubko/soring-scratch/antichain-abc/all8.out'):
    if not line.startswith('ROW'): continue
    p=line.split(); r=int(p[1]); F[r]=int(p[2]); H[r]=int(p[3]); rows[r]=tuple(int(x) for x in p[4].split('=',1)[1].split(','))
canon=make_refined_canon(8); key={canon(v):r for r,v in rows.items()}
up=(10,8,72,0,32,0,0,10)
for (x,y) in [(0,7),(5,6)]:
    for u,v in ((x,y),(y,x)):
        c=add_rel(up,u,v); r=key[canon(c)]
        print('MOVE',u,v,'class',r,'F,H',F[r],H[r],'up',c)
        info,total=certinfo(c)
        print('  certified optimal children:')
        for (a,b),(ea,eb,wit) in info.items():
            c1=add_rel(c,a,b); c2=add_rel(c,b,a)
            r1=key[canon(c1)]; r2=key[canon(c2)]
            if max(F[r1],F[r2])==F[r]-1 and wit:
                print('   pair',a,b,'cert',wit,'child F,H',[(F[r1],H[r1]),(F[r2],H[r2])])

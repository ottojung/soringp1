import sys
def load(fn):
    rows={}
    for line in open(fn):
        if not line.startswith('ROW'): continue
        p=line.split()
        r,F,H=int(p[1]),int(p[2]),int(p[3])
        up=tuple(int(x) for x in p[4].split('=',1)[1].split(','))
        rows[up]=(F,H)
    return rows
a=load(sys.argv[1]); b=load(sys.argv[2])
print('keysets equal:',set(a)==set(b))
Fd=[k for k in a if a[k][0]!=b[k][0]]
Hd=[k for k in a if a[k][1]!=b[k][1]]
print('F diffs:',len(Fd),'H diffs:',len(Hd))
anti=tuple([0]*len(next(iter(a))))
print('antichain up:',anti)
print('  old F,H =',a.get(anti),' new F,H =',b.get(anti))
print('old H>F:',sum(1 for k in a if a[k][1]>a[k][0]),' new H>F:',sum(1 for k in b if b[k][1]>b[k][0]))
# where do H values move: distribution of (old H - F, new H - F)
import collections
c=collections.Counter((a[k][1]-a[k][0], b[k][1]-b[k][0]) for k in a if a[k][1]!=b[k][1])
print('top (oldH-F, newH-F) among diffs:', c.most_common(8))

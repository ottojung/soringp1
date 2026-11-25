#!/usr/bin/env python3
"""Analyze the e=8 m-saturated m=4 family: incomparability graph, pair depths."""
import sys
from lean import count_le, mdepth, fval, is_msat, gen_level, incpairs, child

def analyze(rows,n):
    print('rows=',rows)
    inc=incpairs(rows,n)
    print(' incomparable pairs:',inc)
    # incomparability graph adjacency
    adj={i:[] for i in range(n)}
    for a,b in inc:
        adj[a].append(b); adj[b].append(a)
    print(' incomparability adjacency:',adj)
    m,pd=mdepth(rows,n),None
    from lean import pair_depths
    m,pairs=pair_depths(rows,n)
    print(' m=',m,' pair depths:')
    for p,d1,d2 in pairs: print('   ',p,d1,d2)
    print(' e=',count_le(rows,n))

def main():
    reps=[(0,)]
    for n in range(1,9):
        if n>1: reps=gen_level(reps,n)
        keep=[]
        for rows in reps:
            e=count_le(rows,n,cap=8)
            if e>8: continue
            if mdepth(rows,n)>4: continue
            keep.append(rows)
            if mdepth(rows,n)==4 and is_msat(rows,n) and e==8:
                analyze(rows,n)
                print('---')
        reps=keep

if __name__=='__main__': main()

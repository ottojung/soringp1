#!/usr/bin/env python3
import sys, itertools

def closure(rel, n):
    less = [[False]*n for _ in range(n)]
    for (a,b) in rel:
        less[a][b] = True
    for k in range(n):
        for i in range(n):
            if less[i][k]:
                lk = less[k]
                row = less[i]
                for j in range(n):
                    if lk[j]:
                        row[j] = True
    out = set()
    for i in range(n):
        for j in range(n):
            if less[i][j]:
                out.add((i,j))
    return frozenset(out)

def downsets(parent_rel, n):
    # parent on 0..n-1
    res = []
    elems = list(range(n))
    for mask in range(1<<n):
        S = set()
        for i in range(n):
            if mask & (1<<i):
                S.add(i)
        ok = True
        for x in S:
            for y in range(n):
                if (y,x) in parent_rel and y not in S:
                    ok = False; break
            if not ok: break
        if ok:
            res.append(frozenset(S))
    return res

def upsets(parent_rel, n):
    res = []
    for mask in range(1<<n):
        S = set()
        for i in range(n):
            if mask & (1<<i):
                S.add(i)
        ok = True
        for x in S:
            for y in range(n):
                if (x,y) in parent_rel and y not in S:
                    ok = False; break
            if not ok: break
        if ok:
            res.append(frozenset(S))
    return res

def gen_posets(n):
    if n == 0:
        yield frozenset()
        return
    if n == 1:
        yield frozenset()
        return
    for parent in gen_posets(n-1):
        parent_rel = set(parent)
        # parent on labels 0..n-2
        ds = downsets(parent_rel, n-1)
        us = upsets(parent_rel, n-1)
        for L in ds:
            for U in us:
                if L & U:
                    continue
                # L < U in parent
                good = True
                for d in L:
                    for u in U:
                        if (d,u) not in parent_rel:
                            good = False; break
                    if not good: break
                if not good:
                    continue
                newrel = set(parent_rel)
                v = n-1
                for d in L:
                    newrel.add((d,v))
                for u in U:
                    newrel.add((v,u))
                cl = closure(newrel, n)
                if set(cl) != set(newrel):
                    continue
                yield frozenset(newrel)

def count(n):
    c = 0
    for _ in gen_posets(n):
        c += 1
    return c

if __name__ == '__main__':
    for n in range(1, int(sys.argv[1])+1):
        print(n, count(n), flush=True)

#!/usr/bin/env python3
"""Independent core/poset enumeration via exact linear-extension sets.
State = sorted tuple of extensions (each a bytes permutation). A poset is uniquely
determined by its extension set, so minimax and dedup work directly on these sets."""
import sys
from functools import lru_cache

def pre_of(up,n):
    pre=[0]*n
    for a in range(n):
        q=up[a]
        while q:
            b=(q&-q).bit_length()-1; q&=q-1; pre[b]|=1<<a
    return pre

def ideals(up,n,exts):
    pre=pre_of(up,n)
    order=exts[0]
    res=[]
    def rec(i,mask):
        if i==n: res.append(mask); return
        x=order[i]
        rec(i+1,mask)
        if pre[x]&~mask==0: rec(i+1,mask|(1<<x))
    rec(0,0)
    return res

def child(up,exts,n,I):
    """add maximal element n above ideal I; return (up,exts) or None if e>limit handled by caller"""
    # count and generate
    chromo=[]
    for L in exts:
        p=-1
        m=I
        while m:
            bit=m&-m; x=bit.bit_length()-1; m-=bit
            pos=L.index(x)
            if pos>p: p=pos
        for q in range(p+1,n+1):
            chromo.append(L[:q]+bytes([n])+L[q:])
    up2=list(up)+[0]
    m=I
    while m:
        bit=m&-m; x=bit.bit_length()-1; m-=bit
        up2[x]|=1<<n
    return tuple(up2), tuple(sorted(chromo))

@lru_cache(maxsize=None)
def refine(s,colors):
    n=len(s)
    while True:
        sig=[]
        for a in range(n):
            counts={}
            for b in range(n):
                if a==b: continue
                rel=1 if (s[a]>>b)&1 else 2 if (s[b]>>a)&1 else 0
                key=(rel,colors[b]); counts[key]=counts.get(key,0)+1
            sig.append((colors[a],tuple(sorted(counts.items()))))
        labels={v:i for i,v in enumerate(sorted(set(sig)))}
        new=tuple(labels[x] for x in sig)
        if new==colors: return new
        colors=new

def canon_rec(s,colors):
    n=len(s)
    colors=refine(s,colors)
    cells={}
    for v,c in enumerate(colors): cells.setdefault(c,[]).append(v)
    branch=None
    for c in sorted(cells):
        if len(cells[c])>1: branch=cells[c]; break
    if branch is None:
        order=[v for c in sorted(cells) for v in cells[c]]
        inv=[0]*n
        for i,v in enumerate(order): inv[v]=i
        out=[0]*n
        for i,v in enumerate(order):
            q=s[v]
            while q:
                b=(q&-q).bit_length()-1; q&=q-1
                out[i]|=1<<inv[b]
        return tuple(out)
    best=None; newc=max(colors)+1
    for v in branch:
        cc=list(colors); cc[v]=newc
        got=canon_rec(s,tuple(cc))
        if best is None or got<best: best=got
    return best

@lru_cache(maxsize=None)
def canonical(s):
    return canon_rec(s,tuple([0]*len(s)))

def up_from_exts(exts,n):
    up=[0]*n
    for a in range(n):
        for b in range(n):
            if a==b: continue
            if all(L.index(a)<L.index(b) for L in exts): up[a]|=1<<b
    return tuple(up)

def is_core(up,n):
    for a in range(n):
        comp=0
        for b in range(n):
            if a==b: continue
            if (up[a]>>b)&1 or (up[b]>>a)&1: comp+=1
        if comp==n-1: return False
    return True

@lru_cache(maxsize=None)
def minimax(exts):
    if len(exts)==1: return 0
    n=len(exts[0]); best=10**9
    for a in range(n-1):
        for b in range(a+1,n):
            E1=[];E2=[]
            for L in exts:
                if L.index(a)<L.index(b): E1.append(L)
                else: E2.append(L)
            if E1 and E2:
                v=1+max(minimax(tuple(E1)),minimax(tuple(E2)))
                if v<best: best=v
    return best

def enumerate_levels(E_MAX,N_MAX,t0=None,report=None):
    import time
    n=1
    up=(0,); exts=(bytes([0]),)
    levels={}
    cur={canonical(up):(up,exts)}
    levels[1]=dict(cur)
    while n<N_MAX:
        nxt={}
        for key,(up,exts) in cur.items():
            for I in ideals(up,n,exts):
                cnt=0
                for L in exts:
                    p=-1; m=I
                    while m:
                        bit=m&-m; x=bit.bit_length()-1; m-=bit
                        pos=L.index(x)
                        if pos>p: p=pos
                    cnt+=n-p
                if cnt>E_MAX: continue
                up2,ex2=child(up,exts,n,I)
                c=canonical(up2)
                if c not in nxt: nxt[c]=(up2,ex2)
        n+=1
        levels[n]=dict(nxt)
        if report: report(n,len(nxt),t0)
        cur=nxt
        if not cur: break
    return levels

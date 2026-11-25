#!/usr/bin/env python3
"""Enumerate isomorphism classes of posets with e(P)<=E, filter cores, compute exact minimax.
Scratch research script. POSIX-friendly, stdlib only."""
import sys
from functools import lru_cache

E_MAX=12
N_MAX=12

# ---- poset encoding: tuple up[i] = bitmask of strict successors of i ----
def pre_masks(s):
    n=len(s); pre=[0]*n
    for a in range(n):
        q=s[a]
        while q:
            b=(q&-q).bit_length()-1; q&=q-1
            pre[b]|=1<<a
    return pre

def ext_list(s):
    n=len(s)
    if n==0: return [()]
    pre=pre_masks(s)
    res=[]
    def dfs(mask,order):
        if mask==(1<<n)-1:
            res.append(tuple(order)); return
        for x in range(n):
            bit=1<<x
            if not mask&bit and pre[x]&~mask==0:
                order.append(x); dfs(mask|bit,order); order.pop()
    dfs(0,[])
    return res

def ecount(s):
    n=len(s)
    if n==0: return 1
    pre=pre_masks(s)
    dp=[0]*(1<<n); dp[0]=1
    for mask in range(1<<n):
        v=dp[mask]
        if not v: continue
        for x in range(n):
            bit=1<<x
            if not mask&bit and pre[x]&~mask==0:
                dp[mask|bit]+=v
    return dp[-1]

def ideals(s):
    """all down-sets (ideals) as bitmasks, including empty and full"""
    n=len(s); pre=pre_masks(s)
    out=[]
    for mask in range(1<<n):
        ok=True
        m=mask
        while m:
            bit=m&-m; x=bit.bit_length()-1; m-=bit
            if pre[x]&~mask: ok=False; break
        if ok: out.append(mask)
    return out

def child(s,I):
    """add new maximal element above exactly the ideal I"""
    n=len(s)
    up=list(s)+[0]
    m=I
    while m:
        bit=m&-m; x=bit.bit_length()-1; m-=bit
        up[x]|=1<<n
    return tuple(up)

# ---- canonical form via colour refinement + individualization ----
def refine(s,colors):
    n=len(s); pre=pre_masks(s)
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
    best=None
    newc=max(colors)+1
    for v in branch:
        cc=list(colors); cc[v]=newc
        got=canon_rec(s,tuple(cc))
        if best is None or got<best: best=got
    return best

@lru_cache(maxsize=None)
def canonical(s):
    return canon_rec(s,tuple([0]*len(s)))

def is_core(s):
    n=len(s)
    for a in range(n):
        comp=0
        for b in range(n):
            if a==b: continue
            if (s[a]>>b)&1 or (s[b]>>a)&1: comp+=1
        if comp==n-1: return False
    return True

def add_rel(s,a,b):
    n=len(s)
    up=list(s)
    pre=pre_masks(s)
    # predecessors of a including a
    left=1<<a; m=pre[a]
    while m:
        bit=m&-m; left|=bit; m-=bit
    # successors of b including b
    right=1<<b; m=s[b]
    while m:
        bit=m&-m; right|=bit; m-=bit
    m=left
    while m:
        bit=m&-m; i=bit.bit_length()-1; m-=bit
        up[i]|=right
    return tuple(up)

@lru_cache(maxsize=None)
def minimax(s):
    n=len(s)
    if n<=1: return 0
    if ecount(s)==1: return 0
    best=10**9
    for a in range(n):
        for b in range(a+1,n):
            if (s[a]>>b)&1 or (s[b]>>a)&1: continue
            v=1+max(minimax(canonical(add_rel(s,a,b))),minimax(canonical(add_rel(s,b,a))))
            if v<best: best=v
    return best

def enumerate_classes():
    classes={0:{():None}}  # canonical -> representative
    reps_by_n=[ {():None} ]
    for n in range(0,N_MAX):
        cur=reps_by_n[n]
        nxt={}
        for rep in cur:
            s=rep
            for I in ideals(s):
                t=child(s,I)
                if ecount(t)>E_MAX: continue
                c=canonical(t)
                if c not in nxt: nxt[c]=t
        if not nxt: 
            reps_by_n.append({}); continue
        reps_by_n.append(nxt)
        print('n',n+1,'classes with e<=12:',len(nxt),flush=True)
    return reps_by_n

if __name__=='__main__':
    reps=enumerate_classes()
    total=0
    for n in range(2,N_MAX+1):
        cores=[r for r in reps[n]]
        core=[r for r in cores if is_core(r)]
        bad=[]
        for r in core:
            m=minimax(r)
            if m>4: bad.append((r,ecount(r),m))
        print('n',n,'classes',len(cores),'cores',len(core),'cores with m>4:',len(bad),flush=True)
        for r,e,m in bad[:3]:
            print('   BAD e=',e,'m=',m,'poset=',r,flush=True)
        total+=len(core)
    print('total cores 2..12:',total)

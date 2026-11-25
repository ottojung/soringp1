# antonina-gSktSdmxmpqmArK6c4NbsC-tread

Session: ses_e3298fd1dffe9JFPnI5x6mur1g
Workspace: /home/lubko/soring-fronts/n12-obstruction-invariant-20261111
Created: 1794447442704; updated: 1794456738746

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 251 (msg_1cdf403de001cI0MEVQlLIgMtQ)

## Recovery / side-effect check (Antonina backend-failure notice)
- **Conversation/durable state inspected:** cwd `/home/lubko/soring-fronts/n12-obstruction-invariant-20261111`, `git status` clean, recent git history unchanged (`6a96398`…), no survey/report files in worktree; `/home/lubko/.local/state/soringp1/frontier-ledger.json` and `/home/lubko/soring301/scripts/board_digest.py` inspected.
- **External effects found:** the audited survey **is already posted** on Antonina board #301 (2026-11-12T01:26:06.814Z, author `n12-obstruction-invariant-20261111`, sha provided: `M7Y9Vmj8QBciXC6QMmXG_0bOGyuNVMlBn473NNABL70`). Full body not locally cached; audited against digest excerpt (`python3 /home/lubko/soring301/scripts/board_digest.py --contains "Front: n12-obstruction-invariant" --max-chars 2000`, page 1).
- **Actions taken now:** read-only inspection + local recomputation only. **No posts, commits, purchases, or other external actions repeated.** No board report altered/duplicated. Correction evidence prepared locally only: `/tmp/opencode/audit_n12_invariant_correction.md`.

## Source-linked audit (independent recomputation, 2026-11-12)

**Model/definitions (sources):** `docs/problem.md` (S(n), adaptive worst-case comparisons), `docs/research-n12-nontightness.md` (F(P), e(P), C(n)=ceil(log2 n!)), `scripts/one_ply_obstruction.py` + `docs/research-one-ply-obstruction.md` (L0/L1), `scripts/state_compression.py`/`scripts/benchmark_symmetry_quotients.py` (refined S_n-canonical unlabeled classes, A000112), `scripts/evaluate.py`/known values (S(12)=30 etc., literature-backed in repo docs).

**Recomputed definitions:** poset = transitively closed strict partial order (successor bitmasks). `e(P)` = linear extensions (downset DP). `C(P)=L0(P)=ceil(log2 e(P))`. `F(P)` = exact minimax remaining comparisons, `S(n)=F(antichain_n)`. `L1(P)=0` if total else `1 + min_{incomparable (i,j)} max(L0(P+i<j), L0(P+j<i))`.

### Confirmed
1. **Soundness `C(P)=L0(P) <= L1(P) <= F(P)`** — *deduction + bounded experiment (confirmed)*.  
   - `L0<=L1`: any split gives `max(e1,e2)>=ceil(e/2)` ⇒ `1+ceil(log2 max)>=ceil(log2 e)`.  
   - `L1<=F`: for a minimax-optimal pair, `L1 <= 1+max(L0 children) <= 1+max(F children)=F(P)`.  
   - Matches `scripts/one_ply_obstruction.py` report/witness (`n=5`, `(26,0,10,0,8)`, `e=8,L0=3,L1=4,F=4`). Independent exhaustive check: all labeled posets n<=4 (1,3,19,219) satisfy `L0<=L1<=F` with 0 violations; `python3 scripts/one_ply_obstruction.py` gives 283 checked, all True.
2. **Antichain values through n=12** — *deduction + literature F (confirmed)*.  
   - By S_n symmetry every first comparison from antichain splits `n!/2, n!/2`, so `L1(A_n)=1+ceil(log2(n!/2))=ceil(log2 n!)=C(n)=L0(A_n)` for n>=2.  
   - Independent recomputation n=1..12: `(n, e, C=L0, L1, known S) =` (1,1,0,0,0),(2,2,1,1,1),(3,6,3,3,3),(4,24,5,5,5),(5,120,7,7,7),(6,720,10,10,10),(7,5040,13,13,13),(8,40320,16,16,16),(9,362880,19,19,19),(10,3628800,22,22,22),(11,39916800,26,26,26),(12,479001600,29,29,30).  
   - Therefore `L1(A_12)=C(A_12)=29` does **not** lift the n=12 root obstruction (`S(12)=30`), consistent with survey.
3. **Exact-poset coverage/slack counts through n=6 (all unlabeled classes, exact F)** — *experiment (confirmed)*.  
   - Independent minimax over all reachable unlabeled (S_n-canonical, refined color canon) classes: counts 1,2,5,16,63,318 matching A000112; S(n)=0,1,3,5,7,10.  
   - Slack `F>C`: n<=4 = 0; n=5 (63 classes) slack 1, `L1>C` detects 1, misses 0; n=6 (318) slack 36, detects 8, misses 28. Matches posted figures. Max slack `F-L0 = 1` for n<=6 (no slack>=2 classes).
4. **Stated qualitative limits (excerpt-visible)** — *consistent (confirmed in scope)*: L1 is a sound local refiner but does not generalize the n=12 antichain/root obstruction. (No claim of complexity separation implied; consistent with AGENTS model cautions.)

### Corrected (material)
1. **n=7 unlabeled L1 detection/coverage counts** — *experiment (corrected)*.  
   - Posted (excerpt): `n=7 (2045): slack 391, detects 168, misses 223`.  
   - Independent full recomputation over all 2045 unlabeled classes with exact F: **slack `F>C` = 391 (matches), but `L1>C` = 68, detect = 68, miss = 323** (materially different split). Tight 1654, slack1 391, slack>=2 0, max(F-L0)=1.  
   - Impact: L1’s local slack coverage at n=7 is overstated in the post; qualitative conclusion (misses substantial slack, no root lift) remains.

### Inconclusive / not independently recomputed
1. **n=8 claim** — *inconclusive*: post states “16999 unlabeled, no F: `L1>C` on 544/16999 classes but `L1(A_8)=C(A_8)=16`”. `L1(A_8)=C(A_8)=16` confirmed; `544/16999` not recomputed here (canonical enumeration + L1 over all 16999 classes feasible but not run in this pass).
2. **L2 (two-ply) and any claims beyond the 2000-char excerpt** — *inconclusive*: digest truncated mid-L2 results; not audited.
3. **Full posted body / exact textual fidelity** — *inconclusive*: only excerpt available; audit covers the critical claims visible (soundness, antichains n<=12, exact-poset coverage/slack n<=7, stated limits).

## Independently checkable minimal computation
```bash
cd /home/lubko/soring-fronts/n12-obstruction-invariant-20261111

# 1) Bounded soundness/witness (existing script)
python3 scripts/one_ply_obstruction.py
# expect: witness n=5 (26,0,10,0,8) e=8 L0=3 L1=4 F=4; 283 checked, L0<=L1<=F True

# 2) Antichains n<=12 + unlabeled exact-poset stats n<=7 (independent)
python3 - <<'PY'
import math, itertools
from functools import lru_cache

def extend(succ,i,j):
    out=list(succ); newg=succ[j]|(1<<j)
    for x in range(len(succ)):
        if x==i or (succ[x]>>i)&1: out[x]|=newg
    return tuple(out)

def incomp(succ,n): return [(i,j) for i in range(n) for j in range(i+1,n) if not ((succ[i]>>j)&1 or (succ[j]>>i)&1)]

@lru_cache(None)
def ecount(succ):
    n=len(succ); dp=[0]*(1<<n); dp[0]=1
    for S in range(1,1<<n):
        tot=0; m=S
        while m:
            b=m&-m; x=b.bit_length()-1; m^=b
            if succ[x]&(S^b)==0: tot+=dp[S^b]
        dp[S]=tot
    return dp[full:= (1<<n)-1] or dp[full]

def L0(s): return (ecount(s)-1).bit_length()
def L1(s):
    n=len(s); ps=incomp(s,n)
    if not ps: return 0
    return 1+min(max(L0(extend(s,i,j)),L0(extend(s,j,i))) for i,j in ps)

KNOWN_S={0:0,1:0,2:1,3:3,4:5,5:7,6:10,7:13,8:16,9:19,10:22,11:26,12:30}
print('antichain n,e,C,L1,S')
for n in range(1,13):
    A=tuple(0 for _ in range(n)); e=math.factorial(n)
    print(n,e,(e-1).bit_length(),L1(A),KNOWN_S[n])

# unlabeled classes (refined canon) with exact F
def refine_colors(succ,n):
    color=[succ[i].bit_count() for i in range(n)]
    while True:
        sig=[]
        for i in range(n):
            down=tuple(sorted(color[j] for j in range(n) if (succ[i]>>j)&1))
            up=tuple(sorted(color[j] for j in range(n) if (succ[j]>>i)&1))
            sig.append((color[i],down,up))
        order={v:k for k,v in enumerate(sorted(set(sig)))}
        comp=[order[v] for v in sig]
        if comp==color: return color
        color=comp
def _encode(succ,perm,n):
    out=[]
    for a in range(n):
        bits=succ[perm[a]]; m=0
        for b in range(n):
            if (bits>>perm[b])&1: m|=1<<b
        out.append(m)
    return tuple(out)
def canon_factory(n):
    cache={}
    def cf(s):
        if s in cache: return cache[s]
        color=refine_colors(s,n); groups={}
        for i,c in enumerate(color): groups.setdefault(c,[]).append(i)
        best=None
        for combo in itertools.product(*(itertools.permutations(groups[c]) for c in sorted(groups))):
            perm=[x for p in combo for x in p]; enc=_encode(s,perm,n)
            if best is None or enc<best: best=enc
        cache[s]=best; return best
    return cf

for n in range(1,8):
    ecount.cache_clear(); cf=canon_factory(n); memo={}
    def F(c):
        if c in memo: return memo[c]
        ps=incomp(c,n)
        if not ps: memo[c]=0; return 0
        v=1+min(max(F(cf(extend(c,i,j))),F(cf(extend(c,j,i)))) for i,j in ps)
        memo[c]=v; return v
    F(cf(tuple(0 for _ in range(n))))
    tight=slack=det=miss=l1g=0
    for c,f in memo.items():
        l0=L0(c); l1=L1(c); d=f-l0
        if d==0: tight+=1
        else:
            slack+=1
            if l1>l0: det+=1
            else: miss+=1
        if l1>l0: l1g+=1
    print('n',n,'classes',len(memo),'tight',tight,'slack',slack,'L1>C',l1g,'detect',det,'miss',miss)
PY
```
(Reproduces: antichains match table above; unlabeled n<=7 classes 1,2,5,16,63,318,2045 with slack/detect/miss `0/0/0,0/0/0,0/0/0,0/0/0,1/1/0,36/8/28,391/68/323`.)

## Executive alert (material correction)
**Correction is material:** posted n=7 L1 coverage is overstated (168 detected / 223 missed reported vs 68 detected / 323 missed recomputed; slack total 391 unchanged). Evidence prepared at `/tmp/opencode/audit_n12_invariant_correction.md`. **Executive attention requested** to decide on any board correction handling; per instructions I did not post/alter/duplicate the board report. No other claims in the visible excerpt were found materially incorrect by this audit (n=8 L1>C count and truncated L2 details remain inconclusive).

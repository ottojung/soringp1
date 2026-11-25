# antonina-y0Ez6mI9IH92rxlhtBHMgF-nerve

Session: ses_e12acc806ffeBjg8SMOOVablCF
Workspace: /home/lubko/soring-fronts/exec-known-gap-uniform-adversary-20261118
Created: 1794983016523; updated: 1794983307326

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 189 (msg_1ed573b58001QCfMJFKPFRJ80N)

Wrote `research-known-gap-uniform-adversary.md` in `/home/lubko/soring-fronts/exec-known-gap-uniform-adversary-20261118` (no commits/PRs/Lean).

**Sources read (as requested):** `curator/AGENTS.md`, `curator/docs/problem.md`, `curator/docs/literature.md`, `curator/docs/research-plan.md`, `curator/docs/research-n12-nontightness.md`, `curator/docs/research-one-ply-obstruction.md` (plus supporting local notes consulted for stated values/citations: `research-hardness-boundaries.md`, `research-certificates-barriers.md`).

**C(n)=ceil(log2 n!) [computation] and S(n) table (n=1..22, with local-source basis/uncertainty):**
| n | C(n) | S(n) | gap | basis (local) |
|---:|---:|---:|---:|---|
| 1 | 0 | 0 | 0 | exact small/kernel-checked context |
| 2 | 1 | 1 | 0 | " |
| 3 | 3 | 3 | 0 | " |
| 4 | 5 | 5 | 0 | " |
| 5 | 7 | 7 | 0 | " |
| 6 | 10 | 10 | 0 | " |
| 7 | 13 | 13 | 0 | tight (plan/literature baseline) |
| 8 | 16 | 16 | 0 | tight |
| 9 | 19 | 19 | 0 | tight |
| 10 | 22 | 22 | 0 | tight |
| 11 | 26 | 26 | 0 | tight through n=11 (reported/credited in local lit notes) |
| 12 | 29 | 30 | 1 | Wells 1965/1971, credited/discussed in Peczarski 2012, Stober–Weiß 2023 |
| 13 | 33 | 34 | 1 | Kasai et al. 1994 (cited locally); gap discussed Peczarski 2012 §4 (summary) |
| 14 | 37 | unknown (locally) | unknown (>=1 indicated) | known for n<=22 per local summaries; Peczarski 2012 §4 discusses non-tightness for 13–15, but exact S(14) / primary citation not explicitly recorded locally |
| 15 | 41 | 42 (reported) | 1 (reported) | reported as Jing et al. in local notes; full bibliographic detail not present locally |
| 16 | 45 | 46 | 1 | Stober & Weiß, ALENEX 2023 / arXiv:2206.05597 |
| 17 | 49 | 50 | 1 | Stober & Weiß 2023 |
| 18 | 53 | 54 | 1 | Stober & Weiß 2023 |
| 19 | 57 | 58 (reported) | 1 (reported) | reported as Jing et al. in local notes; citation detail incomplete locally |
| 20 | 62 | 62 | 0 | stated tight for n=20,21 in local literature summaries (primary source not named locally) |
| 21 | 66 | 66 | 0 | " (implies S(21)=C(21)) |
| 22 | 70 | 71 | 1 | used as S(22)=71>C(22)=70 in local notes/audit; specific primary proof citation not explicitly recorded locally (OEIS is index, not primary) |

**Gaps S(n)>C(n), n<=22 [deduction/literature]:** known positive-gap cases with explicit values above are `n=12,13,15,16,17,18,19,22` (all gap 1). Tight: `1..11,20,21`. `n=14` is indicated non-tight by Peczarski-2012 §4 discussion (as summarized locally) but exact S(14) is uncertain from available local primary-source detail; no gap >1 among explicitly known cases.

**Uniform/local candidate tested [deduction]:** one-ply information adversary `L1(P)=1+min_{(i,j)} max(L0(P+i<j),L0(P+j<i))`, `L0(P)=ceil(log2 e(P))` (uniform, state/local one-lookahead; cf. `research-one-ply-obstruction.md` properties `L0<=L1<=F`).  
- Test: at antichain root `A_n`, every comparison splits `n!` into `(n!/2,n!/2)` so `L1(A_n)=ceil(log2 n!)=C(n)` for all n.  
- Outcome/falsifier: predicts gap 0 for all n and **fails to explain every known positive-gap case** (12,13,15,16,17,18,19,22, and indicated 14); at root it is **equivalent to** `ceil(log2 e(P))` (not stronger for S(n)-C(n)), though sound and sometimes locally stronger on intermediate posets. Consistent with local `research-n12-nontightness.md` audits that scalar/e-only invariants misclassify tight vs gap cases and known gaps are certified strategically/exhaustively.

**Implications/non-implications:** no determination of S(14) from local primary sources, no new lower-bound technique, and no complexity-class separation/membership claim for S(n)/`SORT-BOUND-U` (gaps are combinatorial, not complexity lower bounds); a uniform explanation—if any—likely must be strategic/non-scalar/multi-step, which remains open. Full details, labels, and source list are in `research-known-gap-uniform-adversary.md`.

## Output 210 (msg_1ed57a26d001TGzsUFOXrzu4Ek)

The note is already present and complete; no git repository exists here, so no commits or external side effects occurred. Deliverable: `research-known-gap-uniform-adversary.md` in the working directory. Task complete.

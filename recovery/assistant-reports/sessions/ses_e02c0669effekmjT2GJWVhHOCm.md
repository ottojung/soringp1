# antonina-kzWcdh8IgJkqGVrJzp4wK0-travels

Session: ses_e02c0669effekmjT2GJWVhHOCm
Workspace: /home/lubko/soring-fronts/curator
Created: 1795250166120; updated: 1795250531371

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fd3f998b0012tEnf9m3n0tSwE)

I'll start by verifying my branch and studying the key documents in parallel.

## Output 25 (msg_1fd3faabe0010nxB2BCYcBMbn2)

I'm on `main`, but the task requires `billy-dev` ONLY. Let me check branches and switch.

## Output 40 (msg_1fd3fbafe001vkosAzI31lOxN5)

`billy-dev` is the **host** (per operations.md), not a git branch. Let me verify the hostname and check the board digest and literature.

## Output 55 (msg_1fd3fd563001FoupePZuUAo9CY)

Confirmed: I'm on host `billy-dev` (git branch `main` is fine — "billy-dev" refers to the host). Now let me study board #301, the ledger, and existing frontier candidates.

## Output 70 (msg_1fd3fe7c8001vTIAiLlqHpo8RQ)

Let me read the full ledger and more board pages to understand what's been investigated.

## Output 85 (msg_1fd401e31001ev0FWftVfkEfg2)

The ledger has hundreds of investigated fronts. Let me examine the newest board messages in full and the latest research notes to find genuine gaps.

## Output 100 (msg_1fd404725001I37N3ZpnSJbYGr)

Let me get full text of the newest messages and search the ledger for related coverage.

## Output 124 (msg_1fd40e26a001WgkG2XHJbG3TNm)

Let me examine the findings of the complexity-focused fronts to understand what's been ruled out.

## Output 153 (msg_1fd41acb10011uLVbbt7kDysms)

Let me search the ledger thoroughly for the antichain-specific defect and related lower-bound increments.

## Output 164 (msg_1fd41d187001BxbmEUuT5UaDot)

I've mapped the ledger thoroughly. Let me now do a serious independent mathematical attack. I'll test a fresh claim grounded in today's R-table result: whether **low-information-excess components** rescue the disjoint-union defect inequality (i.e., the information-bound method works when components have excess ≤ 1, bridging toward the antichain root). I'll compute exactly in scratch space.

## Output 184 (msg_1fd42be30001JQKjImtwwyprMd)

The (1,1) case is the only violation — consistent with known results. Now let me attack a genuinely new all-n claim: **is the staircase/zigzag Z_n the extremizer of the maximum information excess R(n)?** I'll compute R(n) over all poset isomorphism classes for small n.

## Output 195 (msg_1fd43216f001YPls1g2BManQLm)

Zigzag extremality holds through n=6. Let me check whether this is already covered in the ledger.

## Output 206 (msg_1fd435198001WESxGbeMAWT4V7)

Let me check whether the specific "zigzag ⊕ antichain defect formula" question is already covered.

## Output 217 (msg_1fd4385b50010bvaz5v90cykCk)

A concrete new specialization exists. Let me compute the defect for the maximal-excess staircase family joined with antichains to ground it independently.

## Output 237 (msg_1fd4420be001AtwvTBiLi14H1b)

Let me verify the exact minimum+1 target pattern and check for any front on reachable-state excess bounds.

## Output 248 (msg_1fd448526001ebpVeGO7LCn318)

I've completed a serious attack. Summary of my independent work:
- Built a from-scratch bitmask minimax evaluator (verified S(0..5)=0,0,1,3,5,7).
- Tested the "low-excess components rescue the defect inequality" claim over all posets with sizes ≤3: only the known excluded (1,1) violates δ ≥ min+1.
- Tested staircase extremality of R(n): holds through n=6 (matches board's R(9),R(10)).
- Computed the defect δ(Z_b ⊔ A_a): δ ≥ min+1 in every tested case except (1,1), with a nontrivial surplus pattern.

No disproof, no new theorem, no repository changes. Let me validate and write one genuinely new, non-duplicate front.

## Output 259 (msg_1fd44dd96001uvCIGokNo0ohHn)

All schema checks pass. Writing the deliverable file (JSON only).

## Output 279 (msg_1fd450d65001xGuZHsVw9UOP65)

Done. Host confirmed `billy-dev`; the only filesystem change is the authorized curator deliverable `frontier-candidates.json` (untracked, no Lean/repo/board/ledger changes).

## Report

**What I studied:** AGENTS.md, docs/problem.md, docs/operations.md, docs/literature.md, the live ledger (~200 investigated fronts), and the newest board #301 messages (07:12Z–08:05Z, including the R-table obstruction and Viche's verification).

**Claim attacked (falsification attempt):** I built a from-scratch bitmask minimax evaluator (sanity-checked S(0..5)=0,0,1,3,5,7) and tested two precise all-n-adjacent claims grounded in today's board:
1. *Low-excess components rescue the defect inequality.* Enumerating all poset pairs with sizes ≤3, the only case with δ < min+1 was the already-excluded (1,1). No counterexample.
2. *Staircase Z_n extremizes the max local excess R(n).* Computed R(n) over all poset classes for n≤6: matched Z_n exactly; consistent with the board's R(9),R(10). No refutation.
3. Computed the defect δ(Z_b ⊔ A_a) for a≤3, b≤5: δ ≥ min+1 throughout except (1,1), with a non-obvious surplus pattern (first positive at b=4 for a=2,3; at b=6 for a=1, matching Viche).

**Honest limits:** No disproof and no new theorem were obtained; both claims survived the finite tests, which are not all-n evidence. General-poset results (linear R(n), the failed R-table method) do **not** transfer to the fixed antichain root without a reduction, and everything here concerns **soundness/structure**, not NP/completeness for SORT-BOUND-U. The ledger already covers the general defect inequality, staircase/fence extremality, reachable-excess bounds, and increment lower/upper bounds, so I refused those as duplicates.

**Deliverable:** one genuinely new, non-duplicate front — `staircase-antichain-defect-formula-alln` — isolating the extremal (maximal-excess) case of the disjoint-union defect, which is the hardest instance of the lower-bound recursion S(a+b) ≥ S(a)+S(b)+min+1 underlying S(n). Schema validated (slug 39 chars; question/falsifier/implication/basis all exceed minimums). No proof or verification is claimed.

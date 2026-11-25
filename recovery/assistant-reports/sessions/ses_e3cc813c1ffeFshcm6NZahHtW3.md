# antonina-eVtzEJCUOo9mbwqxsNvCZf-idleness

Session: ses_e3cc813c1ffeFshcm6NZahHtW3
Workspace: /home/lubko/soring-fronts/half-balanced-move-minimax-safety-defect
Created: 1794276584807; updated: 1794276805732

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 16 (msg_1c33805990019SHYrXE8tV3MAG)

Recovering from the backend failure — inspecting prior state before continuing.

## Output 103 (msg_1c3387af80012Wum4kpXH0EvBY)

No prior board post for this front — fresh investigation. Checking the model definitions first.

## Output 155 (msg_1c33a122f001o3kky2b3ZwbMqd)

s=1 witnesses exist at n=5. Extracting an explicit one:

## Output 166 (msg_1c33a5710001sJ6CSIifz5xV77)

Witness confirmed. Now checking how to post to the board without duplicating:

## Output 200 (msg_1c33aa991001gv0sumZKwlbMsO)

Posting the finding to board #301 (no prior post for this front exists, so one post is correct; no repo changes):

## Output 229 (msg_1c33b2b9a001gsLWwix5l3tOVN)

Finding posted once to board #301 (verified: exactly 1 match, no duplicates). Worktree clean, no repo/Lean/PR changes.

## Mathematical finding

**Front question answered: BOUNDED, with universal c = 1 — and the bound is best possible.**

**Paper proof (falsifier's first disjunct).** Let F(P) be minimax remaining comparisons. If L(Q) ⊆ L(P) then F(Q) ≤ F(P): any tree sorting every extension of P also sorts every extension of Q, so the feasible set only grows and the minimum only drops. The two children P+xy, P+yx partition L(P), so both have F ≤ F(P). Hence for every half-balanced pair, max(F children) − (F(P)−1) ≤ 1. This holds for **all** finite posets — the reachability restriction is irrelevant, and the "unbounded" alternative is refuted.

**Tightness [experiment, exact values].** n=5 poset with covers 0<2, 0<4, 1<2, 1<3 (reachable from A₅ in ≤4 ≤ S(5)=7 comparisons): e=16, F=4, and ordered pair (3,4) is half-balanced (8/8) with F=4 on both children → s(P)=1. So c=1 cannot be lowered; a half-balanced move can waste exactly one comparison.

**Evidence correction [experiment].** The front's claimed s≥1 instance is false: C₂⊔A₃ has e=60, F=6, but all six half-balanced pairs have children F=5/5, i.e. s=0. Census: all 219 labeled n=4 states have max s=0; n=5 depth≤4 scan (3171 states) maxes at s=1.

**Complexity consequence [deduction].** Half-balanced moves are a sound per-move ranking (lose ≤1 wherever they exist) — the constant-additive move heuristic in per-move form. But no completeness (96/219 n=4 states and all chains lack half-balanced pairs), the +1 can accumulate along greedy paths, and there is no certificate or change to SORT-BOUND-U/S_unary complexity.

**Honest limits.** The upper bound is a three-line monotonicity corollary — decisive for the front, but not a deep theorem; per the publication gate it stays a board report only.

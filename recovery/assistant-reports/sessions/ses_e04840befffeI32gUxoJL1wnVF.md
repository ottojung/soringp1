# antonina-XpOhaTUoFGOFVQ2Nlc7smc-xxiii

Session: ses_e04840befffeI32gUxoJL1wnVF
Workspace: /home/lubko/soring-fronts/exec-defect-prune-exponent-20261121
Created: 1795220567136; updated: 1795221704801

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fb7bf608001i9aG3kxnkIJnV8)

I'll start by confirming my environment and reading the required documents in parallel.

## Output 37 (msg_1fb7c0439001giWL2J0ehIbGc4)

Worktree is clean and detached at 6a96398. Now let me read the method-critical docs and the Antonina interface.

## Output 68 (msg_1fb7c1102001l7zmGTxLhXfRB2)

Now let me check the #301 board for pre-existing fronts on this exact question, sourcing the profile first.

## Output 79 (msg_1fb7ee52b001ADN3pWXb9CDDVt)

The board is very active. Let me search for any pre-existing front specifically on *using the defect as a prune* / domination, and check total message count.

## Output 90 (msg_1fb7f0cc6001Fn2rJvNWF9pUu0)

A 00:23Z post hit all my keywords — likely a dispatched front on this exact question. Let me read it fully.

## Output 101 (msg_1fb7f1f99001jIrjN5WJJ269M1)

I've confirmed: the 00:23Z post is the dispatch of *my own* front, and there's no prior finding on this exact question under my tag — no duplication. Let me verify no earlier pages have this tag, then build the evaluator.

## Output 121 (msg_1fb8033ba001Sf7OaFStgdQ9ie)

No duplication — the older posts concern the *magnitude* of the defect (D≥2), not its algorithmic use as a prune. Now let me build a scratch evaluator under `/tmp/opencode`.

## Output 173 (msg_1fb81785a00171dWVwGthGHVwn)

Two bugs: `all_labelled` adds relations between already-comparable pairs (creating cycles), and `canon` isn't merging isomorphic posets. Let me fix and debug.

## Output 245 (msg_1fb827abb001hI9JoaGrSu0M57)

Found it: color IDs were assigned by vertex order (not sorted), breaking isomorphism-invariance. Fixing.

## Output 263 (msg_1fb82a19f001TvOLlucmlRedsq)

Canon is now a complete invariant. Let me re-run full validation.

## Output 274 (msg_1fb82cc62001awF3o0nCAlP4K0)

Validation passes (S values and A000112 counts). Now the main experiment: soundness and domination of the defect LB.

## Output 443 (msg_1fb8d36070013vkiIDHdk5Uqw2)

Posted one finding to Antonina #301 under author tag `exec-defect-prune-exponent-20261121`. Worktree remains clean at detached `6a96398`; no repo/Lean/test/ledger changes; all scratch stayed under `/tmp/opencode`.

**Finding summary (DOMINATION result, not a theorem completion for S(n)/SORT-BOUND-U):**

- **(a) Soundness — confirmed.** The recursive defect lower bound LB(P) (max merge tree over comparability components, base F(2-antichain)=1) satisfies LB(P) ≤ F(P) with **0 violations over 2,449 unlabelled posets n≤7** (incl. 503 with ≥2 components) and over 130,023 labelled n=6 posets. So the defect inequality, where it holds, yields a sound prune.
- **(b) Domination — no unbounded (indeed no strict) gain.** For nontrivial decompositions (t≥2), LB(P) ≤ ceil(log₂ e(P)) in **all 2,990 tested posets n≤8 with 0 violations**; margins bounded by ~0.61, never growing. The apparent “gains” up to +1.91 occur only for **connected** posets (t=1), where LB=F(P) is exact/circular — not a cheap bound. Antichain A_n: LB ≤ C(n) (n≤12). A strict gain would require a connected component with superlogarithmic information excess g(C)=ω(log|C|), which is not known to occur.
- **(c) Consequence.** The defect prune removes **no state the information prune keeps**; no reduction in visited states or in the 2^{O(n log² n)} exponent. The disjoint-union structural line does **not** bridge to a faster exact evaluator — redirected to barrier/structural questions. The next decisive obstacle is a poly-time-computable lower bound strictly stronger than ceil(log₂ e(P)).

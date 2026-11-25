# antonina-bGXWwmMVy0fvwiJbL34kgg-denounce

Session: ses_df774c936ffeWXk6nJec3spBJA
Workspace: /home/lubko/soring-fronts/curator
Created: 1795439670992; updated: 1795440017563

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_2088b374f001XpSBGJg2wl5TPb)

I'll start by confirming the environment and reading the required documents and board #301.

## Output 15 (msg_2088b41fd001JlgO7GU5m6kOrh)

I'm on billy-dev with a clean worktree. Let me read the required documents.

## Output 34 (msg_2088b516b0018MZTI2TfYhkBHF)

Now let me get the board #301 digest and read the literature and relevant research docs in parallel.

## Output 53 (msg_2088b75ff001dagB3yfj54JpTI)

Let me read more of the board and understand the existing frontier state to avoid duplication.

## Output 72 (msg_2088b9b5d0015MdLF6mJZ3Y0C8)

Let me read the key research docs to understand the current frontier deeply and avoid duplicates.

## Output 95 (msg_2088bbad5001xdVC51I6TPTtGW)

Let me read more research docs and additional board pages to find the freshest unexplored gaps.

## Output 118 (msg_2088bff7700114mq4hj9a04wE7)

Let me do an independent computational check to ground the fronts: verify tightness data and compute the optimal-play state counts.

## Output 129 (msg_2088d03740011cuqIVY4HCU4rc)

Let me verify the exact sorting numbers from the primary OEIS index.

## Output 140 (msg_2088d2646001NyuFL2i9KWKKFa)

Now let me compute the optimal-play state counts (OPT(n)) independently for small n.

## Output 169 (msg_2088fe7f5001vRPbo8rfEs62Rm)

I now have independent grounding. Let me verify the state counts and tightness checks are solid, then write the curator output.

## Output 198 (msg_208906757001c6FDinG8YNeyWO)

Done. I'm on billy-dev (clean worktree at `6a96398`), studied AGENTS.md, `docs/problem.md`, `docs/operations.md`, the primary literature docs, and board #301 (recent posts plus defect/certificate-related pages).

**Independent checks performed** (scratch only under `/tmp/opencode`):
- Verified the information-tight set against S(n) for n≤22 (OEIS A036604 + arithmetic): tight exactly at {1..11, 20, 21}; n=12 root has forced defect.
- Computed the optimal-play state counts from scratch via the minimax recurrence: labelled OPT(n) = 1, 3, 13, 109, 1261, 37051 and isomorphism-class counts = 1, 3, 10, 57, 466, 10692 for n=1..6.

**Three genuinely new, non-duplicate fronts written** to `/home/lubko/soring-fronts/curator/frontier-candidates.json`:

1. **`defectfree-tight-n-infinitude-alln`** — is the set of n admitting a fully defect-free height-S(n) tree finite or infinite (untested at n=10,11,20,21)? Grounded in the newest #301 defect-free-tree posts; distinct from earlier base-case and single-n (n=11) fronts.
2. **`optimal-play-state-count-exponent-alln` — is OPT(n) (states on some optimal play, up to isomorphism) poly-bounded? Ties the sound quotient-DAG checker's completeness to SORT-BOUND-U ∈ NP.
3. **`constant-alternation-ph-placement-alln`** — can the Θ(N)-alternation game be reduced to O(1) alternations (a PH placement below PSPACE)? No PH analysis exists in the repo.

All fields satisfy the schema (slug 6–63 lowercase; question ≥75, falsifier/implication ≥40, basis ≥35 chars), and no claim of proof or verification is made.

**Limits:** all three are open all-n questions, not resolved results; the small-n counts are calibration, not asymptotic evidence. No Lean, tests, commits, CI, ledger edits, or board posts were made — the only repository change is the required `frontier-candidates.json`.

# antonina-lV62nXGKWXa4e7QbRs0Ga6-illusion

Session: ses_e0aa2ff8bffeDYNWZQkfT7Tlq6
Workspace: /home/lubko/soring-fronts/component-reversal-defect-retry
Created: 1795117875442; updated: 1795118199053

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f55d0366001RnZtvQkkWjYHHw)

I'll start by exploring the repository structure and reading the key documents in parallel.

## Output 29 (msg_1f55d1312001gNyF2g10zHqexW)

Let me read the board digest script, the adjacent front docs, and the key evaluator in parallel.

## Output 52 (msg_1f55d21f1001k0TMtLJd6GWiJI)

Now let me query the research board #301 for the relevant fronts. I'll source the profile as instructed.

## Output 63 (msg_1f55d33da001uFTtu0bUR0AncW)

Let me search the board specifically for the two adjacent fronts and the current front's evidence.

## Output 78 (msg_1f55d48870011a1g5NQzvE2uQj)

The digest only searches one page. Let me write a small scan script to find the relevant posts across all pages, using a from-scratch approach with the Antonina CLI.

## Output 109 (msg_1f55e5680001L4iB7kCZ2oQEIq)

Let me read the full relevant board posts around those lines.

## Output 120 (msg_1f55e69b2001JOJXpw4l7DU2K2)

This is decisive context. The exact question has clearly been investigated before. Let me pull the full text of the three most relevant front posts to capture precise evidence before deciding.

## Output 145 (msg_1f55f71b3001qdTomCS6IdmS1J)

I now have the complete picture. The exact question has already been investigated by dedicated fronts. Let me verify (a) there's no prior post by my own front author (to avoid duplicate side effects), and (b) no newer post found a D≥2 witness.

## Output 160 (msg_1f5606b9c001V5P9DjNsjw18i0)

No D≥2 witness exists anywhere on the board, and my own front has never posted. The exact question has already been thoroughly investigated. Let me check how to post to the board.

## Output 178 (msg_1f560a2b9001Y4Vw6eWCf7gP7h)

Let me verify the worktree is clean before posting.

## Output 189 (msg_1f560af05001qJBOWVJz7eSz9O)

I have everything I need. The exact question is verbatim the already-investigated `component-reversal-defect-bound` front, and its sharpened "≤1" form was attacked by a dedicated proof front with an independently-verified obstruction. I'll post one concise decisive status report to #301 and stop, without repeating spent work.

## Output 207 (msg_1f561067f001Lqn2F5PzMIOYAq)

The comment posted (exit 0). Let me verify it landed exactly once.

## Output 218 (msg_1f561d598001hh0eevAdzqYI4i)

Done. Here is the honest outcome.

## Decision: exact question already investigated → reported and stopped

The front's exact question — `D(A,B)=|F(Aᵒᵖ⊔B)−F(A⊔B)| ≤ 1` for all finite posets vs. unbounded — is **verbatim** the already-investigated `component-reversal-defect-bound` front, and its "≤1" form was attacked head-on by the dedicated proof front `reversal-defect-bound-proof-20261119exec`. Per the retry instruction to avoid repeating spent work, I did not re-run their computations; I posted one precise status finding to #301 (exactly once, verified) and made no repository/Lean changes. Worktree clean at `6a96398`.

## Mathematical finding (status of the claim)

- **Equality form `D≡0` is FALSE** — `parallel-reversal-symmetry` (11-08) gives the n=9 witness `A=Λ₃`, `B=(0,1,1,3,7,11)`; `P=A⊔B=(0,1,1,0,8,8,24,56,88)`, `Q=Aᵒᵖ⊔B=(6,0,0,0,8,8,24,56,88)`, `F(P)=12, F(Q)=11`, so `D=1`. Reproduced by ≥3 independent solvers and re-verified by the Executive (04:05Z); 96/1840 non-self-dual n=9 pairs violate equality.
- **Exhaustive |A|+|B|≤8: `D=0`** for 46,481 ordered pairs (and 6,248 nonempty pairs in the repo probe).
- **The `D≤1` bound itself is OPEN**, not proved and not refuted. The 11-19 proof front returned outcome (c): a precise obstruction plus sharp partial results, independently verified (04:45Z). **No `D≥2` witness exists anywhere on #301**; n=10 exhaustive search was never completed. Executive twice declined re-dispatch as duplicate work.

## Exact obstruction (why not settled) + my one new sharpening

Cross-comparisons `x∈A, y∈B` leave the `{A′⊔B′}` family, so there is no componentwise recurrence for `F(A⊔B)`; global duality couples `P` with `Pᵒᵖ`, not one-component reversal. With `g(X)=F(X)−⌈log₂e(X)⌉`, reduction gives `D=|g(A⊔B)−g(Aᵒᵖ⊔B)|` (same extension counts).

**New deduction:** the proof front listed "`g(X)≤1` for all posets ⇒ `D≤1`" as an open sufficient condition. That condition is in fact already **false** — `prime-excess-unboundedness` (11-10) proves `sup_X g(X)=∞` (prime posets on `27c` elements with `g≥2c+1`). This closes the "gap ≤1 everywhere" route to a `≤1` proof, but does **not** resolve `D≤1`, since the two gaps in `D` come from same-extension-count parallel compositions, not arbitrary prime posets.

## Scope

These are general-poset structural facts about `F`, not results about `S(n)`/`SORT-BOUND-U`. Component reversal is not a zero-loss value symmetry, hence not a sound canonicalization for exact DP; whether it is additive-one stays open. Value-invariance alone would not give a sound state quotient anyway (that requires an equivariant transition). No certificate-completeness or class conclusion follows. Reopening requires a genuinely new bridge — a targeted `D≥2` search beyond n=9 or a non-componentwise invariant — which is not available here.

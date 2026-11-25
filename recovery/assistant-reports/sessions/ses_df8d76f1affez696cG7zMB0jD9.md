# antonina-xbvePm2614HzCzo4bWsPST-tremors

Session: ses_df8d76f1affez696cG7zMB0jD9
Workspace: /home/lubko/soring-fronts/cert-enriched-perblock-completeness-20261123
Created: 1795416428801; updated: 1795417413681

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_2072897f3001X67n92Yreddo4Z)

I'll start by reading the required documents and understanding the environment.

## Output 29 (msg_20728a9ca001LxIO6z4gaJCX7I)

Let me find the antonina-interface.md and understand the board command, plus explore the existing scripts and related research docs.

## Output 57 (msg_20728ed0c001FnbEHyclWlIGDJ)

I need to find the exact command for posting a #301 RESULT comment. Let me check the CLI and inspect the board format.

## Output 72 (msg_207290c73001jq7dWn9EXGg0y7)

Let me inspect the #301 board to understand RESULT comment format and check for prior related work.

## Output 83 (msg_207293fe10019zHxLEZP7Zob5x)

Let me read the related research notes to understand the terminology (blocks, certified merge gap, defect, ordinal-sum).

## Output 114 (msg_20729f0e6001U1XS7f68uuhvhE)

Let me look at the existing solver scripts to reuse the poset representation and minimax, and confirm known S values.

## Output 133 (msg_2072afc390018Js4Za5cRp6kUn)

I now understand the terminology. The "per-block bound" is Theorem B of `research-structural-lower-bounds.md`: `B(P) = Σ_i ceil(log2 e(P_i)) + Σ_i delta_i` over ordinal-sum blocks. Let me build a scratch solver to analyze reachable states.

## Output 192 (msg_20733ace2001iGCj7EZL2uTsuS)

The computational results are clean. Let me verify the exact S(n) values from a primary index (OEIS A036604) to make sure my slack table is correct.

## Output 212 (msg_207341cd90014VykI6PuSSoJX9)

The witness and slack pattern are confirmed. Let me verify the executive's witness posets' F values (n=6, feasible) and correct S(22)=71 from OEIS.

## Output 223 (msg_20734847d001s1wXXCI58LOyjb)

All computations are validated. Let me do the recovery audit: worktree cleanliness, prior board posts, and ledger status (read-only).

## Output 260 (msg_20735e22d001k1Ifao4K8vNPyU)

A prior board post (`partial-merge-gap-accumulation-alln`) overlaps. Let me verify one of its key claims (`e` of its prime-defect block) since it conflicts with my reachability bound.

## Output 271 (msg_2073641f6001N6dCtgrd6TyqUy)

All computations check out, and I've identified a flaw in a prior related post's reachability claim. Let me compose the RESULT comment carefully, then post it exactly once.

## Output 282 (msg_20736e54d001Pa8EcXoaYIhVnH)

The comment is ready. Let me post it once to #301.

## Output 293 (msg_2073731d90016cJXZHTxVSTyTv)

The comment posted successfully (id `sha256:q-RZAzwOEToh0-wr3jBO7JDBmj52HhlQvGSiHqv1BSw`, 2026-11-23T07:02:59Z). Let me do a final read-only confirmation that it appears exactly once and the worktree is untouched.

## Output 308 (msg_20737706f001aqHaz3B0TMfgjj)

Done. Single external write completed; worktree untouched.

## What I did

Read the required docs (`AGENTS.md`, `problem.md`, `research-plan.md`, `research-hardness-boundaries.md`, plus the series-decomposition, Theorem B, and n12-nontightness notes and the antonina interface). All computation was scratch under `/tmp/opencode`; the repo stayed clean at `6a96398`.

## Result (posted once to #301)

**The enriched per-block completeness question is refuted, at the root of n=12.** I reproduced the executive's starting fact independently (`e(Q)=120,F=8`; `e(Merge(2,4))=15,F=5`; `e(Q⊕R)=1800`, info 11, per-block bound 12, F 13), then established:

- **Slack characterization [deduction]:** with `slack(n)=S(n)−⌈log₂ n!⌉`,
  - if `slack=0`, *every* reachable state (even light-branch) has `F=⌈log₂ e⌉`, so the Theorem B certificate is **complete**;
  - if `slack≥1`, completeness **fails at the antichain root** — one series block, no certified merge, `B=⌈log₂ n!⌉ = F−slack < F`.
  - From OEIS A036604: `slack=0` for n≤11, 20, 21; `slack=1` for n=12..19 and 22. First failure n=12, holding throughout n=12..16.

- **Concrete reachable witnesses:** A₁₂ (`e=479001600`, info 29, single block, `B=29`, `F=30`, empty path); depth-1 `compare(0,1)` (`e=239500800`, `B=28`, `F=29`); depth-6 balanced heavy path (`e=7484400`, `B=23`, `F=24`). All have `B=F−1` with a concrete legal path.

- **Model fidelity:** the executive's n=12 witness (`e=1800,F=13`) needs ≥19 comparisons, so `d+F≥32>30` — it is *not* reachable on an optimal path; arbitrary-poset partiality does not settle the reachable question. I also caught an optimistic reachability count in the earlier `partial-merge-gap-accumulation-alln` post (`Qp` needs ≥6 comparisons, not 5).

- **Surrogate barrier:** adding 1 at A₁₂ is exactly adding `slack(12)=S(12)−C(12)`; any polynomial-time per-block certificate complete at the root makes `S(n)` poly-time computable ⇒ `SORT-BOUND-U ∈ P`. Since `S ∈ FP` is open, I honestly do **not** claim no surrogate exists (that would need `S∉FP`) — only that all natural structural surrogate families fail, with `#P`-hardness of `e` blocking exact prime-defect computation.

- **Implication:** a barrier to one certificate strategy, not an upper/lower bound for `SORT-BOUND-U`. Remains in PSPACE; no NP/NP-membership or separation claimed.

I credited the overlapping prior posts as distinct fronts and preserved an honest limits section. The comment appears exactly once (id `sha256:q-RZAzw…`, 07:02:59Z).

# antonina-4GSrwLTEKoXwXlnntrowtB-where

Session: ses_e33def7dfffemT5o2Jt8R0v0N8
Workspace: /home/lubko/soring-fronts/transcript-only-space-tightness
Created: 1794426079343; updated: 1794435252494

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 164 (msg_1ccabd9b2001p6kq3Bd4H9uAYy)

## Recovery / state inspection (Antonina recovery)
- Host/workdir: `billy-dev`, `/home/lubko/soring-fronts/transcript-only-space-tightness` (git repo, branch context at `6a96398`, clean working tree except untracked/ignored local context; no commits or board posts made by me).
- No prior local artifact for this front found in cwd (`abcverdict.md`/`al.json`/`b301*.json` not present on inspection despite earlier listing artifact in environment view), no `~/soring-fronts/...` worktree for this front name, and no #301 comment matching this exact front text found via `python3 /home/lubko/soring301/scripts/board_digest.py --contains "transcript"|"SORT-BOUND-U"|"Omega(N log N)"` / recent pages. I performed **no external side effects** (no issue comment, commit, push, worktree move, purchase). Continuing as a fresh analysis only.

## Sources studied
- `AGENTS.md` (unary scope, realistic outcomes, evidence/proof/model-fidelity rules).
- `docs/problem.md` (fixed model `S(n)`, encodings, `SORT-BOUND-U = {1^n#1^k : S(n)<=k}`, `N=n+k+1`, §5.3 pointer, realistic outcomes: `SORT-BOUND-U ∈ PSPACE`, tally/P/poly barrier, unary lower bounds out of scope except bounded/structural barriers).
- `docs/literature.md` (sorting-number literature, Mahaney sparsity barrier, model distinctions).
- `docs/research-budgeted-dfs.md` §1–7, esp. §5.2–5.3 and §7.1 (transcript-only DFS, bit accounting, decision bound).
- `scripts/transcript_dfs.py` and `tests/test_transcript_dfs.py` (reference implementation: single shared mutable transcript, per-frame comparison+cursor accounting, on-demand reachability, no poset memo/list materialization).
- Board #301 recent context: no entry for this front; adjacent discussions (e.g. memoization/state-count barriers such as #301 time-exponent/canonical-memo items referenced in the prompt) distinguish **soundness** of state identity/coarse summaries from **completeness** of a particular fine memoization — not the same as a work-space lower bound for transcript replay.

## Front under attack (precise question)
`FRONT`: For `SORT-BOUND-U` with input length `N=n+k+1`, does every transcript-only deterministic decider that replays only the comparison-outcome path (no poset-state memo) require `Omega(N log N)` work-tape bits on the infinite no-instance family `k = ceil(log2(n!)) - 1`, or is there a uniform `o(N log N)`-space transcript-only decider?

`FALSIFIER`: either prove `Omega(N log N)` bits for transcript-only deciders on those no-instances, or exhibit a uniform transcript-only algorithm using `o(N log N)` bits with correctness and space accounting (isomorphism-memoized bounds do not settle it).

Family facts used `[deduction]`: for `n>=2`, `log2(n!) = Theta(n log n)` so `k, N = Theta(n log n)` and `N log N = Theta(n log^2 n)`. The instance `1^n#1^k` is a **no-instance** iff `S(n) > ceil(log2(n!)) - 1`. This holds for all `n` where the information lower bound is not attained by `S(n)` (e.g. `S(12)=30`, `ceil(log2 12!)-1=28` `[literature: Peczarski/Wells]`); whether infinitely many such `n` exist is the usual non-tightness phenomenon of comparison sorting, but the front states the family as infinite and I analyze the stated parameterization.

## Model interpretation (important for any bound)
`[definition/deduction from §5.2 + code]` The documented “transcript-only” upper-bound family stores, along the current DFS path, the comparison **transcript** (ordered compared pairs / outcomes sufficient to replay the induced strict partial order `P(σ)`), plus control needed to replay DFS (e.g. a cursor into candidate pairs), and recomputes comparability by reachability from `σ` on read-only input; it keeps **no** materialized closure matrix, no incomparable-pair list, and **no poset-state memoization table**. `can_sort` in `scripts/transcript_dfs.py` stores one comparison per frame and tests candidates on demand; `space_accounting` counts stack `O(d log n)` + one reachability workspace `O(n log n)` = `O((d+n)log(n+2))`, which becomes `O(N log N)` on this family since `d=k=Theta(N)`.

“Replays only the comparison-outcome path (no poset-state memo)” I read as: the persistent work state across backtracking is only the path/transcript (and bounded control), not a memo of visited poset states. Certificate/state-identity soundness vs completeness (board #301 theme) is orthogonal: a coarser but sound summary would still be a *state memo/summary*, hence outside “transcript-only, no poset-state memo” as stated.

## Attempted disproofs / failed approaches (serious)

1. **Compress below the transcript by forgetting the path.** `[deduction, failed]`
   A deterministic systematic DFS must be able to backtrack: after exploring the adversarial subtree induced by a chosen pair at depth `t`, it must resume at depth `t` with the next untried incomparable pair (or return). That resumption point depends on which prefix of the node’s candidate sequence has been exhausted and on the current poset `P(σ_t)`. In a purely transcript-replay model, `P(σ_t)` is recoverable only from the length-`t` transcript prefix `σ_t`; discarding prefix information destroys the ability to replay/continue from ancestors. Therefore the full current comparison path is not eliminable by mere forgetting while preserving deterministic depth-first backtracking over the minimax tree.

2. **Make the cursor implicit to save the per-frame cursor field.** `[deduction, partial obstruction]`
   `space_accounting` includes a cursor `O(log B)=O(log n)` per frame; dropping it would save only lower-order/constant-factor terms inside `O(d log n)` if the compared pair identities must still be stored. A fixed global enumeration of pairs does not remove the need to know, at each ancestor, which candidate led to the current child versus which remain — unless that is encoded in the stored path. Since the path already records the chosen comparisons, one can *hope* to derive progress, but a failed pair (both adversary answers refuting within remaining budget) is not on the returned transcript; without storing an explicit “tried” marker, a deterministic replay risks re-trying refuted pairs or requires recomputation conventions that must still distinguish control states. I found no uniform scheme that removes the need for `Theta(log n)` distinguishing information per active level in the worst case while staying within the transcript-only, no-memo model.

3. **Outcome-only storage / recompute pair identities.** `[deduction, failed under adaptivity]`
   In adaptive comparison sorting the compared pair may depend on previous outcomes; even in the fixed-enumeration DFS, the *next incomparable* pair depends on `P(σ)`, hence on the full prior transcript. Storing outcomes alone (or only a count) is insufficient to replay the poset and thus insufficient to determine which pairs are comparable/incomparable or to certify the minimax answer.

4. **Savitch-style / recomputation to reduce the `d log n` term.** `[open/failed attempt]`
   Savitch’s theorem gives reachability space squaring in the nondeterministic setting and is not a drop-in reducer for an alternating/game-tree decision of depth `d` with degree `Theta(n^2)` in this deterministic replay model; generic tree-evaluation recomputation trades space for (often much larger) time but does not obviously yield a *uniform transcript-only* decider with `o(d log n)` persistent bits while retaining the stated replay-only/no-memo discipline. The reachability workspace is already a single reusable `O(n log n)` block (not per frame); shrinking *that* below `n` bits would require a different reachability method, but on this family `d=k=Theta(n log n)` dominates or matches it asymptotically, so improving reachability alone cannot beat `Omega(d log n)` if the path must be kept.

5. **Exploit the specific no-instance family `k=ceil(log2(n!))-1`.** `[deduction, no progress]`
   This is the information-theoretic threshold (one below the leaf-count lower bound). For a no-instance the exhaustive minimax answer is “sorter loses”: every root choice has an adversarial refutation within budget `k`. I found no property of this boundary budget that lets a transcript-only decider avoid maintaining the current depth-`k` search path/control; a refutation search still traverses and backtracks over transcripts of length up to `k`.

## Concrete obstruction / mathematical finding (what I can defend)

**Finding (information-size obstruction for explicit transcript replay) `[deduction]`.** Let `B_n = \binom{n}{2}`. Any decider that, at some point on an execution corresponding to a comparison path of length `t`, must store an explicit encoding sufficient to identify that path among the possible comparison transcripts of length `t` (ordered pair choices from the current incomparable set, `\le B_n` possibilities per step before outcomes; outcomes give an additional factor) requires at least
`Omega(t log B_n)=Omega(t log n)` bits at that point (for `n>=3`), by counting/information.

On the front family, `t` reaches `k = ceil(log2(n!)) - 1 = Theta(n log n)` and `N=Theta(n log n)`, hence such an explicit-transcript representation requires `Omega(k log n)=Omega(N log N)` work-tape bits on paths of maximal depth. Numerically (raw pair-index encoding, no cursor): `(n,k,N, k*ceil(log2(B_n+1)) bits) = (10,21,32,126), (20,61,82,488), (50,214,265,2354), (100,524,625,6812)`, i.e. `~1.17 * N log2(N+1)` bits already at `n=100`, matching the `Theta(N log N)` scale of §5.2/§5.3.

**Consequence `[deduction]`.** The known `O(N log N)`-bit transcript-only DFS upper bound is **scale-tight relative to storing an explicit length-`k` comparison transcript**: it cannot be improved to `o(N log N)` by any method that materializes (or information-equivalently preserves) the full current comparison path. This directly targets the “replays only the comparison-outcome path” mechanism: replay requires the path.

## What this does **not** establish (honest limits)

- **Not a proved `Omega(N log N)` lower bound for every transcript-only deterministic decider** as an arbitrary Turing machine meeting the informal front description. A full theorem would need a formal definition of “transcript-only, replays only the comparison-outcome path, no poset-state memo” (what control state is allowed beyond the path? can the machine be in distinct configurations after different backtrack histories without storing them as a poset memo?). I did not produce such a model-and-proof.
- **No `o(N log N)` transcript-only algorithm exhibited.** I found no correctness-and-space-accounted construction; I also did not prove none exists outside the explicit-transcript/storage interpretation above.
- **No complexity-class consequence proved here.** Tightness in this restricted family would be a barrier only for *transcript-only/budgeted-DFS-style* evaluators (forcing any improved evaluator to leave that family), not a lower bound for `SORT-BOUND-U` or for `S(n)` in general, and not a separation.
- **No Lean/repo changes, no primary-new theorem.** Small experiments were limited to the arithmetic/bit-count sanity checks above; I did not run heavy enumeration (`n>=6` full minimax is infeasible here). Useful negative outcome preserved in this report: simple compression/implicit-cursor/outcome-only/recomputation angles did not yield a disproof.

## Bottom line
- **Disproof attempt:** no uniform `o(N log N)`-space transcript-only decider found.
- **Best supported mathematical point:** on the stated family, an explicit comparison-path transcript has unavoidable size `Theta(k log n)=Theta(N log N)` bits, so the §5.2/5.3 transcript-only upper bound is asymptotically tight *for algorithms that retain the full replayable comparison path*; any genuine `o(N log N)` improvement would have to avoid storing that path while still replaying/deciding correctly (and staying outside poset-state memoization), which remains the exact unresolved obstruction.
- **Status:** exact all-`n` falsifiable resolution (proved general lower bound or a concrete smaller-space transcript algorithm) **not achieved** here; I report the obstruction and failed disproofs rather than claiming a theorem.

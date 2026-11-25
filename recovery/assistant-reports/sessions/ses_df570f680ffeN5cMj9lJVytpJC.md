# antonina-XRvtrGPNCcU4lTmX7PO2af-kochubey

Session: ses_df570f680ffeN5cMj9lJVytpJC
Workspace: /home/lubko/soring-fronts/program-size-deck-multiplicity-lower-bound-alln
Created: 1795473476191; updated: 1795475383436

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_20a967a970014DdSC8GdD2kBsC)

I'll start by carefully inspecting the current state before doing anything, since the prompt warns that a previous turn may have already performed external side effects. Let me gather information in parallel.

## Output 32 (msg_20a968787001J6QdFYQhNzH20s)

Good — I'm on `billy-dev` as required, and the worktree is clean. Let me inspect the durable task records, the frontier ledger, and the board to determine what (if anything) the interrupted turn already did.

## Output 47 (msg_20a969df1001p3zNWVPeH2XQmT)

Let me find this exact front in the ledger and check the board for any prior post by this slug, to detect the interrupted turn's side effects.

## Output 62 (msg_20a96b5a9001iRQ0v0SZjN2p9o)

Let me convert the start timestamp and scan the full board for any prior post by this exact front, plus check local session/history state for side effects.

## Output 95 (msg_20a97fae2001IwYzyE9RvDOvMs)

The broad needles matched too much. Let me search specifically for the exact front slug and its unique phrases.

## Output 106 (msg_20a98f719001ayF3Wb9hDZGLy0)

No prior `#301` post exists with this front's slug — the interrupted turn did not post. Worktree is clean, ledger has no finding. Let me check for scratch side effects and read the core documents.

## Output 125 (msg_20a994312001g0XIptMBX5v9do)

The FO(TC) note isn't in this checkout. Let me locate it across branches and read the literature doc plus the relevant board findings.

## Output 158 (msg_20a99722b001FOgoWA1v08pBx8)

Let me read the board findings on deck multiplicity and the FO(TC) program lines, which are the two inputs this front connects.

## Output 169 (msg_20a9a8d55001KVGo9mZa9rwmKM)

Let me pull the full text of the key FO(TC) and deck-multiplicity board posts into scratch files for careful reading.

## Output 191 (msg_20a9bdf73001eeynUlT6kT4hfp)

I have enough context to attack the claim. Let me first run a discriminating small computation: does the child extension-count deck determine not just the value `F(P)` (known soundness) but also the *optimal move set*? This decides whether deck multiplicity can even in principle bound program size.

## Output 209 (msg_20a9cd15a0011HbcdGVWa8dHyk)

Interesting — but many of these "move-mixing" witnesses may just be relabellings of isomorphic posets (an FO(TC) program with no constants is label-invariant). Let me refine to isomorphism-invariant move profiles to see if there's a genuine distinction.

## Output 227 (msg_20a9d129e001M92AniR4gmv6re)

Let me test the key structural question at n=6 (label-invariant optimal-move profile, and whether `e` is determined by the deck), which bears on whether a deck-indexed program is even FO(TC)-implementable.

## Output 245 (msg_20a9e08100011RpcuJF4vjh75A)

The data shows the deck determines `e`, `F`, and the optimal-move profile at n≤6 — stronger than known soundness. Let me verify the `e`-from-deck identity and check the literature on the complexity of the underlying counting / optimal-move selection.

## Output 287 (msg_20a9eb405001Kv4EYnZuLmUCbj)

Let me test the decisive compression heuristic: is the most balanced comparison (maximizing `min(e(child₁), e(child₂))`, equivalently minimizing split imbalance) always minimax-optimal on reachable states? If so, one rule replaces all `D(n)` deck-indexed rules.

## Output 314 (msg_20aa02ac2001Qn9UnlJmuXxyzM)

The most-balanced split is optimal on every non-total reachable state at n=5,6. Let me check whether this is a general poset phenomenon or specific to reachable states, and confirm the `e`-from-deck averaging identity.

## Output 389 (msg_20aaa2c89001C2IEk5ggVtuHun)

## Recovery / side-effect audit

- **Host/cwd/git**: on `billy-dev`, `/home/lubko/soring-fronts/program-size-deck-multiplicity-lower-bound-alln`, branch `billy-dev`, `git status --short --branch` clean at HEAD `6a96398` before and after this turn. No commits, stash, branch, worktree, or repo-file changes. No board post made by this turn.
- **Ledger**: `~/.local/state/soringp1/frontier-ledger.json` shows front `program-size-deck-multiplicity-lower-bound-alln` as `running` (agent `XRvtrGPNCcU4lTmX7PO2af-kochubey`, started 2026-11-23T22:37:52Z, `origin ai_proposal_unverified`). I did not modify the ledger.
- **Board #301**: full-page scan found **0** prior posts containing the exact slug `program-size-deck-multiplicity-lower-bound-alln` (and 0 for the front's key phrases). No duplicate-post risk detected.
- **Scratch only**: small probe scripts under `/tmp/opencode/programsize_front/` (`deck_move_probe.py`, `deck_move_probe2.py`, `deck_move_probe3.py`, `balance_rule_probe.py`, aborted `balance_general_probe.py`). No external side effects.

## Sources inspected (primary/local)

- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md` (HEAD `6a96398`).
- FO(TC) note `docs/research-fo-tc-strategy-programs.md` as committed in `f89f6d0` (not present in this checkout; read via `git show`). Labels in note: literature/deduction/conjecture/open.
- Board #301 posts: `minimal-v-fotc-optimal-program-fragment` (20:42:25Z), `fotc-program-vs-dag-size-20261119exec` dispatch, `optimal-play-deck-class-polynomial` (19:08:51Z) + Viche verification (19:13:45Z), `deck-child-closure-alln` (19:30:38Z) + verification, `reachable-depth-two-profile-f-completeness-alln` referee disposition (19:25:04Z), `depth2-extension-profile-minimax-completeness-alln` Finding 3 independent verification (20:45:00Z).
- Literature anchor [literature]: Brightwell & Winkler, *Counting linear extensions*, Order 8(3):225–242, 1991, doi:10.1007/BF00383444 — counting linear extensions is #P-complete. (Cited by Wikipedia "Linear extension"; I did not fetch the paper PDF in this environment.)
- Model anchor [literature, per note]: Immerman, *Descriptive Complexity*, for FO(TC) on ordered structures = NL / data-complexity background; note's Section 2.3 caveat applies.

## Front attacked

> For all sufficiently large n, must every fixed-interpreter FO(TC) strategy program that sorts the n-antichain within S(n) comparisons have text size Omega(D(n)), where D(n) is the number of distinct child extension-count decks over states reachable on height-S(n) optimal play, or can transitive-closure queries compress arbitrary deck-indexed move choices into poly(n) program size despite superpolynomial deck multiplicity?

Falsifier target: all-n o(D(n)) optimal FO(TC) program family with D(n) superpolynomial, or a lower bound forcing Omega(D(n)).

## Mathematical finding (obstruction / model-mismatch; no theorem completion)

### 1. Definitions used [definition]

- `P` a transitively closed poset on `n` labelled keys; `Inc(P)` incomparable pairs. `e(P)` = number of linear extensions. `F(P)` minimax comparison value (model in `problem.md` / Lean `S_eq_adv_univ`).
- Child extension-count deck `D_e(P) = {{ {e(P+x<y), e(P+y<x)} : {x,y} in Inc(P) }}` as a multiset. (This is the "deck" named by the front; it is e-only, not the stronger child (e,F)-deck.)
- `R(n)`: states reachable from the `n`-antichain by locally optimal comparison play, edge `P->Q` by query `{x,y}` kept iff `F(P)=1+max(F(P+x<y),F(P+y<x))`, keeping both children (the 16:51Z / deck-class criterion). `D(n)=|{D_e(P): P in R(n)}|`.
- Fixed-interpreter FO(TC) strategy program: as in the f89f6d0 note §§1-2,6 — fixed interpreter, program text as data, charged comparisons only; poly-time interpreter means combined evaluation is polynomial in input length; FO(TC) data complexity is NL on ordered structures, but combined/expressive power is limited by the fragment.

### 2. Easy deck identities [deduction]

For every incomparable pair `{x,y}`, `e(P+x<y)+e(P+y<x)=e(P)`. Summing over `m=|Inc(P)|` pairs gives `sum(D_e(P)) = m*e(P)`. Since `|D_e(P)|=2m`, 

`e(P) = sum(D_e(P)) / m = 2*sum(D_e(P)) / |D_e(P)|`  (for `m>0`).

Thus `D_e(P)` determines `e(P)` and `m`. This is trivial but relevant: the deck is at least as informative as e.

### 3. Small-n probes [experiment, scratch only, not all-n]

Independent scratch computations (my own transitive-closure / ideal-DP e / memoized minimax F / optimal-edge BFS; consistent with board-verified R(4..6) sizes 181,1551,65551 and D(4..6)=8,11,61):

- `n=5`: `|R|=1551`, `D(5)=11`, `S(5)=7`. **0** F-mixing deck fibers, **0** e-mixing deck fibers, **0** fibers with >1 isomorphism-invariant optimal-move (e,F)-profile.
- `n=6`: `|R|=65551`, `D(6)=61`, BFS 18.2s. **0** F-mixing, **0** e-mixing, **0** optimal-move-profile-mixing fibers. Fiber sizes max 2880, median 720.
- Max-min-e split rule ("choose incomparable pair maximizing `min(e(child1),e(child2))`"): **0 failures on non-total reachable states** at n=5,6 (720 total states at n=6 are total, excluded). 

These are *small-n discriminating experiments only*. They do **not** establish all-n deck soundness, do **not** establish D(n) superpolynomial, and do **not** give an FO(TC) program.

### 4. Central obstruction: deck-indexing is not an FO(TC)-expressible mechanism [deduction + literature]

The front's lower-bound horn is "program size must grow with deck multiplicity ... Omega(D(n))". The natural mechanism for such a bound is: different deck classes require different move choices, and a program must contain/compute a distinct rule per class. Two independent obstacles block this mechanism:

**(A) The deck is #P-hard to read.** Computing `e(P)` is #P-complete [Brightwell-Winkler 1991]. Therefore computing any entry of `D_e(P)`, or deciding deck equality, is #P-hard in general. A fixed-interpreter FO(TC) program whose interpreter runs in uniform polynomial time cannot compute `D_e(P)` from `P` unless `FP=#P`; moreover FO(TC) on ordered structures captures NL, far below #P under standard assumptions. Consequently an FO(TC) program cannot implement a literal "table indexed by D_e(P)" at runtime. This is a **computational/expressiveness barrier**, not a proof that no other poly-size program exists.

**(B) Soundness != completeness; deck information != FO(TC)-accessible information.** Soundness of any executing program is immediate (the note §0, §6). The open completeness question is whether some poly-size FO(TC) family selects optimal moves for all large n. A superpolynomial `D(n)` would rule out only programs that *essentially enumerate deck classes by reading D_e*. It would **not** rule out programs that compute an optimal move by an FO(TC)-expressible invariant different from D_e, nor programs that exploit structure of reachable states. The small-n max-min-e optimality suggests the *information* may compress to a simple split rule, but that rule itself needs e and so is not FO(TC)-implementable.

### 5. Why this does not settle the front

- I did **not** produce an all-n family of poly-size optimal FO(TC) programs (that would be Conjecture C / a major completeness result).
- I did **not** prove `D(n)` is superpolynomial. The deck-class board result is only finite evidence through n=7 / height-two proxies.
- I did **not** prove an unconditional Omega(D(n)) lower bound, nor rule it out. I identified a model mismatch in the *mechanism* suggested by the front: literal deck-indexed branching is not FO(TC)-realizable because D_e is #P-hard to compute.
- I did **not** give an antichain reduction or any complexity-class placement for SORT-BOUND-U. A barrier to one certificate route is not NP/completeness/EXPTIME separation.

### 6. Sharpened falsifiable question (proposed)

Replace "deck-indexed move choices" by an **FO(TC)-distinguishable** invariant: let `I_k(P)` be the FO(TC)_k-type / bounded-rank invariant of the labelled poset structure P (or another poly-time computable invariant). Ask: for reachable optimal-play states, does any poly-time-computable invariant I with poly(n)-many values determine an optimal move, or is there an all-n family requiring superpolynomially many I-classes? This separates *information content* (D_e, #P-hard) from *interpreter-accessible information* (FO(TC)/poly-time), which is the actual completeness bottleneck per note §§2,4,6.

## Concrete failed / limited approaches

1. **Direct D_e-indexed lower bound**: fails as stated because D_e is not readable by a poly-time/FO(TC) interpreter (Brightwell-Winkler #P-completeness). Not a refutation of all lower bounds, only of this mechanism.
2. **Max-min-e split as compression witness**: optimal on R(5),R(6) by probe, but uses e(P) — #P-hard, so not an FO(TC) program rule. Cannot be promoted to the front's falsifier.
3. **All-posets balance probe**: attempted exhaustive/random test; script had bugs then was killed by timeout/resource limits. No result obtained; not needed for the reported obstruction.
4. **Web search**: unavailable/cancelled in this environment; relied on local note, local literature.md, and Wikipedia summary for Brightwell-Winkler identification.

## Honest limits

- **No new theorem/counterexample establishing the front either way.** The reported obstruction is a model-mismatch/expressiveness observation grounded in standard complexity facts; it does not close the FO(TC) completeness conjecture.
- **#P-completeness is a complexity assumption boundary**: "FO(TC)/poly-time cannot compute e" is conditional on standard separations (NL != P#P, FP != #P); I did not prove an unconditional separation.
- **Small-n data n<=6 only** for the new probes; board already had up to n<=7/9 in related fronts. No extrapolation.
- **No repo/Lean/board changes made.** Per AGENTS, nothing here crosses the publication gate as a substantive new theorem/counterexample; it is a precise obstruction to report back to the frontier/board.

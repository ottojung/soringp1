# antonina-KRoSN5CqZQmG8uHdcok4k9-forts

Session: ses_e065bb7b9ffet3977ypEiCaw2a
Workspace: /home/lubko/soring-fronts/exec-fixed-alternation-blocks-20261120
Created: 1795189655723; updated: 1795191123007

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1f9abb75f001pfcx5T0tw20xpz)

I'll start by inspecting the current state carefully, given the warning about potential prior side effects from an interrupted turn. Let me gather information in parallel.

## Output 28 (msg_1f9abca90001FxQ6qAYSw4Tgl3)

No uncommitted changes. Let me inspect the durable records and key documents in parallel.

## Output 55 (msg_1f9abf0ae001RKZsMZ2oiP2MYE)

This is a worktree of `/home/lubko/soring301`. Let me read the operational docs and key research documents, plus check the board digest (read-only) to see whether the interrupted turn already posted anything.

## Output 74 (msg_1f9ac0a9b001mWJBf6BKrFatSp)

Let me check the board digest (read-only), the durable ledger, and search for the related prior work items the user flagged.

## Output 93 (msg_1f9ac1ba1001wDkplcaZB5rLgm)

Let me examine the ledger entry specific to this front and check the board for any prior post on fixed-block alternation (read-only), plus check the host.

## Output 108 (msg_1f9ac759d001v3KBw88PXgFter)

Let me locate the ledger entry for this specific worktree and check the board with other relevant keywords/pages.

## Output 123 (msg_1f9accec9001B9QlEAuDP5zO3T)

Found the ledger entry for this front. Let me read it fully to determine status and whether the prior turn posted anything.

## Output 134 (msg_1f9acf6b9001v34WPus2rDDYWo)

The prior ledger front `fixed-block-alternation-obstruction` is `blocked`/`failed` with no clear result. Let me determine whether a newer front corresponds to this worktree and whether the interrupted turn posted to #301. Let me check time, recent board activity, page 2, and the newest ledger entries.

## Output 176 (msg_1f9b76f980012lGP1teIWYKIXH)

## Recovery / side-effect check (no external actions taken)

- **Git:** branch `research/exec-fixed-alternation-blocks-20261120` at `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`, worktree clean (`git status --porcelain=v1` empty), no new commits.
- **Repo/Lean:** no files created or modified by this session; no `lake build`/formalization started.
- **Board #301:** inspected via `scripts/board_digest.py` (pages 1–2, recent; keyword filters including `alternation`, `fixed-block`, `blocks`, `constant`, `block lower`, `sorter/adversary`, `omega`). No post attributable to this fixed-block front was found (most recent page-1 post at 2026-11-20T15:05:48Z). No post was made in this session.
- **Durable ledger:** `~/.local/state/soringp1/frontier-ledger.json` contains the earlier `fixed-block-alternation-obstruction` entry (`blocked`/failed, no substantive result) but no entry/finding for this worktree/date-specific front. No ledger writes performed.
- **Conclusion:** no evidence of duplicated external side effects from the interrupted turn. The investigation below is the unfinished work only. No finding was posted to #301 because the outcome is a clarified obstruction/missing-lemma formulation (not a mature constant-block construction, not a rigorous all-`n` computational lower bound, and not a theorem that clearly changes the research picture beyond prior alternation fronts); if you want, I can post this summary as a concise board update.

## Scope and sources consulted

- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-certificates-barriers.md` (model `G(n,k)`, Claim A: `SORT-BOUND-U ∈ PSPACE`, Claim B sparsity, Claim C witness size), `docs/literature.md`, and related `docs/research-*` notes (grep for alternation/blocks).
- Frontier ledger excerpts (prior fronts: `ph-hierarchy-alternation-depth`, `adversary-alternation-logn-blocks`, `adversary-game-alternation-bound`, `alternation-depth-quantifier-blocks`, blocked `fixed-block-alternation-obstruction`, `minimax-state-count-polynomial`).
- Board #301 recent context (digest only). Primary complexity anchors already recorded in-repo: Chandra–Kozen–Stockmeyer (*Alternation*, JACM 1981, `APTIME=PSPACE`), Mahaney (1982, sparsity), plus the sorting/comparison-model basics in `problem.md`/`literature.md`. I did not retrieve new external sources beyond what is in the repo and standard results stated cautiously below.

## 1) Model distinctions (requested)

### Numeric budget `k = T(n)` (not alternation)
- `S(n)` is the minimax comparison height. A play/strategy has height `≤ k` if it uses at most `k` comparisons on every adversarial outcome. For informative unary threshold instances `(1^n # 1^k)`, `k` lies in `Θ(n log n)` and the input length is `N = n+k+1 = Θ(n log n)` (`problem.md`, `research-certificates-barriers.md` §0). Thus `k` is a move/horizon/resource count, not a number of quantifier or player-alternation blocks.

### Actual comparison game `G(n,k)` (game/execution alternation)
- `G(n,k)` (`research-certificates-barriers.md` §0, Claim A): state = transitive closure of a partial order on `n` labelled keys; start at the antichain. Each round: **sorter** picks an incomparable pair (an adaptive choice), **adversary** answers `<`/`>` (a worst-case outcome). Sorter wins iff a total order is reached within `k` comparisons. `S(n) ≤ k ⇔` sorter wins `G(n,k)`.
- **Interleaved play:** one sorter move then one adversary move per comparison ⇒ `k` rounds = `2k = Θ(S(n)) = Θ(N)` move-alternations in the extensive form. This is the natural alternation of the *actual game execution*.
- **Batched/oblivious blocks (a different game-level notion):** if the sorter commits to a batch of comparisons before seeing any outcomes in that batch (a non-adaptive phase), then `r` batches give `2r` sorter/adversary alternation blocks. This restricts adaptivity (comparisons inside a batch cannot depend on each other’s outcomes). `r=1` with a fully precommitted comparison set is oblivious/non-adaptive play.
- **Strategy normal form (logical alternation of the game):** `S(n) ≤ k ⇔ ∃σ ∀π : Win(σ,π,n,k)` where `σ` is a sorter strategy (a function from histories/reachable states to legal comparisons) and `π` ranges over adversary answer sequences/paths. This is **2 logical quantifier blocks** (constant) regardless of `k`, but `σ,π` are exponentially structured objects in general.

### Alternation of a proof/ATM (computational/deciding `SORT-BOUND-U`)
- A uniform algorithm deciding `SORT-BOUND-U` with `d` alternation blocks in the complexity-theoretic sense is a poly(`N`)-time ATM with `d` quantifier blocks, i.e. membership in `Σ_d^P ∪ Π_d^P` (constant `d` ⇒ PH). This is alternation of the *verification/decision procedure*, not of played comparisons.
- Claim A gives an interleaved simulation: existentially guess a pair, universally branch on the outcome, repeat `k` times, accept if total ⇒ `ATIME(poly(N))` with `Θ(k)=Θ(N)` alternations, hence `SORT-BOUND-U ∈ APTIME = PSPACE`. 
- **Crucial non-identity:** computational alternation blocks ≠ logical strategy blocks ≠ game move-alternations ≠ `k`. The normal form has 2 logical blocks but does not by itself yield a poly-time 2-alternation ATM unless the witness `σ` (and its verification) is polynomially bounded.

## 2) “Fixed-block” question — analysis

### (a) Constant ATM/proof blocks for deciding `SORT-BOUND-U`? (PH membership)
- **Construction route (constant blocks):** the direct Σ₂-style certificate is `∃σ (poly(N) description) ∀π Verify(σ,π,n,k)`. This would place yes-instances (and, with an appropriate form, the language) into a fixed PH level **iff** there is, for all relevant `(n,k)` with `S(n) ≤ k`, a complete, sound, polynomial-size and polynomial-time-evaluable winning strategy/certificate. 
  - Explicit comparison trees have `≥ 2·n!−1` nodes / `n!` leaves in reduced form (Claim C), i.e. `2^{Θ(N)}` on informative unary inputs — not polynomial.
  - Sound succinct forms (e.g. framed DAG/certificate systems studied in `research-framed-certificate-frontier.md` and ledger fronts) have **unknown completeness** and **unknown polynomial size** for exact/all-`n` optimal play; known soundness does not imply a complete PH certificate.
  - Near-optimal uniform sorting strategies with poly-time descriptions exist as *algorithms* (e.g. merge insertion; Sergeev’s group-insertion gives `log₂(n!)+o(n)` height per `literature.md`/repo notes), certifying upper bounds `S(n) ≤ h(n)` for those `h(n)`. But they do **not** decide `SORT-BOUND-U` inside the remaining uncertainty/gap window where `k < h(n)` yet possibly `k ≥ S(n)`, so they do not yield a constant-block exact decider.
- **Lower-bound route (ω(1) or Ω(log n) computational blocks forced):** proving that no poly(`N`)-time ATM with constant (or sub-logarithmic, as applicable) alternations decides `SORT-BOUND-U` would mean `SORT-BOUND-U ∉ PH` (or below the claimed bound). Since `SORT-BOUND-U ∈ PSPACE` (Claim A), this would imply `PH ≠ PSPACE` (a major open separation). 
  - The general ATM alternation/time hierarchy cannot be transferred to `SORT-BOUND-U` without a reduction/hardness argument: it separates classes in general, not this specific fixed sparse language. 
  - Sparsity (`SORT-BOUND-U` is a tally/threshold language with `O(m^2)` instances of length `≤ m`, Claim B) rules out many-one NP-hardness unless `P=NP` (Mahaney) and is a structural barrier, but it gives no unconditional proof of `∉ PH` and no reduction-free alternation lower bound. (Separately, tally `⊆ P/poly`, so PSPACE-hardness under poly-time Turing reductions would collapse PH — a conditional obstruction, not an established fact here.)
- **Status:** open. Neither a uniform constant-block decider nor a rigorous all-`n` computational ω(1)/Ω(log n) lower bound for deciding `SORT-BOUND-U` follows from current model/literature barriers; this is consistent with prior ledger fronts (`ph-hierarchy-alternation-depth`, `adversary-game-alternation-bound`, `alternation-depth-quantifier-blocks`).

### (b) Constant sorter/adversary blocks for achieving (near-)optimal height?
This depends on the block model:

- **Oblivious precommitment (1 sorter block, no outcome feedback inside):** a fixed comparison network/scheme of size `k` is a constant-block strategy. Uniform oblivious sorting networks of size `O(n log n)` exist (AKS and successors, standard in the comparison-network literature), so **constant blocks suffice to achieve height `O(n log n)`** (asymptotically within a constant factor of `S(n) = Θ(n log n)`). However, this does **not** achieve exact `S(n)` in general (adaptive sorting can be strictly better; e.g. known small cases where optimal adaptive trees beat network size) and is not known to achieve the additive `o(n)`-near-optimal gap `S(n)+o(n)`; with budget `k = n(n-1)/2` a single block trivially sorts by testing all pairs, but that is far from near-optimal height.
- **Adaptive batched rounds (r blocks, feedback only between batches):** to achieve total comparison count near `S(n)` (i.e. `O(n log n)` with the optimal/near-optimal leading behavior), the algorithm must retain strong adaptivity. In the parallel-comparison/rounds model (a standard, distinct line from ATM alternation), it is a well-established qualitative result that a constant number of comparison rounds cannot achieve `O(n log n)` total comparisons for sorting; fixed-round sorting incurs a superlinear comparison cost and `ω(1)` rounds are required for near-linearithmic total comparisons (see the parallel/round sorting literature, e.g. Valiant 1975 on parallelism in comparison problems; Bollobás–Thomason 1983 and subsequent work on sorting/selection in rounds — **[literature pointer, not re-derived here]**). Interpreted this way, constant game-level blocks do **not** suffice for `o(n)`- or exact-near-`S(n)` adaptive height, and an `ω(1)` (typically Ω(log n / log log n)-scale in standard tradeoffs) block requirement is forced for near-optimal total comparisons. This is a statement about *adaptive-round decomposition of sorting strategies*, not about ATM alternations for deciding `SORT-BOUND-U`.
- **Interleaved optimal/adaptive play:** achieving exact height `S(n)` by the natural minimax strategy is an interleaved `Θ(S(n))`-move game execution unless compressed into batches; no constant-batch exact-optimal decomposition is known.

## 3) Why the general ATM hierarchy does not transfer

- `APTIME = PSPACE` and bounded-alternation classes characterize general computations; they do not, without a reduction, lower-bound the alternation needed for the single fixed language `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`.
- `SORT-BOUND-U` is sparse/tally-like and in `P/poly`, so: (i) Mahaney blocks the standard many-one NP-hardness route, (ii) it is not a candidate for many-one EXPTIME-hardness, and (iii) no known reduction places it complete for a level forcing `ω(1)` alternations. Therefore “the natural simulation uses polynomial alternations” is an upper-bound/representation fact, not a proof that polynomially many (or Ω(log n)) blocks are necessary for *every* uniform decider.

## 4) Concrete missing lemma (the fixed-block bottleneck)

**Lemma L (succinct complete strategy/certificate, exact threshold).** There exist a fixed `d` and a uniform family `{C_{n,k}}` such that for all informative `(n,k)` with `N=n+k+1`: if `S(n) ≤ k` then `C_{n,k}` is a winning strategy/certificate for `G(n,k)` of size `poly(N)` verifiable by a `poly(N)`-time predicate with `d` alternation blocks (sound and complete over all `n`), and if `S(n) > k` no such accepting object exists (or dually for co-certificates).

- **Equivalence/force:** L (in Σ₂/PH form) ⇒ `SORT-BOUND-U ∈ PH` (constant ATM blocks). A refutation of L for all fixed `d`/poly encodings would be a strong non-succinctness theorem (beyond current evidence: exponential explicit witnesses, sound-but-incomplete compressed forms, winning-frontier/state explosion) but is not presently a theorem.
- **Weaker gap-closing variant:** a uniform poly-size, poly-time-evaluable strategy achieving height `≤ S(n)+o(n)` for all `n` would give a constant-logical-block *upper-bound* certificate for the easy side of the threshold but still not decide the exact `o(n)` gap without exact `S(n)`.
- **What is missing:** an all-`n` completeness theorem for some succinct representation (state quotient/DAG/program/invariant) at exact height `S(n)`, or an all-`n` incompressibility theorem ruling every such representation out under the encoding/cost model.

## 5) Falsifiable next test (concrete)

**Test T1 (extend the canonical-optimal succinctness probe, exact `S(n)` where known).** 
- **Objects:** for `n ∈ {7,8,9,10,11,12}` (use established exact values `S(7)=13, S(8)=16, S(9)=19, S(10)=22, S(11)=26, S(12)=30`; `literature.md`), compute in the isomorphism-quotient minimax state graph a *canonical optimal policy* `π_n`: from each reachable quotient state `P` with `F(P)=r` choose the lexicographically first comparison (under a fixed canonical labeling) among those with `1 + max(F(child_L),F(child_R)) = r` (a well-defined optimal strategy, as used in prior ledger experiments).
- **Measurements (falsifiable):** (M1) number `q_π(n)` of distinct quotient states visited by `π_n` from the antichain; (M2) size `D_π(n)` of the minimal shared DAG/straight-line description of `π_n` (node = state+action, edges to child states, identical subpolicies shared); (M3) description length in bits under a fixed explicit encoding (state id or canonical poset encoding + action). Prior reported points to extend/replicate under one pipeline: `q_π = 11,14,34,36,123` for `n=5..9` (ledger `minimax-state-count-polynomial`) with union-of-all-optimal states far larger.
- **Hypotheses:** H⁺ (supports L): `q_π(n), D_π(n)` fit `poly(n)` (e.g. `≤ c·n^4`) on `n≤12` with a stable encoding. H⁻ (evidence against L for this family/encoding): superpolynomial/exponential growth consistent with `2^{Ω(n)}` or with the union curve, persisting at `n=10..12`. 
- **Why discriminating but not decisive:** polynomial small-`n` scaling is necessary-but-not-sufficient evidence (no all-`n` theorem); superpolynomial scaling for this canonical family falsifies “this natural family yields a succinct certificate” but not L absolutely (another strategy/encoding might compress). Results must be labeled `[experiment]` and, per `AGENTS.md`, reported as evidence/obstacle, not as a proof of PH membership or separation.

**Test T2 (disambiguate game-blocks vs ATM-blocks, if pursued):** for a fixed budget `k(n)=⌈log₂(n!)⌉ + g(n)` in the Sergeev/o(n) regime, determine (by search or lower-bound argument) the minimum number `r(n)` of adaptive batches (sorter commits a set, adversary answers set) needed by any strategy of total height `≤ k(n)`. A proof that `r(n)=ω(1)` would be an all-`n` *game-execution/block-adaptivity* lower bound for near-optimal height (distinct from deciding `SORT-BOUND-U`); a constant-`r` construction with exact costs would answer the height part under that model.

## 6) Bottom line (target)

- **No uniform constant-block construction found** for deciding `SORT-BOUND-U` (would require a succinct complete all-`n` certificate/strategy ⇒ fixed PH level) and none found that achieves exact `S(n)`; constant (oblivious) blocks do achieve `O(n log n)` height via fixed networks but not exact/known-`o(n)`-optimal height.
- **No rigorous all-`n` computational ω(1)/Ω(log n) alternation lower bound** for deciding `SORT-BOUND-U` (would imply a major separation and cannot be transferred from the general ATM hierarchy without a reduction). A genuine `ω(1)` lower bound does arise in the *different* batched adaptive-round sense for near-optimal comparison count (parallel-sorting tradeoffs, [literature pointer]), but this must not be conflated with ATM/proof alternation or with the numeric budget `k`.
- **Genuinely new beyond prior duplicated fronts here:** an explicit three-way disentangling (budget `k` vs game move/batch blocks vs ATM/proof blocks), the normal-form constant-logical-alternation vs exponential-witness point, and a concrete missing lemma L plus falsifiable tests T1–T2 tied to known exact `S(n)`/existing quotient data. This identifies the precise obstacle rather than claiming a settled constant-block or Ω(log n) theorem.

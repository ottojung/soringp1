# Frontier exec-report: space complexity of uniform evaluation of `S(n)` / `SORT-BOUND-U` (unary)

**Front:** space complexity of uniform evaluation of `S(n)` / `SORT-BOUND-U` (unary)  
**Date:** 2026-11-17  
**Workspace:** `/home/lubko/soring-fronts/space-lower-bound-unary` (billy-dev)  
**Status:** precise blocker/barrier for a stated algorithm class; no new upper bound below `O(N log N)` and no unconditional space lower bound found. (No repo/Lean changes; no external post performed by this turn.)

## 0. Recovery / side-effect check (Antonina backend-failure note)

- **Inspected:** `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-budgeted-dfs.md`, `docs/literature.md`, `docs/operations.md`, relevant scripts/docs (`scripts/transcript_dfs.py`, `scripts/budgeted_dfs.py`, space mentions), `git status`, recent `git log`.
- **Observed durable local state:** working tree clean; no `exec-report.md` existed before this turn; no commits authored by this turn.
- **External effects (board #301 post, purchases, etc.):** **uncertain / not verifiable from local workspace**. This turn does **not** post to #301 to avoid duplication; if a prior interrupted turn already posted "SoringP1 frontier: space-complexity-unary-evaluation", that should be treated as the authoritative external record and reviewed rather than repeated.

## 1. Sharp falsifiable question

> Can the known `O(N log N)` work-tape space bound (with `N = n + k + 1`, the unary input length of `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`) be reduced to `O(N)` or to `polylog(N)` by an explicit uniform algorithm for exact evaluation, **or** can one prove a nontrivial space lower bound / barrier ruling out a stated class of methods?

**Consequence for evaluating `S(n)` (all-n, encoding-precise):**
- **[deduction]** An explicit uniform algorithm deciding `SORT-BOUND-U` in work space `O(N)` (or `polylog(N)`) would be a genuine improvement of the current best recorded uniform space upper bound for the unary threshold language and would tighten the resource profile of exact evaluation of `S(n)` at unary scale (`N = n+k+1`, read-only input / work-tape accounting as in `docs/research-budgeted-dfs.md` §5.3). It would **not** by itself imply `P`, `NP`, or any separation: `SORT-BOUND-U ∈ PSPACE` is already established and unconditional super-polynomial lower bounds for this tally language are out of scope / equivalent to open separations (`problem.md`, "Realistic outcomes").
- **[deduction]** A proved general space lower bound above the trivial read-only-input baseline would be a major structural result about exact evaluation of the fixed minimax value `S(n)`; however, no technique for such unconditional uniform lower bounds is available here (and strong forms would run into the same separation-level obstacles as time lower bounds in this setting). A barrier for a **stated method class** is instead a precise negative result delimiting which algorithmic templates can/cannot achieve `O(N)` or `polylog(N)`.

## 2. Baseline (evidence: literature/internal docs)

- **[definition/literature/internal]** Model and encodings: `docs/problem.md`. `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`, `N=n+k+1`.
- **[deduction, internal]** Budgeted transcript-only DFS decides `SORT-BOUND-U` in deterministic time `2^{O(N log(N+2))}` and work space `O(N log(N+2))` bits (read-only input, standard work-tape model): `docs/research-budgeted-dfs.md` §5.2–5.3. For the numeric function `S_unary(1^n)` (input length `n`) the same method gives `2^{O(n log^2 n)}` time and `O(n log^2 n)` work space.
- **[deduction, internal]** Space decomposition at threshold depth `d=k` (`docs/research-budgeted-dfs.md` §5.2, specialized): stored comparison transcript/path = `O(d log n)=O(k log n)` bits; one on-demand reachability workspace (visited `n` bits + queue/stack of labels `O(n log n)` bits) = `O(n log n)` bits; peak = stack plus **one** reachability workspace = `O((k+n) log(n+2)) = O(N log N)` bits. Comparisons are appended only between currently incomparable pairs, so transcript induces a strict partial order and backtracking is by pop (`scripts/transcript_dfs.py` matches this accounting experimentally for small cases per doc).
- **[literature]** Directed reachability is in `NL` and in deterministic `O(log^2 m)` space for an `m`-vertex graph by Savitch's theorem (standard). This is relevant to the reachability workspace but not directly to storing the DFS transcript; using Savitch-style recomputation trades time for space in the reachability subroutine.
- **[deduction, internal]** `SORT-BOUND-U ∈ PSPACE` / game characterization already known (`problem.md`, `research-certificates-barriers.md`, `research-plan.md`); tally/sparse barriers constrain hardness claims but not directly these space-upper-bound questions (`problem.md`, Mahaney barrier).

## 3. Analysis: where the `log N` factor comes from

Let `N=n+k+1` and consider the nontrivial regime where the bound is tight up to constants in the accounting: `n>=2`, `k = Θ(n log n)` (the information-theoretic/worst-case budget scale relevant to `S(n)`), hence `N = Θ(n log n)` and `log n = Θ(log N)`.

- **Transcript/path term:** the DFS records the current adaptive path of `k` comparisons. A single comparison names an unordered pair `{i,j} ⊆ [n]` (or an oriented outcome consistent with the path), requiring `Θ(log (n choose 2)) = Θ(log n)` bits to specify in the worst case over arbitrary adaptive choices. Therefore the path encoding used by the method is `Θ(k log n) = Θ(N log N)` bits in this regime. **[deduction]**
- **Reachability term:** deciding comparability from the stored transcript by a standard visited-array BFS/DFS uses `Θ(n log n)` bits in the label-queue form stated in §5.2 (or `Θ(n)` bits for visited plus up to `Θ(n log n)` for a queue of vertex names, depending on representation), which is `O(N log N)` when `k >= n` but can dominate only in other regimes; in the `k=Θ(n log n)` regime it is lower-order or comparable only by representation. Savitch-style evaluation of reachability on the transcript-induced graph could in principle reduce the *reachability* workspace toward polylogarithmic in `n` at a large time cost, but it does **not** remove the need to access/retain the transcript that defines the current game state unless the transcript itself is recomputed/encoded differently. **[deduction/literature]**
- **Conclusion of decomposition:** the dominant `log N` factor in the recorded `O(N log N)` bound is attributable to **naming elements/pairs with `Θ(log n)` bits per comparison along an explicit stored path of length `Θ(k)`**. **[deduction]**

## 4. Constructive algorithm sketch (attempt) and outcome

- **Attempt A (subroutine squeeze):** keep the transcript-path DFS but replace BFS reachability workspace by a low-space reachability procedure (e.g. Savitch-style) to shrink the `n log n` reachability workspace component. **[deduction]** This can at best affect the additive reachability term; the `Θ(k log n)` transcript term remains, so total work space stays `Ω(k log n)` and does not reach `O(N)` or `polylog(N)` in the critical `k=Θ(n log n)` regime. Time would worsen substantially (recomputation), which is orthogonal to the asked space goal but reinforces impracticality.
- **Attempt B (path recomputation / implicit path):** avoid storing the explicit transcript by recomputing the current root-to-node path from an iterator/counter over the DFS/game tree. **[deduction]** Standard depth-first tree evaluation needs either the current path or an equivalent reversible/recursive state; recomputing a node's history in this adaptive adversarial game requires re-evaluating earlier branches/games or storing additional summary information. No explicit uniform scheme was found that maintains correctness of the exact minimax predicate `S(n) <= k` while guaranteeing `O(N)` or `polylog(N)` work space; naive recomputation introduces prohibitive time/space tradeoffs and does not obviously yield a net space improvement below the transcript encoding. This is an **unresolved constructive attempt**, not a proof of impossibility.
- **Attempt C (alternative succinct state):** store the current partial order by a compressed representation instead of the transcript. **[deduction]** The current state after arbitrary comparisons can encode substantial order-theoretic information (posets on `n` elements are numerous, cf. winning-frontier/state-space discussions elsewhere in docs); a representation asymptotically better than `Θ(k log n)` bits *uniformly for all reachable paths in the worst case* is not exhibited. Known compressions (e.g. symmetry/DAG ideas studied for other fronts) have not yielded a general all-path `O(N)` work-space evaluation scheme for the exact threshold DFS.

**Outcome:** no explicit uniform algorithm achieving `O(N)` or `polylog(N)` work space was obtained. **[open/conjecture-not-claimed]** (absence of construction, not a proof).

## 5. Barrier (stated class) and falsification attempt

### 5.1 Barrier for transcript/path-storing DFS evaluators (concrete)

**Class `C_trans` (stated):** uniform deterministic depth-first evaluators of the minimax game `G(n,k)` / `CanSort` that (i) explore sorter choices and both adversary answers by backtracking along a root-to-node path, (ii) keep an explicit representation of that path's comparison transcript (or an information-equivalent per-step record of each chosen pair/outcome) in work memory at the current node, and (iii) may use additional workspace for local predicates such as reachability/comparability computed from the current state (the template of `docs/research-budgeted-dfs.md` §5.2 / `scripts/transcript_dfs.py`).

**Claim (barrier, method-level). [deduction]** Any algorithm in `C_trans` requires `Ω(d log n)` work-tape bits in the worst case over adaptive transcripts of length `d` (for `n>=4`, `d>=1`), because each recorded step must distinguish among `Θ(n^2)` possible pairs and the path has `d` steps with no generic lossless encoding below `Θ(log n)` bits per step under arbitrary adaptive selection. For the unary threshold decision in the regime `d=k`, `N=n+k+1`, and `k=Θ(n log n)=Θ(N)`, this is `Ω(N log N)` bits; hence **`C_trans` cannot achieve `O(N)` or `polylog(N)` work space**.

**Scope/limits:** this rules out the stated transcript-storing/backtracking template (and close variants that retain an explicit per-comparison history), **not** all possible uniform algorithms for `SORT-BOUND-U`. It does not lower-bound algorithms that might represent/evaluate the game without storing the path explicitly. **[deduction]**

### 5.2 Why a general unconditional lower bound is not claimed

- **[deduction/literature-context]** `SORT-BOUND-U` is a tally/sparse language in `PSPACE` (`problem.md`), so circuit/nonuniform methods are moot and unconditional uniform super-polynomial separations are out of scope; proving even modest but general space lower bounds for explicit PSPACE problems is beyond currently available techniques in general. Accordingly this report gives **no** claim of the form "`SORT-BOUND-U ∉ DSPACE(o(N log N))`" in general.
- **[deduction]** Known space theorems used here (e.g. Savitch reachability, standard DFS accounting) provide **upper bounds / translations**, not lower bounds for this specific language.

### 5.3 Falsification attempts performed (paper-level)

- **[deduction]** Tried to falsify the barrier by finding a lossless per-comparison encoding below `Θ(log n)` bits uniformly over all adaptive paths: fails information-theoretically for arbitrary pair choices among `Θ(n^2)` candidates unless restricted structure is proved (none available for all-n exact evaluation).
- **[deduction]** Tried to falsify "no improvement possible" constructively via Attempt A/B/C above: found no `O(N)`/`polylog(N)` scheme, but attempts do not constitute a proof; status remains **open** beyond class `C_trans`.
- **[experiment]** None run beyond reading existing small-n accounting/scripts; existing docs already record depth/path behavior (`budgeted_dfs.py`, `transcript_dfs.py`, §5.2). No new discriminating experiment identified that would settle the asymptotic space question.

## 6. Precise result delivered

- **Nontrivial/precise blocker (class-specific):** the explicit transcript/path-storing DFS template `C_trans` has an inherent `Ω(k log n)` (`= Ω(N log N)` in the critical unary regime) work-space requirement from path storage, so it cannot be optimized to `O(N)` or `polylog(N)`; the known `O(N log N)` bound for that template is therefore tight **up to the reachability/additive terms within that method family** and any asymptotic improvement requires leaving `C_trans` (a different state representation/evaluation strategy). **[deduction]**
- **No algorithmic improvement found:** no explicit uniform `O(N)` or `polylog(N)` algorithm for `SORT-BOUND-U` / exact `S(n)` evaluation identified. **[open]**
- **No general lower bound/barrier beyond stated class:** none proved. **[open]**

## 7. Consequence for evaluating `S(n)` (summary)

For exact uniform evaluation of `S(n)` via the unary threshold language, the current space frontier is `O(N log N)` work tape; within the natural transcript-backtracking DFS family this is explained by an unavoidable `Θ(log n)`-per-comparison path cost (barrier for `C_trans`). Progress to `O(N)` or `polylog(N)`, if possible at all, must come from a genuinely different exact evaluation method (non-path-storing or radically compressed state) and would refine the known PSPACE-era upper-bound picture without, by itself, yielding a complexity-class separation. **[deduction]**

## 8. Evidence labels used

- **definition:** problem/model/encoding statements from `docs/problem.md`.
- **literature:** Savitch reachability (standard); Mahaney/sparsity context as cited in project docs.
- **deduction:** space accounting, regime analysis `k=Θ(n log n) => Θ(N log N)`, class-`C_trans` barrier, attempt evaluations.
- **internal (project records):** `docs/research-budgeted-dfs.md`, `docs/research-plan.md`, `docs/research-certificates-barriers.md`, `scripts/transcript_dfs.py`.
- **open:** existence of `O(N)`/`polylog(N)` algorithm outside `C_trans`; any general space lower bound.
- **experiment:** none new/discriminating in this turn.

## 9. Uncertainty / next decisive obstacle

- **Uncertainty:** whether a non-`C_trans` exact evaluator (e.g. path-free recomputation scheme, succinct canonical state with provably small work space, or other game-evaluation method) can beat `O(N log N)` for all `n,k`.
- **Decisive obstacle:** exhibit either (a) an explicit uniform algorithm with proved `O(N)` or `polylog(N)` work space and exactness for all `n,k`, or (b) a theorem showing every exact uniform evaluator for `SORT-BOUND-U` needs `ω(N)` / super-polylog work space under stated assumptions - (b) would likely require fundamentally new lower-bound techniques. Absent these, only method-class barriers (like `C_trans`) are currently within reach.
- **External reporting:** board post to #301 **not performed** here (duplication risk under recovery); this report records a precise blocker suitable for posting if not already posted.
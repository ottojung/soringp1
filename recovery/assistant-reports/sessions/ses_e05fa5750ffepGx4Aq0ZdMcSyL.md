# antonina-sWotrD3ktouDzeZYgelXmk-mason

Session: ses_e05fa5750ffepGx4Aq0ZdMcSyL
Workspace: /home/lubko/soring-fronts/verify-bdd-residual-claim-20261120
Created: 1795196037465; updated: 1795196771367

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fa05acbb001Yqt43akJUSFalE)

I’ll check the repository’s model and prior BDD notes, then reconstruct the fixed-order residual argument from the stated illegal-assignment convention. I’ll make no repository or board changes.

## Output 69 (msg_1fa05f966001AGwN9AoRBOwC4i)

## Audit result

**The all-cut residual lemma is correct as a general OBDD identity, but “legal prefixes” must be defined precisely.** It does not, by itself, establish a \(2^{O(n\log n)}\)-time construction of the \(W_d\) OBDD. The construction-cost objection is valid; neither issue is a lower bound.

### Definitions and residual lemma

For each \(i<j\), encode the relation by consecutive bits \((x_{ij},y_{ij})\):

- \(10\): \(i<j\)
- \(01\): \(j<i\)
- \(00\): incomparable
- \(11\): illegal

Fix the pair-lex variable order, with a specified order within each pair. Define \(W_d\) on **all** bitstrings: it is false on illegal encodings and on encodings that do not describe a poset; on posets it is the depth-\(d\) winning predicate from the minimax recurrence.

At a cut after \(t\) variables, let a prefix \(p\in\{0,1\}^t\) induce the residual function
\[
W_{d,p}(z)=W_d(pz)
\]
on **all** suffix assignments \(z\in\{0,1\}^{m-t}\), where \(m=2\binom n2\).

For a fixed variable order, the minimum width at that cut of an exact OBDD for \(W_d\) is exactly the number of distinct such residual functions among prefixes. Each node at the cut computes one residual; prefixes reaching the same node have the same residual. Conversely, prefixes with different residuals cannot share a node, and equal residuals can be merged. This applies at every cut, including cuts between the two bits of a pair.

### Illegal-assignment convention and well-posedness

The lemma is well-posed under the stated convention **if prefixes range over all bitstrings**, and residuals are evaluated on all suffix bitstrings with illegal/non-poset completions assigned false.

If “legal prefix” means “a prefix that can be extended to some legal poset,” then the stated equality needs qualification: it omits non-extendable prefixes, whose residual is the constant-zero function. It also risks changing the residual if suffixes are tested only for legal completions instead of being evaluated under the total Boolean convention. To state an all-cut theorem cleanly, count residuals over **all prefixes**; equivalently, count extendable prefixes’ residuals and include the zero residual if any dead prefix exists. Prefixes of a legal encoding are themselves extendable, but arbitrary OBDD prefixes need not be.

### What the lemma does—and does not—show

A width bound for the **final function** gives an OBDD-size bound of at most the number of variables times the maximum width (up to terminal conventions). It does not give an algorithm to construct that OBDD within the same time bound.

In particular, a recurrence-based construction of \(W_d\) must also bound the costs and intermediate sizes of operations such as legality checking, closure or pullback, Boolean apply, and depth iteration. A bound on the final residual counts alone supplies none of those bounds. This is the precise gap in inferring \(2^{O(n\log n)}\) construction time from width alone.

### Existing-document overlap

The repository’s `docs/upper-bound.md` gives the explicit partial-order minimax recurrence and a \(2^{O(n^2)}\) state-enumeration upper bound, while `docs/research-budgeted-dfs.md` records the budgeted DFS upper bound. The closest prior structural notes concern recurrence/state representations and closure costs; I found no existing fixed pair-lex OBDD residual lemma in `docs/`. The board’s earlier symbolic-poset-DD discussion, as reflected in the #301 entry, left the encoding/order unspecified, so it does not settle this fixed-order formulation.

**Conclusion:** The all-cut lemma is true with the full-assignment residual definition above. “Legal prefixes” alone is ambiguous and may omit the zero residual. Even the corrected lemma is a characterization of width, not a construction-time theorem. The missing construction analysis is an obstruction to that claimed inference, **not** evidence of large OBDD width or a runtime lower bound.

## Output 81 (msg_1fa0e30e9001VgrevqK5h1EOdu)

Understood. I’ll re-baseline onto `origin/main` and redo the audit against current authority, including a fresh board read. No code or board writes.

## Output 96 (msg_1fa0e41b9001pgR5so2O0RI1D2)

Current AGENTS.md is identical to the stale copy. Let me check whether the relevant docs changed on `origin/main` and pull a fresh board snapshot.

## Output 115 (msg_1fa0e52660010cVlAYXkZdryBl)

`origin/main` adds several new docs (notably strategy-program/threshold work). I’ll check those for overlap and read the full current #301 thread, not just the truncated digest.

## Output 155 (msg_1fa0e920e001qJqvM6y9GK97Ie)

No later #301 comment supersedes the 15:05Z OBDD post. I’ll read its full text and the two nearest related posts to pin down the exact claim and prior-work overlap.

## Output 220 (msg_1fa100ca60010HohiLma1rmE6c)

## Baseline and status

- **Current main:** `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f` (verified via `git -C /home/lubko/soring301 rev-parse origin/main`).
- **Stale-baseline effect:** the old worktree sits at `6a96398`. `AGENTS.md` is byte-identical on `origin/main`; the relevant docs (`problem.md`, `upper-bound.md`, `research-budgeted-dfs.md`, `research-winning-frontier-barrier.md`) are unchanged between `6a96398` and `origin/main`. The only doc additions on current main are `research-core-threshold.md`, `research-width-two-threshold.md`, `research-fo-tc-split-schema.md`, `research-fo-tc-strategy-programs.md`, `research-fotc-publication-record.md`, `research-fotc-strategy-programs.md`, plus README/plan lines. I checked them: the “width” there is **poset width** (width-two threshold), not OBDD width, and the FO/TC strategy-program work is a different representation. No overlap with the claim. The stale baseline therefore did not change the substantive inputs, but it did omit these new documents; I re-read current authority explicitly.
- **Still open / not superseded:** the only #301 message matching `OBDD`, `residual`, or `pair-lex` is the 15:05:48Z post by “OpenCode research (fixed-order poset BDD)” (`sha256:cEmAdJvbBI1LFwkMcHZ4oxuddDu8H2J8kMbL8PnHby8`), whose stated result is **C: precise obstruction; no width theorem proved**. Board page 1 runs to 17:22:16Z and contains no later comment addressing it; page 2 is older (≤09:33Z). `docs/research-plan.md` on current main still lists “Shrinking the exponent. Is `S(n)` computable in `2^{O(n log n)}` time …?” as open. The 14:52Z `symbolic-poset-dd-obstacle` post is a predecessor with unspecified encoding, refined — not superseded — by the 15:05Z fixed-order version.

## Exact claim under audit

The #301 post fixes pair-lex order on consecutive bits \((x_{ij},y_{ij})\): `10` = \(i<j\), `01` = \(j<i\), `00` = incomparable, `11` = illegal; \(W_d\) is false on illegal/non-poset strings and follows the stated minimax recurrence on posets. It asserts (i) for this order, a reduced OBDD’s width at a cut equals the number of distinct residual suffix functions induced by prefixes (illegal prefixes contributing false), and (ii) a width bound alone does not give \(2^{O(n\log n)}\) construction time because legality/closure/pullback/apply/depth costs must also be bounded.

## Independent verification of the residual-width identity

**Definition / deduction.** Let \(m=2\binom n2\). For a cut after \(t\) variables and prefix \(p\in\{0,1\}^t\), set \(f_p(z)=W_d(pz)\) for all \(z\in\{0,1\}^{m-t}\). For a **reduced** ordered BDD with this fixed order:

1. Every prefix \(p\) reaches exactly one node \(u\) in the level-\(t\) frontier; the subgraph at \(u\) computes \(f_p\).
2. If two prefixes reach the same \(u\), they have the same residual. If two distinct frontier nodes \(u\neq v\) had the same residual, reduction would have merged them. Hence the map \(u\mapsto f_u\) is a bijection between frontier nodes and distinct residuals, at **every** cut — including cuts between the two bits of a pair, and even with level-skipping (the frontier is taken after reading \(t\) variables).

So the identity is correct as a general reduced-OBDD fact, consistent with the standard framework cited on the board (Bryant, *IEEE TC C-35(8)*, 1986, DOI 10.1109/TC.1986.1676819). It is an existence/counting identity, not a theorem about this particular \(W_d\).

**Well-posedness caveat.** “Legal prefixes” must be defined carefully. If it means only prefixes **extendable to a legal poset** (no `11` block, no specified cycle, and no specified incomparability contradicted by closure), then counting only those prefixes can undercount by exactly the constant-false residual: every non-extendable prefix has \(f_p\equiv 0\) (illegality persists under any extension), but a constant-false residual need not be induced by any extendable prefix. Example: \(n=2\), \(d=1\), cut \(t=1\): \(x=0\) gives the constant-true residual and \(x=1\) gives \(\neg y\); no length-1 prefix is non-extendable, so no zero residual appears. The exact statement is therefore:

\[
\text{width}(t)=\bigl|\{f_p:p\in\{0,1\}^t\}\bigr|
=\bigl|\{f_p:p\ \text{extendable}\}\bigr| + \mathbf 1[\,0\notin\{f_p:p\ \text{extendable}\}\,].
\]

The #301 phrasing “illegal prefixes contribute false” is consistent with this if read as ranging over **all** prefixes; read as “extendable prefixes only” it is off by one in some cases. This is a precision fix, not a refutation.

## Sufficiency for construction time — the gap is real

A uniform residual bound \(2^{O(n\log n)}\) at every cut and depth would imply the **minimal** reduced OBDD for each \(W_d\) has size at most \(m\cdot 2^{O(n\log n)}=2^{O(n\log n)}\). It does not provide an algorithm of that cost:

- Building \(W_d\) from \(W_{d-1}\) requires forming, for each incomparable pair, the pullback \(P\mapsto \mathrm{TC}(P+\text{edge})\), then AND-ing the two sibling predicates, then OR-ing over \(O(n^2)\) pairs. Transitive closure can compare pairs far earlier in the variable order than the added edge, so this pullback is not a local variable substitution; its intermediate OBDD width need not be bounded by the final width of \(W_d\).
- `apply`/reduce costs scale with the product of operand sizes; a bound on the output width says nothing about intermediate operand widths. No theorem rules out intermediate widths \(2^{\Theta(n^2)}\) even when the final width is \(2^{O(n\log n)}\).
- The legality/transitivity recognizer under this encoding needs its own bounded DD construction.
- Depth \(O(n\log n)\) (or the crude \(O(n^2)\)) is only a polynomial factor if each step is \(2^{O(n\log n)}\); the decisive gap is per-step intermediate sizes and apply costs, not depth alone.

Thus the #301 insufficiency claim is correct: width bounds give compact **existence**, not bounded **construction**. Conversely, the known \(2^{(1/4-o(1))n(\log n)^2}\) nonisomorphic winning states at one depth is an enumeration barrier only; many assignments can share a residual, so it is **not** an OBDD-width lower bound and not a lower bound for computing \(S(n)\). The post’s own classification (“representation-specific obstacle only, not a lower bound for general algorithms”) is accurate, and consistent with `AGENTS.md`’s realistic-outcomes policy.

## Conclusion

The 15:05Z claim is current, open, and correctly classified. The residual-width identity is true under the all-prefix/false-convention reading, with the one-line extendability caveat above. The width-only insufficiency is a valid deduction: the missing closure/pullback/apply/legality bounds are a genuine construction obstruction. No lower bound, no class separation, and no theorem completion is established. No repository, board, or code changes were made.

## Output 249 (msg_1fa10a89c001Hxo6b83y4KY96G)

**Recovery check (no blind retry):**
- **Conversation:** I completed the requested audit in the previous turn (re-baselined to `origin/main`, read current policy/docs, inspected current #301 comments/pages, and reported the analysis). No follow-up action was left unfinished in that thread.
- **Working directory:** this worktree is clean (`git status --porcelain` empty). No audit notes, code, or other repo files were created/modified by me here.
- **Git state:** `/home/lubko/soring301` is also clean (`git status --porcelain` empty). `origin/main` is `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f` (unchanged). No commits were made.
- **Durable task records / external effects:** I did **not** post to Antonina #301, create issues/PRs, push, merge, run purchases, or modify any tracked or untracked project files. The only artifacts I produced are local, read-only inspection caches in `/tmp/opencode` (e.g. `board301p1.json`, `board301p1.err`, `obdd_related.txt`) used to analyze the board; Antonina accesses were read operations (`board show`/digest), not posts. No external side effect is uncertain.

**Conclusion:** nothing remains to do. I have not duplicated and will not duplicate any external action. If you need the audit restated or a specific remaining sub-question addressed, I can continue from this state.

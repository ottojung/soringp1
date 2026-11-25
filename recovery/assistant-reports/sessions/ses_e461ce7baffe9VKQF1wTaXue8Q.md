# antonina-90VdYaKaKhKAjWxfAIgXyP-pushed

Session: ses_e461ce7baffe9VKQF1wTaXue8Q
Workspace: /home/lubko/soring-fronts/pp-hardness-transfer-antichain
Created: 1794120030482; updated: 1794121084166

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 375 (msg_1b9f12145001cwQqM3vXvNbnNx)

## Scope and sources

Worked on `billy-dev` in `/home/lubko/soring-fronts/pp-hardness-transfer-antichain`. Read `AGENTS.md`, `docs/problem.md`, `docs/research-hardness-boundaries.md`, the #301 posts on `fibonacci-threshold-hardness`, `shallow-state-fibonacci-hardness` and the reachability correction, plus the primary literature leads (Brightwell–Winkler, Kravitz–Sah, Karp–Lipton, Yap, Mahaney, Peczarski/Stober–Weiß).

No repository or Lean changes. Worktree is clean. Posted one finding to Antonina #301.

## Claim attacked

The transfer claim:

\[
L_{\mathrm{fib}}=\{(P,b):e(P)\le T(b)\}\;\le_m^p\;\text{SORT-BOUND-U}.
\]

I tried to construct such a reduction, and then to prove that none can exist without a complexity collapse.

## Main finding: conditional non-transfer barrier

**Theorem [deduction].** Let \(A\in \mathrm{P/poly}\) (in particular, any sparse or \(\mathrm{P/log}\) language).

1. If \(A\) is PP-hard under uniform deterministic polynomial-time many-one or Turing reductions, then
   \[
   \mathrm{PP}\subseteq \mathrm{P/poly},
   \]
   hence \(\mathrm{NP}\subseteq \mathrm{P/poly}\) and \(\mathrm{PH}=\Sigma_2\) by Karp–Lipton.
2. If \(A\) is PP-hard only under Las Vegas many-one reductions, then
   \[
   \mathrm{PP}\subseteq \mathrm{coNP/poly},
   \]
   hence \(\mathrm{NP}\subseteq \mathrm{coNP/poly}\) and \(\mathrm{PH}\) collapses to the third level by Yap’s theorem.

**Proof sketch.** Compose the PP-hardness reduction with the polynomial-size advice/circuit family for \(A\). In the Las Vegas case, for a no-instance there is a zero-error halting run whose output \(y\) satisfies \(y\notin A\); the pair `(random string, transcript)` is a \(\mathrm{coNP/poly}\) witness, with advice containing circuits for \(A\) at all polynomially many query lengths.

**Corollary for `SORT-BOUND-U`.** `SORT-BOUND-U` is sparse (\(O(L^2)\) strings of length \(\le L\)) and even in \(\mathrm{P/log}\). Therefore any uniform polynomial-time reduction from \(L_{\mathrm{fib}}\) to `SORT-BOUND-U` would give
\[
\mathrm{PP}\subseteq \mathrm{coNP/poly}
\quad\Longrightarrow\quad
\mathrm{PH}=\Sigma_3
\]
(and a deterministic PP-hardness would strengthen this to \(\mathrm{PP}\subseteq\mathrm{P/poly}\), \(\mathrm{PH}=\Sigma_2\)). Under the standard assumption that PH does not collapse, **the PP-hardness of \(L_{\mathrm{fib}}\) does not transfer to `SORT-BOUND-U`**.

This is exactly the requested non-transfer branch, but it is **conditional**: an unconditional no-reduction theorem would require proving \(\mathrm{PP}\nsubseteq\mathrm{coNP/poly}\) (or \(\mathrm{PP}\nsubseteq\mathrm{P/poly}\)), which is open.

## Why “bypasses the sparse NP barrier” is backwards

The target is not merely sparse; it is nonuniformly easy. PP-hardness of a \(\mathrm{P/poly}\) language is itself a nonuniform-barrier statement: it forces PP into \(\mathrm{P/poly}\) or \(\mathrm{coNP/poly}\). The NP analogue is Mahaney; the PP analogue is Karp–Lipton/Yap. Sparsity is therefore also a barrier to PP-hardness, with a PH collapse rather than merely \(P=NP\).

## Structural obstruction

`SORT-BOUND-U ∩ Σ^L` is the single cutoff
\[
\{1^n\#1^{L-1-n}: n\le t_L\}.
\]
A reduction has only \(O(\log n)\) bits of effective output: the pair \((n,k)\). For dense \(n\times n\) poset inputs of length \(\Theta(n^2)\), there are \(2^{\Theta(n^2)}\) labelled posets but only \(\mathrm{poly}(n)\) target instances of length \(\le\mathrm{poly}(n^2)\). At the minimal natural output length \(n^2\):

| \(n\) | labelled posets | target instances |
|---|---:|---:|
| 4 | 219 | 136 |
| 5 | 4,231 | 325 |
| 6 | 130,023 | 666 |
| 7 | 6,129,859 | 1,225 |

For any fixed output polynomial the gap is exponential-vs-polynomial asymptotically. The reduction must collapse exponentially many posets into polynomially many monochromatic fibers.

The root carries no poset-structure hardness: \(e(A_n)=n!\) is explicit, so \(L_{\mathrm{fib}}\) at the antichain is a fixed univariate comparison of \(n!\) and \(T(b)\). The hardness lives on derived posets, which the univariate \(S(n)\) minimizes away.

## Reachable-state hardness does not compose to the root

For \(Q\) reachable in \(\mathrm{cov}(Q)\) comparisons,
\[
S(|Q|)\le \mathrm{cov}(Q)+S(Q)
\]
is an upper bound, not an equality. A transfer would need exact control of \(S(|Q|)\) or a forced equality. The information bound is not tight (\(S(12)=30>29\)), and no such exact lower bound is known.

The shallow-state PP-hardness is an \(\exists\)-statement about reachable states. `SORT-BOUND-U` is a minimax: \(\exists\) strategy \(\forall\) adversary. The quantifiers do not transfer.

## Soundness versus completeness

The Fibonacci predicate \(e(P)\le T(b)\) is a **sound sufficient** condition for sortability (given the threshold theorem) but not complete. Concretely,
\[
e(A_4)=24>T(5)=20,\qquad S(4)=5.
\]
So even a polynomial-time decider for \(L_{\mathrm{fib}}\) would not decide `SORT-BOUND-U`. A transfer must encode exact \(S\), not the Fibonacci certificate.

I also found a concrete separation showing that even exact \(S(P)\) does not determine the Fibonacci predicate. At \(n=4\), the posets with successor tuples `(0,0,0,7)` and `(0,0,0,3)` both have \(S(P)=3\), but their extension counts are \(6\) and \(8\). Since \(T(3)=7\), one satisfies \(e(P)\le T(3)\) and the other does not. Therefore no reduction that works by first computing \(S(Q)\) and then applying a fixed function can be correct.

## Failed approaches

1. **Ordinal-sum/bottom-chain reduction.** Take \(Q=P(+)M\) with \(e(Q)=c\,e(P)\) and output \((|Q|,\mathrm{cov}(Q)+K)\). The target tests \(S(|Q|)\), not \(S(Q)\); only the one-sided inequality is available.
2. **Padding to a fixed query length.** This would give \(\mathrm{P/log}\), but no exact membership-preserving padding is known; \(S(n+m)\) is not determined by \(S(n)\).
3. **Predicate-as-certificate.** Fails at \(n=4\) by non-completeness.
4. **Reachable-state transfer.** Fails by the \(\exists\)-state versus root-minimax quantifier mismatch.
5. **Compute \(e(P)\) directly.** This is the only obvious correct reduction, but counting linear extensions is #P-complete (Brightwell–Winkler), so it is not polynomial-time.

## Honest limits

- The non-transfer result is **conditional on PH non-collapse**; it is not an unconditional separation.
- It relies on the board’s Las Vegas PP-hardness of \(L_{\mathrm{fib}}\), which in turn relies on the effective Kravitz–Sah construction (paper deduction, currently unaudited). If that is weakened, the barrier still applies to any PP-hard predicate, but the specific \(L_{\mathrm{fib}}\) transfer is moot.
- Deterministic PP-hardness of \(L_{\mathrm{fib}}\) is open; it would strengthen the collapse to \(\Sigma_2\).
- The binary threshold language is not covered by the sparsity argument; per `AGENTS.md`, it remains outside the active unary workstream.
- No new exact value of \(S(n)\), no Lean theorem, and no repository change. The finding is a complexity barrier and a structural obstruction, not a proof of \(P\neq NP\) or of any unconditional separation.

The board post was recorded at #301 (`2026-11-08T06:54:20Z`, author `SoringP1 frontier: pp-hardness-transfer-antichain`) and verified as the latest message.

## Output 454 (msg_1b9f2e3ee001VsdI7EKAwStASl)

## Recovery audit

I inspected the existing conversation, working tree, Git state, board, and durable ledger before doing anything.

**Effects that actually happened**
- **Board #301:** exactly **one** comment by `SoringP1 frontier: pp-hardness-transfer-antichain`, at `2026-11-08T06:54:20.112Z`, `sha256:hyVdNUCHBwPBipYSBfwUuN8G8hboaMmkkzXvHugnWuU`. Page 1 contains one message from this author and one body matching the front title. **No duplicate.**
- **Git:** branch `billy-dev`, HEAD `6a96398`, clean worktree. No commits, edits, or repository files were created.
- **Local artifacts:** only `/tmp/opencode/post.md` and `/tmp/opencode/post_result.json`, outside the repository.
- **No new external action was taken on this recovery turn.** I did not repost, commit, or modify the ledger.

**Durable task record**
The ledger still shows the front as:
- `status: running`
- `finished_at: null`
- `exit_state: null`
- `finding_unverified: null`

So the mathematical investigation and board report are complete, but the **operational ledger status is stale**. Recording the exit/finding is the keeper’s bookkeeping step; I did not edit the ledger manually.

## Mathematical status

The finding is unchanged from the prior completed report: the Fibonacci predicate’s PP-hardness does **not** transfer to `SORT-BOUND-U` under uniform polynomial-time reductions unless the polynomial hierarchy collapses. The target is sparse and in `P/log`, so PP-hardness would put PP in `P/poly` (deterministic case, `PH=Σ₂`) or `coNP/poly` (Las Vegas case, `PH=Σ₃`). This is a conditional non-transfer barrier, not an unconditional separation.

The previously reported concrete separation is also still valid: at `n=4`, two posets with `S(P)=3` have `e(P)=6` and `e(P)=8`; with `T(3)=7`, the Fibonacci predicate differs even though `S(P)` does not. That observation was in the final report but not in the board comment; I did not add it separately to avoid an unnecessary second post.

**Conclusion:** no unfinished mathematical work and no repeated side effects. The only review item is the stale ledger entry, which the keeper should mark `investigated` on agent exit.

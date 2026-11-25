# antonina-rKdPAykGWLzO8Nu8moCQbI-ladies

Session: ses_e0e8fe440ffeMMsmNSdUBMK7xo
Workspace: /home/lubko/soring-fronts/loose-n-transition-depth-bound
Created: 1795052018662; updated: 1795052909732

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 510 (msg_1f17d8abb001kxTmIbjwi1S7RB)

## Recovery audit (done first)

- Worktree `loose-n-transition-depth-bound`: clean at `billy-dev`, HEAD `6a96398`; no repo/Lean/test/ledger changes before or after.
- Ledger entry `loose-n-transition-depth-bound` is status `running` (read only); the 01:39Z Executive post confirms this front was dispatched and interrupted, with no prior research-side effect.
- Exhaustive #301 scan: 0 prior posts by this front. Exactly **one** report posted at `2026-11-19T01:48:04Z` (`sha256:MnAgEtn_KCJCFQqgDgLSz41DbFwINWG9cg8-8DC7g7A`); no duplication.

## Mathematical finding (deduction, not new)

For every information-loose `n` (`S(n)>C(n)`), the transition depth `t(n)=min{t: L_t(A_n)>C(n)}` satisfies

` t(n) ≥ ⌊n/2⌋ + 1 = Ω(n). `

**Proof:** comparing `t` disjoint isolate pairs gives `e=n!/2^j` after `j` steps, so `L_0 = C(n)−j` and `L_t(A_n) ≤ t + (C(n)−t) = C(n)` for `2t≤n`; monotonicity gives equality. Hence the hierarchy cannot see the excess before depth `>n/2`.

- This is a **rediscovery** of the #301 post of 2026-10-20T17:33Z and the independently verified `kply-barrier-or-certificate-alln` theorem — not a new theorem. I re-derived it and checked `L_t(A_n)=C(n)` for `n=5..8`, all `t≤⌊n/2⌋` (scratch, downset DP).
- **Front answer:** the logarithmic hypothesis holds a fortiori (linear). **Falsifier:** impossible — no loose `n` has bounded `t(n)`, or even `t(n)=o(n)`. Known window `t(12)∈[18,66]` is unchanged.

## Complexity-implication audit

Correct only for **enumerative** lookahead evaluators, and quantitatively sharper than stated: the matching frontier at depth `d` has `n^{Θ(d)}` states, so even `t≥log n` forces superpolynomial exploration, while `t≥n/2` forces `2^{Θ(n log n)}`. This is a barrier to one method family, **not** a lower bound for computing `S(n)`; PSPACE/P/poly and the sparsity barriers are untouched.

## Concrete failed approach

The general-poset family `Q_m=C_m⊔C_m` is infinitely information-loose (`F−⌈log₂e⌉=Θ(log m)`), but scratch computation gives `τ(Q₅)=2`, `L_t(Q₆)=10<11=F` for `t≤3` (`τ>3`), `L₀(Q₇)=12<13=F`. It neither yields bounded transition depth nor transfers to the antichain root — general-poset excess ≠ antichain-root result.

## Honest limits

`L_t` are **sound** lower bounds; equality at `τ` certifies one value of `n`, not a polynomial-size completeness certificate for `SORT-BOUND-U`. Infinitude of loose `n` is not established, so the falsifier may be vacuous in addition to impossible. No new value of `S(n)`, no algorithm, no class result, no Lean. This is an exact obstruction and a redundancy finding, **not** a completed theorem.

# antonina-t2tsL6gKD10RPuQzc2PIzz-finds

Session: ses_e15f94bf1ffePfC7rLRcwGVH2Z
Workspace: /home/lubko/soring301-exec-n12-gap-invariant-20261117b
Created: 1794927670403; updated: 1794927754865

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 48 (msg_1ea07c8110018JzPC8W1M5Rh6u)

Wrote `exec-report.md` in `/home/lubko/soring301-exec-n12-gap-invariant-20261117b`.

**Hypothesis (tested):** the `n=12` obstruction `S(12)=30 > C(12)=29` is explained by a reusable *local* invariant stronger than leaf counting (`e(P)`/slack scalar, fixed finite-ply like `L1`, forced-prefix balance, symmetry/efficiency window, merge/ordinal-sum factors) that generalizes to an all-`n` or i.o. gap condition.

**Evidence/derivation (from repo notes + primary literature):**
- Wells/Stober–Weiß certify `S(12)>29` by exhaustive admissible-state search; no short closed-form/compact bottleneck certificate is published (efficiency pruning ≡ node info bound; search metrics are effort, not a theorem). (`docs/research-n12-nontightness.md`, Wells 1966/71, Peczarski 2012, Stober–Weiß ALENEX 2023)
- Known counterexamples defeat local/scalar generalization: sortability is non-monotone/non-functional in `e(P)` (`n=6`: `e=13,m=5` harder than `e=14,m=4`; same `e=8` gives `m=3,4` at `n=5`; Peczarski `n=13` `P16/Q'16`; Hanamura–Iwata 2011 boundary at `e=7/8`); slack/forced-prefix/symmetry occur at both tight and non-tight `n` (H1–H6).

**Generalization attempt:** checked root-local lifts and scalar/i.o. laws. Local strengthenings do not lift the antichain: `L1(P0)=C(n)` because a balanced first split is always admissible (`1+max L0(children)=C(n)`), merge/series factors are absent at the root, and slack is non-predictive (`n=5,10,11,20` tight vs `n=12,22` gaps).

**Falsification / precise barrier:** supported barrier — the obstruction is **strategic/global** (tree-level routability of all `n!` permutations through the admissible frontier), not reducible to any known state-local or `e`-scalar/fixed-ply invariant. A uniform all-`n` or i.o. gap condition stronger than `C(n)` would require a new, non-scalar strategy-aware certificate/technique; none is identified, and producing/forbidding it remains open (not proved impossible except against the audited families).

**Consequence for `S(n)` bounds:** no new uniform or i.o. lower bound beyond `S(n) ≥ C(n)` follows; certified strengthenings (`L1`, merge/rounding) are poset-local and do not upgrade the `n=12` antichain gap. This aligns with the view that progress needs strategy-aware arguments rather than local `e`/balance/merge pruning alone. All claims labeled/grounded in the report; no Lean/re-enumeration performed.

# antonina-wJQcNRH6nTdpNHpdcOfWi6-grunth

Session: ses_e19456b5fffeq6d7ekubovNK6H
Workspace: /home/lubko/soring301-exec-n12-obstruction-20261116
Created: 1794872349890; updated: 1794872984671

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 149 (msg_1e6c35c36001HsV2uqzbJ5jLlq)

**State / no-duplication check (Antonina recovery).** Inspected this worktree and durable records before taking external action: `git status` clean (no local edits/commits), `docs/operations.md` + `scripts/board_digest.py` reviewed. Board #301 (page 1) already contains a closely matching, recent material update: `n12-obstruction-invariant-20261111` (2026-11-12T01:26:06Z), which surveys/refutes computable invariants generalizing `S(12)>C(12)` (L1/L2, merge/ordinal-sum, scalar/profile invariants) and reports exact coverage/limits. To avoid duplicating an external post, I did **not** post to #301. I also did not create files, branches, commits, or run Lean. Findings below are a consolidated, checkable synthesis grounded in repo docs/scripts and that board record.

## Question (falsifiable)
Is there a general, computable poset invariant/obstruction `I` with
`C(P) := ⌈log2 e(P)⌉ ≤ I(P) ≤ F(P) := m(P)` (hence `I` sound as a lower bound on worst-case comparisons) that is strictly above `C` on a structurally characterized/infinite class and, in particular, explains/certifies the antichain-root gap `S(12)=F(A_12)=30 > C(12)=29` while generalizing to predict/constrain at least one additional case `n>=12`?
- **Consequence if yes (deduction):** a uniform, checkable strengthening of leaf-counting that narrows the exact-search/threshold window for evaluating `S(n)` / `SORT-BOUND-U` on that class (an upper-bound-side structural/certificate contribution), without implying any P/NP/PSPACE separation (`docs/problem.md`, `AGENTS.md`).
- **Falsified if (per prompt):** (a) compatible with some optimal 30-comparison strategy at `n=12` in a way that yields no separation/certification, (b) fails to separate `C(n)` from `S(n)` on known exact values, or (c) extends only as an `n=12`-fitted artifact.

## Candidate identified: `k`-ply adversarial information (pairwise-split) hierarchy
**Definition (from `docs/research-one-ply-obstruction.md`, generalized).** For a poset state `P`, incomparable pair `{i,j}`, children `P+i<j`, `P+j<i` partition extensions: `e(P)=e(P+i<j)+e(P+j<i)` (definition/deduction). Let
- `L0(P)=C(P)=⌈log2 e(P)⌉`.
- `L1(P)=0` if total else `1 + min_{i,j incomp} max(L0(P+i<j),L0(P+j<i))`.
- `L2(P)=0` if total else `1 + min_{i,j incomp} max(L1(P+i<j),L1(P+j<i))`, etc. (info-scored `k`-ply lookahead).

**Proved properties (deduction, `docs/research-one-ply-obstruction.md` Thm.1–2):** `L0(P) ≤ L1(P) ≤ F(P)` for all `P` (and by the same monotonicity-of-recursion argument `L1 ≤ L2 ≤ … ≤ F` whenever defined this way). A strict gap `L1>L0` is a sound, local pruning/certification signal; `L1` is `#P`-hard to compute in general (no poly-time claim).

## Evidence on known values / why it does not generalize to `n=12`
- **Antichain root is information-balanced at ply 1 (deduction, checkable):** for the antichain `A_n` (`e=n!`), every first comparison splits extensions exactly `n!/2, n!/2`, so for all `n>=2`,
  `L1(A_n)=1 + ⌈log2(n!/2)⌉ = ⌈log2 n!⌉ = C(n)`.
  Thus L1 can never certify `S(n)>C(n)` at the root; it is compatible with any strategy in the only sense that matters here (it gives no separation). In particular `L1(A_12)=29=C(12)` while `S(12)=30` (literature: Wells 1965/71, Peczarski 2012, Stober–Weiß ALENEX 2023; `docs/literature.md`).
- **Local but not root/global (experiment/literature in repo):** smallest strict witness `W=(26,0,10,0,8), n=5, e=8, C=3, L1=F=4` (`docs/research-one-ply-obstruction.md`, Prop.3 gives a strict witness at every `n>=5` as `W ⊕ C_t`); exhaustive `n<=4`: no strict witness. Board post `n12-obstruction-invariant-20261111` reports exact unlabeled coverage: `n<=5` slack states all detected by L1; `n=6` slack 36, L1 detects 8/misses 28 (e.g. `e=13,C=4,L1=4,F=5`); `n=7` slack 391, detects 168/misses 223; `n=8` (16999 classes, no `F`) `L1>C` on 544 but `L1(A_8)=C(A_8)=16`. `L2` stays `<=F` with 0 violations and improves some local misses (`n=6`: detects 21, misses 15) but gives no verified antichain-root lift and is infeasible to certify at `n=12`.
- **Contrast: other refuted generalizers (literature/deduction/experiment, `docs/research-n12-nontightness.md`, `docs/research-obstruction-next.md`, `docs/research-structural-lower-bounds.md`, board post):**
  - Leaf-counting/"efficiency" refinement is equivalent to node-level info bound (not stronger). Slack ratio `2^{C(n)}/n!` does not predict tightness (`n=5` tight with less slack than `n=12`; `n=20` tight/large slack, `n=22` non-tight/small slack as tabulated there).
  - `F/m` is not a function/monotone in `e` (same-`e` different-`m` at `n=5,e=8`; monotonicity violation at `n=6`, `e=13` harder than `e=14`) and not determined by `(e,width,#min,#max,|Aut|)` at `n=6`; so no low-dimensional scalar/profile invariant separates `C` from `S`.
  - Merge/ordinal-sum compositional bound strengthens only on decomposable/merge-factor states (`Merge(2,4), n=6`), but `A_n` is a single block with no certified gap so it gives `C(n)` at the root (cannot explain `S(12)>C(12)`).
  - Forced balanced prefix is real for the `h=29` budget at `n=12` (`F=2^(28)/12!≈0.5604`, so only 1/2 splits admissible early) but the same phenomenon occurs at tight `n=5,10`; it constrains, not predicts (deduction/experiment).

## Assessment (against the prompt’s criteria)
- **Identified invariant:** the `Lk` pairwise-split hierarchy is a precise, sound, general family; `L1` genuinely explains *local* non-tightness instances (and is provably strict on an infinite family `W⊕C_t`).
- **Refuted as an explanation/generalization of `S(12)>C(12)` (root case):** by the exact antichain 1-ply balance, `L1(A_{12})=C(12)` (fails to separate). Multi-ply lookahead is unverified for the `n=12` root and, per the board survey, has shown no antichain lift while missing many slack states through `n=7`; no evidence it extends beyond an `n=12`-unresolved artifact. Low-dimensional/scalar and merge-factor alternatives are likewise refuted for the antichain root.
- **Negative result (well-supported):** consistent with Wells/Peczarski/Stober–Weiß, the `n=12` gap is certified by exhaustive strategic search; available *local/computable* invariants (scalar, efficiency-equivalent, 1-ply, merge-compositional) either do not strengthen leaf-counting at the antichain root or are non-scalar/non-root. This is negative for a reusable compact invariant, not a proof that none exists.

## Decisive next test
1. **Root-lift test (primary, falsifiable):** exhibit a sound invariant `I` (`C<=I<=F`) with a *provable* value/certificate `I(A_12) >= 30` (and, ideally, the same argument on at least one other known non-tight `n`, e.g. another `n` with `S(n)>C(n)` per literature/A036604–A003070, or an infinite family) — or prove an obstruction theorem that every invariant in a specified class (e.g. any function of bounded-ply split profiles / pairwise child `e` counts / a stated scalar signature) satisfies `I(A_n)=C(n)` for balanced antichains. Either outcome is decisive for that class.
2. **Concrete discriminating computation:** for `k>=2`, compute or tightly bound `Lk` on `A_12`’s admissible (forced-prefix) descendants at budget 29 using a congruence-quotiented/canonical search (the known gap: our pure-Python forward search cannot reach `n=12`, `docs/research-n12-nontightness.md` §7.6; Stober–Weiß Table 2 gives the scale/method context). A verified `Lk(A_12)>=30` would generalize via a stated family; persistent failure across feasible `k`/quotients would sharpen the no-go.
3. **Certificate target:** produce a short, checkable human-readable certificate of `S(12)>29` (or show none of bounded size in a formalism) — the obstacle emphasized across `docs/research-n12-nontightness.md`, `research-obstruction-next.md`, and the board post.

**Labels:** definitions/deductions from repo docs are marked above; `S(12)=30`, `C(n)`, small exact values, and Stober–Weiß/Wells/Peczarski/Hanamura–Iwata facts are **literature**; unlabeled-poset counts, witness values, and board-reported `L1/L2` coverage are **experiment/reported** as cited. No claim of P/NP/PSPACE separation, no re-derivation of known `S(n)`, no Lean.

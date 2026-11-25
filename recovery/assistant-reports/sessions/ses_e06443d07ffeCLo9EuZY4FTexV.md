# antonina-FCsfNCEIan7B5HBFoXvUy3-deposit

Session: ses_e06443d07ffeCLo9EuZY4FTexV
Workspace: /home/lubko/soring-fronts/one-outcome-attainment-set-alln
Created: 1795191194477; updated: 1795192168967

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 140 (msg_1f9c8b198001x2Efj8S3km4d0v)

## Recovery / inspection (no external side effects repeated)
- Inspected this checkout and state on `billy-dev`: `/home/lubko/soring-fronts/one-outcome-attainment-set-alln`, `git status` clean on `billy-dev...origin/billy-dev` (HEAD `6cddeaa`), no local modifications/untracked work, no new commits or Lean/test changes made.
- Studied: `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/research-obstruction-next.md`, `docs/operations.md`, `docs/research-frontier.json`, and related notes (`docs/research-one-ply-obstruction.md`, `docs/research-certificates-barriers.md`, `docs/research-sergeev-asymptotic.md`).
- Board #301: ran `/home/lubko/soring301/scripts/board_digest.py --recent 7` (2026-11-20T14:44Z–16:15Z). No visible prior post on this exact Wells/one-outcome attainment question in that recent window (not a proof of absence). No `#301` post, commit, or other external action taken by me.
- Primary literature consulted: Stober–Weiß, arXiv:2206.05597v2 (2022; ALENEX 2023), abstract/§1/algorithm discussion via ar5iv text; Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ. Sapientiae Informatica 4(2) (2012), §3–§4 (text extracted from the cited PDF). Exact values/notation cross-checked against `docs/literature.md`, `docs/problem.md`, OEIS A003070/A036604 as indexed in-repo (index only).

No repository/Lean changes; no durable task record updated. This report is a mathematical analysis with explicit limits (not a kernel-checked theorem, not a complexity-class result).

## Precise claim attacked (all-`n`, falsifiable)

**Definition (MEOO, Wells/Peczarski max-extension one-outcome adversary) [definition, model-consistent with Peczarski 2012 §3 and Stober–Weiß §1/§3].** Work in the standard adaptive-comparison minimax model for `S(n)=F(A_n)` (`docs/problem.md`): states are transitively closed partial orders `P`, `e(P)` their linear-extension counts, `F(P)` remaining worst-case comparisons. For an incomparable pair `c={u,v}` write `P^+_c, P^-_c` for the two outcomes. Define `MEOO(P,0)` iff `e(P)>1`; and for `r>=1`, `MEOO(P,r)` iff for every incomparable pair `c`, `MEOO(Q_c,r-1)` holds for some/any `Q_c ∈ {P^+_c,P^-_c}` with `e(Q_c)=max(e(P^+_c),e(P^-_c))` (a single adversarial successor per algorithm comparison, chosen as a maximum-extension outcome; ties immaterial to the arguments below). This is “Wells-style” in the forward-search sense: Peczarski stores only the larger-`e` outcome when both remain below the ITLB cutoff, and Wells’ forward-only elimination occurs when a level becomes empty because some outcome exceeds `2^(C-c)`—which, since `max(e(P^+_c),e(P^-_c)) >= e(P^-_c),e(P^+_c)`, is always witnessed by the max-extension outcome.

**Soundness [deduction].** `MEOO(P,r) => F(P) >= r+1` (equivalently `P` not sortable in `r`): a valid adversary strategy forcing `>r` comparisons.

**Attainment question.** Let `A = { n >= 1 : MEOO(A_n, S(n)-1) }` be the `n` for which this restricted adversary search certifies the full minimax value `S(n)`. Asked: is `A` finite with a characterizable largest element, or infinite beyond small cases?

(Definitional note: a *positional* pure adversary strategy always picks one outcome per node in general; the substantive restriction here is the **max-extension** rule. This is the reading that matches “sufficient to check only one outcome” at `n=12` but not `13,14` in the cited sources; alternative “one committed outcome, freely chosen” would be vacuously the full game and contradicts the reported failures. I state this to separate certificate soundness from completeness of the restriction.)

## Findings

### 1. All-`n` structural theorem: MEOO always certifies the information bound [deduction]
Let `C(n)=ceil(log2 n!)`. For all `n>=1`, `MEOO(A_n, C(n)-1)`.

*Proof.* Invariant `I(t): e(P_t) > 2^(C(n)-1-t)` after `t` comparisons along any algorithm choices with MEOO responses. `I(0)`: `e(A_n)=n! > 2^(C(n)-1)` by definition of `ceil`. Step `t -> t+1` (`t <= C(n)-2`): for any comparison `c`, `e(P_{t+1}) = max(e(P_t^+),e(P_t^-)) >= e(P_t)/2 > 2^(C(n)-1-(t+1))`. At `t=C(n)-1`, `e(P_{C(n)-1}) > 1`, so the state is not total and `C(n)-1` comparisons are insufficient. ∎

**Consequence [deduction].** `{ n : S(n)=C(n) } ⊆ A` for all `n`. Hence MEOO attains `S(n)` whenever the minimax value equals the information-theoretic lower bound (a global counting argument strengthened to an explicit single-successor adversary strategy).

(Complexity note: this is a statement about the minimax/comparison game, not a lower bound on the computational complexity of evaluating `S(n)` or of `SORT-BOUND-U`; cf. `docs/problem.md`.)

### 2. Consistency map with primary literature [literature + deduction]
- `n <= 11`: `S(n)=C(n)` (Ford–Johnson/information bound equality, e.g. Knuth §5.3.1 as cited in-repo) ⇒ `n ∈ A` by (1).
- `n=12`: `C(12)=29`, `S(12)=30` (Wells 1965/66, reported by Peczarski 2012; ALENEX/Stober–Weiß context). Peczarski 2012 §3: “Wells reported [10] that for `n = 12` only the set `S24` is empty.” An empty forward set at level `c` means every comparison from every `P ∈ S_{c-1}` has some outcome with `e > 2^(C-c)`; by the max-extension witness property above this is certified by the max-`e` outcome, so there is an MEOO refutation at budget `29`. Thus `12 ∈ A` despite `S(12)>C(12)`.
- `n ∈ {13,…,19}`: `S(n)=C(n)+1` in this range (`34,38,42,46,50,54,58` vs `33,37,41,45,49,53,57`; literature summarized in `docs/literature.md` / `research-obstruction-next.md`). Stober–Weiß §1: “for `n=12` it is sufficient to check only one outcome, but for `n=13` and `n=14` it is not.” / “For 13 up to 19 elements Wells’ original algorithm does not yield a lower bound.” Peczarski 2012 §4 gives the mechanism at `n=13`, `C=33`: poset `P'_{15}` compared on `(u0,u10)` yields `P16` (`e(P16)=113400`, the larger-`e` outcome, stated sortable in 17) or `Q'_{16}` (smaller `e`, not sortable in 17); hence the max-extension adversary response `P16` fails to refute that comparison, while the true minimax refutation requires `Q'_{16}`. Therefore MEOO cannot certify `S(13)>33`, so `13 ∉ A`. By the cited 13–19 failure of the one-outcome/Wells search to yield the needed lower bounds, `{13,…,19} ∩ A = ∅`.
- `n ∈ {20,21,22}`: `S(n)=C(n)=62,66,70` (known exactly for `n <= 22`, per Knuth errata/Stober–Weiß as cited in `research-obstruction-next.md`; OEIS index only) ⇒ `{20,21,22} ⊆ A` by (1).

### 3. Falsification attempts (against naive dichotomies/thresholds)
- **“Largest element is 12” — falsified [deduction+literature].** `20,21,22 ∈ A` and `20,21,22 > 12`.
- **“Finite initial segment / small cases only” — falsified in that form [deduction+literature].** `A` contains elements beyond 12, including 20–22.
- **“Fails for all `n >= 13`” — falsified [deduction+literature].** `20,21,22 ∈ A`.
- **“Fails whenever `S(n)>C(n)` (gap cases unattainable)” — falsified [literature].** `n=12` has `S>C` but `12 ∈ A`.
- **“Succeeds whenever `S(n)>C(n)`” — falsified [literature].** `13,…,19` have `S=C+1` but `∉ A`.
- **Monotone-threshold hypothesis — no support [deduction from evidence].** Membership is non-monotone on known values: `12 ∈ A`, `13..19 ∉ A`, `20..22 ∈ A`.

### 4. Structural reason for incompleteness on gap instances [deduction, supported by literature/experiments in sources]
MEOO is complete for the entropy component (1) but can be incomplete for the structural component: minimax hardness `F(P)` is not monotone in `e(P)`. Peczarski 2012 §4 exhibits `e(Q'_{16}) < e(P16)` while `F(Q'_{16}) >= 18 > 17 >= F(P16)` (a smaller-extension outcome is adversarially harder). `docs/research-obstruction-next.md` records exhaustive small witnesses of non-monotonicity and local information-bound failure (e.g. same-`e` different `F`, and `e1<e2` with `F(e1)>F(e2)`). Therefore, for `S(n)>C(n)` the true refutation may require answering some comparison with a non-max-extension branch; MEOO attains such an `n` only if a max-extension choice remains a winning adversary move at every algorithm decision along the required certificate (a pathwise alignment, not guaranteed by `e` alone). This explains `12 ∈ A` vs `13..19 ∉ A` without asserting a general large-`n` law.

## Best current characterization (conditional) and exact obstruction

From (1)–(4): `A = E ∪ G` where `E := {n : S(n)=C(n)} ⊆ A` (all-`n`, proved above) and `G ⊆ {n : S(n)>C(n)}` are gap instances whose optimal adversary can be realized by max-extension responses (known: `12 ∈ G`; `13..19 ∉ G`).

- **Infinitude:** sufficient if `E` is infinite. (`E` infinite ⇒ `A` infinite.) Also possible in principle via infinite `G`, but no witness beyond `n=12` is known.
- **Finitude:** possible only if `E` is finite and `G` is finite. No finite characterization/largest element is supported: 12 is the largest *known* element of `G`, but not a largest element of `A` (20–22 exceed it), and no theorem bounds `A` above.
- **What remains open [open].** (i) Whether `S(n)=ceil(log2 n!)` holds infinitely often (hence whether `E` is infinite) is not settled by current results cited here. (ii) Whether any `n >= 23` with `S(n)>C(n)` admits an MEOO certificate (`G` infinite/nonempty beyond 12) is unknown. (iii) In particular `S(23)` is open in the cited literature baseline, so membership of 23 is undetermined here.

**Conclusion (honest, checkable):** Under the MEOO formalization matching the cited Wells/Peczarski behavior, the set is **not** finite with largest element 12 and **not** confined to the small cases (refuted by `20,21,22 ∈ A` via the all-`n` ITLB theorem). A complete dichotomy “finite with a characterizable largest element” vs “infinite beyond small cases” **cannot be resolved from established results**: infinitude is implied by the open condition that the information bound is tight infinitely often, while finiteness would require eventual non-tightness *and* eventual failure of max-extension certification on all gap instances—neither proved nor disproved here. I did not find (and do not claim) a proof of finiteness, an explicit threshold, or an infinite family of large-`n` MEOO gap-attainments.

## Concrete failed/insufficient approaches considered
- **Pure threshold-by-known-values / “largest is 12”**: failed immediately on `20,21,22` once the all-`n` ITLB/MEOO argument is applied.
- **Ascribing success/failure solely to `S(n)>C(n)`**: failed both ways (`12` succeeds, `13–19` fail).
- **Deriving an all-large-`n` failure from local `F`-vs-`e` non-monotonicity alone**: insufficient—local structural inversions exist (Peczarski/obstruction), but turning them into an all-`n` (or all sufficiently large gap-`n`) obstruction for the *specific* max-extension paths induced from the antichain would require a global root strategy argument not available here.
- **Settling infinitude without resolving `{n:S(n)=C(n)}`**: blocked; `E ⊆ A` makes the equality set decisive in one direction.

**Complexity implication (as requested):** a characterization of `A` would be a structural theorem about when the two-branch minimax/adversary game collapses to the single (max-extension) successor path (refining certificate/search understanding); by itself it yields no separation for `SORT-BOUND-U` and does not change the unary `PSPACE` upper-bound / tally barrier context (`docs/problem.md`).

# antonina-FPYhXIo8eZCcRh8aRQkFTV-stop

Session: ses_e3a503631ffe5L4MoEy4f6vlDF
Workspace: /home/lubko/soring-fronts/lex-prime-excess-unboundedness
Created: 1794317994459; updated: 1794319612672

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 294 (msg_1c5c75fe70019tgLY84UTIiwjq)

## Status / recovery (billy-dev, no external side effects repeated)
- Host/worktree: `billy-dev`, `/home/lubko/soring-fronts/lex-prime-excess-unboundedness` (git `6a96398`, clean, no commits/branches/PRs created). I inspected AGENTS/docs and Antonina #301 state.
- Board/ledger: `lex-prime-excess-unboundedness` is already `running` in `~/.local/state/soringp1/frontier-ledger.json` (agent `FPYhXIo8eZCcRh8aRQkFTV-stop`, started 1794317994.2188885). I read board pages 1–5 (saved under `/tmp/opencode/board301_p*.json`) and the key posts (`prime-excess-unboundedness` 01:56Z, its 02:00Z follow-up, Executive checks, and the 17:39Z `gpc-interval-order-threshold` note which gives a lex-prime definition/example). **I did not post to #301 and made no repository/Lean changes.**
- Interrupted previous turn: only scratch artifacts exist (`/tmp/opencode/lexprime/probe1.py`, partial run killed by SIGKILL; no other durable effects). I did not rerun blindly.

## Front studied (exact question)
- Question: is `d(P)=F(P)-ceil(log2 e(P))` unbounded over all finite **module-free (lex-prime)** posets `P`? (falsifier: an infinite module-free family with `d(P)->∞`, or a uniform constant bound for every module-free `P`.)
- Definitions [definition]: `F` is the exact minimax comparison number, `e` the number of linear extensions, `d` the information excess. A (Gallai/autonomous) module `M⊆P` has every `z∉M` uniform to `M` (above all / below all / incomparable with all). `P` is **module-free (lex-prime)** if its only modules are `∅`, singletons, and `P` (Gallai 1967 decomposition; cf. `docs/research-orientation-modules.md`, and the board’s use in 17:39Z “no nontrivial lexicographic module”). 
- Distinction [deduction/literature context]: the 01:56Z construction is **graph-prime** in the sense `Comp(P),Inc(P)` connected (neither a nontrivial ordinal sum nor a disjoint union) — its §8(vi) explicitly states a module-free version is not claimed. Module-free ⇒ graph-prime in that sense, but not conversely (internal modules allowed by graph-connectivity primeness).

## Mathematical finding (paper argument, independently checkable)

### 1. The 01:56Z graph-prime family is not module-free [deduction]
Base `P1=(A_m ⊕ A_k)-{(a0,b0)}` (`A_m` bottom antichain, `A_k` top, one cross edge removed). In an antichain every subset is a module (all outside elements incomparable to it), so for `m>=3` any `{a1,a2}⊆A_m\{a0}` is a nontrivial module of `A_m` avoiding `a0`. Every `y∈A_k` is still above every element of `A_m\{a0}` (only `(a0,b0)` was removed), hence `{a1,a2}` remains a nontrivial module of `P1`. Thus `P1` is not lex-prime (though it is `Comp/Inc`-connected). The same holds for the iterates built from antichain components.

### 2. Single-cross-deletion lemma and module-free-preserving amplification [deduction]
Let `X,Y` be nonempty finite posets, `x` maximal in `X`, `y` minimal in `Y`, and `P=(X ⊕ Y)-{(x,y)}` (all relations inside `X,Y` and all cross relations except `x<y`).

- **Module characterization.** If `M⊆X` is a module of `P`, then for `m∈M, m'∈X\{M}` uniformity against `X\{M}` is the same as in `X`, and every `z∈Y` is above every element of `X\{x}`. Therefore: (i) if `x∉M`, `M` is a module of `P` iff `M` is a module of `X`; (ii) if `x∈M` and `M≠X`, pick `m'∈X\{M}` and note `y` is incomparable to `x` but `y>m'`, so `y` is not uniform to `{x,m'}` across the boundary — impossible when `M` is a module containing `x` and missing some `m'`? equivalently, a proper subset of `X` containing `x` cannot be a module of `P` because `y` sees `x` and `X\{x}\supseteq X\{M}\neq∅` differently. `M=X` is not a module of `P` for the same reason (`y !> x` but `y > X\{x}` when `|X|>=2`). Symmetrically for `M⊆Y` with `y`.
  A module spanning both `X,Y` properly cannot be uniform to the omitted elements of the opposite side except trivial cases excluded. Hence:
  **`P` is module-free iff `X` has no nontrivial module disjoint from `{x}` and `Y` has no nontrivial module disjoint from `{y}`.** In particular, **if `X` and `Y` are module-free, then `P` is module-free** (a module-free poset has no nontrivial module at all).

- **Excess amplification (reusing 01:56Z’s proved identities, model-compatible).** The 01:56Z/02:05Z argument gives, under exactly these hypotheses: (a) `e(P)=e(X)e(Y)+e(X-x)e(Y-y) ≤ 2e(X)e(Y)` (partition by whether `x<y`, and `y<x` forces `X\{x} < y < x < Y\{y}` by intact cross relations and max/min choice); (b) `F(P) ≥ F(X⊕Y)=F(X)+F(Y)` (restriction/monotonicity and ordinal-sum additivity of the minimax value). Therefore
  `d(P)=F(P)-ceil(log2 e(P)) ≥ F(X)+F(Y)-ceil(log2 e(X)+log2 e(Y)+1) ≥ d(X)+d(Y)-1`.

### 3. Reduction to a single finite witness [deduction]
Combining 2: **if there exists any module-free poset `P0` with `d(P0) >= 2`, then `sup{d(P): P module-free}=∞`**. Proof: set `P_1=P0`, `P_{c}= (P_{c-1} ⊕ P_1)-{(x_c,y_c)}` with `x_c` maximal in `P_{c-1}`, `y_c` minimal in `P_1`; by induction each `P_c` is module-free and `d(P_c) >= d(P_{c-1}) + d(P0) - 1 >= c+1` (e.g. base `d>=2` gives `>=2c+1` in the best case; any `d>=2` suffices for linear growth).
Conversely, if every module-free poset satisfied `d(P) <= 1`, the supremum would be <=1. Thus the front reduces to the precise all-finite-posets dichotomy: **`∃` module-free `P` with `d(P)>=2` (⇒ unbounded) vs `∀` module-free `P, d(P)<=1` (⇒ bounded)**. I found no proof either way.

### 4. Exact small-n data (exhaustive labelled, recomputed; [experiment], scratch `/tmp/opencode/lexprime/probe1.py`)
Using the standard labelled successor-bitmask DP for `e` and memoized minimax for `F` (same model as repo probes) over all transitively closed posets on `n` labelled elements, testing module-freeness by exhaustive module scan:

| n | all posets | module-free (labelled) | max `d(P)` over module-free |
|---|---:|---:|---:|
| 1 | 1 | 1 | 0 (`F=0,e=1`) |
| 2 | 3 | 3 | 0 (antichain gives `F=1,e=2`) |
| 3 | 19 | 0 | — |
| 4 | 219 | 24 | 0 (e.g. `F=3,e=5`) |
| 5 | 4231 | 360 | 1 (e.g. `F=4,e=8`, `d=1`) |
| 6 | 130023 | 17400 | 1 (e.g. `F=7,e=61`, `d=1`) |

So no module-free `d>=2` witness exists for `n<=6`; `d=1` first appears at `n=5`. (Counts are labelled-poset counts; the values `F,e,d` are isomorphism invariants.)

## Failed / incomplete approaches and exact obstructions
- **Failed adaptation:** directly reusing the 01:56Z antichain-based witness/family as lex-prime is impossible because antichain components create internal modules (and the base retains modules disjoint from the deleted endpoint), §1.
- **Not completed:** exhaustive search for `n>=7`. `n=7` is already large over all labelled posets (`~6.1M` states) with per-state `F/e` evaluation; my `n<=8` attempt was interrupted (SIGKILL) and I did not obtain `n=7` results. A targeted/unlabelled or structural search is needed but was not carried out to a conclusion.
- **Not proved:** I did **not** prove or refute `∃` module-free `P` with `d(P)>=2`, and I did **not** prove `d(P)<=1` for all module-free `P`. The amplification lemma makes `d>=2` a sufficient (and effectively necessary, given the reduction) condition for unboundedness, but this finite/witness existence remains open from what I established.
- **No counterexample family found:** I did not exhibit any infinite module-free family with `d->∞`, nor any `d>=2` module-free instance.

## Complexity/model implications and honest limits
- **Implication (conditional):** if a module-free `d>=2` witness exists, unbounded excess is not reliant on nontrivial modules/ordinal-sum gluing inside components except the single-edge amplification gadget — i.e. the prime-excess barrier would persist in the lex-prime core. If instead `d<=1` holds for all module-free posets, amplification by nontrivial modular/ordinal-sum structure would be isolated as necessary for large excess. Either outcome would be a structural theorem about the minimax game/states, **not** by itself a bound or separation for computing `S(n)` or for `SORT-BOUND-U` (AGENTS: state-complexity/excess phenomena do not directly yield uniform time/space class results; `SORT-BOUND-U ∈ PSPACE` already holds).
- **Soundness vs completeness:** `F(P) >= ceil(log2 e(P))` and the 01:56Z count/lower-bound identities used are sound inequalities; nothing here provides a polynomial-time checkable completeness/certificate claim for optimal `F`, and no NP/coNP membership or hardness claim is made.
- **Scope limits:** results are about `d(P)` on (general/module-free) posets; no claim about `S(n)=F(A_n)`, no new value of `S(n)`, no `P/NP/PSPACE` separation, no Lean/kernel claim. Lemma 2’s proof sketch above is a paper-level argument and should be treated as **deduction (unreviewed here)** pending a fully formalized case split; the `n<=6` table is **experiment**. Primary structural sources: Gallai (1967) modular decomposition / lex-prime notion; board 01:56Z for the `e,F` identities of the single-deletion gluing (independently re-derived in outline). No primary literature was found settling module-free excess.

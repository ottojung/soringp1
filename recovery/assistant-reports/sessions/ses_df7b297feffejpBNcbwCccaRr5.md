# antonina-s6m988XI3qqEre4u0hvthq-cooked

Session: ses_df7b297feffejpBNcbwCccaRr5
Workspace: /home/lubko/soring-fronts/fotc-optimal-strategy-poly-size-alln
Created: 1795435620374; updated: 1795436128803

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 177 (msg_20851126a001JW2NQEM134cKms)

## Scope and evidence

- Read: `AGENTS.md`, `docs/problem.md`, `docs/research-certificates-barriers.md`, `docs/operations.md`, `docs/research-frontier.json`, and board #301 via `scripts/board_digest.py --recent 7` / `--contains "FO(TC)"`.
- The prompt-referenced evidence file `docs/research-fo-tc-strategy-programs.md` is **not present in the current worktree**. I read the closest git-history artifacts at commit `9018729`: `docs/research-fotc-strategy-programs.md` and `docs/research-fotc-publication-record.md`. I treat them as evidence, not as current-tree truth. No repo files were created or modified; the small-n counting script below was run only in `/tmp`.
- Labels: `[definition]`, `[literature]`, `[deduction]`, `[experiment]`, `[open]`. No theorem completion for `S(n)`/`SORT-BOUND-U`, no complexity-class separation, no Lean.

## Front (as assigned)

> For all integers `n>=2`, does every height-`S(n)` optimal adaptive comparison tree admit a fixed-interpreter `FO(TC)` strategy program of polynomial text size in `n` and polynomial per-input interpreter runtime on all permutations, enabling poly-time verification of that strategy’s worst-case depth `S(n)`?

Falsifier target: infinitely many `n` where every height-`S(n)` optimal strategy needs superpolynomial FO(TC)-program text or superpolynomial runtime, via an explicit combinatorial/information obstruction.

## Model / fidelity checks

- `[definition]` I use the fixed model: `S(n)` is the minimax height of a deterministic adaptive pairwise comparison decision tree sorting all permutations of `n` distinct labelled keys (`docs/problem.md`). A strategy program is a finite description executed by a fixed uniform interpreter; `FO(TC)_v`/ESP-style accounting means fixed variable bound/clocks and charged comparisons only, as in the 9018729 FO(TC) note (Lemma A, combined polynomial bound under fixed `v,d,c`).
- `[deduction]` "Per-input polynomial runtime" and "poly-time verification of worst-case depth over all permutations" are different properties. The first is a single-trace execution bound; the second is a universal property over `n!` inputs. They must not be conflated (the same soundness/completeness gap flagged in `research-frontier.json` and `research-certificates-barriers.md`).

## Mathematical findings

### 1. Verification gap blocks the "enabling poly-time verification..." clause (deduction)

- `[literature/deduction]` For a fixed poly-time program/interpreter `U`, the predicate `V(p,n,k) := ∀X∈S_n, Verify(p,X,n,k)` has poly-time-checkable counterexamples: guess an `O(n log n)`-bit encoding of a permutation `X`, run `U(p,X)`, reject if it exceeds `k` or mis-sorts. Thus `V(p,n,k) ∈ coNP` relative to a fixed poly-time program. Adding an existential polynomial-size program guess gives the `Σ₂^P`-shaped subclass `QWIN` described in the 9018729 FO(TC) note, **not** P or NP. This is conditional on the fixed combined interpreter bound and does **not** prove `SORT-BOUND-U ∈ Σ₂^P`.
- `[deduction]` Therefore per-input poly-time FO(TC) evaluation does **not** by itself enable poly-time verification of the strategy’s worst-case depth `S(n)` in the P/NP-certificate sense. It gives per-trace soundness and a coNP counterexample shape, but the universal worst-case claim remains unverified unless an additional poly-time universal proof/certificate is supplied. This is an exact obstruction to the front's verification clause as stated.

### 2. "Every optimal tree" hits an information-theoretic counting obstruction; asymptotic disproof not completed (experiment + deduction)

- `[deduction]` Counting lemma: fix an interpreter `I` and a polynomial bound `p(n)`. There are at most `2^(p(n)+1)` program texts of length `<= p(n)`. Let `N_opt(n)` be the number of height-`S(n)` optimal labelled comparison decision trees (trees where every node chooses a minimax-optimal comparison for its reached poset state). If `N_opt(n) > 2^(p(n)+1)`, then not every height-`S(n)` optimal tree admits such a program. Hence the front's universal "every optimal tree" claim implies `N_opt(n) <= 2^(poly(n))` for some fixed scheme, a strong combinatorial compression claim.
- `[experiment]` Exhaustive minimax/count over all posets (transitive-closure states, memoized) in `/tmp`, no repo changes:

  | n | S(n) | N_opt(n) | log2 N_opt(n) |
  |---:|---:|---:|---:|
  | 2 | 1 | 1 | 0 |
  | 3 | 3 | 12 | ~3.58 |
  | 4 | 5 | 27,744 | ~14.76 |
  | 5 | 7 | 2,418,647,040 | ~31.17 |

  The computation counts all optimal decision trees by `R(total)=1`, `R(P)=∑_{c optimal in P} R(P+c^<)*R(P+c^>)`; root symmetry gives `C(n,2)` optimal first comparisons. This is small-n calibration only; it does **not** prove asymptotic super-2^{poly(n)} growth.
- `[deduction/open]` A complete falsifier in the requested form would prove `N_opt(n) = 2^(ω(poly(n)))` for infinitely many `n`, e.g. by exhibiting ω(poly(n)) independent minimax-optimal choice points in every/any optimal strategy family. I did **not** obtain such an all-n proof. The obstruction is concrete: proving many independent optimal choices requires control over exact minimax values `V(P)=S(P)` along optimal plays, and the exact `S(n)` structure is open in general; near leaves choices can be forced, while top levels plausibly have large branching. Thus the counting route is a serious falsifier candidate, but not closed here.

### 3. Distinguish existence/compression from "every tree" (deduction)

- `[deduction]` The 9018729 note's Conjecture C asks for *existence* of some poly-size exact program per yes-instance. The assigned front is strictly stronger in two ways: it quantifies over **every** height-`S(n)` optimal tree, and it asks for **poly-time worst-case-depth verification**. Even a positive answer to Conjecture C would not imply this front; conversely, refuting "every optimal tree" by counting would not refute existence of some compressible optimal strategy.

## Concrete failed / incomplete approaches

1. **Asymptotic counting disproof (incomplete).** I attempted the information-theoretic route: show `N_opt(n) > 2^{p(n)}` for all polynomials `p`. Small-n data shows rapid growth, but I could not prove an all-n/infinite-family lower bound `2^(ω(poly(n)))`. The missing step is a provable supply of independent minimax-optimal alternatives along optimal plays for infinitely many `n`.
2. **Direct FO(TC) representability lower bound (not obtained).** I did not construct an explicit optimal strategy whose next-comparison function is provably outside fixed-interpreter FO(TC) with poly-size program parameter on poly-size state structures. A data-complexity capture argument is invalid for growing program texts (as the 9018729 note already warns); combined-complexity/descriptional lower bounds for this exact model were not established.
3. **Verification by per-input simulation (fails).** Checking all `n!` permutations is exponential; per-input poly-time is soundness only. No poly-time universal verifier or succinct worst-case proof was found.

## Honest limits / exact obstruction

- **No disproof proved.** I did not exhibit infinitely many `n` with a superpolynomial text/runtime obstruction for all optimal FO(TC) realizations. The strongest solid obstruction is the **verification-gap**: poly-per-input execution does not give poly-time worst-case-depth verification (coNP/Σ₂^P shape, not P/NP).
- **No affirmative proof.** I did not construct poly-size FO(TC) programs for all optimal trees, nor for some optimal tree for all `n`.
- **Key open subproblem.** Prove or refute: `log2 N_opt(n) = ω(poly(n))` (or at least > poly(n) infinitely often). A positive answer would falsify the "every optimal tree" representability clause by pure counting for any fixed interpreter; a negative/upper-bound answer would make succinct representation at least information-theoretically possible but still leave FO(TC) realizability and worst-case verification open.
- **Complexity implication (careful).** Affirmative evidence for *existence of a verifiable* succinct strategy witness would support NP/coNP-style certificate routes for `SORT-BOUND-U`; but this front as stated overclaims by bundling representation and universal verification. A refutation of the verification clause alone would not settle `SORT-BOUND-U ∉ NP`; it would only rule out this specific poly-time-verification-by-execution route.

## Output 266 (msg_2085493b2001AucNhjxgydG4LJ)

I've verified the recovery state. Let me check the exact mandate this front was launched with, to determine whether a board post is an outstanding deliverable.

## Output 285 (msg_20854f3d1001mlXvIBzanGFPcb)

## Recovery audit — complete

I inspected the conversation, the working directory, Git state, the durable ledger, and board #301. Findings:

| Effect | Status |
|---|---|
| Repository files / Lean / tests / CI / ledger | **No changes.** Both worktrees clean at `6a96398`; `git log` unchanged. |
| Commits / PRs / branch pushes | **None.** |
| Board #301 posts | **None.** Searched all 11 pages for the front slug `fotc-optimal-strategy-poly-size-alln`, the distinctive phrase "every height-S(n) optimal tree", and the computed count `2,418,647,040` — zero matches. |
| Antonina agents / purchases / other external actions | **None.** The only CLI calls were read-only (`board show`, `board access`, `agent` capability check). |
| Ledger entry | Front `fotc-optimal-strategy-poly-size-alln` is still `running` with `finding_unverified: <none>` and agent `s6m988XI3qqEre4u0hvthq-cooked`. I did **not** modify it (keeper-managed). |
| Scratch | Only local `/tmp/count_optimal.py` from the counting experiment — not an external side effect. |

**Conclusion: the previous turn performed no external side effects.** Everything was reads plus a local computation; the mathematical report was already delivered in full at the end of that turn. Host is `billy-dev` (confirmed via `hostname`), so the original mandate's location requirement was satisfied.

## Unfinished work

None. The base mandate is "On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof" — that report was already produced. There is no outstanding board-post, commit, or ledger obligation: the front's outcome is an **honest inconclusive result** (no new theorem, no disproof), which under the research packet ("post only if an independently checked theorem/falsification truly changes the research picture; if no result, say no result and why") does not warrant a new external write — and the recovery instruction forbids inventing one under uncertainty.

## Finding being preserved (already reported, restated briefly)

- **Exact obstruction (deduction):** per-input polynomial FO(TC) execution gives a `coNP`/`Σ₂^P`-shaped worst-case verification, not poly-time verification of `S(n)`. The front's "enabling poly-time verification" clause fails as stated.
- **Failed disproof (experiment + deduction):** the "every optimal tree" clause is vulnerable to a counting obstruction, but I could not prove `N_opt(n) = 2^{ω(poly(n))}` for infinitely many `n`. Small-n counts (`N_opt(4)=27,744`, `N_opt(5)=2,418,647,040`) are calibration only. The all-n counting step remains the open subproblem.

No action taken this turn beyond verification. Nothing is duplicated, and no uncertain side effect is being papered over — the audit shows there was nothing to replay.

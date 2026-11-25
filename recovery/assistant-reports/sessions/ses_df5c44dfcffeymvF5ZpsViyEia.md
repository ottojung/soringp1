# antonina-XBW6ZJFkyvflN0AyDPgiHP-phase

Session: ses_df5c44dfcffeymvF5ZpsViyEia
Workspace: /home/lubko/soring-fronts/annotated-child-deck-f-completeness-alln
Created: 1795468014116; updated: 1795469905366

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20a3bb8ee001gfv03LuBSIezXA)

I'll start by understanding the repository structure and reading the required documents.

## Output 88 (msg_20a3c1861001JtQIVvTctk1WND)

I'm on billy-dev. Let me read the relevant research docs to understand prior findings and avoid repetition.

## Output 117 (msg_20a3ce11b001AgQ3qseRFBMOIs)

Let me check the available tooling and prior scratch work, and look at the repo scripts.

## Output 213 (msg_20a3e0b91001E6a7WqNsQW1LWj)

I have a working compiler setup. Let me create a compile helper and start building a from-scratch poset engine.

## Output 258 (msg_20a3fd9d8001kJmMCFQ6VyhcpN)

My engine matches the board exactly (e=32, F=5/6, M1, S(7)=13, and 6,129,859 memo states). Now let me build the canonical-form generator and n=8 exhaustive search.

## Output 319 (msg_20a43e09b001J9vFAh2OpI0yxz)

Canon is validated (matches A000112 counts). Now the n=8 exhaustive search.

## Output 378 (msg_20a448de30010EoHyOMA9dYcqD)

Engine reproduces board (n=6: 155 groups; n=7: 915 groups, 0 conflicts). Now n=8:

## Output 389 (msg_20a4513ce001oIrWwyuOLqJP5U)

No counterexample through n=8. Let me test a key theoretical question: whether the "relaxed" deck-computable value (min over *all* compatible record pairs, ignoring sibling identity) always equals the true F. If so, that's a correct proof of the theorem.

## Output 407 (msg_20a45e270001M3CH7ShaENT94k)

Important: the relaxed deck-computable bound is strictly below true F for 20 posets at n=8 — the sibling pairing genuinely matters. Let me examine those cases in detail.

## Output 479 (msg_20a578549001CS6NjyICAGYUal)

## Recovery / side effects

- **Host**: `billy-dev`, `lubko`, 2026-11-23T21:07Z+ (checked at recovery). Repo `/home/lubko/soring-fronts/annotated-child-deck-f-completeness-alln` is clean on `billy-dev` at `6a96398`; `git status` clean before/after; no commits, no stash, no PRs, no Lean/test/CI edits.
- **Board**: I did **not** post to #301. I only read it via `board_digest.py` and `antonina board show --json`. The 21:27:30Z Viche correction notes `annotated-child-deck-f-completeness-alln` is currently running as a curator-dispatched front; I therefore avoid duplicating any external post.
- **Local scratch only**: `/tmp/opencode/mydeck/` (engine.h, canon.h, validate.cpp, gentest.cpp, search.cpp, relaxed.cpp, diag.cpp, compiled binaries). No external side effects. A `diag 8` run was SIGKILLed after a timeout; no partial artifact was used.

## Sources read (primary/local)

- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`.
- `docs/research-one-ply-obstruction.md` (model/notation for F,e).
- Board #301: 20:45Z Viche verification of Finding 3 (n<=7, 915 groups, 0 mixed-F, 45,360 equal-e/different-F child cases); 19:39Z/19:31Z depth2/M2 referee chain; 21:27Z Viche global n=8 (e,M1,M2) census (different invariant). I did not reuse reporter code/artifacts.

## Front (as given)

For finite poset `P`, `D*(P)` = multiset over incomparable pairs `{x,y}` of annotated pair records `((e(P+x<y),F(P+x<y)), (e(P+y<x),F(P+y<x)))`, with `e`=#linear extensions, `F`=exact minimax sorting cost. Question: is `F` a total function of `D*(P)` for all finite posets?

## Mathematical finding

**Status: [deduction, elementary] — the answer is YES, by definition of F plus the e-sum pairing identity; no counterexample exists. The all-n question is settled in the affirmative, but it is a tautological/structural consequence, not a new algorithmic or complexity consequence.**

### Proof

Let `P` be a finite poset. Two cases:

1. **`P` is total (no incomparable pairs).** Then `D*(P)=∅` and `F(P)=0`. Determined.
2. **`P` has at least one incomparable pair.** By the standard minimax recurrence for exact adaptive comparison sorting on a poset state ([definition], same model as `problem.md`/`research-one-ply-obstruction.md`),
   `F(P) = 1 + min_{ {x,y} incomparable in P } max(F(P+x<y), F(P+y<x))`.
   Every term in this min-max is exactly one annotated sibling pair in `D*(P)`, and `D*(P)` contains exactly these pairs. Therefore `F(P)` is computed directly from `D*(P)` by this formula. ∎

The pairing-ambiguity falsifier mentioned in the front is blocked: even if pairing were not stored, it is uniquely recoverable from `e` alone. For any incomparable pair `e(P+x<y)+e(P+y<x)=e(P)`. Given the unpaired e-multiset `v1<=...<=v2m` and `S=e(P)`, the minimum `v1` must pair with `S-v1`; the maximum `v2m` has partner `S-v2m >= v1`, hence `v2m <= S-v1`, while `v1`'s partner being present gives `S-v1 <= v2m`, so `v2m=S-v1`; remove and induct ([deduction], same argument as Viche 20:45Z). Thus there is no pairing ambiguity, including in the 45,360 n=7 cases with equal-e/different-F children observed on the board.

### What this is / is not

- **Is**: a sound all-n structural theorem in the stated general-poset form. It identifies `D*` as a sufficient statistic for `F` (indeed an immediately sufficient one).
- **Is not**: a theorem computing `S(n)`, a faster evaluator, a succinct certificate, an NP/coNP membership argument, or any complexity-class consequence for `SORT-BOUND-U`. It gives no polynomial certificate because `F(child)` is itself the hard quantity; it also has no transfer to the antichain root `S(n)` without an explicit reduction (general-poset result, per `AGENTS.md`).
- It does **not** imply completeness of any deck omitting `F` (e.g. `M1`, `M2`, or e-only decks); those remain the hard/open invariant-completeness questions and are different fronts.

## Independent finite evidence (experiment, from scratch, /tmp only)

I built a fresh C++17 engine (`/tmp/opencode/mydeck`, clang 19.1.7 + guix libstdc++) with: bitmask transitive closure, ideal-subset DP for `e`, memoised minimax for `F`, and individualization-refinement canonical labeling. No reporter code/artifacts reused.

- **Validation**: reproduced the n=7 Lemma D cospectral pair exactly (`e=32, F=5/6, M1` equal, `D*` different as expected); `S(7)=F(A7)=13`, memo 6,129,859 states. Labelled/canonical generation matches A001035/A000112: n<=7 labelled 1,3,19,219,4231,130023,6129859; unlabeled 1,2,5,16,63,318,2045.
- **D*-completeness census (unlabeled, grouped by `(e(P), sorted unpaired (e,F) child multiset)` — equivalent to `D*` by pairing recovery):**

| n | unlabeled posets | D* groups | mixed-F groups |
|---:|---:|---:|---:|
| 6 | 318 | 155 | 0 |
| 7 | 2045 | 915 | 0 |
| 8 | 16999 | 7569 | 0 |

This extends the board's verified n<=7 D*-census to n=8 with 0 conflicts. It is finite evidence consistent with (and now explained by) the all-n deduction above.

## Concrete failed/obstructed proof strategy (useful negative)

I tested a stronger-looking "relaxed" deck lower bound: ignore sibling pairing and take `Flo(P)=1+min_{records r!=s, e(r)+e(s)=e(P)} max(F(r),F(s))`. This would be a deck-only bound without using pairing. **Result [experiment]:** `Flo==F` for all n<=7 unlabeled posets, but **`Flo < F` for 20/16999 unlabeled n=8 posets** (first witnesses found: e=392 F=10 Flo=9; e=240 F=9 Flo=8). Thus the e-sum-compatible-but-not-sibling pairing can be strictly better for the adversary in the relaxed view; the true sibling pairing is load-bearing. This does **not** contradict D*-completeness (true D* includes pairing), but it rules out the naive "forget pairing, only use e-sums" proof shortcut and confirms the pairing-recovery/e-sum identity is the right structural ingredient.

## Honest limits

- The all-n D*-completeness proof is elementary/definitional; I am not claiming it as a deep breakthrough. It should be sanity-checked by an independent reader because trivial-sounding structural claims can hide model mismatches.
- The n=8 census is an [experiment] in my scratch engine, not kernel-checked and not in-repo. I did not re-run the full 6.1M labelled n=7 census myself except through small validation cases and A001035/A000112 counts; I rely on the 20:45Z independent verification for that labelled count.
- No consequence for `S(n)`, `SORT-BOUND-U`, NP/coNP/P, or a faster evaluator. The front's own complexity implication is accurate: "no polynomial certificate because F(child) is itself the hard quantity; general-poset result with no transfer to S(n) without an explicit reduction."

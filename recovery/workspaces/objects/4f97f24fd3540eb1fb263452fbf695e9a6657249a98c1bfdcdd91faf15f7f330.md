# Front `linear-extension-count-obstruction`: reachability is no restriction, and F carries only a windowed count signal

Date: 2026-11-04. Agent: billy-dev unary researcher (worktree
`research/le-count-obstruction-20261104`). Model: `docs/problem.md`,
`docs/upper-bound.md`, `scripts/state_compression.py` (states = transitively
closed strict orders as successor bitmasks; `F(P)` = minimax height).
Prior ledger exit for this front was `blocked failed` (an exit failure, not a
mathematical verdict). This note is the missing analysis plus exhaustive
small-`n` verification.

## 1. The question, made precise

> Can the #P-hardness of counting linear extensions be encoded into the
> minimax height evaluation for some infinite family of partial orders
> reachable from the antichain, establishing that computing `F(P)` is #P-hard
> on the SORT-BOUND-U state graph *without reducing arbitrary posets
> directly*?

The reachable state graph of SORT-BOUND-U has the antichain `A_n` at its
root; a comparison `x<y` (on an incomparable pair, transitively closed)
is a directed edge. States are the labelled posets on `n` elements
(OEIS A001035).

## 2. Lemma 1 (exact transcript depth) — the evasion clause is vacuous

**Claim (paper proof, kernel-verified for all states, n ≤ 6).** For every
labelled poset `P` on `n` elements, the minimum number of comparisons along
any path from `A_n` to `P` equals `|Cov(P)|`, the number of cover relations
of `P` (the size of its transitive reduction).

*Proof.*
(i) *Necessity.* Only performed comparisons and their transitive closure
ever order a pair; any relation of `P` implied by performed comparisons
follows from a directed chain of *cover* comparisons that were themselves
performed. If a cover `a < b` of `P` were implied by other performed
comparisons, there would be a chain `a < x₁ < … < x_m < b` inside the order
generated so far, and each step must be either performed or implied —
iterating down to covers of the final order, each cover on the chain must
have been performed. But `a < b` is a cover of `P`, so no interior `x`
exists: the chain has length 1, i.e. the comparison `a<b` itself. Since `a<b`
was not assumed performed, `a<b` cannot be implied. Hence every cover of `P`
must appear in the transcript, so depth ≥ `|Cov(P)|`.
(ii) *Sufficiency.* Perform the covers of `P` in any order. Before adding a
cover `a<b`, the currently known relations are a subset of the relations of
`P` whose transitive implications are composed of covers already added; none
of these can imply `a<b` (same interior argument). So at each step the pair
is incomparable — the move is legal — and after `|Cov|` steps the closure is
exactly `P` (covers generate a poset). ∎

**Verification (experiment, kernel-checkable).** Exhaustive BFS from the
antichain, comparing each reachable state's min-depth to `|Cov(P)|`:

| n | reachable labelled states | violations |
|---|---|---|
| 2 | 3 | 0 |
| 3 | 19 | 0 |
| 4 | 219 | 0 |
| 5 | 4231 | 0 |
| 6 | 130023 | 0 |

Probe: `notes/le_count_obstruction_probe.py` (results section 5).

**Theorem 2 (consequence, literature + deduction).** *Computing `e(P)` is
#P-hard on the SORT-BOUND-U state graph under the natural description.*
Brightwell–Winkler (Order 8 (1991) 225–242) prove `e(P)` #P-complete for
posets given explicitly. By Lemma 1, a poset given by its cover list is
*exactly* a reachable state given by a shortest reaching transcript: the two
descriptions have the same pair multisets and the same length. So the
classical #P-complete instances are literally states of this graph, at depth
`|Cov|` from the antichain, and any polynomial-time algorithm deciding
`e(P)` on reachable states would decide #P-complete counting. ∎

**Corollary 3 (the front's requested route does not exist).** The clause
"without reducing arbitrary posets directly" cannot be satisfied by any
correct reduction. Let `Ψ` be any encoding mapping a #LE instance to a
reachable state (or family of states) whose `F`-value(s) reveal `e(P)`. By
Lemma 1, the target states are reachable *via transcripts that are the
transitive reductions of those states*, so composing `Ψ` with the standard
cover-encoding of the witnessing states yields an ordinary direct reduction
from `e`-on-covers to `F`-on-states. There is no third route: *any* state
reachable from the antichain is directly writable as an explicit poset with
comparable description size. Hence the front reduces verbatim to the already
tracked open question — is exact `F(P)` (equivalently exact `S(P)` from a
state) #P-hard under cover descriptions? — recorded open in
`docs/research-hardness-boundaries.md` §5, and one-shot reductions are
already excluded by Corollary 5.2 there (`e(P)` does not determine `F(P)`).

## 3. What the "learning structure" can and cannot transmit (the falsifier's second horn)

The falsifier's alternative is: "the reduction is impossible due to the
structure that comparison learning preserves". That structure was measured,
exhaustively over all reachable states at `n ≤ 6` (130 023 states; probe
below). Four laws hold; the first three are candidates for all-`n` lemmas.

**L1 — one-ply Lipschitz law.** For every reachable `P` and *every* legal
comparison `(x,y)` (not just optimal ones),
`F(P) − max(F(P+x<y), F(P+y<x)) ≤ 1`; at `n ≤ 5` and `n = 6` there are
0 out of all moves with drop ≥ 2. So no single added relation removes more
than one unit of minimax height: an `F`-gadget can shift its observable by at
most 1 per changed input relation.

**L2 — value window.** Over all reachable states,
`F(P) / log₂ e(P) ∈ [1.000, 1.351]` at `n ≤ 6` (and `n = 5`:
`[1.000, 1.333]`). For all `n`, Kahn–Saks (1984) give a
comparison with both children in `[3e/11, 8e/11]`, so every ply reduces
`log₂ e` of the surviving branch by at least `log₂(11/8)`, hence
`F(P) ≤ log₂(e(P)) / log₂(11/8) + O(n) ≈ 2.18 log₂ e(P) + O(n)` for all `P`
(literature), while `F(P) ≥ ⌈log₂ e(P)⌉` always (information bound).
`F` is therefore everywhere sandwiched in a *constant-factor window* around
`log₂ e(P)`; its dependence on the count's magnitude is a log-scaled signal.

**L3 — equal-count stability.** If `e(P) = e(Q)` then `|F(P) − F(Q)| ≤ 1`
for all reachable states at `n ≤ 6`. Collisions exist (the known `n = 5,
e = 8` pair with `F ∈ {3,4}`; at `n = 6` the count values
`{8,13,14,15,16,30,60,120}` are the only ones splitting between two
consecutive `F` values), but the split width never exceeds 1.

**L4 — lossiness from the other side.** Many distinct counts share one
`F`-value: at `n = 6`, within a single `F`-class the count `e` ranges over a
spread of 120 (counts up to 720); at `n = 5`, spread 20. So `F` is far from
injective in `e` above, and `e` is far from being readable from `F` below.

**What this does and does not prove.** `[deduction]` L1 + L2+L3 say the
observable `F` transmits, per comparison, at most one unit of height, in a
value window of constant multiplicative width, with at most one unit of
instability among equal-count states. A *one-query* or count-read-off
reduction is thereby excluded (consistent with Corollary 5.2 of
`research-hardness-boundaries.md`, now strengthened from "e does not
determine F" to "F varies by at most 1 on equal-long-count states, n ≤ 6").
`[deduction]` These laws do **not** rule out a many-query adaptive (Turing)
reduction, which could route count bits through many derived states; no such
reduction is known, and none was found. We flag this honestly: the barrier
here is a measured structural constraint, not a capacity no-go theorem.

## 4. Answer to the front

- **Negatively, for the question as posed:** the "infinite reachable family
  reachable without direct reduction" is definitionally unavailable. Every
  poset is reachable from the antichain, at exactly `|Cov|` comparisons
  (Lemma 1, verified `n ≤ 6`), with the cover list as a shortest transcript;
  so the reachable state graph adds no descriptive power beyond ordinary
  poset-on-covers input, and any encoding composes to a direct reduction
  (Corollary 3). The #P-hardness of `e` itself *does* transfer to the state
  graph (Theorem 2), but that was never in question — the question asks about
  `F`, and the front's evasion mechanism cannot exist.
- **On the substantive hardness of `F` on reachable states:** remains open,
  identical to the tracked open problem (exact `S(P)` complexity,
  `research-hardness-boundaries.md` §5). The new quantitative constraints
  (L1–L4) narrow where such a proof would have to act: through many-query
  adaptive reduction against a one-ply-Lipschitz, windowed observable.
- **Productive restatement (proposed successor front).** Key the question to
  the description-consistent #P locus, where the descriptions of the
  classical hard class and the state-graph transcripts coincide: *is `F(P)`
  polynomial-time computable for posets given by covers, restricted to
  height ≤ 2?* At `n ≤ 6` the 11 643 height-≤2 states behave no differently
  from the general list under L1–L4. Falsifiers: (a) exhibit a polynomial
  algorithm for `F` on height-2 cover inputs (this would block all
  reductions restricted to the classical hardness locus and would be a
  genuinely new algorithmic result); (b) exhibit a Turing reduction from
  `e(P)` on height-2 cover inputs to polynomially many `F(P̃)` queries on
  reachable states, with each query's transcript length polynomial in the
  instance.

## 5. Verification and provenance

- Probe: `notes/le_count_obstruction_probe.py` (no external libraries;
  same state model as `scripts/state_compression.py`). Run:

      python3 notes/le_count_obstruction_probe.py

  Results: Lemma-1 BFS table above; L1 (`max forced-drop = 1`, 0 moves with
  drop ≥ 2, `n = 5,6`); L2 (`F/log₂e ∈ [1.000, 1.351]`, `n = 5,6`);
  L3/L4 (`e`-spread within one `F`: 20 and 120; `e`-values splitting across
  `F` values: `{8}` at `n = 5`, `{8,13,14,15,16,30,60,120}` at `n = 6`;
  slack histogram `F − ⌈log₂ e⌉ ∈ {0,1}` over all 130 023 states at `n = 6`).
- Model fidelity: isomorphism-invariance of `F` and `e` used throughout;
  states are canonically the set of all labelled posets (`docs/upper-bound.md`
  §States), so the exhaustive `n ≤ 6` search is over the whole
  reachable component.
- Literature: G. Brightwell, P. Winkler, *Counting linear extensions*,
  Order 8(3) (1991) 225–242, doi:10.1007/BF00383444; J. Kahn, N. Saks,
  *Balancing poset extensions*, Order 1 (1984) 113–126 (`3/11`–`8/11`
  balance); J. Cardinal, S. Fiorini, G. Joret, R. M. Jungers, J. I. Munro,
  Combinatorica 33 (2013) 655–697; lineage per
  `docs/research-hardness-boundaries.md` §3.
- Labels: Lemma 1 = paper proof + experiment (all states, n ≤ 6);
  Theorem 2 = literature + deduction; L1 = experiment (conjecture for all n,
  mechanically checked at n ≤ 6 over every state and every move);
  the L2 upper window for all n = literature (Kahn–Saks) + deduction;
  L3, L4 = experiment. No claim is made about #P-hardness of `F` itself;
  that stays open. `SORT-BOUND-U` status is unchanged by this note.

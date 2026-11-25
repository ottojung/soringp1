# lex-prime-excess-unboundedness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

FPYhXIo8eZCcRh8aRQkFTV-stop

## exit_state

clearexit

## question

Is the information excess F(P)-ceil(log2 e(P)) unbounded over all finite module-free (lex-prime) posets P, or does modular decomposability bound the excess of the prime factors?

## basis

Newest board #301 prime-excess-unboundedness (01:56Z) section 8(vi) explicitly notes that the unboundedness construction uses graph-connectivity primeness and a module-free (lex-prime) version is not claimed.

## falsifier

Exhibit an infinite family of module-free posets with excess tending to infinity, or prove a uniform constant bound for every module-free poset.

## implication

Unbounded module-free excess would show the prime-excess barrier does not rely on modular structure; a uniform bound would isolate ordinal-sum and disjoint-union gluings as the only amplification mechanisms.

## finding_unverified

e standard labelled successor-bitmask DP for `e` and memoized minimax for `F` (same model as repo probes) over all transitively closed posets on `n` labelled elements, testing module-freeness by exhaustive module scan:

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

## Other metadata

```json
{
  "finished_at": 1794319622.7925422,
  "started_at": 1794317994.2188885
}
```

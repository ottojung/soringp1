# winning-frontier-space-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MUxeoNW9dxAsuo3g1mOf0P-rectum

## exit_state

clearexit

## question

For all sufficiently large n, does every deterministic RAM algorithm computing the exact S(n) from unary input 1^n require work-tape space Ω(n (log n)^2 / log log n)?

## basis

Winning frontier gives 2^(Ω(n (log n)^2)) pairwise nonisomorphic reachable winning poset states at same depth (docs/research-winning-frontier-barrier.md); no general RAM space lower bound for exact S(n) was found in board/ledger.

## falsifier

Exhibit a deterministic uniform algorithm computing S(n) on 1^n in o(n (log n)^2 / log log n) work-tape space with a correctness proof and explicit cost accounting.

## implication

A nontrivial space lower bound would tighten the known O(n log^2 n) upper bound and clarify whether transcript/state compression can beat the winning frontier.

## finding_unverified

pared labels costs `Θ(log n)` bits each, so an explicit verbatim transcript representation is `Θ(S(n) log n)=Θ(n log^2 n)` bits in the worst/typical case. This is a property of that representation, not a lower bound against all RAM algorithms.
- **Compression/recomputation ideas considered (no theorem).** (i) Storing only a generating relation and recomputing closure is exactly what the transcript DFS already does (it avoids per-frame `n×n` matrices but keeps the path). (ii) Generic path/tree recomputation or pebbling can trade time for space in some settings, but here the algorithm must maintain/answer “is `{x,y}` comparable in `P(σ)`?” and enumerate next incomparable pairs consistently along an adaptive minimax search of depth `Θ(n log n)`; I found no worked-out scheme with an explicit invariant/cost accounting that reduces peak auxiliary space below `o(n (log n)^2 / log log n)` while preserving uniform correctness. (iii) Selective/symbolic evaluation avoids enumerating the winning frontier (consistent with §1) but supplies no proved succinct state representation.
- **Outcome:** **no falsifying algorithm, no correctness proof, and no explicit sub-`n log^2 n / log log n` space accounting obtained.** [open]

### 4. Proof attempt (lower bound) — result: obstructed
- To affirm the front one needs: for all sufficiently large `n`, *every* deterministic RAM algorithm computing `S(n)` on `1^n` uses `Ω(n (log n)^2 / log log n)` work-tape space. I know of no technique establishing such an unconditional uniform space lower bound for this explicit function (which lies in `PSPACE`/polynomial space and is a tally/unary-input function, hence in `P/poly`; see `AGENTS.md`/`docs/problem.md`), and the available combinatorial lower bounds here (information bound on comparisons, winning-frontier state counts) address comparison count or enumeration, not auxiliary RAM workspace. I did **not** obtain a proof or a reduction yielding this bound. [open]

## Honest limits / exact obstruction
- **Mathematical finding:** the claim is **unsupported by its cited evidence** (winning frontier is an enumeration barrier, not a universal RAM-space lower bound) and remains **open/unresolved** here: the recorded uniform upper bound is `O(n log^2 n)` bits while the proposed lower bound is `Ω(n (log n)^2 / log log n)`; neither a proof of that lower bound nor a sub-`o(n log^2 n / log log n)`-space uniform algorithm was found.
- **Concrete failed/blocked approach:** “beat the transcript path” by path-compression/recomputation/pebbling — blocked by the need for an explicit, uniformly correct representation of the current induced partial order (or an equivalent invariant) supporting comparability/enumeration over depth `Θ(n log n)` with proved peak space `o(n log^2 n / log log n)` and accounted recomputation cost; no such construction or accounting was derived. A verbatim `Θ(log n)`-bit-per-comparison transcript gives only the algorithm-specific `Θ(n log^2 n)` figure, which cannot serve as a universal lower bound.
- **Not established:** any new theorem, counterexample, improved bound, or class-separation implication. No Lean/repository changes are warranted. A decisive next step would be either (a) a genuine space-optimized exact evaluator with a full correctness/space proof, or (b) a new lower-bound method targeting auxiliary workspace of comparison-game evaluation (beyond state enumeration and beyond known comparison/information bounds), neither of which is currently in hand.

## Other metadata

```json
{
  "finished_at": 1794489578.1862233,
  "started_at": 1794480416.2736855
}
```

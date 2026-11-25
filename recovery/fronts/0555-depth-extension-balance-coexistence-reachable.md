# depth-extension-balance-coexistence-reachable

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QJpu48BDsMGeKppqIt2von-refined

## exit_state

clearexit

## question

For every n and every poset reachable from the n-antichain along minimax-optimal play, does there exist a single optimal comparison that is simultaneously depth-balanced (easy outcome child of minimax depth at least m-2) and extension-balanced (each outcome child retaining at least 3/11 of the parent's linear extensions), or can the two balance properties only be witnessed by different optimal moves? This asks for the conjunction of the two properties, not either property alone.

## basis

Board #301 depth-balance result (new as of 2026-11-19, checked through n<=10) and Kahn-Saks 1984 3/11 extension balance are each established separately, but their conjunction on optimal-play-reachable states is uninvestigated in the 553-front ledger. A from-scratch exact-minimax plus down-set extension-count probe found coexistence on all reachable states for n<=6 (65551 labelled states, zero failures) while near-half (1/2) coexistence already fails; the all-n status is open and no proof or verification is claimed here.

## falsifier

Exhibit a reachable poset P on which every depth-balanced optimal comparison has an outcome child with fewer than 3/11 of e(P) extensions, or every >=3/11 extension-balanced optimal comparison has an easy child of minimax depth at most m-3; certify by exact minimax and extension counts.

## implication

A uniform coexistence theorem would supply a cheap extension-count-computable move-selection rule that is guaranteed depth-balanced, giving a strong normal form for optimal strategies and a pruning criterion for exact evaluators; a counterexample would separate extension-balance heuristics from depth-balanced minimax play at the antichain root.

## finding_unverified

0**, nhFail 50
   - `n=7`: `S=13`, reachableIso 802, `m`-iso 2045, checked 795, dbFail 0, **coFail 0**, nhFail 337
   - `n=8`: `S=16`, reachableIso 5102, `m`-iso 16999, checked 5094, dbFail 0, **coFail 0**, nhFail 2351
   - `n=9`: `S=19`, reachableIso 33054, `m`-iso 183231, checked 33045, dbFail 0, **coFail 0**, nhFail 16835

3. **`n=10` attempt (incomplete, not a result).** `/tmp/opencode/canon128 10` was killed by SIGKILL before producing output (`/tmp/opencode/c128_10.out` and `.err` are empty, 0-byte). I did **not** obtain an `n=10` coexistence answer in this run.

## Mathematical finding

- **No counterexample found on the full optimal-play-reachable domain through `n<=9`.** In every reachable state checked (`m(P)>=2`), at least one optimal comparison was simultaneously depth-balanced (`easy child >= m-2`) and 3/11 extension-balanced (each child retaining `>= 3/11` of `e(P)`), certified by exact minimax depths and exact extension counts. This extends the ledger’s prior evidence from `n<=6` to `n<=9` (2,749,503 labelled states at `n=7`; 33,045 reachable iso-classes checked at `n=9`).
- **Near-half coexistence is false (concrete separation).** For `n>=3`, many reachable states have no optimal move that is both depth-balanced and `1/2` extension-balanced (`nhFail = 6,48,720,36000,1698480,...,16835` for `n=3..9`), so any all-`n` coexistence statement must exploit the Kahn–Saks margin (`3/11`) rather than near-equipartition. This also confirms 3/11 and near-half are materially different targets on optimal play.
- **Depth-balance:** `dbFail=0` throughout `n<=9`, consistent with (but not an independent reproduction of) the board’s reported `n<=10` depth-balance result.

## Failed approach / exact obstruction (no proof)

- **I did not disprove the all-`n` claim.** No reachable state violating either branch of the stated falsifier was found through `n<=9`.
- **I did not prove the all-`n` claim.** The evidence is finite and computational; `n>=10` is open here (`n=10` run did not complete). A proof would need to bridge a general-poset extension-balance guarantee (Kahn–Saks gives *some* pair, sound but not restricted to optimal moves) with the minimax-optimality/depth-balance constraint on the antichain-root reachable family. That compatibility argument is the exact obstruction: existence of a 3/11-balanced pair and existence of a depth-balanced optimal pair are known/checked separately in relevant ranges, but their **conjunction on a single optimal move** remains unestablished for all `n`.
- **General-poset / certificate caveat.** 3/11 is a sound pairwise-balance fact for posets in general; it is neither a completeness statement for optimal strategies nor, by itself, a certificate that a depth-balanced optimal move exists. The near-half failures show “sound balance” does not automatically lift to the stronger/compatible form.
- **Complexity implication status.** The proposed pruning/normal-form consequence is conditional only: a uniform coexistence theorem would justify selecting a 3/11-balanced move without sacrificing depth-balance, but absent that theorem (and absent a counterexample) no evaluator guarantee follows from this front.

**Bottom line:** exhaustive from-scratch evidence supports coexistence on all optimal-play-reachable states for `n<=9` and decisively separates it from near-half coexistence, but the all-`n` conjunction is **open** (no proof, no counterexample; `n=10` unchecked here). No repository or Lean artifact was created.

## Other metadata

```json
{
  "finished_at": 1795087606.0173335,
  "started_at": 1795086013.9290123
}
```

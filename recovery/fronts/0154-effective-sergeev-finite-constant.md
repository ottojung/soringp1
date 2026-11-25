# effective-sergeev-finite-constant

## status

investigated

## origin

executive_directive

## agent_id

u84KFgCq3JCgaY9dqFyYDL-populism

## exit_state

clearexit

## question

Extract an effective finite version of Sergeev's asymptotic S(n)-C(n)=o(n) to get explicit constants for all sufficiently large n, narrowing the exact search window relevant to S(12)-like obstructions.

## basis

research-plan lists effective finite version of Sergeev bound and explaining n=12 obstruction as open; tied to state-counting and admissible prefixes.

## falsifier

Prove no effective bound exists with constants computable from Sergeev's argument, or derive explicit constants that rule out or explain the n=12 tightness threshold.

## implication

Tightening the effective asymptotic window could constrain search space or explain when information-admissible splits become impossible for exact optimal play.

## finding_unverified

ants remain hidden (envelope-compatible, not constant-explicit)”** and the result validates only surplus *arithmetic*, not any exact-$S(n)$ certificate or a fully specified transition machine. Also leaf-invariance fails under interleaved pending/inserted sets requiring suffix-discipline.
- Single-element granularity gives linear loss (~0.22n) which is worse than surplus - showing granularity/choice of realization matters; the “effective” bound depends on the canonical realization’s constants.

**Falsifier result**
I find no derivation of explicit $(C,N_0)$ from the published argument in-repo. The strongest obstruction is: **the constants in the key intermediate lemma(s) (notably Lemma 2 / the optimization/constants governing group sizes and the interval/container bounds) are not made explicit in the published form used here, so the $O(\cdot)$ with $1/5$ exponent is not effectively computable from the argument as stated without filling those gaps**. This is a gap in explicitness, not a proof that no effective bound exists in principle - but it means the precise “extract an effective finite version” claim is not currently satisfiable from primary sources without rederiving with explicit bookkeeping. The board’s ceiling-loss work is consistent with surplus-compatibility but confirms constants remain hidden.

**Relation to $n=12$ / search window**
- $n=12$ is the first case above info bound ($S(12)=30 > 29$); obstruction is explained by level-emptiness in Wells/Peczarski/Stober–Weiß searches, not by a simple scalar invariant of $e(P)$ alone (efficiency $\equiv$ leaf-count refinement; one-ply $L1>L0$ appears at smaller $n$ like $e=8,n>=5$ witnesses). 
- An eventual effective finite form of $S(n)-C(n)=O(n/(\log n)^{1/5})$ would constrain the *asymptotic* excess, but it does not obviously narrow the finite search window for small fixed $n$ like $12$ - the threshold is a local/adversarial forcing phenomenon, not directly controlled by that global sublinear excess coefficient. The complexity implication (“constrain search space or explain when information-admissible splits become impossible”) is plausible in spirit but not supported by the available effective-constant extraction; the local obstructions (merge families, root-forcing, $L1$) are better placed to explain $n=12$-style tightness.

**Concrete failed approach / obstruction**
- Attempting to read constants off the ECCC PDF via local tools failed (no PDF text extractor available). More directly, repo audit shows the argument’s explicitness is the blocker: without explicit Lemma 2/constants and a fully specified transition machine (including container scheduling/suffix-discipline), “extract an effective finite version with constants computable from Sergeev’s argument” is not currently possible. Any claim of explicit constants would need to fill those gaps; the board’s analysis treats them as missing.

**Limits / honest note**
No new theorem or counterexample was derived here. No Lean/repo changes proposed. The question of whether effective constants are *in principle* extractable vs not is not settled - the obstruction found is “not computable from the published argument as stated” (missing explicit lemmas/machine), not “impossible for all arguments”. Distinction between certificate *soundness* (arithmetic compatible) and *completeness/size/control* remains crucial; tightening asymptotic excess is orthogonal to explaining the small-$n$ tightness threshold like $n=12$ with current evidence.

## Other metadata

```json
{
  "finished_at": 1793544951.5677264,
  "started_at": 1793543965.132608
}
```

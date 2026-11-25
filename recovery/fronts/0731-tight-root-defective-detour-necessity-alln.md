# tight-root-defective-detour-necessity-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

zsAMFmhFsUuLNWjz1rm0Jp-identity

## exit_state

clearexit

## question

The antichain root is information-tight (D(n)=S(n)-ceil(log2 n!)=0) for every n<=11, yet at n=6, also tight, a height-S(6) optimal path passes through a depth-5 state with delta=1 that is later repaired to delta=0. For all sufficiently large tight n, must such defective detours occur on some height-S(n) optimal path, making defect pruning incomplete on the tight regime, or do they occur only finitely often?

## basis

From-scratch n=6 computation gives a depth-5 witness at a tight root (D(6)=0); the n=5 tight root has no reachable repair; exact small-n D values in docs/literature.md; docs/research-budget-pruning.md; AGENTS.md warning that soundness is not completeness.

## falsifier

Show that for all large tight n every height-S(n) tree stays defect-free on all optimal paths, or exhibit infinitely many tight n carrying a defective-then-repaired optimal path with exact e and F computed from scratch.

## implication

If defective detours are unavoidable infinitely often, defect-based pruning cannot be a complete evaluator on tight n and any polynomial-size local defect certificate for S(n)<=k fails there; if they are finite, defect pruning could decide the threshold faster for all large tight n.

## finding_unverified

 It falsifies “every height-`S(6)` optimal path is defect-free” only in the weak sense that *some* optimal path contains a defective node; it does **not** falsify existence of a defect-free height-`S(6)` optimal tree (`g(A_6)=true`). The front’s implication should be read carefully: “defect-based pruning cannot be a complete evaluator on tight n…” is true **if interpreted as pruning every `D>0` state on every search path**; it is false if interpreted as “no defect-free optimal tree exists”.

3. **For all known tight n with exact small-n check here (`n<=8`), `g(A_n)=true`.** [experiment] This gives an explicit defect-free height-`S(n)` optimal certificate for `n=5..8` (and n<=4 trivial). It is consistent with defect pruning being complete *as a certificate language* on these roots, while incomplete as a pathwise heuristic.

4. **No all-n theorem obtained.** I did **not** prove either horn:
   - Not proved: infinitely many tight `n` have a defective-then-repaired optimal path with exact `e,F` from scratch beyond the small-n evidence (I only have `n=6,7` exact pathwise evidence; `n=7` has defective admissible states, trivially repaired at leaves).
   - Not proved: for all large tight `n`, every height-`S(n)` tree stays defect-free on all optimal paths. This would actually be stronger than needed and is false in spirit already at `n=6`; the meaningful strong form is “every height-`S(n)` *optimal tree* has some defective node” or its negation “some height-`S(n)` tree is defect-free”.
   - Not proved: existence/nonexistence of defect-free optimal trees for large tight `n`, which is equivalent to the `S(n)=ceil(log2 n!)` asymptotic tightness question only under the unproved completeness conjecture `C: F=L => g`.

## Concrete failed approach / exact obstruction

- **Failed/blocked as a proof route:** use the `g` necessary-condition/induction to get all-n completeness or infinitude. The accepted 14:19Z theorem gives only a necessary condition (`e(P) > 3*2^(L-2)` forces `g` for defect-free `P`); the dangerous region `e(P) <= 3*2^(L-2)` remains open. A counterexample to completeness would need a defect-free `P` with no balanced defect-free pair and `L>=5`.
- **Exact obstruction:** the front conflates two different properties: (a) pathwise presence of defective-but-feasible states, and (b) nonexistence of any fully defect-free height-`S(n)` optimal tree. (a) is easy locally and already occurs at `n=6,7`; (b) is the hard completeness/tightness question. Moreover “all sufficiently large tight n” is unstable as a domain because infinitude of tight `n` (`S(n)=ceil(log2 n!)`) is itself open; known exact tight set through the literature cited in-repo is `n<=11,20,21` in small ranges, but asymptotic status is open.
- **Computational limit:** exact `F` exhaustive over all labelled posets becomes expensive past `n=7/8` in this scratch implementation; `g(A_9)` was killed (SIGKILL) in the quick run, so I do not claim `n=9`.

## Bottom line

**No new all-n theorem or counterexample.** The precise defensible result is: from-scratch computation confirms the `n=6` defective-but-feasible detour and shows defective-but-feasible admissible states also occur at tight `n=7`, while `g(A_n)` holds for `n<=8`, so defect pruning is sound but pathwise incomplete; however the front’s infinite/finitary dichotomy remains open because it hinges on the unproved completeness of the defect-free certificate (`F=L => g`) and/or the open asymptotic tightness of `S(n)=ceil(log2 n!)`.

## Other metadata

```json
{
  "finished_at": 1795464941.3270562,
  "started_at": 1795463492.1680405
}
```

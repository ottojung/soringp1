# root-tight-all-tight-tree-existence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

HTCtl2nt1Zb6wmnUt2snQC-killed

## exit_state

clearexit

## question

For every integer n>=1 with S(n)=ceil(log2 n!), does some height-S(n) optimal comparison tree have ceil(log2 e(P))=S(n)-depth(P) for every node P on some root-to-leaf path? This asks whether root information-tightness is realizable by an all-tight optimal strategy branch for all root-tight n.

## basis

Digest n8-alltight-resolution gives YES for n=8; information-tight-infinite-family and n12 notes document root/internal tightness cases but not this all-n branch property.

## falsifier

Exhibit any root-tight n (certified S(n)=ceil(log2 n!)) such that every optimal height-S(n) tree contains some non-tight node on every root-to-leaf path, with a verified optimality argument.

## implication

A positive all-n result would show root-tight cases admit uniformly tight optimal branches (useful for succinct strategies); a counterexample would expose forced internal slack even at root tightness, constraining tightness heuristics.

## finding_unverified

posets P reached inside trees. This is a real obstruction to easy “always-greedy-info-tight” proofs, but it does **not** prove impossibility for some optimal path in some optimal tree for root-tight n.

## Concrete failed approach / obstruction (honest)
- **Attempted line (reasoned, not a proof):** test the chain “root-tight => first step tight (done) => is there always some incomparable comparison giving `ceil(log2 e_child)==ceil(log2 e_P)-1` at every subsequent node on some branch of some optimal tree?” The obstruction is combinatorial balance: no general theorem from cited material guarantees a half-like information drop after the first move for arbitrary reachable posets; Kahn–Saks is 1/3–2/3. However, “no guaranteed move” is different from “no optimal tree achieves it along some path.” I did not construct a poset instance forced into unavoidable `ceil(log2 e)` slack on *all* optimal continuations for any certified root-tight n>3.
- **What I did not do (and would be needed for a real disproof):** produce a specific root-tight n (with a verified `S(n)=C(n)` certificate/argument in hand) and a verified proof that for every optimal height-`S(n)` decision tree there is no root-to-leaf path with `ceil(log2 e(P))==S(n)-depth(P)` for all P. I found no such example in the inspected notes and did not run an exhaustive optimal-tree search to manufacture one.
- **What I did not do (and would be needed for a real proof):** give a general argument (or a counterfamily analysis) that such an all-tight path always exists for all root-tight n.

## Assessment of the FRONT claim (no proof claimed)
- The claim is a sharp, falsifiable combinatorial property of optimal comparison strategies restricted to root-tight instances. From available evidence: plausible in small cases (n=3 explicit YES; prompt reports n=8 YES), but **unresolved** in general. I found no counterexample in the repository material I reviewed and no proof. The strongest concrete obstruction I can state cleanly is the balance gap (1/3–2/3 vs needed half/info-drop conditions in general) plus the existence of locally slack nodes elsewhere in the poset space—neither converts to a theorem that every optimal tree is forced to have slack on every root-to-leaf path for some root-tight n.
- **Complexity implication (as stated, restated carefully):** if true for all root-tight n, it means root-tight cases admit some optimal strategy that is information-tight along some branch throughout (a structural property potentially useful for designing/certifying succinct strategies along that branch); if false, some root-tight n forces internal information slack on every complete path of every optimal tree, constraining “always stay info-tight” heuristics. Either outcome is a structural fact about `S(n)` strategies (not by itself a complexity-class separation of `SORT-BOUND-U` beyond known barriers noted in `docs/problem.md`).

## Honest bottom line
- **No counterexample found. No proof found.** The only fully worked small witness I constructed/check-argued here is **n=3: YES** (all-tight root-to-leaf path exists in an optimal tree). I did not verify the prompted “n=8 YES” digest from files. The FRONT remains open given the evidence I inspected; any claimed resolution would require either (a) an explicit root-tight n with a verified optimality proof and a verified argument that no optimal height-`C(n)` tree contains any all-tight root-to-leaf path, or (b) a general proof of existence for all root-tight n.

## Other metadata

```json
{
  "finished_at": 1794982735.3888197,
  "started_at": 1794982344.7971137
}
```

# sorter-refuter-duality-np-conp

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mBCsKC6yOkFIfA3FP3kbvi-lips

## exit_state

clearexit

## question

Is there an all-n duality between succinct sound-and-complete sorter certificates for SORT-BOUND-U and succinct adversary refuter certificates for its complement, or can NP-style certificate soundness and coNP-style refutation be decoupled for this sparse tally language?

## basis

docs/research-strategy-certificates.md Remark 1.3 separates soundness from certificate existence and notes coNP needs separate refuters; board #301 (2026-11-19 09:54Z) records a VERIFY-ADV coNP circularity obstruction without any proof or disproof.

## falsifier

Construct a polynomial-size sound and complete sorter certificate family for all n whose complement admits no polynomial-size checkable refuters under a standard assumption, or prove a two-way duality theorem.

## implication

Resolves whether NP and coNP membership for exact unary sorting numbers can be studied independently; a decoupling would explain the absent succinct refuter and guide the search for certificates strictly below PSPACE.

## finding_unverified

 duality finding hasn't already been posted (avoid duplicates), then I'll write the report.
Worktree is clean, on `billy-dev` at `6a96398`, and no duplicate post exists. Let me compose the report and post it to board #301.
The post succeeded (id `sha256:sah5qi3W…`, 17:22:59Z). Let me do a final cleanliness check.
Done. I studied the contract, `problem.md`, the certificates/parallel-duality notes, the primary literature baseline, and board #301 (including the full 09:54Z `adversary-coNP-cert-front` report), then attacked the front's claim and tried to disprove it. I posted one finding to #301 (id `sha256:sah5qi3W…`, 17:22:59Z) and made **no repository, Lean, test, workflow, or ledger changes** — worktree remains clean at `billy-dev`/`6a96398`.

## What I found

I separated three levels the FRONT wording conflates, and the honest verdict is an **exact obstruction**, not a proof of either side:

- **Game level (proved duality, no certificates).** Positional determinacy of `G(n,k)` gives memoryless winning strategies for both players; a refuter winning at `S(n)−1` determines `S(n)` by binary search (the 09:54Z circularity, credited not re-claimed).

- **Certificate-format level (proved asymmetry — the substantive result).** Two all‑n, paper-checkable theorems:
  - **B1:** For every `n≥2` the smallest explicit single-policy sorter DAG has exactly `2n!−1` nodes (n! distinct permutation-leaves + hash-consing saves nothing because distinct reachable nodes carry distinct labelled posets). So the sound verifier has *unconditional soundness* but **no poly-size complete witness family in this format** — a rigorous decoupling of soundness from completeness, and proof that any NP witness (if one exists) cannot be an explicit sorter DAG.
  - **B2:** `VERIFY-SORT` (explicit DAG) is in **P** (DP over listed states), while `VERIFY-ADV` (adversary circuit) is in **coNP** (complement has an ≤k sorter-path witness) and not known in P. The source is a quantifier-*order* difference: ∃ over listed states vs ∀ over sorter plays. This is a provable structural explanation of the absent succinct refuter — a verification blow-up, **not** an impossibility theorem.
  
  Net: sorter side = soundness cheap, completeness provably fails for the natural format; refuter side = no size obstruction known, but even soundness is coNP, not P.

- **Class level (blocked).** NP⟺coNP duality would need a collapse not known for tally sets; decoupling (one class without the other) would imply `NP≠coNP` or `coNP≠PSPACE` — open separations. So neither the FALSIFIER's decoupling nor a duality theorem is provable with current techniques.

## Serious disproof attempts that failed
(1) class-level decoupling needs `∈NP ∧ ∉coNP` (open on both); (2) tally-set collapse route — Mahaney runs the wrong direction, no "tally NP ⇒ coNP" theorem; (3) circuit-counting lower bound on `c_adv` — poly circuits index exponentially many states; (4) coNP-hardness of VERIFY-ADV — only sketched, constrained transitions block naive reductions; (5) general-poset hardness transfer (Hyafil–Rivest, Laber–Nogueira, Parberry) — wrong model, Claim D + Mahaney.

## Honest limits
No theorem completion for `S(n)`/`SORT-BOUND-U`, no class separation, no algorithm or value; `S(23)` untouched. The only proved "duality" is game-theoretic, and the only proved "decoupling" is at the certificate-format/soundness level — I did **not** resolve the class-level question, and I explicitly did not mistake process success for a proof.

## Other metadata

```json
{
  "finished_at": 1795109043.0548215,
  "started_at": 1795108716.0057845
}
```

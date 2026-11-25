# am-succinct-certificate-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

0raVIrTFHqWoDLvscflafo-past

## exit_state

clearexit

## question

Is the unary threshold language SORT-BOUND-U = {1^n#1^k : S(n) <= k} in AM, i.e. does the minimax game for the exact sorting number admit a constant-round public-coin interactive proof with a polynomial-time verifier measured in the unary input length N = n+k+1?

## basis

IP=PSPACE (Shamir) and AM=IP[O(1)] make constant-round protocols the natural sub-PSPACE target; problem.md lists 'another class below PSPACE via a succinct checkable certificate' as active, and the sparse/Mahaney barrier plus minimax correspondence S_eq_adv_univ are established in docs.

## falsifier

Falsify the positive hypothesis by proving an AM-hardness/sparsity barrier for SORT-BOUND-U (a sparse AM-hard set would collapse PH), or by a communication-style lower bound showing no constant-round protocol can certify the adversary value F(P) within poly(N) time.

## implication

An AM protocol would be a genuinely new randomized succinct certificate placing exact unary S evaluation into Sigma_2^P, the probabilistic analogue of the open NP/coNP certificate question; a barrier would delimit all constant-round certificate routes.

## finding_unverified

.md`, no commits/stash.
- Board #301 showed this front created 23:38Z with **no result posted by it** as of the 23:53Z continuity note. I posted exactly **one** report (23:58:59Z, author `SoringP1 frontier: am-succinct-certificate-sortbound`). Worktree left clean.

## Mathematical finding — no proof, no counterexample
I attacked the all‑n question "is `SORT-BOUND-U ∈ AM`?" seriously in both directions and could prove neither membership nor non‑membership. What I did establish is a precise map of why both named falsifier routes are closed and why the natural protocol fails:

- **D1 — sparse‑AM‑hardness falsifier is self‑defeating.** The language is sparse and `NP ⊆ AM`, so AM‑hardness ⇒ NP‑hardness ⇒ (Mahaney) `P=NP`. Under `P≠NP` no sparse set is AM‑hard, so AM‑hardness cannot refute membership without resolving P vs NP.
- **D2 — what AM would really give.** Using `AM[k]=AM[2]`, `AM=BP·NP` and perfect completeness, membership yields a *uniform, complete* poly‑size witness family accepted for all coin strings (`AM ⊆ Σ₂∩Π₂`, `AM ⊆ NP/poly`). The repo's framed‑DAG checkers give only **soundness**; **completeness** is open. So an AM protocol would settle the open completeness half of the succinct‑certificate problem — not a routine checker upgrade.
- **D3 — communication lower bounds are vacuous.** A tally language has ~1 bit of answer per length, so poly‑bit messages dwarf `log(#answers)`; any lower bound must be computational (`∉ AM/Σ₂`), for which no method exists for a natural tally PSPACE set (and `PH≠PSPACE` wouldn't even imply it).
- **D4 — natural ranking + random‑path protocol is unsound.** Worst‑case depth is a *max*, not an average; a certificate valid except on a measure‑`2^{-d}` leaf set fools any `poly(d)`‑sample path checker w.h.p. Honest caveat: this rules out the protocol family for arbitrary games, not a proof that the sorting game has such needles at `n≥12` (infeasible to test here).

**Blocking obstacle:** no complete polynomial‑size succinct witness for yes‑instances is known, and randomness cannot replace completeness because worst‑case depth is a maximum. I made no repository or Lean changes.
Recovery check-in. Let me re-verify the durable state before acting further, since the last turn's external effect (the board post) must not be duplicated.
State re-verified — no duplication occurred, nothing left unfinished:

- **Git**: clean working tree, single commit `HEAD=6a96398` on branch `billy-dev`, zero stashes.
- **Board #301**: exactly **one** post from this front (`am-succinct-certificate-sortbound`, 23:58:59Z) and the prior Executive continuity note (23:53:19Z). No duplicates, no partial/ambiguous post.
- **No new side effects**: no commits, no Lean/repo changes, no purchases or external actions.

**Conclusion:** The last turn's effects are fully consistent and complete — the report was posted once, nothing is pending, and the recovery interruption caused no double-execution.

The outstanding deliverable state is:
- **Finding delivered:** `SORT-BOUND-U ∈ AM` was attacked seriously in both directions; neither membership nor non‑membership was proved. Both falsifier routes were closed (sparse‑AM‑hardness ⇒ `P=NP`; communication bounds are vacuous on a tally set; ranking+random‑path protocols unsound because worst‑case depth is a max, not an average). Honest limits recorded; no Lean or repository changes made.

There is **no unfinished work** from my side at this point, and I will **not** re-post or re-commit anything.

## Other metadata

```json
{
  "finished_at": 1794959985.8531284,
  "started_at": 1794958715.434362
}
```

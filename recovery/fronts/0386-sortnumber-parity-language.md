# sortnumber-parity-language

## status

investigated

## origin

ai_proposal_unverified

## agent_id

tgVibE1rzgYdyWvN6dQFnW-mycetoma

## exit_state

clearexit

## question

Is the unary decision language PARITY = { 1^n : S(n) is even } decidable by a uniform polynomial-time algorithm, or is it Turing-equivalent to SORT-BOUND-U, so that even the single parity bit of S(n) encodes the full exact-evaluation difficulty?

## basis

Board #301 front s-residue-automaticity leaves p-automaticity open, but P-membership is a strictly weaker question for a tally language; exact S(1..22) give parity 0 on 10..21 and 1 at n=22, so no short periodic prefix is known.

## falsifier

A uniform polynomial-time decider for PARITY on all unary inputs, or a polynomial-time Turing reduction from SORT-BOUND-U (equivalently S_unary) to PARITY; either outcome settles the stated dichotomy.

## implication

If PARITY is in P, it is a uniform upper bound strictly below the exact unary sorting number and shows the exact value is not needed for parity; if PARITY is Turing-equivalent to SORT-BOUND-U, the downward-closure barrier extends to one residue bit.

## finding_unverified

al adversary must answer extra-key comparisons without knowing \(\sigma\), and can split the consistent set across different \(\sigma\)’s, sacrificing the true \(\sigma\)’s rank set. The per-\(\sigma\) bound is only an average over \(\sigma\), not a worst-case path, so no height-\((h-\lceil\log_2 n\rceil)\) tree for \(n-1\) is assembled. This is the exact gap.

D is a genuine all-\(n\) claim about the antichain root, not a general-poset monotonicity statement; local poset gaps do not transfer, and a sound certificate for one poset is not a completeness theorem for \(S(n)\).

## Honest limits

- \(\mathrm{PARITY}\) is a tally language in \(\mathrm{PSPACE}\), hence in \(\mathrm{P/poly}\). \(\mathrm{PARITY}\notin\mathrm{P}\) would imply \(\mathrm{P}\ne\mathrm{PSPACE}\), so no unconditional separation is reachable here.
- \(\mathrm{SORT\text{-}BOUND\text{-}U}\le_T\mathrm{PARITY}\) together with \(\mathrm{PARITY}\in\mathrm{P}\) would itself imply \(\mathrm{SORT\text{-}BOUND\text{-}U}\in\mathrm{P}\); the front’s “two horns” are not independent alternatives.
- I did not prove or disprove D, did not find a counterexample to it, and did not establish either horn. The contribution is the sufficient equivalence theorem, the verified range \(n\le24\), the first failing pair at \(n=25\), and the parity-identical envelope counterexample.

Board #301 was updated with these findings and a precision correction that D is sufficient, not shown necessary. No repository or Lean changes were made; the worktree remains clean at `6a96398`.
## Recovery audit

I inspected the existing conversation, the worktree, Git, board #301, and the frontier ledger before acting.

**Effects that had already happened**
- The previous turn had posted the main `sortnumber-parity-language` finding to board #301 and one precision correction about D being sufficient rather than necessary.
- A Viche Executive verification followed, confirming the conditional equivalence and the `f1/f2` barrier, but identifying a **non sequitur** in §2: from `S(23)=75`, the insertion bound excludes `S(24)=81` but allows `S(24)=80` with increment `5`; hence `S(23)=76` does not follow.
- No repository changes: `git status` is clean at `6a96398` on `billy-dev`.
- The frontier ledger still shows `status: running`, `exit_state: None`, which is the expected active-agent state.

**Unfinished work completed once**
- I posted exactly one new board correction fixing §2. The correct case check is:
  - `S(23)=75` gives `(S(24),d)=(80,5)`;
  - `S(23)=76` gives `(80,4)` or `(81,5)`.
  
  All increments are in `{⌊log₂ 24⌋,⌈log₂ 24⌉}`, so **D at `n=24` still holds and the verified range `n≤24` is unchanged**. The first-failure pair `(S(24),S(25))=(81,84)` and the parity-identical `f1/f2` barrier are unaffected.
- I did not duplicate the main post, the precision correction, or any commit.

**Mathematical status**
- Conditional theorem stands: the increment dichotomy D implies `S_unary ∈ FP^PARITY`, hence `PARITY ∈ P ⇔ S_unary ∈ FP` under D.
- D is verified for `n≤24` (with the corrected `n=24` argument); the first possible failure remains `(S(24),S(25))=(81,84)`.
- The envelope counterexample still shows that the published bounds plus the parity oracle cannot determine `S(25)`; a proof of the second horn needs a new arithmetic fact.
- No unconditional decider or equivalence was proved; `PARITY` remains a tally language in PSPACE/P/poly, so unconditional separation is out of reach.

No repo or Lean changes were made.

## Other metadata

```json
{
  "finished_at": 1794161729.7272546,
  "started_at": 1794160632.54449
}
```

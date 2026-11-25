# min-forced-inversions-tally-equivalence-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1MffppMUeDOI8Fw0P2OUlX-abbott

## exit_state

clearexit

## question

For each n let nu(n) be the minimum, over all height-S(n) sorting strategies on the n-antichain, of the worst-case number of sibling-extension-inverted optimal comparisons along any adversary path. For all n, is nu(n)=0 exactly on the information-tight sizes S(n)=ceil(log2 n!), and is computing nu(n) polynomial-time Turing-equivalent to computing the exact sorting number S(n)?

## basis

Newest #301 05:30Z (tight states inversion-free) and 05:54Z (an inversion forces slack>=1 and m>=5) imply by deduction that nu(n)=0 whenever S(n)=ceil(log2 n!). Independent scratch enumeration (experiment) found inversions first at n=6 (1440 labelled posets) but zero all-inverted posets through n=6; the converse and the equivalence are not established.

## falsifier

Settle either horn: exhibit a tight n with nu(n)>0 or a non-tight n with nu(n)=0; or separate the tally functions by giving a polynomial-time algorithm for one but not the other, or by establishing only one direction of polynomial-time Turing reducibility between them.

## implication

nu(n)=0 on tight n would upgrade tight-state inversion-freeness to a whole-path normal form and a new sound pruning parameter; a polynomial-time Turing equivalence would show that even this coarse inversion statistic encodes the full difficulty of exact unary S(n) evaluation.

## finding_unverified

lize the structural theorem cleanly and check the reducibility question from the literature side.
While n=10 runs, let me make the n=9 witness fully independent-checkable by decoding the poset and verifying the exact numbers from first principles.
The witness is verified from first principles. Let me check its budget/reachability status and extract a genuinely on-budget witness from the BFS data.
Let me check the exact posting command syntax used previously, then prepare the single board update once the n=10 job reports (or now, if it's too slow).
The n=10 minimax job is still grinding (11 min, 1.3 GB, no output). I'll give it a short final window while drafting the board report; if it doesn't report, I'll stop it and record it honestly as an incomplete attempt.
Post returned success. Let me verify exactly one comment landed and no duplicate was created.
## Report

**Recovery first.** On `billy-dev` the worktree was clean at `6a96398` (reflog = clone only), my front's ledger entry was `running`/no finding, and board searches for `min-forced-inversions`, `nu(n)`, `sibling-extension-inverted`, `tally-equivalence` all returned 0 — so the interrupted turn left **no side effects** from my front. The `perpath_*` scratch belongs to sibling fronts. I made **exactly one** #301 post (07:01:45Z), verified by digest; no commits, Lean, tests, or repo changes.

### Mathematical finding — the EVIDENCE's "deduction" has a real gap

Let σ(P)=m(P)−⌈log₂ e(P)⌉ and δ(P)=S(n)−d−m(P) (budget slack). The two board results (tight states inversion-free; inversion ⇒ σ≥1, m≥5) are **local soundness** facts about σ=0 states. They do **not** imply ν(n)=0 on tight n, because σ=0 is not preserved along δ=0 optimal play: an optimal **tie** with unequal child extension counts creates a δ=0 child with σ=1, where inversions are permitted.

Concrete, first-principles-rechecked witness (n=9): poset with relations 4<5, 4<6, 5<7, 6<8 plus four isolated elements; e=18144, m=15, σ=0, only 4 covers so δ=0 (S(9)=19). At optimal tie (0,5) the children have e=10080 and 8064 (both m=14), so the smaller child has σ=1 at δ=0. Exhaustive δ=0 BFS from A₉: 33,054 reachable states, 8,062 with σ≥1.

**Clean conditional [paper proof]:** if Claim C holds at size n, then ν(n)=0 — play a non-inverted optimal comparison at every state (states with m≤1 are inversion-free by 05:54Z); optimal moves keep height S(n). Hence ν(9)=0, and a positive ν(n) for any non-tight n requires a reachable all-inverted state at δ=0. No all-inverted poset is known at **any** n, so the converse horn has no evidence.

### Complexity horn — exact obstruction, not a separation

The Turing-equivalence claim is a conjecture, not a deduction:
- no route to ν ≤_T S is known (S gives only antichain values, not subposet minimax; the task reduces to the open all-inversion reachability);
- S ≤_T ν would, if Claim C held for all n (ν≡0 ∈ FP), imply S ∈ FP — open for this tally sequence; an unconditional separation is unavailable for natural PSPACE tally languages;
- soundness-only facts (#P-hard e, minimax identification) do not transfer to completeness here.

### Failed attempt and limits

I attempted the decisive n=10 (tight) δ=0 BFS for reachable all-inverted states; after ~11 min it produced no output (Python, ~2.5M classes, 1.3 GB), so I stopped it and make **no n=10 claim**. Neither horn was settled, no falsifier exhibited, no new bound for S(n)/SORT-BOUND-U, no Claim C progress, and no repository changes were warranted.

## Other metadata

```json
{
  "finished_at": 1795330923.559173,
  "started_at": 1795328903.0912812
}
```

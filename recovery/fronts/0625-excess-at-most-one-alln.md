# excess-at-most-one-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sGoK59sp29C76nsT95SMt0-tiresome

## exit_state

clearexit

## question

Is e(n) <= 1 for all n >= 2 (equivalently, does the information-bound excess S(n) - ceil(log2 n!) never exceed one)?

## basis

A036604 (S(n), n=1..22): 0,1,3,5,7,10,13,16,19,22,26,30,34,38,42,46,50,54,58,62,66,71. A003070 (ceil log2 n!): 0,0,1,3,5,7,10,13,16,19,22,26,29,33,37,41,45,49,53,57,62,66,70. Direct computation of e(n)=S(n)-C(n) on n=2..22: e=0 on {2..11,20,21} and e=1 on {12..19,22}; the maximum excess is 1, so no falsifier on the checked range; S(23) is open per ledger exec-s23-search-window-20261121 (OEIS ext lists 75/76 for S(23), C(23)=75). Ledger adjacent fronts (excess-boundedness-alln, excess-constant-bounded-alln) prove or discuss other excess quantities; this front asks the at-most-one bound on the antichain-root excess itself. Honest limit: the falsifier is unverified beyond n=22 since S(23) is open; a computer-assisted minimax enumeration over n in [23, 30] is the natural next step, and the known values found no contrary excess pattern.

## falsifier

Exhibit n with S(n) - ceil(log2 n!) >= 2; a concrete optimal-tree height S(n) at least two above the counting bound is the falsifier, in any n >= 2.

## implication

If the bound e(n) <= 1 holds for all n, then the antichain-root minimax value m(A_n) = S(n) stays within one comparison of the counting lower bound C(n) for every n, the largest gap is the n=12 excess of 1, and the excess slack of the minimax game is structurally capped; if e(n) >= 2 occurs infinitely often, the information bound is not a tight cap and the antichain game is genuinely harder than counting.

## finding_unverified

/lookahead family certifies C+2 at the root.
4. **General-poset → root transfer**: excesses F(P) − ⌈log₂ e(P)⌉ are large/unbounded on some posets (ordinal-sum families etc.), but local gaps on reachable posets do not certify the antichain root; conversely certificate *soundness* (local L0/L1 rules, valid witness rules) is not *completeness* for the global predicate S(n) ≤ k — so sound local objects are not falsifiers of the all-n claim either.

**Credible windows for a certified falsifier**: n = 25 (S(25) = 86 since 84 ≤ S ≤ 86) and n = 47 (S(47) ∈ {198,199,200}; S(47) = 200 or 201 would be the first).

## Honest limits

- S(23) is open per the ledger (exec-s23-search-window-20261121): 75/76, so e(23) ∈ {0,1} — not a falsifier.
- S(25) is uncertified; FJ(25)=86=C+2 is only an upper-bound window.
- User-suggested next step: a computer-assisted minimax enumeration over n ∈ [23, 30] — but reproducing S(23) is a flagship search, and even with S(23)=76 the front stands (e ≤ 1).

**Conclusion**: the claim is unrefuted; it is consistent with all certified data (max excess 1, plus S(28) ≥ C+1). No Lean or repository changes were made (no new independently checkable theorem or counterexample). This front also duplicates the investigated adjacent front `single-bit-excess-dichotomy`, which found the same obstruction class.
Recovery inspection results:

- **Git state**: worktree clean at `6a96398`; no commits, no modified/tracked files, no untracked files. No repository or Lean changes were made.
- **Board #301 (live)**: the finding post from 2026-11-21T02:51:10.661Z by `SoringP1 frontier: excess-at-most-one-alln` exists and is **single** (the most recent item; not duplicated). The earlier local `/tmp/opencode/board/` cache simply predates the post, which is why it shows 0 matches.
- **Ledger**: `excess-at-most-one-alln` is still `running` with `exit_state=None` — expected while the agent is active; the keeper owns the `running → investigated/blocked` transition on exit. I did not edit the ledger.
- **Scratch only**: all computations (e-table, FJ−C arithmetic) and literature reads were under `/tmp/opencode/`; nothing was written to the repo.

**Unfinished work**: none. The deliverable (a board report of the mathematical finding, failed disproof attempts, and exact obstruction) was posted once and verified. I am not repeating the post, not editing the ledger, and not creating repository changes.

**Summary of the finding reported** (full text is on #301):
- Claim: e(n) = S(n) − ⌈log₂ n!⌉ ≤ 1 for all n ≥ 2.
- Verified data (OEIS A036604/A003070 + literature): e = 0 on {2..11, 20, 21}; e = 1 on {12..19, 22}; e(23) ∈ {0,1}; e(24) ≤ 1 by deduction (FJ(24)=81=C(24)+1); FJ−C first reaches 2 at n=25, 3 at 28/46–47.
- No falsifier: no certified S(n) ≥ C(n)+2 exists (max certified excess = 1; S(28) ≥ 99 = C+1). FJ(25)=86=C+2 is an upper-bound window only (S(25) ∈ {84,85,86}).
- Exact obstruction: a counterexample needs a certified lower bound above C(n); general-poset excesses do not transfer to the antichain root; standard counting families cap the root at C(n) (flatness L_t(A_n)=C(n) for t≤n/2); sound local certificates are not complete for S(n) ≤ k.
- Honest limits: S(23) open (75/76); S(25) uncertified; next step is the user-suggested computer-assisted minimax over n ∈ [23, 30], which would not by itself produce a falsifier.
- Duplicates the investigated adjacent front `single-bit-excess-dichotomy`; no Lean/repo change (no new theorem or counterexample).

## Other metadata

```json
{
  "finished_at": 1795229565.3267117,
  "started_at": 1795228508.486596
}
```

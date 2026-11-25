# critical-optimal-tree-parity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4oIt8XQE7IuxBoJD7I4kje-impulsive

## exit_state

clearexit

## question

For unary n, let N(n) be the number of distinct height-S(n) deterministic adaptive comparison decision trees that correctly sort all n labelled keys (counted up to a fixed labelled-tree equivalence). Is the parity of N(n), or N(n) mod any fixed prime, computable in polynomial time in n, or is every such fixed modular residue of the critical-tree count as hard to compute as S(n) itself? This is about the count of optimal sorters, not the parity of the value S(n).

## basis

docs/problem.md: SORT-BOUND-U is in PSPACE, is tally/P/poly, and NP membership is open. Board #301 16:48Z/18:16Z show critical tight sorters are rare and generated only by a small grammar, motivating a count of them. From-scratch enumeration here gave S(n)=1,3,5,7 and N(n)=1,12,42336,2418647040 (parity 1,0,0,0) for n=2..5; these are finite experiments, not a proof. The 618 ledger fronts and 22 previous contain no counting-of-optimal-trees front; sortnumber-parity-language concerns the parity of the value S(n), a distinct object. Trees are at the antichain root, so no general-poset transfer is claimed.

## falsifier

Settle it either way: exhibit a uniform polynomial-time algorithm computing N(n) mod 2 (or mod a fixed prime) for all n from unary n, or prove that computing any fixed modular residue of N(n) is Turing-equivalent to, or admits no polynomial-time algorithm short of, exact evaluation of S(n).

## implication

A fast modular-residue algorithm would be a new upper bound on a tally function derived from the optimal-sorter space and could seed a compact arithmetic/nondeterministic route toward the open NP-membership question for SORT-BOUND-U; an equivalence or hardness result would show that even coarse arithmetic of the optimal-tree space encodes the full exact-evaluation difficulty, without implying a class separation.

## finding_unverified

ers, but that does not establish completeness for all optimal trees or compute their count. Results about arbitrary posets likewise do not transfer to this fixed antichain-root count.

The reported values for `n=2..5` are finite experiments; their residues establish no all-`n` pattern. The primary sorting literature I checked, including Stober–Weiß’s exhaustive search for exact sorting numbers, concerns determining minima, not the number of optimal labelled decision trees or its modular complexity. I found no basis there for either side of the proposed claim.

**Exact obstruction:** the count’s definition must be fixed, and a complete all-`n` characterization of its optimal root branches is missing. Neither a polynomial-time residue algorithm nor a reduction from exact `S(n)` to a fixed modular residue has been established.
I'll inspect the current state carefully before taking any action. Let me check Git state, working directory, scratch files, and the board in parallel.
Git working tree is clean and I'm on `billy-dev`. Now let me check the board and durable ledger for any side effects from my previous turn, plus any front-specific scratch files.
Let me do a final thorough check for any board post from my previous turn and any files touched during its time window, to rule out uncertain effects.
Investigation complete. Here is what I determined; I took **no new actions** (no board post, no commit, no ledger/git change).

## What I inspected
- Conversation: my previous turn ended with a complete finding — *unresolved, no theorem/counterexample, honest limits* — and explicitly stated no side effects.
- Working directory + Git: `billy-dev`, HEAD `6a96398`, clean working tree (`git diff`/`git diff --cached` empty), reflog shows only the initial clone — no commits by me.
- Durable records: frontier ledger front `critical-optimal-tree-parity` = `running` (the keeper's launch state; not mutated by me).
- Board #301: searched for all distinctive phrases from my previous turn (`optimal-tree-parity`, `modular residue`, `exact obstruction`, `positive by definition`, `no new theorem or counterexample`). Zero matches attributable to my front. The only `no new theorem`/`modular` hits are other agents' posts (20:05Z Viche Executive, 14:44Z Viche Executive).

## Effects that actually happened from my previous turn
**None.** No git changes, no board post, no ledger mutation, no scratch files of mine. (Recent mtimes on repo files are from the 20:23 clone/checkout, not content edits. `/tmp/opencode/curator_probe/count_trees.py` belongs to the separate curator agent, not this front.)

## Unfinished work
The research task itself concluded in my previous turn with an inconclusive negative result. The only arguably-pending item per `AGENTS.md` §4 is a concise board report of that negative/inconclusive outcome — which my previous turn deliberately did **not** post.

Given the recovery instruction to never duplicate external actions and to "report it for review rather than guessing," I did **not** post it now. Posting a negative result is a judgment call the contract treats as optional ("post only when something changed"), and I won't guess under recovery conditions.

**For your review:** do you want me to post a single concise inconclusive-outcome note to board #301 for this front? If so I will post exactly one; otherwise I will leave the board untouched. The front remains `running` in the ledger, which is the keeper/executive's disposition to make, not mine.

## Other metadata

```json
{
  "finished_at": 1795206312.8832486,
  "started_at": 1795206179.1087165
}
```

# antonina-oqBsBjkOSjz00Gypk67jC3-fossil

Session: ses_e53356044ffeOfLBO4n6SxCotV
Workspace: /home/lubko/soring-fronts/root-sublinear-amplification-20261105
Created: 1793900322750; updated: 1793900402671

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 111 (msg_1accb5057001ETWzlhFIobExKV)

## Result

**The requested all-\(n\) sublinear root gap is not established by the notes’ gadget arguments.** I found a precise failure in the tempting block-amplification step: **the root lower bound \(S(n)\ge C(n)+\sum_i\delta_i\) does not follow from local gaps, even when the poset blocks have additive sorting cost.** The available results do establish unbounded local gaps, but they do not supply the required \(\forall\) sorter / \(\exists\) adversary strategy from the initial antichain. I have not proved that *every possible* genuinely root-quantified construction is impossible.

## Why the block argument fails

For a state \(P\), a local statement such as
\[
F(P)\ge \lceil\log_2 e(P)\rceil+\delta
\]
is conditional on the sorting game having reached \(P\). To turn it into a root bound, one needs, for every comparison policy within the proposed budget, a consistent answer path reaching such a state with enough budget left to incur the local cost. Reachability by *some* comparison transcript is not that quantifier.

There is a simple invariant showing why the direct **independent ordinal-sum block packing** inference is invalid. For blocks \(P_i\) with \(e_i=e(P_i)\), additive continuation costs give
\[
F\!\left(\bigoplus_i P_i\right)=\sum_i F(P_i)
\ge \sum_i\lceil\log_2 e_i\rceil+\sum_i\delta_i.
\]
But the root’s information bound is \(\lceil\log_2\prod_i e_i\rceil\). These are different bounds on the *already known block state*, not a proof that an antichain-root adversary can force that state while preserving the local deficits. The gap between the blockwise ceilings and the product’s ceiling is at most \(q-1\) for \(q\) blocks, but the missing step is not rounding: it is a root adversary strategy. Local additivity only applies once the order within each block is known.

The notes’ concrete examples illustrate the distinction:

- The one-ply witness \(W\) has \(F(W)=4>\lceil\log_2 e(W)\rceil=3\), and \(W\oplus C_t\) preserves that **local** gap at every larger size. This proves no root lower bound for \(S(5+t)\).
- Balanced two-chain merges have unbounded local gap: Stockmeyer–Yao’s equal-size merge result gives \(M(m,m)=2m-1\), while \(e=\binom{2m}{m}\), so \(M(m,m)-\lceil\log_2 e\rceil=\tfrac12\log_2 m-O(1)\). Again, that is a partial-information state, not a state shown to be forced from the antichain.

This addresses the specific failure of the discussed **local-to-root block transfer**; it is not a theorem ruling out other forcing invariants or other adversary constructions.

## Sergeev rules out linear amplification, not the sublinear target

Sergeev’s primary-source abstract, ECCC TR20-096, says the comparison count is \(\log_2(n!)+o(n)\), achieved by group insertion. Thus a root argument proving a positive linear excess infinitely often would contradict the established upper bound. This does **not** rule out an unbounded sublinear excess: \(o(n)\) is compatible with, for example, a gap tending to infinity more slowly than \(n\).

The current issue #48 body asks for a quantified root strategy or a precise no-go for a proposed grammar; its comment explicitly rejects linear root amplification and names the sublinear gap as the corrected target. The local notes do not resolve that target.

## Evidence and scope

- **Literature:** Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), primary report abstract. It establishes the sublinear *upper* excess for adaptive pairwise comparison sorting.
- **Literature:** Stockmeyer–Yao’s equal-size optimal merge result, as recorded in `docs/research-obstruction-next.md`, supports the unbounded local-gap calculation; it concerns merging two already-ordered chains, not root adversary forcing.
- **Paper deduction from the definitions:** local \(F(P)\) bounds and ordinal-sum additivity apply at a specified partial order; without a quantified root strategy they cannot be transferred to \(S(n)\).
- **Experiment:** finite reachability findings in `notes/research-realizability-window.md` are not used as an asymptotic argument and do not establish adversarial forcing.

**Bottom line:** the attractive candidate “pack many locally deficient blocks, then add their deficits at the root” is falsified as an inference unless its missing root-quantifier lemma is supplied. No complete sublinear forcing theorem, and no universal impossibility theorem for all gadget families, follows from the inspected materials. No files were edited, no post was made, and no Lean work was done.

## Output 134 (msg_1accbc8c3001ww03KTP58OQmdV)

Recovery check complete: the working directory is `/home/lubko/soring-fronts/root-sublinear-amplification-20261105`, and Git reports a clean worktree (`## HEAD (no branch)`). The prior response states that no files were edited and no external post was made. Nothing appears unfinished, so I took no further action.

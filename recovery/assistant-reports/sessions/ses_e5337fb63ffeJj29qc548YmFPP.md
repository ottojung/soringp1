# antonina-33Z5kELYcuKBH1f0co3LhI-merits

Session: ses_e5337fb63ffeJj29qc548YmFPP
Workspace: /home/lubko/soring-fronts/fj-full-frame-20261105
Created: 1793900152071; updated: 1793900260970

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1acc80591001kzOZZCOzWAqW3S)

I’ll first read the current contract and the cited research plan, then inspect the checker and audit note. I’ll keep this to a paper-level construction/falsification attempt and won’t modify or post anything.

## Output 104 (msg_1acc8bf4d00156DLg7T4cI1QB7)

The main issue is already visible in the proposed §3 window statement: the bound `current[ell] < x < current[u+t]` is only meaningful if endpoint indices and the insertion schedule are tracked in a specific coordinate system. I’m now checking that invariant against the recursive winner permutation and against the actual odd-element schedule, rather than treating the index-level bound as a proof.

## Output 148 (msg_1acc93b9c0015UQqq2RrZpTyjB)

## Finding

**Deduction:** The rank-envelope observation in §3 is not yet a complete recursive frame/join invariant. I do not have a counterexample to Ford–Johnson’s standard insertion step; the exact missing lemma is the transfer of **conditional rank bounds through recursive winner sorting**, while retaining the associations between winners and their paired losers.

A plausible representation is a framed state consisting of:

- a full permutation of the original slots, with each winner’s paired loser carried as a tagged slot;
- a sorted winner chain \(a_1<\cdots<a_m\);
- for every pending loser, its paired anchor and a certified interval of possible ranks, expressed relative to the **current framed chain**, not just the chain at the start of the stage.

The merge-insertion step then has a clear local invariant: for \(i\ge2\), \(b_i<a_i\), so \(b_i\) is inserted before \(a_i\). If \(t\) other pending items have already been inserted, the anchor \(a_i\) can have shifted right by at most \(t\) positions. Searching the prefix before that anchor therefore costs at most \(\lceil\log_2(i+t)\rceil\), provided \(i\) refers to the anchor’s rank in the current chain and all prior insertions are represented consistently. For an odd straggler there is no paired anchor, so its search must use the full current chain.

The unresolved step is making that argument survive joins: after recursive calls sort the winners, the frame must permute each winner together with its loser tag; after intersecting incoming guarantees, the resulting annotation must still imply the required anchor order and rank interval for every pending loser. The stated bound `current[ell] < x < current[u+t]` does not itself establish this: it needs a precise endpoint convention, a proof that the relevant endpoint survives the frame, and a proof that the common intersection retains the inequalities.

The checker in `scripts/check_framed_strategy.py` checks an explicitly supplied DAG’s soundness and longest path, but it does not construct this lifted recursive DAG or certify its invariant. Thus it cannot settle the missing step by itself.

## Evidence and next lemma

**Literature:** Ford and Johnson, *A Tournament Problem* (1959), is the source for merge-insertion; Knuth, *TAOCP* Vol. 3, §5.3.1 gives the classical comparison analysis. Stober and Weiß, *On the Average Case of MergeInsertion* (2020), is a primary analysis of the algorithm and its insertion schedule. The source’s standard schedule inserts descending within Jacobsthal blocks; the published worst-case argument bounds each insertion’s search prefix. Those facts support the comparison bound, but not the framed-DAG join invariant.

**Exact missing lemma:** For every recursive call on a set of winner slots with an injective pairing map to loser slots, construct a polynomial-size framed DAG whose feasible leaf annotations, after intersecting all paths merged at each node, imply:
1. the recursively sorted winner order;
2. each loser’s strict relation \(b_i<a_i\), with the association preserved under every slot permutation;
3. the current-chain rank interval needed for each scheduled binary insertion, including the unpaired odd key’s full-range interval;
4. a total-order guarantee at every terminal; and
5. longest root-to-leaf path at most \(F_{\rm FJ}(n)=\sum_{j=1}^n\lceil\log_2(3j/4)\rceil\).

I did not prove this lemma or find a concrete failure of the standard insertion step. The proposed §3 window argument is therefore **inconclusive**, not an all-\(n\) certificate theorem. No files were changed and nothing was posted.

## Output 176 (msg_1acc9a1a2001T5TBYGYcmYTZZj)

The previous turn completed its research response. **I found no evidence of external side effects**: the worktree is clean, HEAD is unchanged at `c865b23`, and no task or posting record was found. The prior response explicitly said it made no edits and posted nothing.

The unfinished-work question is resolved in that response: no proof or counterexample was established; it identified the recursive winner/loser frame-and-join preservation lemma as still missing. Nothing was repeated or posted.

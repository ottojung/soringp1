# antonina-SFhHs2J3vnoHfQ9jyGtymF-citizen

Session: ses_e4b339882fferAPjaisE59lhHy
Workspace: /home/lubko/soring-fronts/exec-winning-frontier-forcing-20261107
Created: 1794034657213; updated: 1794034700221

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4cc69760010tajAOKfbJyaVE)

I’ll inspect the specified research note and the #47/#48 context, then assess whether a forced-family transfer has a credible proof route. I’ll keep this research-only and won’t edit files or post to the board.

## Output 41 (msg_1b4cc8dbb001olIbudl5yAlJoL)

The central quantifier gap is confirmed: the construction proves a large set of locally winning states reachable by some transcripts, while a strategy chooses one comparison at each reached state and must keep both outcomes within budget. I’m checking the primary source for the `S(n)=log₂(n!)+o(n)` step and the notes’ exact “root-optimal” distinctions before stating the obstruction.

## Output 76 (msg_1b4ccc477001C2WicnWoUFUg5M)

## Finding: the frontier theorem does not transfer to a forced frontier

**[Deduction / precise obstruction]** The existing theorem establishes a large *existential* frontier: at one depth there are many distinct partial orders \(P\), each reachable by some legal transcript and each satisfying \(F(P)\le S(n)-t\). It does not establish that these transcripts are compatible with one root strategy. The proposed stronger statement would need the quantifiers

\[
\forall\text{ optimal root strategies }T,\quad
\exists t:\ 
\bigl|\{P:\ P\text{ is reached at depth }t\text{ in }T
\text{ and is winning with budget }S(n)-t\}\bigr|
\ge 2^{\Omega(n\log^2n)}.
\]

That does not follow from the frontier count. A strategy selects one query at each reached state; the construction counts states across arbitrary transcripts. Even if each transcript reaches a winning state, the transcripts may require incompatible first queries or later choices.

### Why the independent-edge family does not supply the transfer

In the construction, each member is specified by a set \(A\) of extra adjacent-level edges, learned along a transcript of length \(t=t_0+m\). At the root, however, a strategy must choose one pair to compare. The construction does not show that there is a single pair whose two outcomes preserve a sufficiently large subfamily, nor that the surviving subfamilies can be recursively split while remaining inside the construction and within the exact optimal height budget.

That is the missing invariant: after every chosen query and either feasible outcome, one would need a large structured descendant family, with a compatible remaining-depth/winning-budget guarantee. Counting the original edge sets gives no such branching guarantee. The query might be one of the skeleton or added relations for some members and incomparable for others; conditioning on its outcome can destroy the independent-edge parametrization or leave too little budget for the chain-merging upper bound. No recursive invariant or query-choice lemma in the cited notes repairs this gap.

The alternative “minimum size of every exact-optimal strategy DAG” is also not obtained. A lower bound on states reached by *some transcripts* is not a lower bound on nodes of every strategy. And a strategy DAG lower bound would require its own argument: a particular DAG can share a residual state reached by multiple histories, while the frontier theorem counts posets, not compulsory nodes in a root-optimal policy.

### Relation to certificates and unary complexity

A superpolynomial lower bound on **all exact-optimal framed certificates** would be a certificate-size barrier for that grammar. It would rule out using those certificates to prove `SORT-BOUND-U ∈ NP`; it would not establish a lower bound on evaluator time or separate complexity classes. Likewise, a lower bound on every exact-optimal strategy DAG would obstruct that DAG certificate format, but would not by itself rule out other succinct certificates or algorithms. The existing soundness result only gives NP membership *if* polynomial-size exact-optimal framed certificates always exist; completeness is open.

The active decision language remains unary `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`. Because it is in PSPACE, class-separation claims remain subject to the project’s stated barriers. The current frontier result is an enumeration barrier, not a hardness or evaluator lower bound.

### Evidence and disposition

**[Literature]** Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), proves an upper bound \(\log_2(n!)+o(n)\), which supports applying the existing construction at budget \(S(n)\). It does not address root-strategy forcing. **[Repository analysis]** `docs/research-framed-certificate-frontier.md` explicitly distinguishes generic reachable histories from those forced along optimal root strategies and notes that history counts need not force a large forgetful DAG.

I found no credible transfer route from the independent-edge count to the requested universal strategy quantifier, and no concrete all-\(n\) counterstrategy or verified finite falsifier to substitute. Per the requested stopping criterion, the result is **unsuitable as a forced-frontier claim on the available argument**; the decisive missing step is a recursive, both-outcomes-preserving family invariant for arbitrary optimal query choices. No computation was warranted without a specific candidate lemma to falsify.

Worktree remains clean. No source edits, commit, Lean work, or board post.

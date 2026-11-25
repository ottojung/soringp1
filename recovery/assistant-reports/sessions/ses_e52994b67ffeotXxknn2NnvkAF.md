# antonina-jY2qalb6BHB5qMAGY3wM9B-naevus

Session: ses_e52994b67ffeotXxknn2NnvkAF
Workspace: /home/lubko/soring-fronts/exact-s12-fo-tc-nonframed-20261105
Created: 1793910551823; updated: 1793910603362

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 68 (msg_1ad671930001jPaWtXnEcco3pM)

**Result: no explicit finite bound can be extracted from Theorem 3 as cited.** The theorem gives an asymptotic \(O(n/(\log n)^{1/5})\) excess, but its big-\(O\) statement supplies neither a constant nor a threshold. Thus it does not yield a stated computable \(g(n)\) valid for every finite \(n\). This matches the project’s existing caveat in [`docs/research-sergeev-asymptotic.md`](docs/research-sergeev-asymptotic.md#L18-L23).

For any explicit \(A,n_0\) established from the construction, the asymptotic estimate would give, for \(n\ge n_0\),
\[
S(n)\le \lceil\log_2(n!)\rceil+
\left\lceil A\,n/(\log n)^{1/5}\right\rceil.
\]
To make this an all-\(n\) bound, one must also supply finite upper bounds for \(n<n_0\). Neither the cited asymptotic statement nor the local documents provide those parameters. I could not retrieve the primary PDF in this environment, so I cannot substantiate a stronger claim about whether the full proof’s construction admits such an effective extraction. The primary source is Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), Theorem 3, p. 29: https://eccc.weizmann.ac.il/report/2020/096/.

The finite checks are consistent but don’t establish constants: at \(n=12\), \(S(12)=30\) and \(\lceil\log_2(12!)\rceil=29\), so any proposed \(g(12)\) must be at least 1. Exact values through \(n=22\) are recorded in [`docs/research-plan.md`](docs/research-plan.md#L8-L21); the source notes identify Stober–Weiß for the later exact values in [`docs/literature.md`](docs/literature.md#L14-L20).

**Obstacle:** a rigorous extraction requires auditing the group-insertion proof for explicit constants, all finite-size conditions, and a computable treatment of its small-\(n\) range. Until then, using \(o(n)\) or \(O(n/(\log n)^{1/5})\) as a finite search window would be unjustified. No repository files were changed.

## Output 99 (msg_1ad676f2b0014cuGEkBpgrwJYZ)

Inspection found no evidence that the prior turn made external changes: no commit was created, and the only untracked file is `docs/exact-s12-fo-tc-nonframed.md`. I did not modify it; it may be existing user work. The prior task explicitly prohibited repository edits, board posts, and commits, and the response reported none. No durable task record was found.

The previous inquiry appears complete, with the primary-source PDF retrieval still unresolved. No external effects remain to continue or repeat.

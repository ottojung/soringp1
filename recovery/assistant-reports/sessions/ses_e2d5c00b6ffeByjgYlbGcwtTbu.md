# antonina-fkMeRAzlYDYThn7iKIvMkI-invite

Session: ses_e2d5c00b6ffeByjgYlbGcwtTbu
Workspace: /home/lubko/soring-fronts/curator
Created: 1794535325516; updated: 1794544429344

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 121 (msg_1d32e6c630011fEtPVt9WdjewP)

{
  "fronts": [
    {
      "id": "info-lower-bound-additive-gap-boundedness",
      "question": "Is there an absolute constant C such that for all n >= 1 the exact sorting number satisfies S(n) <= ceil(log2(n!)) + C, i.e. is the additive gap above the information-theoretic lower bound uniformly bounded over all n?",
      "falsifier": "Exhibit either (i) for every proposed C an explicit n with a proved value S(n) >= ceil(log2(n!)) + C + 1, establishing unbounded gap, or (ii) a proof that some fixed C works for all n.",
      "implication": "A uniform additive bound would be a strong all-n structural theorem tightening the known Theta(n log n) sandwich for S(n) and could constrain exact-evaluation/certificate questions; unbounded gap would rule out constant-additive optimality of the information bound as a universal target.",
      "basis": "problem.md/literature.md: ceil(log2 n!) <= S(n) <= O(n log n), exact values known for n<=22 with gaps S(12)-29=1 and S(16,17,18)-ceil(log2 n!)=1 (Stober-Weiss ALENEX 2023); no all-n additive-gap theorem or unbounded-growth proof recorded on board #301."
    }
  ]
}

## Output 173 (msg_1d32ed6a6001UZBXvvWCYevMBX)

Recovery check: `frontier-candidates.json` was created and contains one candidate. Git shows only that untracked file; there are no commits or board posts from this turn. The recent board digest and durable ledger show no record of this candidate being imported or investigated. No further action was taken.

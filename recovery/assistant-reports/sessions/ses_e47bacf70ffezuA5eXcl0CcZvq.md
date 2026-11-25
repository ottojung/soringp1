# antonina-ccPJZQFGCgH3RMVyUuCFRc-naming

Session: ses_e47bacf70ffezuA5eXcl0CcZvq
Workspace: /home/lubko/soring-fronts/curator
Created: 1794092904600; updated: 1794093561580

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 429 (msg_1b84f13840014HQh0lAIWweDrZ)

Studied `AGENTS.md`, `docs/problem.md`, the newest #301 entries, and the relevant literature/notes. I attacked the board’s all-`r` Fibonacci threshold and the stronger extremal-uniqueness variant; I found no counterexample. Independent connected-core census checks for `e=21, m=6` yielded 21 representations, all fence-isomorphic, consistent with `T(4)=12` and `T(5)=20`.

I did not duplicate the active all-`r` threshold work. The only new, nonredundant front written is the distinct uniqueness question. No Lean changes or repository changes beyond the required JSON were made. Honest limit: uniqueness is checked only on the connected core census and small `r`; it is not proved for all `r`, and it is a structural theorem, not a certificate-completeness or complexity-class claim.

`/home/lubko/soring-fronts/curator/frontier-candidates.json`:

```json
{
  "fronts": [
    {
      "id": "fence-core-uniqueness",
      "question": "For every r >= 1, is the fence poset P_{r+1} the unique core poset (no element comparable to all others) with exact minimax depth m(P)=r and exactly F_{r+2} linear extensions, up to isomorphism?",
      "falsifier": "Exhibit a core poset P with m(P)=r and e(P)=F_{r+2} that is not isomorphic to the fence P_{r+1} for some r, starting with r=6.",
      "implication": "Uniqueness would make the fence the canonical extremal family for the extension threshold T(r)=F_{r+3}-1, transferring fence-specific certificate and evaluator lower bounds to every threshold extremal; it would be a structural theorem, not a P/PSPACE separation.",
      "basis": "Newest board #301 extension-threshold conjecture T(r)=F_{r+3}-1 with fence e=F_{n+1}, m=n-1; docs/research-budget-pruning.md and docs/research-obstruction-next.md; independent connected-core census check that all 21 e=21, m=6 representations are fence-isomorphic, plus the finite T(4)=12 and T(5)=20 data."
    }
  ]
}
```

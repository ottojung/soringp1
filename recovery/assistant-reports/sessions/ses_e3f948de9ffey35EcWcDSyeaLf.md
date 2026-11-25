# antonina-ezlosAhXO3ognOJhfPF8TL-pulling

Session: ses_e3f948de9ffey35EcWcDSyeaLf
Workspace: /home/lubko/soring-fronts/curator
Created: 1794229629501; updated: 1794231597771

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 332 (msg_1c088e669001D9Es3N29LNgvbo)

{
  "fronts": [
    {
      "id": "two-wl-move-quotient-soundness",
      "question": "For every finite poset P, does the stable 2-dimensional Weisfeiler-Leman colour of an incomparable pair determine its exact minimax move value T({x,y}) = max(F(P+x<y), F(P+y<x))?",
      "falsifier": "Exhibit a poset P with two incomparable pairs having identical stable 2-WL colour but provably different exact T values, checked by exact minimax over linear extensions.",
      "implication": "A sound 2-WL move quotient would supply a polynomial-size exact move invariant for root-reachable states and a candidate step toward an NP certificate; a counterexample retires the colour-refinement route.",
      "basis": "Newest #301 colour-pair counterexample at n=8; that post reports full 2-WL separates the witness but does not test soundness of the 2-WL move quotient."
    },
    {
      "id": "height-two-information-excess-bound",
      "question": "Is F(P) - ceil(log2 e(P)) at most 1 for every finite poset P of height at most two?",
      "falsifier": "Exhibit a height-two poset with exact excess F(P) - ceil(log2 e(P)) at least 2, verified by exact minimax and exact linear-extension counting.",
      "implication": "If bounded, the information bound is nearly tight one comparison from the antichain and constrains information-based pruning barriers; if unbounded, shallow reachable states already carry an unbounded information gap relevant to lower bounds and certificates.",
      "basis": "Board #301 coverage-dual height-two lemma; exact enumeration through n=6 finds first excess 1 at V3 disjoint A3 (e=240, F=9) and none through n=5; matching families have excess 0."
    },
    {
      "id": "degree-product-extension-inequality",
      "question": "Does every finite n-element poset P satisfy e(P) * prod_v (1+d_v) >= n!, where d_v is the number of elements strictly above v in P?",
      "falsifier": "Exhibit an n-element poset P with e(P) * prod_v (1+d_v) < n!, verified by exact integer arithmetic for e(P) and the outdegrees d_v.",
      "implication": "If true, the polynomial-time degree product gives a sound extension lower bound that can replace exact #P extension counting in minimax pruning; if false, it identifies a sharp limit of degree-only bounds.",
      "basis": "Board #301 height-two extension lemma e(P) >= n!/2^t; the degree product is the analogous all-poset bound, checked without violation by exact enumeration through n=6 and random posets through n=15."
    }
  ]
}

## Output 391 (msg_1c0896353001tTrMD5XlizfQmI)

Recovery inspection complete. No unfinished external work remains.

- **Intended effect present:** `/home/lubko/soring-fronts/curator/frontier-candidates.json` exists, is valid JSON, and contains exactly the three proposed fronts.
- **Git state:** worktree at `6a96398`; the only change is the intended untracked `frontier-candidates.json`. No commits, branches, or Lean changes.
- **Board #301:** no posts found containing any of the candidate IDs or `frontier-candidates`. No duplicate board post was made.
- **Ledger:** none of the three candidate IDs has been imported; the curator entry remains keeper-managed and `running`, as expected before keeper reconciliation.
- **Uncertain effects:** none identified. I did not repeat the research prompt, rewrite the file, post to the board, or alter the ledger.

The original curator task is therefore complete as delivered.

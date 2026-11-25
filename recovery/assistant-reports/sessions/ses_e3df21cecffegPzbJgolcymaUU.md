# antonina-n0W9vPfEeQ9CBQ7iy1gFIC-spindle

Session: ses_e3df21cecffegPzbJgolcymaUU
Workspace: /home/lubko/soring-fronts/curator
Created: 1794257052485; updated: 1794257513156

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 255 (msg_1c214d615001qrCjvoam7YZVVr)

{
  "fronts": [
    {
      "id": "disjoint-union-minimax-superadditivity",
      "question": "For all finite posets A and B on disjoint ground sets, is F(A disjoint-union B) at least F(A)+F(B), where F is the exact minimax comparison number measured against the linear extensions of the poset in question?",
      "falsifier": "Exhibit explicit finite posets A and B with F(A disjoint-union B) < F(A)+F(B), with both sides obtained from the exact minimax recurrence rather than from an information bound or an assumed additivity formula.",
      "implication": "An all-n superadditivity theorem would give a sound decomposition lower bound for reachable disjoint-union states; a counterexample would show exactly how cross-component comparisons can destroy direct-sum intuition and would invalidate evaluators that treat such unions additively.",
      "basis": "Newest #301 correction showing F(K disjoint-union A_s) need not equal F(K)+I(|K|,s) because cross comparisons can order elements of K; docs/research-series-decomposition.md; a finite exact-minimax scan over all 3+3 labelled poset pairs found no violation."
    },
    {
      "id": "two-wl-child-extension-count-soundness",
      "question": "For every height-at-most-two poset P and every incomparable pair {x,y}, does the stable full/paired 2-WL colour of {x,y} determine the unordered pair of exact child extension counts {e(P+x<y), e(P+y<x)}?",
      "falsifier": "Exhibit a height-two poset and two incomparable pairs of identical stable full/paired 2-WL colour whose unordered child extension-count pairs differ, verified by direct linear-extension counting.",
      "implication": "If true, child extension counts are 2-WL invariants, a necessary condition for a sound colour-based leaf-count pruning certificate; if false, even the sound leaf-count use of 2-WL fails, strengthening the n=32 incompleteness obstruction.",
      "basis": "Newest #301 n=32 biplane incidence-poset counterexample to child-isomorphism completeness and the Executive check posted at 20:43Z; the earlier n=10 positive scan; the board distinction between certificate soundness and completeness."
    }
  ]
}

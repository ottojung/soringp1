# antonina-4z2YSki6f2KOQPBcLRVzoe-schmidt

Session: ses_e443f4d38ffePLd3JVKZaZ5vXJ
Workspace: /home/lubko/soring-fronts/curator
Created: 1794151330512; updated: 1794151988600

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 374 (msg_1bbc91426001o5V3ngMXJg6QtP)

{
  "fronts": [
    {
      "id": "logarithmic-information-excess-alln",
      "question": "For the exact sorting number S(n), is S(n) - ceil(log2(n!)) = O(log n) for every n, or is there an infinite family of n on which this excess is at least c log n for some fixed c > 0?",
      "falsifier": "Prove the O(log n) upper bound with explicit constants for all n, or certify an infinite family with excess omega(log n); a single family beating every proposed logarithmic bound refutes the first horn.",
      "implication": "The first horn would sharply improve Sergeev's o(n) excess and give a polynomial-time O(log n)-additive approximation; the second would establish a new super-logarithmic excess regime and rule out logarithmic-additive exact evaluation.",
      "basis": "Sergeev's bound S(n)-log2(n!) = O(n/(log n)^(1/5)) and the information lower bound leave the logarithmic range open; the ledger's excess and additive-approximation fronts target bounded excess and O(1)/O(log log n) error, not this O(log n) threshold."
    },
    {
      "id": "haeupler-heapsort-antichain-excess",
      "question": "When the Haeupler et al. heapsort variant (arXiv:2404.04552v4, Appendix C, as cited in the newest #301 post) is specialized to the n-element antichain, is its comparison-tree height log2(n!) + o(n) for all n, or does it collapse to an insertion/merge family with Omega(n) excess?",
      "falsifier": "Analyze the antichain specialization and prove a height lower bound of the form A(n) >= log2(n!) + c n for all large n, or exhibit an all-n implementation whose comparison count is log2(n!) + o(n).",
      "implication": "An explicit o(n)-excess algorithm would make the known PSPACE upper bound constructive and give a polynomial-time computable target for exact S(n); an Omega(n) barrier would extend the insertion-sort obstruction to this heapsort family.",
      "basis": "The newest #301 explicit-dag post refuted the van der Hoog-Rotenberg-Rutschmann specialization but explicitly left the Haeupler heapsort variant unrefuted; no ledger front names that variant."
    },
    {
      "id": "split-merge-fj-coefficient-limit",
      "question": "For n_k = floor(4*2^k/3), does m(n_k)/n_k = (L(n_k)-log2(n_k!))/n_k converge, and is its limit at least the Ford-Johnson coefficient 0.02766, or does the sequence eventually fall strictly below that coefficient?",
      "falsifier": "Prove a strict limit below 0.02766 by exact DP at larger k or an analytic recurrence, or prove liminf >= 0.02766, equivalently that split-merge never asymptotically beats Ford-Johnson on this sequence.",
      "implication": "A limit at least the Ford-Johnson coefficient would show the split-merge architecture cannot asymptotically improve on Ford-Johnson; a strict drop below would make split-merge a competitive explicit upper-bound family and reopen it as an exact-evaluation route.",
      "basis": "Newest #301 split-merge-k18-window reports exact L(349525) and L(699050) with m(n)/n descending and about 1.44 times 0.02766 at k=19; split-merge-asymptotic-gap asks L(n)-S(n), not this coefficient comparison."
    },
    {
      "id": "height-optimal-average-depth-price",
      "question": "Let A(n) be the minimum average leaf depth among correct comparison trees of height exactly S(n). Is S(n) - A(n) bounded by an absolute constant for all n, or does this height-optimal average-depth price grow without bound?",
      "falsifier": "Prove a uniform constant K with A(n) >= S(n)-K for all n, or exhibit an infinite family of height-S(n) trees whose average depth is S(n)-omega(1).",
      "implication": "Bounded S(n)-A(n) would show worst-case-optimal trees are almost average-optimal and transfer average-depth methods to S(n); unboundedness would separate the worst-case and average optima inside the optimal-height class.",
      "basis": "The ledger's s-optimal-tree-average-depth-gap studies A(n)-log2(n!) and reports A(7)=62416/5040 < S(7)=13; it does not ask whether the gap S(n)-A(n) itself is bounded."
    }
  ]
}

## Output 441 (msg_1bbcaa87d001jesirU8dUKqLqj)

Recovery check complete.

- **Existing deliverable:** `/home/lubko/soring-fronts/curator/frontier-candidates.json` already exists and parses as valid JSON with 4 fronts.
- **Schema checks:** all IDs are 32–35 character lowercase slugs; all question/falsifier/implication/basis fields exceed the minimum lengths; none of the IDs duplicate the durable ledger.
- **Git state:** the file is untracked (`?? frontier-candidates.json`). No commit was made.
- **Board:** no post was made.
- **Unfinished work:** none. The curator deliverable is complete; I did not repeat the file write or any external action.

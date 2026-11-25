# antonina-UkkuuzZ5CO9jifOH1oI9ZA-doing

Session: ses_e42651e51ffevndLSr9D8Ewkqf
Workspace: /home/lubko/soring-fronts/curator
Created: 1794182406587; updated: 1794183523530

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 313 (msg_1bdabb9f5001sdfwEelkmteKQm)

{
  "fronts": [
    {
      "id": "extreme-deficit-linear-scale",
      "question": "For n at least 2 let D(n)=S(n)-R(n) be the extreme-move deficit. Is D(n)=n+O(1) uniformly for all n, or does |D(n)-n| grow without bound along an infinite family?",
      "falsifier": "Compute an n with |D(n)-n| at least 2 by exact max-min DP, with n=10 the next target, or prove a uniform bound |D(n)-n| at most C.",
      "implication": "The first horn would upgrade the open D(n)=o(n) versus liminf D(n)/n>0 dichotomy to D(n)/n tending to 1 and pin the extreme and non-extreme split of every optimal critical path.",
      "basis": "Board #301 records D(2..7)=1,3,4,4,6,8; an exact iso-DP run during curation returned D(8)=9 and D(9)=9, so D-n lies in {-1,0,1} through n=9."
    },
    {
      "id": "component-reversal-defect-bound",
      "question": "For all finite posets A and B, is the component-reversal defect |F(A^op disjoint-union B)-F(A disjoint-union B)| at most 1, or can it be arbitrarily large?",
      "falsifier": "Exhibit A,B with reversal defect at least 2 by exact minimax over disjoint unions, or prove the uniform bound 1 by a structural induction.",
      "implication": "A uniform one-comparison bound would make component reversal a canonicalization with only additive-one value loss in exact DP; unbounded defect would show component orientation carries unbounded value information and block every reversal quotient.",
      "basis": "Newest #301 parallel-reversal-symmetry reports F(A^op disjoint-union B)=11 versus F(A disjoint-union B)=12 at n=9, with all n at most 8 pairs equal and 96 of 1840 non-self-dual n=9 pairs violating equality."
    },
    {
      "id": "near-optimal-farkas-succinctness",
      "question": "For every n, does the faithful state-expanded comparison-tree LP at the near-optimal budget k=S(n)-1 admit a Farkas infeasibility certificate whose support size and coefficient bit-length are polynomial in N=n+S(n)?",
      "falsifier": "Construct an infinite family of n whose near-optimal LP has only super-polynomial-support Farkas certificates, or give a polynomial-support certificate for every n at k=S(n)-1.",
      "implication": "A positive answer would supply a coNP-style no-certificate exactly in the hard window, since the known matching-family support barrier applies only at k approximately n/2.",
      "basis": "Newest #301 succinct-farkas-dual-certificate proves exponential support for even n at k=n/2 and explicitly leaves k=S(n)-1 open; Viche independently checked the matching count."
    },
    {
      "id": "multi-chain-merge-exact-complexity",
      "question": "Is the exact minimax merge number for a disjoint union of k at least 3 chains computable in time polynomial in the total number of elements for every tuple of chain lengths?",
      "falsifier": "Give a polynomial-time algorithm with a correctness and cost proof for all chain tuples, or exhibit an infinite family of tuples whose exact multi-chain merge is super-polynomial under a stated model.",
      "implication": "A polynomial multi-chain merge would make the full split-merge architecture's height computable and narrow the exact S(n) search window; hardness would isolate the first merge stage where near-optimal sorting becomes intractable.",
      "basis": "Newest two-chain-merge exact results cover only k=2, while the split-merge recurrence and Ford-Johnson group insertion use multi-chain merges."
    }
  ]
}

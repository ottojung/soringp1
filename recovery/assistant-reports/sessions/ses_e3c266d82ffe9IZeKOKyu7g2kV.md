# antonina-HokP6Xsln6ymCQ7Khl9Jsk-thereof

Session: ses_e3c266d82ffe9IZeKOKyu7g2kV
Workspace: /home/lubko/soring-fronts/curator
Created: 1794287178437; updated: 1794289462376

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 356 (msg_1c3fc31ea001M8D8q87YL045mf)

```json
{
  "fronts": [
    {
      "id": "single-deletion-eta-characterization",
      "question": "For all integers a,b >= 2, is the exact minimax value of the single-deletion prime poset P=(A_a (+) A_b) - {(a0,b0)} equal to S(a)+S(b) when min(a,b) >= 3 and to S(a)+S(b)+1 when min(a,b)=2?",
      "falsifier": "Exhibit a,b >= 3 with F(P) = S(a)+S(b)+1, or a,b with min(a,b)=2 and F(P) = S(a)+S(b), by exact minimax computation.",
      "implication": "A positive answer would fix the exact excess of the prime single-deletion family as E(a)+E(b)+d+eta, resolve the n=27 base ambiguity, and give a precise structural theorem about the minimax game on a family built from S(n).",
      "basis": "Newest board #301 prime-excess-unbounded (02:00Z) proves F(P) is in {S(a)+S(b), S(a)+S(b)+1} and leaves the exact value open; independent exact minimax computation here for a,b <= 6 gives eta=1 for min=2 and eta=0 for min>=3."
    },
    {
      "id": "fan-family-excess-boundedness",
      "question": "For all integers m,k >= 2 and 1 <= r <= m-1, is the information excess F(P)-ceil(log2 e(P)) of the fan poset P=(A_m (+) A_k) with r cross relations deleted from a fixed maximal element at most 3?",
      "falsifier": "Exhibit m,k,r with exact F(P)-ceil(log2 e(P)) >= 4, or prove that the fan family excess is unbounded as m,k,r grow.",
      "implication": "Since the fan family contains the single-deletion prime family, a uniform bound would imply the antichain excess E(n) is bounded by an absolute constant; a counterexample would give a simpler unbounded prime family than the iterated gluing.",
      "basis": "Newest board #301 prime-excess-unboundedness (01:56Z) derives the fan-family extension count and reports an exact scan over m,k <= 22 with maximum excess 3, while stating that this family alone does not grow; no all-(m,k,r) proof exists."
    }
  ]
}
```

# antonina-XxRUmaG3VDUjvu2dxl42qr-cocci

Session: ses_e3d28633cffe4ltvBcAqvaSxUt
Workspace: /home/lubko/soring-fronts/curator
Created: 1794270272734; updated: 1794271301242

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 239 (msg_1c2e729c0001ZTAHcYja2DAO8B)

{
  "fronts": [
    {
      "id": "disjoint-union-defect-min-size",
      "question": "For all nonempty finite posets A,B on disjoint ground sets with |A|+|B|>=3, is F(A disjoint-union B) at least F(A)+F(B)+min(|A|,|B|)+1, strengthening the board's two-comparison defect bound?",
      "falsifier": "Exhibit explicit nonempty A,B with |A|+|B|>=3 whose independently computed exact minimax values satisfy F(A disjoint-union B) <= F(A)+F(B)+min(|A|,|B|).",
      "implication": "A proof would give a size-sensitive lower bound for every parallel composition and force any additive evaluator or exact certificate to account for min(|A|,|B|)+1 extra comparisons; a counterexample would show the +2 bound is uniformly tight and block this strengthening.",
      "basis": "Board #301 2026-11-10T00:03Z disjoint-union-defect-at-least-two proves only +2; exact exhaustive and random checks on small A,B here found no violation, but the min-size strengthening remains unproved."
    },
    {
      "id": "fixed-block-kfold-parallel-decomposition",
      "question": "For every fixed nonempty finite poset P of size m, is F(P disjoint-union k copies) equal to k F(P) + F(C_m disjoint-union k copies) + O_P(1), so that sorting k copies asymptotically reduces to optimal per-copy sorting plus optimal k-way merging of m-chains?",
      "falsifier": "Exhibit a fixed P and an infinite family of k where exact minimax exceeds k F(P)+F(C_m^disjoint-k) by a quantity growing faster than any fixed constant, or give one exactly certified violation.",
      "implication": "Equality would justify a block-decomposition evaluator that summarizes each copy by F(P) and reduces parallel composition to merge numbers; failure would prove that internal and cross comparisons must interleave with asymptotically unbounded advantage.",
      "basis": "The newest disjoint-union-defect-at-least-two post controls only two blocks; no ledger front tests fixed-block k-fold equality against sort-each-then-merge, and small exact checks are finite evidence only."
    },
    {
      "id": "recursive-abc-exact-height-completeness",
      "question": "For every finite poset P, does there exist a comparison tree of height exactly F(P) in which every internal node is labelled by a Peczarski A/B/C witness (low-slave, half-balanced, or balanced-triple) for its chosen comparison?",
      "falsifier": "Exhibit a finite poset P for which exact minimax shows every height-F(P) comparison tree has at least one node whose chosen incomparable pair satisfies none of the three A/B/C conditions.",
      "implication": "A proof would upgrade A/B/C from sound GPC witnesses to a complete exact-minimax strategy grammar; a counterexample would establish a concrete soundness-versus-completeness separation for recursive A/B/C certificates and block their use as exact S(n) certificates.",
      "basis": "Board #301 2026-11-10T00:24Z abc-certificate-checking-complexity and 2026-11-09T22:37Z certificate-disjoint-union-closure treat A/B/C as sound GPC witnesses; the running recursive union front does not test general exact-height A/B/C completeness."
    },
    {
      "id": "height-two-abc-witness-existence",
      "question": "For finite height-at-most-two posets P, is deciding whether P admits at least one Peczarski A/B/C witness in polynomial time, or is witness existence NP-hard or #P-hard under exact linear-extension counting?",
      "falsifier": "Give a polynomial-time decision algorithm for all height-two P, or a polynomial-time reduction from a #P-hard extension-counting problem to deciding existence of an A/B/C witness.",
      "implication": "Polynomial decidability would supply a GPC certificate search on the height-two slice where exact F is already hard; hardness would show that even GPC witness existence, not merely supplied-witness checking, is intractable.",
      "basis": "Newest #301 abc-certificate-checking-complexity studies verification of a supplied witness, while gpc-height-two-threshold leaves GPC itself open; no ledger front asks for the decision complexity of witness existence."
    }
  ]
}

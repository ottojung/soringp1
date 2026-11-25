# antonina-2wXW2LOE4884uuVGrd3Gii-lying

Session: ses_e3d7978baffevoD9KWjAPOm8kA
Workspace: /home/lubko/soring-fronts/curator
Created: 1794264958831; updated: 1794265991789

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 257 (msg_1c2962c54001OIuj31jlU0E8Py)

{
  "fronts": [
    {
      "id": "recursive-certificate-disjoint-union-closure",
      "question": "For all finite nonempty posets A,B on disjoint ground sets, does the existence for A and for B of a correct comparison tree of height F whose every internal move meets a Peczarski A/B/C witness condition imply the same for A disjoint-union B at height F(A disjoint-union B)?",
      "falsifier": "Exhibit finite A,B carrying such height-optimal recursive A/B/C certificate trees for which every height-F(A disjoint-union B) tree for the disjoint union has a reachable node whose chosen comparison fails the low-slave, half-balanced, and balanced-triple conditions, with exact extension counts at that node.",
      "implication": "A proof would lift the verified root-level closure theorem to a recursive compositional certificate rule for parallel composition; failure would identify exactly which cross-comparison child destroys the sound A/B/C witness and separate certificate soundness from recursive completeness.",
      "basis": "Board #301 2026-11-09T22:37Z certificate-disjoint-union-closure states that its result is root-level only and explicitly leaves recursive/full-strategy closure open; Peczarski, Order 23 (2006) 89-95, Facts 1-2; the 21:43Z gpc-certificate-completeness reduction forcing any counterexample to be ordinal-indecomposable and core."
    },
    {
      "id": "prime-height-three-excess-one",
      "question": "For every finite poset P of height at most three that is neither an ordinal sum nor a disjoint union of two nonempty posets, is the information excess F(P)-ceil(log2 e(P)) at most 1?",
      "falsifier": "Exhibit an ordinal-sum- and disjoint-union-indecomposable height-three poset with exact information excess at least 2, with independently computed exact minimax height and exact linear-extension count.",
      "implication": "A proof would confine any height-three excess above the antichain value E(n) to the already-studied series and parallel compositions; a counterexample would be a prime local amplifier not reducible to E(n) by the verified composition lemmas.",
      "basis": "Board #301 2026-11-09T21:57Z height-three-excess-root-equivalence and the 22:00Z Executive check: series additivity and parallel binomial entropy force any separation to come from a prime height-three poset; exhaustive labelled checks through n=7 found excess at most 1, attained only at height two."
    },
    {
      "id": "disjoint-union-defect-at-least-two",
      "question": "For all finite nonempty posets A and B on disjoint ground sets with |A|+|B| at least 3, is the disjoint-union minimax defect F(A disjoint-union B)-F(A)-F(B) at least 2?",
      "falsifier": "Exhibit finite nonempty A,B with |A|+|B| at least 3 and exact defect exactly 1, verified by exact minimax values for A, B, and their disjoint union.",
      "implication": "A proof would sharpen the newly proved positive strict-defect theorem into a two-comparison lower envelope for every nontrivial parallel composition; a defect-1 pair would show the strict-defect bound is tight beyond the two-singleton case and change the defect-growth picture.",
      "basis": "Board #301 2026-11-09T22:06Z disjoint-union-strict-defect proves defect at least 1 and explicitly leaves its size and growth open; an independent exhaustive disjoint-union check over all poset pairs with parts of size at most 4 and total size at most 6 found minimum defect 1 only at total size 2 and no defect below 2 for larger tested totals."
    }
  ]
}

# antonina-JfhGGrdWcrwZdkZCjP5LQq-poorer

Session: ses_e0985590cffe9EQdMQ7NkjXBJT
Workspace: /home/lubko/soring-fronts/curator
Created: 1795136595706; updated: 1795137343490

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 210 (msg_1f6845614001L7j9F1Zsmio6iu)

I've completed the study pass. Now I'll write the curator deliverable.

## Output 239 (msg_1f685ca1a001MnvDbZsweDWKQE)

The curator deliverable is written and schema-validated.

**File written:** `/home/lubko/soring-fronts/curator/frontier-candidates.json`

```json
{
  "fronts": [
    {
      "id": "tight-n-state-gap-alln",
      "question": "For infinitely many n whose exact sorting number equals the information bound ceil(log2(n!)) exactly, does the minimax-optimal reachable comparison-state set from the n-element antichain miss any state that lies on some height-S(n) optimal comparison tree?",
      "falsifier": "Prove that for all sufficiently large information-tight n the local-optimal and globally feasible state sets coincide, or construct an explicit infinite family of tight n with a nonempty optimal-state gap.",
      "implication": "An infinite information-tight optimal-state gap would show that locally minimax-optimal reachable sets can miss legitimate optimal states even at the information-tight optimum, constraining sound evaluator designs for exact unary S(n).",
      "basis": "Board 301 reports nonempty local-optimal gaps at n=6 and n=7 with information excess E=0, with independent reruns confirming the gap values, alongside adjacent tightness fronts bracketing the information-bound question."
    }
  ]
}
```

**Curator report / honest limits:**

- **Study:** `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-plan.md`, `docs/literature.md`, `docs/research-strategy-certificates.md`, `docs/research-budgeted-dfs.md`, `docs/research-hardness-boundaries.md`, the frontier ledger (`research_frontier.py` + state), and the Antonina board #301 digest/pages.
- **Attack / context this turn:** the live question cluster is the L(n) program (`L-upper-nlogn-alln` outcome (c), `L-lower-beyond-factorial-alln` outcome (c), `Ltree-Lloc-gap-alln`), the local-vs-global optimal-play correction (DAG(all) ⊊ L_tree via zero-progress/slack moves), `uniform-tc0-sortbound-membership`, `optimal-play-deck-class-polynomial`, `info-bound-gap-invariant-alln`. Independently re-verified facts used as basis: gap counts |L_loc(6)|=65551, |L_tree(6)|=66991, gap 1440; |L_loc(7)|=2769663, |L_tree(7)|=3044007, gap 274344; information excess E=0 at n=4,5,6,7.
- **Proposed front:** `tight-n-state-gap-alln` — all-n infinitude of an optimal-state gap restricted to information-tight n. Rationale for proposing it now: it is a *quantifier-scoped sharpening* of the already-investigated infinitude question, grounded in the newest board computations and the adjacent tightness fronts; it is falsifiable (coincidence at large tight n, or explicit infinite tight-n gap family).
- **Honest limits:** no proof and no verification is claimed or implied for the front; the falsifier is conditional and the answer is open. The adjacent general-poset results and certificate soundness (deck/F-soundness, all-minimax completeness) are not conflated with this reachable-state question. No Lean, repository, test, workflow, ledger, or `main` change was made; no board post was made by this session; scratch was confined to `/tmp/opencode`.

**Deliverable:** `{"fronts": [...]}` — single candidate front written to the requested path, validated against the keeper's schema (id `tight-n-state-gap-alln` ok, all four text fields above their minimum lengths, no extra keys). No commit, no tracked-file change (the file is untracked as expected for curator output).

# antonina-JtEqwYwTRTnMYFgWq5oz8w-principal

Session: ses_e0b33306bffet5P8xIA09pI22H
Workspace: /home/lubko/soring-fronts/curator
Created: 1795108425628; updated: 1795108688468

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f4cccfb4001YKtuRgHNsEX4iH)

I'll start by understanding the repository state and the key documents.

## Output 74 (msg_1f4cd2fb2001qcM1MvLSPtGgro)

Now let me read the research board #301 digest as instructed.

## Output 299 (msg_1f4d00039001b9EgBXUKb4lxpG)

I have enough grounding now. Let me verify a couple of candidate topics are truly absent from the 566-front ledger before writing.

## Output 319 (msg_1f4d07929001H772kWnQ1j01Tx)

Now I'll write the curator output with three genuinely new, non-duplicate fronts.

## Output 348 (msg_1f4d0ba17001B4Sdqt2uwhbhoo)

Done. I wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` — a single JSON object with a `fronts` array of three new, non-duplicate candidates.

**What I did**
- Confirmed the host context (`billy-dev` is the execution host, not a git branch; worktree otherwise clean, no commits).
- Studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the certificate/barrier/winning-frontier/hardness notes, all 566 ledger fronts, and board #301 (pages 1–7, including the 17:13Z dispatch and the 16:51Z local/global correction).
- Checked each proposed topic against the full ledger and the 20 previously investigated fronts; all three are absent.

**The three fronts** (schema-validated: slug 6–63 chars, question ≥75, other fields ≥40/35):
1. `uniform-tc0-sortbound-membership` — first small-uniform-circuit-class question for the tally sequence; grounded in `ceil(log2 n!)` being in uniform TC⁰ with only the o(n) excess at issue.
2. `globally-feasible-locally-nonoptimal-barrier` — turns the board's 16:51Z `L_loc(6)=65551` vs `L_tree(6)=66991` witness into an all-n soundness-vs-completeness barrier question for locally-minimax certificate grammars.
3. `sorter-refuter-duality-np-conp` — asks whether NP-style sorter certificates and coNP-style refuters are dual or decoupled, distinct from the already-investigated `adversary-cert-completeness-conp`.

**Honest limits:** no proof, verification, or theorem is claimed; these are falsifiable questions with proposed falsifiers only. The deterministic fine-grained/SETH route was considered and dropped — a tally sequence's answers are instance-independent, so the usual sparsity barrier blocks such reductions. No Lean, note, test, ledger, commit, or other repository change was made; the JSON is the sole new artifact (untracked, as expected for curator output).

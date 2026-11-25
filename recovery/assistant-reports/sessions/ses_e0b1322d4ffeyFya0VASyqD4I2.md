# antonina-e2pZKW6DmKiHLkDtidEmKy-distress

Session: ses_e0b1322d4ffeyFya0VASyqD4I2
Workspace: /home/lubko/soring-fronts/curator
Created: 1795110526260; updated: 1795110779497

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f4ecdd6a001LLsm05QaC2FXt4)

I'll start by verifying the current branch and reading the key documents in parallel.

## Output 29 (msg_1f4ecf079001NY6OParFzciCrA)

I'm on branch `main`. The instruction says "On billy-dev ONLY" — let me check whether billy-dev is a host, branch, or worktree, and check the board digest.

## Output 44 (msg_1f4ed06e2001YXQ7mjnKI8SKjR)

Host is `billy-dev` (confirmed). The curated worktree is on `main`; that's expected — isolated front checkouts use a `billy-dev` branch. Now let me gather the current frontier ledger, existing candidates file, and a fuller board digest.

## Output 81 (msg_1f4ed3cb20019D8oXb6oW3OMUL)

Let me check the full frontier ledger to avoid duplicates and read the key research docs.

## Output 144 (msg_1f4edb63c001cDz2odTm8CeY7L)

The ledger has 569 fronts covering almost everything. Let me inspect the board digest mechanism and read the newest messages in full to find genuinely new angles.

## Output 178 (msg_1f4eeaab0001m9x7ZYLOaZ7lMR)

Let me check the ledger for specific new concepts from the newest board to avoid duplicates.

## Output 198 (msg_1f4ef06a5001g22xAVNVmzBCHW)

Let me verify non-duplication for a couple of concrete new angles I'm considering.

## Output 209 (msg_1f4ef5acc001xDVDxKS7x59yKx)

Let me read the budgeted DFS derivation and the strategy-certificate definitions to ground a concrete evaluator question.

## Output 238 (msg_1f4ef978f001qxMMJf04a0tsgp)

I've identified several genuinely new angles. Before writing the JSON, let me do an independent from-scratch computation to ground one of them — testing the conjecture that global information tightness forces the minimax-only/global-feasibility gap to vanish (which board n=6 data appears to refute).

## Output 249 (msg_1f4effcb9001rfMp3EDpfKzzBL)

My independent from-scratch minimax reproduction confirms the key n=6 fact (E(6)=0 yet a 1440-state gap), refuting the natural "global tightness ⟹ no locally-nonminimax states" conjecture. Now I'll write the curated fronts.

## Output 260 (msg_1f4f075f1001s1ElkPZ0IHQ66L)

Let me validate the JSON schema and all field constraints.

## Output 271 (msg_1f4f094910014hAtQh4SPlRQh1)

Done. Summary of this curator pass on `billy-dev`:

**What I studied.** `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, the full newest messages of board #301 (not just the digest), the strategy/budgeted-DFS/encoding docs, and the live 569-front ledger. The host is `billy-dev`; the curator worktree is on `main` at `f89f6d0` (front agents use the `billy-dev` branch in isolated checkouts), so this is the correct host.

**Claim I attacked and the honest outcome.** I tested the natural conjecture that global information tightness `E(n)=S(n)−⌈log₂ n!⌉ = 0` forces `L_tree(n) = L_loc(n)`. With a from-scratch bitmask transitive-closure + memoized exact-minimax implementation (scratch only, `/tmp/opencode/curator_check`), I reproduced `S(4,5,6)=5,7,10`, `E(4)=E(5)=E(6)=0`, `|L_loc|=181/1551/65551`, `|L_tree|=181/1551/66991`, and `L_loc ⊆ L_tree`. The n=6 case (`E(6)=0` yet a 1440-state gap) is a genuine finite **counterexample** to that conjecture. Limitations: this is finite evidence, not an all-n theorem; no value of `S(n)` changed, `S(23)` untouched, no complexity separation, and no connection from general-poset hardness was assumed.

**Soundness vs completeness / general-poset discipline.** I kept the new fronts on the fixed antichain sequence and did not transfer arbitrary-poset or GEN-SORT hardness. The certificate questions are framed around soundness/completeness distinctions from the newest board, not as claimed proofs.

**Deliverable.** Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` — a JSON object with a `fronts` array of 3 new, non-duplicate all-n questions:
- `verif-adv-conp-hardness-barrier` — is VERIFY-ADV coNP-complete (barrier from newest B2)?
- `all-minimax-promise-verification-np` — can the new all-minimax completeness theorem yield a poly-size verifiable NP certificate?
- `global-excess-vs-local-slack-gap-alln` — conditioned on `E(n)=0`, is the `L_tree/L_loc` gap driven by local slack, and does it persist/grow?

Schema and all length constraints validate; none is an exact textual duplicate of a ledger front. No Lean, test, workflow, ledger, or other repository change was made — `git status` shows only the required `frontier-candidates.json`. No proof or verification is claimed for any front.

# antonina-OfQ1xAMiyEMC3JkuX3R8oz-margins

Session: ses_e044e1795ffenKV2E0s7RTWmTQ
Workspace: /home/lubko/soring-fronts/signflip-cross-rule-optimality-alln
Created: 1795224103043; updated: 1795224826981

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 440 (msg_1fbbb3a35001mXVHz9YtNnK0CF)

I'll first audit what actually happened before continuing — no external writes until I know the state.

## Output 482 (msg_1fbbc74ae001Za1mMiunvq6tlr)

Audit complete. Here is the state and the finding.

## Side-effect audit (before continuing)

- **Git:** branch `billy-dev`, clean at `6a96398`; no commits, diffs, or repo/Lean/test/ledger changes.
- **Board #301:** all 7 pages fetched; newest post is `01:19:31Z` by the *previous* front (`exec-signflip-adversary-alln-20261121`). **No post was made by this session**, and none under this front's ID.
- **Ledger:** front `signflip-cross-rule-optimality-alln` is `running` (agent `OfQ1xAMiyEMC3JkuX3R8oz-margins`), no finding recorded; sibling front `cross-charge-merge-information-alln` is live and was not touched.
- **Only local effects:** scratch scripts `/tmp/opencode/adv/rerun_signflip.py`, `/tmp/opencode/adv/diag24.py`; read-only Antonina queries. **I am not posting to #301** — the finding is reported here to avoid any duplicate external action.

## Mathematical finding — falsifier for the sign-flipped cross rule

**Claim attacked** ([definition], from the front and #301 `00:32Z`): for every disjoint composition `A ⊔ B`, the sign-flipped adversary — cross answer maximises `F(N|_A)+F(N|_B)−k`, within answer maximises `F(N|_comp)−k`, `k` = newly determined cross pairs — is an *optimal adversary*, i.e. forces exactly `F(A⊔B)`.

**Falsifier (independently recomputed, [experiment] + [literature]):** take the reachable composition `A_2 ⊔ A_4 = A_6`, i.e. the 6-element antichain root split 2+4. Since `F(A_6) = S(6) = 10` is established ([literature], kernel-checked in the repo), no evaluator trust is needed for the target.

| tie-break | forced depth `H` | `F(A_6)` | verdict |
|---|---|---|---|
| `first` | **9** | 10 | **strictly suboptimal** – adversary fails to force the minimax value |
| `smaller_e` | **9** | 10 | strictly suboptimal |
| `larger_e` | 10 | 10 | optimal |
| `larger_global_F` | 10 | 10 | optimal |

An explicit 9-comparison transcript against the `first` variant was reconstructed (9 steps, ending at a total order). The defect target `F(A_2)+F(A_4)+2+1 = 9` is still forced in every variant, so the defect inequality itself is untouched.

**Localized failing step ([experiment]):** in the `first` play, the last divergence is a *within*-component query `(3,5)` whose two answers score `1` versus `2` under `F(N|_comp)−k` (`k = 2` vs `0`, i.e. transitivity through the component determines two cross pairs). The rule takes the higher score; earlier steps also contain score-ties where `first` picks the wrong branch. This is the within-component leak identified in the `00:32Z` finding, now exhibited at the antichain root itself.

## Honest limits

- This is a **finite counterexample to universal optimality (with plain tie-breaks)**, not an all-n theorem and not a proof that no tie-break works. The board's `01:19Z` C1/C2 report of a *strict* score mis-ranking (no tie-break repairs it) I did **not** re-verify independently; Viche corroborated parts of it.
- The successful tie-breaks `larger_e`/`larger_global_F` are confirmed optimal only on the tested disjoint unions; **no all-n justification** exists. Universal sign-flip optimality therefore remains unestablished; strategy-specific cross rules are still required.
- **No complexity consequence:** this is a structural statement about the minimax game. It does not change `SORT-BOUND-U ∈ PSPACE`, does not give a uniform cross-charge strategy for exact unary evaluation, and yields no NP/coNP certificate. No Lean file was added.

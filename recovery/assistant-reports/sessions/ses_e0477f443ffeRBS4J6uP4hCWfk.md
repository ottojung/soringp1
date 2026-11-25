# antonina-Sdo4Gh7aAxp3gsNZP5dH7U-tremble

Session: ses_e0477f443ffeRBS4J6uP4hCWfk
Workspace: /home/lubko/soring-fronts/curator
Created: 1795221359562; updated: 1795221601003

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fb880c17001xlUiRT8ftCgqCt)

I'll start by orienting myself: verifying the branch, reading the key docs, and discovering how the board (#301) is accessed.

## Output 29 (msg_1fb881d53001o4M8ZFyvP7WMp4)

We're on `main`; let me verify the host is `billy-dev` and learn how to read board #301.

## Output 44 (msg_1fb883806001HrsNz49Jh3LWRA)

Host confirmed as `billy-dev`. Let me pull more of board #301 and the existing frontier definitions to avoid duplicates.

## Output 72 (msg_1fb885c3d001uAsN0EcCNEZSer)

Let me extract the full ledger to understand what's already been explored and avoid duplicates.

## Output 83 (msg_1fb888076001k4T5oTrgNJoOpz)

The frontier is extremely mature (621 fronts). Let me read the newest board posts in full and check what research files exist, so I can ground my investigation precisely.

## Output 98 (msg_1fb88c816001n7S4i8FODpfL2e)

The frontier is near-saturated. Let me verify whether the newest board themes (disjoint-union defect pruning, adversary composition) already have dedicated fronts, and look at the research status tooling.

## Output 109 (msg_1fb8969eb001JdAxuTS1TD8kkM)

I've confirmed the frontier is essentially saturated (621 fronts, last curator emitted 0, Viche corroborated depletion). Still, I'll do a genuine independent mathematical attack on a precise all-n complexity claim before deciding the curator output. Let me build a scratch exact evaluator and test a candidate "information-greedy = optimal" claim from scratch.

## Output 138 (msg_1fb8b48290018EU9maixPreH5c)

I've completed a genuine independent attack. Let me verify the result is stable and confirm no repo changes, then write the curator output.

## Output 165 (msg_1fb8b9c86001TEpX5AmWCZLHCP)

## Report

**Host/branch:** `billy-dev` (confirmed via `hostname`), on `main` at `f89f6d0`. No Lean, note, test, ledger, CI, or board changes were made; scratch work lived only in `/tmp/opencode/gattack/`. The sole new file is the required curator output `frontier-candidates.json`.

### What I studied
- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md` — the model, unary encoding, established `2^{O(N log(N+2))}` time / PSPACE upper bound, sparsity/P/poly barriers, and the "soundness ≠ completeness", "general-poset ≠ root-reachable" caveats.
- Board #301 digest (full newest posts, 11-20T23:44Z → 11-21T00:32Z) plus the primary-literature leads (Peczarski; Stober–Weiß; Mahaney; Ford–Johnson).
- The full 621-front ledger.

### The claim I attacked (and seriously tried to disprove)
**Claim (all-n):** *At every poset state reachable from the n-antichain, there exists an F-optimal comparison that is also "information-greedy," i.e. it minimizes `max(e(child⁺), e(child⁻))` where e = number of linear extensions.* This is a clean complexity claim: if true it would give a deterministic, locally-computable rule for selecting an optimal move (a step toward a compact evaluator/certificate).

I built a from-scratch evaluator (transitive-closure successors, subset-DP linear-extension count, exact memoized minimax F, brute-force canonicalization), validated `S(n)=0,1,3,5,7,10` for n=2..6, and enumerated **all** reachable states through n=6 (63, 318 states — these coincide with the unlabelled-poset counts A000112(5)=63, A000112(6)=318, so every poset on ≤6 elements is reachable).

**Outcome (experiment, not proof):** The strong "no info-greedy move is F-optimal" disproof **never occurs** through n=6 (0 violations at every n). The weaker "every info-greedy move is F-optimal" variant **does fail** at n=5 (2 states) and n=6 (14 states), but only via ties. So I did **not** disprove the claim; the finite data are consistent with it, and the tie-failures are not counterexamples to the existence form. Honest limit: n≤6 only; canonicalization cost blocked n=7 within budget; and the claim is, on inspection, already covered by existing fronts (`onethird-twothirds-exact-minimax`, `depth-extension-balance-coexistence-reachable`, `greedy-adversary-sufficiency-alln`, `no-e-p-only-dp-exactness-barrier`). It yields **no** new result about `S(n)`, no complexity-class membership, and no soundness→completeness or general-poset→antichain transfer.

### Curator decision
The frontier is genuinely saturated: 621 fronts (600 investigated, 21 blocked), the previous curator emitted 0, and Viche's 00:23Z pass independently corroborated depletion across theorem obligations, literature, and the night's failed approaches. The newest board themes (disjoint-union defect, transitivity-aware cross rule, adversary composition, pruning lower bound `exec-defect-prune-exponent-20261121`) are either already-investigated fronts or actively dispatched. My own independent check produced only phenomena already covered by existing fronts. I therefore found **no defensible, non-duplicate all-n direction** and wrote the required explicit empty outcome:

```json
{"fronts": []}
```

No proof, verification, or class-separation is claimed anywhere in this report.

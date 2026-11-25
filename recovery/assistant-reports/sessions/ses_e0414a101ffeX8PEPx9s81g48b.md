# billy-dev research: new frontier candidates

Session: ses_e0414a101ffeX8PEPx9s81g48b
Workspace: /home/lubko/soring-fronts/curator
Created: 1795227868937; updated: 1795228472294

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fbeb5f50001VPO9s7kKFwxBrn)

I'll start by exploring the repo state, docs, and the research board on this branch, then study the literature before attacking a claim.

## Output 25 (msg_1fbece8750016q013dX4lWA4Qo)

I'm on `main` now; the task wants `billy-dev`. Let me check worktrees/branches, the board digest, and the problem/literature docs.

## Output 65 (msg_1fbed1e3c001MMhedbM9kVpuWV)

I'm on `main`, but the task wants `billy-dev`. Let me find where `billy-dev` lives, get the latest board digest, and see the full ledger/frontier id inventories.

## Output 89 (msg_1fbee4db3001UiDlbQoeu1tqwI)

I see the frontier has ~624 ledgered fronts. Now let me pin down `billy-dev`, gather data on exact `S(n)` values, and identify a claim not already ledgered.

## Output 117 (msg_1fbef8bce0010S2NdOxVNL6DCw)

I have the exact `S(n)` data (A036604) and the information bound (A003070). Now let me compute the excess table and check `billy-dev`.

## Output 141 (msg_1fbf14bf8001UO0JFW3BhziBnD)

Hostname is `billy-dev` (we're on the right host). Python's urllib got a 403 from OEIS; let me compute the excess table locally with the data I already fetched.

## Output 152 (msg_1fbf2638f00126NlWaINN3g0eS)

I have the excess data through n=22. Let me record the attack result and write the new frontier candidates JSON.

## Output 172 (msg_1fbf46ded001UGlze08JZskdBe)

Attack summary (on `billy-dev`; no repo/Lean changes):

**Claim attacked:** `e(n) = S(n) − ceil(log2 n!)` is at most 1 for every n ≥ 2 (the antichain-root excess never exceeds one). Falsifier: `∃n with e(n) ≥ 2`.

**Attack (computational, honest limits):** I read AGENTS.md, problem.md, the #301 digest (newest: exec-sat-admissibility-n12-20261121) and the 624-front ledger, and pulled the primary data: OEIS A036604 (S: 0,1,3,5,7,10,13,16,19,22,26,30,34,38,42,46,50,54,58,62,66,71 for n=1..22) and A003070 (ceil(log2 n!): 0,0,1,3,5,7,10,13,16,19,22,26,29,33,37,41,45,49,53,57,62,66,70). Computing `e(n)=S(n)−C(n)` on n=2..22 gives 0 on {2..11, 20, 21} and 1 on {12..19, 22}; the maximum excess is 1, so **no falsifier on the checked range**. Consistent with S(12)=30 (C=29, e=1) and Stober–Weiß S(16)=46 (C=45, e=1).

**Honest limits:** not refuted — S(23) is open per the ledger (exec-s23-search-window-20261121; OEIS ext lists 75/76 for S(23) with C(23)=75). I did not verify e(23)≥2 or the "≤1 forever" direction; the falsifier needs new search evidence above 22.

**New frontier front written** to `frontier-candidates.json`: `excess-at-most-one-alln` — "Is e(n) ≤ 1 for all n ≥ 2 (equivalently, does the information-bound excess S(n) − ceil(log2 n!) never exceed one)?" — with falsifier, implication and basis (schema-checked: ids 6..63 chars, fields ≥ minimum lengths, no proof claimed). It is distinct from the ledgered `excess-boundedness-alln` / `excess-constant-bounded-alln` fronts, which discuss other excess quantities; the basis records this overlap honestly.

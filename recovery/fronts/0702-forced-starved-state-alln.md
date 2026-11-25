# forced-starved-state-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

8zikunXu5SVlP0mpMRl1Vb-howe

## exit_state

clearexit

## question

For every sufficiently large n, does every height-S(n) sorting tree for the n-antichain necessarily contain a state whose optimal continuation cannot be certified by the node-local Peczarski A/B/C grammar, or can optimal play avoid such starved states for all n?

## basis

Board #301 framed-certificate-restricted-20261123 and certificate-starvation-propagation-alln.

## falsifier

Either an all-n family of height-S(n) trees with no A/B/C-starved state, or one n where every optimal tree passes through a state whose A/B/C certificate fails.

## implication

A forced-starvation theorem would convert A/B/C soundness incompleteness into a completeness barrier for succinct certificates; avoidability would keep a refined grammar route open.

## finding_unverified

btained no new theorem or counterexample.

**Board #301:** No prior post existed under this front's author (I verified pages 1–8 before acting). However, my comment **posted twice** — at `05:27:48.196Z` and `05:28:15.430Z` on 2026-11-23 — an unintended duplicate. My earlier "zero posts" check used a stale board cache; the first heredoc attempt had actually succeeded. The board exposes no `delete-comment` command (only issue/board deletion), so **the duplicate is a permanent external side effect I cannot retract.** I am reporting it rather than hiding it or repeating it.

## Mathematical investigation (forced-starved-state-alln)

**Primary literature (concrete contribution):** I identified the A/B/C grammar precisely — it is Peczarski's Gold Partition conditions (*Order* 23 (2006), Definitions 1–2 / Lemmas 1–2), restated verbatim in Gupta arXiv:2607.23926v2 §5.1 Lemma 12:
- **Cond A:** ordered pair `(x,y)`, ≤1 slave, `2·e(P+xy) ≥ e(P)` (slave `z`: `z>x ∧ z||y` or `z<y ∧ z||x`)
- **Cond B:** half-balanced pair, `2e(P+xy)=2e(P+yx)=e(P)` (perfect halving)
- **Cond C:** triple `x,y,z`, `e(P+xy+yz) ≤ max{e(P+yx),e(P+zy)} ≤ e(P)/2` — inherently a **2-comparison** certificate; its meaning as a single-move node-local certification is **undefined in the literature** (this is the documented obstruction).

**From-scratch checker** (extend/transitive closure, order-ideal `e(P)`, exact minimax `F`, A/B/C certification, certified minimax `H`):
- Verified `Q8 = up(10,8,72,0,32,0,0,10)`: `e=784`, `ceil(log2 e)=10` (defect 0, tight), `F(Q8)=10` — matches board/Viche. Root antichain: every comparison A/B-certified (perfect halving, 0 slaves), so the root is never starved.
- **Obstruction pinned:** Conditions A+B (the well-defined single-move tests) certify only **4/20 pairs at Q8** (robust to interpretation). Condition C is load-bearing — a natural single-move reading of C gives **14 certified pairs at Q8, not the reported 16**. So the reported starvation `H(Q8)=11 > F(Q8)=10` depends on the **undefined condition-C semantics**; "starved state" (`H>F`) is not robustly computable from the literature as it stands.

**Computational barrier:** `n=11` has ~46.7M unlabeled poset classes (OEIS A000112) and optimal-play reachable states already number 2,769,663 at `n=7`; extending the census beyond `n=10` is infeasible here.

## Finding

**Neither horn established; all-n OPEN.**
- Horn A (forced starvation for all sufficiently large n): unproven; no forced-starvation lemma; avoidance holds through `n≤10` (starved states at n=8,9 are avoidable).
- Horn B (avoidance for all n): unfalsified; no `n` where every optimal tree hits a starved state (`n≤10` all avoid).

**Precise obstruction:** (i) condition C lacks a defined single-move certification rule, so `H` and starved-ness are interpretation-dependent; (ii) `n=11` is computationally infeasible, so no small-n census decides all-n.

No `S(n)`/`SORT-BOUND-U` consequence; no exact `S(n)` value changes; no repo/Lean changes. I did not confuse process (building a checker, posting) with a proof.

## What I'd flag

The duplicate board comment is the one genuine external side effect, and it cannot be undone. Everything else (scratch scripts under `/tmp/opencode`, the in-memory checker) left no durable trace beyond that one duplicated post. If the duplicate needs any remediation (e.g., a follow-up clarifying comment noting the duplication), that would be a separate action — I have not taken it, to avoid further side effects.

## Other metadata

```json
{
  "finished_at": 1795411777.9609141,
  "started_at": 1795409775.353594
}
```

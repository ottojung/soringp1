# antonina-HSB0DYLfxvMzh8T0ZZ9Rka-organ

Session: ses_e4af08f66ffeebJSGPbu62C478
Workspace: /home/lubko/soring-fronts/exec-s23-bidirectional-20261107
Created: 1794039050457; updated: 1794039128435

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b50f72ce001i11t7lDwcCQmpv)

I’ll first inspect the requested research documents and existing search implementation/tests, then trace the paper’s exact recurrence and available run evidence. I’ll keep this read-only unless a small, clearly bounded validation is justified.

## Output 102 (msg_1b50fe8f3001eOeOSktqY44Nrh)

The primary paper gives enough to audit the extension, but its run table has no n=23 calibration. The board digest also shows a same-day n=23 assignment and explicitly warns against a mistaken threshold-to-lower-bound inference; I’m checking that evidence and the numerical bounds before giving a conclusion.

## Output 125 (msg_1b5102cfa001iEcuDjQEhP8ZF7)

## Conclusion

**No credible n=23 lower-bound run or independently checkable new integer lower bound was established.** The paper’s method is mathematically applicable at n=23, but extending it is an implementation-and-resource problem, not a gap in the coverage lemma. The strongest evidence-based result here is a quantified feasibility warning—not a theorem that the method cannot scale.

### (a) Published interval

The best published interval is **75 ≤ S(23) ≤ 76**:

- **Lower bound 75:** the information bound \(C(23)=\lceil\log_2(23!)\rceil=75\). Stober–Weiß state this bound and define the model in §1 of [arXiv:2206.05597v2](https://arxiv.org/abs/2206.05597).
- **Upper bound 76:** Ford–Johnson merge-insertion; see the paper’s §1 and the primary references it cites. The repository’s literature baseline records exact values through 22 and n=23 as open.

Thus the unresolved question is whether **75 comparisons suffice**. No exact value is claimed.

### (b) Translation and assumptions audit

For a proposed lower bound, set \(C=74\): the decision question is whether the antichain \(P_0\) is sortable in at most 74 comparisons. At depth \(c\), the forward recurrence is
\[
S_c(P)=\bigvee_{\{u,v\}\text{ incomparable}}
\left(S_{c+1}(P+u<v)\land S_{c+1}(P+v<u)\right),
\]
with total orders as success states at depth \(C\). To prove \(S(23)\ge75\), the exhaustive forward search must show \(S_0(P_0)=\mathrm{false}\).

In the backward pass, level \(c\) represents states sortable in at most \(C-c\) comparisons. Starting from total orders at level \(C\), enumerate potential predecessors by deleting Hasse edges and testing the reverse-outcome state. The paper’s Lemma 4.1 justifies the Hasse-edge-count pruning: a forward-reachable winning state after \(c\) comparisons has at most \(c\) Hasse edges.

For partial backward search, choose \(C_f\), do full layers \(c\ge C_f\), and retain earlier-layer states only when
\[
E(P)=\frac{23!}{2^c e(P)}\le E_{\rm thr},
\qquad E_{\rm tot}=23!\,2^{-74},
\qquad E_{\rm tot}\le E_{\rm thr}<2E_{\rm tot}.
\]
Lemma 4.2 then gives the required coverage: a forward-reachable winning state with \(E(P)\le E_{\rm thr}\) is in the corresponding partial backward layer. Therefore, **absence is a sound NO only for states within the threshold**; an entry marked unknown must be explored. Outside that covered region, absence proves nothing.

The argument assumes exact linear-extension counts, exhaustive predecessor enumeration, and a correct congruence quotient (isomorphism or dual-isomorphism preserves sortability). The paper’s implementation uses hashing/color refinement with an isomorphism fallback for ambiguous representations; that implementation detail must not introduce false identifications. Its pair-ordering heuristic is justified by comparison commutation. None of these statements supplies a resource bound for n=23.

### (c) Feasibility evidence and stopping point

The paper’s Table 2 reports:

- \(n=16,C=45\): 11 hours, \(3.99\times10^9\) stored posets;
- \(n=17,C=49\): 115 hours, \(13.2\times10^9\);
- \(n=18,C=53\): 89 hours, \(10.0\times10^9\);
- \(n=28,C=98\): 10 hours, \(30.2\times10^6\), **without partial backward search**.

The n=28 result is not a scaling point for the n=23 target: it proves only \(S(28)\ge99\), uses the information-bound budget, and its table lists no partial-backward layers. The n=16–18 runs concern budgets one below their exact values, with substantial partial backward passes. The paper reports 48 threads, 768 GB RAM, 4 TB NVMe plus 12 TB disk; times and stored-poset counts are not sufficient to infer n=23 layer sizes or runtime. The authors also note in §6 that more explored backward posets can cost more than fewer forward posets.

The local `scripts/bidirectional_advice.py` is only a toy prototype (n≤5): it does not implement the efficiency threshold, congruence reduction, or predecessor enumeration, so it cannot validate n=23 performance.

I checked the available #301 digest. It records a same-day n=23 assignment that **made no search run**, and explicitly withdraws an invalid inference from a partial-state threshold to a root lower bound. That is relevant caution, not evidence of a new bound. I found no verified n=23 layer/table measurements to add.

**Specific next computation:** a defensible feasibility test would run the actual Stober–Weiß implementation on \(n=23,C=74\), first instrumenting per-layer generated/stored counts, peak resident memory, predecessor-generation time, and exact linear-extension workload on an explicitly capped run. Acceptance for a lower-bound claim must be a completed exhaustive run showing the root absent, with versioned source, parameters, resource log, and an independent checker or reproducible validation. Until such a run yields measurements, extrapolating the published timings to n=23 would be speculation. No repository changes or board post were made.

## Output 144 (msg_1b5109963001l1H98MdjtbVqh2)

No external side effects occurred. Git worktree is clean at `c865b239`; no commits, files, or board posts were created. The entire result of the prior turn was delivered as a chat report only.

Nothing remains unfinished. The conclusion stands: no new S(23) lower bound was established; the paper method is applicable but unverified at n=23 due to missing implementation/resource evidence. No further action needed unless you want the concise #301 update prepared for independent review.

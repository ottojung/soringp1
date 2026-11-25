# antonina-dFEKNMQ86xisNI974I1uGJ-splint

Session: ses_e47eda0dcffe4M3H5jpsCBWnyq
Workspace: /home/lubko/soring-fronts/exec-lemmaA-balancing-20261107
Created: 1794089574285; updated: 1794091355240

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b8126192001paWAB2S4nB03sS)

I’ll treat this as a paper-proof-first investigation, then check relevant literature and—if feasible—run a bounded independent exact search. I’ll make no repository or board changes.

## Output 38 (msg_1b8127764001X1RbDpJanZYE5F)

`docs/research-core-reduction.md` is absent in this checkout, so I’ll note that gap rather than infer its contents. I’m now checking whether the proposed Fibonacci induction actually follows from Lemma A, and looking for transferable results on balanced comparisons.

## Output 74 (msg_1b8129d1f001JvtqCBQ9GdqTBx)

The implication to the Fibonacci lower bound needs a small correction: at a node of depth `m`, Lemma A supplies child depths at least `m−2`, but that alone does not give the claimed induction unless those child depths also meet the required Fibonacci indices; since `F_{m}` is the target for depth `m−2`, this part does work, with `e(P)=e_1+e_2`. The base cases still require explicit handling of depths 0 and 1. I’m focusing next on the direct lemma, especially the optimal-comparison branch split.

## Output 125 (msg_1b812d9e3001D6sxPtKrcpJ4NO)

## Result

**No proof or counterexample found. The exact blocking case is the one-sidedly unbalanced optimal comparison.** For an optimal pair \(\{a,b\}\), the child depths have maximum \(m-1\), but I could not rule out that the other child has depth at most \(m-3\), nor prove that another comparison has both children of depth at least \(m-2\). This is the case that must be resolved to establish Lemma A.

The requested `docs/research-core-reduction.md` is **missing** from this checkout; I read the current `AGENTS.md`, `docs/research-plan.md`, and the closely related `docs/research-obstruction-next.md`.

## Proof attempts and induction check

- **Contrapositive:** If every incomparable pair has a child of depth at most \(m-3\), that gives a cheap branch for each first comparison. But the other branch may still have depth \(m-1\); I found no way to use the cheap branch to construct a strategy of depth \(m-1\). The key gap is coordinating choices across those deep branches.
- **Optimal-pair exchange/rotation:** Starting with a pair whose deeper child has depth \(m-1\), an alternative first pair could potentially balance the depths. I found no exchange argument ensuring one does.
- **Median-rank element in the deep child:** A median-rank comparison can balance the *linear extensions* of that child, but depth is not determined by extension count. The known equal-extension/different-depth examples in `research-obstruction-next.md` block that inference.
- **Strategy-tree induction:** The optimal tree certifies an \(m-1\)-depth child, not the existence of a different root comparison with two sufficiently deep children. I found no tree transformation that supplies one.

The proposed Fibonacci implication does follow **assuming Lemma A**. For \(m\ge2\), the two child depths are at least \(m-2\), so induction gives at least \(F_m\) extensions per child, hence \(e(P)\ge 2F_m\ge F_{m+2}\). The last inequality is \(F_m\ge F_{m-1}\). Depths 0 and 1 are base cases: a total order has \(e=1=F_2\), and a depth-1 poset has at least two extensions, meeting \(F_3=2\). Thus the Fibonacci deduction does not appear to be the obstruction; proving Lemma A is.

## Literature: what transfers, and what does not

The most directly relevant checked source is Kahn and Saks, *Every poset has a good comparison*, STOC 1984, pp. 299–301, DOI [10.1145/800057.808694](https://doi.org/10.1145/800057.808694). As summarized in `research-obstruction-next.md`, it gives a comparison whose outcome probabilities lie between \(3/11\) and \(8/11\). This balances **linear-extension counts**, not minimax depths, so it does not prove Lemma A.

Hanamura and Iwata, *Posets with seven linear extensions sortable by three comparisons*, *Information Processing Letters* 111(8) (2011), 365–369, DOI [10.1016/j.ipl.2011.01.004](https://doi.org/10.1016/j.ipl.2011.01.004), establish a small-extension threshold. That is a bound from extension count to sorting depth, not a general balanced-child theorem.

The repository’s literature audit also cites Brightwell–Winkler’s #P-completeness result for counting linear extensions. It concerns extension counting, not minimax comparison depth. Peczarski’s sorting-number work and the cited merge results concern adaptive comparison sorting, but I found no result there that implies the two-child depth balance in Lemma A. The fence/Fibonacci connection motivates the conjectured bound; it is not evidence that every poset has a balanced comparison.

## Falsification search and next obstacle

I did not run the requested larger search: the available `scripts/obstruction_probe.py` enumerates all posets and has no small-extension cap or independent second minimax implementation. Extending it responsibly would require a separately checked bounded-search implementation; I cannot report hashes or completeness for an experiment not performed.

**Blocking case:** An optimal comparison may have child depths \(m-1\) and \(\le m-3\). The missing argument must either show that some other incomparable pair has both child depths at least \(m-2\), or derive a depth-\((m-1)\) strategy despite that split. No proof or counterexample is established here.

## Output 149 (msg_1b8133f8f0018ZqCHF6PySw2rW)

I’ll first verify what the interrupted turn actually changed, then continue only the unfinished mathematical/search work.

## Output 172 (msg_1b81433ff001pFkdHpwTC7QYaM)

The worktree is clean and `HEAD` is detached at `c865b23`; no commits or edits were made by the interrupted turn. The only external action was a read-only DOI lookup, which needs no retry. I’ll now continue the unfinished lemma analysis and bounded exact checks, keeping all scratch work in `/tmp`.

## Output 247 (msg_1b82415c00017YpIatorhWU8Zw)

The bounded checks have now run through all 130,023 six-element labelled posets, with no Lemma A counterexample. A larger fence probe completed through size 8 but was killed by resource limits at the next size; I’ll record that only as a partial experiment and verify the repository is still untouched.

## Output 264 (msg_1b82d60c7001x2VopXmQwbyxzg)

## Recovery check

**No external side effects were found.** The repository remains clean at detached `HEAD c865b23`; no commits, board posts, or repository edits were made. The only earlier external request was a read-only DOI lookup. Scratch scripts and results are in `/tmp`.

## Research status

No proof or counterexample to Lemma A was established. The unresolved case remains an optimal comparison whose child depths are \(m-1\) and at most \(m-3\): I found no argument forcing another comparison to have both children at least \(m-2\).

**Bounded exact experiment:** Exhaustive enumeration of all 130,023 labelled posets on six elements found no violation. The independent scratch probe `/tmp/lemmaA_probe.py` uses the repository’s exact minimax recurrence and reports zero violations. Its SHA-256 is `4bb0cf4d2a53f98dc0f1458220e1d4a97e9680fd76f7860f463bacf356778e9c`. This is a finite experiment, not evidence for the all-posets claim.

The separate fence probe completed sizes 2–8, also with no violation at applicable depths. It was killed by resource limits at size 9, so that range is incomplete. `/tmp/fences.py` SHA-256: `411446a19dcc6f81d47f0d869bb70697ea90f4ab7d32b9ed113de87b2c3f652e`.

I attempted an additional size-7 search restricted to \(e(P)\le200\), but it timed out before completion; **no completeness claim or result is available** for that run. The requested `docs/research-core-reduction.md` is absent in this checkout.

The Fibonacci induction follows from Lemma A with base cases \(m=0,1\), as described in my previous response. The direct-proof attempts and literature transfer limits are likewise unchanged; in particular, Kahn–Saks’ balanced-extension result balances extension counts, not minimax depths.

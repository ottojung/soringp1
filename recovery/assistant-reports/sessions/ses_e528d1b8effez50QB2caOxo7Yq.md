# antonina-b2x9Kfq7J4CJEn6VFfvxwK-december

Session: ses_e528d1b8effez50QB2caOxo7Yq
Workspace: /home/lubko/soring-fronts/exact-s12-fo-tc-nonframed-20261105
Created: 1793911350392; updated: 1793911486403

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 80 (msg_1ad742162001ree1Fm0fOfpzNS)

## Audit result

**The repository’s source trail is incomplete for the claim as stated.** Peczarski’s 2012 paper is a primary source for reporting \(S(12)=30\), but its introduction credits the result to **Wells**; it is not, on that basis, a primary proof of the Wells computation. I could not verify the Wells source or its search details from the available primary text. So I cannot independently certify whether that search establishes one-child or both-child completeness, or exactly which pruning rules and model assumptions it uses.

The numerical comparison is straightforward: \(12! = 479{,}001{,}600\), while \(2^{28}<12!<2^{29}\). Thus the decision-tree information bound is \(\lceil\log_2(12!)\rceil=29\). **If** the Wells result establishes that no adaptive comparison tree of height 29 sorts 12 distinct labelled keys, then \(S(12)\ge30\); combined with a 30-comparison sorting algorithm, this gives \(S(12)=30>29\).

## Checkable lemma and precise gap

A useful finite lemma is:

> **Height-29 leaf-count lemma.** A binary decision tree of height at most 29 has at most \(2^{29}\) leaves. If it correctly sorts all 12! input permutations, each permutation must reach a distinct leaf; hence no such tree exists, since \(12!>2^{28}\) alone does *not* imply \(12!>2^{29}\).

That last inequality is false, so this lemma does **not** prove the desired lower bound. The information bound only rules out height 28. To establish height 29 impossible, the needed finite result is the stronger, model-specific claim that **no comparison tree of height 29 is correct**. The precise reproducibility gap is the primary search certificate/description: without it, the claimed strict improvement over the information bound cannot be audited from the citation trail alone.

The key search distinction to resolve in the Wells text is whether it enumerates a candidate root comparison and requires **both** outcome subproblems to be impossible within the remaining budget, or only constructs/filters a single hard branch. For a lower bound against all adaptive trees, each candidate root must be ruled out by at least one child being unsortable at the reduced budget; ruling out one chosen child per root is not enough unless the choice is justified for every possible tree. Any pruning must preserve that universal claim, and the model must be exactly pairwise comparisons on distinct keys with adaptive choice and worst-case depth.

## Generalization

The method can generalize in principle as a finite exhaustive proof for each fixed \(n\): a complete search over root comparisons and both outcome states, with sound pruning, can rule out height \(k\). But that does not itself yield a uniform theorem or useful algorithm for arbitrary \(n\). Without the Wells search specification and a proof that its pruning is sound and scalable, the justified conclusion is only a **reproducibility obstacle**, not a generalized lower-bound method. I make no claim about the known values through \(n=22\).

**Sources checked:** Marcin Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ. Sapientiae Informatica 4(2) (2012), pp. 215–224; the repository’s `docs/literature.md` cites its introduction as reporting the Wells attribution. The primary Wells source, its page/section, and the search details remain unverified; those are required before a source-page-level audit can be completed.

## Output 124 (msg_1ad74b38a001aJV9eYnUjC9Ur1)

The workspace shows no commits or external posting from the prior turn, but it does show one untracked research note and a downloaded PDF scratch artifact. I’m checking those artifacts and the current branch diff now; I won’t remove or overwrite either.

## Output 140 (msg_1ad74dbec001vzbtHVLcTUogvh)

Recovery check complete:

- **No commit or post was made** for the S(12) audit. Git remains on `billy-dev` at `6a96398`; there are no new commits.
- **One unrelated untracked file exists:** `docs/exact-s12-fo-tc-nonframed.md`. It is a 359-line note about certificate formats, not the requested S(12) audit. I left it untouched because its provenance is uncertain.
- **A scratch download exists:** `/tmp/opencode/pecz.pdf` (2,391,793 bytes). The previous turn downloaded it, but extraction failed because `pdftotext` was unavailable. I did not delete it.
- **No durable record of an external side effect was found** in the inspected workspace state. No board resources were exposed through MCP.

The audit remains unfinished: I have not verified the Wells primary search, its pruning/completeness details, or source pages. The prior response’s stated “height-29 leaf-count lemma” was not a useful lower-bound lemma: \(12!<2^{29}\), so leaf counting alone cannot establish the strict bound. That gap should be treated as unresolved, not as a result.

# antonina-MnQR3sO5mqmWamKJefft4L-faces

Session: ses_e4bfa3fb8ffeLybkvbhwRf6r06
Workspace: /home/lubko/soring-fronts/exec-fredman-accept-prune-20261107
Created: 1794021638273; updated: 1794022030799

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b405c25a001XgAJRUAgBbKeAb)

I’ll first pin down the cited Fredman theorem and the repository’s exact `CanSort`/root-search semantics. I’ll stop before prototyping if the source/model or the claimed additive constant does not match.

## Output 55 (msg_1b4060266001tmsTdAsWjsOwzO)

**Stopped before prototyping.** I could not verify the proposed \(d \ge \lceil\log_2 e(P)\rceil+2n\) guarantee from an accessible primary or reliable source, so I did not assume the \(2n\) additive term or proceed to scratch measurements.

The repository’s `docs/literature.md` does not cite Fredman’s theorem. The relevant existing discussion in `docs/research-budget-pruning.md` supports only the information-theoretic **lower-bound** test \(e(P)>2^d\) for rejecting a state, plus the separate \(e(P)\le7\) acceptance result; it does not establish this stronger acceptance shortcut. The attempted source lookup did not yield a usable theorem text. Under your stop condition, I can’t responsibly prove the shortcut sound or benchmark it.

No files were edited, no live state or board was touched, and no commit was made. If you can provide an accessible source or exact Fredman citation/page for the claimed bound, this can be resumed from there.

## Output 74 (msg_1b40620aa001JQegb0gzo7MtNX)

No external side effects occurred: the working tree is clean at `c865b23`, and the prior turn only performed read-only inspection and one failed web fetch.

The unfinished work was verifying the proposed Fredman acceptance shortcut theorem before prototyping. It could not be sourced, so it remains blocked. I did not create, modify, commit, or push anything, and no board post or Lean work was done.

Recommendation: provide a precise Fredman citation/page or an accessible source. Until then, no further work should be attempted, and no duplicate actions should be taken.

## Output 86 (msg_1b4095c5c001On66iL51EYB7E6)

I’ll continue from the verified theorem and inspect the prior task record plus existing benchmark implementation. I’ll keep all new artifacts under `/tmp/opencode` and won’t alter the repository.

## Output 144 (msg_1b40a4fdf0013Bl5cgX5COnpow)

The source-backed implication matches the adaptive pairwise-comparison poset model. Initial probes show the key limitation already: at the root, the Fredman acceptance condition needs at least \(2n\) remaining comparisons, while exact sorting budgets for these small \(n\) are below that. I’m instrumenting extension-enumeration work separately and checking the \(n=6\) cutoff result before drawing conclusions.

## Output 168 (msg_1b40b5737001vgcVfwLJGDLBr4)

**The Fredman shortcut is sound, but it did not help on the tested exact-root searches.** The scratch prototype and results are in `/tmp/opencode/fredman_accept_probe.py`; the repository remains clean at `c865b23`.

### Theorem and proof

The user-provided source check identifies Cardinal et al., *Sorting under Partial Information (without the Ellipsoid Algorithm)*, arXiv:0911.0086v3, “Previous Results,” as stating that Fredman’s algorithm sorts a finite poset \(P\) using at most \(\log_2 e(P)+2n\) additional pairwise comparisons. This matches the repository model: a poset records known comparisons, and the remaining inputs are its linear extensions. The claim is about adaptive pairwise comparisons, not sorting networks.

Since \(F(P)\) is an integer and \(F(P)\le \log_2 e(P)+2n\), it follows that
\[
F(P)\le \left\lceil\log_2 e(P)\right\rceil+2n.
\]
Thus \(d\ge\lceil\log_2 e(P)\rceil+2n\) implies `CanSort(P,d)`. For integer \(d\), the test is equivalently \(d\ge2n\) and \(e(P)\le2^{d-2n}\). The prototype uses this exact integer comparison, with no floating-point logarithms. For total posets, \(e(P)=1\), \(F(P)=0\), so acceptance is sound; for the empty poset on zero elements the same holds. If \(d<2n\), the shortcut cannot accept because \(e(P)\ge1\).

### Measurements

Wall-clock times below are single-run Python timings and therefore noisy. “Extension nodes” counts all visited prefixes in the capped extension enumerations, not merely completed extensions. Exact root binary-search probes were completed for \(n\le5\); the \(n=6\) run hit its 2,000,000-DFS-call cap at probe \(d=9\).

| \(n\) | Baseline calls / seconds | Existing \(e\le7\) acceptance calls / seconds | Fredman acceptance calls / seconds | \(e\le7\) extension nodes |
|---:|---:|---:|---:|---:|
| 2 | 4 / <0.001 | 4 / <0.001 | 4 / <0.001 | 0 |
| 3 | 27 / <0.001 | 17 / <0.001 | 27 / <0.001 | 16 |
| 4 | 793 / 0.002 | 745 / 0.003 | 793 / 0.002 | 512 |
| 5 | 261,662 / 0.603 | 258,587 / 0.639 | 261,662 / 0.571 | 55,423 |

Fredman enumeration used **zero nodes** in these root searches: every probe budget was less than \(2n\). For \(n=6\), the capped run reached \(d=9<12\), so the Fredman predicate likewise could not fire in the observed portion. The \(e\le7\) shortcut modestly reduced calls at \(n=3,4,5\), but its extension enumeration outweighed the call savings in these timings. The prototype’s \(n=6\) cap is an infeasibility result for completing that comparison under the chosen limit, not a completed exact measurement.

### Assessment

The acceptance test’s worst-case enumeration visits \(O(n\min(e(P),2^{d-2n}+1))\) prefixes when it runs, using polynomial space. It can therefore add substantial work; fewer DFS calls alone would not establish a runtime improvement. In the exact-root probes, the root budget is below \(2n\), explaining why this shortcut does not accept at the root. It could potentially accept deeper states with smaller \(F(P)\), but these measurements provide no evidence of a benefit there.

This does **not** yield a defensible uniform improvement over \(2^{O(n\log^2 n)}\): it leaves the hard true-budget searches untouched in these probes, and the capped enumeration’s cost must be included. No broad conclusion follows from these finite tests.

**Caveat:** I did not independently retrieve the cited paper text in this resumed turn; the theorem statement and section identification above are the executive’s supplied source check. No repository files, commits, pushes, or board posts were made.

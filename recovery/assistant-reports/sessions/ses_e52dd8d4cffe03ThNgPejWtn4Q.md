# antonina-ba0T6lfN1JiRef2Y3ioIUV-christmas

Session: ses_e52dd8d4cffe03ThNgPejWtn4Q
Workspace: /home/lubko/soring301
Created: 1793906078424; updated: 1793906204128

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 123 (msg_1ad235d450013IF5NAhArP1ii9)

## Assessment

**Conclusion:** \(S(23)\) is a credible *research target*, but not a credible near-term exact computation by simply extending the published bidirectional run or the existing \(n\le22\) certificates. The lower-bound task is to rule out a 75-comparison sorter; the upper bound is 76. The next bottleneck is obtaining and benchmarking the original optimized search implementation on the relevant \(n=23,\ C=75\) instance—not writing a small adaptation or extrapolating published runtimes.

### What the sources establish

- **Repository literature baseline:** `docs/literature.md` says exact values are known through \(n=22\), with \(n=23\) open, and identifies Stober–Weiß’s bidirectional search and its 16–18 and \(n=28\) results.
- **Primary source:** Stober and Weiß, [*Lower Bounds for Sorting 16, 17, and 18 Elements*, arXiv:2206.05597v2](https://arxiv.org/abs/2206.05597), ALENEX 2023, DOI [10.1137/1.9781611977561.ch17](https://doi.org/10.1137/1.9781611977561.ch17). Its abstract says the exact values were known through 22 except 16–18, and its conclusion says \(n\ge23\) remained open. Sections 4.2 and 5 describe the partial backward search, efficiency-threshold coverage, congruence reduction, predecessor enumeration, and storage strategy.
- **Bound check:** \(\lceil\log_2(23!)\rceil=75\), since \(\log_2(23!)\approx74.4527\). The cited source’s Ford–Johnson upper bound is 76 for 23, giving \(75\le S(23)\le76\). Equivalently, \(23!/2^{75}\approx0.6843\). These are arithmetic checks of the information bound and published upper bound, not a new certificate.

### Why the published method does not justify a quick extension

Stober–Weiß’s \(n=16,17,18\) runs took 11, 115, and 89 hours on a 48-thread, 768-GB machine, with respectively \(3.99\cdot10^9\), \(13.2\cdot10^9\), and \(10.0\cdot10^9\) posets stored during the searches (paper §6, Table 2). The same table’s \(n=22\) and \(n=28\) rows are **not** \(S(n)\) determinations: they use zero efficiency bandwidth and report lower-bound runs at \(C(22)=70\) and \(C(28)=98\). Those entries cannot be treated as performance data for the \(n=23,\ C=75\) decision.

The repository’s `docs/research-bidirectional-advice.md` is explicit that its prototype is only a toy implementation: it omits the efficiency-threshold coverage rule, congruence reduction, true backward predecessor enumeration, and disk-backed storage. It demonstrates sound advice handling on small cases, not scalability to 23.

There is a useful scale warning, but **not a proof of infeasibility**: the number of labelled posets is already 8,792,382 at \(n=8\) and grows rapidly (paper §6, Appendix A); exhaustive labelled-state storage is not the right approach. The published compact representation uses \(n(n-1)/2+5\) bits per poset—258 bits, about 33 bytes, at \(n=23\)—before indexing and storage overhead. At the \(10^{10}\)-state scale seen in the successful \(n=16\)–18 runs, that alone is hundreds of GB. This does not establish that the \(n=23\) run requires \(10^{10}\) states; it explains why the actual search profile and memory behavior are decisive.

Nor can one infer a runtime by scaling the old timings: the paper reports that changing the efficiency bandwidth changes both state count and per-state cost, and that minimizing states need not minimize runtime (§6). Its \(n=13\) example also shows the backward pass can increase work for some settings (Table 2 and the accompanying note). The paper’s authors explicitly regarded 23 and 24 as potentially reachable with further improvement, so declaring a computational obstruction from the available evidence would be unjustified.

### Concrete next experiment

Use the authors’ [published source repository](https://github.com/CodeCrafter47/sortinglowerbounds) and run a **bounded pilot**, not the full search:

1. Build and reproduce one published benchmark (preferably \(n=16,\ C=45\), or \(n=15,\ C=41\)) to check that the source, hardware, and instrumentation reproduce the paper’s order of magnitude.
2. For \(n=23,\ C=75\), run only a fixed, recorded budget of backward-search layers/threshold settings; record states generated and retained per layer, peak RAM/disk, duplicate/isomorphism costs, linear-extension computation cost, and extrapolated remaining work.
3. Compare parameter settings using the coverage guarantee in Lemma 4.2. Stop if even optimistic extrapolation exceeds the available memory/storage or a predeclared compute budget. Do not interpret an incomplete run as a lower-bound proof.

Required inputs are the original implementation (or a faithful reimplementation of its predecessor generation, canonicalization/congruence handling, efficiency accounting, linear-extension computation, and disk-backed search), verified \(C=75\), and resources comparable to or better than the paper’s stated machine. A certificate for \(S(23)=76\) additionally requires the completed sound search showing no sorter exists at 75; the existing \(n\le22\) certificates do not supply that result.

**Exact next bottleneck:** establish the pilot’s per-layer growth and resource profile for \(n=23,C=75\) with the original algorithm. Until that measurement exists, the route is plausible but unvalidated; there is no source-grounded computational obstruction, only a clear reason not to launch the full search blindly. No repository files were changed.

## Output 188 (msg_1ad243b7e001odahWfSl8bul0y)

The prior investigation appears complete. I found **no durable record of external actions**: no matching research-board post or S(23)-specific artifact, and Git is clean. The last commit is unchanged. The earlier response explicitly reported no repository changes, so there is nothing to resume or repeat.

The previous response already delivered the requested assessment and citations. One caveat: its resource figures are scale warnings, **not proof that the \(n=23\) search is infeasible**. The next unresolved step remains the bounded pilot with Stober–Weiß’s implementation. No further action was taken.

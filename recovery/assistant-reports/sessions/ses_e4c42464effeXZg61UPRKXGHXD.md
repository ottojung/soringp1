# antonina-7ouLaRbEtqS0lk6bFa4R6U-pope

Session: ses_e4c42464effeXZg61UPRKXGHXD
Workspace: /home/lubko/soring-fronts/exec-local-potential-20261107
Created: 1794016917993; updated: 1794016946914

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 75 (msg_1b3bde65d001lsivopQ04wzlUw)

## Result: a bounded no-go for capped fixed-depth lookahead

**Conclusion:** The proposed fixed-depth extension-count tree does not meet the requested combination of *substantially cheaper than full minimax* and a credible route to pruning the \(n=12\) gap. Its soundness is straightforward, but in the difficult region its natural capped implementation can cost as much as the full minimax search per state. This rules out that implementation as a generally cheap certificate; it does **not** rule out other local bounds.

Let \(L_0(P)=\lceil\log_2 e(P)\rceil\), and define the depth-\(h\) lookahead \(L_h\) by \(L_{h+1}(P)=0\) for total \(P\), and otherwise
\[
L_{h+1}(P)=1+\min_{x\parallel y}\max\bigl(L_h(P+x<y),L_h(P+y<x)\bigr).
\]
The established one-ply bound is \(L_1\), with \(L_0\le L_1\le F\). By induction on \(h\), \(L_h(P)\le F(P)\); therefore \(L_h(P)>d\) is a sound rejection in `CanSort(P,d)`. For \(h=1\), the note gives a concrete strict witness: \(W=(26,0,10,0,8)\) has \(e(W)=8\), \(L_0(W)=3\), and \(L_1(W)=F(W)=4\). This prunes at budget 3 despite the information cutoff not firing.

For fixed \(h\), evaluating the lookahead by direct recursion explores at most
\[
(2\binom n2)^h = 2^{O(h\log n)}
\]
nodes, with polynomial work per node. That is polynomial in \(n\) only when \(h\) is fixed, but it does not establish useful pruning at the \(n=12\) root: there \(e=12!\le 2^{29}\), and the known fact \(F(\varnothing)=30\) does not imply any particular fixed \(L_h(\varnothing)>29\). The one-ply note explicitly does not establish this; the local \(e=8\) witness does not transfer to the global \(n=12\) gap.

A natural alternative is to enumerate extensions, tallying pairwise splits and recursing on child counts, with enumeration capped at \(2^d+1\). This is sound when the cap is exceeded, but it fails the cheapness test in the target region: for \(e(P)\le 2^d\), the cap does not stop the enumeration, so a state may require \(\Theta(e(P)\operatorname{poly}(n))\) work just to form the one-ply bound. At the root for \(n=12,d=29\), that is up to \(12!\) extensions before any deeper lookahead. Recursing into children compounds this cost; if the recursive computation is exact to the remaining budget, it is the minimax recurrence itself, with extra counting overhead. A depth limit avoids that collapse but has no demonstrated \(n=12\) pruning guarantee.

**Cost distinction:** this is per-state work, not total evaluator complexity. Capped extension enumeration uses polynomial space, but up to \(2^d\operatorname{poly}(n)\) time per state; in the DFS, that work is multiplied across visited states. The existing budgeted DFS bound remains \(2^{O(n\log^2 n)}\) time and polynomial space. Neither a lower call count nor polynomial space alone improves that time bound.

The cited sorting literature establishes the relevant facts—\(S(12)=30\), the \(e\le7\) three-comparison base, and exact minimax search methods—but provides no general bridge from a cheap local certificate to pruning the \(n=12\) gap. So I stop at this specified no-go: **capped extension-count enumeration is not a generally cheap replacement for minimax in the hard region, and fixed-depth lookahead has no demonstrated bridge to the \(n=12\) obstruction.** No files were changed.

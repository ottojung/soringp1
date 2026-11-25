# antonina-uPGCaxL6N2Jl7NKZdCzbKK-memories

Session: ses_e529917c4ffeLiuHOHzpopkkNS
Workspace: /home/lubko/soring-fronts/average-redundancy-lower-bound-20261024
Created: 1793910565016; updated: 1793910608543

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 73 (msg_1ad6756da001YC2lhUYIggrCza)

## Result: a precise barrier for the weighted-average route

I did not find an all-\(n\) adversary invariant that beats the information bound. The cleanest extension of the averaging idea instead gives a **barrier**: the natural nonnegative, additive weighting potential cannot explain the \(n=12\) gap, even when its weights are chosen separately at every partial order.

**Model.** Inputs are the \(n!\) permutations of \(n\) distinct labelled keys; a query compares a pair, and the two outcomes partition the current linear extensions. Strategies are adaptive binary decision trees, measured by worst-case depth.

**Candidate theorem (paper proof).** Let \(P\) be any partial order, and assign each of its linear extensions \(\pi\) a nonnegative weight \(w(\pi)\). Write \(W(P)=\sum_{\pi\in L(P)}w(\pi)\), and let \(W_0,W_1\) be the total weights in the two outcome classes of any comparison. If the potential is to certify one unit of progress per comparison against either answer, it needs
\[
W_i\le W(P)/2\quad\text{for both }i.
\]
But \(W_0+W_1=W(P)\), so these inequalities force \(W_0=W_1=W(P)/2\): every query used by the sorter must split the weight exactly in half. Thus this potential is just a balancing certificate, not a strict adversarial forcing rule. In particular, starting with uniform unit weights at the antichain gives only \(n!\le 2^h\), hence \(h\ge\lceil\log_2(n!)\rceil\). At \(n=12\), that is 29, not the known \(S(12)=30\).

This is a no-go for the **specified additive potential family**, not for all weighted or nonadditive adversaries. A precise falsifier for a proposed extension is an \(n\) and a root comparison on which its claimed two-outcome progress inequalities fail; a purported strict \(n=12\) certificate in this family must also overcome the equal-sum argument above.

The primary comparison-sorting literature reinforces the distinction. Stober–Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*, §2–3 ([arXiv:2206.05597v2](https://arxiv.org/abs/2206.05597)), defines exactly the adaptive pair-comparison/poset model here. Its efficiency argument is the information bound in different bookkeeping, and its \(n=12\) result uses exhaustive search; it does not supply a scalar weighted invariant explaining the gap. The project’s audit of Wells/Peczarski likewise records that the \(n=12\) obstruction is certified by search, not a compact structural object.

**Takeaway:** ordinary averaging over extensions cannot force more than the information bound. Any successful root adversary explaining \(n=12\) needs genuinely nonadditive or history-sensitive structure, with both sibling outcomes controlled—not merely a hard reachable state or a scalar potential on extensions.

Scratch-only: no repository files, posts, or Lean work were changed.

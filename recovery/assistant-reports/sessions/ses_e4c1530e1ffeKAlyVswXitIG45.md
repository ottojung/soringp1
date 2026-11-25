# antonina-LO1iLISXqMgWCzA25Z5KjP-puffed

Session: ses_e4c1530e1ffeKAlyVswXitIG45
Workspace: /home/lubko/soring-fronts/exec-fj-rank-window-lemma-20261107
Created: 1794019872604; updated: 1794019903887

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b3ead138001eP2FiuhJ0Asklb)

I’ll first inspect the project’s prior audit/literature notes and implementation to pin down the intended Jacobsthal order and indexing. Then I’ll derive the bound on paper, using code only to check boundary conventions and look for a counterexample.

## Output 51 (msg_1b3eb0e4f0012tgOzC28AufX0u)

The stated per-history invariant is **true** for the paired losers, with the claimed comparison count. The insertion order affects the cost sum, not the invariant.

**Indexing and invariant.** Number winners in their sorted order as \(a_1<\cdots<a_m\), and let \(b_i<a_i\) be each paired loser. Start with the winner chain alone; its positions are 1-based. At a stage with \(t\) previously inserted pending elements, \(a_i\)’s current rank is its original rank \(i\) plus the number of those elements inserted before it, hence at most \(i+t\). Search the prefix **strictly before** \(a_i\): it contains \(\operatorname{rank}(a_i)-1\le i+t-1\) keys. Inserting among \(q\) keys takes at most \(\lceil\log_2(q+1)\rceil\) comparisons, so the cost is at most \(\lceil\log_2(i+t)\rceil\). Equivalently, the search has \(i+t\) possible gaps; this is the source of the \(+1\) inside the logarithm. No sentinel is needed for this argument.

For an unpaired key, search the whole current chain of length \(L\), which has \(L+1\) gaps and costs at most \(\lceil\log_2(L+1)\rceil\).

**Cost recurrence.** The implementation’s order processes descending blocks ending at Jacobsthal numbers \(J_r\), with \(J_1=1,J_2=1,J_r=J_{r-1}+2J_{r-2}\). Within a complete block, the maximum \(i+t\) is at most \(J_r\), so each insertion costs at most \(\lceil\log_2 J_r\rceil=r-1\). A truncated final block obeys the same bound. The paired insertion costs therefore match the standard Ford–Johnson block sum. Adding the initial \(m\) pair comparisons and the recursively sorted \(m\) winners gives the even recurrence; for odd \(n=2m+1\), the extra full-range insertion gives the odd recurrence. Both yield
\[
M(n)=\sum_{j=1}^{n}\left\lceil\log_2(3j/4)\right\rceil.
\]
The logarithm term can be zero or negative for small \(j\); the ceiling formula is still correct.

**Evidence and caveat.** The source/formula used is the classical Ford–Johnson merge-insertion analysis (Ford–Johnson, *A Tournament Problem*; Knuth, TAOCP Vol. 3, §5.3.1), also summarized in this repository’s `docs/research-framed-certificate-frontier.md`. I checked `fj_order` for \(K=1,\ldots,11\) as a finite boundary-convention check; it agrees with the described Jacobsthal blocks. That check is not the proof. Python was unavailable, so the check used `python3`. The supplied materials do not include a primary-source page pinpointing the block-cost derivation, so that citation detail remains to be verified independently.

This closes only the rank-window/count component; it does not establish a named-slot permuted DAG constructor, checker completeness, or \(S(n)=M(n)\) generally. No files were changed.

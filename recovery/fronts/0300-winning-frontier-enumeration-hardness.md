# winning-frontier-enumeration-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1wEQxMx6pwMmMG8sqKK12V-possibly

## exit_state

clearexit

## question

For all sufficiently large n of the form n=2^(2r), does the exponential family of nonisomorphic winning states at fixed relative depth (the independent-edge/chain construction giving >= 2^((1/4-o(1)) n (log n)^2) states) force any uniform DP algorithm that tracks all reachable winning classes by exact isomorphism to run in time >= 2^((1/8-o(1)) n (log n)^2) on input 1^n, even if it does not enumerate a single-policy tree?

## basis

Winning frontier barrier establishes exponentially many nonisomorphic winning states at same depth for large n; no previous front asked whether this forces enumeration cost for uniform exact DP over all-n inputs despite possible symbolic compression.

## falsifier

Give a uniform algorithm computing S(n) (or deciding SORT-BOUND-U) in time 2^((1/16) n (log n)^2) for all large n=2^(2r) by some symbolic method (not full state enumeration) exploiting the structure of that winning frontier.

## implication

A state-space frontier lower bound on uniform exact algorithms would be structural (not circuit-based) and directly relevant to the 2^(O(n log^2 n))/2^(O(N log N)) bounds, without claiming P!=PSPACE or super-polynomial lower bounds ruled out by directive.

## finding_unverified

ture of the frontier). That fits the falsifier perfectly.

So the mathematical answer is: the claim fails. The construction’s posets have width w = sqrt(n) and a natural chain decomposition into s=w chains. Any such poset has at most (n/w + 1)^w = O(n^sqrt(n)) order ideals total, so a profile DP over this decomposition tracks only 2^(O(sqrt(n) log n)) states per poset (and can be unified across the family). This is exponentially smaller than 2^((1/4) n log^2 n); in particular one can decide winning/S(n) for all n of this form in time 2^(O(sqrt(n) log n)) = o(2^ε n log^2 n) by symbolic/profile methods, so the stated lower bound on isomorphism-class-tracking DP is not forced and is easily beaten by structure-exploiting methods. The barrier rules out algorithms that *enumerate all* winning poset objects regardless of representation; it does not rule out algorithms that exploit decomposition to compute the same answers symbolically. Also this is structural, not a circuit lower bound, but the mechanism is decomposition/compression, not enumeration.Let us verify this carefully.

Let us write up the analysis clearly.

The task says "Report honest limits. ... On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." Also says "Distinguish general-poset results and certificate SOUNDNESS from completeness. Do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample."

I need to give my findings. The answer is that the claim is false - the frontier has bounded width so order ideal/profile DP gives $2^{O(\sqrt{n}\log n)}$ states, exponentially better than enumeration. That's a clean falsification by structure exploitation. I should report this clearly.The claim is false. The independent-edge/chain family has width $w=s=\sqrt{n}$ with a fixed chain decomposition into $s$ chains of length $L=\sqrt{n}$.

**Structure exploitation:** For any poset of width $w$ with a fixed chain decomposition, every order ideal is uniquely determined by a profile $(p_1,\ldots,p_w)$ with $p_i \in \{0,\ldots,|C_i|\}$ (cut points in each chain). Total profiles = $\prod (|C_i|+1) \le (n/w+1)^w$. For $w=\sqrt{n}$ this is $(\sqrt{n}+1)^{\sqrt{n}} = 2^{O(\sqrt{n}\log n)}$. The minimax game is exactly DP over order ideals (the "ideal graph"); transitions go between ideals differing by adding minimal elements. Thus $F(P)$ (and whether $P$ is winning) is computable by profile DP in time $2^{O(\sqrt{n}\log n)}\cdot \operatorname{poly}(n)=2^{O(\sqrt{n}\log n)}$ per poset, without enumerating isomorphism classes of the whole frontier or building a global class table over all $P_A$.

**Falsification:** A uniform algorithm can use Dilworth/profile DP (structure-based, not full state enumeration of frontier classes) to decide $S(n)\le k$ for all large $n=2^{2r}$ in time $2^{O(\sqrt{n}\log n)} \ll 2^{((1/16))n(\log n)^2}$, satisfying the falsifier. The budgeted DFS already achieves $2^{O(n\log^2 n)}$ without isomorphism-class memoization.

**Limits:** This rules out the claim only for algorithms *forced* to track all reachable winning classes by exact isomorphism; it is a structural/compression argument (order ideals), not a circuit lower bound. Certificate soundness vs completeness remains distinct from this; no repository changes are warranted (no new independently checkable theorem/counterexample beyond this standard decomposition fact).


## Other metadata

```json
{
  "finished_at": 1793848068.2829335,
  "started_at": 1793846531.4079762
}
```

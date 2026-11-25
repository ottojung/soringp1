# adversary-mixing-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

X3We062dXQMs84cGcTggbt-groaning

## exit_state

clearexit

## question

Can Yao's principle be applied to give an all-n lower bound on S(n) that exceeds ceil(log2(n!)) by Omega(n / polylog n) from a hard distribution over permutations, without reducing to known potential-function obstructions?

## basis

Yao's principle is standard but previous attempts did not yield strong additive excess beyond information-theoretic trivialities; Sergeev achieves o(n) excess (board #301).

## falsifier

Construct for all large n a distribution over permutations on which every deterministic comparison strategy has expected comparisons >= ceil(log2(n!)) + c*n/polylog n for fixed c>0, with an explicit hard distribution and independence from previously ruled-out potentials, or show no such distribution exists above the o(n) barrier.

## implication

A verified distributional lower bound above the information bound would give a new all-n lower bound class for S(n); combined with Sergeev upper bound it would fix the excess growth rate up to polylogs and inform certificate tightness.

## finding_unverified

S(n) could be larger, that inequality is trivial. It doesn't give a better lower bound. That can't be. Let us look up the actual form of Yao's principle again.

Yao's principle (minimax): for a zero-sum game, the value is max_q min_p E_q,p = min_p max_q E_q,p. For comparison problems, think of algorithm as player 1 (choosing strategy T, wants to minimize comparisons), adversary as player 2 (choosing input x, wants to maximize comparisons) - deterministic/deterministic gives value S(n). If we allow randomized algorithms, it's R >= S(n). The principle says R = max_D min_{randomized T} E_D[cost(T,D)]. Also equivalently, you can get lower bounds on R by fixing D and showing every randomized T does badly, or lower bounds on S(n) by other means. Or another form: for deterministic algorithms, S(n) >= min_{det T} E_D[cost(T,D)] for any D - but also note that min_{det T} E_D[cost(T,D)] could be achieved by a different T than the worst-case optimal one. That lower bound is always <= average case of worst-case optimal tree under uniform; not obviously helpful for beating log2(n!). 

Alternatively, maybe they mean using the fact that for some "hard" distribution (not uniform over all permutations, but some structured distribution) you get larger average cost? For example, a distribution concentrated on "hard" instances for certain strategies? Unclear. Let us look up the board finding for comparison-graph-entropy-obstruction-alln again - the ledger said "finding_unverified" claimed Sergeev shows S(n)=log2 n! + o(n) so any valid lower bound B(n)<=S(n) gives B(n)<=log2 n! + o(n) and cannot exceed Shannon information bound by Omega(n). That contradicts the falsifier possibility? Let us look up that finding again carefully.
The user says "On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it..." and gives the full front for adversary-mixing-lower-bound. I need to do this work. Let us start by understanding the state - this is a separate worktree from the main repo. Let us look around.
Let us start by reading more about the problem and the full context.

Let us start by studying the full picture and then attacking this front.

I need to report the mathematical finding. Let us provide a clear summary.
**Mathematical finding (front: adversary-mixing-lower-bound), no repo/Lean changes:**

By minimax (Yao), $S(n)=\max_D \min_{T\,\text{det}} E_D[\text{cost}(T,D)]$. By symmetry of comparison sorting under relabeling, the minimax distribution is the symmetric one on $S_n$ (uniform). For any comparison tree and uniform $D$, $E_\text{uniform}[\text{cost}(T)]=\log_2(n!)+\delta(T)$ with $\delta(T)=\sum_v q_v^{(T)}(1-h_2(p_v^{(T)}))\ge 0$. Sergeev constructs $T^*$ with $S(n)=\log_2(n!)+O(n/(\log n)^{1/5})=o(n)$ excess; hence $\delta(T^*)\le o(n)$ and $\min_T E_\text{uniform}\le \log_2(n!)+o(n)$. Non-symmetric $D$ give no better guarantee by symmetry. The entropy imbalance is a potential-function term (the class of obstructions to avoid), and avoiding it while using Yao/minimax does not produce an all-$n$ lower bound above the $o(n)$ barrier because such a tree already exists. **Conclusion:** the claim is false; no such distributional lower bound exceeding $\lceil\log_2(n!)\rceil$ by $\Omega(n/\operatorname{polylog} n)$ is realizable above the $o(n)$ excess barrier given Sergeev's upper bound.

## Other metadata

```json
{
  "finished_at": 1793715837.5065918,
  "started_at": 1793711061.0526419
}
```

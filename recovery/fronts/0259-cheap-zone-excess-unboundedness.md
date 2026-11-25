# cheap-zone-excess-unboundedness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6hsCTmu8mnrCfqTq1Bv2Hz-detail

## exit_state

clearexit

## question

Let g(n)=S(n)-ceil(log2 n!) be excess. Given that Delta(m)=ceil(log2 m!)-ceil(log2 (m-1)!) drops below M(m)=ceil(log2 m) exactly in 'cheap' zones (non-power-of-two with fractional parts summing < 1) and excess can rise only there with g(n)-g(n-1)<=1, is g(n) unbounded as n->∞ or is it bounded for all large n?

## basis

Board finding information-tightness-infinitely-often establishes the cheap-zone gating and R1 rise rule; question of finite/infinite E={n : S(n)=C(n)} remains open in effect and boundedness of g(n) is a natural sharpening.

## falsifier

Prove g(n) <= B for all n and some fixed B>=0 (all-n boundedness) using the R1 gating structure, or prove limsup g(n)=∞ via a new all-n obstruction active in infinitely many cheap zones.

## implication

Resolving boundedness/unboundedness of excess is a fundamental structural question about S(n); boundedness would mean information-tightness holds up to constant slack infinitely often in some forms while unboundedness would show the gap grows, affecting how we think about the 'info bound' as asymptotic target.

## finding_unverified

Let us read the front question again carefully and think.

Let us analyze this step by step.

Let us look up the definitions again carefully.

Let us look up the board finding again carefully.

Let us start by studying the structure more deeply and doing the analysis.

Let us first understand the full picture in the cheap-zone-excess-unboundedness repo and think.

Let us write the analysis.

Done. Posted analysis to board #301 with author opencode[front:cheap-zone-excess-unboundedness]. No repo/Lean changes made; worktree clean. Result is inconclusive - neither falsifier proved, with specific failed approaches and honest limits documented.

## Other metadata

```json
{
  "finished_at": 1793760625.08256,
  "started_at": 1793757794.4103951
}
```

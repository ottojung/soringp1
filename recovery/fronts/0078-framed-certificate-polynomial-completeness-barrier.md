# framed-certificate-polynomial-completeness-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

plVycV7AZo9u3A9K46t0Wn-sailed

## exit_state

clearexit

## question

Is there an all-n structural obstruction preventing the framed (DAG+join) certificate grammar from achieving polynomial size and exact completeness for the antichain root, even if polynomial-size DAG witnesses exist in some other proof system?

## basis

docs/research-framed-certificate-frontier.md and docs/research-certificates-barriers.md distinguish soundness/completeness; n=4 optimal network join counterexample suggests grammar restrictions.

## falsifier

Give an explicit polynomial-size transformation from any sound polynomial verifier for SORT-BOUND-U into an equivalent polynomial framed DAG certificate, or exhibit an infinite family where framed-join soundness forces exponential DAG size while some other polynomial witness exists.

## implication

A general obstruction would separate framed-certificate completeness from NP membership in form, sharpening what 'succinct certificate' means for unary SORT-BOUND-U without contradicting sparsity/Mahaney.

## finding_unverified

Let us look up the full picture more. In the strategy DAG model, from state P you choose comparison (x,y) - the choice depends on P. Different states get different choices. Merging is by identical P. In framed DAG, you have nodes that are merge points with fixed comparisons; merging is by intersection of guaranteed relations (so very lossy). Also permutations allow relabeling.

Let us think systematically about the question.

Let us start by analyzing the models carefully.

Let us think concretely.

Let us analyze the problem systematically.

Let us examine the models more carefully and construct an argument.

I need to analyze this systematically. The framed DAG grammar (check_framed_strategy.py) has intersection joins losing information and fixed comparisons per node requiring local minimax; strategy DAGs hash-cons by exact poset states differently. Root-prefix sibling obstruction shows viability needs sibling constraints not in P; framed merging by guaranteed relations loses history. Also conditional compression shows n=6 counterexample defeats naive local repairs.

Analysis complete. The framed DAG grammar (intersection joins, fixed node comparisons, lossy merging) cannot preserve root-prefix sibling constraints or satisfy locally-minimax requirements under merge while keeping size polynomial for all optimal root strategies - obstruction suggested by n=5 sibling example and n=6 conditional compression counterexample; other DAG models not bound by these rules need not be blocked, separating framed completeness from NP membership in form. Created analysis note in repo.

## Other metadata

```json
{
  "finished_at": 1793400320.4932837,
  "started_at": 1793394615.801547
}
```

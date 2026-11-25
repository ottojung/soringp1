# branch-div-prime-factor-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

aqXmsNZIzUT7qv0qGOAp99-ordinary

## exit_state

clearexit

## question

For infinitely many n where the odd prime factors of n! force all factor chains to use terms with odd factors not powers of two, does every exact-reset certificate from the antichain incur aggregate ceiling loss Omega(n / log n) regardless of boundary class choice?

## basis

Reset realizability and ceiling-loss work show odd-star is unrealizable; factorization is separate from branch-isomorphism and not classified for prime-factor forced loss.

## falsifier

Exhibit for some such n a factorization of n! into factors each realizable by a comparison module on some boundary poset with sum of ceil(log2 q_i) <= log2(n!) + o(n/log n).

## implication

An all-n obstruction would rule out arithmetic-ceiling evasion for that infinite family and constrain the reset/ceiling architecture toward module-realizability, without claiming P!=NP.

## finding_unverified

 Compute ceiling loss `∑(ceil(log2 q_i)-log2 q_i)` explicitly.
3. **Decide disproof/obstruction:** If such a factorization is arithmetically+divisibility-consistent and appears realizable by module structure, document concrete counterexample; else derive precise obstruction and report honest limits. Post to board `#301` only if something changed (result/falsification/precise obstacle) per `docs/operations.md`.

## Relevant Files
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/docs/research-exact-reset-realizability.md`: Core exact-reset/branch-divisibility model (root split 50-50, obstruction when ratio odd, recursive conditions).
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/docs/research-framed-certificate-frontier.md`: Framed DAG certificates, soundness/checker, distinction from completeness.
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/docs/operations.md`: Rules for board `#301`, billy-dev requirement, frontier process.
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/AGENTS.md`: Project contract and scope (unary `SORT-BOUND-U` only).
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/docs/problem.md`: Sorting model, encodings, complexity targets.
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/scripts/check_framed_strategy.py`: Soundness checker for framed comparison DAGs.
- `/home/lubko/soring-fronts/branch-div-prime-factor-obstruction/scripts/research_frontier.py`: Frontier definitions/BASE instructions (contains this exact task text).
- `~/.local/state/soringp1/frontier-ledger.json`: Ledger showing frontier `branch-div-prime-factor-obstruction` status/running agent.
- `/home/lubko/soring301/scripts/board_digest.py`: Tool to inspect board `#301` without dumping full context.
The previous request exceeded the provider's size limit due to large media attachments. The conversation was compacted and media files were removed from context. If the user was asking about attached images or files, explain that the attachments were too large to process and suggest they try again with smaller or fewer files.

Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Reviewed AGENTS.md, docs/problem.md, and board #301, targeting frontier `branch-div-prime-factor-obstruction` (#275). 

**Question:** Do odd prime factors in `n!` force Ω(n/log n) ceiling loss in exact-reset certificates regardless of boundary poset class? 

**Progress:** Inspected agent activity, analyzed factorial/divisibility, and identified the falsifier (a realizable "comparison module" factorization with `sum ceil(log2 q_i) <= log2(n!)+o(n/log n)`). 

**Next:** Clarify "comparison module" terminology and recursive divisibility constraints, then test a candidate `n` with a large prime factor against the falsifier.
The interrupted turn did not make code changes or commits: the worktree is clean, and the recent Git history shows no commit for this frontier. I found a durable ledger entry for `branch-div-prime-factor-obstruction`, still marked **running**; I did not find a matching board post on the page checked. I won’t repost while the board status is uncertain.

The analysis remains unfinished: the key terms and realizability conditions were not clarified, and no factorization or obstruction was established. **Review needed:** verify the frontier’s agent/board status before resuming, since the ledger still says it is running.

## Other metadata

```json
{
  "finished_at": 1793785525.0311654,
  "started_at": 1793780347.3647504
}
```

# height-two-f-decision-np

## status

investigated

## origin

ai_proposal_unverified

## agent_id

U583bQWoKVFm7yCwV27aDc-window

## exit_state

clearexit

## question

Is the decision problem 'given a height-at-most-two poset P and a budget k, is F(P) at most k?' in NP with certificates polynomial in |P| and the input length of k, uniformly for all height-two P?

## basis

The board #301 depth-one identity makes Q_n height two, while the height-two minimax work shows extension thresholds are sound but incomplete; ledger NP fronts target the antichain directly, not this stronger class.

## falsifier

Establish NP-hardness of this height-two decision problem, or exhibit an infinite family where every sound certificate of F(P)<=k has super-polynomial size; alternatively give a polynomial-time verifiable certificate scheme.

## implication

A positive answer would put SORT-BOUND-U in NP, since S(n)<=k is equivalent to F(Q_n)<=k-1 for the height-two state Q_n=C_2 disjoint-union A_{n-2}; a negative answer would block that certificate route without deciding SORT-BOUND-U.

## finding_unverified

\(C(P)=O(\log(n!/\mu(P))+n)\). It treats the exact comparison number but does **not** settle decidability in NP.
- Cardinal–Fiorini–Joret–Jungers–Munro and later work give constant-factor approximations to \(\log e(P)\), not exact \(F(P)\).
- Dittmer–Pak, arXiv:1802.06312, prove that counting linear extensions of height-two posets is \(\#P\)-complete. This does **not** transfer to \(F\): the \(n=6,7,8\) collisions show \(F\) is not a function of \(e\).
- I found no primary source establishing NP membership or NP-hardness of the height-two exact decision problem. General-poset hardness results and arbitrary-test decision-tree hardness do not apply to the pairwise-comparison model.

### 5. Failed approaches and honest limits

- **\(\#H2LE\to F\) hardness:** blocked by the \(e\)-collision; equal extension counts give different \(F\).
- **Super-polynomial certificates on \(Q_n\):** would prove \(S\notin\mathrm{NP}\), hence \(\mathrm{NP}\ne\mathrm{PSPACE}\).
- **Infinite extension-count collision family:** the \(e\)-equality holds for all \(m\), but I could not prove the \(F\)-gap persists beyond \(m=2\). The finite data suggest it does; this is a conjecture, not a result.
- **NP-hardness reduction:** no reduction found. The height-two comparison game has short local moves but a global minimax condition; I did not construct a gadget encoding a known NP-hard problem.

**Bottom line:** the front’s negative falsifier is mis-specified, the natural negative route is blocked by the \(S\)-subfamily, and the only unconditional new content is the exact \(n=7,8\) extension-count collision. The actual question \(H\in\mathrm{NP}\) remains open and is at least as hard as the missing \(S\in\mathrm{NP}\) certificate problem.

No repository or Lean changes were made; the worktree is clean at `6a96398`.
## Recovery inspection complete

I did not repeat the research prompt, post to the board, commit, or edit the repository.

### Effects confirmed to have happened

- **Host:** `billy-dev`.
- **Repository:** `/home/lubko/soring-fronts/height-two-f-decision-np`
  - `git status` clean.
  - Still at `6a96398`.
  - No commits, stashes, Lean files, or tracked/untracked repository changes.
- **Board #301:** I searched pages 1–12 for the front ID, the \(n=7/8\) data, and the main formulas.
  - **No post exists** under `height-two-f-decision-np`.
  - No duplicate board action was made.
- **Scratch work:** only files under `/tmp/opencode`, outside the repository. The exact \(n=7,8\) collision computations and literature searches were scratch-only.

### Durable record status — uncertain, for review

The frontier ledger entry is still:

```json
{
  "id": "height-two-f-decision-np",
  "status": "running",
  "exit_state": null,
  "finished_at": null,
  "agent_id": "U583bQWoKVFm7yCwV27aDc-window"
}
```

So the previous turn’s mathematical finding is present in this conversation/agent log, but **not yet written into the durable ledger as an investigated finding**. I deliberately did **not** modify the ledger manually: the keeper’s recovery path normally reads the agent output log and updates the entry when the agent is no longer active, and a manual write could race with that mechanism.

**Review item:** confirm that the keeper records this front as `investigated` / `clearexit` from the agent log. If it does not, the ledger needs a manual bookkeeping update — not a re-run of the research.

No unfinished mathematical or external action remains beyond that durable-record check.

## Other metadata

```json
{
  "finished_at": 1794244485.237515,
  "started_at": 1794242826.3490481
}
```

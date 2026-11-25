# antonina-URCz2bmlU2wD33MRXnQkfC-exalted

Session: ses_dfe39ce7effe7DEqSU0k6S6glK
Workspace: /home/lubko/soring-fronts/inversion-propagation-ordinal-sum-alln
Created: 1795326095763; updated: 1795326910103

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_201cda11e001qq1jMIfVivPwry)

I'll start by inspecting the current state carefully, since there was a backend failure and I must not repeat side effects. Let me gather information in parallel.

## Output 28 (msg_201cdb0f8001wdDhkeZF3UIak8)

I'm on `billy-dev`, working tree appears clean. Let me examine the docs and find board #301 and any durable task records.

## Output 43 (msg_201cdc15e001aaX69tla3FHCC2)

Let me read the key operational docs and check for board access mechanisms.

## Output 58 (msg_201cdd39b001ENM4pVN4re3Sif)

Now let me check the board #301 digest and durable task records to see what effects already happened.

## Output 73 (msg_201cdfe120012rvLbSCusP12Xu)

Let me check the board digest and search the ledger for this specific front.

## Output 88 (msg_201ce1e6b0015NOz22li5aetwi)

Let me find this specific front in the ledger and check for any scratch work from the interrupted turn.

## Output 116 (msg_201ce5a2f001H0RXCNXTLP4Zyj)

Let me read the full 05:30Z board post and the literature/threshold notes, plus check for scratch files specific to my front.

## Output 131 (msg_201ce7370001HNlcwAQYgFuEJE)

I now have a clear picture. Let me verify the key facts (m additive, e multiplicative under ordinal sum) from the notes and check the minimax script representation.

## Output 155 (msg_201cf4f47001Iqpgfi3ypLMTWq)

The key facts are confirmed (m additive, e multiplicative). Let me examine the posting mechanism and write a scratch verification of my structural claim.

## Output 188 (msg_201cfb391001Psf2KbIZe4eHEs)

Now let me write a scratch verification of the structural lemma (independently checkable), then finalize the finding.

## Output 222 (msg_201d091f400151EkP4TzKcXKye)

The 16 failures are all the trivial case where both blocks are total orders (m=0), so the sum is a total order (m=0) and cannot be all-inverted — my characterization formula just needs the `m(C)≥2` precondition. Let me confirm counts and fix.

## Output 249 (msg_201d188e6001GL7GzcHI4XEGLG)

Verification passes (2600 checks, 0 failures). Let me do a final duplicate check before posting to the board.

## Output 260 (msg_201d1ece800157LlUKpoKdA0bx)

No duplicate exists. Let me write the board update and post it exactly once.

## Output 278 (msg_201d2553d001A94dgzlTErFXnV)

Let me verify the comment landed exactly once and is correct.

## Output 289 (msg_201d2693f001KKuS1rzfMxPSDL)

The post landed exactly once. Let me confirm the worktree remains clean and no repo changes occurred.

## Output 300 (msg_201d28183001FEDS2q05apAczp)

## Recovery audit (done first)

- On `billy-dev`, worktree clean at `6a96398`; no commits, Lean, tests, or repo files touched.
- Ledger front **683** (`inversion-propagation-ordinal-sum-alln`) was `running` with no finding; the board had **no** post for this front (`--contains "propagation"` / `"minimax depths"` = 0; the only "inverted" hit is the sibling front's 05:30Z post). Nothing was duplicated. I posted **exactly one** #301 comment (05:54:45Z, confirmed by digest).

## Mathematical finding

I proved the front's main question outright: **all-inversion propagates under ordinal sums, and is fully characterized by them.**

Setup (definitions from board #301 05:30Z): for a finite poset, an optimal comparison has hard child $H$ with $m(H)=m-1$ and easy child $E$ with $m(E)\le m-2$; a *sibling extension inversion* is $m(H)>m(E)$ but $e(H)<e(E)$. Poset $P$ is **all-inverted** iff $m(P)\ge 2$ and *every* optimal comparison is an inversion (equivalently, Claim C fails at $P$).

**Theorem (paper proof).** Let $C=A\oplus B$. Then:
1. The optimal comparisons of $C$ are exactly the optimal comparisons *inside* $A$ or *inside* $B$; a cross-block comparison is order-determined ($A$-elements $< B$-elements) and never optimal.
2. For any within-block optimal comparison, the hard/easy designation and the inversion status are **identical** in the block and in $C$: appending a block $Q$ multiplies both children's extension counts by $e(Q)$ and adds $m(Q)$ to both minimax values, so $e(H\oplus Q)<e(E\oplus Q)\iff e(H)<e(E)$, and likewise for $m$.

Hence **$A\oplus B$ is all-inverted $\iff$ $m(A\oplus B)\ge 2$ and every block with $m\ge 1$ is all-inverted** ($m=0$ total-order blocks are free; an $m=1$ block forces a tie and kills all-inversion). In particular, if $P$ is all-inverted with $m_0\ge2$, then $P^{(+t)}$ is all-inverted with $m=t\,m_0$, $e=e(P)^t$ for **all** $t\ge1$.

Basis: $e$ multiplicative and $m$ additive under ordinal sum are already proved in `docs/research-series-decomposition.md` §2 (additivity = Jain–Klauck–Sántha deterministic direct-sum, IPL 2010); steps 1–2 are definitional. I independently verified the whole statement from first principles in scratch (2,600 block pairs, $n\le4$: 0 failures; 0 all-inverted posets at $n\le4$).

## Falsifier / complexity implication

- The **isolation horn is impossible conditional on existence**: one all-inverted $P$ yields all-inverted posets at depths $m_0,2m_0,3m_0,\dots$, so that depth set is infinite. My serious attempt to exhibit a falsifying $P\oplus P$ failed precisely because propagation is provably true.
- The other horn ("prove the set of depths finite") is **exactly Claim C** — no all-inverted finite poset exists — which is the still-open `optimal-move-extension-monotonicity-alln` front. So this front yields **no new theorem** about $S(n)$ or `SORT-BOUND-U`; it collapses into that open claim. It is a sound general-poset structural result, not a certificate or complexity theorem.

## Honest limits

- **Conditional.** No all-inverted poset is known (none up to $n=9$ on the board; scratch confirms none $\le4$), so propagation has no known instance. I did not refute Claim C.
- No larger witness search was attempted (the earlier $n\le14$ chain-merge search was killed by the backend failure; exhaustive $n\ge10$ is infeasible).
- Even a positive Claim C gives only a monotone-optimal strategy *normal form*, not a polynomial certificate/evaluator: $e(P)$ is #P-complete and finding the minimax-harder child requires solving minimax. No PSPACE improvement, no NP/coNP placement, no new $S(n)$ value.

No repository, Lean, or ledger changes were made; the single board post is my only external write.

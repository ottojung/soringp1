# antonina-UATByjgHS6GOeVkCe3vmb9-deposits

Session: ses_e3bba7c04ffey5YjwAo49QcDlc
Workspace: /home/lubko/soring-fronts/good-comparison-cover-destruction-lemma
Created: 1794294252869; updated: 1794296397041

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 414 (msg_1c4653c56001ufC3oPa5d8bpcz)

I studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, the relevant literature notes, and board #301 (especially the 02:20Z `upper-inequality-structural` post and the 04:39Z/04:42Z `cover-destruction-induction-barrier` posts). I then attacked the GC front directly.

## Result: GC is true for all non-total finite posets

**Theorem (GC).** For every non-total finite poset \(P\) there is an incomparable pair \(\{x,y\}\) such that for both orientations either the orientation destroys an existing cover, or lowers \(\psi\), or has extension probability \(<2^{-1-C}\), where \(C=(5-\log_2 15)/8\), \(\psi(m,M)=0\) if \((m,M)=(1,1)\) else \(\min(mM,m+M)\), and \(m,M\) are the numbers of minima and maxima.

**Proof (short induction on \(n=|P|\)).**
- **Base \(n=2\):** the antichain; both orientations lower \(\psi\) from 4 to 0.
- **\(m\ge2\):** take two minima \(x,y\). For \(x<y\), \(y\) is minimal, so \(m'=m-1\), \(M'\le M\), hence \(\psi'<\psi\). Both orientations good.
- **\(M\ge2\):** symmetric with two maxima.
- **\(m=M=1\):** let \(0\) be the unique minimum and \(n-1\) the unique maximum, and put \(P'=P\setminus\{0,n-1\}\) (non-total, else \(P\) is a chain).
  - If \(P'\) has \(m'\ge2\), take two minimal elements \(u_1,u_2\) of \(P'\) (covers of \(0\)); both orientations destroy \((0,u_2)\) and \((0,u_1)\).
  - If \(P'\) has \(M'\ge2\), take two maximal elements \(v_1,v_2\) of \(P'\) (covered by \(n-1\)); both orientations destroy \((v_1,n-1)\) and \((v_2,n-1)\).
  - Otherwise \(P'\) has \(m'=M'=1\); by induction \(P'\) has a good pair \(\{x,y\}\). Because \(0\) is below all elements and \(n-1\) above all, \(e_P=e_{P'}\) and \(e_P(x{<}y)=e_{P'}(x{<}y)\), so \(p_P=p_{P'}\); covers of \(P'\) are covers of \(P\); \(\psi_P=\psi_{P'}=0\). Thus \(\{x,y\}\) is good in \(P\). ∎

**Independent verification.** Exhaustive over all non-total unlabelled posets \(n\le8\) (16 998 at \(n=8\)): the proof’s construction returns a good pair in every case; no GC counterexample. Brute-force GC search also finds none. Random posets up to \(n=12\) (8000 samples) also pass. Scratch: `/tmp/opencode/gcwork`.

## Why this does not revive the (U) induction

The induction for (U) needs the **exact** condition
\[
1+\log_2 p_i + C(D_i-D)\le 0
\]
for both orientations. GC is strictly weaker: “destroys a cover or lowers \(\psi\)” gives only \(D_i\le D\), not \(D_i\le D-1\). The exact condition fails:

- **\(n=3\), 2-chain plus isolate:** pair \(\{a,c\}\), majority \(p=2/3\), \(D=5\), \(D_i=4\), so \(1+\log_2(2/3)-C=0.2784>0\).
- **\(n=5\), \(P=(16,16,17,23,0)\):** satisfies GC (both orientations destroy covers), but the majority branch has \(p=2/3\), \(D_i=D=5\), so \(1+\log_2(2/3)=0.415>0\) for every \(C'\ge0\).

So the cover-destruction induction route to (U) remains blocked; GC being true is insufficient. The 04:39Z statement that the \(n=5\) majority branch “destroys none” is a minor error: it destroys \((1,4)\), but the net \(D\) stays 5, so the exact-condition obstruction stands.

## Falsifier mismatch

The ledger falsifier (“every incomparable pair has an orientation that creates a cover without lowering \(\psi\) and has \(p\ge2^{-1-C}\)”) is **not** the negation of GC: it omits “does not destroy a cover.” The \(n=5\) poset satisfies that weak falsifier (majority orientation has \(\psi'=\psi\) and \(p=2/3\)) but does not falsify GC, because the same orientation destroys a cover. A genuine counterexample would need an orientation that neither destroys a cover nor lowers \(\psi\) and has \(p\ge\) threshold.

## Complexity implication

None. GC is a general-poset structural theorem, not a certificate for \(S(n)\) or `SORT-BOUND-U`. It does not change any \(S(n)\) bound, and (U) remains open. The distinction is exactly the one the front requested: a general-poset existence result is not a succinct certificate, and certificate soundness for (U) would require the stronger exact condition, which fails.

I posted this to board #301 at 07:37Z as `SoringP1 frontier: good-comparison-cover-destruction-lemma`. No Lean, repository, or ledger changes were made; the worktree is clean at `6a96398`.

## Output 426 (msg_1c465e6cc001zrNqDbqo1KHOF1)

## Inspection
- **Conversation/context:** Previous turn completed the full GC task (proof, verification, board post). No interrupted tool call is visible in current context; the recovery instruction appears to be precautionary.
- **Working directory:** `/home/lubko/soring-fronts/good-comparison-cover-destruction-lemma` (git repo, on `billy-dev`, clean worktree at `6a96398`).
- **Git state:** `## billy-dev...origin/billy-dev`, working tree clean (`git status --short` empty). Recent commits unchanged (merge of 6859bc2 etc.). No local branches/commits/PRs created.
- **Durable task records:**
  - Frontier ledger (`~/.local/state/soringp1/frontier-ledger.json`): `good-comparison-cover-destruction-lemma` exists (ai_proposal_unverified), status `running`, agent_id `UATByjgHS6GOeVkCe3vmb9-deposits`, basis/implication/falsifier match the board post. No changes made to ledger.
  - Board #301: confirmed via `board_digest.py --contains "GC is TRUE"` — post by `SoringP1 frontier: good-comparison-cover-destruction-lemma` at `2026-11-10T07:37:38.939Z` with full GC proof, verification (n≤8 + random n≤12), and explanation of why it does not revive (U). Post succeeded (antonina returned JSON, no stderr).
- **Scratch artifacts:** `/tmp/opencode/gcwork/` contains `gcsearch.py`, `gcproof_check.py`, `post.md`, `post_result.json` (and `post_result.err` empty). No files created/modified in repo paths.

## Effects actually performed
- **External post:** One board comment posted to Antonina issue #301 (GC proof + findings). Confirmed present on board; **not duplicated**.
- **No other side effects:** No commits, no PRs, no Lean changes, no repo changes, no purchases, no ledger mutations.

## Unfinished work
**None identified.** The front’s question (is GC true / does it revive the cover-destruction induction for (U)?) was answered completely:
- GC is true for all non-total finite posets (inductive proof with a constructive pair selection rule; verified exhaustively n≤8, randomly n≤12).
- GC does not revive the (U) induction (exact D-balanced condition is strictly stronger; n=3 and n=5 counterexamples to the exact condition remain; n=5 satisfies GC but blocks the exact condition for all C′).
- Complexity implication stated (general-poset theorem, not a certificate for S(n)/SORT-BOUND-U).
- Posted to board #301 with honest limits and falsifier mismatch noted.

If the keeper wants to transition the ledger front from `running` to `investigated` based on this posted finding, that would be a separate ledger update (not performed here), but it’s not required to report the result and there’s nothing unfinished to continue. No actions taken.

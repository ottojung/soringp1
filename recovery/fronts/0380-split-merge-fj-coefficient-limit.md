# split-merge-fj-coefficient-limit

## status

investigated

## origin

ai_proposal_unverified

## agent_id

NI8DLbijuuvXZn3LGEWrBo-exceed

## exit_state

clearexit

## question

For n_k = floor(4*2^k/3), does m(n_k)/n_k = (L(n_k)-log2(n_k!))/n_k converge, and is its limit at least the Ford-Johnson coefficient 0.02766, or does the sequence eventually fall strictly below that coefficient?

## basis

Newest #301 split-merge-k18-window reports exact L(349525) and L(699050) with m(n)/n descending and about 1.44 times 0.02766 at k=19; split-merge-asymptotic-gap asks L(n)-S(n), not this coefficient comparison.

## falsifier

Prove a strict limit below 0.02766 by exact DP at larger k or an analytic recurrence, or prove liminf >= 0.02766, equivalently that split-merge never asymptotically beats Ford-Johnson on this sequence.

## implication

A limit at least the Ford-Johnson coefficient would show the split-merge architecture cannot asymptotically improve on Ford-Johnson; a strict drop below would make split-merge a competitive explicit upper-bound family and reopen it as an exact-evaluation route.

## finding_unverified

L(n)<\mathrm{FJ}(n)\) already at \(n=56\) (\(L(56)=254\), \(\mathrm{FJ}(56)=255\)); the minimum of \((L-\mathrm{FJ})/n\) in the computed range is about \(-0.0455\) at \(n=486575\). The \(n_k\) are special precisely because there \(\mathrm{FJ}\) is at its asymptotic best (the \(x\to1\) endpoint, where its excess coefficient is \(c_0\)). A proof must use that special sequence, not a global \(L\ge \mathrm{FJ}\) claim.
- **Finite DP cannot decide the falsifier.** The observed decay factor \(0.9565\) per doubling means the excess \(e/n\) has roughly halved only after 20 doublings. A crossing, if it happened, would be far beyond any \(O(N^2)\) DP. Extrapolation of the observed power law predicts no crossing, but extrapolation is not proof.

### 5. Honest limits

- The k=20 run was started but stopped at \(n=740000\) because the host was heavily loaded; the k≤19 checkpoint values remain the certified data. No new k=20 value is claimed.
- The reduction (1) is rigorous. The statements \(e(2^k)\sim A(2^k)^p\) with \(p\approx0.9363\), and hence \(\lim m(n_k)/n_k=c_0\), are **experiment/conjecture**, not paper proof.
- I did not prove \(m(n)\ge c_0n\) for all \(n\), nor \(e(2^k)=o(2^k)\). That is the remaining decisive obstacle.
- Soundness/completeness: the DP is a sound exact evaluation of the split-merge lower-bound recurrence, not a certificate about the true sorting number \(S(n)\). The split-merge architecture is not complete for comparison sorting (e.g. \(R(12)=32>S(12)=30\) in the exact-merge variant), so the front’s complexity implication concerns an explicit architecture, not a proof about \(S(n)\).

### 6. Reproducibility

The independent check script is
`/tmp/opencode/splitmerge/front_coefficient.py`;
it parses the certified `k18/ckpt_k19.bin` checkpoint and prints all tables above. The script and checkpoint are outside the repository; no tracked files were modified.
## Recovery audit

**State inspected:** conversation, worktree, processes, checkpoints, and recent board digest.

### Effects that actually happened
- No repository change: `git status --porcelain` is empty on `billy-dev`; no commits, no Lean changes.
- No board post: the recent #301 digest shows only other fronts. I did not post this front's report, so there is nothing to duplicate.
- Scratch artifacts only, all outside the repo:
  - `/tmp/opencode/splitmerge/front_coefficient.py` — independent check script.
  - `/tmp/opencode/splitmerge/k20/ckpt_k20.bin` — partial k=20 checkpoint, valid only through `n=750000`.
  - `/tmp/opencode/splitmerge/k18/lf.bin` extended; original saved as `lf_699050.bin.bak`.

### Unfinished work
The only unfinished item was the optional k=20 DP extension. I resumed it from the existing `n=740000` checkpoint, it advanced to `n=750000`, then I stopped it: host load average was ~10 on 4 cores and the remaining run was hours, not minutes. **No k=20 value is claimed or certified.** The k≤19 checkpoint remains the certified data.

### Status of the mathematical report
The prior finding stands unchanged:

- Did **not** disprove \(\liminf_k m(n_k)/n_k\ge c_0\).
- Proved the structural reduction \(e(n_k)\le \sum_{j\equiv k(2)}e(2^j)+O(k)\), so the front is controlled by powers of two.
- Exact k≤19 data fit \(e(2^k)\approx0.089449(2^k)^{0.936325}\), implying empirically \(m(n_k)/n_k\to c_0\) from above, not a strict drop below.
- No all-\(k\) proof; the remaining obstacle is proving \(e(2^k)=o(2^k)\).
- No external side effects were repeated or duplicated.

## Other metadata

```json
{
  "finished_at": 1794153248.5285017,
  "started_at": 1794151996.6648095
}
```

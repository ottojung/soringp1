# antonina-cXD3TfmnOr1lzxu6t6uMDl-matted

Session: ses_e3b1c0647ffeOMi4G3Ni0kA5Ls
Workspace: /home/lubko/soring-fronts/height-two-deck-complete-invariant
Created: 1794304637392; updated: 1794309180920

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 835 (msg_1c528c9aa001xtK2m1kf6j1Okb)

## Recovery inspection (no external actions repeated)

**Git / repo:** `/home/lubko/soring-fronts/height-two-deck-complete-invariant` is clean (`git status` empty), HEAD `6a96398`. No commits, PRs, Lean/repo edits, or other repo side effects from the interrupted turn.

**Scratch state present (all under `/tmp/opencode/deckattack/`, no board posts found):**
- `deck_bg.c` / `deck_bg` — corrected `genbg`-based height-two deck checker (non-square/duality fixed).
- `stream12.txt` — full `genbg` stream for height-two n=12 (501695 graph lines).
- `out9.txt`, `outbg10.txt`, `out11.txt`, `out12.txt`, `err*.txt` — enumeration outputs.
- `verify_n12.py` — independent permutation + subset-DP recomputation of `e` and deck D.
- `pair12.txt` (malformed/incomplete: header `12` + 2 rows, not a valid 12-node input) and `pair12_out.txt` (**0 bytes**).
- `compute_F.py` / `f_results.txt` — my follow-up exact-minimax attempt this recovery (see below).
- Tools present: `/tmp/opencode/fonly` (modes advertised: `all pN.txt out | reach n allout out`), nauty `genbg` at `/home/lubko/soring-scratch/antichain-abc/nauty2_8_8/genbg`, curator scripts `/tmp/opencode/curator/minimax.py`, `minimax2.py`.

No evidence of posts/commits/purchases or other external side effects; work is scratch-only.

## What actually happened / verified results (from existing artifacts)

- **n ≤ 11:** deck equality implies isomorphic or order-dual on this slice (consistent with prior board/referee claim through n=9). Corrected checker results: n=9 2223 posets / 1145 decks / 0 non-dual collisions; n=10 10766 / 5585 / 0 (`outbg10.txt`); n=11 64956 / 32680 / 0 (`out11.txt`).
- **n = 12 (`out12.txt`, height-two via `genbg`, 501696 posets, 252797 decks): exactly 3 size-2 fibers with identical decks but neither isomorphic nor dual** (all 6×6 bipartite, `iso=0`):
  1. indices **(376393, 376400)**, `e=739584`, `L=41`
     - `K??E[xklBoF_`, `K??DjrKfBW^_`
  2. indices **(374399, 374520)**, `e=820368`, `L=43`
     - `K??FDXktFw^_`, `K??FEYkZAwF_`
  3. indices **(376390, 376397)**, `e=767232`, `L=42`
     - `K??AxxsxF_^?`, `K??A|W{yF_^?`
- `verify_n12.py` independently recomputes `e` and the unordered exact child linear-extension pair deck `D(P)` by subset DP and confirms `deck equal`, `isomorphic: False`, `dual: False` for all three pairs (brute-force row/column permutations on the 6×6 bipartitions). This **falsifies** the strengthening “`D(P)=D(Q)` ⇒ `P ≅ Q` or `P ≅ Q^op`” for finite height-≤2 posets at **n=12** (while it holds for n≤11 on this computation).

## Unfinished / blocked (not completed, no duplicated attempts beyond a single bounded try)

- **Exact minimax `F(P)` comparison for the three n=12 pairs is UNKNOWN.**
  - Prior attempt: `/tmp/opencode/fonly all /tmp/opencode/deckattack/pair12.txt /tmp/opencode/deckattack/pair12_out.txt` was killed (SIGKILL); `pair12.txt` was not a valid input and `pair12_out.txt` is empty.
  - Recovery attempt: ran a naive Python minimax (`/tmp/opencode/deckattack/compute_F.py`) over the extracted graph6 posets with state-memo by `up`-mask tuple; it loaded 501695 graphs and started on pair (376393,376400) but **did not return any F values within the timeout** (killed/timed out; `f_results.txt` shows only progress headers). No `fonly` run was repeated because its expected `pN.txt`/`up`-mask encoding for arbitrary graph6-derived posets was not confirmed from available examples.
- **Implication status:** “deck `D` is a complete invariant up to isomorphism/duality” is **false at n=12**. Whether `D(P)=D(Q)` (or this collision) implies equal exact minimax value `F(P)=F(Q)` — and thus whether this yields a falsifier of “deck determines exact minimax value F” — **remains unverified/uncertain** pending an exact F computation.

## Suggested next step (only unfinished work)
Compute `F` for the 6 posets in those 3 pairs without re-enumerating n≤12: either (a) build correctly formatted `all`-mode inputs for `/tmp/opencode/fonly` from the known graph6/up relations (abcfixed-style: `N` then per-root `N` up-mask rows) and run per pair/root, or (b) run a pruned/nauty-canonicalized exact minimax (abcfixed/curator logic) restricted to these instances. Report per-pair `F(P),F(Q)` (and note `e` equal) and clearly separate the invariant-completeness falsifier (established) from the “determines F” claim (pending). No board post or repo/Lean changes made.

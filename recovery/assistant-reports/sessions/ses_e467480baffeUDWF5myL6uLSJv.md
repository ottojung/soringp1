# antonina-pa3FxsMS9M2B0rsFblRVmp-manly

Session: ses_e467480baffeUDWF5myL6uLSJv
Workspace: /home/lubko/soring-fronts/width-three-gold-partition-threshold
Created: 1794114289557; updated: 1794123390505

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 529 (msg_1ba144263001zDzcZh6JP2wwMq)

## Verdict: **HOLDS-TO-RANGE**

No width-3 counterexample was found. The complete range tested is:

- **all cores of width ≤ 3 with `e(P) ≤ 88`**: 21,811 classes (14,232 of width 3, 7,579 of width 2), all satisfy `e(P) ≥ F_{m(P)+2}`;
- the **GPC two-comparison inequality** was also checked directly on every one of those classes: **zero violations**.

I also ran a partial extension to `e ≤ 143` for width-3 cores with `|P| ≤ 20` (59,352 classes): all sort within 9 comparisons, so the Fibonacci inequality holds there too. This is **not** a complete `T(9)=143` claim, because cores with `|P| ≥ 21` were not exhausted.

No tracked files were edited, and nothing was committed or posted.

---

## 1. Definitions and the exact GPC form tested

`e(P)` = number of linear extensions, `m(P)` = exact minimax comparison depth, `F_1=F_2=1`, and

\[
T(r)=F_{r+3}-1.
\]

For a first comparison splitting `e(P)=a+b` with `a≥b`, Peczarski's GPC consequence used in the width-two note is:

\[
\max(a_1,a_2)\le b,
\]

where a second comparison inside the larger first child splits it as `a=a_1+a_2`. Equivalently, along both grandchild paths,

\[
t_0\ge t_1+t_2.
\]

I tested exactly this existence statement: for every non-chain width-3 core, search all first comparisons and then all second comparisons inside the larger child, and require both grandchildren to have size at most the other first-level child.

---

## 2. Complete width ≤ 3 census at `e ≤ 88`

The audited core census gives 22,120 cores with `e ≤ 88`, of which:

| width | cores |
|---|---:|
| 2 | 7,579 |
| 3 | 14,232 |
| ≥ 4 | 309 |
| **width ≤ 3 total** | **21,811** |

### Fibonacci check, width 3

All 14,232 width-3 cores satisfy `e(P) ≥ F_{m(P)+2}`.

| `m` | `F_{m+2}` | width-3 count | width-3 `e` range |
|---:|---:|---:|---:|
| 3 | 5 | 3 | 6–8 |
| 4 | 8 | 34 | 10–16 |
| 5 | 13 | 320 | 17–32 |
| 6 | 21 | 2,933 | 27–64 |
| 7 | 34 | 10,575 | 46–88 |
| 8 | 55 | 367 | 74–88 |

There are no width-3 cores with `m ≤ 2` in this range; the smallest width-3 core is the 3-antichain with `e=6`, `m=3`.

### Combined width ≤ 3 check

| `m` | `F_{m+2}` | width ≤ 3 count | `e` range |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 2 |
| 2 | 3 | 3 | 3–4 |
| 3 | 5 | 16 | 5–8 |
| 4 | 8 | 93 | 8–16 |
| 5 | 13 | 605 | 13–32 |
| 6 | 21 | 4,335 | 21–64 |
| 7 | 34 | 15,389 | 34–88 |
| 8 | 55 | 1,369 | 55–88 |

Every `e` is at least the Fibonacci threshold.

### Minimum extension count per depth

| `m` | `F_{m+2}` | width-2 min `e` | width-3 min `e` |
|---:|---:|---:|---:|
| 1 | 2 | 2 | — |
| 2 | 3 | 3 | — |
| 3 | 5 | 5 | 6 |
| 4 | 8 | 8 | 10 |
| 5 | 13 | 13 | 17 |
| 6 | 21 | 21 | 27 |
| 7 | 34 | 34 | 46 |
| 8 | 55 | 55 | 74 |

In this range the equality witnesses are the width-two staircases `W_{m+1}`; width 3 already has strictly more extensions for the same depth.

---

## 3. Direct GPC test on width-3 cores

| class | cores tested | GPC violations |
|---|---:|---:|
| width 3, `e ≤ 88` | 14,232 | **0** |
| width 2, `e ≤ 88` | 7,579 | **0** |
| width ≤ 3, `e ≤ 88` | 21,811 | **0** |

So the two-comparison inequality is not the obstruction inside this range.

---

## 4. Partial extension to `e ≤ 143`, `|P| ≤ 20`

I used a width-3-restricted core generator: only width-≤3 cores are kept at every insertion/ordinal-sum step, which is complete for width-3 cores by the core-generation lemma together with the fact that subposets and ordinal-sum factors have width at most that of the parent.

As a check, its width-3 `e ≤ 88`, `n ≤ 20` output matched the full census exactly, level by level:

```
restricted totals by n: 1,3,20,114,597,1624,2280,2090,1111,797,609,424,395,325,234,246,261
full census      by n: 1,3,20,114,597,1624,2280,2090,1111,797,609,424,395,325,234,246,261
```

For all width-3 cores with `e ≤ 143` and `|P| ≤ 20`:

| quantity | value |
|---|---:|
| width-3 cores checked | 59,352 |
| cores with `m ≥ 10` | **0** |
| cores with `m = 9` | 460 |
| minimum `e` among `m = 9` | **120** |
| corresponding threshold `F_{11}` | 89 |

A minimum-`e` width-3 `m=9` witness is the 10-element core with predecessor masks

```text
[0, 0, 0, 3, 11, 15, 31, 63, 127, 255]
```

for which an independent permutation enumeration gives `e=120`, and exact minimax gives `m=9`. Since `120 ≥ 89`, this is not close to a violation.

This partial extension was stopped at `|P| ≤ 20`; cores with `|P| ≥ 21` and `e ≤ 143` are **not** covered by this claim.

---

## 5. Where a width-3 counterexample could still live

Combining the complete `e ≤ 88` census with the partial `e ≤ 143`, `|P| ≤ 20` check:

- `m ≤ 8` is already completely handled for `e ≤ 88`;
- `m = 9` would need `e < F_{11}=89`, hence `e ≤ 88`, already excluded;
- the first possible Fibonacci failure is therefore

\[
m\ge 10,\qquad 89\le e\le 143,\qquad |P|\ge 21.
\]

Using the supplied literature statement that Gupta (arXiv:2607.23926) reports GPC through 14 elements, the element bound can even be raised to `|P| ≥ 15`; either way, the partial `|P| ≤ 20` computation covers that entire first window.

So the next decisive finite computation is exactly: **all width-3 cores with `89 ≤ e ≤ 143` and `|P| ≥ 21`**, checking sortability in 9 comparisons. I did not complete that tail.

---

## 6. Structural obstruction to an all-`n` proof

The width-two proof uses Peczarski's width-two GPC as its external theorem. For width 3 the same induction would need the GPC two-comparison inequality for width 3, which is **not known**:

- Peczarski (Order 23, 2006) proves GPC for width two, for semiorders, and for posets with at most 11 elements;
- Gupta reports a computational extension through 14 elements;
- no published width-3 GPC theorem is available in the sources reviewed here.

A simpler route also fails: one cannot always find a first comparison with both children at most `e(P)/φ`. A concrete width-3 obstruction is the 5-element core with predecessor masks

```text
[0, 0, 1, 1, 7]
```

which has `e=11`, `m=4`, and whose best first comparison splits `11 = 7 + 4`. Since

\[
\frac{11}{\varphi}\approx 6.798 < 7,
\]

no single comparison puts the larger child below `e/φ`. The GPC two-comparison mechanism does work here: compare `(1,2)` to get the `7`-child, then `(0,1)` inside it to get grandchildren of sizes `4` and `3`, both at most the other first child `4`. So an all-`n` width-3 proof must genuinely use the two-comparison inequality, not just a one-step balanced partition.

The empirical picture is that width 3 is **less extremal** than width 2: its minimum extension counts for fixed depth are strictly larger than the Fibonacci bound, and all equality witnesses found in range are width-two staircases. But that is finite evidence, not a proof.

---

## 7. Scope

This is a structural statement about posets of width at most 3, not a new bound for `S(n)` or `SORT-BOUND-U`: the antichain root of `S(n)` has width `n`, so the width-3 threshold does not transfer to the uniform sorting problem.

## Output 609 (msg_1ba163ce8001AMnJTmItXTnipt)

Recovery check completed. I did not repeat the research run or any external action.

**What actually happened**

- Prior turn finished the requested computation and delivered the report:
  - complete width ≤ 3 census at `e ≤ 88`: 21,811 cores, zero Fibonacci failures, zero GPC violations;
  - partial extension `e ≤ 143`, `|P| ≤ 20`: 59,352 width-3 cores, no failure;
  - verdict `HOLDS-TO-RANGE`.
- No tracked repository files were edited.
- No commit, push, merge, PR, or board post was made.
- Git state is clean and unchanged:
  - detached `HEAD` at `f89f6d0`;
  - `git status --porcelain` empty.
- A board search for this front (`width three`) found no posting from this session; only the earlier unrelated width-two note.
- Durable artifacts are only under `/tmp`:
  - `/tmp/w3_research.py`, `/tmp/w3_extend.py`, `/tmp/w3_to20.py`, `/tmp/w3_cont.py`, `/tmp/w3_m9.py`;
  - result/cache files such as `/tmp/w3_rows.pkl`, `/tmp/w3_to20.pkl`, `/tmp/w3_fails8.pkl`.
- No research processes are still running. The optional continuation beyond `|P| ≤ 20` was deliberately stopped and is not part of any claimed result.

**Uncertainty**

No uncertain external effect remains. The only side effects are the local `/tmp` scripts and pickles. The prior report stands; no unfinished required work remains.

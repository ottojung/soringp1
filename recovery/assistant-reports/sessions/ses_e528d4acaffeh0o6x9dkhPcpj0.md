# antonina-MbhBhTjaA2v0KCozJyDK5i-excesses

Session: ses_e528d4acaffeh0o6x9dkhPcpj0
Workspace: /home/lubko/soring-fronts/fo-tc-n8-residual-20261024
Created: 1793911338395; updated: 1793911399064

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad72b60a001W2mHiEp1VrqgQo)

I’ll check the repository’s literature and operational constraints, then consult the primary Stober–Weiß source for the reported frontier/profile data. I’ll keep this to a bounded feasibility estimate and won’t launch a search or change files.

## Output 90 (msg_1ad733eb40012Hao2wFWtSiJ72)

## Feasibility verdict

**The repository and Stober–Weiß paper do not provide enough measured data to give a defensible time or memory estimate for resolving \(S(23)\).** They give the target budget and useful algorithmic precedents, but not the per-frontier counts or profiles needed to extrapolate to 23. A large search should not be authorized on this evidence alone.

### Target budget

For the exact-value proof, the search should test whether 23 keys can be sorted within the Ford–Johnson comparison count \(F(23)\); a negative result establishes \(S(23)>F(23)\), while a positive result would not by itself determine \(S(23)\).

Using the standard merge-insertion count \(F(n)=\sum_{i=1}^n\lceil\log_2(3i/4)\rceil\), **\(F(23)=79\)**. The information lower bound is **\(C(23)=\lceil\log_2(23!)\rceil=75\)**. Thus the relevant initial exact-search budget is 79 comparisons; if the test succeeds, the next candidate is 78, then downward. The gap is four comparisons. (These are deductions from the standard Ford–Johnson schedule and information bound; the repository’s literature summary does not tabulate the \(n=23\) row.)

### What the primary source actually measures

Stober–Weiß (ALENEX 2023; [arXiv:2206.05597](https://arxiv.org/abs/2206.05597)) report:

- At \(n=13,\ C=33\): forward search generates **2,032,125** posets; their bidirectional run explores **254,574**. A *full* backward search at this target traverses **682 million** posets, which is why they prune it.
- For \(n=16,17,18\), their computations took about **11, 115, and 89 hours** on a 48-thread, 768-GB machine (repository summary). Their paper explains that the full search spaces could not be stored, and reports that backward advice is loaded into memory for the forward pass.
- The paper’s partial backward search is controlled by the full-layer cutoff \(C_f\) and efficiency threshold \(E_{\rm thr}\). Its Table 2 gives selected configurations and aggregate counts/times; it does **not** give a per-layer frontier profile for \(n=23\), nor an empirically validated scaling law from 18 to 23.
- The repository notes an important caution from Table 2: for \(n=12\), the bidirectional method *increased* the stored-poset count; the reported 6,190 is not a count of special “bottleneck” states. Thus “bidirectional” is not a guaranteed reduction.

These figures establish that the method is real and can be effective, not that \(n=23\) fits a particular machine or time budget.

### Resource envelope and limits

At \(n=23\), the paper’s compact representation needs \(23·22/2+5=\) **258 bits, about 33 bytes per poset**, before hash-table/index overhead. A deliberately optimistic raw-storage illustration is:

| Distinct stored posets | Raw compact records only |
|---:|---:|
| \(10^8\) | 3.3 GB |
| \(10^9\) | 33 GB |
| \(10^{10}\) | 330 GB |

Actual resident memory is higher because of lookup structures, flags, allocator overhead, and simultaneous layers; disk-backed storage also costs extra work. These are capacity conversions, **not predicted frontier sizes**.

A falsifiable planning envelope is therefore conditional: if a bounded pilot’s largest required advice frontier is at most \(10^8\) states and measured peak memory stays within a predeclared budget after indexing, that run may be feasible on a sufficiently provisioned host. If it approaches \(10^9\) states, the compact records alone are tens of GB and a 768-GB-class setup may be needed after overhead; at \(10^{10}\), even raw records exceed that machine’s RAM. No corresponding defensible wall-time bound follows from the published data: the 18-element runtimes do not isolate work per state or provide enough frontier data to scale to 23.

### Resources and a calibration benchmark

Per `docs/operations.md`, manual experiments and local work are authorized on **billy-dev**; GitHub Actions CI is separate and permitted. CI is not evidence of access to a large-memory, long-running research machine, and no CI runner capacity or authorization for a massive search is established here. External published computing is evidence only, not available project capacity. **billy-dev is relevant only if its actual RAM, cores, scratch/durable disk, and runtime allocation are checked against a measured pilot.** I did not inspect or assume those resources.

A useful bounded calibration is to reproduce the paper’s **\(n=13,\ C=33\)** bidirectional configuration, including its stated efficiency bandwidth 0.05, and record per-layer backward and forward counts, peak resident memory, disk traffic, and elapsed time. The published aggregate of 254,574 explored posets is a check on the reproduction; the full-backward 682-million figure is a useful warning, not a pilot target. A reproduction that cannot match the paper’s aggregate—or whose layer profile differs materially—would falsify extrapolation from that implementation. Even a successful calibration would not settle \(n=23\); it would supply a baseline for deciding whether further, still-bounded benchmarks are warranted.

**Bottom line:** budget 79 is clear; frontier sizes and \(n=23\) costs are not. Existing published and repository data are insufficient for a reliable resource commitment. No search, code edit, post, or provisioning was performed.

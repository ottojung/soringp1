# SoringP1 research website

A dependency-free static website generated entirely from the research archive.
It is a reading and discovery interface, not an active research service.

Build locally with Python 3.10+:

    python3 site/build.py
    python3 -m http.server 8000 --directory site/_site

Then open http://localhost:8000. The build is deterministic for a fixed Git
revision. Verify it with `python3 site/verify.py` and `node site/test-search.js`. Its output is not checked into main. The Pages workflow builds
and deploys it on changes to the website or the archive.

The explorer searches titles, metadata and indexed text from the archived
fronts, board messages, source objects, historical patches, assistant
reports, task commissions, mixed-session reports, GitHub discussions,
and curated/canonical documents. Large text files are indexed up to the
first 1 MiB, and compressed experiment outputs by metadata only. Searches
are local to the browser; no external search service or tracking is used.

Evidence tags are historical workflow labels, not proof assessments.
The curated results and corrections pages distinguish established
theorems, independently reproduced computations, open questions and
disputed or refuted claims. Original evidence is always linked.

The site has pre-rendered evidence-graded results, topic, front, board-message, scratch-reference, historical-label and guide pages,
plus paginated collection indexes; these are usable without JavaScript.
The search interface uses a sharded inverted index and loads it on demand.

To activate GitHub Pages for a newly configured repository, select
**Settings → Pages → Build and deployment → Source → GitHub Actions**.
The expected public URL is https://ottojung.github.io/soringp1/.
The administrator must enable Pages once; a default Actions token cannot
activate a disabled Pages site. Thereafter no separate hosting service,
additional token or runtime backend is required.

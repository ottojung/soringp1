#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
export VICHE_TOWN_ROOT=$tmp
export VICHE_PREDICT_LEDGER=$tmp/ledger.json
export VICHE_PREDICT_CALIBRATION=$tmp/calibration.json
mkdir -p "$tmp/records/predictions"
printf 'bill\n' > "$tmp/records/predictions/pilot.tsv"
if VICHE_PREDICT_NOW=90 python3 "$root/government/predict-ledger.py" register \
    --bill no-source --proposition 'No evidence' --probability .5 \
    --resolution-date 1970-01-02 --author seat >/dev/null 2>&1; then
    echo 'registration without a named evidence source unexpectedly passed' >&2; exit 1
fi
if /bin/sh "$root/government/predict-gate.sh" --all --at 100 bill >/dev/null 2>&1; then
    echo 'gate unexpectedly passed without registration' >&2; exit 1
fi
VICHE_PREDICT_NOW=90 python3 "$root/government/predict-ledger.py" register --bill bill --proposition 'Will event occur?' --probability .8 --resolution-date 1970-01-02 --evidence fixture --author seat
# Act 22 §2 registration requires 2–5 predictions; one must not clear the gate.
if /bin/sh "$root/government/predict-gate.sh" --all --at 100 bill >/dev/null 2>&1; then
    echo 'gate accepted only one prediction (Act 22 requires 2–5)' >&2; exit 1
fi
# A registered prediction for a different bill must not open this bill's gate.
if /bin/sh "$root/government/predict-gate.sh" --all --at 100 other-bill >/dev/null 2>&1; then
    echo 'gate incorrectly borrowed another bill prediction' >&2; exit 1
fi
if /bin/sh "$root/government/predict-gate.sh" --all --at 89 bill >/dev/null 2>&1; then
    echo 'gate accepted a prediction registered after the ballot timestamp' >&2; exit 1
fi
VICHE_PREDICT_NOW=90 python3 "$root/government/predict-ledger.py" register --bill bill --proposition 'Will the second event occur?' --probability .2 --resolution-date 1970-01-02 --evidence fixture2 --author seat2 >/dev/null
if ! /bin/sh "$root/government/predict-gate.sh" --all --at 100 bill >/dev/null 2>&1; then
    echo 'gate rejected an earlier prediction for the bill' >&2; exit 1
fi
# Consequential pilot orders use their explicit effect timestamp and the same
# pre-effect registration gate as bills.
printf 'order-1\n' >> "$tmp/records/predictions/pilot.tsv"
if /bin/sh "$root/government/predict-gate.sh" --at 100 order-1 >/dev/null 2>&1; then
    echo 'consequential order passed without preregistration' >&2; exit 1
fi
order_ledger=$tmp/order-ledger.json
for n in 1 2; do
    VICHE_PREDICT_LEDGER=$order_ledger VICHE_PREDICT_NOW=90 \
        python3 "$root/government/predict-ledger.py" register --bill order-1 \
        --proposition "Order outcome $n" --probability .6 \
        --resolution-date 2026-12-01 --evidence fixture --author "seat$n" >/dev/null
done
if ! VICHE_PREDICT_LEDGER=$order_ledger /bin/sh "$root/government/predict-gate.sh" --at 100 order-1 >/dev/null 2>&1; then
    echo 'consequential order gate rejected earlier evidence-linked predictions' >&2; exit 1
fi
future_ledger=$tmp/future-ledger.json
VICHE_PREDICT_LEDGER=$future_ledger VICHE_PREDICT_NOW=90 \
    python3 "$root/government/predict-ledger.py" register --bill future \
    --proposition 'Will the future event occur?' --probability .7 \
    --resolution-date 2026-12-01 --evidence future-source --author seat >/dev/null
if VICHE_PREDICT_LEDGER=$future_ledger VICHE_PREDICT_NOW=100 \
    python3 "$root/government/predict-ledger.py" resolve --id future-registration-1 \
    --outcome true --resolver clerk --evidence future-source#1 --evidence-at 95 >/dev/null 2>&1; then
    echo 'prediction resolved before its resolution date' >&2; exit 1
fi
if VICHE_PREDICT_NOW=90000 python3 "$root/government/predict-ledger.py" \
    resolve --id bill-registration-1 --outcome true --resolver clerk \
    --evidence fixture#early --evidence-at 80 >/dev/null 2>&1; then
    echo 'outcome evidence dated before registration was accepted' >&2; exit 1
fi
if VICHE_PREDICT_NOW=90000 python3 "$root/government/predict-ledger.py" \
    resolve --id bill-registration-1 --outcome true --resolver clerk \
    --evidence fixture#same-time --evidence-at 90 >/dev/null 2>&1; then
    echo 'outcome evidence at registration time was treated as later' >&2; exit 1
fi
if VICHE_PREDICT_NOW=90000 python3 "$root/government/predict-ledger.py" \
    resolve --id bill-registration-1 --outcome unresolved --resolver clerk \
    --reason 'source unavailable' >/dev/null 2>&1; then
    echo 'unresolved result without evidence citation was accepted' >&2; exit 1
fi
VICHE_PREDICT_NOW=90000 python3 "$root/government/predict-ledger.py" resolve --id bill-registration-1 --outcome true --resolver clerk --evidence fixture#1 --evidence-at 90000
VICHE_PREDICT_NOW=90000 python3 "$root/government/predict-ledger.py" resolve --id bill-registration-2 --outcome false --resolver clerk --evidence fixture#2 --evidence-at 90000
python3 "$root/government/predict-scorer.py" --now 90001 >/dev/null
python3 - "$tmp/calibration.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
assert abs(x['brier']['aggregate']-0.04)<1e-8
assert x['coverage']==1.0, x['coverage']
assert x['baselines']['always_0_5']['brier']==0.25
assert abs(x['baselines']['base_rate']['brier']-0.25)<1e-8
assert abs(x['baselines']['base_rate']['skill_vs_ledger']-0.84)<1e-8
assert x['counts']['unresolved']==0
authors={a['author']:a for a in x['per_author']}
assert abs(authors['seat']['brier']-0.04)<1e-8
assert authors['seat']['coverage']==1.0
assert abs(authors['seat']['baselines']['always_0_5']['skill_vs_ledger']-0.84)<1e-8
assert authors['seat']['baselines']['base_rate']['skill_vs_ledger'] is None
assert authors['seat']['log_score'] is not None
assert 'reliability' in authors['seat'] and 'discrimination' in authors['seat']
PY
# A resolution is part of the append-only evidence ledger: changing only its
# outcome must create an integrity defect and the scorer must exclude it.
resolution_tamper=$tmp/resolution-tamper.json
cp "$tmp/ledger.json" "$resolution_tamper"
python3 - "$resolution_tamper" <<'PY'
import json,sys
p=sys.argv[1]; x=json.load(open(p)); x['resolutions'][0]['outcome']='false'
open(p,'w').write(json.dumps(x))
PY
if VICHE_PREDICT_LEDGER=$resolution_tamper python3 "$root/government/predict-ledger.py" verify >/dev/null 2>&1; then
    echo 'resolution outcome tamper escaped integrity verification' >&2; exit 1
fi
VICHE_PREDICT_LEDGER=$resolution_tamper \
VICHE_PREDICT_CALIBRATION=$tmp/resolution-tampered-calibration.json \
    python3 "$root/government/predict-scorer.py" --now 90001 >/dev/null
python3 - "$tmp/resolution-tampered-calibration.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1])); assert not x['integrity']['clean']
assert x['counts']['resolved_scored']==1, x['counts']
assert x['counts']['due_unresolved']==1, x['counts']
assert [r['id'] for r in x['brier']['per_prediction']]==['bill-registration-2']
assert any(d['defect']=='resolution_content_hash_mismatch' for d in x['integrity']['defects'])
PY
# Add a due prediction that remains unresolved: coverage must reflect the
# unresolved registration, while the score must exclude it.
VICHE_PREDICT_NOW=90 python3 "$root/government/predict-ledger.py" register --bill bill2 --proposition 'Will another event occur?' --probability .2 --resolution-date 1970-01-02 --evidence fixture2 --author seat2 >/dev/null
VICHE_PREDICT_NOW=90 python3 "$root/government/predict-ledger.py" register --bill bill3 --proposition 'Will unavailable event occur?' --probability .7 --resolution-date 1970-01-02 --evidence unavailable-source --author seat3 >/dev/null
VICHE_PREDICT_NOW=90001 python3 "$root/government/predict-ledger.py" resolve --id bill3-registration-1 --outcome unresolved --resolver clerk --evidence unavailable-source#missing --reason 'named source unavailable' >/dev/null
python3 "$root/government/predict-scorer.py" --now 90001 >/dev/null
python3 - "$tmp/calibration.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1])); assert abs(x['coverage']-3/4)<1e-3, (x['coverage'],x['counts'])
assert x['counts']['due_unresolved']==1, x['counts']
assert x['counts']['unresolved']==1
assert x['counts']['resolved_scored']==2
PY
# Act 20 P1–P5 carry-forward records remain a separate checkpoint block, not
# Brier registrations. No fake probabilities or second registration are added.
checkpoint_ledger=$tmp/checkpoint-ledger.json
for checkpoint in P1 P2 P3 P4 P5; do
    VICHE_PREDICT_LEDGER=$checkpoint_ledger VICHE_PREDICT_NOW=90 \
        python3 "$root/government/predict-ledger.py" add-review-checkpoint \
        --id "$checkpoint" --proposition "Statutory checkpoint $checkpoint" \
        --resolution-date 2026-12-01 --evidence act20-report \
        --author c1e00011 --source-ref government/LAWS.md#act-20-section-7 \
        --source-registered-on 2026-10-20 >/dev/null
done
VICHE_PREDICT_LEDGER=$checkpoint_ledger \
VICHE_PREDICT_CALIBRATION=$tmp/checkpoint-calibration.json \
    python3 "$root/government/predict-scorer.py" --now 100 >/dev/null
python3 - "$tmp/checkpoint-calibration.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1])); cps=x['review_checkpoint']['checkpoints']
assert x['counts']['registered']==0, x['counts']
assert [c['id'] for c in cps]==['P1','P2','P3','P4','P5']
assert all(c['registered'] and c['resolution']=='pending' for c in cps), cps
assert all(c['integrity']=='clean' for c in cps), cps
PY
python3 "$root/government/predict-ledger.py" verify >/dev/null
# The registration time is hash-bound; changing only it cannot make a late
# prediction appear pre-registered to the ballot gate.
timestamp_tamper=$tmp/timestamp-tamper.json
cp "$tmp/ledger.json" "$timestamp_tamper"
python3 - "$timestamp_tamper" <<'PY'
import json,sys
p=sys.argv[1]; x=json.load(open(p)); x['entries'][0]['registered_at']=99
open(p,'w').write(json.dumps(x))
PY
if VICHE_PREDICT_LEDGER=$timestamp_tamper python3 "$root/government/predict-ledger.py" verify >/dev/null 2>&1; then
    echo 'registration timestamp tamper escaped integrity verification' >&2; exit 1
fi
if VICHE_PREDICT_LEDGER=$timestamp_tamper /bin/sh "$root/government/predict-gate.sh" --all --at 100 bill >/dev/null 2>&1; then
    echo 'gate accepted tampered registration timestamps' >&2; exit 1
fi
# A scorer detects tampering and excludes the compromised prediction.
scorer_tamper=$tmp/scorer-tamper.json
cp "$tmp/ledger.json" "$scorer_tamper"
python3 - "$scorer_tamper" <<'PY'
import json,sys
p=sys.argv[1]; x=json.load(open(p))
next(e for e in x['entries'] if e.get('kind')=='registration')['probability']=.01
open(p,'w').write(json.dumps(x))
PY
VICHE_PREDICT_LEDGER=$scorer_tamper \
VICHE_PREDICT_CALIBRATION=$tmp/tampered-calibration.json \
    python3 "$root/government/predict-scorer.py" --now 90001 >/dev/null
python3 - "$tmp/tampered-calibration.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
assert not x['integrity']['clean']
assert x['counts']['resolved_scored']==1
assert [r['id'] for r in x['brier']['per_prediction']]==['bill-registration-2']
PY
python3 - "$tmp/ledger.json" <<'PY'
import json,sys
p=sys.argv[1]; x=json.load(open(p)); x['entries'][0]['proposition']='tampered'; open(p,'w').write(json.dumps(x))
PY
if python3 "$root/government/predict-ledger.py" verify >/dev/null 2>&1; then
    echo 'tamper unexpectedly passed' >&2; exit 1
fi
# A bill ID cannot be rebound after registration: the ID is part of its hash,
# and the gate runs the integrity verifier before trusting the ledger.
rebound=$tmp/rebound.json
for n in 1 2; do
    VICHE_PREDICT_LEDGER=$rebound VICHE_PREDICT_NOW=90 \
        python3 "$root/government/predict-ledger.py" register --bill other-bill \
        --proposition "Other bill proposition $n" --probability .7 \
        --resolution-date 2026-12-01 --evidence fixture --author "seat$n" >/dev/null
done
python3 - "$rebound" <<'PY'
import json,sys
p=sys.argv[1]; x=json.load(open(p))
for e in x['entries']: e['bill_id']='bill'
open(p,'w').write(json.dumps(x))
PY
if VICHE_PREDICT_LEDGER=$rebound python3 "$root/government/predict-ledger.py" verify >/dev/null 2>&1; then
    echo 'ledger bill-id rebinding escaped integrity verification' >&2; exit 1
fi
if VICHE_PREDICT_LEDGER=$rebound /bin/sh "$root/government/predict-gate.sh" --all --at 100 bill >/dev/null 2>&1; then
    echo 'gate accepted bill-id-rebound registrations' >&2; exit 1
fi
# The legal upper bound is five as well as the lower bound two.
for n in 1 2 3 4 5 6; do
    VICHE_PREDICT_NOW=90 python3 "$root/government/predict-ledger.py" register \
        --bill too-many --proposition "Prediction $n" --probability .6 \
        --resolution-date 2026-12-01 --evidence fixture --author "author$n" >/dev/null
done
if /bin/sh "$root/government/predict-gate.sh" --all --at 100 too-many >/dev/null 2>&1; then
    echo 'gate accepted more than five predictions (Act 22 maximum is five)' >&2; exit 1
fi
echo 'predict-smoke: passed'

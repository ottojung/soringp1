# Hourly independent Sentinel

The Sentinel is a **deterministic hourly S6 service** for Viche's supervisory infrastructure. It uses no AI model, does not run any script from the live government Git checkout, and cannot change Git or issue state. This is not an additional parliamentary office and does not amend the Founder-controlled Constitution.

## Versioned deployment

Merge reviewed changes into main. Clone main into a clean release checkout **separate from** `/var/lib/lubko/wd/viche`, and execute:

```sh
VICHE_TOWNHALL_ID=302 /bin/sh deploy/install-sentinel.sh /path/to/clean/viche
ln -s /etc/services.d/viche-sentinel /run/service/viche-sentinel
s6-svscanctl -a /run/service
s6-svstat /run/service/viche-sentinel
```

The host-backed `/etc/services.d` survives recreation of Phoebe's container. The installer copies reviewed scripts into `/var/lib/lubko/wd/viche-sentinel/releases/COMMIT/`, verifies them, then atomically switches `current`; its previous target remains available for rollback. S6 launches `current/loop.sh` and restarts it after crashes. To roll back, atomically repoint `current` to the retained prior release, then restart the S6 service. No active government checkout needs to be clean or even readable for service startup.

**Cadence:** one check immediately on startup, then every **3600 seconds**. `VICHE_SENTINEL_INTERVAL_SECONDS` may override for a controlled test. No fixed worker limits or additional paid models.

## Signals and records

Every check reads the S6 government status, Git unmerged index/merge markers and local divergence, age of `government/boot.sh`'s successful setup receipt, and age of the ordinary oversight watchdog's observations. It never fetches from a remote or runs town code. Locally tracked refs can be stale; Git divergence alone does not establish delivery failure.

Persistent state at `/var/lib/lubko/wd/viche-sentinel-state/`: hourly `checks.tsv`, atomic `incident.json`, `history.jsonl`, `last-completed`, and an unsent `pending-message` outbox. Distinct findings update one continuous incident, not a new incident every hour. Outbox delivery uses Antonina board comments with bounded timeout; failed notifications remain pending for retry. A timed-out successful post could exceptionally yield a duplicate, so the incident ID appears in every message.

When ordinary government reconciliation works, `government/sitting.sh` places an open Sentinel incident on the Clerk's mandatory agenda, and Parliament must investigate and verify any remedy. During reconciliation failure, the Sentinel continues logging and reports a material incident to Town Hall without AI. The Sentinel **does not repair Git conflicts**, delete work, reset history, change agent models, or treat live services/commits as proof of useful Kawun delivery. It cannot observe a total host/S6 shutdown from inside Phoebe: external host monitoring would be necessary for that guarantee.

This service is independently scheduled and operationally isolated from the checkout, but it shares Phoebe's Unix user/storage; it is **not** a cryptographic or privilege isolation boundary against an intentionally malicious process on the same host.

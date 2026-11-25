# Independent Viche recovery service

The three branches can all fail simultaneously. A separate **general-purpose
AI recovery steward** must therefore remain summonable even when legislative,
executive and judiciary boot/appointments are unhealthy.

Install `deploy/s6/viche-recovery/run` as the persistent S6 entrypoint at
`/etc/services.d/viche-recovery/run` on the Viche execution machine.
The minimal supervised loop is
`government/recovery-steward-service.sh`; the launch-only transaction is
`government/recovery-steward-cycle.sh`. The *actual investigation and repair
authority* is the broad, editable `government/RECOVERY-STEWARD.md` agent
mandate, subject to the Founder Constitution and current laws.

This is an Executive-support operational investigator, not a government
branch, voter, judge or autonomous lawmaker. The independent service makes
no substantive policy or repair decisions. It preserves terminal evidence,
never replays uncertain old tools, and appoints a fresh investigator after
the previous agent dies. Every new invocation must re-check all relevant
signals and the actual utility of Viche's downstream deliveries.

Do not disable the service just because the Clerk/Executive/recovery scripts
are broken. Changes to operational behavior require signed, reviewed commits
and the applicable Viche quality gate. Keep the Founder-controlled bootstrap
and charter separately protected.

#!/bin/sh
set -eu
repo=${1:?Provide clean release checkout}
: "${VICHE_TOWNHALL_ID:?Host Town Hall ID required}"
[ -z "$(git -C "$repo" status --porcelain)" ] || exit 1
sha=$(git -C "$repo" rev-parse HEAD)
root=${VICHE_SENTINEL_ROOT:-/var/lib/lubko/wd/viche-sentinel}
services=${VICHE_SENTINEL_SERVICES:-/etc/services.d}
mkdir -p "$root/releases/$sha" "$services/viche-sentinel"
for file in check.sh loop.sh; do
  install -m 0555 "$repo/sentinel/$file" "$root/releases/$sha/$file"
  cmp "$repo/sentinel/$file" "$root/releases/$sha/$file"
done
if [ -L "$root/current" ]; then
  ln -s "$(readlink "$root/current")" "$root/previous.$sha"
fi
ln -s "releases/$sha" "$root/next.$$"
mv -Tf "$root/next.$$" "$root/current"
{ printf '#!/bin/sh\nexport VICHE_TOWNHALL_ID=%s\n' "$VICHE_TOWNHALL_ID"; sed '1d' "$repo/deploy/s6/viche-sentinel/run"; } > "$services/viche-sentinel/run.next"
chmod 0755 "$services/viche-sentinel/run.next"
mv -f "$services/viche-sentinel/run.next" "$services/viche-sentinel/run"
printf 'Installed Sentinel %s\n' "$sha"

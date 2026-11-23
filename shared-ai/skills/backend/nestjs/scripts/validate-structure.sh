#!/usr/bin/env bash
# Read-only structural smoke check. Source contents are never executed.
set -eu

if [[ $# -lt 1 || $# -gt 2 || ! -d "$1" ]]; then
  printf 'Usage: %s <project-dir> [entry-relative-to-project]\n' "$0" >&2
  exit 2
fi

root=$(CDPATH= cd -- "$1" && pwd -P)
entry=${2-src/main.ts}
if [[ -z "$entry" || "$entry" == /* || "/$entry/" == */../* ]]; then
  printf 'Entry must be a project-relative path without parent traversal.\n' >&2
  exit 2
fi

failed=0
for path in package.json "$entry"; do
  if [[ ! -f "$root/$path" || ! -s "$root/$path" ]]; then
    printf 'Missing or empty: %s\n' "$path" >&2
    failed=1
  fi
done
if (( failed == 0 )); then
  printf 'NestJS structure OK: package.json and %s\n' "$entry"
fi
exit "$failed"

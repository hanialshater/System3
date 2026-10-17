#!/usr/bin/env bash
# Replays vercel.json's ignoreCommand, as it stood at aefb10a, against saved commit messages (record item C1).
# Vercel semantics: ignoreCommand exit 1 = BUILD (deploy), exit 0 = skip ("Canceled by Ignored Build Step").
# Runs in an empty temp dir, so the `git log` fallback finds no repo and only VERCEL_GIT_COMMIT_MESSAGE decides.
set -u
here="$(cd "$(dirname "$0")" && pwd)"
cmd="$(node -e 'process.stdout.write(JSON.parse(require("fs").readFileSync(process.argv[1],"utf8")).ignoreCommand)' "$here/vercel.json.at-aefb10a")"
tmp="$(mktemp -d)"
for f in "$here"/messages/*.txt; do
  c="$(basename "$f" .txt)"
  ( cd "$tmp" && VERCEL_GIT_COMMIT_MESSAGE="$(cat "$f")" bash -c "$cmd" >/dev/null 2>&1 ); rc=$?
  if [ $rc -eq 1 ]; then v=BUILD; else v=skip; fi
  echo "${c:0:9} rc=$rc $v  subject: $(head -1 "$f" | cut -c1-70)"
done
rm -rf "$tmp"

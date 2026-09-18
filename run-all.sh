#!/usr/bin/env bash
# Run every solution file and report which ones fail their assertions.
# Usage: ./run-all.sh [topic-dir]
set -uo pipefail

target="${1:-.}"
pass=0
fail=0
failed_files=()

while IFS= read -r -d '' file; do
    if output=$(python3 "$file" 2>&1); then
        pass=$((pass + 1))
    else
        fail=$((fail + 1))
        failed_files+=("$file")
        printf '\033[31mFAIL\033[0m %s\n' "$file"
        printf '%s\n' "$output" | sed 's/^/     /'
    fi
done < <(find "$target" -name '[0-9]*.py' -not -name 'TEMPLATE.py' -print0 | sort -z)

printf '\n%d passed, %d failed\n' "$pass" "$fail"
[[ $fail -eq 0 ]] || exit 1

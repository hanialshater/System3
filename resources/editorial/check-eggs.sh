#!/usr/bin/env bash
# Checks the easter-egg anchors listed in easter-egg-register.md.
# CONFIRMED seeds fail the check (exit 1). PROPOSED seeds only warn.
# Usage: resources/editorial/check-eggs.sh   (run from the repository root)
set -u
cd "$(dirname "$0")/../../chapters" || exit 2
fail=0
check () { # tier file anchor
  if [ -f "$2" ] && grep -qF -- "$3" "$2"; then printf 'ok    %-9s %-40s %s\n' "$1" "$2" "$3";
  elif [ "$1" = confirmed ]; then printf 'FAIL  %-9s %-40s %s\n' "$1" "$2" "$3"; fail=1;
  else printf 'warn  %-9s %-40s %s\n' "$1" "$2" "$3"; fi
}
check confirmed 00-preface.md "Your coffee is still too hot."
check confirmed 02-the-algorithm-vortex.md "## The Coffee Test"
check confirmed 10-fluent-autonomy.md "## The Second Coffee Test"
check confirmed 13-the-prophecy.md "Decaf."
check proposed 01-why-im-betting-on-ai-agents.md "octopuses: eight-armed problem-solvers"
check proposed 04-system-3.md "hyper-intelligent octopus"
check proposed 12-after-capacity.md "It requires an octopus"
check proposed 13-the-prophecy.md "Hadn’t the octopus dreamed it was love?"
check proposed 00-preface.md "at least one loose cable"
check proposed 04-system-3.md "taps an undersea cable"
check proposed 05-the-society-of-agents.md "One of the culprits was a loose cable."
check proposed 13-the-prophecy.md "Shark biting cables."
check proposed 04-system-3.md "*Can your tongue touch your ear?*"
check proposed appendix-zen-of-system-3.md "The tongue cannot reach the ear."
check proposed 13-the-prophecy.md "But so would simulated fingers touching a simulated face."
check proposed 01-why-im-betting-on-ai-agents.md "Do you bet on DNA, a biological fax machine"
check proposed 13-the-prophecy.md "Your DNA is just a fax machine"
check proposed 04-system-3.md "consider a camel"
check proposed 11-the-store-that-builds-itself.md "And now the camel comes back"
check proposed 12-after-capacity.md "camels are native to Croatia"
check proposed 07-recursive-self-improvement.md "The Learner Dreams, and the Dream Can Be Wrong"
check proposed 13-the-prophecy.md "hadn’t he dreamed he was an octopus?"
check proposed 00-preface.md "Eventually there is a cathedral"
check proposed 03-deep-mode.md "A Cathedral on a Shopping Cart"
check proposed 05-the-society-of-agents.md "with no one standing outside it"
check proposed 13-the-prophecy.md "Behind it: forty monitors. Every timeline."
check proposed 00-preface.md "Capacity over power."
check proposed 12-after-capacity.md "## Capacity Over Power"
check proposed 13-the-prophecy.md "Capitalism doesn’t."
check proposed 00-preface.md "we never thought to call it an architecture"
check proposed 12-after-capacity.md "In October 1947"
check proposed 13-the-prophecy.md "11:53 PM, three minutes."
check confirmed 01-why-im-betting-on-ai-agents.md "Reviewer 2"
check confirmed 02-the-algorithm-vortex.md "Reviewer 2"
# New material (added with the part structure)
check proposed alternative-ending.md "An Alternative Ending"
check proposed reveal-we-call-it-science.md "We call it science."
exit $fail

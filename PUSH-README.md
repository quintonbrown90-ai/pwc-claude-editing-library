# PUSH — how this becomes the repo Q's Claude pulls from

This tree is PUSH-READY. It is NOT yet pushed — the parent (main agent)
runs the push after confirming TWO things with Q:
1. Repo name (suggested: pwc-claude-editing-library)
2. Visibility: PRIVATE (recommended — this is Q's prompt library and
   editing system) vs PUBLIC.

## Exact commands (run from ~/workspace/claude-editing/github-repo/)
gh repo create pwc-claude-editing-library --private --source=. --remote=origin --push
# then verify: gh repo view pwc-claude-editing-library --web

## What the repo carries
- parts/ — all 79 modular parts in 19 categories (the pull route: Claude
  fetches any part on demand by path)
- CATEGORIES.md — the category index (repo README links here)
- design-system/ + skills-distilled/ — the distilled skill sources
- SAFETY.md, CONTINUOUS-LEARNING.md, INDEX.md — the operating docs

## What it NEVER carries (.gitignore enforced)
Raw videos (.mp4/.mov), audio, zips, tarballs, venvs, node_modules,
archives/, research video dumps. The folder stays the master archive for
raw material; the repo carries distilled knowledge only.

## After the push
- Record the repo URL in INDEX.md + CATEGORIES.md.
- The weekly sweep updates this tree (new parts) and pushes on the same
  remote. Claude's pull route: fetch parts/<category>/<part>.md by path.

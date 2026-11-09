# SAFETY PROTOCOL — claude-editing harvest (Q's order, Nov 8, 2026)

**Be safe. No hacks, no scams, no phishing.** Every download that enters this
folder runs through this protocol. No exceptions — not for a creator Q likes,
not for a repo with 29K stars, not for something already half-folded in.

## 1. QUARANTINE

Every download (video, repo, skill zip, prompt pack, PDF, script) lands
FIRST in `uploads/QUARANTINE/`. Nothing moves into `skills/`, `code/`, or the
Claude zips until it passes review (§4). Quarantine is the default state;
promotion is the exception.

```
uploads/QUARANTINE/<item-name>/   ← raw download, untouched
research/<stream>/<name>/         ← only after review passes
skills/ | code/ | zips/           ← only after review + scan pass
```

## 2. NEVER RUN untrusted code

- No executing scripts, installers, or binaries from harvested material
  without reading them first — every line, or the item stays parked.
- No `curl | bash`, no `wget | sh`, no pip/npm install from unknown sources
  without inspecting the package first.
- Claude Code skills are TEXT + scripts. Read every script before it runs.
- Never run a harvested skill's install/setup script on the main machine
  without reading it. If it needs a key, a login, or a download from a third
  host, that is a flag (§4).

## 3. NEVER enter credentials or API keys in the harvest

- No "free Claude Pro" sign-ups, no key-gated "free" tools that ask for
  logins, no OAuth grants to unknown apps.
- A tool that requires an API key is not automatically suspicious — but the
  key is Q's, entered only by Q in the official place, never pasted into a
  harvested script, form, or chat. Note free tiers where they exist
  (ElevenLabs, Groq) and move on.
- Never paste Q's credentials, tokens, or session data into any harvested
  material, repo issue, or third-party page.

## 4. VERIFY sources before trusting content

Check the creator/repo is real before trusting its content:
- Account age, followers, stars, README quality, LICENSE file present,
  last push date, cross-check across TWO sources.
- A repo with no README, no license, and 2 stars is not a source — park it.

## 5. EXCLUDE on sight

Flag and EXCLUDE (park with the reason — never fold in):
- Fake giveaway / "free Claude Pro" links.
- Credential-harvesting pages (asks for a login to download).
- "Download this tool to unlock" flows.
- Obfuscated code, base64 blobs, packed/minified scripts with no readable
  source.
- Exfiltration: code that sends files, keys, env vars, or clipboard contents
  outward to an external host.
- Crypto miners, wallet/seed-phrase requests, anything touching
  `~/.ssh`, `~/.aws`, keychains, browser credential stores.
- Paywalled or pirated content (same rule as the harvest briefs).

## 6. SCAN — before any harvested code is folded in

Grep every harvested code/script folder for red flags and record the result
in its SOURCES.md (`SCAN: pass | flag — <what was found>`):

```bash
grep -rInE "requests\.|urllib|socket|curl|wget|fetch\(|XMLHttpRequest" <dir>
grep -rInE "os\.environ|process\.env|~/.ssh|~/.aws|keychain|getpass|readline" <dir>
grep -rInE "eval\(|exec\(|subprocess|os\.system|child_process" <dir>
grep -rInE "base64|fromhex|atob|btoa" <dir>
grep -rInE "seed|mnemonic|wallet|private[_-]?key" <dir> --include="*.py" --include="*.js" --include="*.sh"
```

- **Pass:** no hits beyond what the tool legitimately needs (e.g. a
  downloader that fetches a public video URL is fine — note it; a script
  that reads `~/.ssh` is not).
- **Flag:** any hit that cannot be explained by the tool's stated purpose →
  item is PARKED with the reason in SOURCES.md + the INDEX. Never folded in,
  never staged as a zip.
- Scripts that only run locally with no network and no credential access
  (e.g. ffmpeg wrappers, caption renderers) are the lowest-risk class.

## 7. Only public, freely licensed material is ever used

MIT / Apache-2.0 / BSD / CC BY / clearly-public tutorials only, license
recorded in SOURCES.md. License-unclear = parked. Paywalled = excluded.
Non-commercial licenses (e.g. CC BY-NC) are flagged loud and never staged
as a skill without Q's explicit word.

## 8. Reporting

Every report to Q lists: items harvested, items PARKED as suspicious with
the reason, and scan results for anything folded in. Q explicitly wants to
know what got kept out and why.

---
## 9. Independent confirmation — the dual-model safety review (Jack Roberts, Nov 8, 2026)

Q's quarantine-first rule is confirmed from an independent source. Jack Roberts, teaching the Find Skills meta-skill (a skill whose whole job is finding and installing other skills), states the rule in his own words:

> "But importantly, never install the skill until you run it through ChatGPT and Claude to make sure it's safe."

— Jack Roberts (@jackroberts___), reel DePtyBoAOPd, 31.3–36.8s (transcript, parent-decoded Nov 8, 2026). Caption: "Skim each one before it runs."

The doctrine, as a rule: **no skill is installed until its SKILL.md has been run through TWO models (ChatGPT + Claude) for a safety review.** One model is not enough — the review is dual-model by definition. If either model flags it, the skill is PARKED, not installed "carefully".

The visual that teaches it — the clearest exfiltration-check visual in the harvest (frame f_035, DePtyBoAOPd): ChatGPT + Claude icons above a SKILL.md reading "# unknown-skill, description: …, steps: - read files - run script - ~~send data~~" with the "send data" step struck out and a gold X. The check strikes out the data-exfiltration step. That frame IS the safety doctrine: read the steps, strike the exfiltration, refuse the install. Reusable (PWC skin: the strike maps to gold) in Q's own safety teaching.

This confirmation does not change the protocol — quarantine first (§1), SCAN PASS (§6), no credentials ever, only public freely-licensed material (§7) all still bind. It confirms them from outside Q's operation: the creator whose lane is installing other people's skills states the same rule Q's library already enforces. The dual-model review is now written here as its own section so the confirmation is on the record, not just in a decode file.

Source file: `research/video-harvest/instagram/jack_roberts_DePtyBoAOPd_DECODE.md` ("The safety doctrine (his words — adopt as a rule)").

*Enforced in every phase. The weekly sweep runs the same protocol — see
CONTINUOUS-LEARNING.md, "Weekly loop", step 2 (vet + quarantine + scan).*

## Variants (v9)
- **v9 · @agi_point, DfTB2aCiCd1 / DfTRYzSgTwA:** 66. @agi_point, DfTB2aCiCd1 / DfTRYzSgTwA — Nvidia Skill Spector ("anti-virus for skills") → variant on SAFETY.md §6/§9 (the scan-before-install rule is already the doctrine; the product is the enforcement). Differs: none — the doctrine already covers it. Setup guide gated; "7 billion free AI tokens / 600+ models / 60+ styles / 50% less code" unverified (GAP). DfTRYzSgTwA is a duplicate of DfTB2aCiCd1. _(source: v9_variants_bulk_a.md)_

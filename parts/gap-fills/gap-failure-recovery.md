<!-- PART: gap-fills/gap-failure-recovery.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# GAP-FILL — Failure recovery [Q didn't ask, mastermind added]

Source: AGENTS.md lessons (Oct 10–Nov 8): TTS defects, staging 500s,
timeouts that posted anyway, moov-at-end, approval expiry, queue
deadlocks. Mark: GAP-FILL.

## The rule
Every failure has a named next step. Never retry blindly, never assume a
failure means "nothing happened."

## The playbook
| Failure | What actually happened | Next step |
|---|---|---|
| IG staging HTTP 500, one file | Moov atom at end of file | Lossless faststart remux; if it still 500s, full re-encode (crf 23, yuv420p, 30fps, faststart); if THAT 500s, the fault is IG/caption-side — park it |
| IG staging 500, 2160x3840 file | Reels serve at 1080 wide | Downscale to 1080x1920 (29MB posted in ~1 min where 93MB 4K failed for 16 min) |
| CLI timeout (180s) after approval | Post often WENT LIVE; CLI never got confirmation | Check the account's recent posts for the caption signature BEFORE retrying — a retry posts a duplicate |
| TTS segment too long / looping | Backend returned a repeated phrase and CACHED it | Alter punctuation inaudibly (periods→commas) to bust the cache; verify duration 0.6–1.6× expected before rebuilding |
| TTS truncated / quiet tail | Backend returned short audio reported as OK | Verify segment durations vs word count (~200 wpm) + tail volume before assembling |
| Approval card expired (~10 min) | Q missed it; post NOT performed | Keep it in the queue; re-fire as soon as he's back; greet him with "I'm ready" — never silently drop it |
| A post flops (low views) | Usually 2–3 fixable dip moments | Retention-dip re-edit at the drop-offs (martinwang case) before deleting; deletion needs Q's word + a profile-list duplicate check, never a direct link |
| A render fails QC (freeze, dead air) | Builder said done; export says otherwise | Quarantine, fix, re-render, re-run the FULL gate — a re-cut re-opens every gate |
| Queue deadlock (pgrep self-match) | A wait loop matched its own command line | Sequence queue work inside ONE process; wait on a lock/PID file, never pgrep on your own string |

## Executable steps
1. Name the failure from the table before acting. If it isn't in the
   table, log it (what failed, what the evidence showed, what fixed it)
   and add the row — the table grows.
2. Verify the real state before retrying (is it live? is the file
   actually broken? is the queue actually stuck?).
3. Report the failure + the fix in one plain sentence. A fix that isn't
   written down will be re-learned the expensive way.

## Worked example
VID-M01-3 failed staging twice — moov-at-end, then again after the
faststart remux. Full re-encode fixed it. The table row exists so the
next M01-3 costs minutes, not a day.

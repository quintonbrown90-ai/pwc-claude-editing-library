<!-- PART: creator-systems/claude-eyes-watch.md | UPLOAD: SKILL + GITHUB | MAX: 50KB / 10 files -->
# CREATOR SYSTEMS — give Claude eyes: /watch (download → frames → transcript)

Source: @_mosvlih reel DfLFqtOubn8 (the /watch command) + @build.with.alan
reel DbVirYiPtu- (yt-dlp + ffmpeg, "give Claude eyes") + @davis.mcm reel
Det2_FPo9Ni (6-step video-editing-as-coding; step 3 loads "a watch skill
so Claude can actually watch" — variant). All PUBLISHED (spoken verbatim
+ on-screen text). The EYES link (Alan) is GATED behind comment EYES —
never chased. Rebuild from the visible specs only, INFERRED where the
build is described but not shown.

## The rule
"Claude only reads a video's transcript, so it misses everything
happening on screen." The transcript alone misses the screen; the
frames are the eyes.

## Executable steps
1. **/watch (Mosvlih):** "Claude can't watch Instagram videos. You
   paste a real link and it just says it can't see it. So I built a
   command so it can. It's called Watch." "You give it a link, it
   downloads the video, pulls out the frames and writes down every
   word that's said. Then Claude looks at the frames and reads the
   transcript. So it actually watches the reel, like you would." "And
   when it's done, it deletes the video so your storage doesn't fill
   up." Build it: "just tell Claude Code, make me a command that
   downloads a video from a [link]…" (his build line, as spoken).
2. **The two skills (Alan):** "The first is Y-T-D-L-P. It downloads
   the video for Claude to process. The second is F-F-M-P-E-G. It
   extracts every frame, so Claude can analyze the video frame by
   frame instead of relying only on the transcript. That means you can
   break down reels, shorts, YouTube videos, or even a 30-minute
   recording with far more context." "Runs locally, fast, zero API
   fees."
3. **What the eyes are for:** break down a reel (hook, pacing, devices,
   proof — the harvest's own decode shape); study references frame by
   frame (the davis.mcm step-2 use: "Claude watches them frame by
   frame and writes down the style. Fonts, colors, pacing, motion.");
   verify a render on its own frames (the self-check shape: screenshot
   every 0.25s, flag overlaps and crops).
4. **The hygiene rules (from the sources, stated as rules):** download
   → frames + transcript → analyze → DELETE the video when done
   (Watch deletes it so storage doesn't fill up); local only, no
   credentials, no logins; public reels only — never log into
   Instagram, never scrape behind a login.

## Worked example (PWC)
This harvest IS the method: yt-dlp + ffmpeg + transcript + frames
produced 630 decodes, and this part is the method written down as a
command. Q's use: "/watch @realskytan <reel link>" → frames + transcript
→ decode → the steal lands in the library as a part, a variant, or a
GAP. Keyword WAITLIST.

## Human-made check
The frames are the check on the transcript — ASR mis-hears ("Claude"
as "Clawed/Cloud/Clot/Flood"), and the frames are what correct it. A
decode that trusts the transcript alone is a decode with invented
words in it.

## PWC skin
No new tool is installed by this part — yt-dlp and ffmpeg are already
in Q's operation. The command is local-only; nothing uploads, nothing
phones home, nothing asks for a login. The gated EYES link stays gated
(GAP).

## Variants (v9)
- **v9 · @?, ?:** 91. @_mosvlih, DfLFqtOubn8 / @build.with.alan, DbVirYiPtu- — /watch + yt-dlp/ffmpeg eyes → folded into the new draft claude-eyes-watch.md. EYES link gated (GAP). _(source: v9_variants_bulk_a.md)_

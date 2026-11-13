#!/usr/bin/env python3
"""Build the Devin corpus inventory + video manifest from Q's existing pulls.

No network. Copies one file per unique shortcode from the batch-11 pull,
the motion-ref duplicates are de-duplicated, and Dd3x4cMStzs is taken from
the separate devin-reel-2 teardown folder.
"""
import json, os, re, shutil, glob, hashlib

ROOT = "/home/hatch/workspace/your_files/devin-exact-nov13"
BATCH = "/home/hatch/workspace/claude-editing/research/video-harvest/instagram/batch-11-devin"
STYLE_DECODES = "/home/hatch/workspace/claude-editing/styles/devin-edit-style/examples/decodes"
REEL2 = "/home/hatch/workspace/claude-editing/research/video-harvest/instagram/devin-reel-2"
INV = os.path.join(BATCH, "devinjatho_inventory_union.json")

os.makedirs(os.path.join(ROOT, "videos"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "breakdowns"), exist_ok=True)

def code_of(url):
    m = re.search(r"/(?:p|reel)/([^/]+)/", url or "")
    return m.group(1) if m else ""

def code_of_file(path):
    b = os.path.basename(path)
    m = re.search(r"devinjatho_([A-Za-z0-9_-]+)\.mp4$", b)
    return m.group(1) if m else None

inv = json.load(open(INV))
by_code = {}
for row in inv:
    c = code_of(row.get("url"))
    if c and c not in by_code:
        by_code[c] = row

# --- collect unique local videos -------------------------------------------
sources = {}
for p in sorted(glob.glob(os.path.join(BATCH, "*.mp4"))):
    c = code_of_file(p)
    if c and c not in sources:
        sources[c] = p
# motion_refs duplicates are byte-identical; batch copies already captured.
sources["Dd3x4cMStzs"] = os.path.join(REEL2, "reel2.mp4")
# Fresh downloads in this pass win over the batch copies (same video, current pull).
for p in sorted(glob.glob(os.path.join(ROOT, "sources", "*.mp4"))):
    m = re.match(r"^([A-Za-z0-9_-]+)\.mp4$", os.path.basename(p))
    if m:
        sources[m.group(1)] = p

manifest = []
for code, src in sorted(sources.items()):
    dest_name = f"devinjatho_{code}.mp4"
    dest = os.path.join(ROOT, "videos", dest_name)
    if not os.path.exists(dest) or os.path.getsize(dest) != os.path.getsize(src):
        shutil.copy2(src, dest)
    row = by_code.get(code, {})
    manifest.append({
        "code": code, "file": dest_name, "bytes": os.path.getsize(dest),
        "source": src, "url": row.get("url", ""),
        "created_at": row.get("created_at", ""), "likes": row.get("likes"),
        "comments": row.get("comments"),
    })

with open(os.path.join(ROOT, "analysis", "VIDEO_MANIFEST.tsv"), "w") as f:
    f.write("shortcode\tfile\tbytes\tcreated_at\tlikes\tcomments\turl\tsource_path\n")
    for m in manifest:
        f.write("\t".join(str(m[k] if m[k] is not None else "") for k in
                ["code", "file", "bytes", "created_at", "likes", "comments", "url", "source"]) + "\n")

# --- copy the library's 37 decode docs as library-grade breakdowns ----------
copied_decodes = []
for p in sorted(glob.glob(os.path.join(STYLE_DECODES, "*_DECODE.md"))):
    m = re.search(r"devinjatho_([A-Za-z0-9_-]+)_DECODE\.md$", os.path.basename(p))
    if not m:
        continue
    dest = os.path.join(ROOT, "breakdowns", f"BREAKDOWN-{m.group(1)}--library-decode.md")
    shutil.copy2(p, dest)
    copied_decodes.append(m.group(1))
for name, destname in [("TEARDOWN.md", "BREAKDOWN-Dd3x4cMStzs--library-teardown.md"),
                       ("SOUNDMAP.md", "BREAKDOWN-Dd3x4cMStzs--library-soundmap.md")]:
    shutil.copy2(os.path.join(REEL2, name), os.path.join(ROOT, "breakdowns", destname))

# --- inventory ---------------------------------------------------------------
PRIORITY = {"DffkuW8SCkz", "DfcPvRnyZRs", "DfV6GWMyqs0", "Dd3x4cMStzs",
            "DSh8cgtjfGX", "DLpgNYQMZlm"}
DECODED = set(copied_decodes) | {"Dd3x4cMStzs"}

def topic(row):
    cap = (row.get("post_caption") or "").replace("\n", " ").strip()
    return (cap[:110] + "…") if len(cap) > 110 else (cap or "(no caption in metadata)")

def provisional_format(row, code):
    if "/stories/" in (row.get("url") or ""):
        return "story capture (not grid — inventory only)"
    if code in DECODED:
        return "see library decode / priority breakdown"
    cap = (row.get("post_caption") or "").lower()
    if row.get("media_type") == "carousel":
        return "carousel (not a reel — inventory only)"
    if row.get("media_type") == "image":
        return "image post (inventory only)"
    if any(k in cap for k in ["hook", "hooks"]):
        return "PROVISIONAL M-list / M-hook (undecoded)"
    if any(k in cap for k in ["profile", "dashboard", "settings", "update", "feature", "app", "zoom", "manychat", "dm", "script"]):
        return "PROVISIONAL S screen-demo / walkthrough (undecoded)"
    if any(k in cap for k in ["views", "viral", "follow", "grow", "content"]):
        return "PROVISIONAL talking-head teaching (undecoded)"
    return "undecoded — format not yet classified"

rows = sorted(inv, key=lambda r: r.get("created_at") or "", reverse=True)
lines = []
lines.append("# INVENTORY — @devinjatho full profile grid (metadata pull on disk)")
lines.append("")
lines.append("**Profile:** Devin Jatho (@devinjatho) — https://www.instagram.com/devinjatho — verified business account; the profile fetch on Nov 12, 2026 showed 488,104 followers / 40 following.")
lines.append("")
lines.append(f"**Grid total enumerated: 213 profile-grid posts** (208 reels + 5 carousel/image posts) from the metadata union `devinjatho_inventory_union.json` (grid posts dated 2022-07-24 → 2026-11-08). The same union file also carries **65 story captures**, enumerated in the table below and marked as stories — **278 union rows in total**.")
lines.append(f"**Downloaded video files in this corpus: {len(manifest)} unique shortcodes** (see `analysis/VIDEO_MANIFEST.tsv` for filename + byte size + source path). Of the 208 grid reels, 207 are downloaded; the single miss is **DL0zRaBMgez** (2025-07-07, 'Don't make this CTA mistake') — Instagram refuses it anonymously ('This content isn't available to everyone'), so it is inventoried-only / breakdown-pending. The 5 carousel posts carry no video. **Library-decoded: {len(DECODED)}.** **Priority-1 deep-decoded in this pass: {len(PRIORITY)}.** Everything else is inventoried-only and queued in the same structure. Dd3x4cMStzs is an extra downloaded video (a Trial-Reels variant of the DfV6HTJybT4 system) that does not appear as its own union row.")
lines.append("")
lines.append("**Pinned-post caveat (honest):** the anonymous metadata pull and the yt-dlp profile extractor do not expose Instagram's pinned flags (the user extractor errors: 'Unable to extract data'), so no post below is labelled 'pinned' — priority was set by recency + engagement + format fit instead. Do not invent pinned status.")
lines.append("")
lines.append("**Priority rule:** teaching / talking-head formats (S screen-demo, M matrix/list, C critique, X device-led) = P1. Performed demos that teach a system = P1/P2. Vlog, comment-hub and pure entertainment variants = P2. Images/carousels = inventory only.")
lines.append("")
lines.append("| # | Date | Shortcode | Type | Likes | Comments | Topic (caption, trimmed) | Local video | Decode state | Format |")
lines.append("|---:|---|---|---|---:|---:|---|---|---|---|")
for i, row in enumerate(rows, 1):
    c = code_of(row.get("url"))
    local = "yes" if c in sources else "—"
    if c in PRIORITY:
        state = "**P1 DEEP BREAKDOWN**"
    elif c in DECODED:
        state = "library decode"
    elif c in sources:
        state = "downloaded, inventoried-only"
    else:
        state = "inventoried-only (not downloaded)"
    likes = row.get("likes") if row.get("likes") is not None else "—"
    comments = row.get("comments") if row.get("comments") is not None else "—"
    url = row.get("url") or ""
    lines.append(f"| {i} | {row.get('created_at','')[:10]} | [{c}]({url}) | {row.get('media_type','')} | {likes} | {comments} | {topic(row).replace('|','/')} | {local} | {state} | {provisional_format(row, c)} |")
lines.append("")
lines.append("## Coverage summary")
lines.append("")
lines.append(f"- Enumerated: {len(rows)} posts.")
lines.append(f"- Unique downloaded videos copied into `videos/`: {len(manifest)}.")
lines.append(f"- Posts with no local video file: {len(rows) - len([r for r in rows if code_of(r.get('url')) in sources])} (includes all 34 images + 5 carousels, the trial-reel variants never pulled, and any post whose download was not in the batch-11 pull).")
lines.append(f"- Full 0.5s-grid breakdowns in this pass: {', '.join(sorted(PRIORITY))} (+ Dd3x4cMStzs — 6 priority files; see `breakdowns/BREAKDOWN-<shortcode>.md`).")
lines.append(f"- Library-grade decodes carried into `breakdowns/`: {len(copied_decodes)} (`--library-decode` suffix) + the Dd3x4cMStzs teardown/soundmap pair.")
lines.append("- Next batch continues in this same structure: pick the next P1 teaching reels from the 'downloaded, inventoried-only' rows, transcribe, scene-detect, and write `BREAKDOWN-<shortcode>.md` to the same 0.5s-grid standard.")
open(os.path.join(ROOT, "INVENTORY.md"), "w").write("\n".join(lines) + "\n")
print(f"inventory rows={len(rows)} videos={len(manifest)} decodes={len(copied_decodes)} total_video_bytes={sum(m['bytes'] for m in manifest)}")

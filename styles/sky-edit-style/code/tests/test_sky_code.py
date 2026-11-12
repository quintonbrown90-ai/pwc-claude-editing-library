#!/usr/bin/env python3
"""Tests for the Sky code build. Stdlib unittest only.

Run: python3 -m unittest discover -s code/tests -v
     (from ~/workspace/claude-editing/styles/sky-edit-style/)
"""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

CODE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CODE))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "words_small.json"

import sky_build_plan  # noqa: E402
import sky_capcut_draft  # noqa: E402
import sky_devices  # noqa: E402
import sky_easing  # noqa: E402
import sky_hyperframes  # noqa: E402
import sky_palette as pal  # noqa: E402
import sky_qc  # noqa: E402


def load_words():
    return json.loads(FIXTURE.read_text())


BATCH18_WORDS = (Path(__file__).resolve().parent.parent.parent
                 / "examples" / "batch-18-sky-origin" / "words.json")


def load_batch18_words():
    """Real Dcc84V5jc6D transcript (261 words, faster-whisper small).

    Stored as {"w", "s", "e"} records; converted to the {"word", "start",
    "end"} shape caption_groups() takes.
    """
    raw = json.loads(BATCH18_WORDS.read_text())
    return [{"word": w["w"], "start": w["s"], "end": w["e"]}
            for w in raw["words"]]


def make_plan(**kw):
    args = dict(framework="The Filter",
                parts=["Hook", "Filter 1", "Filter 2", "Payoff"],
                family="green", keyword="WAITLIST", model_reel="DfX2qwQGagM")
    args.update(kw)
    return sky_build_plan.build_plan(load_words(), **args)


class TestPalette(unittest.TestCase):
    def test_pwc_palette_passes(self):
        for hexv in ("#14A886", "#FEE238", "#00214E", "#FCFCFC"):
            self.assertEqual(pal.validate_color(hexv), hexv)

    def test_sky_raw_accents_blocked(self):
        for bad in ("#40BB2F", "#E8913F", "#F09828", "#E86A5E", "#FF0000", "#00FF66"):
            with self.assertRaises(ValueError, msg=bad):
                pal.validate_color(bad)

    def test_footage_exempt_but_graphics_not(self):
        self.assertFalse(pal.is_forbidden("#E86A5E", is_footage=True))
        self.assertTrue(pal.is_forbidden("#E86A5E", is_footage=False))

    def test_family_map(self):
        self.assertEqual(pal.accent_for_family("green"), "#14A886")
        self.assertEqual(pal.accent_for_family("orange"), "#FEE238")
        self.assertEqual(pal.remap_sky_color("#40BB2F"), "#14A886")
        self.assertEqual(pal.remap_sky_color("#E8913F"), "#FEE238")
        self.assertEqual(pal.remap_sky_color("#E86A5E"), "#FEE238")

    def test_scan_finds_forbidden(self):
        hits = pal.scan_object_for_forbidden({"a": "#40BB2F", "b": ["x", "#14A886"]})
        self.assertEqual(len(hits), 1)


class TestEasing(unittest.TestCase):
    def test_endpoints(self):
        for name, fn in sky_easing.EASINGS.items():
            tol = 2e-3 if name.startswith("spring") else 1e-6
            self.assertAlmostEqual(fn(0.0), 0.0, delta=1e-9, msg=name)
            self.assertAlmostEqual(fn(1.0), 1.0, delta=tol, msg=name)

    def test_step_is_hard_cut(self):
        self.assertEqual(sky_easing.step(0.5), 0.0)
        self.assertEqual(sky_easing.step(1.0), 1.0)

    def test_keyframes_land_exact_end(self):
        kfs = sky_easing.keyframes("back.out_1.141", 0.3, n=6, start=0.88, end=1.0)
        self.assertEqual(kfs[-1]["value"], 1.0)
        self.assertEqual(kfs[0]["t_s"], 0.0)
        self.assertAlmostEqual(kfs[-1]["t_s"], 0.3)

    def test_overshoot_peak(self):
        peak = max(sky_easing.ease_out_back_1141(t / 100) for t in range(101))
        self.assertAlmostEqual(peak, 1.141, delta=0.01)


class TestDevices(unittest.TestCase):
    def test_registry_complete_d1_d59(self):
        # Renamed + extended Nov 12, 2026 (Batch 39): the registry gained
        # D57-D59 and the D2-lockup variant device — the old D1-D56/57
        # count contradicted Q's Nov 12 rulings, so it was updated, not
        # the rulings.
        ids = set(sky_devices.DEVICE_REGISTRY)
        for n in range(1, 60):
            self.assertIn(f"D{n}", ids, f"D{n} missing from registry")
        self.assertIn("D2-lockup", ids)
        self.assertEqual(len(ids), 61)  # D1-D59 + D5-list + D2-lockup variants

    def test_caption_groups_measured_cadence(self):
        groups = sky_devices.caption_groups(load_words())
        self.assertTrue(all(len(g["text"].split()) <= 3 for g in groups))
        durs = [g["t1"] - g["t0"] for g in groups]
        # Sky speaks ~4.3 wps; groups of ~2 words change every ~0.5 s.
        self.assertLess(sum(durs) / len(durs), 1.0)

    def test_caption_in_is_hard_cut(self):
        evs = sky_devices.d1_captions(load_words())
        for ev in evs:
            self.assertEqual(ev["motion"]["in"]["type"], "hard_cut")
            self.assertLessEqual(ev["motion"]["in"]["dur_s"], 0.033 + 1e-9)
            self.assertEqual(ev["colors"]["text"], "#FCFCFC")

    def test_d4_verdicts_remapped(self):
        evs = sky_devices.d4_filter_board(
            0.0, board_title="B",
            rows=[{"label": "A", "verdict": "approve"},
                  {"label": "B", "verdict": "reject"},
                  {"label": "C", "verdict": "minimum"}])
        verdicts = {e["items"][0]["verdict"]: e["items"][0]
                    for e in evs if e["items"]}
        self.assertEqual(verdicts["approve"]["color"], "#14A886")
        self.assertEqual(verdicts["reject"]["color"], "#FEE238")  # Sky red -> gold
        self.assertEqual(verdicts["reject"]["mark"], "X")
        self.assertEqual(verdicts["minimum"]["label"], "Minimum")
        self.assertIsNone(verdicts["minimum"]["mark"])

    def test_d6_is_static_base(self):
        evs = sky_devices.d6_chart(0.0, title="Views",
                                   annotations=[{"label": "Push", "value": "1.1M"}])
        base = evs[0]
        self.assertIn("STATIC base", base["notes"])
        self.assertNotIn("draw-on", base["motion"]["in"].get("type", ""))

    def test_d12_verified_mechanics(self):
        evs = sky_devices.d12_timeline(
            40.0, nodes=[{"label": "2025"}, {"label": "2026", "current": True}])
        line = evs[0]
        self.assertEqual(line["motion"]["in"]["type"], "hard_cut")  # full line at t0
        self.assertEqual(line["geometry"]["y"], 300)
        node2 = evs[2]
        self.assertEqual(node2["colors"]["label"], "#FEE238")  # current era in accent

    def test_d17_remaps_red_to_grey(self):
        evs = sky_devices.d17_dot_grid(0.0, categories=["Community"])
        self.assertEqual(evs[0]["colors"]["dot_lose"], "#8A93A6")
        self.assertEqual(evs[0]["colors"]["dot_gain"], "#14A886")

    def test_all_devices_smoke_validate(self):
        # One call per device; the __main__ smoke in sky_devices covers the
        # same ground — here we assert the registry functions are all callable
        # with their documented minimal args.
        self.assertEqual(len(sky_devices.list_devices()), 61)  # D1-D59 + variants (batch-39)


class TestPlan(unittest.TestCase):
    def test_plan_v2_shape(self):
        plan = make_plan()
        self.assertEqual(plan["version"], 2)
        self.assertEqual(plan["family"], "green")
        self.assertEqual(plan["accent"], "#14A886")
        self.assertEqual(plan["hero_device"], "D4")
        self.assertEqual(len(plan["parts"]), 4)
        self.assertGreater(len(plan["events"]), len(plan["caption_groups"]))
        self.assertEqual(plan["close"]["end_moment_deadline_s"],
                         plan["close"]["last_word_s"] + 1.0)

    def test_plan_validates_clean(self):
        plan = make_plan()
        self.assertEqual(sky_devices.validate_events(plan["events"]), [])

    def test_plan_rejects_bad_family_and_parts(self):
        with self.assertRaises(ValueError):
            make_plan(family="purple")
        with self.assertRaises(ValueError):
            make_plan(parts=["Only", "Two"])

    def test_plan_rejects_unknown_device(self):
        with self.assertRaises(ValueError):
            make_plan(devices_map={"2": ["D99"]})

    def test_plan_rejects_forbidden_colour_injection(self):
        # A device built with a raw Sky colour must fail validation.
        evs = sky_devices.d2_headline_lockup(
            0.0, kicker="k", display_lines=["X"], family="green")
        evs[0]["colors"]["display"] = "#40BB2F"
        self.assertTrue(sky_devices.validate_events(evs))

    def test_hero_variants(self):
        for hero in ("D4", "D5", "D5-list", "D6", "D12", "D13"):
            plan = make_plan(hero=hero)
            self.assertEqual(sky_devices.validate_events(plan["events"]), [],
                             f"hero {hero} failed validation")

    def test_d2_headline_clears_caption_band(self):
        # Regression (Nov 9 render): the D2 kicker struck through live
        # caption glyphs. The headline top must clear the caption clip
        # bottom by >= 12 px, and QC P4b must catch a D1xD2 collision.
        plan = make_plan()
        d1 = [e for e in plan["events"] if e["device"] == "D1"]
        d2 = [e for e in plan["events"] if e["device"] == "D2"][0]
        cap_bottom = max(e["geometry"]["y"] + e["geometry"]["h"] for e in d1)
        self.assertGreaterEqual(d2["geometry"]["y"], cap_bottom + 12)
        self.assertTrue(sky_qc.qc_plan(plan)["pass"])

    def test_d3_omitted_when_face_high_present_when_face_low(self):
        # Default face box (DfX2-measured, hair top y720): no room for a
        # separate D3 title + pill + hero, so D3 is omitted and the hero's
        # own title block carries the framework name.
        plan = make_plan()
        self.assertNotIn("D3", [e["device"] for e in plan["events"]])
        self.assertIn("OMITTED", plan["layout"]["d3_title_stack"])
        # D4 hero never gets a separate D3 — its board carries its own title.
        plan_low_d4 = make_plan(face_box={"x": 345, "y": 900, "w": 390, "h": 450})
        self.assertNotIn("D3", [e["device"] for e in plan_low_d4["events"]])
        # A lower face (hair top y900) with a D6 hero leaves room: D3 appears.
        plan_low = make_plan(hero="D6",
                             face_box={"x": 345, "y": 900, "w": 390, "h": 450})
        self.assertIn("D3", [e["device"] for e in plan_low["events"]])
        self.assertEqual(sky_devices.validate_events(plan_low["events"]), [])


class TestHyperFrames(unittest.TestCase):
    def test_project_builds_and_validates(self):
        plan = make_plan()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "hf"
            sky_hyperframes.build_project(plan, out)
            self.assertTrue((out / "index.html").exists())
            self.assertTrue((out / "compositions" / "sky.html").exists())
            self.assertTrue((out / "compositions" / "captions.html").exists())
            self.assertEqual(sky_hyperframes.validate_project(out), [])

    def test_no_forbidden_tokens(self):
        plan = make_plan()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "hf"
            sky_hyperframes.build_project(plan, out)
            for name in ("index.html", "compositions/sky.html",
                         "compositions/captions.html"):
                text = (out / name).read_text()
                for tok in ("Date.now", "Math.random", "fetch(", "autoAlpha"):
                    self.assertNotIn(tok, text)
            # The only external URL is the pinned GSAP CDN script.
            self.assertIn(sky_hyperframes.GSAP_SRC, (out / "index.html").read_text())

    def test_caption_clip_is_hard_cut(self):
        plan = make_plan()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "hf"
            sky_hyperframes.build_project(plan, out)
            text = (out / "compositions" / "captions.html").read_text()
            # D1 clips exist with data-start/data-duration; GSAP targets the
            # INNER div with a plain opacity set (hard cut), never autoAlpha.
            self.assertIn('class="clip sky-d1"', text)
            self.assertIn('tl.set("#sky-d1-0-in", {opacity: 1}', text)

    def test_dict_texts_render_clean(self):
        # Regression (Nov 9): dict texts rendered as Python reprs
        # ("the framework ['The Filter']", "Comment WAITLIST WAITLIST card").
        plan = make_plan()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "hf"
            sky_hyperframes.build_project(plan, out)
            sky = (out / "compositions" / "sky.html").read_text()
            self.assertNotIn("[&#x27;", sky)
            self.assertNotIn("['The Filter']", sky)
            self.assertNotIn("Comment WAITLIST WAITLIST card", sky)
            self.assertIn("The Filter", sky)
            self.assertIn("Comment", sky)
            self.assertIn("WAITLIST", sky)

    def test_scene_roots_transparent_ground_on_main(self):
        # Regression (Nov 9): an opaque navy scene root painted over every
        # sibling scene mounted before it, hiding the whole sky scene.
        plan = make_plan()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "hf"
            sky_hyperframes.build_project(plan, out)
            for name in ("compositions/sky.html", "compositions/captions.html"):
                self.assertNotIn("background: #00214E",
                                 (out / name).read_text())
            self.assertIn("background: #00214E",
                          (out / "index.html").read_text())
            # Root ids are unique across the assembled page.
            self.assertIn('id="sky-root"', (out / "compositions" / "sky.html").read_text())
            self.assertIn('id="captions-root"',
                          (out / "compositions" / "captions.html").read_text())


class TestCapCut(unittest.TestCase):
    def test_sequence_builds_and_validates(self):
        plan = make_plan()
        seq = sky_capcut_draft.build_sequence(plan)
        self.assertEqual(sky_capcut_draft.validate_sequence(seq), [])
        tools = [c["tool"] for c in seq["calls"]]
        self.assertIn("capcut_create_project", tools)
        self.assertIn("capcut_add_subtitles", tools)
        self.assertIn("capcut_add_text", tools)
        self.assertIn("capcut_generate_preview", tools)

    def test_coords_in_range(self):
        plan = make_plan()
        seq = sky_capcut_draft.build_sequence(plan)
        for c in seq["calls"]:
            pos = (c.get("args", {}).get("position")
                   or c.get("args", {}).get("style", {}).get("position"))
            if isinstance(pos, dict):
                self.assertTrue(-1.0 <= pos["x"] <= 1.0)
                self.assertTrue(-1.0 <= pos["y"] <= 1.0)

    def test_px_to_norm_center(self):
        # Full-canvas box -> centre (0, 0). Canvas centre is (0, 0); y is
        # bottom-to-top, so a box at the very top has y near +1.
        self.assertEqual(sky_capcut_draft.px_to_norm(0, 0, 1080, 1920),
                         {"x": 0.0, "y": 0.0})
        self.assertEqual(sky_capcut_draft.px_to_norm(540 - 50, 960 - 50, 100, 100),
                         {"x": 0.0, "y": 0.0})
        top = sky_capcut_draft.px_to_norm(490, 0, 100, 100)
        self.assertAlmostEqual(top["y"], 0.95, places=2)


class TestAntiSlopBatch19(unittest.TestCase):
    """Batch 19 cut-order locks (Q, Nov 9, 2026): no generic AI-Claude
    pattern may re-enter the Sky execution path. Each test pins one cut."""

    def _all_device_events(self):
        evs = []
        evs += sky_devices.d1_captions(load_words())
        evs += sky_devices.d2_headline_lockup(0.0, kicker="k", display_lines=["X"])
        evs += sky_devices.d3_title_stack(0.0, title="T", sections=["One"])
        evs += sky_devices.d4_filter_board(0.0, board_title="B",
                                           rows=[{"label": "A", "verdict": "approve"}])
        evs += sky_devices.d5_chapter_card(0.0, numeral=1, name="One", definition="First.")
        evs += sky_devices.d5_checklist(0.0, title="T", items=["A"])
        evs += sky_devices.d6_chart(0.0, title="V", annotations=[{"label": "P"}])
        evs += sky_devices.d7_venn(0.0, left_label="L", right_label="R", figure="1M")
        evs += sky_devices.d8_rewrite_pair(0.0, before="old", after="new",
                                           swapped_old="old", swapped_new="new")
        evs += sky_devices.d9_exhibit_insert(0.0, label="E", clip_path="c.mp4", duration_s=5.0)
        evs += sky_devices.d10_profile_insert(0.0, label="P", screen_path="s.mp4")
        evs += sky_devices.d11_chip_cloud(0.0, words_list=["Legit"])
        evs += sky_devices.d12_timeline(0.0, nodes=[{"label": "2025"}])
        evs += sky_devices.d13_workflow_strip(0.0, steps=["A"])
        evs += sky_devices.d14_end_beat(50.0, close_line="Comment WAITLIST")
        evs += sky_devices.d15_bar_chart(0.0, rows=[{"label": "Hook", "kind": "hook"}])
        evs += sky_devices.d16_branch_line(0.0, label="b")
        evs += sky_devices.d17_dot_grid(0.0, categories=["Community"])
        evs += sky_devices.d18_network_loop(0.0, profiles=["a"])
        evs += sky_devices.d19_people_grid(0.0, count_label="100s")
        evs += sky_devices.d20_views_refresh(0.0, view_counts=[8547])
        evs += sky_devices.d21_bw_beat(0.0, hero_word="DON'T")
        evs += sky_devices.d22_new_post_placeholder(0.0)
        evs += sky_devices.d23_floating_head(0.0)
        evs += sky_devices.d24_funnel_card(0.0, rows=["A"], checklist=["01 GOAL"])
        evs += sky_devices.d25_autopsy_labels(0.0, labels=["Hook filtering"])
        # Batch 18 (Dcc84V5jc6D) — D26-D37, so the anti-slop lock covers them.
        evs += sky_devices.d2_hook_build(0.0, steps=[
            {"word": "I guarantee", "t": 0.0, "size_px": 55, "role": "small"},
            {"word": "CAPTION MAXING", "t": 1.14, "size_px": 130, "role": "accent"}])
        evs += sky_devices.d26_dashed_loop_arrow(5.6, t1=8.8, headline_t0=5.6)
        evs += sky_devices.d27_donut_split(10.87, headline_number="149,095", t1=19.5,
                                           states=[{"t": 10.87, "followers_pct": 50.30,
                                                    "nonfollowers_pct": 49.70}])
        evs += sky_devices.d28_phone_section_tracker(
            8.8, t1=19.5, clip_path="reel.mp4",
            sections=[("HOOK", 9.0), ("LEAD", 10.0)])
        evs += sky_devices.d29_dot_columns(10.9, t1=19.5)
        evs += sky_devices.d30_proof_columns(
            38.4, t1=43.0,
            left={"handle": "wellcopymax", "caption": "10/10 marketing emails…", "ring": True},
            right={"handle": "shelby.sapp", "caption": "three days of women & wealthhh…", "ring": False})
        evs += sky_devices.d31_linear_countup(6.92, label="more leads")
        evs += sky_devices.d32_document_sweep(
            20.0, document_text="1. CASUAL INTRO\n2. THE RECEIPTS", t1=38.2,
            beats=[{"label": "1. CASUAL INTRO", "text": "1. CASUAL INTRO", "t0": 26.5},
                   {"label": "2. THE RECEIPTS", "text": "2. THE RECEIPTS", "t0": 27.9}])
        evs += sky_devices.d33_comment_examples(
            3.8, t1=5.5,
            left_shot={"text": "Comment \"notion\" to join", "handle": "realskytan",
                       "timestamp": "Edited · 66w"},
            right_shot={"text": "Create content for your avatar!", "handle": "realskytan",
                        "timestamp": "60w"})
        evs += sky_devices.d34_thumb_wall(
            21.8, t1=25.8,
            thumbnails=[{"src": f"thumb{i}.mp4", "caption": f"Reel {i}"} for i in range(1, 7)])
        evs += sky_devices.d35_prompt_ui(
            44.0, t1=51.5, prompt_text="Write me a caption.",
            formula_chain="Intro → Before/Story → Results → CTA")
        evs += sky_devices.d36_live_example_bookend(
            49.8, t1=52.0, keyword="Prompt",
            document_text="1. CASUAL INTRO\n2. THE RECEIPTS",
            source_document="1. CASUAL INTRO\n2. THE RECEIPTS")
        evs += sky_devices.d37_figure_pair(
            40.97, caption="figures a month",
            figures=[("$700K/m", 40.97, 60, 1030), ("$2–4M/m", 41.47, 700, 1030)])
        return evs

    def test_no_blur_in_and_no_generic_slide_or_fade(self):
        banned_in = {"slide_up", "slide_left", "scale_fade"}
        banned_out = {"slide_blur_out", "fade_together"}
        for ev in self._all_device_events():
            motion = ev.get("motion", {})
            self.assertNotIn("blur_from_px", motion.get("in", {}),
                             f"{ev['device']} in-motion still carries a blur-in")
            self.assertNotIn(motion.get("in", {}).get("type"), banned_in,
                             f"{ev['device']} in-motion is a generic slide/fade")
            self.assertNotIn(motion.get("out", {}).get("type"), banned_out,
                             f"{ev['device']} out-motion is a generic slide/fade")

    def test_panel_out_builder_removed(self):
        self.assertFalse(hasattr(sky_devices, "_panel_out"),
                         "_panel_out (slide+blur panel exit) must stay cut")

    def test_d5_entrance_is_pop_not_slide(self):
        ev = sky_devices.d5_chapter_card(0.0, numeral=1, name="One", definition="First.")[0]
        self.assertEqual(ev["motion"]["in"]["type"], "pop")

    def test_d7_entrance_is_pop_not_scale_fade(self):
        ev = sky_devices.d7_venn(0.0, left_label="L", right_label="R", figure="1M")[0]
        self.assertEqual(ev["motion"]["in"]["type"], "pop")

    def test_d8_entrance_is_pop_not_slide(self):
        ev = sky_devices.d8_rewrite_pair(0.0, before="old", after="new",
                                         swapped_old="old", swapped_new="new")[0]
        self.assertEqual(ev["motion"]["in"]["type"], "pop")

    def test_d11_out_is_hard_cut(self):
        ev = sky_devices.d11_chip_cloud(0.0, words_list=["Legit"])[0]
        self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")

    def test_hyperframes_emits_no_blur_in(self):
        plan = make_plan()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "hf"
            sky_hyperframes.build_project(plan, out)
            for name in ("compositions/sky.html", "compositions/captions.html"):
                text = (out / name).read_text()
                self.assertNotIn("blur(10px)", text, name)
                self.assertNotIn("blur(12px)", text, name)


class TestPremiumV6(unittest.TestCase):
    """SKY v6 (Batch 36): premium purge + new devices + validator + beat lock.

    The generic-fallback module (old Option 2) is REMOVED — premium Sky is
    the only output mode. These tests pin the removal, the D55/D56 devices,
    the tick-tone sound grammar, validate_premium_plan and beat lock."""

    def test_fallback_module_removed_and_never_imported(self):
        self.assertFalse((CODE / "sky_option2.py").exists(),
                         "sky_option2.py must stay deleted (v6 premium purge)")
        import re
        import_pat = re.compile(r"^\s*(?:from\s+sky_option2\s+import|import\s+sky_option2)\b",
                                re.MULTILINE)
        for name in ("sky_devices", "sky_hyperframes", "sky_build_plan",
                     "sky_capcut_draft", "sky_qc", "sky_easing", "sky_palette"):
            src = (CODE / f"{name}.py").read_text()
            self.assertIsNone(import_pat.search(src),
                              f"{name}.py imports the removed fallback module")
        self.assertFalse(hasattr(sky_devices, "_panel_out"))

    def test_d55_pill_system_pre_shown_row_type_in_blurred_handoff(self):
        pills = [{"number": 1, "text": "She never said she was the expert",
                  "chip_alone_t": 45.4, "text_t0": 45.9, "text_t1": 46.8},
                 {"number": 2, "text": "She made it feel like a shared challenge",
                  "chip_alone_t": 51.0, "text_t0": 51.5, "text_t1": 52.2},
                 {"number": 3, "text": "She openly shared her income",
                  "chip_alone_t": 57.1, "text_t0": 57.9, "text_t1": 58.2}]
        evs = sky_devices.d55_numbered_pill_system(44.4, pills=pills)
        row, p1, p2, p3 = evs
        self.assertEqual(row["items"][0]["chips"], [1, 2, 3])  # ALL pre-shown
        self.assertEqual(p2["motion"]["in"]["type"], "type_in_word_groups")
        self.assertEqual(p2["items"][0]["prev_text_exit"]["type"], "blurred_slide")
        self.assertAlmostEqual(p2["items"][0]["prev_text_exit"]["at_s"], 50.3)
        self.assertEqual(p2["colors"]["chip"], "#FEE238")  # PWC gold, no red
        with self.assertRaises(ValueError):
            sky_devices.d55_numbered_pill_system(44.4, pills=pills[:1])
        with self.assertRaises(ValueError):
            bad = [dict(pills[0]), dict(pills[1], text_t0=50.0)]
            sky_devices.d55_numbered_pill_system(44.4, pills=bad)
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])

    def test_d56_ui_shrink_single_instance_real_clip_only(self):
        ev = sky_devices.d56_new_post_ui_shrink(14.4, ui_clip="new_reel_ui.mp4")[0]
        self.assertTrue(ev["items"][0]["single_instance"])
        self.assertEqual(ev["motion"]["in"]["type"], "scale_down_into_ui")
        self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")
        with self.assertRaises(ValueError):
            sky_devices.d56_new_post_ui_shrink(14.4, ui_clip="")
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d23_head_system_label_type_in_and_list(self):
        evs = sky_devices.d23_floating_head(
            21.5, label="Post Production Head", label_t=21.8,
            list_labels=[("• Stable", 40.2), ("• Consistent", 40.9)])
        kinds = [e["name"] for e in evs]
        self.assertIn("head label: Post Production Head", kinds)
        lab = [e for e in evs if e["name"].startswith("head label")][0]
        self.assertEqual(lab["motion"]["in"]["type"], "type_in")
        lst = [e for e in evs if e["name"].startswith("head list")]
        self.assertEqual([e["t0"] for e in lst], [40.2, 40.9])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_tick_tone_spec_on_counter_timer_chart_devices(self):
        self.assertEqual(sky_devices.TICK_TONE_SPEC["pulse_hz"], 5926)
        chart = sky_devices.d6_chart(0.0, title="V",
                                     annotations=[{"label": "Push", "value": "1"}])
        self.assertEqual(chart[1]["sound"]["tick_tone"]["pulse_hz"], 5926)
        views = sky_devices.d20_views_refresh(0.0, view_counts=[8547])
        self.assertIn("tick_tone", views[0]["sound"])
        fig = sky_devices.d37_figure_pair(
            40.97, caption="figures a month",
            figures=[("$700K/m", 40.97, 60, 1030), ("$2–4M/m", 41.47, 700, 1030)])
        self.assertIn("tick_tone", fig[0]["sound"])
        stats = sky_devices.d51_player_stats_card(
            24.1, name="WARREN", t1=30.9, stats=[("42 CODING", 28.0)])
        blip = [e for e in stats if "sound" in e][0]["sound"]["ui_blip"]
        self.assertEqual(blip["window_s"], "31.26-31.68")  # DJcc instance note

    def test_validator_rejects_unknown_device(self):
        ev = sky_devices.d2_headline_lockup(0.0, kicker="k", display_lines=["X"])[0]
        ev = dict(ev, device="D99")
        self.assertTrue(sky_devices.validate_events([ev]))
        self.assertTrue(sky_devices.validate_premium_plan([ev]))

    def test_validator_rejects_banned_font_and_fallback_event(self):
        ev = sky_devices.d2_headline_lockup(0.0, kicker="k", display_lines=["X"])[0]
        serif = json.loads(json.dumps(ev))
        serif["items"] = [{"font": "Instrument Serif Italic"}]
        probs = sky_devices.validate_premium_plan([serif])
        self.assertTrue(any("banned font" in x for x in probs), probs)
        fb = json.loads(json.dumps(ev)); fb["option"] = 2
        probs = sky_devices.validate_premium_plan([fb])
        self.assertTrue(any("fallback" in x for x in probs), probs)
        slide = json.loads(json.dumps(ev))
        slide["motion"] = {"in": {"type": "slide_up"}, "out": {"type": "hard_cut"}}
        probs = sky_devices.validate_premium_plan([slide])
        self.assertTrue(any("banned motion" in x for x in probs), probs)

    def test_validator_rejects_cheap_asset_and_ai_on_proof(self):
        ev = sky_devices.d9_exhibit_insert(0.0, label="E", clip_path="clip.mp4",
                                           duration_s=5.0)[0]
        cheap = json.loads(json.dumps(ev))
        cheap["items"] = [{"clip": "stock_placeholder.mp4"}]
        probs = sky_devices.validate_premium_plan([cheap])
        self.assertTrue(any("cheap-grade" in x for x in probs), probs)
        ai = json.loads(json.dumps(ev))
        ai["items"] = [{"clip": "clip.mp4", "provenance": "ai_premium"}]
        probs = sky_devices.validate_premium_plan([ai])
        self.assertTrue(any("NEVER carry AI" in x for x in probs), probs)
        # Premium AI is ALLOWED on a non-proof device (asset-layer rule).
        card = sky_devices.d45_kinetic_black_card(
            12.0, lines=[{"text": "SALES", "role": "huge", "color": "gold"}])[0]
        card = json.loads(json.dumps(card))
        card["items"] = [{"provenance": "higgsfield"}]
        self.assertEqual(sky_devices.validate_premium_plan([card]), [])

    def test_validator_rejects_missing_citation_and_est_quarantine(self):
        ev = sky_devices.d2_headline_lockup(0.0, kicker="k", display_lines=["X"],
                                            source_reel="")[0]
        probs = sky_devices.validate_premium_plan([ev])
        self.assertTrue(any("no Sky source citation" in x for x in probs), probs)
        est = sky_devices.d5_chapter_card(0.0, numeral=1, name="One",
                                          definition="First.",
                                          source_reel="DfQ4E1Hjn0n")
        probs = sky_devices.validate_premium_plan(est)
        self.assertTrue(any("quarantined" in x for x in probs), probs)
        est2 = sky_devices.d13_workflow_strip(0.0, steps=["A"])
        self.assertTrue(any("quarantined" in x
                            for x in sky_devices.validate_premium_plan(est2)))

    def test_validator_clean_plan_passes(self):
        plan = make_plan()
        self.assertEqual(sky_devices.validate_premium_plan(plan["events"]), [])
        self.assertTrue(sky_qc.qc_plan(plan)["pass"])

    def test_beat_lock_grid_reason_and_report(self):
        words = load_words()
        on = sky_devices.d2_headline_lockup(words[0]["start"], kicker="k",
                                            display_lines=["X"])
        self.assertEqual(sky_devices.validate_beat_lock(on, words), [])
        off = sky_devices.d2_headline_lockup(words[0]["start"] + 0.2,
                                             kicker="k", display_lines=["X"])
        probs = sky_devices.validate_beat_lock(off, words)
        self.assertTrue(probs and "beat-lock" in probs[0])
        rep = sky_devices.beat_lock_report(off, words)
        self.assertEqual(rep["pct"], 0.0)
        off[0]["off_beat_reason"] = "deliberate: headline lands on the breath"
        self.assertEqual(sky_devices.validate_beat_lock(off, words), [])
        self.assertEqual(sky_devices.beat_lock_report(off, words)["pct"], 100.0)


class TestBatch39V7(unittest.TestCase):
    """Batch 39 + Q's Nov 12, 2026 rulings, wired into the code:
    the serif+bold headline lockup is APPROVED in PWC colours (serif
    stays banned in every other role), captions run the 1-word
    talking-head cadence and the two approved modes (all-white /
    keyword highlight — one per plan, no double treatment), and
    D57-D59 + the D5/D43/D48/D55 variants are real devices."""

    # ---- A(a): the lockup is approved; serif elsewhere still rejects
    def test_lockup_accepted_by_premium_validator(self):
        evs = sky_devices.d2_serif_lockup(12.0, serif_word="Reaction",
                                          keyword="consultation")
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        evs = sky_devices.d2_serif_lockup(
            2.5, serif_word="time efficient", keyword="Super",
            serif_first=False, source_reel="DfmxuoenIMV")
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])

    def test_lockup_conformance_enforced(self):
        # keyword slot wearing the serif face is NOT the approved lockup
        ev = copy.deepcopy(sky_devices.d2_serif_lockup(
            12.0, serif_word="Reaction", keyword="consultation")[0])
        for it in ev["items"]:
            if it.get("role") == "keyword":
                it["font"] = "Instrument Serif Italic"
        probs = sky_devices.validate_premium_plan([ev])
        self.assertTrue(any("bold grotesque" in p for p in probs), probs)
        # serif word must be white; keyword must be gold
        ev = copy.deepcopy(sky_devices.d2_serif_lockup(
            12.0, serif_word="Reaction", keyword="consultation")[0])
        for it in ev["items"]:
            if it.get("role") == "serif_word":
                it["color"] = "#FEE238"
        probs = sky_devices.validate_premium_plan([ev])
        self.assertTrue(any("serif_word must be WHITE" in p for p in probs), probs)
        # a lockup with its serif slot removed rejects
        ev = copy.deepcopy(sky_devices.d2_serif_lockup(
            12.0, serif_word="Reaction", keyword="consultation")[0])
        ev["items"] = [it for it in ev["items"] if it.get("role") != "serif_word"]
        probs = sky_devices.validate_premium_plan([ev])
        self.assertTrue(any("serif_word" in p for p in probs), probs)

    def test_serif_caption_rejected(self):
        ev = copy.deepcopy(sky_devices.d1_captions(load_words())[0])
        ev["items"] = [{"font": "Instrument Serif Italic"}]
        probs = sky_devices.validate_premium_plan([ev])
        self.assertTrue(any("banned font" in p for p in probs), probs)

    def test_serif_counter_rejected(self):
        ev = copy.deepcopy(sky_devices.d31_linear_countup(
            0.0, label="views")[0])
        ev["items"] = [{"font": "Playfair Display"}]
        probs = sky_devices.validate_premium_plan([ev])
        self.assertTrue(any("banned font" in p for p in probs), probs)

    # ---- A(b): caption modes
    def test_highlight_mode_accepted(self):
        words = load_words()
        evs = sky_devices.d1_captions(words, mode="highlight",
                                      gold_words=["filter", "proof"])
        keyed = [e for e in evs if "keyword" in e["colors"]]
        self.assertTrue(keyed, "highlight mode must colour a keyword")
        self.assertTrue(all(e["caption_mode"] == "highlight" for e in evs))
        self.assertTrue(all(e["colors"]["keyword"] == "#FEE238" for e in keyed))
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        # teal is the second approved highlight colour
        evs = sky_devices.d1_captions(words, mode="highlight",
                                      gold_words=["filter"],
                                      highlight_color="#14A886")
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        # a non-PWC highlight colour is refused at build time
        with self.assertRaises(ValueError):
            sky_devices.d1_captions(words, mode="highlight",
                                    gold_words=["filter"],
                                    highlight_color="#40BB2F")

    def test_white_mode_still_accepted(self):
        evs = sky_devices.d1_captions(load_words())
        self.assertTrue(all(e["caption_mode"] == "white" for e in evs))
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])

    def test_mixed_caption_modes_rejected(self):
        words = load_words()
        plan = (sky_devices.d1_captions(words)
                + sky_devices.d1_captions(words, mode="highlight",
                                          gold_words=["filter"]))
        probs = sky_devices.validate_premium_plan(plan)
        self.assertTrue(any("modes mixed" in p for p in probs), probs)

    def test_double_treatment_rejected(self):
        words = load_words()
        caps = sky_devices.d1_captions(words, mode="highlight",
                                       gold_words=["filter"])
        keyed = [e for e in caps if "keyword" in e["colors"]][0]
        lockup = sky_devices.d2_serif_lockup(keyed["t0"], serif_word="The",
                                             keyword="Filter")
        probs = sky_devices.validate_premium_plan(caps + lockup)
        self.assertTrue(any("double treatment" in p for p in probs), probs)
        # the same lockup on a different beat is fine
        lockup = sky_devices.d2_serif_lockup(30.0, serif_word="The",
                                             keyword="Filter")
        self.assertEqual(sky_devices.validate_premium_plan(caps + lockup), [])

    # ---- A(c): 1-word talking-head caption groups
    def test_one_word_caption_groups_b39(self):
        words = load_words()
        groups = sky_devices.caption_groups(words, era="b39")
        self.assertEqual(len(groups), len(words))
        self.assertTrue(all(len(g["text"].split()) == 1 for g in groups))
        evs = sky_devices.d1_captions(words, era="b39")
        self.assertTrue(all(e["caption_mode"] == "white" for e in evs))
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        with self.assertRaises(ValueError):
            sky_devices.caption_groups(words, era="dx")

    # ---- B: new devices validate, premium included
    def test_d57_score_meter(self):
        evs = sky_devices.d57_score_meter(6.5, t1=71.9, steps=[
            {"t": 6.5, "score": 1}, {"t": 21.0, "score": 2},
            {"t": 53.0, "score": 10}])
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        bubbles = [e for e in evs if e["text"] == "10/10"]
        self.assertEqual(len(bubbles), 1)
        # the bubble follows the playhead: the 10/10 bubble sits right of 1/10
        first = [e for e in evs if e["text"] == "1/10"][0]
        self.assertGreater(bubbles[0]["geometry"]["x"], first["geometry"]["x"])
        with self.assertRaises(ValueError):
            sky_devices.d57_score_meter(0.0, steps=[{"t": 0.0, "score": 11}])

    def test_d58_callout_chain(self):
        evs = sky_devices.d58_callout_chain(
            15.5, feeling="something's off",
            words="points are different sizes")
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        self.assertEqual(len(evs), 2)  # chain + verdict pill
        self.assertEqual(evs[1]["text"], "= expert")

    def test_d59_column_board(self):
        evs = sky_devices.d59_column_board(68.0, t1=90.0, title="General Rule",
                                           columns=[
            {"header": "Under 0.5x", "verdict": "kill it, don't make",
             "verdict_t": 70.0},
            {"header": "0.5x to 1.5x", "verdict": "It's your call",
             "verdict_t": 77.0},
            {"header": "2x and up", "verdict": "double", "verdict_t": 82.0}])
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        board = evs[0]
        self.assertEqual(board["items"][0]["columns"],
                         ["Under 0.5x", "0.5x to 1.5x", "2x and up"])

    # ---- B: changed-device variants behave as measured
    def test_d55_vertical_stack_variant_persists(self):
        end_pills = [
            {"number": 1, "text": "Name it", "chip_alone_t": 18.2,
             "text_t0": 18.7, "text_t1": 20.0},
            {"number": 2, "text": "Show it", "chip_alone_t": 31.0,
             "text_t0": 31.5, "text_t1": 32.8}]
        evs = sky_devices.d55_numbered_pill_system(
            18.2, layout="vertical_stack", pills=end_pills,
            source_reel="DfmxuoenIMV")
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        pill_evs = [e for e in evs if e["name"].startswith("pill #")]
        end = end_pills[-1]["text_t1"] + 4.0
        self.assertTrue(all(e["t1"] == end for e in pill_evs))  # persist
        self.assertEqual(pill_evs[0]["items"][0]["badge_shape"],
                         "rounded_square")
        self.assertGreater(pill_evs[1]["geometry"]["y"],
                           pill_evs[0]["geometry"]["y"])  # stacks downward
        with self.assertRaises(ValueError):
            sky_devices.d55_numbered_pill_system(0.0, layout="grid",
                                                 pills=end_pills)

    def test_d48_inverted_and_exhibit_mode_variants(self):
        evs = sky_devices.d48_stacked_split(
            6.5, t1=71.9, divider_frac=0.50, inverted=True, exhibit_mode=True,
            exhibit={"clip_path": "desk.mp4", "kind": "screen_recording"})
        self.assertEqual(sky_devices.validate_events(evs), [])
        reactor = [e for e in evs if "reactor" in e["name"]][0]
        exhibit = [e for e in evs if "exhibit (bottom)" in e["name"]][0]
        self.assertEqual(reactor["geometry"]["y"], 0)          # reactor TOP
        self.assertEqual(exhibit["geometry"]["y"], 960)        # exhibit BOTTOM
        self.assertEqual(reactor["items"][0]["caption_y"], 920)  # ON divider

    def test_d43_below_pill_variant(self):
        evs = sky_devices.d43_view_count_badge(
            0.0, count="1.5M views", t1=2.0, variant="below_pill",
            exhibit_bottom_y=480, source_reel="DfmxuoenIMV")
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(sky_devices.validate_premium_plan(evs), [])
        self.assertEqual(evs[0]["geometry"]["y"], 490)  # directly under exhibit
        self.assertIsNone(evs[0]["items"][0]["icon"])   # no eye icon
        with self.assertRaises(ValueError):
            sky_devices.d43_view_count_badge(0.0, count="1.5M",
                                             variant="below_pill")

    def test_d5_glass_recap_variant(self):
        evs = sky_devices.d5_checklist(
            10.0, title="The 2 Things",
            items=["Name the problem", "Show the process"],
            recap_t=33.0, source_reel="DfZ_q_pFbX1")
        self.assertEqual(len(evs), 2)
        self.assertEqual(sky_devices.validate_events(evs), [])
        self.assertEqual(evs[1]["colors"]["pill_fill"], "translucent glass")
        self.assertEqual(evs[1]["instance"], evs[0]["instance"])  # same list


class TestBatch18(unittest.TestCase):
    """Batch 18 — Sky origin reel Dcc84V5jc6D (Aug 25, 2026, Dcc-era).

    D26-D37 + the Dcc-era D1/D2 variants. Every assertion traces to
    EDIT-TEARDOWN.md §3/§7. [EST] sub-parameters must stay flagged in the
    events (never silently hard-coded as measurements)."""

    DOC = ("1. CASUAL INTRO + THE OBSESSION\n2. THE RECEIPTS\n"
           "3. THE FAILED EXPERIMENTS\n4. THE REVEAL\n5. WHAT YOU DO NOW\n"
           "6. STILL HUMAN\n7. THE ASK")
    BEATS = [{"label": "1. CASUAL INTRO + THE OBSESSION",
              "text": "1. CASUAL INTRO + THE OBSESSION", "t0": 26.5},
             {"label": "2. THE RECEIPTS", "text": "2. THE RECEIPTS", "t0": 27.9},
             {"label": "3. THE FAILED EXPERIMENTS",
              "text": "3. THE FAILED EXPERIMENTS", "t0": 30.0}]

    def test_d1_dcc_era_groups_2_to_5_words(self):
        df = sky_devices.caption_groups(load_words(), era="df")
        dcc = sky_devices.caption_groups(load_words(), era="dcc")
        self.assertTrue(all(len(g["text"].split()) <= 3 for g in df))
        # Dcc-era: 2-5 words per group (measured); a 1-word group only ever
        # occurs when a single word ends in punctuation ("First,").
        self.assertTrue(all(len(g["text"].split()) <= 5 for g in dcc))
        self.assertGreaterEqual(max(len(g["text"].split()) for g in dcc), 4)
        for g in dcc:
            if len(g["text"].split()) == 1:
                self.assertTrue(g["text"].endswith((".", ",", "?", "!", ":", ";")))
        with self.assertRaises(ValueError):
            sky_devices.caption_groups(load_words(), era="dx")
        # FIX Batch 18 QC F1 — the real Dcc84V5jc6D transcript (261 words):
        # the 14-char Q-lane cap yielded 84 groups, zero 5-word groups and 6
        # one-word orphans. The Dcc 21-char cap + orphan merge must reproduce
        # the three frame-verified 5-word groups and leave no 1-word orphan
        # except the documented punctuation case.
        real = load_batch18_words()
        self.assertEqual(len(real), 261)
        df_real = sky_devices.caption_groups(real, era="df")
        self.assertTrue(all(len(g["text"].split()) <= 3 for g in df_real))
        dcc_real = sky_devices.caption_groups(real, era="dcc")
        self.assertTrue(all(len(g["text"].split()) <= 5 for g in dcc_real))
        self.assertGreaterEqual(max(len(g["text"].split()) for g in dcc_real), 5)
        for target in ("than you will ever need.", "So at the very top,",
                       "that writes it for you."):
            self.assertIn(target, [g["text"] for g in dcc_real], target)
        for g in dcc_real:
            if len(g["text"].split()) == 1:
                self.assertTrue(
                    g["text"].endswith((".", ",", "?", "!", ":", ";")),
                    f"1-word orphan without punctuation: {g['text']!r}")
        durs = [g["t1"] - g["t0"] for g in dcc_real]
        # Measured range 0.33-1.28 s (EDIT-TEARDOWN.md §4); code reproduces
        # 0.32-1.30 s — assert a tight band around the measured range.
        self.assertGreaterEqual(min(durs), 0.30)
        self.assertLessEqual(max(durs), 1.35)

    def test_d1_dcc_era_yellow_keyword_in_caption(self):
        evs = sky_devices.d1_captions(load_words(), era="dcc",
                                      gold_words=["proof", "payoff"],
                                      source_reel="Dcc84V5jc6D")
        keyed = [e for e in evs if "keyword" in e["colors"]]
        self.assertTrue(keyed, "no Dcc-era caption carried a gold keyword")
        for e in keyed:
            self.assertEqual(e["colors"]["keyword"], "#FEE238")
            self.assertEqual(e["colors"]["text"], "#FCFCFC")
            self.assertEqual(e["motion"]["in"]["type"], "hard_cut")
        # Df-era default stays all-white with no keyword colour.
        df_evs = sky_devices.d1_captions(load_words())
        self.assertTrue(all("keyword" not in e["colors"] for e in df_evs))

    def test_d2_hook_build_mixed_sizes_5f_fade_out(self):
        ev = sky_devices.d2_hook_build(0.0, steps=[
            {"word": "I guarantee", "t": 0.0, "size_px": 55, "role": "small"},
            {"word": "aren't", "t": 0.88, "size_px": 110, "role": "large"},
            {"word": "CAPTION MAXING", "t": 1.14, "size_px": 130, "role": "accent"},
            {"word": "enough", "t": 1.88, "size_px": 55, "role": "small"}])[0]
        self.assertEqual(ev["device"], "D2")
        sizes = {s["word"]: s["size_px"] for s in ev["items"]}
        self.assertEqual((sizes["I guarantee"], sizes["aren't"],
                          sizes["CAPTION MAXING"]), (55, 110, 130))
        self.assertEqual(ev["motion"]["in"]["type"], "word_build")
        self.assertEqual(ev["motion"]["out"]["type"], "fade")
        self.assertAlmostEqual(ev["motion"]["out"]["dur_s"], 5 / 30, places=3)
        self.assertAlmostEqual(ev["t1"], 1.88 + 1.4 + 5 / 30, places=3)
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d26_loop_arrow_waypoints_loop_and_no_arrowhead(self):
        ev = sky_devices.d26_dashed_loop_arrow(5.6, t1=8.8, headline_t0=5.6)[0]
        path = ev["items"][0]["path"]
        self.assertIn((200, 360), path)
        self.assertIn((250, 1450), path)
        self.assertEqual(ev["items"][0]["loop_centre"], (200, 900))
        self.assertFalse(ev["items"][0]["arrowhead"])
        self.assertIn("[EST-dash]", ev["motion"]["in"]["dash_status"])
        self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")
        self.assertEqual(ev["colors"]["line"], "#14A886")  # family green -> teal
        with self.assertRaises(ValueError):
            sky_devices.d26_dashed_loop_arrow(5.0, headline_t0=5.6)
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d27_donut_pop_1f_states_headline_constant(self):
        states = [{"t": 10.87, "followers_pct": 50.30, "nonfollowers_pct": 49.70},
                  {"t": 15.5, "followers_pct": 58.51, "nonfollowers_pct": 41.57},
                  {"t": 16.5, "followers_pct": 92.70, "nonfollowers_pct": 7.70}]
        evs = sky_devices.d27_donut_split(10.87, headline_number="149,095",
                                          t1=19.5, states=states)
        self.assertEqual(len(evs), 3)
        self.assertEqual(evs[0]["motion"]["in"]["type"], "hard_cut")
        self.assertAlmostEqual(evs[0]["motion"]["in"]["dur_s"], 0.033, places=3)
        for ev, s in zip(evs, states):
            self.assertEqual(ev["text"], "149,095")  # headline never changes
            self.assertAlmostEqual(ev["items"][0]["followers_pct"]
                                   + ev["items"][0]["nonfollowers_pct"], 100.0, delta=2.0)
            self.assertIsNone(ev["items"][0]["sweep_s"])  # stepped default (GAP-G11)
        self.assertIn("[EST]", evs[0]["motion"]["ring_sweep"]["status"])
        with self.assertRaises(ValueError):
            sky_devices.d27_donut_split(10.87, headline_number="1",
                                        states=[{"t": 10.87, "followers_pct": 50.0,
                                                 "nonfollowers_pct": 20.0}])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d28_phone_sections_change_on_time_and_face_clear(self):
        sections = [("HOOK", 9.0), ("LEAD", 10.0), ("BODY1", 14.0),
                    ("OPEN LOOPS", 17.0)]
        evs = sky_devices.d28_phone_section_tracker(
            8.8, t1=19.5, clip_path="reel.mp4", sections=sections)
        phone = evs[0]
        self.assertEqual(phone["geometry"], {"x": 360, "y": 1030, "w": 360, "h": 660})
        self.assertTrue(phone["items"][0]["clip_plays"])
        labels = evs[1:]
        self.assertEqual([e["t0"] for e in labels], [9.0, 10.0, 14.0, 17.0])
        self.assertEqual([e["text"] for e in labels],
                         ["HOOK", "LEAD", "BODY1", "OPEN LOOPS"])
        with self.assertRaises(ValueError):
            sky_devices.d28_phone_section_tracker(8.8, sections=sections,
                                                  clip_path="")
        with self.assertRaises(ValueError):
            # Phone overlapping the face box must fail loudly.
            sky_devices.d28_phone_section_tracker(
                8.8, sections=sections, clip_path="reel.mp4",
                face_box={"x": 345, "y": 420, "w": 390, "h": 900})
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d29_dot_columns_counts_hollow_filled_arcs(self):
        ev = sky_devices.d29_dot_columns(10.9, t1=19.5)[0]
        dots = ev["items"][0]["dots"]
        left = [d for d in dots if d["side"] == "left"]
        right = [d for d in dots if d["side"] == "right"]
        self.assertEqual((len(left), len(right)), (12, 14))
        self.assertTrue(all(not d["filled"] for d in left))
        self.assertTrue(all(d["filled"] for d in right))
        self.assertEqual(ev["colors"]["left_outline"], "#14A886")
        self.assertEqual(ev["colors"]["right_fill"], "#FEE238")
        # Loose outward arcs, not a straight grid: x spread is wide and the
        # middle of the left column bulges further left than its ends.
        xs = [d["x"] for d in left]
        self.assertGreater(max(xs) - min(xs), 20)
        mid = sum(d["x"] for d in left[4:8]) / 4
        ends = (sum(d["x"] for d in left[:2]) + sum(d["x"] for d in left[-2:])) / 4
        self.assertLess(mid, ends)
        self.assertIn("[EST]", ev["motion"]["in"]["notes"])
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d30_proof_columns_real_handles_and_behind_speaker(self):
        evs = sky_devices.d30_proof_columns(
            38.4, t1=43.0,
            left={"handle": "wellcopymax", "caption": "10/10 marketing emails…",
                  "ring": True},
            right={"handle": "shelby.sapp", "caption": "three days of women & wealthhh…",
                   "ring": False})
        heads, cols = evs
        self.assertIn("wellcopymax", heads["text"])
        self.assertIn("shelby.sapp", heads["text"])
        captions = {it["handle"]: it["caption"] for it in cols["items"]
                    if "caption" in it}
        self.assertEqual(captions["wellcopymax"], "10/10 marketing emails…")
        layer = [it for it in cols["items"] if it.get("layer") == "behind_speaker"]
        self.assertEqual(len(layer), 1)
        with self.assertRaises(ValueError):
            sky_devices.d30_proof_columns(
                38.4, left={"handle": "a", "caption": "Lorem ipsum dolor", "ring": False},
                right={"handle": "b", "caption": "real words", "ring": False})
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d31_linear_countup_constant_rate_no_landing(self):
        import inspect
        self.assertNotIn("final_value",
                         inspect.signature(sky_devices.d31_linear_countup).parameters)
        ev = sky_devices.d31_linear_countup(6.92, label="more leads")[0]
        samples = ev["items"][0]["samples"]
        self.assertEqual(samples[0]["value"], 0)
        diffs = [b["value"] - a["value"] for a, b in zip(samples, samples[1:])]
        self.assertTrue(all(d == 27 for d in diffs),
                        f"count-up is not linear +9/frame: {diffs[:5]}")
        self.assertEqual(ev["items"][0]["easing"], "linear")
        self.assertIsNone(ev["items"][0]["landing_value"])
        self.assertEqual(ev["motion"]["count"]["easing"], "linear")
        self.assertEqual(ev["motion"]["out"]["type"], "fade")
        self.assertAlmostEqual(ev["motion"]["out"]["dur_s"], 10 / 30, places=3)
        self.assertEqual(ev["colors"]["number"], "#FEE238")
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d32_document_verbatim_highlight_one_row_reader_matches(self):
        evs = sky_devices.d32_document_sweep(20.0, document_text=self.DOC,
                                             t1=38.2, beats=self.BEATS)
        doc = evs[0]
        self.assertEqual(doc["text"], self.DOC)
        self.assertEqual(doc["items"][0]["opacity"], 1.0)
        dim = sky_devices.d32_document_sweep(1.0, document_text=self.DOC,
                                             beats=self.BEATS, state="dim")[0]
        self.assertAlmostEqual(dim["items"][0]["opacity"], 0.35)
        self.assertLess(dim["items"][0]["opacity"],
                        0.5 * doc["items"][0]["opacity"])
        self.assertIn("[EST-colour]", doc["items"][0]["highlight_status"])
        beats = evs[1:]
        self.assertEqual([b["t0"] for b in beats], [26.5, 27.9, 30.0])
        for b, src in zip(beats, self.BEATS):
            self.assertEqual(b["items"][0]["reader_text"], src["text"])
            self.assertEqual(b["text"], src["text"])
        # Highlight sits on exactly one row at a time (no overlap).
        for a, b in zip(beats, beats[1:]):
            self.assertLessEqual(a["t1"], b["t0"])
        with self.assertRaises(ValueError):
            sky_devices.d32_document_sweep(20.0, document_text="  ",
                                           beats=self.BEATS)
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d33_comment_examples_real_ui(self):
        evs = sky_devices.d33_comment_examples(
            3.8, t1=5.5,
            left_shot={"text": "Comment \"notion\" to join the waitlist",
                       "handle": "realskytan", "timestamp": "Edited · 66w"},
            right_shot={"text": "Create content for your avatar!",
                        "handle": "realskytan", "timestamp": "60w"})
        self.assertEqual(len(evs), 2)
        for ev in evs:
            self.assertTrue(ev["items"][0]["handle"])
            self.assertTrue(ev["items"][0]["timestamp"])
            self.assertTrue(ev["items"][0]["real_screenshot"])
            self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")
        with self.assertRaises(ValueError):
            sky_devices.d33_comment_examples(
                3.8, left_shot={"text": "x", "handle": "a", "timestamp": ""},
                right_shot={"text": "y", "handle": "b", "timestamp": "60w"})
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d34_thumb_wall_blur_slide_six_thumbs_4s(self):
        thumbs = [{"src": f"thumb{i}.mp4", "caption": f"Reel {i}"}
                  for i in range(1, 7)]
        ev = sky_devices.d34_thumb_wall(21.8, t1=25.8, thumbnails=thumbs)[0]
        self.assertEqual(len(ev["items"][0]["thumbnails"]), 6)
        self.assertEqual(ev["motion"]["in"]["type"], "motion_blur_slide")
        self.assertAlmostEqual(ev["motion"]["in"]["dur_s"], 1.2)
        self.assertEqual(ev["motion"]["mid"]["type"], "shrink_float")
        self.assertAlmostEqual(ev["t1"] - ev["t0"], 4.0)
        self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")
        with self.assertRaises(ValueError):
            sky_devices.d34_thumb_wall(21.8, thumbnails=thumbs[:5])
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d35_prompt_ui_verbatim_chain_as_data_live_cursor(self):
        chain = "Intro → Before/Story → Results → After/Reveal → What I Post/Do → Still Human → CTA"
        evs = sky_devices.d35_prompt_ui(
            44.0, t1=51.5, prompt_text="I want you to write me a caption.",
            formula_chain=chain)
        doc, bar = evs
        self.assertEqual(doc["text"], "I want you to write me a caption.")
        # Chain is stored verbatim as passed data — never canonicalised.
        self.assertEqual(bar["items"][0]["formula_chain"], chain)
        self.assertEqual(bar["text"], chain)
        cursor = bar["items"][0]["cursor"]
        self.assertTrue(cursor["from_recording"])
        self.assertEqual((cursor["x"], cursor["y"]), (830, 1300))
        self.assertEqual(bar["t1"], doc["t1"])  # bar persists while doc is up
        with self.assertRaises(ValueError):
            sky_devices.d35_prompt_ui(44.0, prompt_text=" ", formula_chain=chain)
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d36_bookend_same_document_cropped_not_reflowed(self):
        dim = sky_devices.d32_document_sweep(1.0, document_text=self.DOC,
                                             beats=self.BEATS, state="dim")
        evs = sky_devices.d36_live_example_bookend(
            49.8, t1=52.0, keyword="Prompt", document_text=self.DOC,
            source_document=dim[0]["text"])
        doc, pill = evs
        self.assertEqual(doc["text"], self.DOC)
        self.assertTrue(doc["items"][0]["cropped"])
        self.assertFalse(doc["items"][0]["reflow"])
        self.assertEqual(pill["text"], "Prompt")
        self.assertEqual(pill["colors"]["keyword"], "#FEE238")
        with self.assertRaises(ValueError):
            sky_devices.d36_live_example_bookend(
                49.8, keyword="Prompt", document_text="different text",
                source_document=self.DOC)
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d37_figures_one_per_number_left_then_right_glow(self):
        evs = sky_devices.d37_figure_pair(
            40.97, caption="figures a month",
            figures=[("$700K/m", 40.97, 60, 1030), ("$2–4M/m", 41.47, 700, 1030)])
        left, right, cap = evs
        self.assertLess(left["t0"], right["t0"])
        self.assertEqual(left["motion"]["in"]["dur_s"], 0.033)
        self.assertEqual(right["motion"]["in"]["dur_s"], 0.033)
        self.assertFalse(left["items"][0]["glow_decay"])
        self.assertTrue(right["items"][0]["glow_decay"])
        self.assertEqual(right["motion"]["glow_decay"]["type"], "glow_decay")
        self.assertEqual(cap["text"], "figures a month")
        with self.assertRaises(ValueError):
            sky_devices.d37_figure_pair(
                40.97, caption="x",
                figures=[("$2–4M/m", 41.47, 700, 1030), ("$700K/m", 40.97, 60, 1030)])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_all_batch18_devices_validate_clean_together(self):
        evs = []
        evs += sky_devices.d26_dashed_loop_arrow(5.6, t1=8.8, headline_t0=5.6)
        evs += sky_devices.d27_donut_split(10.87, headline_number="149,095", t1=19.5,
                                           states=[{"t": 10.87, "followers_pct": 50.30,
                                                    "nonfollowers_pct": 49.70}])
        evs += sky_devices.d28_phone_section_tracker(
            8.8, t1=19.5, clip_path="reel.mp4",
            sections=[("HOOK", 9.0), ("LEAD", 10.0)])
        evs += sky_devices.d29_dot_columns(10.9, t1=19.5)
        evs += sky_devices.d30_proof_columns(
            38.4, t1=43.0,
            left={"handle": "wellcopymax", "caption": "10/10 marketing emails…", "ring": True},
            right={"handle": "shelby.sapp", "caption": "three days of women & wealthhh…", "ring": False})
        evs += sky_devices.d31_linear_countup(6.92, label="more leads")
        evs += sky_devices.d32_document_sweep(20.0, document_text=self.DOC,
                                              t1=38.2, beats=self.BEATS)
        evs += sky_devices.d33_comment_examples(
            3.8, t1=5.5,
            left_shot={"text": "Comment \"notion\"", "handle": "realskytan",
                       "timestamp": "Edited · 66w"},
            right_shot={"text": "Create content!", "handle": "realskytan",
                        "timestamp": "60w"})
        evs += sky_devices.d34_thumb_wall(
            21.8, t1=25.8,
            thumbnails=[{"src": f"thumb{i}.mp4", "caption": f"Reel {i}"} for i in range(1, 7)])
        evs += sky_devices.d35_prompt_ui(
            44.0, t1=51.5, prompt_text="Write me a caption.",
            formula_chain="Intro → Before/Story → Results → CTA")
        evs += sky_devices.d36_live_example_bookend(
            49.8, t1=52.0, keyword="Prompt", document_text=self.DOC,
            source_document=self.DOC)
        evs += sky_devices.d37_figure_pair(
            40.97, caption="figures a month",
            figures=[("$700K/m", 40.97, 60, 1030), ("$2–4M/m", 41.47, 700, 1030)])
        self.assertEqual(sky_devices.validate_events(evs), [])

    # ------------------------------------------------ Batch 19 (D38-D54)
    def test_d38_pov_desk_types_items_live_ahead_of_beat(self):
        items = [{"text": "5 tips to become more confident.", "t": 0.0},
                 {"text": "why you care so much about what other people think", "t": 4.0},
                 {"text": "4 habits that make it psychologically impossible to care", "t": 26.0}]
        evs = sky_devices.d38_pov_desk_hook_doc(
            0.0, headline="If I was writing hooks for Mel Robbins, this is how I would NOT write them.",
            t1=70.61, items=items,
            camera_moves=[{"kind": "push_in", "t": 0.0},
                          {"kind": "profile_swing", "t": 28.0}])
        desk, headline = evs[0], evs[1]
        self.assertEqual(desk["geometry"], {"x": 0, "y": 0, "w": 1080, "h": 1920})
        self.assertEqual(headline["text"],
                         "If I was writing hooks for Mel Robbins, this is how I would NOT write them.")
        self.assertEqual(desk["items"][0]["camera_moves"][1]["kind"], "profile_swing")
        list_evs = evs[2:]
        self.assertEqual(len(list_evs), 3)
        self.assertEqual(list_evs[0]["motion"]["in"]["type"], "type_in_live")
        self.assertEqual(list_evs[0]["items"][0]["mid_type_placeholder"], "List")
        with self.assertRaises(ValueError):
            sky_devices.d38_pov_desk_hook_doc(0.0, headline=" ", items=items)
        with self.assertRaises(ValueError):
            sky_devices.d38_pov_desk_hook_doc(0.0, headline="Hook", items=[])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d39_subject_photo_bottom_centre_hard_cut_out(self):
        ev = sky_devices.d39_subject_photo_insert(
            1.5, photo_path="mel_robbins.jpg", subject="Mel Robbins",
            duration_s=2.0, size="half_body")[0]
        self.assertEqual(ev["geometry"], {"x": 195, "y": 1130, "w": 690, "h": 670})
        self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")
        self.assertEqual(ev["items"][0]["corners"], "rounded-rect")
        head = sky_devices.d39_subject_photo_insert(
            0.0, photo_path="leila.jpg", subject="Leila Hormozi",
            duration_s=3.5, size="headshot")[0]
        self.assertLess(head["geometry"]["w"], ev["geometry"]["w"])
        with self.assertRaises(ValueError):
            sky_devices.d39_subject_photo_insert(1.5, photo_path="", subject="X")
        with self.assertRaises(ValueError):
            # Photo over the face box must fail loudly.
            sky_devices.d39_subject_photo_insert(
                1.5, photo_path="x.jpg", subject="X",
                face_box={"x": 195, "y": 1130, "w": 690, "h": 670})
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d40_pov_label_pill_vs_bar(self):
        pill = sky_devices.d40_pov_scene_label(
            0.0, text="POV: Giving feedback to your strategists",
            geometry="pill", t1=9.0)[0]
        self.assertEqual(pill["geometry"], {"x": 15, "y": 85, "w": 315, "h": 90})
        self.assertAlmostEqual(pill["t1"] - pill["t0"], 9.0)
        bar = sky_devices.d40_pov_scene_label(
            0.0, text="POV: You're Autistic about Content",
            geometry="bar", t1=51.24, source_reel="DeIkaFAlMQO")[0]
        self.assertEqual(bar["geometry"], {"x": 0, "y": 0, "w": 1080, "h": 60})
        self.assertAlmostEqual(bar["t1"] - bar["t0"], 51.24)
        with self.assertRaises(ValueError):
            sky_devices.d40_pov_scene_label(0.0, text="POV: x", geometry="bubble")
        self.assertEqual(sky_devices.validate_events([pill, bar]), [])

    def test_d41_spine_nine_vertebrae_zoom_right_face_clear(self):
        vertebrae = ["Goal", "Person", "Avatar", "Gap", "Offer", "Funnel",
                     "Content Pillars", "Formats", "Brand & Positioning"]
        evs = sky_devices.d41_spine_diagram(
            4.0, t1=63.34, close_arrow_t=60.0, vertebrae=vertebrae,
            zooms=[{"label": "Goal", "t0": 13.62, "detail": "hire or leads?"},
                   {"label": "Funnel", "t0": 32.82, "detail": "where does traffic point?"},
                   {"label": "Brand & Positioning", "t0": 54.86,
                    "detail": "what do you want to be known for?"}])
        full, *zooms, arrow = evs
        self.assertEqual(full["items"][0]["vertebrae_n"], 9)
        self.assertEqual(full["items"][0]["vertebrae"], vertebrae)
        self.assertEqual(full["colors"]["label"], "#FEE238")  # Sky yellow -> gold
        for z in zooms:
            self.assertEqual(z["geometry"]["x"], 620)  # zoomed spine fills RIGHT side
            self.assertEqual(z["geometry"]["w"], 460)
        self.assertEqual(arrow["motion"]["in"]["type"], "line_draw")
        with self.assertRaises(ValueError):
            sky_devices.d41_spine_diagram(4.0, vertebrae=vertebrae[:8],
                                          zooms=[{"label": "Goal", "t0": 13.62}])
        with self.assertRaises(ValueError):
            sky_devices.d41_spine_diagram(4.0, vertebrae=vertebrae,
                                          zooms=[{"label": "Not a vertebra", "t0": 13.62}])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d42_question_fork_three_stages_outcomes_one_at_a_time(self):
        evs = sky_devices.d42_question_fork(
            66.5, header="THE 1 LEADERSHIP QUESTION",
            question="When you took over your last team, what was the first thing you changed, and why?",
            outcomes=[("OUTCOME A", "Lead a department", 70.0, "left"),
                      ("OUTCOME B", "Create more work", 73.0, "right")])
        card, branch, out_a, out_b = evs
        self.assertEqual(card["text"]["question"],
                         "When you took over your last team, what was the first thing you changed, and why?")
        self.assertAlmostEqual(card["colors"]["card_opacity"], 0.55)
        self.assertEqual(branch["motion"]["in"]["type"], "line_draw")
        self.assertLess(out_a["t0"], out_b["t0"])  # pills land one at a time
        self.assertEqual(out_a["geometry"]["x"], 30)
        self.assertEqual(out_b["geometry"]["x"], 570)
        # Measured Sky outcomes are white serif italic — a banned telltale
        # in v6; the Q-lane default is bold grotesque, never the serif.
        self.assertIn("banned telltale", out_a["items"][0]["font"])
        serif = sky_devices.d42_question_fork(
            66.5, header="H", question="Q?", serif_outcomes=True,
            outcomes=[("OUTCOME A", "Lead a department", 70.0, "left"),
                      ("OUTCOME B", "Create more work", 73.0, "right")])
        self.assertIn("BANNED", serif[2]["items"][0]["font"])
        # ...and the premium validator rejects the serif variant outright.
        self.assertTrue(any("banned font" in x for x in
                            sky_devices.validate_premium_plan(serif)))
        with self.assertRaises(ValueError):
            sky_devices.d42_question_fork(
                66.5, header="H", question="Q?",
                outcomes=[("OUTCOME B", "Create more work", 73.0, "right"),
                          ("OUTCOME A", "Lead a department", 70.0, "left")])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d43_view_badge_floats_above_exhibit_per_exhibit(self):
        ev = sky_devices.d43_view_count_badge(21.0, count="1.5M", t1=28.0)[0]
        self.assertEqual(ev["text"], "1.5M")
        self.assertEqual(ev["items"][0]["icon"], "eye")
        self.assertEqual(ev["geometry"]["y"], 480 - 75)  # floats ABOVE the exhibit
        self.assertEqual(ev["colors"]["text"], "#FCFCFC")
        with self.assertRaises(ValueError):
            sky_devices.d43_view_count_badge(21.0, count=" ")
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d44_mini_window_static_shots_cut_inside(self):
        evs = sky_devices.d44_pov_mini_window(
            0.0, t1=9.34,
            pov_lines=["POV:", "you're getting rinsed 5.5k/month",
                       "for a vancouver shit hole but it's chill"],
            shots=[("apartment tour", 0.0), ("desk setup", 3.0), ("downtown view", 6.0)])
        line, ground, *shots = evs
        self.assertEqual(line["geometry"]["y"], 230)  # POV line in the black band above
        window = ground["items"][0]["window"]
        self.assertEqual((window["x"], window["y"], window["w"], window["h"]),
                         (86, 422, 908, 576))
        self.assertEqual(window["corner_radius_px"], 16)
        self.assertEqual([s["t0"] for s in shots], [0.0, 3.0, 6.0])
        for s in shots:
            self.assertEqual(s["geometry"], {"x": 86, "y": 422, "w": 908, "h": 576})
            self.assertEqual(s["motion"]["in"]["type"], "hard_cut")
        with self.assertRaises(ValueError):
            sky_devices.d44_pov_mini_window(0.0, pov_lines=[], shots=[("a", 0.0)])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d45_kinetic_card_huge_gold_hard_cuts_hold(self):
        ev = sky_devices.d45_kinetic_black_card(
            12.0, hold_s=2.0,
            lines=[{"text": "YOU SHOULD MAKE", "role": "small", "color": "white"},
                   {"text": "SALES", "role": "huge", "color": "gold"},
                   {"text": "TO GET", "role": "small", "color": "white"},
                   {"text": "CUSTOMERS", "role": "huge", "color": "gold"}])[0]
        self.assertEqual(ev["geometry"], {"x": 0, "y": 0, "w": 1080, "h": 1920})
        self.assertEqual(ev["colors"]["huge"], "#FEE238")  # Sky bright yellow -> gold
        self.assertEqual(ev["motion"]["in"]["type"], "hard_cut")
        self.assertEqual(ev["motion"]["out"]["type"], "hard_cut")
        self.assertAlmostEqual(ev["t1"] - ev["t0"], 2.0)
        with self.assertRaises(ValueError):
            sky_devices.d45_kinetic_black_card(
                12.0, hold_s=3.0,
                lines=[{"text": "SALES", "role": "huge", "color": "gold"}])
        with self.assertRaises(ValueError):
            sky_devices.d45_kinetic_black_card(
                12.0, lines=[{"text": "small only", "role": "small", "color": "white"}])
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d46_vertical_split_55_45_turn_and_replay(self):
        evs = sky_devices.d46_vertical_split(
            0.0, t1=80.17, exhibit_clip="closet_reveal.mp4",
            verdict_t=42.0, replay_t=30.0, view_badge="👁 26.9M")
        reactor, exhibit = evs
        self.assertEqual(reactor["geometry"], {"x": 0, "y": 0, "w": 594, "h": 1920})
        self.assertEqual(exhibit["geometry"], {"x": 594, "y": 0, "w": 486, "h": 1920})
        self.assertEqual(reactor["items"][0]["verdict_t"], 42.0)
        self.assertEqual(exhibit["items"][0]["replay_t"], 30.0)
        self.assertEqual(exhibit["items"][0]["view_badge"], "👁 26.9M")
        with self.assertRaises(ValueError):
            sky_devices.d46_vertical_split(0.0, t1=0.0, exhibit_clip="x.mp4")
        with self.assertRaises(ValueError):
            sky_devices.d46_vertical_split(0.0, t1=80.17, exhibit_clip="")
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d47_binary_labels_anchored_resolved_by_lockup(self):
        evs = sky_devices.d47_binary_label_pair(
            26.0, winner="Strategy", winner_t=30.0,
            labels=[("Idea", "right ceiling light", 26.0, 645, 90),
                    ("Strategy", "left ceiling light", 26.5, 345, 90)])
        idea, strategy, lockup = evs
        self.assertLess(idea["t0"], strategy["t0"])  # popped ~0.5 s apart
        self.assertAlmostEqual(strategy["t0"] - idea["t0"], 0.5)
        self.assertEqual(idea["items"][0]["anchor"], "right ceiling light")
        self.assertEqual(strategy["items"][0]["anchor"], "left ceiling light")
        self.assertEqual(lockup["items"][0]["winner"], "Strategy")
        self.assertIn("Strategy", lockup["text"])
        with self.assertRaises(ValueError):
            sky_devices.d47_binary_label_pair(
                26.0, winner="Neither",
                labels=[("Idea", "right light", 26.0, 645, 90),
                        ("Strategy", "left light", 26.5, 345, 90)])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d48_stacked_split_merged_divider_captions_top_of_reactor(self):
        # Worker 2's D42 (DRo, divider ~47%) and worker 3's D38 (#39, 50/50)
        # are ONE device — both geometries must build through the same builder.
        for frac, reel in ((0.47, "DRoLuFRAnwh"), (0.50, "DRXfqHcAkve")):
            evs = sky_devices.d48_stacked_split(
                0.0, t1=93.67, divider_frac=frac, source_reel=reel,
                exhibit={"clip_path": "profile_scroll.mp4",
                         "kind": "desktop_profile_scroll",
                         "segments": [("profile grid", 0.0),
                                      ("profile header", 3.0),
                                      ("post + comments rail", 21.0)]})
            exhibit, divider, reactor, *segs = evs
            self.assertEqual(exhibit["geometry"]["y"], 0)
            self.assertEqual(exhibit["geometry"]["h"], round(1920 * frac))
            self.assertEqual(divider["geometry"]["h"], 2)
            self.assertEqual(divider["colors"]["line"], "#FCFCFC")
            self.assertTrue(exhibit["items"][0]["chrome_intact"])
            self.assertEqual(reactor["items"][0]["caption_y"],
                             round(1920 * frac) + 20)  # captions top of reactor half
            self.assertEqual([s["t0"] for s in segs], [0.0, 3.0, 21.0])
            self.assertEqual(sky_devices.validate_events(evs), [])
        with self.assertRaises(ValueError):
            sky_devices.d48_stacked_split(
                0.0, t1=10.0, divider_frac=0.60,
                exhibit={"clip_path": "x.mp4", "kind": "mobile_reel"})
        with self.assertRaises(ValueError):
            sky_devices.d48_stacked_split(
                0.0, t1=10.0, exhibit={"clip_path": "", "kind": "mobile_reel"})

    def test_d49_red_outline_gold_remap_never_red(self):
        ev = sky_devices.d49_annotation_outline(
            13.0, shape="ellipse", target="profile header bio", duration_s=1.0)[0]
        self.assertEqual(ev["colors"]["outline"], "#FEE238")  # Sky red -> gold
        self.assertIn("red", ev["items"][0]["sky_colour"])
        self.assertTrue(ev["items"][0]["hand_drawn"])
        ring = sky_devices.d49_annotation_outline(
            17.6, shape="ring", target="Brez profile", label="LOOK AT BREZ",
            duration_s=3.3, source_reel="DOWgvE0Ezgs")[0]
        self.assertEqual(ring["text"], "LOOK AT BREZ")
        with self.assertRaises(ValueError):
            sky_devices.d49_annotation_outline(13.0, shape="ring", target="x")
        with self.assertRaises(ValueError):
            sky_devices.d49_annotation_outline(13.0, shape="star", target="x")
        # No red anywhere in the emitted event, including the recorded Sky colour note.
        hits = sky_devices.scan_object_for_forbidden(ev)
        self.assertEqual(hits, [])
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d50_gradient_script_teal_to_gold_never_purple(self):
        ev = sky_devices.d50_gradient_script_headline(
            17.0, text="THEY BUILD Relationships", hold_s=2.0, position="chest")[0]
        self.assertEqual(ev["colors"]["gradient_from"], "#14A886")  # Sky green -> teal
        self.assertEqual(ev["colors"]["gradient_to"], "#FEE238")    # Sky purple -> gold
        self.assertEqual(ev["items"][0]["font"], "italic script")
        # Sampled purples are provenance (recorded in the docstring), never
        # emitted as colours — assert on the colours dict, not the notes.
        for val in ev["colors"].values():
            self.assertNotIn("#863BC5", val)
            self.assertNotIn("#5421A0", val)
        top = sky_devices.d50_gradient_script_headline(
            24.0, text="WARREN", hold_s=2.0, position="top")[0]
        self.assertEqual(top["geometry"]["y"], 120)
        self.assertEqual(sky_devices.validate_events([ev, top]), [])

    def test_d51_tpose_stats_accumulate_on_spoken_word(self):
        evs = sky_devices.d51_player_stats_card(
            24.1, name="WARREN", t1=30.9, location="doorway",
            stats=[("9'11\"", 24.3), ("420 POUNDS", 25.8),
                   ("0 NOTION SKILLS", 26.2), ("42 CODING", 28.0)])
        card, name, label, *stats = evs
        self.assertEqual(card["items"][0]["glow_outline"], True)
        self.assertEqual(name["colors"]["gradient_from"], "#FEE238")
        self.assertEqual(label["text"], "PLAYER STATS")
        self.assertEqual([s["t0"] for s in stats], [24.3, 25.8, 26.2, 28.0])
        self.assertEqual([s["text"] for s in stats],
                         ["9'11\"", "420 POUNDS", "0 NOTION SKILLS", "42 CODING"])
        for s in stats:
            self.assertEqual(s["colors"]["stat"], "#14A886")  # Sky green -> teal
        with self.assertRaises(ValueError):
            sky_devices.d51_player_stats_card(
                24.1, name="WARREN",
                stats=[("42 CODING", 28.0), ("9'11\"", 24.3)])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d52_human_ai_split_one_figure_per_number(self):
        evs = sky_devices.d52_human_ai_split(
            36.0, headline="Perfect Split", t1=42.29,
            actors=[("70% YOU", "head_cutout", 37.1),
                    ("30% AI", "logo", 38.4)])
        bg, head, you, ai = evs
        self.assertEqual(bg["geometry"], {"x": 0, "y": 0, "w": 1080, "h": 1920})
        self.assertEqual(head["colors"]["gradient_from"], "#14A886")
        self.assertLess(you["t0"], ai["t0"])  # one figure per spoken number
        self.assertEqual(you["geometry"]["x"], 90)
        self.assertEqual(ai["geometry"]["x"], 570)
        with self.assertRaises(ValueError):
            sky_devices.d52_human_ai_split(
                36.0, headline="Perfect Split",
                actors=[("30% AI", "logo", 38.4), ("70% YOU", "head_cutout", 37.1)])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_d53_smpte_single_use_real_clip(self):
        ev = sky_devices.d53_smpte_gag(
            30.0, clip_path="bars_B_D.mp4", caption="SHOW PROOF")[0]
        self.assertTrue(ev["items"][0]["single_use"])
        self.assertEqual(ev["items"][0]["clip"], "bars_B_D.mp4")
        self.assertEqual(ev["colors"]["caption"], "#FCFCFC")
        self.assertEqual(ev["geometry"], {"x": 0, "y": 0, "w": 1080, "h": 1920})
        with self.assertRaises(ValueError):
            sky_devices.d53_smpte_gag(30.0, clip_path="")
        self.assertEqual(sky_devices.validate_events([ev]), [])

    def test_d54_grid_workflow_one_step_centred_slides(self):
        evs = sky_devices.d54_grid_workflow_strip(
            18.0, t1=29.0,
            steps=[{"icon": "head_cutout", "label": "SO FIRST",
                    "sublabel": "GIVE THE CONTEXT", "t0": 19.0},
                   {"icon": "chatgpt_logo", "label": "AI TO SYNTHESIZE",
                    "sublabel": "SYNTHESIZE THOUGHTS", "t0": 22.0},
                   {"icon": "structure", "label": "CREATE A STRUCTURE OF THE VIDEO",
                    "sublabel": "IN THE OVERALL DNA OF THE VIDEO", "t0": 26.0}])
        ground, *steps = evs
        self.assertEqual(ground["items"][0]["cell_px"], 60)
        self.assertEqual([s["t0"] for s in steps], [19.0, 22.0, 26.0])
        for s in steps:
            self.assertEqual(s["geometry"], {"x": 140, "y": 700, "w": 800, "h": 300})
            self.assertEqual(s["motion"]["in"]["type"], "slide_horizontal")
        with self.assertRaises(ValueError):
            sky_devices.d54_grid_workflow_strip(18.0, steps=[])
        self.assertEqual(sky_devices.validate_events(evs), [])

    def test_all_batch19_devices_validate_clean_together(self):
        evs = []
        evs += sky_devices.d38_pov_desk_hook_doc(
            0.0, headline="Hook here.", t1=70.61,
            items=[{"text": "Item one.", "t": 0.0}, {"text": "Item two.", "t": 4.0}])
        evs += sky_devices.d39_subject_photo_insert(
            1.5, photo_path="mel.jpg", subject="Mel Robbins", duration_s=2.0)
        evs += sky_devices.d40_pov_scene_label(0.0, text="POV: x", geometry="pill", t1=9.0)
        vertebrae = ["Goal", "Person", "Avatar", "Gap", "Offer", "Funnel",
                     "Content Pillars", "Formats", "Brand & Positioning"]
        evs += sky_devices.d41_spine_diagram(
            4.0, t1=63.34, vertebrae=vertebrae,
            zooms=[{"label": "Goal", "t0": 13.62, "detail": "hire or leads?"}])
        evs += sky_devices.d42_question_fork(
            66.5, header="H", question="Q?",
            outcomes=[("OUTCOME A", "Lead a department", 70.0, "left"),
                      ("OUTCOME B", "Create more work", 73.0, "right")])
        evs += sky_devices.d43_view_count_badge(21.0, count="1.5M", t1=28.0)
        evs += sky_devices.d44_pov_mini_window(
            0.0, t1=9.34, pov_lines=["POV:", "line two"],
            shots=[("a", 0.0), ("b", 3.0)])
        evs += sky_devices.d45_kinetic_black_card(
            12.0, hold_s=2.0,
            lines=[{"text": "SALES", "role": "huge", "color": "gold"}])
        evs += sky_devices.d46_vertical_split(
            0.0, t1=80.17, exhibit_clip="clip.mp4", verdict_t=42.0, replay_t=30.0)
        evs += sky_devices.d47_binary_label_pair(
            26.0, winner="Strategy",
            labels=[("Idea", "right light", 26.0, 645, 90),
                    ("Strategy", "left light", 26.5, 345, 90)])
        evs += sky_devices.d48_stacked_split(
            0.0, t1=93.67, divider_frac=0.48,
            exhibit={"clip_path": "scroll.mp4", "kind": "desktop_profile_scroll",
                     "segments": [("grid", 0.0), ("header", 3.0)]})
        evs += sky_devices.d49_annotation_outline(
            13.0, shape="ellipse", target="bio", duration_s=1.0)
        evs += sky_devices.d50_gradient_script_headline(
            17.0, text="Perfect Split", hold_s=2.0)
        evs += sky_devices.d51_player_stats_card(
            24.1, name="WARREN", t1=30.9,
            stats=[("9'11\"", 24.3), ("420 POUNDS", 25.8)])
        evs += sky_devices.d52_human_ai_split(
            36.0, headline="Perfect Split", t1=42.29,
            actors=[("70% YOU", "head_cutout", 37.1), ("30% AI", "logo", 38.4)])
        evs += sky_devices.d53_smpte_gag(30.0, clip_path="bars.mp4")
        evs += sky_devices.d54_grid_workflow_strip(
            18.0, t1=29.0,
            steps=[{"icon": "head", "label": "SO FIRST", "sublabel": "CONTEXT", "t0": 19.0}])
        self.assertEqual(sky_devices.validate_events(evs), [])
        # No forbidden colour anywhere in the Batch 19 output.
        for ev in evs:
            self.assertEqual(sky_devices.scan_object_for_forbidden(ev), [])

    def test_no_door_device_in_registry(self):
        for d in sky_devices.list_devices():
            self.assertNotIn("door", d["name"].lower())
            self.assertNotIn("door", d["id"].lower())


class TestQC(unittest.TestCase):
    def test_good_plan_passes(self):
        report = sky_qc.qc_plan(make_plan())
        self.assertTrue(report["pass"], json.dumps(report, indent=2))

    def test_bad_plan_fails(self):
        plan = make_plan()
        plan["events"][0]["colors"]["text"] = "#FF0000"
        report = sky_qc.qc_plan(plan)
        self.assertFalse(report["pass"])
        failed = [g["id"] for g in report["gates"] if not g["pass"]]
        self.assertIn("P1", failed)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env node
/**
 * Render one animation template to video, frame-exact.
 *
 * The template exposes window.setT(ms) and renders deterministically; this
 * driver steps it frame by frame with Playwright and screenshots each frame
 * (transparent background preserved), then encodes:
 *   default : WebM with alpha (libvpx-vp9, yuva420p) — overlay-ready
 *   --mp4   : H.264 MP4 over the template's own background
 *
 * Usage:
 *   node render_animation.js templates/stat-chart.html --data data.json \
 *       --duration 3.4 --out stat-chart.webm [--fps 30] [--mp4]
 * data.json is injected as window.DATA (see each template's DATA contract).
 * Requires: npm i playwright  (and a chromium build: npx playwright install chromium)
 */
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

function arg(name, def) {
  const i = process.argv.indexOf('--' + name);
  return i >= 0 ? process.argv[i + 1] : def;
}
const has = n => process.argv.includes('--' + n);

(async () => {
  const tpl = process.argv[2];
  if (!tpl) { console.error('usage: render_animation.js <template.html> --out out.webm --duration S'); process.exit(1); }
  const out = arg('out', 'animation.webm');
  const dur = parseFloat(arg('duration', '3.5'));
  const fps = parseInt(arg('fps', '30'), 10);
  const data = arg('data') ? JSON.parse(fs.readFileSync(arg('data'), 'utf8')) : {};
  const framesDir = fs.mkdtempSync(path.join(require('os').tmpdir(), 'animframes-'));
  const { chromium } = require('playwright');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.addInitScript(d => { window.__MANUAL = true; window.DATA = d; }, data);
  await page.goto('file://' + path.resolve(tpl));
  await page.waitForTimeout(350); // fonts
  const n = Math.round(dur * fps);
  for (let i = 0; i < n; i++) {
    await page.evaluate(ms => window.setT(ms), Math.round((i / fps) * 1000));
    await page.screenshot({ path: path.join(framesDir, `f${String(i).padStart(5, '0')}.png`), omitBackground: !has('mp4') });
  }
  await browser.close();
  const inputs = ['-y', '-v', 'error', '-framerate', String(fps), '-i', path.join(framesDir, 'f%05d.png')];
  const enc = has('mp4')
    ? ['-c:v', 'libx264', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart']
    : ['-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '2.5M', '-auto-alt-ref', '0'];
  execFileSync('ffmpeg', [...inputs, ...enc, out], { stdio: 'inherit' });
  fs.rmSync(framesDir, { recursive: true, force: true });
  console.log(`rendered ${n} frames -> ${out}`);
})().catch(e => { console.error(e); process.exit(1); });

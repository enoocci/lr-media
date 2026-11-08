// Generic renderer: HTML -> JPG card, or HTML with CSS animations -> MP4 Reel.
// Used by build.js (same file in templates/fp and templates/ss).
//
//   const R = require('./render');
//   await R.card(browser, htmlPath, outJpg, 1080, 1350);
//   await R.reel(browser, htmlPath, outMp4, {w:1080,h:1920,dur:18,fps:30,music,offset});
//
// Video method: every CSS animation is paused, then for each frame we set
// animation.currentTime = t and take a screenshot that is piped into ffmpeg
// (libx264 yuv420p crf 20 + aac 160k, loudnorm -14 LUFS, audio fade in/out).
// Needs: npm i playwright@1 (Chromium in /opt/pw-browsers, never `playwright install`).
const { spawn } = require('child_process');
const path = require('path');

function launch() {
  const { chromium } = require('playwright');
  // Use the preinstalled Chromium (its revision may differ from the npm playwright one).
  const fs = require('fs');
  let exe = process.env.CHROME;
  if (!exe) {
    const base = '/opt/pw-browsers';
    const d = fs.existsSync(base) ? fs.readdirSync(base).filter(x => /^chromium-\d+$/.test(x)).sort().pop() : null;
    if (d) exe = `${base}/${d}/chrome-linux64/chrome`;
  }
  return chromium.launch({ executablePath: exe, args: ['--disable-gpu', '--font-render-hinting=none'] });
}

async function open(browser, html, w, h) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(html));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  return page;
}

// Fails loudly if any element marked .chk overflows its box.
async function overflow(page) {
  return page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('.chk').forEach(e => {
      if (e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1) bad.push(e.className + ': ' + e.textContent.slice(0, 40));
    });
    const r = document.body.getBoundingClientRect();
    if (document.body.scrollHeight > innerHeight + 1) bad.push('body taller than viewport');
    return bad;
  });
}

async function card(browser, html, out, w = 1080, h = 1350) {
  const page = await open(browser, html, w, h);
  const bad = await overflow(page);
  await page.screenshot({ path: out, type: 'jpeg', quality: 92 });
  await page.close();
  return bad;
}

async function reel(browser, html, out, o) {
  const { w = 1080, h = 1920, dur = 18, fps = 30, music, offset = 0 } = o;
  const page = await open(browser, html, w, h);
  await page.evaluate(() => document.getAnimations().forEach(a => a.pause()));
  const fadeOut = dur - 1.8;
  const ff = spawn('ffmpeg', ['-v', 'error', '-y',
    '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
    '-ss', String(offset), '-t', String(dur), '-i', music,
    '-filter_complex', `[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100,afade=t=in:d=0.6,afade=t=out:st=${fadeOut}:d=1.8[a]`,
    '-map', '0:v', '-map', '[a]',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', String(fps),
    '-c:a', 'aac', '-b:a', '160k', '-ar', '44100', '-t', String(dur), '-movflags', '+faststart', out],
    { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => ff.on('close', c => c ? rej(new Error('ffmpeg ' + c + ' ' + out)) : res()));
  const n = Math.round(dur * fps);
  const badAll = new Set();
  for (let i = 0; i < n; i++) {
    const t = (i / fps) * 1000;
    await page.evaluate(t => document.getAnimations().forEach(a => { a.currentTime = t; }), t);
    if (i % 60 === 0) (await overflow(page)).forEach(b => badAll.add(b));
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await done;
  await page.close();
  return [...badAll];
}

module.exports = { launch, card, reel };

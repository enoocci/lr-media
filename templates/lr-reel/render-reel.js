// Reel « L'ACTU EN 30 SECONDES » — Le Rapporteur
// node render-reel.js <config.json> <out.mp4>
// config: {theme:"light"|"dark", series:"IMMIGRATION", hook:{big,sub}, screens:[{k,big,txt}], final:{q,opts:[A,B,C],suite:bool},
//          music:"music/lr-news-1.mp3", musicStart:10, hookDur:2.5, scrDur:4.6, finalDur:5}
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../..');
const FPS = 30, W = 1080, H = 1920;

const [cfgPath, out] = process.argv.slice(2);
const c = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
const hookDur = c.hookDur || 2.5, scrDur = c.scrDur || 4.6, finalDur = c.finalDur || 5.5;
const total = hookDur + c.screens.length * scrDur + finalDur;
const dark = c.theme === 'dark';
const fg = dark ? '#F4F5F2' : '#141816', bg = dark ? '#141816' : '#F4F5F2', mute = dark ? '#B9C0BB' : '#4A524D';
const F = 'file://' + ROOT + '/templates/lr-card/fonts/';
const mark = 'file://' + ROOT + '/templates/lr-card/' + (dark ? 'lr-mark-blanc.png' : 'lr-mark.png');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');

let scr = '', t = hookDur;
scr += `<div class="s hook" style="animation:io ${hookDur}s linear 0s both"><div class="hb">${esc(c.hook.big)}</div>${c.hook.sub ? `<div class="hs">${esc(c.hook.sub)}</div>` : ''}</div>`;
c.screens.forEach((s, i) => {
  scr += `<div class="s" style="animation:io ${scrDur}s linear ${t}s both"><div class="num">${i + 1}/${c.screens.length}</div><div class="k">${esc(s.k)}</div><div class="big">${esc(s.big)}</div><div class="txt">${esc(s.txt)}</div></div>`;
  t += scrDur;
});
scr += `<div class="s fin" style="animation:in ${finalDur}s linear ${t}s both"><div class="q">${esc(c.final.q)}</div>${c.final.opts.map((o, i) => `<div class="o"><b>${'ABC'[i]}</b>${esc(o)}</div>`).join('')}<div class="fc">🔔 Abonnez-vous : chaque soir, l'actu qui compte</div>${c.final.suite ? '<div class="suite">La suite demain</div>' : ''}</div>`;

const html = `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Oswald;src:url('${F}Oswald.ttf');font-weight:200 700}
@font-face{font-family:Plex;src:url('${F}IBMPlexSansCondensed-Bold.ttf');font-weight:700}
@font-face{font-family:Plex;src:url('${F}IBMPlexSansCondensed-SemiBold.ttf');font-weight:600}
*{margin:0;box-sizing:border-box}
body{width:${W}px;height:${H}px;overflow:hidden;background:${bg};color:${fg};font-family:Plex,'Noto Color Emoji'}
.bar{position:absolute;left:0;top:0;height:12px;background:#C3232B;animation:bar ${total}s linear 0s both}
.top{position:absolute;top:110px;left:70px;right:70px;display:flex;gap:16px;flex-wrap:wrap}
.pill{font-weight:700;font-size:34px;letter-spacing:.1em;color:#fff;padding:10px 22px;border-radius:8px}
.red{background:#C3232B}.grn{background:#0E7447}
.s{position:absolute;left:70px;right:70px;top:300px;bottom:420px;display:flex;flex-direction:column;justify-content:center;opacity:0}
.hb{font-family:Oswald;font-weight:700;font-size:126px;line-height:1.06;text-transform:uppercase}
.hs{margin-top:34px;font-weight:700;font-size:54px;color:#0E7447;${dark ? 'color:#4FC48A;' : ''}}
.num{font-weight:700;font-size:32px;color:${mute};letter-spacing:.1em}
.k{margin-top:18px;align-self:flex-start;font-weight:700;font-size:40px;letter-spacing:.12em;color:#fff;background:#0E7447;padding:8px 20px;border-radius:6px}
.big{margin-top:30px;font-family:Oswald;font-weight:700;font-size:118px;line-height:1.05;text-transform:uppercase}
.txt{margin-top:34px;font-weight:600;font-size:56px;line-height:1.25;color:${fg}}
.q{font-family:Oswald;font-weight:700;font-size:78px;line-height:1.1;margin-bottom:34px;color:${fg}}
.o{display:flex;gap:24px;align-items:center;font-weight:700;font-size:52px;margin:14px 0;color:${fg}}
.o b{flex:none;width:80px;height:80px;border-radius:50%;background:${fg};color:${bg};display:flex;align-items:center;justify-content:center;font-family:Oswald;font-size:48px}
.fc{margin-top:46px;font-weight:700;font-size:50px;line-height:1.2;color:#C3232B}
.suite{margin-top:20px;font-family:Oswald;font-weight:700;font-size:56px;color:#0E7447;text-transform:uppercase}
.cta{position:absolute;left:0;right:0;bottom:170px;height:100px;background:#C3232B;color:#fff;font-weight:700;font-size:48px;display:flex;align-items:center;justify-content:center;animation:cta ${total}s linear 0s both}
.brand{position:absolute;left:0;right:0;bottom:0;height:170px;display:flex;align-items:center;justify-content:center;gap:22px;border-top:4px solid #0E7447}
.brand img{height:84px}.brand .n{font-family:Oswald;font-weight:700;font-size:54px;letter-spacing:.04em}
.brand .w{font-weight:700;font-size:32px;color:#C3232B}
@keyframes io{0%{opacity:0;transform:translateY(40px)}7%{opacity:1;transform:none}93%{opacity:1;transform:none}100%{opacity:0;transform:translateY(-20px)}}
@keyframes in{0%{opacity:0;transform:scale(.96)}8%{opacity:1;transform:none}100%{opacity:1;transform:none}}
@keyframes bar{from{width:0}to{width:100%}}
@keyframes cta{0%,${(3 / total * 100).toFixed(2)}%{transform:translateY(130%);opacity:0}${(3.3 / total * 100).toFixed(2)}%,100%{transform:none;opacity:1}}
</style></head><body><div class="bar"></div>
<div class="top"><span class="pill red">L'ACTU EN 30 SECONDES</span>${c.series ? `<span class="pill grn">${esc(c.series)}</span>` : ''}</div>
${scr}
<div class="cta">🔔 Abonnez-vous</div>
<div class="brand"><img src="${mark}"><span class="n">LE RAPPORTEUR</span><span class="w">lerapporteur.net</span></div>
</body></html>`;

(async () => {
  const tmp = out.replace(/\.mp4$/, '');
  fs.writeFileSync(tmp + '.html', html);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto('file://' + path.resolve(tmp + '.html'));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  await p.evaluate(() => document.getAnimations().forEach(a => a.pause()));
  const n = Math.round(total * FPS);
  const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', '' + FPS, '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium', tmp + '-v.mp4'], { stdio: ['pipe', 'ignore', 'inherit'] });
  const checks = (c.checks || [1.2, hookDur + 2, hookDur + scrDur * 2 + 2, total - 1]).map(s => Math.round(s * FPS));
  for (let i = 0; i < n; i++) {
    await p.evaluate(ms => document.getAnimations().forEach(a => a.currentTime = ms), i * 1000 / FPS);
    const buf = await p.screenshot({ type: 'jpeg', quality: 90 });
    if (checks.includes(i)) fs.writeFileSync(`${tmp}-chk-${i}.jpg`, buf);
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
  const ms = c.musicStart || 0;
  execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', tmp + '-v.mp4', '-ss', '' + ms, '-t', '' + total, '-i', path.join(ROOT, c.music || 'music/lr-news-1.mp3'),
    '-filter_complex', `[1:a]afade=t=in:st=0:d=0.6,afade=t=out:st=${(total - 1.8).toFixed(2)}:d=1.8,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]`,
    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out]);
  fs.unlinkSync(tmp + '-v.mp4');
  console.log('OK', out, total.toFixed(1) + 's', n, 'frames');
})();

// Stars & Style (@thestarsandstyle) Reel template, 1080x1920, 18 s.
// Black #14110C, gold #D4A937, cream #EFE2BF. Bodoni Moda (titles, numbers) +
// IBM Plex Sans Condensed (text). "S✦S" top right.
// Bodoni Moda has no hyphenation-friendly glyph handling here: NEVER put hyphens in titles.
// Timeline (s): big intro word 0-2.6 | kicker+title 2.8 | steps 3.6.. | scene 2 at 14.4: question,
// A/B/C options, follow line | end 18.
const D = __dirname;
const CSS = `@font-face{font-family:Bodoni;src:url('file://${D}/fonts/bodoni-moda-latin-standard-normal.woff2') format('woff2');font-weight:400 900;font-style:normal}
@font-face{font-family:Bodoni;src:url('file://${D}/fonts/bodoni-moda-latin-standard-italic.woff2') format('woff2');font-weight:400 900;font-style:italic}
@font-face{font-family:Plex;src:url('file://${D}/fonts/IBMPlexSansCondensed-SemiBold.ttf');font-weight:600}
@font-face{font-family:Plex;src:url('file://${D}/fonts/IBMPlexSansCondensed-Bold.ttf');font-weight:700}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:#14110C;color:#EFE2BF;font-family:Plex,'Noto Color Emoji';hyphens:none}
.glow{position:absolute;inset:0;background:radial-gradient(circle at 50% 42%,rgba(212,169,55,.16) 0%,rgba(212,169,55,.05) 32%,rgba(20,17,12,0) 60%);animation:breathe 6s ease-in-out infinite alternate both}
@keyframes breathe{from{opacity:.75}to{opacity:1}}
.fr{position:absolute;inset:44px;border:2.5px solid #D4A937}
.top{position:absolute;left:100px;right:100px;top:140px;display:flex;justify-content:space-between;align-items:center}
.top span{font-weight:700;font-size:27px;letter-spacing:.32em;color:#D4A937}
.top .logo{font-family:Bodoni;font-weight:800;font-size:66px;letter-spacing:.04em;color:#D4A937}
.foot{position:absolute;left:0;right:0;bottom:140px;text-align:center;font-weight:700;font-size:28px;letter-spacing:.34em;color:#cbbd97}
.big{position:absolute;left:0;right:0;top:820px;text-align:center;font-family:Bodoni;font-weight:600;font-size:230px;line-height:1;color:#D4A937;letter-spacing:.02em;
 animation:bigin 1s cubic-bezier(.2,.8,.3,1) .1s both,bigout .45s ease-in 2.25s forwards}
@keyframes bigin{from{opacity:0;letter-spacing:.25em;filter:blur(8px)}to{opacity:1;letter-spacing:.02em;filter:blur(0)}}
@keyframes bigout{to{opacity:0;transform:scale(.92)}}
.s1,.s2{position:absolute;left:100px;right:100px;top:600px}
.s1{animation:hide .45s ease-in 13.9s forwards}
@keyframes hide{to{opacity:0;transform:translateY(-30px)}}
.k{font-weight:700;font-size:28px;letter-spacing:.36em;color:#D4A937;margin-bottom:26px}
.t{font-family:Bodoni;font-weight:500;font-size:116px;line-height:1.02;text-wrap:balance}
.t i,.q i{color:#D4A937}
.rule{width:160px;height:3px;background:#D4A937;margin:52px 0 40px;transform-origin:left}
.in{animation:rise .6s cubic-bezier(.2,.8,.3,1) both}
@keyframes rise{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}
.grow{animation:grow .6s ease-out both}@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.st{display:flex;align-items:baseline;gap:40px;padding:30px 0 32px;border-bottom:1.5px solid rgba(239,226,191,.24)}
.st b{font-family:Bodoni;font-weight:800;font-variation-settings:'opsz' 28;font-size:72px;line-height:1;color:#D4A937;min-width:46px}
.st span{font-weight:600;font-size:50px;line-height:1.25;text-wrap:balance}
.q{font-family:Bodoni;font-weight:500;font-size:110px;line-height:1.05;margin-bottom:56px;text-wrap:balance}
.op{display:flex;align-items:center;gap:30px;padding:22px 26px;margin-bottom:28px;border:2.5px solid #D4A937}
.op b{width:80px;height:80px;flex:none;background:#D4A937;color:#14110C;display:grid;place-items:center;font-family:Bodoni;font-weight:800;font-size:56px;line-height:1}
.op span{font-weight:700;font-size:50px}
.fol{margin-top:56px;font-weight:700;font-size:52px;color:#D4A937}`;

function reel(r) {
  const n = r.steps.length;
  const st = n === 4 ? [3.8, 6.3, 8.8, 11.3] : [3.8, 7.0, 10.2];
  const steps = r.steps.map((s, i) => `<div class="st in" style="animation-delay:${st[i]}s"><b>${i + 1}</b><span>${s}</span></div>`).join('');
  const ops = r.opts.map((o, i) => `<div class="op in" style="animation-delay:${15.0 + i * .35}s"><b>${'ABC'[i]}</b><span>${o}</span></div>`).join('');
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>
<div class="glow"></div><div class="fr"></div>
<div class="top"><span>STARS &amp; STYLE</span><span class="logo">S✦S</span></div>
<div class="big" style="font-size:${Math.min(230, Math.round(1150 / r.big.length))}px">${r.big}</div>
<div class="s1"><div class="k in" style="animation-delay:2.7s">${r.kicker}</div><div class="t in" style="animation-delay:2.85s">${r.title}</div><div class="rule grow" style="animation-delay:3.3s"></div>${steps}</div>
<div class="s2"><div class="q in" style="animation-delay:14.5s">${r.q}</div>${ops}<div class="fol in" style="animation-delay:${15.0 + r.opts.length * .35 + .3}s">✦ Follow @thestarsandstyle</div></div>
<div class="foot">STYLE · STARS · STORIES</div>
</body></html>`;
}

module.exports = { reel };

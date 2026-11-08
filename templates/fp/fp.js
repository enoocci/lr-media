// Full Pocket templates: feed card (1080x1350) and Reel (1080x1920, 18 s).
// Brand: green #0D4F3C, gold #F2B63C, mint #E6F2EC, $100 bill photo watermark,
// green pocket logo with gold coin. Titles Lora 700, body Poppins.
const D = __dirname;
const F = `@font-face{font-family:Lora;src:url('file://${D}/fonts/lora-latin-wght-normal.woff2') format('woff2');font-weight:400 700}
@font-face{font-family:Pop;src:url('file://${D}/fonts/poppins-latin-500-normal.woff2');font-weight:500}
@font-face{font-family:Pop;src:url('file://${D}/fonts/poppins-latin-600-normal.woff2');font-weight:600}
@font-face{font-family:Pop;src:url('file://${D}/fonts/poppins-latin-700-normal.woff2');font-weight:700}
@font-face{font-family:Pop;src:url('file://${D}/fonts/poppins-latin-800-normal.woff2');font-weight:800}
*{margin:0;box-sizing:border-box}
body{overflow:hidden;font-family:Pop,'Noto Color Emoji'}
h1,.t{text-wrap:balance}.sub,.opt span{text-wrap:pretty}`;

// Green pocket with dashed gold stitch and a gold coin peeking out.
const LOGO = s => `<svg viewBox="0 0 100 100" width="${s}" height="${s}"><circle cx="50" cy="24" r="17" fill="#F2B63C" stroke="#c98f1c" stroke-width="3"/><text x="50" y="32" text-anchor="middle" font-family="Pop" font-weight="700" font-size="22" fill="#7a5408">$</text><path d="M15 36 H85 V66 Q85 92 50 97 Q15 92 15 66 Z" fill="#0D4F3C" stroke="#F2B63C" stroke-width="2.5"/><path d="M23 47 Q50 57 77 47" stroke="#F2B63C" stroke-width="2.5" fill="none" stroke-dasharray="4 3"/></svg>`;

const CARD_CSS = `body{width:1080px;height:1350px}
.c{position:relative;width:100%;height:100%;padding:80px 80px 70px;display:flex;flex-direction:column}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.ov{position:absolute;inset:0}
.c>*:not(.ph):not(.ov){position:relative}
.top{display:flex;align-items:center;gap:22px}
.top .n{font-family:Lora;font-weight:700;font-size:46px}
.top .n span{color:#F2B63C}
.tag{margin-left:auto;font-weight:700;font-size:24px;letter-spacing:.2em;text-transform:uppercase;padding:13px 24px;border-radius:999px}
h1{font-family:Lora;font-weight:700;font-size:86px;line-height:1.08;margin-top:auto}
h1 em{font-style:normal;color:#F2B63C}
.nw{white-space:nowrap}.blank{display:inline-block;width:300px;height:.8em;border-bottom:7px solid #c98f1c;vertical-align:baseline}
.sub{margin-top:34px;font-weight:500;font-size:40px;line-height:1.35;max-width:900px}
.sub b{color:#F2B63C;font-weight:700}
.box{margin-top:44px;display:grid;gap:22px}
.opt{display:flex;align-items:center;gap:24px;font-weight:700;font-size:38px;line-height:1.25;padding:22px 28px;border-radius:18px}
.opt b{width:62px;height:62px;border-radius:50%;display:grid;place-items:center;font-size:30px;font-weight:700;flex:none}
.foot{margin-top:auto;padding-top:40px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:24px;letter-spacing:.06em}
.cr{font-weight:500;font-size:17px;opacity:.75;letter-spacing:0}
.tip{background:#0D4F3C;color:#fff}
.tip .ph{background-image:url('file://${D}/ph-100a.jpg');filter:saturate(.55)}
.tip .ov{background:linear-gradient(180deg,rgba(13,79,60,.78) 0%,rgba(13,79,60,.84) 60%,rgba(13,79,60,.9) 100%)}
.tip .tag{background:#F2B63C;color:#0D4F3C}
.tip .opt{background:rgba(255,255,255,.1);border:2px solid rgba(242,182,60,.5)}
.tip .opt b{background:#F2B63C;color:#0D4F3C}
.tip .foot{color:#E6F2EC}
.qst{background:#E6F2EC;color:#0D4F3C}
.qst .ph{background-image:url('file://${D}/ph-100b.jpg');filter:saturate(.7)}
.qst .ov{background:linear-gradient(180deg,rgba(230,242,236,.83) 0%,rgba(230,242,236,.9) 55%,rgba(230,242,236,.94) 100%)}
.qst .tag{background:#0D4F3C;color:#F2B63C}
.qst h1 em,.qst .top .n span,.qst .sub b{color:#c98f1c}
.qst .opt{background:#fff;border:2px solid #0D4F3C22}
.qst .opt b{background:#0D4F3C;color:#F2B63C}`;

function card({ kind, tag, h1, sub = '', opts = null }) {
  const o = opts ? '<div class="box">' + opts.map(([k, v]) => `<div class="opt"><b>${k}</b><span>${v}</span></div>`).join('') + '</div>' : '';
  const s = sub ? `<p class="sub">${sub}</p>` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><style>${F}${CARD_CSS}</style></head><body><div class="c ${kind}"><div class="ph"></div><div class="ov"></div>
<div class="top">${LOGO(92)}<div class="n">Full <span>Pocket</span></div><div class="tag">${tag}</div></div>
<h1>${h1}</h1>${s}${o}
<div class="foot"><span>MONEY MADE SIMPLE 💸</span><span class="cr">Photo: Unsplash</span></div></div></body></html>`;
}

// Reel timeline (s): emoji intro 0-2.7 | title 2.8 | steps 3.6 / 6.8 / 10.0 (/ 12.4 if 4)
// | scene 2 at 14.2: question, options, follow | end 18.
const REEL_CSS = `body{width:1080px;height:1920px;background:#0D4F3C;color:#fff}
.bg{position:absolute;inset:-40px;background:url('file://${D}/ph-100a.jpg') center/cover;filter:saturate(.55);animation:zoom 18s linear both}
.ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,79,60,.74) 0%,rgba(13,79,60,.82) 45%,rgba(13,79,60,.95) 85%,#0D4F3C 100%)}
@keyframes zoom{from{transform:scale(1)}to{transform:scale(1.07)}}
.top{position:absolute;left:84px;top:96px;display:flex;align-items:center;gap:20px}
.top .n{font-family:Lora;font-weight:700;font-size:54px}.top .n span{color:#F2B63C}
.foot{position:absolute;left:0;right:0;bottom:118px;text-align:center;font-weight:700;font-size:30px;letter-spacing:.14em;color:#E6F2EC}
.emo{position:absolute;left:0;right:0;top:520px;text-align:center;font-size:280px;line-height:1;font-family:'Noto Color Emoji';animation:pop .7s cubic-bezier(.3,1.6,.5,1) .15s both,bob 1.4s ease-in-out .85s 2 alternate both,out .4s ease-in 2.35s forwards}
@keyframes pop{from{transform:scale(0) rotate(-18deg);opacity:0}to{transform:scale(1);opacity:1}}
@keyframes bob{from{translate:0 0}to{translate:0 -36px}}
@keyframes out{to{opacity:0;scale:.6}}
.s1,.s2{position:absolute;left:80px;right:80px;top:560px}
.s1{animation:hide .4s ease-in 13.9s forwards}
@keyframes hide{to{opacity:0;transform:translateY(-30px)}}
.t{font-family:Lora;font-weight:700;font-size:100px;line-height:1.08;margin-bottom:56px}
.t em{font-style:normal;color:#F2B63C}
.in{animation:rise .55s cubic-bezier(.2,.8,.3,1) both}
@keyframes rise{from{opacity:0;transform:translateY(46px)}to{opacity:1;transform:none}}
.st{display:flex;align-items:center;gap:30px;padding:30px 34px;margin-bottom:30px;border-radius:22px;background:rgba(255,255,255,.08);border:2px solid rgba(242,182,60,.55);font-weight:600;font-size:46px;line-height:1.3}
.st b{width:84px;height:84px;flex:none;border-radius:50%;background:#F2B63C;color:#0D4F3C;display:grid;place-items:center;font-size:42px;font-weight:700}
.st span{text-wrap:balance}
.q{font-family:Lora;font-weight:700;font-size:92px;line-height:1.1;margin-bottom:50px;text-wrap:balance}
.q em{font-style:normal;color:#F2B63C}
.op{display:flex;align-items:center;gap:28px;padding:24px 30px;margin-bottom:26px;border-radius:18px;background:#E6F2EC;color:#0D4F3C;font-weight:700;font-size:48px}
.op b{width:76px;height:76px;flex:none;border-radius:50%;background:#0D4F3C;color:#F2B63C;display:grid;place-items:center;font-size:40px}
.fol{margin-top:56px;color:#F2B63C;font-weight:700;font-size:52px}`;

function reel(r, L) {
  const x = r[L];
  const n = x.steps.length;
  const st = n === 4 ? [3.6, 6.2, 8.8, 11.4] : [3.6, 6.8, 10.0];
  const steps = x.steps.map((s, i) => `<div class="st in" style="animation-delay:${st[i]}s"><b>${i + 1}</b><span>${s}</span></div>`).join('');
  const ops = x.opts.map((o, i) => `<div class="op in" style="animation-delay:${14.9 + i * .35}s"><b>${'ABC'[i]}</b>${o}</div>`).join('');
  return `<!doctype html><html><head><meta charset="utf-8"><style>${F}${REEL_CSS}</style></head><body>
<div class="bg"></div><div class="ov"></div>
<div class="top">${LOGO(104)}<div class="n">Full <span>Pocket</span></div></div>
<div class="emo">${r.emoji}</div>
<div class="s1"><div class="t in" style="animation-delay:2.8s">${x.title}</div>${steps}</div>
<div class="s2"><div class="q in" style="animation-delay:14.4s">${x.q}</div>${ops}<div class="fol in" style="animation-delay:${14.9 + x.opts.length * .35 + .3}s">🔔 ${L === 'es' ? 'Sigue a Full Pocket' : 'Follow Full Pocket'}</div></div>
<div class="foot">${L === 'es' ? 'FINANZAS SIN COMPLICACIONES' : 'MONEY MADE SIMPLE'} 💸</div>
</body></html>`;
}

module.exports = { card, reel };

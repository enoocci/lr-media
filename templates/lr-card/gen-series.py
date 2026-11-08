#!/usr/bin/env python3
"""LR evergreen card generator (1080x1350), no photos needed.

Usage:
  python3 gen-series.py cards.json OUT_DIR [--render]

cards.json = list of cards. Common keys: id, layout, q (A/B/C question, without 💬),
fol (end of the red « 🔔 Abonnez-vous à Le Rapporteur … » line), src (full "Sources : …").
Layouts:
  dark     : badge, title (HTML, <em> = green), lede, icon (key of lr_icons.ICONS), bg (badge color),
             keys [[number, text], ...]   -> « LE SAVIEZ-VOUS ? » and practical energy/health cards
  histoire : country, name, dates, wm (watermark initials), quote, qsrc (quote attribution),
             tagline (HTML), keys [[year, text] x3]  -> series « ILS ONT MARQUÉ L'HISTOIRE »
  chiffre  : tag (small line above), num (big number), unit (line under number), ctx [line1, line2]
             -> « LE CHIFFRE » card
Writes OUT_DIR/lr-<id>.html (assets resolved via <base> to this folder) and, with --render,
OUT_DIR/lr-<id>.jpg using render.js (Chromium at /opt/pw-browsers/chromium).
Title tip: glue the last two words with &nbsp; so no orphan word ends up alone on a line.
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lr_icons import ICONS, svg

CSS = '''@font-face{font-family:Oswald;src:url('fonts/Oswald.ttf');font-weight:200 700}
@font-face{font-family:Plex;src:url('fonts/IBMPlexSansCondensed-Bold.ttf');font-weight:700}
@font-face{font-family:Plex;src:url('fonts/IBMPlexSansCondensed-SemiBold.ttf');font-weight:600}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:#F4F5F2;font-family:Plex;color:#141816;position:relative}
.hero{position:absolute;left:0;right:0;top:0;background:#141816;height:520px;overflow:hidden}
.hero:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.04) 0 2px,transparent 2px 90px)}
.hero:after{content:"";position:absolute;left:0;right:0;bottom:0;height:10px;background:linear-gradient(90deg,#C3232B 50%,#0E7447 50%)}
.ic{position:absolute;right:30px;top:60px;opacity:.95}
.ser{display:inline-block;text-transform:uppercase;color:#fff;font-family:Oswald;font-weight:700;font-size:30px;letter-spacing:.12em;padding:6px 16px;border-radius:6px;background:#0E7447}
.ser.sm{font-size:24px;padding:5px 12px;margin-left:8px;vertical-align:4px}
h1{font-family:Oswald;font-weight:700;text-transform:uppercase;line-height:1.05;text-wrap:balance}
h1 em{font-style:normal;color:#0E7447}
.dkt{position:absolute;left:64px;top:70px;width:640px}
.dkt h1{color:#fff;font-size:72px;margin-top:22px}.dkt h1 em{color:#3FB27A}
.dkt .lede{margin-top:18px;color:#C9D1CC;font-weight:600;font-size:27px;line-height:1.3}
.body{position:absolute;left:64px;right:64px;top:556px;bottom:205px;display:flex;flex-direction:column;justify-content:center}
.keys{display:grid;gap:14px}
.k{display:flex;gap:20px;align-items:center;background:#fff;border:2px solid #D5DAD6;border-radius:14px;padding:16px 22px}
.k .n{flex-shrink:0;font-family:Oswald;font-weight:700;font-size:46px;line-height:1;min-width:200px;color:#0E7447;white-space:nowrap}
.k .t{font-weight:600;font-size:26px;line-height:1.28}.k .t b{color:#141816}
.q{margin-top:22px;font-weight:700;font-size:29px;color:#141816;line-height:1.25}
.fol{margin-top:12px;font-weight:700;font-size:27px;color:#C3232B}
.src{position:absolute;left:64px;right:64px;bottom:140px;font-weight:600;font-size:18px;color:#58615C;line-height:1.3}
.nb{position:absolute;left:64px;right:64px;bottom:34px;display:flex;align-items:center;justify-content:center;gap:22px}
.nb img{height:74px}.nb .w{display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.nb .t{font-family:Oswald;font-weight:600;font-size:40px;letter-spacing:.2em;line-height:1}
.nb .r{height:5px;width:100%;background:linear-gradient(90deg,#C3232B 50%,#0E7447 50%)}
.nb .u{font-weight:700;font-size:22px;letter-spacing:.1em;color:#58615C}
.k .t,.cx,.dkt .lede{text-wrap:pretty}.q{text-wrap:pretty}
.k3{gap:18px}.k3 .k{padding:22px 24px}.k3 .k .t{font-size:28px}.k3 .k .n{font-size:54px;min-width:230px}
/* histoire */
.wm{position:absolute;right:-30px;top:-40px;font-family:Oswald;font-weight:700;font-size:520px;line-height:1;color:rgba(255,255,255,.05)}
.hs{position:absolute;left:64px;right:64px;top:62px}
.hs .cty{font-weight:700;font-size:26px;letter-spacing:.2em;color:#9FD8B9;text-transform:uppercase}
.hs .nm{font-family:Oswald;font-weight:700;font-size:86px;line-height:1.02;color:#fff;text-transform:uppercase;margin-top:6px;text-wrap:balance}
.hs .dt{font-family:Oswald;font-weight:600;font-size:44px;color:#C9D1CC;margin-top:6px;letter-spacing:.04em}
.qt{margin-top:26px;border-left:10px solid #C3232B;padding:4px 0 4px 26px}
.qt .x{font-weight:700;font-style:italic;font-size:33px;line-height:1.32;color:#fff}
.qt .s{margin-top:10px;font-weight:600;font-size:21px;color:#9AA59F}
.hb{justify-content:flex-start;padding-top:0;bottom:auto}.hb h1{font-size:58px;margin:16px 0 18px}
/* chiffre */
.cf{position:absolute;left:64px;right:64px;top:64px;text-align:center}
.cf .tg{margin-top:22px;font-weight:700;font-size:28px;letter-spacing:.14em;color:#9FD8B9;text-transform:uppercase}
.cf .num{font-family:Oswald;font-weight:700;font-size:200px;line-height:1;color:#fff;margin-top:6px;white-space:nowrap}
.cf .num em{font-style:normal;color:#3FB27A}
.cf .un{font-weight:700;font-size:34px;line-height:1.25;color:#E6ECE8;margin-top:34px;text-wrap:balance}
.ctx{display:grid;gap:14px}
.cx{display:flex;gap:18px;align-items:flex-start;background:#fff;border:2px solid #D5DAD6;border-left:10px solid #0E7447;border-radius:12px;padding:16px 22px;font-weight:600;font-size:30px;line-height:1.32}
.cx .d{font-family:Oswald;font-weight:700;color:#0E7447;font-size:30px;line-height:1.2}
'''

FIT = ('<script>for(const e of document.querySelectorAll(".num")){let f=parseFloat(getComputedStyle(e).fontSize);'
       'while(e.scrollWidth>e.clientWidth&&f>60){f-=4;e.style.fontSize=f+"px"}}</script>')
LOGO = '<div class="nb"><img src="lr-mark.png"><div class="w"><div class="t">LE RAPPORTEUR</div><div class="r"></div><div class="u">lerapporteur.net</div></div></div>'


def keys_html(keys, big=True):
    cls = 'keys k3' if big and len(keys) <= 3 else 'keys'
    return f'<div class="{cls}">' + ''.join(
        f'<div class="k"><div class="n">{n}</div><div class="t">{t}</div></div>' for n, t in keys) + '</div>'


def tail(c):
    # keep each A/B/C option on one line
    q = re.sub(r'\b([ABC])\) ([^·]+)', lambda m: m.group(1) + ')&nbsp;' + m.group(2).strip().replace(' ', '&nbsp;') + ' ', c['q'])
    q = q.strip().replace(' · ', '&nbsp;· ')
    return f'<div class="q">💬 {q}</div><div class="fol">🔔 Abonnez-vous à Le Rapporteur {c["fol"]}</div>'


def card(c):
    L = c.get('layout', 'dark')
    if L == 'dark':
        lede = f'<div class="lede">{c["lede"]}</div>' if c.get('lede') else ''
        bg = c.get('bg', '#0E7447')
        hero = (f'<div class="hero"><div class="ic">{svg(ICONS[c["icon"]], 340)}</div><div class="dkt">'
                f'<span class="ser" style="background:{bg}">{c["badge"]}</span><h1>{c["title"]}</h1>{lede}</div></div>')
        body = f'<div class="body">{keys_html(c["keys"])}{tail(c)}</div>'
    elif L == 'histoire':
        hero = (f'<div class="hero" style="height:{c.get("hh", 520)}px"><div class="wm">{c.get("wm", "")}</div><div class="hs">'
                f'<div class="cty">{c["country"]}</div><div class="nm">{c["name"]}</div><div class="dt">{c["dates"]}</div>'
                f'<div class="qt"><div class="x">« {c["quote"]} »</div><div class="s">{c["qsrc"]}</div></div></div></div>')
        top = c.get('hh', 520) + 36
        body = (f'<div class="body hb" style="top:{top}px"><div><span class="ser">ILS ONT MARQUÉ L\'HISTOIRE</span>'
                f'<span class="ser sm">{c["country"]}</span></div><h1>{c["tagline"]}</h1>{keys_html(c["keys"], False)}{tail(c)}</div>')
    elif L == 'chiffre':
        hero = (f'<div class="hero" style="height:{c.get("hh", 560)}px"><div class="cf"><span class="ser r" style="background:#C3232B">LE CHIFFRE</span>'
                f'<div class="tg">{c["tag"]}</div><div class="num">{c["num"]}</div><div class="un">{c["unit"]}</div></div></div>')
        ctx = '<div class="ctx">' + ''.join(f'<div class="cx"><span class="d">▸</span><span>{t}</span></div>' for t in c['ctx']) + '</div>'
        body = f'<div class="body" style="top:{c.get("hh", 560) + 40}px">{ctx}{tail(c)}</div>'
    else:
        raise SystemExit('unknown layout ' + L)
    h = (f'<!doctype html><html><head><meta charset="utf-8"><base href="file://{HERE}/"><style>{CSS}{c.get("css", "")}</style></head>'
         f'<body>{hero}{body}<div class="src">{c["src"]}</div>{LOGO}{FIT}</body></html>')
    # keep number ranges / units together
    h = re.sub(r'(\d) (%|°C|km|m\b|h\b|min\b|ans\b|j\b)', '\\1\u00a0\\2', h)
    h = h.replace('Port-au-Prince', 'Port\u2011au\u2011Prince')
    return h


def main():
    cards = json.load(open(sys.argv[1]))
    out = os.path.abspath(sys.argv[2]); os.makedirs(out, exist_ok=True)
    only = [a for a in sys.argv[3:] if not a.startswith('--')]
    for c in cards:
        if only and c['id'] not in only:
            continue
        f = os.path.join(out, f'lr-{c["id"]}.html')
        open(f, 'w').write(card(c))
        if '--render' in sys.argv:
            subprocess.run(['node', os.path.join(HERE, 'render.js'), f, f[:-5] + '.jpg'], check=True, cwd=HERE)
        print(c['id'])


if __name__ == '__main__':
    main()

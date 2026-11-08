# Goals & Buckets card generator (1080x1350).
# Usage from a cards script:  import gb; gb.build({'gb-xxx': gb.page(...)}, out_dir)
import os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, 'build')          # HTML is written here (paths ../gb-base.css etc. resolve)
RENDER = os.path.join(HERE, '..', 'lr-card', 'render.js')

LOGO = ('<div class="nb"><img src="../lr-mark-blanc.png" alt=""><div class="w"><div class="t">LE RAPPORTEUR</div>'
        '<div class="r"></div><div class="u">lerapporteur.net</div></div></div>')


def page(tag, body, deco='', css=''):
    """tag: top-left label (e.g. 'NBA · Histoire'); body: HTML inside .mid;
    deco: optional '<div class="yr">1995</div>' or '<div class="qm">?</div>'; css: per-card overrides."""
    return ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../gb-base.css">'
            '<style>' + css + '</style></head><body><div class="c">' + deco +
            '<div class="top"><div class="tag"><span class="b"></span>' + tag + '</div>'
            '<div class="mag"><span><small>Magazine</small>Goals &amp; Buckets</span><img src="../gb-logo.png" alt=""></div></div>'
            '<div class="mid">\n' + body + '\n</div>' + LOGO + '</div></body></html>')


def clues(rows):
    return '<div class="clues">' + ''.join(f'<div class="cl"><b>{b}</b><span>{s}</span></div>' for b, s in rows) + '</div>'


def ops(*opts):
    return '<div class="ops">' + ''.join(f'<div class="op"><b>{"ABC"[i]}</b>{o}</div>' for i, o in enumerate(opts)) + '</div>'


def top5(rows, unit):
    return '<div class="top5">' + ''.join(
        f'<div class="r5{" one" if i == 0 else ""}"><div class="rk">{i+1}</div><div class="nm"><b>{n}</b><span>{s}</span></div>'
        f'<div class="g">{g}<small>{unit}</small></div></div>' for i, (n, s, g) in enumerate(rows)) + '</div>'


def duel(left, right, rows):
    r = ''.join(f'<tr><td>{a}</td><td class="l">{l}</td><td>{b}</td></tr>' for a, l, b in rows)
    return f'<table class="du"><tr><th>{left}</th><th></th><th>{right}</th></tr>{r}</table>'


def nobreak(html):
    # keep scores like 2–1 together, and non-breaking space before French ? ! : ;
    html = re.sub(r'(\d)–(\d)', '\\1\u2060–\u2060\\2', html)
    return re.sub(r' ([?!:;])', '\u00a0\\1', html)


def build(cards, out_dir, render=True):
    os.makedirs(BUILD, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)
    for name, html in cards.items():
        p = os.path.join(BUILD, name + '.html')
        open(p, 'w').write(nobreak(html))
        if render:
            subprocess.run(['node', RENDER, p, os.path.join(out_dir, name + '.jpg')], check=True,
                           cwd=os.path.join(HERE, '..', 'lr-card'))
        print(name)

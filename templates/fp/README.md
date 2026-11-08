# Full Pocket templates (cards + Reels)

Rebuilt 8 Nov 2026 after the old local generators were lost. Everything needed is in this folder.

| File | What |
|---|---|
| `fp.js` | HTML templates: `card()` 1080x1350 (`kind: 'tip'` dark green, `'qst'` mint) and `reel()` 1080x1920, 18 s, EN/ES |
| `render.js` | Playwright renderer: card → JPG; Reel → frames at 30 fps piped to ffmpeg (libx264 yuv420p crf 20, aac 160k, loudnorm I=-14 TP=-1.5 LRA=11, audio fade in/out). Warns on overflow. |
| `build.js` | `node build.js weeks/<week>.js [--only cards\|reels] [--id ID] [--par 3] [--out DIR]` → `media/<date>/<id>.jpg`, `<id>.mp4` (EN), `<id>-es.mp4` (ES) |
| `weeks/*.js` | Content for each week (texts, captions, music offsets) |
| `ph-100a.jpg`, `ph-100b.jpg` | $100 bill photos (Unsplash), watermark for tip / question cards |
| `fonts/` | Lora (variable), Poppins 500–800 — SIL OFL 1.1, licences included |

Brand: green `#0D4F3C`, gold `#F2B63C`, mint `#E6F2EC`; green pocket logo with gold coin (SVG in `fp.js`).
Footer: "MONEY MADE SIMPLE 💸" (EN) / "FINANZAS SIN COMPLICACIONES 💸" (ES). Music: `music/fp-chill-1.mp3` (163 s; use a new `offset` per Reel).

Reel timeline: emoji intro 0–2.7 s → title 2.8 s → steps (3 or 4) → question + A/B/C + "🔔 Follow Full Pocket" from 14.2 s.

## Setup
```
npm i playwright@1          # do NOT run `playwright install`; render.js uses /opt/pw-browsers/chromium-*/chrome-linux64/chrome (or $CHROME)
```
Emoji come from the system font Noto Color Emoji. Title tips: use `&nbsp;` to keep word groups together (`text-wrap: balance` is on).
Check every output: `ffmpeg -ss 13 -i x.mp4 -frames:v 1 still.png`.

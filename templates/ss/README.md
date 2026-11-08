# Stars & Style templates (Instagram Reels)

Rebuilt 8 Nov 2026 to match the published `media/ss/ss-reel-*.mp4` style.

| File | What |
|---|---|
| `ss.js` | `reel()` 1080x1920, 18 s: big gold intro word → kicker + Bodoni title + numbered steps (3 or 4) → question with A/B/C boxes + "✦ Follow @thestarsandstyle" |
| `render.js` | Same Playwright + ffmpeg renderer as `templates/fp/render.js` |
| `build.js` | `node build.js weeks/<week>.js [--id ID] [--par 2]` → `media/ss/<id>.mp4`; flags hyphens in Bodoni text |
| `weeks/*.js` | Reel content + Instagram captions + music offsets |
| `fonts/` | Bodoni Moda (variable wght+opsz, roman+italic), IBM Plex Sans Condensed SemiBold/Bold — SIL OFL 1.1 |
| `ss-galliano.html` | Older S&S feed card (1080x1350) style for reference |

Brand: black `#14110C`, gold `#D4A937`, cream `#EFE2BF`; "S✦S" top right, "STARS & STYLE" top left, footer "STYLE · STARS · STORIES".
Rules: **no hyphens in titles** (Bodoni Moda breaks them badly); step numbers are Bodoni 800 at opsz 28 (heavier).
Music: `music/ss-runway-1.mp3` (193 s) — use a new `offset` for each Reel. Used so far (Nov 2026): 38, 92, 146.
Setup: see `templates/fp/README.md` (`npm i playwright@1`, no `playwright install`).

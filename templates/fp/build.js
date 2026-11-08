// Build Full Pocket media for one week.
//   node build.js weeks/2026-11-08.js [--out ../../media] [--only cards|reels] [--id fp-reel-x] [--par 2]
// Output: <out>/<date>/<id>.jpg, <id>.mp4 (English) and <id>-es.mp4 (Spanish).
const fs = require('fs'), path = require('path'), os = require('os');
const T = require('./fp'), R = require('./render');
const a = process.argv.slice(2), opt = k => { const i = a.indexOf(k); return i >= 0 ? a[i + 1] : null; };
const week = require(path.resolve(a[0]));
const out = path.resolve(opt('--out') || path.join(__dirname, '../../media'));
const only = opt('--only'), id = opt('--id'), par = +(opt('--par') || 2);
const MUSIC = path.join(__dirname, '../../music/fp-chill-1.mp3');
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'fp-'));

(async () => {
  const jobs = [];
  if (only !== 'reels') for (const c of week.cards) if (!id || id === c.id) jobs.push({ kind: 'card', c });
  if (only !== 'cards') for (const r of week.reels) for (const L of ['en', 'es']) if (!id || id === r.id) jobs.push({ kind: 'reel', r, L });
  const browser = await R.launch();
  const problems = [];
  let k = 0;
  async function worker() {
    while (k < jobs.length) {
      const j = jobs[k++];
      const it = j.c || j.r;
      fs.mkdirSync(path.join(out, it.date), { recursive: true });
      if (j.kind === 'card') {
        const html = path.join(tmp, it.id + '.html'); fs.writeFileSync(html, T.card(it));
        const f = path.join(out, it.date, it.id + '.jpg');
        const bad = await R.card(browser, html, f);
        bad.forEach(b => problems.push(it.id + ' ' + b)); console.log('card', f);
      } else {
        const name = it.id + (j.L === 'es' ? '-es' : '');
        const html = path.join(tmp, name + '.html'); fs.writeFileSync(html, T.reel(it, j.L));
        const f = path.join(out, it.date, name + '.mp4');
        const bad = await R.reel(browser, html, f, { music: MUSIC, offset: it.offset });
        bad.forEach(b => problems.push(name + ' ' + b)); console.log('reel', f);
      }
    }
  }
  await Promise.all(Array.from({ length: par }, worker));
  await browser.close();
  console.log(problems.length ? 'OVERFLOW:\n' + problems.join('\n') : 'no overflow');
})().catch(e => { console.error(e); process.exit(1); });

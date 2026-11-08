// Build Stars & Style Reels for one week.
//   node build.js weeks/2026-11-09.js [--out ../../media/ss] [--id ss-reel-x] [--par 2]
// Output: <out>/<id>.mp4  (music: ../../music/ss-runway-1.mp3, offset per reel)
const fs = require('fs'), path = require('path'), os = require('os');
const T = require('./ss'), R = require('./render');
const a = process.argv.slice(2), opt = k => { const i = a.indexOf(k); return i >= 0 ? a[i + 1] : null; };
const week = require(path.resolve(a[0]));
const out = path.resolve(opt('--out') || path.join(__dirname, '../../media/ss'));
const id = opt('--id'), par = +(opt('--par') || 2);
const MUSIC = path.join(__dirname, '../../music/ss-runway-1.mp3');
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'ss-'));
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const jobs = week.reels.filter(r => !id || r.id === id);
  const browser = await R.launch();
  const problems = []; let k = 0;
  async function worker() {
    while (k < jobs.length) {
      const r = jobs[k++];
      const html = path.join(tmp, r.id + '.html'); fs.writeFileSync(html, T.reel(r));
      if (/-/.test((r.title + r.q + r.big).replace(/<[^>]+>/g, ''))) problems.push(r.id + ' hyphen in Bodoni title');
      const f = path.join(out, r.id + '.mp4');
      (await R.reel(browser, html, f, { music: MUSIC, offset: r.offset })).forEach(b => problems.push(r.id + ' ' + b));
      console.log('reel', f);
    }
  }
  await Promise.all(Array.from({ length: par }, worker));
  await browser.close();
  console.log(problems.length ? 'PROBLEMS:\n' + problems.join('\n') : 'no overflow');
})().catch(e => { console.error(e); process.exit(1); });

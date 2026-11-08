// node check.js build/*.html  -> reports overflow of .mid and line counts of title (.dv), options, rows
const { chromium } = require('../lr-card/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + require('path').resolve(f)); await p.evaluate(() => document.fonts.ready);
    const r = await p.evaluate(() => {
      const mid = document.querySelector('.mid'), kids = [...mid.children];
      const top = kids[0].getBoundingClientRect().top, bot = kids[kids.length - 1].getBoundingClientRect().bottom;
      const tagR = document.querySelector('.tag').getBoundingClientRect().bottom, nbT = document.querySelector('.nb').getBoundingClientRect().top;
      const lines = el => { const cs = getComputedStyle(el); return Math.round(el.getBoundingClientRect().height / parseFloat(cs.lineHeight)); };
      const dv = document.querySelector('.dv');
      const wide = [...document.querySelectorAll('.cl span,.op,.note2,.q2,.fol,.sub,.r5 .nm b')].filter(e => e.scrollWidth > e.clientWidth + 1).length;
      return { content: Math.round(bot - top), gapTop: Math.round(top - tagR), gapBot: Math.round(nbT - bot),
               dvLines: dv ? lines(dv) : 0, q2Lines: lines(document.querySelector('.q2')), folLines: lines(document.querySelector('.fol')),
               opLines: [...document.querySelectorAll('.op')].map(o => Math.round((o.getBoundingClientRect().height - 30) / 36)), wide };
    });
    console.log(require('path').basename(f), JSON.stringify(r));
  }
  await b.close();
})();

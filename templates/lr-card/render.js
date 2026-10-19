// node render.js <abs/path/file.html> <out.jpg>   (1080x1350)
const { chromium } = require('playwright');
(async()=>{const [src,out]=process.argv.slice(2);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+src);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:out,type:'jpeg',quality:92});await b.close();})();

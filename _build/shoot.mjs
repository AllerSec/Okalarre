import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const targets = process.argv.slice(2);
const pages = targets.length ? targets : ["index.html"];

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });

async function autoscroll(page){
  await page.evaluate(async () => {
    await new Promise((res) => {
      let y = 0; const step = 400;
      const t = setInterval(() => {
        window.scrollBy(0, step); y += step;
        if (y >= document.body.scrollHeight) { clearInterval(t); res(); }
      }, 80);
    });
    window.scrollTo(0,0);
  });
  await new Promise(r=>setTimeout(r,800));
}

for (const p of pages){
  const slug = p.replace(/[\/\.]/g,"_");
  for (const [w,h,tag] of [[1440,900,"desktop"],[390,844,"mobile"]]){
    const page = await browser.newPage();
    await page.setViewport({ width:w, height:h, deviceScaleFactor:1 });
    await page.goto(`${BASE}/${p}`, { waitUntil:"networkidle2", timeout:30000 });
    await autoscroll(page);
    await page.screenshot({ path: path.join(OUT, `${slug}_${tag}.png`), fullPage:true });
    console.log("shot", slug, tag);
    await page.close();
  }
}
await browser.close();
console.log("DONE");

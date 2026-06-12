import puppeteer from "puppeteer-core";
import os from "os"; import path from "path";
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args:["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width:1440, height:820 });
await page.goto("http://127.0.0.1:8000/index.html", { waitUntil:"networkidle2" });
for (let i=0;i<4;i++){
  await new Promise(r=>setTimeout(r, i===0?500:6200));
  // report active slide index
  const idx = await page.evaluate(()=>Array.from(document.querySelectorAll('.hero__slide')).findIndex(s=>s.classList.contains('is-active')));
  await page.screenshot({ path: path.join(OUT, `slide_${i}_idx${idx}.png`) });
  console.log("frame",i,"active",idx);
}
await browser.close(); console.log("DONE");

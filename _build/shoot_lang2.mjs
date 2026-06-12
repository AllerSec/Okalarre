import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900 });
await page.goto(`${BASE}/okalarre.html`, { waitUntil: "networkidle2", timeout: 30000 });
// scroll down in small steps (real-user-like), then up to trigger the solid nav reveal
await page.evaluate(async () => {
  for (let i = 0; i < 5; i++) { window.scrollBy(0, 350); await new Promise(r => setTimeout(r, 150)); }
  await new Promise(r => setTimeout(r, 400));
  for (let i = 0; i < 2; i++) { window.scrollBy(0, -150); await new Promise(r => setTimeout(r, 150)); }
});
await new Promise((r) => setTimeout(r, 1000));
await page.screenshot({ path: path.join(OUT, "lang_solid2.png") });
await browser.close();
console.log("DONE");

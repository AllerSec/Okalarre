import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
await page.goto(`${BASE}/index.html`, { waitUntil: "networkidle2", timeout: 30000 });

const sections = [".marquee", ".panels", ".bento", ".photo-marquee", ".cta-banner", ".editorial-wrap"];
for (const sel of sections) {
  await page.evaluate((s) => document.querySelector(s)?.scrollIntoView({ block: "center" }), sel);
  await new Promise((r) => setTimeout(r, 2200));
  await page.screenshot({ path: path.join(OUT, `check_${sel.replace(/[^a-z-]/g, "")}.png`) });
  console.log("shot", sel);
}
await browser.close();
console.log("DONE");

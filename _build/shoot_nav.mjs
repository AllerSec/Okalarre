import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900 });
await page.goto(`${BASE}/index.html`, { waitUntil: "networkidle2", timeout: 30000 });

// scroll down past the fold in steps -> nav should hide
await page.evaluate(async () => {
  for (let i = 0; i < 6; i++) { window.scrollBy(0, 400); await new Promise(r => setTimeout(r, 120)); }
});
await new Promise((r) => setTimeout(r, 900));
const hiddenDown = await page.evaluate(() => document.querySelector(".nav").classList.contains("nav--hidden"));
await page.screenshot({ path: path.join(OUT, "nav_down.png") });

// scroll up a bit -> nav should reappear
await page.evaluate(() => window.scrollBy(0, -300));
await new Promise((r) => setTimeout(r, 900));
const hiddenUp = await page.evaluate(() => document.querySelector(".nav").classList.contains("nav--hidden"));
await page.screenshot({ path: path.join(OUT, "nav_up.png") });
console.log("hidden after down:", hiddenDown, "| hidden after up:", hiddenUp);

// mobile home + bodas
const m = await browser.newPage();
await m.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
await m.goto(`${BASE}/bodas.html`, { waitUntil: "networkidle2", timeout: 30000 });
await m.evaluate(() => document.querySelector(".cta-banner")?.scrollIntoView({ block: "center" }));
await new Promise((r) => setTimeout(r, 2000));
await m.screenshot({ path: path.join(OUT, "mobile_bodas_cta.png") });
await m.goto(`${BASE}/index.html`, { waitUntil: "networkidle2", timeout: 30000 });
await m.evaluate(() => document.querySelector(".panels")?.scrollIntoView({ block: "start" }));
await new Promise((r) => setTimeout(r, 2000));
await m.screenshot({ path: path.join(OUT, "mobile_home_panels.png") });

await browser.close();
console.log("DONE");

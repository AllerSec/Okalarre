import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 600, deviceScaleFactor: 1.5 });
await page.goto(`${BASE}/index.html`, { waitUntil: "networkidle2", timeout: 30000 });
await new Promise((r) => setTimeout(r, 1800));
await page.screenshot({ path: path.join(OUT, "lang_hero.png"), clip: { x: 0, y: 0, width: 1920, height: 140 } });

await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight / 2));
await new Promise((r) => setTimeout(r, 600));
await page.evaluate(() => window.scrollBy(0, -200));
await new Promise((r) => setTimeout(r, 900));
await page.screenshot({ path: path.join(OUT, "lang_solid.png"), clip: { x: 0, y: 0, width: 1920, height: 140 } });
await browser.close();
console.log("DONE");

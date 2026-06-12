import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

// usage: node shoot_sections.mjs page.html [mobile]
const target = process.argv[2] || "index.html";
const mobile = process.argv[3] === "mobile";
const [w, h] = mobile ? [390, 844] : [1440, 900];

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: w, height: h, deviceScaleFactor: 1 });
await page.goto(`${BASE}/${target}`, { waitUntil: "networkidle2", timeout: 30000 });
await new Promise(r => setTimeout(r, 2500)); // let loader + reveal settle

const total = await page.evaluate(() => document.body.scrollHeight);
const slug = target.replace(/[\/\.]/g, "_") + (mobile ? "_m" : "_d");
let i = 0;
for (let y = 0; y < total; y += h) {
  await page.evaluate((yy) => window.scrollTo(0, yy), y);
  await new Promise(r => setTimeout(r, 1200));
  await page.screenshot({ path: path.join(OUT, `${slug}_sec${String(i).padStart(2,"0")}.png`) });
  i++;
}
console.log("DONE", i, "sections");
await browser.close();

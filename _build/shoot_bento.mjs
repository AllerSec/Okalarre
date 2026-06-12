import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 1000, deviceScaleFactor: 1.5 });
await page.goto(`${BASE}/index.html`, { waitUntil: "networkidle2", timeout: 30000 });
await page.evaluate(() => document.querySelector(".bento")?.scrollIntoView({ block: "center" }));
await new Promise((r) => setTimeout(r, 2500));
const el = await page.$(".bento");
await el.screenshot({ path: path.join(OUT, "check_bento_hi.png") });
await browser.close();
console.log("DONE");

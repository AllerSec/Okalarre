import puppeteer from "puppeteer-core";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const BASE = "http://127.0.0.1:8000";

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox","--hide-scrollbars"] });

async function shot(url, sel, name, scroll) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.goto(`${BASE}/${url}`, { waitUntil: "networkidle2", timeout: 30000 });
  if (sel) await page.evaluate((s) => document.querySelector(s)?.scrollIntoView({ block: "center" }), sel);
  if (scroll === "up") await page.evaluate(() => window.scrollBy(0, -200)); // trigger nav reveal
  await new Promise((r) => setTimeout(r, 2200));
  await page.screenshot({ path: path.join(OUT, `${name}.png`) });
  console.log("shot", name);
  await page.close();
}

await shot("bodas.html", null, "polish_bodas_hero");
await shot("bodas.html", ".cta-banner", "polish_bodas_cta");
await shot("contacto.html", ".form", "polish_contacto_form");
await shot("fr/mariages.html", ".cta-banner", "polish_fr_cta");
await browser.close();
console.log("DONE");

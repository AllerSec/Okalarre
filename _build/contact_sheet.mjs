/* Contact sheet of all site photos with filename labels, for visual curation.
   Run: node _build/contact_sheet.mjs (needs http.server on 8000) */
import puppeteer from "puppeteer-core";
import fs from "fs";
import os from "os";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT = path.join(os.tmpdir(), "okalarre_shots");
const ROOT = path.resolve(import.meta.dirname, "..");

const names = [];
for (const folder of ["venue", "gallery"]) {
  for (const f of fs.readdirSync(path.join(ROOT, "assets", "img", folder))) {
    if (f.endsWith(".webp")) names.push(`${folder}/${f.replace(".webp", "")}`);
  }
}

const cell = (n) => `<figure><img src="http://127.0.0.1:8000/assets/img/${n}.webp"><figcaption>${n.split("/")[1]}</figcaption></figure>`;
const html = (chunk) => `<!doctype html><html><head><style>
body{margin:0;background:#111;font-family:monospace}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;padding:6px}
figure{margin:0}img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}
figcaption{color:#0f0;font-size:20px;text-align:center;padding:2px 0}
</style></head><body><div class="grid">${chunk.map(cell).join("")}</div></body></html>`;

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox"] });
const pg = await browser.newPage();
const PER = 16;
for (let i = 0; i < names.length; i += PER) {
  const chunk = names.slice(i, i + PER);
  const rows = Math.ceil(chunk.length / 4);
  await pg.setViewport({ width: 1600, height: rows * 290 + 20, deviceScaleFactor: 1 });
  await pg.setContent(html(chunk), { waitUntil: "load", timeout: 60000 });
  await pg.evaluate(() => Promise.all([...document.images].map((im) => im.decode().catch(() => {}))));
  await new Promise((r) => setTimeout(r, 400));
  await pg.screenshot({ path: path.join(OUT, `sheet_${i / PER}.png`) });
  console.log("sheet", i / PER, chunk.length, "imgs");
}
await browser.close();

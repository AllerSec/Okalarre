/* Recreate the original fincaokalarre.com favicon (charcoal #48484A circle,
   white serif "O") crisply at all modern sizes. Run: node _build/favicon.mjs */
import puppeteer from "puppeteer-core";
import fs from "fs";
import path from "path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const ROOT = path.resolve(import.meta.dirname, "..");
const BRAND = path.join(ROOT, "assets", "img", "brand");
// served by `python -m http.server 8000` from project root
const FONT = "http://127.0.0.1:8000/assets/fonts/playfair-display-600-latin.woff2";

// circle on transparent for tab icons; full square for touch/manifest icons
const page_html = (size, square) => `<!doctype html><html><head><style>
@font-face { font-family:"PD"; src: url("${FONT}") format("woff2"); }
html,body { margin:0; background:transparent; }
.wrap { width:${size}px; height:${size}px; display:grid; place-items:center;
  ${square ? "background:#48484A;" : ""} }
.circle { width:${square ? size * 0.86 : size}px; height:${square ? size * 0.86 : size}px;
  border-radius:50%; background:#48484A; display:grid; place-items:center; }
.o { font-family:"PD",serif; font-weight:600; color:#fff;
  font-size:${Math.round(size * (square ? 0.56 : 0.66))}px; line-height:1;
  transform: translateY(-${Math.round(size * 0.02)}px); }
</style></head><body><div class="wrap">${square
    ? `<div class="o">O</div>`
    : `<div class="circle"><div class="o">O</div></div>`}</div></body></html>`;

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox", "--allow-file-access-from-files"] });
const pg = await browser.newPage();

async function shoot(size, square, file) {
  await pg.setViewport({ width: size, height: size, deviceScaleFactor: 1 });
  await pg.setContent(page_html(size, square), { waitUntil: "load" });
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: file, omitBackground: !square });
  console.log("made", path.basename(file), `${size}px`);
}

for (const s of [16, 32, 48]) await shoot(s, false, path.join(BRAND, `favicon-${s}.png`));
for (const s of [180, 192, 512]) await shoot(s, true, path.join(BRAND, `favicon-${s}.png`));
await browser.close();

// build favicon.ico with PNG-encoded entries (16+32+48)
const entries = [16, 32, 48].map((s) => ({ s, data: fs.readFileSync(path.join(BRAND, `favicon-${s}.png`)) }));
const header = Buffer.alloc(6);
header.writeUInt16LE(0, 0); header.writeUInt16LE(1, 2); header.writeUInt16LE(entries.length, 4);
let offset = 6 + entries.length * 16;
const dirs = [], blobs = [];
for (const { s, data } of entries) {
  const d = Buffer.alloc(16);
  d.writeUInt8(s === 256 ? 0 : s, 0); d.writeUInt8(s === 256 ? 0 : s, 1);
  d.writeUInt8(0, 2); d.writeUInt8(0, 3);
  d.writeUInt16LE(1, 4); d.writeUInt16LE(32, 6);
  d.writeUInt32LE(data.length, 8); d.writeUInt32LE(offset, 12);
  offset += data.length;
  dirs.push(d); blobs.push(data);
}
fs.writeFileSync(path.join(ROOT, "favicon.ico"), Buffer.concat([header, ...dirs, ...blobs]));
console.log("made favicon.ico");

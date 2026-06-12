import puppeteer from "puppeteer-core";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const BASE = "http://127.0.0.1:8000";
const PAGES = [
  "index.html", "bodas.html", "contacto.html", "galeria.html", "espacios.html",
  "preguntas-frecuentes.html", "en/index.html", "eu/index.html", "fr/index.html",
  "fr/mariages.html", "eu/ezkontzak.html", "en/weddings.html", "404.html",
];

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox"] });
let issues = 0;
for (const p of PAGES) {
  const page = await browser.newPage();
  const errs = [];
  page.on("console", (m) => { if (m.type() === "error" || m.type() === "warning") errs.push(m.type() + ": " + m.text()); });
  page.on("pageerror", (e) => errs.push("pageerror: " + e.message));
  page.on("requestfailed", (r) => errs.push("reqfail: " + r.url()));
  await page.goto(`${BASE}/${p}`, { waitUntil: "networkidle2", timeout: 30000 });
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight / 2));
  await new Promise((r) => setTimeout(r, 1200));
  if (errs.length) { issues += errs.length; console.log("==", p); errs.forEach((e) => console.log("  ", e)); }
  else console.log("OK", p);
  await page.close();
}
await browser.close();
console.log(issues ? `ISSUES: ${issues}` : "ALL CLEAN");

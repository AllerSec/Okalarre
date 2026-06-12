import puppeteer from "puppeteer-core";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const BASE = "http://127.0.0.1:8000";
const PAGES = ["index.html", "gastronomia.html", "bodas.html", "en/gastronomy.html"];

const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--no-sandbox"] });
let bad = 0;

for (const p of PAGES) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1366, height: 850 });
  await page.goto(`${BASE}/${p}`, { waitUntil: "domcontentloaded", timeout: 30000 });
  // right after DCL: anything inside the first viewport must already be visible
  await new Promise((r) => setTimeout(r, 150));
  const hiddenAbove = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll(".reveal, .hero__sub, .hero__cta").forEach((el) => {
      const r = el.getBoundingClientRect();
      const inView = r.top < innerHeight * 0.86 && r.bottom > 0;
      const cs = getComputedStyle(el);
      // CSS-animated hero bits may still be mid-entrance: opacity rising is fine, 0 after 150ms+delay means stuck
      if (inView && parseFloat(cs.opacity) < 0.01 && !el.getAnimations().length) out.push(el.className);
    });
    return out;
  });
  // below-fold reveals must be hidden (armed to animate), then appear after scroll
  const armedBelow = await page.evaluate(() => {
    let armed = 0;
    document.querySelectorAll(".reveal").forEach((el) => {
      if (el.getBoundingClientRect().top >= innerHeight * 0.86 && parseFloat(getComputedStyle(el).opacity) < 0.01) armed++;
    });
    return armed;
  });
  await page.evaluate(() => window.scrollTo({ top: document.body.scrollHeight, behavior: "instant" }));
  await new Promise((r) => setTimeout(r, 1600));
  const stuckAfterScroll = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll(".reveal").forEach((el) => {
      if (parseFloat(getComputedStyle(el).opacity) < 0.05) out.push(el.className + " :: " + el.textContent.slice(0, 40));
    });
    return out;
  });
  const ok = !hiddenAbove.length && !stuckAfterScroll.length;
  if (!ok) bad++;
  console.log((ok ? "OK " : "BAD") , p, `| armed below-fold: ${armedBelow}`,
    hiddenAbove.length ? `| hidden above-fold: ${JSON.stringify(hiddenAbove)}` : "",
    stuckAfterScroll.length ? `| stuck after scroll: ${JSON.stringify(stuckAfterScroll)}` : "");
  await page.close();
}
await browser.close();
console.log(bad ? "FAIL" : "ALL CLEAN");

/* ==========================================================================
   FINCA OKALARRE — main.js
   GSAP animations, page loader (first visit), lang detect, lightbox, nav, FAQ
   ========================================================================== */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const onReady = (fn) => (document.readyState !== "loading" ? fn() : document.addEventListener("DOMContentLoaded", fn));

  /* -------------------------------------------------- LANGUAGE AUTO-DETECT
     Runs ASAP. Only redirects on the canonical Spanish root, only on first
     ever visit, never forces Euskara as a default. */
  (function langDetect() {
    try {
      const saved = localStorage.getItem("okalarre_lang");
      if (saved) return; // respect explicit choice
      const path = location.pathname;
      // only auto-redirect from the ES root index (default site language)
      const atRoot = /\/(index\.html)?$/.test(path) && !/\/(eu|fr)\//.test(path);
      if (!atRoot) return;
      if (sessionStorage.getItem("okalarre_redirected")) return;
      sessionStorage.setItem("okalarre_redirected", "1");

      const langs = (navigator.languages || [navigator.language || "es"]).map((l) => l.toLowerCase());
      let target = "es"; // default site language
      for (const l of langs) {
        if (l.startsWith("es")) { target = "es"; break; }
        if (l.startsWith("fr")) { target = "fr"; break; }
        if (l.startsWith("en")) { target = "en"; break; }
        if (l.startsWith("eu")) { target = "es"; break; } // never auto-Euskara → fall back to ES
        // any other language → English (international default)
        target = "en"; break;
      }
      if (target === "fr" || target === "en") {
        const base = location.pathname.replace(/index\.html$/, "");
        location.replace(base + target + "/");
      }
    } catch (e) { /* no-op */ }
  })();

  /* -------------------------------------------------- PAGE LOADER (first visit only) */
  onReady(function () {
    const loader = document.getElementById("loader");
    if (!loader) return;
    const seen = sessionStorage.getItem("okalarre_loaded");
    if (seen) {
      loader.remove();
      return;
    }
    sessionStorage.setItem("okalarre_loaded", "1");
    const done = () => { loader.classList.add("hide"); setTimeout(() => loader.remove(), 750); };
    // hide after assets settle (cap so it never blocks)
    window.addEventListener("load", () => setTimeout(done, prefersReduced ? 200 : 900));
    setTimeout(done, 3500); // safety
  });

  /* -------------------------------------------------- NAV: scroll state + hide/reveal + mobile */
  onReady(function () {
    const nav = document.querySelector(".nav");
    const burger = document.querySelector(".nav__burger");
    const hasHero = document.querySelector(".hero, .err-page");
    let lastY = window.scrollY;

    const onScroll = () => {
      if (!nav) return;
      const y = window.scrollY;
      const solid = y > (hasHero ? window.innerHeight * 0.6 : 20);
      nav.classList.toggle("nav--solid", solid || !hasHero);
      // hide when scrolling down past the fold, reveal on any scroll up
      const goingDown = y > lastY + 4;
      const goingUp = y < lastY - 4;
      if (goingDown && y > window.innerHeight && !document.body.classList.contains("menu-open")) {
        nav.classList.add("nav--hidden");
      } else if (goingUp || y <= window.innerHeight) {
        nav.classList.remove("nav--hidden");
      }
      lastY = y;
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    if (burger) {
      burger.addEventListener("click", () => {
        const open = document.body.classList.toggle("menu-open");
        burger.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.style.overflow = open ? "hidden" : "";
      });
      document.querySelectorAll(".mobile-menu a").forEach((a) =>
        a.addEventListener("click", () => {
          document.body.classList.remove("menu-open");
          document.body.style.overflow = "";
          burger.setAttribute("aria-expanded", "false");
        })
      );
    }
  });

  /* -------------------------------------------------- HERO SLIDER (home) */
  onReady(function () {
    const slider = document.querySelector(".hero__slider");
    if (!slider) return;
    const slides = Array.from(slider.querySelectorAll(".hero__slide"));
    if (slides.length < 2) return;
    const dots = Array.from(document.querySelectorAll(".hero__dot"));
    let idx = 0, timer = null;
    const DELAY = 6000;

    const go = (n) => {
      slides[idx].classList.remove("is-active");
      if (dots[idx]) dots[idx].classList.remove("is-active");
      idx = (n + slides.length) % slides.length;
      // restart ken-burns by forcing reflow on the active img
      const img = slides[idx].querySelector("img");
      if (img) { img.style.animation = "none"; void img.offsetWidth; img.style.animation = ""; }
      slides[idx].classList.add("is-active");
      if (dots[idx]) {
        // restart dot progress
        const d = dots[idx]; d.classList.remove("is-active"); void d.offsetWidth; d.classList.add("is-active");
      }
    };
    const next = () => go(idx + 1);
    const start = () => { stop(); timer = setInterval(next, DELAY); };
    const stop = () => { if (timer) clearInterval(timer); };

    dots.forEach((dot, i) => dot.addEventListener("click", () => { go(i); start(); }));
    // pause when tab hidden
    document.addEventListener("visibilitychange", () => (document.hidden ? stop() : start()));
    slides[0].classList.add("is-active");
    if (dots[0]) dots[0].classList.add("is-active");
    start();
  });

  /* -------------------------------------------------- FAQ accordion */
  onReady(function () {
    document.querySelectorAll(".faq__q").forEach((q) => {
      q.addEventListener("click", () => {
        const item = q.closest(".faq__item");
        const a = item.querySelector(".faq__a");
        const open = item.classList.toggle("open");
        q.setAttribute("aria-expanded", open ? "true" : "false");
        a.style.maxHeight = open ? a.scrollHeight + "px" : "0";
      });
    });
  });

  /* -------------------------------------------------- LIGHTBOX */
  onReady(function () {
    const items = Array.from(document.querySelectorAll("[data-lightbox]"));
    if (!items.length) return;
    const box = document.getElementById("lightbox");
    if (!box) return;
    const imgEl = box.querySelector("img");
    let idx = 0;
    const srcs = items.map((el) => el.getAttribute("data-lightbox"));

    const show = (i) => {
      idx = (i + srcs.length) % srcs.length;
      imgEl.src = srcs[idx];
      const thumb = items[idx].querySelector("img");
      imgEl.alt = thumb ? thumb.alt : "";
      box.classList.add("open");
      document.body.style.overflow = "hidden";
    };
    const close = () => { box.classList.remove("open"); document.body.style.overflow = ""; };

    items.forEach((el, i) => el.addEventListener("click", (e) => { e.preventDefault(); show(i); }));
    box.querySelector(".lightbox__close").addEventListener("click", close);
    box.querySelector(".lightbox__nav.prev").addEventListener("click", () => show(idx - 1));
    box.querySelector(".lightbox__nav.next").addEventListener("click", () => show(idx + 1));
    box.addEventListener("click", (e) => { if (e.target === box) close(); });
    document.addEventListener("keydown", (e) => {
      if (!box.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") show(idx + 1);
      if (e.key === "ArrowLeft") show(idx - 1);
    });
  });

  /* -------------------------------------------------- CONTACT FORM (Formspree-ready) */
  onReady(function () {
    const form = document.getElementById("contact-form");
    if (!form) return;
    const status = form.querySelector(".form__status");
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const btn = form.querySelector("button[type=submit]");
      const original = btn.textContent;
      btn.disabled = true; btn.textContent = btn.dataset.sending || "Enviando…";
      try {
        const res = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" },
        });
        if (res.ok) {
          status.className = "form__status ok";
          status.textContent = form.dataset.ok || "¡Gracias! Te responderemos muy pronto.";
          form.reset();
        } else throw new Error("bad response");
      } catch (err) {
        status.className = "form__status err";
        status.textContent = form.dataset.err || "No se pudo enviar. Escríbenos a info@fincaokalarre.com";
      } finally {
        btn.disabled = false; btn.textContent = original;
      }
    });
  });

  /* -------------------------------------------------- SCROLL PROGRESS BAR */
  onReady(function () {
    const bar = document.createElement("div");
    bar.className = "progress";
    bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);
    let ticking = false;
    const update = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = "scaleX(" + (max > 0 ? Math.min(window.scrollY / max, 1) : 0) + ")";
      ticking = false;
    };
    window.addEventListener("scroll", () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  });

  /* -------------------------------------------------- GSAP ANIMATIONS
     Hero entrance lives in animations.css (pure CSS, starts at first paint).
     Here we only handle scroll reveals — and anything already on screen when
     JS boots is left visible (never hidden + re-animated → no flash). */
  onReady(function () {
    if (typeof gsap === "undefined" || prefersReduced) {
      document.querySelectorAll(".reveal").forEach((el) => el.classList.add("is-in"));
      return;
    }
    gsap.registerPlugin(ScrollTrigger);

    const mm = gsap.matchMedia();

    mm.add("(prefers-reduced-motion: no-preference)", () => {
      const vh = window.innerHeight;

      // Generic scroll reveals — skip elements already past their trigger point
      gsap.utils.toArray(".reveal").forEach((el) => {
        if (el.getBoundingClientRect().top < vh * 0.78) { el.classList.add("is-in"); return; }
        gsap.fromTo(el, { autoAlpha: 0, y: 36 }, {
          autoAlpha: 1, y: 0, duration: 0.9, ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 78%", once: true },
        });
      });

      // Staggered groups — same rule: visible groups stay untouched
      gsap.utils.toArray("[data-stagger]").forEach((group) => {
        if (group.getBoundingClientRect().top < vh * 0.76) return;
        const kids = group.children;
        gsap.fromTo(kids, { autoAlpha: 0, y: 40 }, {
          autoAlpha: 1, y: 0, duration: 0.8, ease: "power2.out", stagger: 0.12,
          scrollTrigger: { trigger: group, start: "top 76%", once: true },
        });
      });

      // Scroll-linked hero parallax: the image drifts down slower than the page
      // scrolls (translate only, no zoom). Sliders parallax the wrapper instead.
      gsap.utils.toArray(".hero__media > img, .hero__media > video").forEach((media) => {
        gsap.to(media, {
          yPercent: 18, ease: "none",
          scrollTrigger: { trigger: media.closest(".hero"), start: "top top", end: "bottom top", scrub: true },
        });
      });
      gsap.utils.toArray(".hero__slider").forEach((sl) => {
        gsap.to(sl, {
          yPercent: 10, ease: "none",
          scrollTrigger: { trigger: sl.closest(".hero"), start: "top top", end: "bottom top", scrub: true },
        });
      });

      // Count-up stats
      gsap.utils.toArray("[data-count]").forEach((el) => {
        const target = parseFloat(el.dataset.count);
        const obj = { v: 0 };
        gsap.to(obj, {
          v: target, duration: 1.6, ease: "power1.out",
          scrollTrigger: { trigger: el, start: "top 82%", once: true },
          onUpdate: () => { el.textContent = Math.round(obj.v) + (el.dataset.suffix || ""); },
        });
      });

      return () => {}; // matchMedia auto-cleanup
    });

    // Safety net: after full load, force-reveal anything still hidden
    // (covers print, headless renders, or a stalled ScrollTrigger).
    window.addEventListener("load", () => {
      ScrollTrigger.refresh();
      setTimeout(() => {
        document.querySelectorAll(".reveal").forEach((el) => {
          if (parseFloat(getComputedStyle(el).opacity) < 0.05) {
            gsap.set(el, { autoAlpha: 1, y: 0, clearProps: "transform" });
          }
        });
        ScrollTrigger.refresh();
      }, 1200);
    });
  });

  /* -------------------------------------------------- current year */
  onReady(function () {
    document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
  });
})();

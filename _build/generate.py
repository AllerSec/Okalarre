# -*- coding: utf-8 -*-
"""
Finca Okalarre — static site generator.
Emits ES (root), EU (/eu/), FR (/fr/): home + subpages + legal + 404,
plus sitemap.xml, robots.txt, manifest. Uses only the client's real photos.
Run from project root:  python _build/generate.py
"""
import os, sys, html, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)

from content import BIZ, LANGS, SLUGS, NAV, UI, WHY
from pages import PAGES, FAQ, HOME, IMG, HERO, alt, VENUE, GAL
import icons as I

def e(s): return html.escape(s, quote=True)

# order of pages in nav and celebrations hub
CELEB = ["bodas","comuniones","eventos","empresa"]
LEGAL = ["aviso-legal","privacidad","cookies"]

def rel_prefix(lang):
    """Path back to site root from a page in this language folder."""
    return "../" if LANGS_BY[lang]["dir"] else ""

LANGS_BY = {l["code"]: l for l in LANGS}

def url_for(lang, page):
    """Absolute-from-root URL (e.g. 'eu/ezkontzak.html' or 'index.html')."""
    d = LANGS_BY[lang]["dir"]
    slug = SLUGS[page][lang]
    return f"{d}{slug}.html"

def href(cur_lang, page):
    """Link from a page in cur_lang to another page (same lang)."""
    return rel_prefix(cur_lang) + url_for(cur_lang, page)

def asset(lang, path):
    return rel_prefix(lang) + "assets/" + path

def img_tag(lang, name, alt_text, cls="", sizes="", eager=False):
    folder = "gallery" if name.startswith("gallery") else ("venue" if name.startswith("venue") else "brand")
    src = asset(lang, f"img/{folder}/{name}.webp")
    loading = "eager" if eager else "lazy"
    fetch = ' fetchpriority="high"' if eager else ''
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{src}"{c} alt="{e(alt_text)}" loading="{loading}" decoding="async"{fetch} width="1200" height="800">'

# --------------------------------------------------------------------- HEAD
def head(lang, page, title, desc):
    L = LANGS_BY[lang]
    canonical = f'{BIZ["domain"]}/' + (url_for(lang, page).replace("index.html",""))
    # hreflang alternates
    alts = []
    for ll in LANGS:
        u = url_for(ll["code"], page).replace("index.html","")
        alts.append(f'<link rel="alternate" hreflang="{ll["html"]}" href="{BIZ["domain"]}/{u}">')
    alts.append(f'<link rel="alternate" hreflang="x-default" href="{BIZ["domain"]}/{url_for("es", page).replace("index.html","")}">')
    og_img = f'{BIZ["domain"]}/assets/img/{("venue" if HERO.get(page,"venue-01").startswith("venue") else "gallery")}/{HERO.get(page,"venue-01")}.webp'
    a = lambda p: asset(lang, p)
    return f'''<!doctype html>
<html lang="{L['html']}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Unax Aller — unaxaller.com">
<link rel="canonical" href="{canonical}">
{chr(10).join(alts)}
<meta name="theme-color" content="#46583f">
<meta name="geo.region" content="ES-NA"><meta name="geo.placename" content="Bera, Navarra">
<meta name="geo.position" content="{BIZ['lat']};{BIZ['lng']}"><meta name="ICBM" content="{BIZ['lat']}, {BIZ['lng']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Finca Okalarre">
<meta property="og:locale" content="{ {'es':'es_ES','eu':'eu_ES','fr':'fr_FR','en':'en_GB'}[lang] }">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="{rel_prefix(lang)}favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="{a('img/brand/favicon-32.png')}" sizes="32x32">
<link rel="apple-touch-icon" href="{a('img/brand/favicon-180.png')}">
<link rel="manifest" href="{rel_prefix(lang)}site.webmanifest">
<link rel="preload" href="{a('fonts/playfair-display-600-latin.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{a('fonts/inter-400-latin.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{a('css/main.css')}">
<link rel="stylesheet" href="{a('css/animations.css')}">
{schema(lang, page, title, desc)}
</head>'''

# --------------------------------------------------------------------- SCHEMA
def schema(lang, page, title, desc):
    base = {
      "@context":"https://schema.org","@type":["EventVenue","LocalBusiness"],
      "name":"Finca Okalarre","description":desc,
      "url":BIZ["domain"]+"/","image":f'{BIZ["domain"]}/assets/img/venue/venue-01.webp',
      "telephone":"+34"+BIZ["phone1"].replace(" ",""),
      "email":BIZ["email"],"priceRange":"€€€",
      "address":{"@type":"PostalAddress","streetAddress":"Ctra. Ibardin, Elzaurdia s/n",
                 "postalCode":BIZ["zip"],"addressLocality":"Bera","addressRegion":"Navarra","addressCountry":"ES"},
      "geo":{"@type":"GeoCoordinates","latitude":BIZ["lat"],"longitude":BIZ["lng"]},
      "areaServed":["Navarra","Gipuzkoa","Iparralde","País Vasco"],
      "maximumAttendeeCapacity":150,
      "sameAs":["https://www.instagram.com/fincaokalarre/",
                "https://www.facebook.com/Okalarre-Bodas-Eventos-141045566335509/",
                "https://www.pinterest.com/bodasokalarre/"]
    }
    out = [f'<script type="application/ld+json">{json.dumps(base, ensure_ascii=False)}</script>']
    if page == "faq":
        faq = {"@context":"https://schema.org","@type":"FAQPage",
               "mainEntity":[{"@type":"Question","name":q,
                              "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ[lang]]}
        out.append(f'<script type="application/ld+json">{json.dumps(faq, ensure_ascii=False)}</script>')
    return "\n".join(out)

# --------------------------------------------------------------------- NAV
def nav(lang, current):
    n = NAV[lang]; u = UI[lang]
    def link(p, label=None):
        cur = ' aria-current="page"' if p==current else ''
        return f'<a class="nav__link" href="{href(lang,p)}"{cur}>{label or n[p]}</a>'
    # lang switcher: same page in each language
    langsw = '<div class="lang" role="group" aria-label="Idioma">' + "".join(
        f'<a href="{lang_link(lang, ll["code"], current)}" hreflang="{ll["html"]}" aria-current="{"true" if ll["code"]==lang else "false"}" onclick="try{{localStorage.setItem(\'okalarre_lang\',\'{ll["code"]}\')}}catch(e){{}}">{ll["short"]}</a>'
        for ll in LANGS) + '</div>'
    celeb_dd = '<div class="nav__dd">' + "".join(f'<a href="{href(lang,p)}">{n[p]}</a>' for p in CELEB) + '</div>'
    desktop = f'''
  <ul class="nav__links">
    <li>{link("okalarre")}</li>
    <li class="nav__item">{link("celebraciones")}{celeb_dd}</li>
    <li>{link("espacios")}</li>
    <li>{link("gastronomia")}</li>
    <li>{link("galeria")}</li>
    <li>{link("localizacion")}</li>
    <li>{link("contacto")}</li>
    <li>{langsw}</li>
  </ul>
  <a class="btn btn--accent nav__cta desktop-cta" href="https://wa.me/{BIZ['whatsapp']}" target="_blank" rel="noopener">{I.WHATSAPP}{u['whatsapp']}</a>'''
    mobile_items = ["okalarre"]+CELEB+["espacios","gastronomia","galeria","localizacion","faq","contacto"]
    mobile = '<nav class="mobile-menu" id="mobile-menu" aria-label="Menú móvil">' + "".join(
        f'<a href="{href(lang,p)}">{n[p]}</a>' for p in mobile_items) + langsw + \
        f'<a class="btn btn--accent" style="margin-top:1.5rem" href="https://wa.me/{BIZ["whatsapp"]}" target="_blank" rel="noopener">{I.WHATSAPP}{u["whatsapp"]}</a></nav>'
    return f'''<a class="skip-link" href="#main">{u['skip']}</a>
<header class="nav"><div class="container nav__inner">
  <a class="nav__logo" href="{href(lang,'home')}" aria-label="Finca Okalarre — inicio"><img src="{asset(lang,'img/brand/logo.png')}" alt="Finca Okalarre" width="644" height="304"></a>
  {desktop}
  <button class="nav__burger" aria-label="{u['menu']}" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
</div></header>
{mobile}'''

def lang_link(cur_lang, target_lang, page):
    """Relative href from a page in cur_lang to the same page in target_lang."""
    target = url_for(target_lang, page)
    if page == "home":
        target = target.replace("index.html", "")
    return rel_prefix(cur_lang) + target

# --------------------------------------------------------------------- FOOTER
def footer(lang):
    n = NAV[lang]; u = UI[lang]
    explore = [("okalarre"),("espacios"),("gastronomia"),("galeria")]
    contact = f'''<ul>
      <li><a href="tel:{BIZ['phone1_tel']}">{BIZ['phone1']}</a></li>
      <li><a href="tel:{BIZ['phone2_tel']}">{BIZ['phone2']}</a></li>
      <li><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
      <li>{BIZ['address']}<br>{BIZ['zip']} Bera, Navarra</li>
    </ul>'''
    legal_links = " ".join(f'<a href="{href(lang,p)}">{n.get(p, p)}</a>' for p in LEGAL)
    legal_names = {"es":["Aviso legal","Privacidad","Cookies"],
                   "eu":["Lege-oharra","Pribatutasuna","Cookieak"],
                   "fr":["Mentions légales","Confidentialité","Cookies"],
                   "en":["Legal notice","Privacy","Cookies"]}[lang]
    legal_links = " ".join(f'<a href="{href(lang,p)}">{name}</a>' for p,name in zip(LEGAL, legal_names))
    return f'''<footer class="footer"><div class="container">
  <div class="footer__grid">
    <div>
      <div class="footer__logo"><img src="{asset(lang,'img/brand/logo.png')}" alt="Finca Okalarre" width="644" height="304"></div>
      <p style="font-size:var(--fs-sm);max-width:34ch;color:rgba(245,241,232,.7)">{e(HOME[lang]['hero_sub'])}</p>
      <div class="footer__social">
        <a href="https://wa.me/{BIZ['whatsapp']}" target="_blank" rel="noopener" aria-label="WhatsApp">{I.WHATSAPP}</a>
        <a href="https://www.instagram.com/fincaokalarre/" target="_blank" rel="noopener" aria-label="Instagram">{I.IG}</a>
        <a href="https://www.facebook.com/Okalarre-Bodas-Eventos-141045566335509/" target="_blank" rel="noopener" aria-label="Facebook">{I.FB}</a>
      </div>
    </div>
    <div><h4>{u['footer_explore']}</h4><ul>{"".join(f'<li><a href="{href(lang,p)}">{n[p]}</a></li>' for p in explore)}</ul></div>
    <div><h4>{u['footer_celebrate']}</h4><ul>{"".join(f'<li><a href="{href(lang,p)}">{n[p]}</a></li>' for p in CELEB)}</ul></div>
    <div><h4>{u['footer_contact']}</h4>{contact}</div>
  </div>
  <div class="footer__bottom">
    <span>© <span data-year>2026</span> {BIZ['name']} · {u['rights']}</span>
    <span class="footer__legal-links">{legal_links}</span>
    <span>{u['designed']} <a href="{BIZ['author_url']}" target="_blank" rel="noopener">unaxaller.com</a></span>
  </div>
</div></footer>'''

# --------------------------------------------------------------------- COMMON TAIL
def tail(lang):
    return f'''
<a class="wa-float" href="https://wa.me/{BIZ['whatsapp']}" target="_blank" rel="noopener" aria-label="WhatsApp">{I.WHATSAPP}</a>
<div class="lightbox" id="lightbox" role="dialog" aria-label="Galería" aria-modal="true">
  <button class="lightbox__close" aria-label="Cerrar">&times;</button>
  <button class="lightbox__nav prev" aria-label="Anterior">&#8249;</button>
  <img src="" alt="">
  <button class="lightbox__nav next" aria-label="Siguiente">&#8250;</button>
  <!-- lightbox image alt set dynamically -->

</div>
<script src="{asset(lang,'js/gsap.min.js')}" defer></script>
<script src="{asset(lang,'js/ScrollTrigger.min.js')}" defer></script>
<script src="{asset(lang,'js/main.js')}" defer></script>
</body></html>'''

def loader(lang):
    return f'''<div class="loader" id="loader"><div class="loader__mark">
  <img class="lo-logo" src="{asset(lang,'img/brand/logo.png')}" alt="Finca Okalarre" width="644" height="304">
  <div class="loader__bar"><i></i></div>
</div></div>'''

# --------------------------------------------------------------------- HERO
def hero(lang, page, title, sub, eyebrow, full=False, cta=True, slides=None):
    u = UI[lang]
    himg = HERO.get(page, "venue-01")
    cls = "hero" if full else "hero hero--page"
    cta_html = f'''<div class="hero__cta btn-group">
      <a class="btn btn--lg" href="{href(lang,'contacto')}">{u['cta_idea']}{I.ARROW}</a>
      <a class="btn btn--lg btn--ghost-light" href="https://wa.me/{BIZ['whatsapp']}" target="_blank" rel="noopener">{I.WHATSAPP}{u['whatsapp']}</a>
    </div>''' if cta else ''
    scroll = f'''<div class="hero__scroll" aria-hidden="true"><span class="mouse"></span>{u['scroll']}</div>''' if full else ''
    eb = f'<p class="eyebrow" style="color:var(--sage-soft)">{eyebrow}</p>' if eyebrow else ''
    if slides:
        slide_html = "".join(
            f'<div class="hero__slide{ " is-active" if i==0 else "" }">{img_tag(lang, nm, title, eager=(i==0))}</div>'
            for i, nm in enumerate(slides))
        dots = "".join(f'<button class="hero__dot" type="button" aria-label="Imagen {i+1}"></button>' for i in range(len(slides)))
        media = f'<div class="hero__media"><div class="hero__slider">{slide_html}</div></div><div class="hero__dots" role="tablist" aria-label="Galería del hero">{dots}</div>'
    else:
        media = f'<div class="hero__media">{img_tag(lang, himg, title, eager=True)}</div>'
    return f'''<section class="{cls}">
  {media}
  <div class="container hero__inner">
    {eb}
    <h1 class="hero__title">{title}</h1>
    {f'<p class="hero__sub">{sub}</p>' if sub else ''}
    {cta_html}
  </div>
  {scroll}
</section>'''

# --------------------------------------------------------------------- BUILDERS
def write(path_rel, content):
    p = os.path.join(ROOT, path_rel)
    os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

def body_paras(paras):
    return "\n".join(f'<p class="reveal">{e(p)}</p>' for p in paras)

def gallery_strip(lang, names, n=5):
    """Asymmetric mosaic: first image large (2x2), four satellites."""
    items = "".join(f'<a href="{href(lang,"galeria")}">{img_tag(lang, nm, f"Okalarre {i+1}")}</a>'
                    for i,nm in enumerate(names[:n]))
    return f'<div class="gallery-preview gallery-preview--mosaic" data-stagger>{items}</div>'

def marquee(lang):
    n = NAV[lang]
    items = [n["bodas"], n["comuniones"], n["eventos"], n["empresa"]] + [t for _,t,_ in WHY[lang]]
    spans = "".join(f'<span>{e(t)}</span>' for t in items)
    return f'''<div class="marquee" aria-hidden="true"><div class="marquee__track">
  <div class="marquee__group">{spans}</div><div class="marquee__group">{spans}</div>
</div></div>'''

def quote_band(lang):
    q = {"es":"Quince años de experiencia avalan un proyecto donde los límites solo los pones tú.",
         "eu":"Hamabost urteko esperientziak abalatzen du proiektu hau: mugak zuk bakarrik jartzen dituzu.",
         "fr":"Quinze ans d'expérience soutiennent un projet où les seules limites sont les vôtres.",
         "en":"Fifteen years of experience back a project where you set the only limits."}[lang]
    cta = {"es":"Descubre Okalarre","eu":"Ezagutu Okalarre","fr":"Découvrez Okalarre","en":"Discover Okalarre"}[lang]
    return f'''<section class="band" data-parallax>
  <div class="band__media">{img_tag(lang,"venue-14","Finca Okalarre — Baztan-Bidasoa")}</div>
  <div class="container band__inner">
    <p class="band__quote reveal">{e(q)}</p>
    <a class="btn btn--lg btn--ghost-light reveal" href="{href(lang,'okalarre')}">{cta}{I.ARROW}</a>
  </div>
</section>'''

def faq_section(lang, n=6):
    nv = NAV[lang]
    items = "".join(f'''<div class="faq__item reveal"><button class="faq__q" aria-expanded="false"><span>{e(q)}</span><span class="plus" aria-hidden="true"></span></button>
      <div class="faq__a"><p>{e(a)}</p></div></div>''' for q,a in FAQ[lang][:n])
    btn = {"es":"Ver todas las preguntas","eu":"Ikusi galdera guztiak","fr":"Voir toutes les questions","en":"See all questions"}[lang]
    return f'''<section class="section bg-alt"><div class="container container--narrow">
  <header class="text-center" style="margin-bottom:2.5rem">
    <p class="eyebrow center">{nv['faq']}</p>
    <h2 class="section-title reveal" style="margin-inline:auto">{ {"es":"Las dudas más frecuentes","eu":"Ohiko zalantzak","fr":"Les questions les plus fréquentes","en":"The most common questions"}[lang] }</h2>
  </header>
  <div class="faq">{items}</div>
  <div class="text-center" style="margin-top:2.5rem"><a class="btn btn--outline reveal" href="{href(lang,'faq')}">{btn}{I.ARROW}</a></div>
</div></section>'''

# ---- HOME ----
def build_home(lang):
    u=UI[lang]; n=NAV[lang]; h=HOME[lang]
    why = "".join(f'''<div class="feature reveal"><div class="feature__icon">{I.ICONS[ic]}</div>
       <h3>{t}</h3><p>{d}</p></div>''' for ic,t,d in WHY[lang])
    celeb_cards = "".join(f'''<a class="card--photo reveal" href="{href(lang,p)}">
       {img_tag(lang, HERO[p], n[p])}
       <div class="card--photo__body"><h3>{n[p]}</h3><span class="card__link">{u['discover']} {I.ARROW}</span></div></a>'''
       for p in CELEB)
    # italic accent on the closing word of the hero title
    parts = h["hero_t"].rsplit(" ", 1)
    title_html = f'{e(parts[0])} <em class="hero__accent">{e(parts[1])}</em>' if len(parts)==2 else e(h["hero_t"])
    eyebrow_home = {"es":"Bera · Navarra — Valle del Baztan-Bidasoa",
                    "eu":"Bera · Nafarroa — Baztan-Bidasoa harana",
                    "fr":"Bera · Navarre — Vallée du Baztan-Bidassoa",
                    "en":"Bera · Navarre — Baztan-Bidasoa valley"}[lang]
    content = f'''{head(lang,"home",h["seo_t"],h["seo_d"])}
<body>
{loader(lang)}
{nav(lang,"home")}
<main id="main">
{hero(lang,"home",title_html,h["hero_sub"],eyebrow_home,full=True,slides=["gallery-09","gallery-08","gallery-10","gallery-11","gallery-21"])}
{marquee(lang)}

<section class="section text-center">
  <div class="container container--narrow">
    <p class="eyebrow center">Okalarre</p>
    {I.LEAF_DIVIDER}
    <p class="lead reveal" style="font-family:var(--font-display);font-size:var(--fs-xl);line-height:1.4;color:var(--charcoal)">{e(h["anchor"])}</p>
    <p class="reveal mx-auto" style="margin-top:1.5rem">{e(h["intro"])}</p>
  </div>
</section>

<section class="section bg-alt">
  <div class="container">
    <header class="text-center" style="margin-bottom:3rem">
      <p class="eyebrow center">{u['celebrations']}</p>
      <h2 class="section-title reveal" style="margin-inline:auto">{u['ph_celebrations']}</h2>
    </header>
    <div class="grid grid--4" data-stagger>{celeb_cards}</div>
  </div>
</section>

<section class="section bg-forest">
  <div class="container">
    <header class="text-center" style="margin-bottom:3rem">
      <p class="eyebrow center" style="color:var(--sage-soft)">{u['why_title']}</p>
    </header>
    <div class="grid grid--4" data-stagger>{why}</div>
    <div class="stats" style="margin-top:4rem">
      <div><div class="stat__num" data-count="15">0</div><div class="stat__label">{ {"es":"Años de experiencia","eu":"Esperientzia urte","fr":"Ans d'expérience","en":"Years of experience"}[lang] }</div></div>
      <div><div class="stat__num" data-count="150">0</div><div class="stat__label">{ {"es":"Invitados máx.","eu":"Gonbidatu max.","fr":"Invités max.","en":"Guests max."}[lang] }</div></div>
      <div><div class="stat__num">1</div><div class="stat__label">{ {"es":"Evento al día","eu":"Ekitaldi egunean","fr":"Événement / jour","en":"Event per day"}[lang] }</div></div>
      <div><div class="stat__num">15'</div><div class="stat__label">{ {"es":"De Irun","eu":"Irundik","fr":"D'Irun","en":"From Irun"}[lang] }</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      {media_framed(lang,"venue-04", n["espacios"])}
      <div class="split__body stack">
        <p class="eyebrow">{ {"es":"El espacio","eu":"Espazioa","fr":"L'espace","en":"The space"}[lang] }</p>
        <h2 class="section-title reveal">{NAV[lang]["espacios"]}</h2>
        <p class="reveal has-dropcap">{e(PAGES["espacios"][lang]["body"][0])}</p>
        <a class="btn btn--outline reveal" href="{href(lang,'espacios')}">{u['view_spaces']}{I.ARROW}</a>
      </div>
    </div>
  </div>
</section>

<section class="section bg-alt text-center">
  <div class="container">
    <p class="eyebrow center">{n['galeria']}</p>
    <h2 class="section-title reveal" style="margin:0 auto 2.5rem">{ {"es":"Lo mejor que tenemos: el lugar","eu":"Dugun onena: lekua","fr":"Le meilleur de nous : le lieu","en":"Our greatest asset: the place"}[lang] }</h2>
    {gallery_strip(lang, IMG["home"]+["gallery-13","gallery-22","gallery-23"], 6)}
    <a class="btn reveal" style="margin-top:2.5rem" href="{href(lang,'galeria')}">{u['view_gallery']}{I.ARROW}</a>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split split--reverse">
      {media_framed(lang,"venue-01", n["localizacion"])}
      <div class="split__body stack">
        <p class="eyebrow">{u['how_arrive']}</p>
        <h2 class="section-title reveal">{ {"es":"A 15 min de Irun, 30 de Donosti","eu":"Irundik 15 min, Donostiatik 30","fr":"À 15 min d'Irun, 30 de Donosti","en":"15 min from Irun, 30 from Donosti"}[lang] }</h2>
        <p class="reveal has-dropcap">{e(PAGES["localizacion"][lang]["body"][0])}</p>
        <a class="btn btn--outline reveal" href="{href(lang,'localizacion')}">{u['how_arrive']}{I.ARROW}</a>
      </div>
    </div>
  </div>
</section>

{cta_band(lang)}
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,"home"), content)

def cta_band(lang):
    u=UI[lang]
    return f'''<section class="section bg-forest text-center">
  <div class="container container--narrow">
    {I.LEAF_DIVIDER}
    <h2 class="reveal" style="color:var(--cream)">{ {"es":"Cuéntanos tu idea","eu":"Kontaiguzu zure ideia","fr":"Parlez-nous de votre projet","en":"Tell us your idea"}[lang] }</h2>
    <p class="reveal" style="color:rgba(245,241,232,.85);margin:1rem auto 2rem">{ {"es":"Ven, cuéntanos cómo lo imaginas y nosotros pondremos todo el cariño y la dedicación que mereces.","eu":"Etorri, kontaiguzu nola irudikatzen duzun eta merezi duzun maitasun eta gogo guztia jarriko dugu.","fr":"Venez nous raconter comment vous l'imaginez et nous y mettrons tout le soin et le dévouement que vous méritez.","en":"Come and tell us how you imagine it, and we'll bring all the care and dedication you deserve."}[lang] }</p>
    <div class="btn-group" style="justify-content:center">
      <a class="btn btn--lg btn--accent" href="{href(lang,'contacto')}">{u['cta_idea']}{I.ARROW}</a>
      <a class="btn btn--lg btn--ghost-light" href="https://wa.me/{BIZ['whatsapp']}" target="_blank" rel="noopener">{I.WHATSAPP}{u['whatsapp']}</a>
    </div>
  </div>
</section>'''

# ---- GENERIC CONTENT PAGE ----
def media_framed(lang, img_name, alt_text):
    return f'<div class="split__media-wrap reveal"><div class="split__media">{img_tag(lang, img_name, alt_text)}</div></div>'

def build_content_page(lang, page):
    u=UI[lang]; n=NAV[lang]; d=PAGES[page][lang]; imgs=IMG[page]
    sections=[]
    paras=d["body"]
    extra_imgs = imgs[1:]
    last = len(paras)-1
    for idx,para in enumerate(paras):
        rev = 'split--reverse' if idx%2 else ''
        num = f'<span class="sec-num reveal">{idx+1:02d}</span>'
        if idx==0:
            body = (f'<p class="eyebrow">{d["eyebrow"]}</p>'
                    f'<h2 class="section-title reveal">{e(d["title"])}</h2>'
                    f'<p class="reveal has-dropcap">{e(para)}</p>')
            sections.append(f'''<section class="section">
  <div class="container"><div class="split">
    {media_framed(lang, imgs[0], alt(lang,page,1))}
    <div class="split__body stack">{body}</div>
  </div></div></section>''')
        else:
            img = extra_imgs[(idx-1)%len(extra_imgs)]
            # final paragraph rendered as an elegant pull-quote
            if idx==last and len(para) < 220:
                ptext = f'<p class="pullquote reveal">{e(para)}</p>'
            else:
                ptext = f'<p class="reveal">{e(para)}</p>'
            sections.append(f'''<section class="section {'bg-alt' if idx%2 else ''}">
  <div class="container"><div class="split {rev}">
    {media_framed(lang, img, alt(lang,page,idx+1))}
    <div class="split__body stack">{num}{ptext}</div>
  </div></div></section>''')
    gallery = f'''<section class="section text-center"><div class="container">
    <p class="eyebrow center">{n['galeria']}</p>
    <h2 class="section-title reveal" style="margin:0 auto 2.5rem">{ {"es":"Inspírate","eu":"Inspiratu","fr":"Inspirez-vous","en":"Get inspired"}[lang] }</h2>
    {gallery_strip(lang, imgs, 6)}
    <a class="btn reveal" style="margin-top:2.5rem" href="{href(lang,'galeria')}">{u['view_gallery']}{I.ARROW}</a>
  </div></section>'''
    content=f'''{head(lang,page,d["seo_t"],d["seo_d"])}
<body>
{nav(lang,page)}
<main id="main">
{hero(lang,page,e(d["title"]),e(d["sub"]),d["eyebrow"])}
{"".join(sections)}
{gallery}
{cta_band(lang)}
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,page), content)

# ---- CELEBRACIONES HUB ----
def build_celeb(lang):
    u=UI[lang]; n=NAV[lang]
    cards="".join(f'''<a class="card reveal" href="{href(lang,p)}">
      <div class="card__media">{img_tag(lang, HERO[p], n[p])}</div>
      <div class="card__body"><h3>{n[p]}</h3><p>{e(PAGES[p][lang]['sub'])}</p><span class="card__link">{u['discover']} {I.ARROW}</span></div></a>''' for p in CELEB)
    seo={"es":("Celebraciones — Bodas, comuniones, eventos y empresa | Finca Okalarre",
              "Bodas, comuniones, fiestas privadas y reuniones de empresa en plena naturaleza, en Okalarre. Un único evento al día y privacidad total."),
         "eu":("Ospakizunak — Ezkontzak, jaunartzeak, ekitaldiak eta enpresa | Finca Okalarre",
              "Ezkontzak, jaunartzeak, festa pribatuak eta enpresa bilerak naturan, Okalarren. Egunean ekitaldi bakarra eta erabateko pribatutasuna."),
         "fr":("Célébrations — Mariages, communions, événements et entreprise | Finca Okalarre",
              "Mariages, communions, fêtes privées et réunions d'entreprise en pleine nature, à Okalarre. Un seul événement par jour et une intimité totale."),
         "en":("Celebrations — Weddings, communions, events & corporate | Finca Okalarre",
              "Weddings, communions, private parties and corporate meetings in pure nature, at Okalarre. One single event per day and total privacy.")}[lang]
    content=f'''{head(lang,"celebraciones",seo[0],seo[1])}
<body>
{nav(lang,"celebraciones")}
<main id="main">
{hero(lang,"celebraciones",NAV[lang]["celebraciones"], UI[lang]["ph_celebrations"], UI[lang]["celebrations"])}
<section class="section"><div class="container">
  <div class="grid grid--4" data-stagger>{cards}</div>
</div></section>
{cta_band(lang)}
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,"celebraciones"), content)

# ---- GALLERY ----
def build_gallery(lang):
    n=NAV[lang]
    items="".join(f'<figure class="gallery__item" data-lightbox="{asset(lang,f"img/gallery/{g}.webp")}">{img_tag(lang,g,f"Finca Okalarre — galería {i+1}")}</figure>' for i,g in enumerate(GAL))
    seo={"es":("Galería de fotos — Finca Okalarre | Bodas y eventos en Bera, Navarra",
              "Galería de fotos de Finca Okalarre: bodas, espacios interiores y exteriores, terrazas y el entorno natural del valle Baztan-Bidasoa."),
         "eu":("Argazki galeria — Finca Okalarre | Ezkontzak eta ekitaldiak Beran",
              "Finca Okalarreren argazki galeria: ezkontzak, barne eta kanpoko espazioak, terrazak eta Baztan-Bidasoa haraneko ingurune naturala."),
         "fr":("Galerie photos — Finca Okalarre | Mariages et événements à Bera",
              "Galerie photos de Finca Okalarre : mariages, espaces intérieurs et extérieurs, terrasses et l'environnement naturel de la vallée du Baztan-Bidassoa."),
         "en":("Photo gallery — Finca Okalarre | Weddings & events in Bera, Navarre",
              "Photo gallery of Finca Okalarre: weddings, indoor and outdoor spaces, terraces and the natural surroundings of the Baztan-Bidasoa valley.")}[lang]
    content=f'''{head(lang,"galeria",seo[0],seo[1])}
<body>
{nav(lang,"galeria")}
<main id="main">
{hero(lang,"galeria",n["galeria"], {"es":"Las imágenes lo dicen todo.","eu":"Irudiek dena diote.","fr":"Les images disent tout.","en":"The images say it all."}[lang], n["galeria"], cta=False)}
<section class="section"><div class="container">
  <div class="gallery">{items}</div>
</div></section>
{cta_band(lang)}
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,"galeria"), content)

# ---- FAQ ----
def build_faq(lang):
    n=NAV[lang]
    items="".join(f'''<div class="faq__item reveal"><button class="faq__q" aria-expanded="false"><span>{e(q)}</span><span class="plus" aria-hidden="true"></span></button>
      <div class="faq__a"><p>{e(a)}</p></div></div>''' for q,a in FAQ[lang])
    seo={"es":("Preguntas frecuentes — Finca Okalarre | Bodas y eventos en Navarra",
              "Resolvemos las dudas más frecuentes sobre celebrar en Okalarre: aforo, catering propio, menús especiales, horarios y exclusividades."),
         "eu":("Ohiko galderak — Finca Okalarre | Ezkontzak eta ekitaldiak Nafarroan",
              "Okalarren ospatzeari buruzko ohiko zalantzak argitzen ditugu: edukiera, catering propioa, menu bereziak, ordutegiak eta esklusibotasunak."),
         "fr":("Questions fréquentes — Finca Okalarre | Mariages et événements en Navarre",
              "Nous répondons aux questions les plus fréquentes sur célébrer à Okalarre : capacité, traiteur maison, menus spéciaux, horaires et exclusivités."),
         "en":("FAQ — Finca Okalarre | Weddings & events in Navarre",
              "We answer the most common questions about celebrating at Okalarre: capacity, in-house catering, special menus, timing and exclusivities.")}[lang]
    content=f'''{head(lang,"faq",seo[0],seo[1])}
<body>
{nav(lang,"faq")}
<main id="main">
{hero(lang,"faq",n["faq"], {"es":"Las dudas más frecuentes, resueltas.","eu":"Ohiko zalantzak, argituta.","fr":"Les questions les plus fréquentes, résolues.","en":"The most common questions, answered."}[lang], n["faq"])}
<section class="section"><div class="container container--narrow"><div class="faq">{items}</div></div></section>
{cta_band(lang)}
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,"faq"), content)

# ---- LOCALIZACION ----
def build_localizacion(lang):
    u=UI[lang]; n=NAV[lang]; d=PAGES["localizacion"][lang]
    maps_q=f'{BIZ["lat"]},{BIZ["lng"]}'
    embed=f'https://www.google.com/maps?q={maps_q}&hl={lang}&z=14&output=embed'
    body="".join(f'<p class="reveal">{e(p)}</p>' for p in d["body"])
    dist={"es":["Irun · 15 min","San Sebastián · 30 min","Pamplona · 45 min"],
          "eu":["Irun · 15 min","Donostia · 30 min","Iruñea · 45 min"],
          "fr":["Irun · 15 min","Saint-Sébastien · 30 min","Pampelune · 45 min"],
          "en":["Irun · 15 min","San Sebastián · 30 min","Pamplona · 45 min"]}[lang]
    chips="".join(f'<span class="feature" style="padding:1rem 1.4rem">{c}</span>' for c in dist)
    content=f'''{head(lang,"localizacion",d["seo_t"],d["seo_d"])}
<body>
{nav(lang,"localizacion")}
<main id="main">
{hero(lang,"localizacion",e(d["title"]), e(d["sub"]), d["eyebrow"])}
<section class="section"><div class="container">
  <div class="split">
    <div class="split__body stack">{body}
      <div class="btn-group" style="margin-top:1rem">
        <a class="btn" href="https://www.google.com/maps/dir/?api=1&destination={maps_q}" target="_blank" rel="noopener">{I.PIN}{u['open_maps']}</a>
        <a class="btn btn--outline" href="tel:{BIZ['phone1_tel']}">{I.PHONE}{u['call']}</a>
      </div>
    </div>
    <div class="map-embed reveal"><iframe src="{embed}" title="Mapa Finca Okalarre" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  </div>
  <div class="grid grid--3" style="margin-top:3rem" data-stagger>{chips}</div>
</div></section>
{cta_band(lang)}
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,"localizacion"), content)

# ---- CONTACTO ----
def build_contacto(lang):
    u=UI[lang]; n=NAV[lang]
    seo={"es":("Contacto — Finca Okalarre | Bodas y eventos en Bera, Navarra",
              "Contacta con Finca Okalarre: formulario, WhatsApp y teléfono. Cuéntanos tu idea y te responderemos muy pronto."),
         "eu":("Harremanetarako — Finca Okalarre | Ezkontzak eta ekitaldiak Beran",
              "Jarri harremanetan Finca Okalarrerekin: formularioa, WhatsApp eta telefonoa. Kontaiguzu zure ideia eta laster erantzungo dizugu."),
         "fr":("Contact — Finca Okalarre | Mariages et événements à Bera, Navarre",
              "Contactez Finca Okalarre : formulaire, WhatsApp et téléphone. Parlez-nous de votre projet et nous vous répondrons très vite."),
         "en":("Contact — Finca Okalarre | Weddings & events in Bera, Navarre",
              "Get in touch with Finca Okalarre: contact form, WhatsApp and phone. Tell us your idea and we'll reply very soon.")}[lang]
    intro={"es":"Puedes rellenar el formulario si deseas contactar con Okalarre, o bien hacernos llegar un e-mail o llamarnos a cualquiera de nuestros teléfonos.",
           "eu":"Formularioa bete dezakezu Okalarrerekin harremanetan jarri nahi baduzu, edo e-mail bat bidali edo gure telefonoetako edozeinetara deitu.",
           "fr":"Vous pouvez remplir le formulaire si vous souhaitez contacter Okalarre, ou bien nous envoyer un e-mail ou nous appeler à l'un de nos téléphones.",
           "en":"Fill in the form if you'd like to contact Okalarre, or send us an e-mail or call any of our phone numbers."}[lang]
    content=f'''{head(lang,"contacto",seo[0],seo[1])}
<body>
{nav(lang,"contacto")}
<main id="main">
{hero(lang,"contacto",n["contacto"], intro, n["contacto"], cta=False)}
<section class="section"><div class="container">
  <div class="split">
    <div class="split__body stack">
      <p class="eyebrow">{u['footer_contact']}</p>
      <div class="contact-list" style="margin-top:1rem">
        <a href="tel:{BIZ['phone1_tel']}">{I.PHONE}{BIZ['phone1']}</a>
        <a href="tel:{BIZ['phone2_tel']}">{I.PHONE}{BIZ['phone2']}</a>
        <a href="mailto:{BIZ['email']}">{I.MAIL}{BIZ['email']}</a>
        <span>{I.PIN}{BIZ['address']}, {BIZ['zip']} Bera (Navarra)</span>
      </div>
      <a class="btn btn--accent" style="margin-top:1.5rem;align-self:flex-start" href="https://wa.me/{BIZ['whatsapp']}" target="_blank" rel="noopener">{I.WHATSAPP}{u['whatsapp']}</a>
    </div>
    <form class="form" id="contact-form" action="https://formspree.io/f/your-id" method="POST"
          data-ok="{u['form_ok']}" data-err="{u['form_err']}">
      <div class="form__status" role="status" aria-live="polite"></div>
      <div class="field--row">
        <div class="field"><label for="name">{u['name']} <span class="req">*</span></label><input id="name" name="name" type="text" required autocomplete="name"></div>
        <div class="field"><label for="email">{u['email']} <span class="req">*</span></label><input id="email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="field"><label for="subject">{u['subject']}</label><input id="subject" name="subject" type="text"></div>
      <div class="field"><label for="message">{u['message']} <span class="req">*</span></label><textarea id="message" name="message" required></textarea></div>
      <p class="form__note">{u['required']}</p>
      <button class="btn btn--lg" type="submit" data-sending="{u['sending']}">{u['send']}{I.ARROW}</button>
    </form>
  </div>
</div></section>
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,"contacto"), content)

# ---- LEGAL ----
def legal_body(lang, kind):
    from legal_content import LEGAL_TEXT
    return LEGAL_TEXT[kind][lang]

def build_legal(lang, kind):
    n=NAV[lang]
    names={"aviso-legal":{"es":"Aviso legal","eu":"Lege-oharra","fr":"Mentions légales","en":"Legal notice"},
           "privacidad":{"es":"Política de privacidad","eu":"Pribatutasun politika","fr":"Politique de confidentialité","en":"Privacy policy"},
           "cookies":{"es":"Política de cookies","eu":"Cookie politika","fr":"Politique de cookies","en":"Cookie policy"}}[kind][lang]
    from legal_content import LEGAL_TEXT
    # legal paragraphs intentionally contain inline HTML (mailto links) → not escaped
    blocks="".join(f'<h2 class="reveal">{e(h2)}</h2>'+"".join(f'<p class="reveal">{p}</p>' for p in ps) for h2,ps in LEGAL_TEXT[kind][lang])
    desc=f'{names} — Finca Okalarre.'
    content=f'''{head(lang,kind,f"{names} — Finca Okalarre",desc)}
<body>
{nav(lang,kind)}
<main id="main">
<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)"><div class="container container--narrow stack">
  <p class="eyebrow">{UI[lang]['footer_legal']}</p>
  <h1 class="reveal">{names}</h1>
  {blocks}
</div></section>
</main>
{footer(lang)}
{tail(lang)}'''
    write(url_for(lang,kind), content)

# ---- 404 ----
def build_404(lang):
    u=UI[lang]
    content=f'''{head(lang,"home",u["err_title"]+" — Finca Okalarre", u["err_text"])}
<body>
{nav(lang,"home")}
<main id="main"><section class="err-page">
  <div class="err-page__bg">{img_tag(lang,"venue-01","Finca Okalarre", eager=True)}</div>
  <div class="container stack" style="max-width:640px">
    <div class="err-code">404</div>
    <h1 style="color:var(--cream)">{u['err_title']}</h1>
    <p style="color:rgba(245,241,232,.9);margin-inline:auto">{u['err_text']}</p>
    <a class="btn btn--lg btn--ghost-light mx-auto" style="margin-top:1rem" href="{href(lang,'home')}">{u['back_home']}{I.ARROW}</a>
  </div>
</section></main>
{footer(lang)}
{tail(lang)}'''
    # ES 404 at root; localized ones inside folders
    path = "404.html" if lang=="es" else f'{LANGS_BY[lang]["dir"]}404.html'
    write(path, content)

# --------------------------------------------------------------------- SITE FILES
def build_sitemap():
    urls=[]
    pages=list(SLUGS.keys())
    for lang in [l["code"] for l in LANGS]:
        for p in pages:
            loc=f'{BIZ["domain"]}/'+url_for(lang,p).replace("index.html","")
            alts="".join(f'<xhtml:link rel="alternate" hreflang="{ll["html"]}" href="{BIZ["domain"]}/{url_for(ll["code"],p).replace("index.html","")}"/>' for ll in LANGS)
            urls.append(f'<url><loc>{loc}</loc>{alts}<changefreq>monthly</changefreq><priority>{"1.0" if p=="home" else "0.8"}</priority></url>')
    xml=f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>'''
    write("sitemap.xml", xml)

def build_robots():
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BIZ['domain']}/sitemap.xml\n")

def build_manifest():
    m={"name":"Finca Okalarre","short_name":"Okalarre","start_url":"/","display":"standalone",
       "background_color":"#46583f","theme_color":"#46583f","icons":[
         {"src":"/assets/img/brand/favicon-192.png","sizes":"192x192","type":"image/png"},
         {"src":"/assets/img/brand/favicon-512.png","sizes":"512x512","type":"image/png"}]}
    write("site.webmanifest", json.dumps(m, ensure_ascii=False, indent=2))

def build_404_redirect():
    # GitHub Pages serves /404.html for unknown paths automatically.
    pass

# --------------------------------------------------------------------- RUN
def main():
    for lang in [l["code"] for l in LANGS]:
        build_home(lang)
        build_okalarre(lang)
        build_celeb(lang)
        for p in CELEB: build_content_page(lang,p)
        for p in ["espacios","gastronomia"]: build_content_page(lang,p)
        build_gallery(lang)
        build_localizacion(lang)
        build_faq(lang)
        build_contacto(lang)
        for k in LEGAL: build_legal(lang,k)
        build_404(lang)
    build_sitemap(); build_robots(); build_manifest()
    print("OK - Site generated.")

def build_okalarre(lang):
    build_content_page(lang,"okalarre")

if __name__=="__main__":
    main()

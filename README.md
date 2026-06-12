# Finca Okalarre — Bodas & Eventos

Sitio web estático, trilingüe (ES · EU · FR), para Finca Okalarre (Bera, Navarra).
Diseñado y desarrollado por [unaxaller.com](https://unaxaller.com).

## Stack

- **HTML + CSS + JS estático** (sin framework, sin build en producción).
- **GSAP + ScrollTrigger** (self-hosted) para animaciones y microinteracciones.
- **Fuentes self-hosted**: Playfair Display (display) + Inter (cuerpo), subset latin/latin-ext WebP.
- **Imágenes**: WebP optimizadas, solo fotografía real del cliente (`assets/img/venue`, `assets/img/gallery`).

## Estructura

```
/                 → ES (idioma por defecto)
/eu/              → Euskara
/fr/              → Français
/assets/          → css, js, img (brand/venue/gallery), fonts
/legal            → avisos legales integrados en cada idioma
/_build/          → generador (Python) y contenido fuente — NO se publica
/contenido/       → archivo original extraído del sitio antiguo — NO se publica
sitemap.xml · robots.txt · site.webmanifest · 404.html · favicon.ico
```

Cada idioma tiene: inicio, okalarre, celebraciones, bodas, comuniones, eventos,
reuniones de empresa, espacios, gastronomía, galería, localización, preguntas
frecuentes, contacto, y páginas legales (aviso legal, privacidad, cookies) + 404.

## Características

- Detección automática de idioma por país (nunca euskara por defecto).
- Page loader solo en la primera visita de la sesión.
- Galería con lightbox, formulario conectable a Formspree, WhatsApp flotante.
- SEO completo: títulos/meta por página, hreflang ES/EU/FR, JSON-LD
  (`LocalBusiness` + `EventVenue` + `FAQPage`), Open Graph, geo tags, canonical.
- Responsive mobile-first, sin filas huérfanas en grids, `prefers-reduced-motion`.

## Regenerar el sitio

El HTML se genera desde `_build/` (contenido como datos, para mantener la paridad
trilingüe). Tras editar contenido:

```bash
python _build/generate.py
```

## Desplegar

- **GitHub Pages**: el contenido está en la raíz. Incluye `.nojekyll`.
- **Netlify**: incluye `_redirects` (404 por idioma). `npx netlify deploy --prod`.

## Pendiente de configurar por el cliente

- `action` del formulario de contacto (`_build/generate.py` → `formspree.io/f/your-id`).
- Enlaces reales de Instagram / Facebook en el footer.
- Dominio `fincaokalarre.com` con HTTPS.

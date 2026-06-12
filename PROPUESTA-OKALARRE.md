# Propuesta de nueva web — Finca Okalarre · Bodas & Eventos

> Documento de propuesta. Estructura, sitemap, wireframes, copy reescrito (manteniendo la esencia del original) y mejoras técnicas/SEO. Sin código todavía: esto es para validar con el cliente antes de construir.

---

## 0. Diagnóstico de la web actual (qué falla hoy)

| Problema | Detalle | Impacto |
|---|---|---|
| **WordPress 4.7.33 (2017)** | 8 años sin actualizar | Riesgo de hackeo, plugins muertos |
| **HTTP sin HTTPS** | Sin candado de seguridad | Google la marca "no segura", penaliza ranking |
| **Contenido congelado en 2019** | Blog parado en 2017 | Parece un negocio abandonado |
| **Catering desactualizado** | Mezcla Mahercatering con sponsors viejos (Divinus, Bokado, Gutizi) | Confunde al cliente |
| **Login de usuarios en el pie** | Residuo de BuddyPress | Inútil, da sensación de descuido |
| **Sin Google Maps embebido real / sin WhatsApp** | Solo coordenadas en texto | Fricción para contactar |
| **No responsive del todo / lenta** | Tema antiguo + imágenes sin optimizar | Mala experiencia en móvil (donde miran las novias) |

**Lo que SÍ funciona y conservamos:** las 36 fotos profesionales del entorno, el argumentario emocional (privacidad, naturaleza, sin límite de horario), la estructura trilingüe ES/EU/FR y el NAP correcto.

---

## 1. Stack recomendado: **Astro + Tailwind**

Lo elijo yo por estas razones concretas para este caso:

- **Trilingüe (ES/EU/FR)** → Astro tiene i18n nativo y limpio; evita duplicar 12 páginas a mano × 3.
- **Galería pesada (36+ fotos)** → Astro optimiza imágenes automáticamente (WebP, lazy-load, tamaños responsive). Clave para una web de bodas que entra por el ojo.
- **Estático = rápido y barato** → se despliega gratis en **Netlify/GitHub Pages**, sin servidor, sin WordPress que mantener ni hackear.
- **SEO** → genera HTML puro perfecto para Google, con `hreflang` por idioma bien hecho.

> Alternativa más simple si el cliente quiere algo ultraligero: HTML+CSS+JS estático (como ubela). Funciona, pero con 3 idiomas obliga a mantener todo triplicado a mano. Astro lo evita.

---

## 2. Sitemap nuevo (arquitectura de la web)

Simplifico de ~12 páginas dispersas a una estructura clara, manteniendo todas las secciones reales:

```
/  (Home)
│
├── /okalarre            → "Okalarre" (presentación + el lugar + 15 años exp.)
│
├── /celebraciones       → hub de tipos de evento
│   ├── /bodas
│   ├── /comuniones
│   ├── /eventos          (antes "cuadrillas" / fiestas privadas)
│   └── /reuniones-empresa
│
├── /espacios            → interior + terrazas/jardín (con planos/capacidades)
├── /gastronomia         → Mahercatering (menús, premios)
├── /galeria             → las 36 fotos, en grid filtrable
├── /preguntas-frecuentes
├── /localizacion        → mapa Google embebido + cómo llegar
├── /contacto            → formulario + WhatsApp + teléfonos
└── /blog                → reactivado (o "Bodas reales" / testimonios)

Cada ruta existe en 3 idiomas:  /es/...  /eu/...  /fr/...
```

**Cambios clave vs. la web vieja:**
- Agrupo bodas/comuniones/eventos/empresa bajo **Celebraciones** (menú más limpio).
- "Cuadrillas" → **Eventos / Fiestas privadas** (nombre más universal y buscable).
- **Presentación** deja de estar escondida en la home y tiene su página `/okalarre`.
- Añado **WhatsApp** como canal principal (es como contactan las novias hoy).

---

## 3. Wireframe por página (qué lleva cada una)

### 🏠 HOME
```
┌─────────────────────────────────────────────┐
│ [Logo Okalarre]      ES·EU·FR    [Pide cita] │  ← nav fija
├─────────────────────────────────────────────┤
│                                             │
│     HERO a pantalla completa                │
│     (foto del mirador al valle + vídeo)     │
│     "Bodas y eventos en plena naturaleza"   │
│     "en el valle del Baztan-Bidasoa"        │
│     [Ver espacios]  [WhatsApp]              │
├─────────────────────────────────────────────┤
│  Frase emocional (la del original):         │
│  "¿Cuántas cosas excepcionales suceden a    │
│   las personas que queremos...?"            │
├─────────────────────────────────────────────┤
│  3 tarjetas: BODAS · EVENTOS · EMPRESA      │
├─────────────────────────────────────────────┤
│  Bloque "Por qué Okalarre" (4 iconos):      │
│  Privacidad · Sin horario · Naturaleza ·    │
│  Catering propio premiado                   │
├─────────────────────────────────────────────┤
│  Galería preview (6 fotos) → [Ver galería]  │
├─────────────────────────────────────────────┤
│  Mapa + "A 15min Irun / 30min Donosti"      │
├─────────────────────────────────────────────┤
│  CTA final: "Cuéntanos tu idea" + form      │
├─────────────────────────────────────────────┤
│  Footer: NAP · redes · idiomas · © 2026    │
└─────────────────────────────────────────────┘
```

### 💍 BODAS  (mismo patrón para comuniones / eventos / empresa)
```
- Hero con foto + titular
- Texto emocional (el original de "Una boda única", con sus estilos:
  romántica, vintage, civil, con carpa, otoñal...)
- Bloque "Sin límite de horario" destacado
- Galería específica de bodas
- FAQ rápida (3-4 preguntas top)
- CTA: "Pide presupuesto" / WhatsApp
```

### 🏞️ ESPACIOS
```
- Interior 150 pax (ventanales, vistas valle)
- Terraza-jardín sur con haima (cóctel/ceremonia/baile)
- Terraza oeste + chill-out
- Terraza de bienvenida (mirador al Larun)
- Cada espacio con foto + capacidad + uso recomendado
```

### 🍽️ GASTRONOMÍA (Mahercatering)
```
- Presentación del catering + premios reales
  (Madrid Fusión, Wedding Awards 2017, Gob. Navarra...)
- "Experience & Food"
- Tipos de menú + menús especiales (vegano, celíaco, diabético...)
- CTA: pedir dosier gastronómico
```

### 🖼️ GALERÍA
```
- Grid masonry con las 36 fotos (WebP, lazy-load)
- Lightbox al hacer clic
- (opcional) filtros: Bodas / Espacios / Entorno
```

### 📍 LOCALIZACIÓN
```
- Mapa Google embebido (GPS 43.304798, -1.679727)
- Cómo llegar: desde Bera (5km) o desde Urruña/Iparralde (6,5km)
- Distancias: Irun 15' · Donosti 30' · Pamplona 45'
- Botón "Abrir en Google Maps"
```

### 📞 CONTACTO
```
- Formulario (Nombre, Email, Asunto, Mensaje) → conectado a email real
- Botón WhatsApp grande
- 2 teléfonos clicables (tel:)
- NAP completo
```

---

## 4. Copy reescrito (manteniendo la esencia del original)

> Mantengo frases y tono del original (el cliente las eligió), solo afino titulares, añado CTAs y mejoro para SEO. No invento datos.

### Home — Hero
- **Titular:** *Bodas y eventos en plena naturaleza, en el valle del Baztan-Bidasoa*
- **Subtítulo:** *Un excepcional enclave natural en las alturas del valle encantado. Privacidad total, exteriores de ensueño y una celebración sin límite de horario.*
- **CTA:** `Cuéntanos tu idea` · `WhatsApp`

### Home — Frase ancla (original, se conserva)
> *"¿Cuántas cosas excepcionales suceden a las personas que queremos y que merezcan celebrarse? Muchísimas… Estamos seguros de que Okalarre es el lugar perfecto para celebrar al menos uno de esos acontecimientos tan especiales."*

### Bodas (se conserva el cuerpo original, nuevo titular + CTA)
- **Titular:** *Tu boda, como tú la imaginas — en un lugar único para vosotros*
- **Cuerpo:** el párrafo original de los estilos (romántica, vintage, civil, con carpa, otoñal, íntima…) + *"sin límite de horario"*.
- **CTA:** `Pide tu presupuesto sin compromiso`

### Okalarre / Presentación (texto original conservado)
> *"Vistas maravillosas, tranquilidad absoluta, aire puro, una construcción única con una gran terraza, jardín y un mirador envidiable… 15 años de experiencia avalan un proyecto donde los límites solo los pones tú."*

### Bloque "Por qué Okalarre" (nuevo, resume sus ventajas reales)
- 🔒 **Privacidad total** — sin vecinos, solo un evento al día
- 🕐 **Sin límite de horario** — la fiesta dura lo que queráis
- 🌿 **Naturaleza** — valle del Bidasoa, mirador al Larun
- 🍽️ **Catering propio premiado** — Mahercatering

*(Los textos EU y FR se reaprovechan de las páginas ya traducidas que extrajimos: `aurkezpena`, `presentation`, etc. No hay que retraducir desde cero.)*

---

## 5. Identidad visual propuesta

| Elemento | Propuesta | Por qué |
|---|---|---|
| **Estética** | Editorial / natural elegante | Encaja con bodas en naturaleza |
| **Paleta** | Verde salvia + crema/hueso + terracota suave + carbón (#2b2b2b para texto) | Tonos del valle y del original (#48484a) |
| **Tipografía** | Titulares serif elegante (Playfair Display — la que ya usaban) + cuerpo sans limpio (Inter / Open Sans) | Continuidad con la marca + legibilidad |
| **Fotografía** | Las 36 fotos profesionales a gran tamaño, protagonistas | Es lo mejor que tienen |
| **Animación** | Sutil: fade-in al scroll, parallax suave en heros (GSAP/CSS) | Sensación premium sin recargar |

---

## 6. Mejoras técnicas y SEO (lo que más mueve la aguja)

- ✅ **HTTPS** + dominio limpio (`fincaokalarre.com` con certificado)
- ✅ **Responsive real** mobile-first (las novias buscan desde el móvil)
- ✅ **Velocidad** — imágenes WebP optimizadas, lazy-load (Core Web Vitals en verde)
- ✅ **SEO local** — Schema markup `LocalBusiness` + `EventVenue`, ficha Google Business enlazada
- ✅ **hreflang** correcto ES/EU/FR (hoy lo hacen mal con `?lang=`)
- ✅ **Títulos/meta** por página orientados a búsqueda: *"Bodas en Navarra"*, *"Finca para bodas Bera Bidasoa"*, *"Espacio eventos Gipuzkoa"*
- ✅ **WhatsApp Business** como CTA principal
- ✅ **Formulario funcional** (Netlify Forms / Formspree) que llega a `info@fincaokalarre.com`
- ✅ **Google Maps** embebido + botón directo
- ✅ **Sitemap.xml + robots** nuevos
- 🔄 **Blog reactivado** como "Bodas reales" (cada boda celebrada = 1 post con fotos = SEO fresco)

---

## 7. Material disponible para construir (ya extraído)

- **43 páginas** de texto original en `/contenido` (ES·EU·FR + blog)
- **253 imágenes** descargadas (17,2 MB), incluidas las **36 fotos de galería**
- **NAP, GPS, premios y argumentario** completos y verificados
- Todo trilingüe ya traducido por el propio cliente → **reaprovechable**

---

## 8. Siguiente paso

Cuando valides esta propuesta, construyo la web en **Astro + Tailwind**, multipágina y trilingüe, con las 36 fotos integradas y lista para desplegar en Netlify. Tiempo estimado de primera versión navegable: rápido, porque el contenido y las imágenes ya están listos.

> ¿Ajustamos algo de la estructura, la paleta o el enfoque del copy antes de empezar a construir?

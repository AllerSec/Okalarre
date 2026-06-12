# -*- coding: utf-8 -*-
"""
Finca Okalarre — trilingual content store (ES / EU / FR).
Original copy preserved verbatim from the client's existing site.
Image references point to /assets/img/...
"""

# Shared business data (NAP)
BIZ = {
    "name": "Finca Okalarre",
    "tagline_es": "Bodas & Eventos",
    "phone1": "650 981 950",
    "phone2": "631 893 698",
    "phone1_tel": "+34650981950",
    "phone2_tel": "+34631893698",
    "whatsapp": "34650981950",
    "email": "info@fincaokalarre.com",
    "address": "Ctra. Ibardin · Elzaurdia s/n",
    "zip": "31780",
    "city": "Bera",
    "region": "Navarra",
    "country": "ES",
    "lat": "43.304798",
    "lng": "-1.679727",
    "domain": "https://fincaokalarre.com",
    "author_url": "https://unaxaller.com",
}

# Languages: code, html lang, label, folder ('' = root for ES)
LANGS = [
    {"code": "es", "html": "es", "label": "Español", "short": "ES", "dir": ""},
    {"code": "eu", "html": "eu", "label": "Euskara", "short": "EU", "dir": "eu/"},
    {"code": "fr", "html": "fr", "label": "Français", "short": "FR", "dir": "fr/"},
    {"code": "en", "html": "en", "label": "English", "short": "EN", "dir": "en/"},
]

# Per-language page slugs (file names). Key = canonical page id.
SLUGS = {
    "home":        {"es": "index",         "eu": "index",          "fr": "index",        "en": "index"},
    "okalarre":    {"es": "okalarre",      "eu": "okalarre",       "fr": "presentation", "en": "about"},
    "celebraciones":{"es":"celebraciones", "eu": "ospakizunak",    "fr": "celebrations", "en": "celebrations"},
    "bodas":       {"es": "bodas",         "eu": "ezkontzak",      "fr": "mariages",     "en": "weddings"},
    "comuniones":  {"es": "comuniones",    "eu": "jaunartzeak",    "fr": "communions",   "en": "communions"},
    "eventos":     {"es": "eventos",       "eu": "festa-pribatuak","fr": "evenements",   "en": "events"},
    "empresa":     {"es": "reuniones-empresa","eu":"enpresa-bilerak","fr":"reunions-entreprise","en":"corporate-events"},
    "espacios":    {"es": "espacios",      "eu": "espazioak",      "fr": "espaces",      "en": "spaces"},
    "gastronomia": {"es": "gastronomia",   "eu": "gastronomia",    "fr": "gastronomie",  "en": "gastronomy"},
    "galeria":     {"es": "galeria",       "eu": "galeria",        "fr": "galerie",      "en": "gallery"},
    "localizacion":{"es": "localizacion",  "eu": "kokapena",       "fr": "localisation", "en": "location"},
    "faq":         {"es": "preguntas-frecuentes","eu":"ohiko-galderak","fr":"questions-frequentes","en":"faq"},
    "contacto":    {"es": "contacto",      "eu": "harremanetarako","fr": "contact",      "en": "contact"},
    "aviso-legal": {"es": "aviso-legal",   "eu": "lege-oharra",    "fr": "mentions-legales","en":"legal-notice"},
    "privacidad":  {"es": "privacidad",    "eu": "pribatutasuna",  "fr": "confidentialite","en":"privacy"},
    "cookies":     {"es": "cookies",       "eu": "cookieak",       "fr": "cookies",      "en": "cookies"},
}

# Navigation labels per language
NAV = {
    "es": {"home":"Inicio","okalarre":"Okalarre","celebraciones":"Celebraciones","bodas":"Bodas",
           "comuniones":"Comuniones","eventos":"Eventos","empresa":"Reuniones de empresa",
           "espacios":"Espacios","gastronomia":"Gastronomía","galeria":"Galería",
           "localizacion":"Localización","faq":"Preguntas frecuentes","contacto":"Contacto"},
    "eu": {"home":"Hasiera","okalarre":"Okalarre","celebraciones":"Ospakizunak","bodas":"Ezkontzak",
           "comuniones":"Jaunartzeak","eventos":"Festa pribatuak","empresa":"Enpresa bilerak",
           "espacios":"Espazioak","gastronomia":"Gastronomia","galeria":"Galeria",
           "localizacion":"Kokapena","faq":"Ohiko galderak","contacto":"Harremanetarako"},
    "fr": {"home":"Accueil","okalarre":"Présentation","celebraciones":"Célébrations","bodas":"Mariages",
           "comuniones":"Communions","eventos":"Événements","empresa":"Réunions d'entreprise",
           "espacios":"Espaces","gastronomia":"Gastronomie","galeria":"Galerie",
           "localizacion":"Localisation","faq":"Questions fréquentes","contacto":"Contact"},
    "en": {"home":"Home","okalarre":"Okalarre","celebraciones":"Celebrations","bodas":"Weddings",
           "comuniones":"Communions","eventos":"Events","empresa":"Corporate events",
           "espacios":"Spaces","gastronomia":"Gastronomy","galeria":"Gallery",
           "localizacion":"Location","faq":"FAQ","contacto":"Contact"},
}

# UI strings
UI = {
    "es": {
        "skip":"Saltar al contenido", "menu":"Menú", "close":"Cerrar",
        "cta_idea":"Cuéntanos tu idea", "cta_quote":"Pide presupuesto", "whatsapp":"WhatsApp",
        "view_spaces":"Ver espacios", "view_gallery":"Ver galería completa", "discover":"Descubrir",
        "scroll":"Desliza", "celebrations":"Celebraciones", "explore":"Explorar",
        "why_title":"Por qué Okalarre", "send":"Enviar mensaje", "sending":"Enviando…",
        "form_ok":"¡Gracias! Te responderemos muy pronto.",
        "form_err":"No se pudo enviar. Escríbenos a info@fincaokalarre.com",
        "name":"Nombre","email":"E-mail","subject":"Asunto","message":"Mensaje",
        "required":"Todos los campos marcados son obligatorios.",
        "open_maps":"Abrir en Google Maps","how_arrive":"Cómo llegar","call":"Llamar",
        "footer_explore":"Explorar","footer_celebrate":"Celebraciones","footer_contact":"Contacto","footer_legal":"Legal",
        "rights":"Todos los derechos reservados","designed":"Diseñado por",
        "back_home":"Volver al inicio","err_title":"Página no encontrada",
        "err_text":"Lo sentimos, la página que buscas se ha perdido entre las montañas del Bidasoa.",
        "ph_celebrations":"Cada celebración, un mundo propio. Elige el tuyo.",
    },
    "eu": {
        "skip":"Edukira jauzi", "menu":"Menua", "close":"Itxi",
        "cta_idea":"Kontaiguzu zure ideia", "cta_quote":"Eskatu aurrekontua", "whatsapp":"WhatsApp",
        "view_spaces":"Ikusi espazioak", "view_gallery":"Ikusi galeria osoa", "discover":"Ezagutu",
        "scroll":"Lerratu", "celebrations":"Ospakizunak", "explore":"Arakatu",
        "why_title":"Zergatik Okalarre", "send":"Bidali mezua", "sending":"Bidaltzen…",
        "form_ok":"Eskerrik asko! Laster erantzungo dizugu.",
        "form_err":"Ezin izan da bidali. Idatzi info@fincaokalarre.com helbidera",
        "name":"Izena","email":"E-maila","subject":"Gaia","message":"Mezua",
        "required":"Markatutako eremu guztiak derrigorrezkoak dira.",
        "open_maps":"Ireki Google Maps-en","how_arrive":"Nola iritsi","call":"Deitu",
        "footer_explore":"Arakatu","footer_celebrate":"Ospakizunak","footer_contact":"Harremanetarako","footer_legal":"Legezkoa",
        "rights":"Eskubide guztiak erreserbatuta","designed":"Diseinatzailea:",
        "back_home":"Itzuli hasierara","err_title":"Orria ez da aurkitu",
        "err_text":"Sentitzen dugu, bilatzen ari zaren orria Bidasoako mendien artean galdu da.",
        "ph_celebrations":"Ospakizun bakoitza, mundu bat. Aukeratu zurea.",
    },
    "fr": {
        "skip":"Aller au contenu", "menu":"Menu", "close":"Fermer",
        "cta_idea":"Parlez-nous de votre projet", "cta_quote":"Demander un devis", "whatsapp":"WhatsApp",
        "view_spaces":"Voir les espaces", "view_gallery":"Voir toute la galerie", "discover":"Découvrir",
        "scroll":"Défiler", "celebrations":"Célébrations", "explore":"Explorer",
        "why_title":"Pourquoi Okalarre", "send":"Envoyer le message", "sending":"Envoi…",
        "form_ok":"Merci ! Nous vous répondrons très vite.",
        "form_err":"Envoi impossible. Écrivez-nous à info@fincaokalarre.com",
        "name":"Nom","email":"E-mail","subject":"Objet","message":"Message",
        "required":"Tous les champs marqués sont obligatoires.",
        "open_maps":"Ouvrir dans Google Maps","how_arrive":"Comment venir","call":"Appeler",
        "footer_explore":"Explorer","footer_celebrate":"Célébrations","footer_contact":"Contact","footer_legal":"Légal",
        "rights":"Tous droits réservés","designed":"Conçu par",
        "back_home":"Retour à l'accueil","err_title":"Page introuvable",
        "err_text":"Désolé, la page que vous cherchez s'est perdue dans les montagnes de la Bidassoa.",
        "ph_celebrations":"Chaque célébration, un monde. Choisissez le vôtre.",
    },
    "en": {
        "skip":"Skip to content", "menu":"Menu", "close":"Close",
        "cta_idea":"Tell us your idea", "cta_quote":"Request a quote", "whatsapp":"WhatsApp",
        "view_spaces":"View spaces", "view_gallery":"View full gallery", "discover":"Discover",
        "scroll":"Scroll", "celebrations":"Celebrations", "explore":"Explore",
        "why_title":"Why Okalarre", "send":"Send message", "sending":"Sending…",
        "form_ok":"Thank you! We'll get back to you very soon.",
        "form_err":"Couldn't send. Please email us at info@fincaokalarre.com",
        "name":"Name","email":"E-mail","subject":"Subject","message":"Message",
        "required":"All marked fields are required.",
        "open_maps":"Open in Google Maps","how_arrive":"How to get here","call":"Call",
        "footer_explore":"Explore","footer_celebrate":"Celebrations","footer_contact":"Contact","footer_legal":"Legal",
        "rights":"All rights reserved","designed":"Designed by",
        "back_home":"Back to home","err_title":"Page not found",
        "err_text":"Sorry, the page you're looking for got lost among the mountains of the Bidasoa.",
        "ph_celebrations":"Every celebration, a world of its own. Choose yours.",
    },
}

# ---- Why-Okalarre feature blocks (4) ----
WHY = {
    "es":[("privacy","Privacidad total","Sin vecinos: un solo evento al día, solo para vosotros."),
          ("clock","Sin límite de horario","La fiesta dura exactamente lo que vosotros queráis."),
          ("leaf","Naturaleza pura","Valle del Bidasoa, con mirador al monte Larun."),
          ("plate","Catering propio premiado","Mahercatering, gastronomía de vanguardia.")],
    "eu":[("privacy","Erabateko pribatutasuna","Auzokorik gabe: egunean ekitaldi bakarra, zuentzat soilik."),
          ("clock","Ordutegi mugarik gabe","Festak zuek nahi duzuena iraungo du, zehazki."),
          ("leaf","Natura hutsa","Bidasoa harana, Larun mendira begira."),
          ("plate","Catering propio saritua","Mahercatering, abangoardiako gastronomia.")],
    "fr":[("privacy","Intimité totale","Sans voisins : un seul événement par jour, rien que pour vous."),
          ("clock","Sans limite d'horaire","La fête dure exactement le temps que vous voulez."),
          ("leaf","Nature pure","Vallée de la Bidassoa, avec vue sur le mont Larun."),
          ("plate","Traiteur maison primé","Mahercatering, gastronomie d'avant-garde.")],
    "en":[("privacy","Total privacy","No neighbours: one single event per day, just for you."),
          ("clock","No time limit","The party lasts exactly as long as you want it to."),
          ("leaf","Pure nature","Bidasoa valley, overlooking Mount Larun."),
          ("plate","Award-winning in-house catering","Mahercatering, avant-garde cuisine.")],
}

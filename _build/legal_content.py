# -*- coding: utf-8 -*-
"""Legal pages (Spain): Aviso legal (LSSI-CE), Privacidad (RGPD/LOPDGDD), Cookies.
Structure: LEGAL_TEXT[kind][lang] = list of (h2, [paragraphs])."""

_TITULAR = "Finca Okalarre"
_DOMINIO = "fincaokalarre.com"
_EMAIL = "info@fincaokalarre.com"
_DIR = "Ctra. Ibardin, Elzaurdia s/n, 31780 Bera (Navarra)"

LEGAL_TEXT = {
"aviso-legal": {
 "es":[
  ("Datos identificativos",[f"En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de la Sociedad de la Información y Comercio Electrónico (LSSI-CE), se informa de que este sitio web ({_DOMINIO}) es titularidad de {_TITULAR}, con domicilio en {_DIR} y correo electrónico de contacto <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Objeto",["El presente aviso legal regula el uso del sitio web, cuyo objeto es ofrecer información sobre los servicios de celebración de bodas, comuniones, eventos privados y reuniones de empresa, así como facilitar el contacto con la finca."]),
  ("Condiciones de uso",["El acceso y la navegación por este sitio implican la aceptación de las presentes condiciones. El usuario se compromete a hacer un uso adecuado de los contenidos y a no emplearlos para actividades ilícitas o contrarias a la buena fe."]),
  ("Propiedad intelectual",["Todos los contenidos del sitio (textos, fotografías, logotipos, diseño y código) son titularidad de Finca Okalarre o de terceros que han autorizado su uso, y están protegidos por la normativa de propiedad intelectual e industrial. Queda prohibida su reproducción total o parcial sin autorización."]),
  ("Responsabilidad",["Finca Okalarre no se responsabiliza de los daños derivados del uso del sitio ni de la presencia de virus u otros elementos lesivos que pudieran causar alteraciones en los sistemas informáticos del usuario."]),
  ("Legislación aplicable",["Las presentes condiciones se rigen por la legislación española. Para la resolución de cualquier controversia, las partes se someten a los juzgados y tribunales del domicilio del titular, salvo que la ley disponga otra cosa."]),
 ],
 "eu":[
  ("Identifikazio-datuak",[f"Informazioaren Gizartearen eta Merkataritza Elektronikoaren Zerbitzuei buruzko 34/2002 Legearen (LSSI-CE) 10. artikulua betez, jakinarazten da webgune honen ({_DOMINIO}) titularra {_TITULAR} dela, {_DIR} helbidean, eta harremanetarako helbide elektronikoa <a href='mailto:{_EMAIL}'>{_EMAIL}</a> dela."]),
  ("Xedea",["Lege-ohar honek webgunearen erabilera arautzen du, zeinaren xedea ezkontza, jaunartze, festa pribatu eta enpresa bileren ospakizun-zerbitzuei buruzko informazioa eskaintzea baita."]),
  ("Erabilera-baldintzak",["Webgunera sartzeak eta nabigatzeak baldintza hauek onartzea dakar. Erabiltzaileak edukien erabilera egokia egiteko konpromisoa hartzen du."]),
  ("Jabetza intelektuala",["Webguneko eduki guztiak (testuak, argazkiak, logotipoak, diseinua eta kodea) Finca Okalarreren edo erabilera baimendu duten hirugarrenen titulartasunekoak dira, eta jabetza intelektual eta industrialaren araudiak babesten ditu."]),
  ("Erantzukizuna",["Finca Okalarre ez da webgunearen erabileratik eratorritako kalteen erantzule."]),
  ("Lege aplikagarria",["Baldintza hauek Espainiako legediaren arabera arautzen dira."]),
 ],
 "fr":[
  ("Données d'identification",[f"Conformément à l'article 10 de la loi 34/2002 relative aux services de la société de l'information (LSSI-CE), il est précisé que ce site web ({_DOMINIO}) appartient à {_TITULAR}, domicilié à {_DIR}, e-mail de contact <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Objet",["Les présentes mentions légales régissent l'utilisation du site, dont l'objet est d'offrir des informations sur les services de célébration de mariages, communions, fêtes privées et réunions d'entreprise."]),
  ("Conditions d'utilisation",["L'accès et la navigation sur ce site impliquent l'acceptation des présentes conditions. L'utilisateur s'engage à faire un usage approprié des contenus."]),
  ("Propriété intellectuelle",["Tous les contenus du site (textes, photographies, logos, design et code) appartiennent à Finca Okalarre ou à des tiers ayant autorisé leur usage, et sont protégés par la réglementation sur la propriété intellectuelle et industrielle."]),
  ("Responsabilité",["Finca Okalarre n'est pas responsable des dommages résultant de l'utilisation du site."]),
  ("Législation applicable",["Les présentes conditions sont régies par la législation espagnole."]),
 ],
 "en":[
  ("Identification details",[f"In compliance with article 10 of Law 34/2002 on Information Society Services and Electronic Commerce (LSSI-CE), it is hereby stated that this website ({_DOMINIO}) is owned by {_TITULAR}, with registered address at {_DIR} and contact email <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Purpose",["These legal terms govern the use of the website, whose purpose is to provide information about wedding, communion, private event and corporate meeting services, as well as to facilitate contact with the estate."]),
  ("Terms of use",["Accessing and browsing this site implies acceptance of these terms. The user agrees to make appropriate use of the content and not to use it for unlawful purposes or those contrary to good faith."]),
  ("Intellectual property",["All site content (texts, photographs, logos, design and code) is owned by Finca Okalarre or by third parties who have authorised its use, and is protected by intellectual and industrial property regulations. Total or partial reproduction without authorisation is prohibited."]),
  ("Liability",["Finca Okalarre is not liable for damages arising from the use of the site or from the presence of viruses or other harmful elements that could alter the user's computer systems."]),
  ("Applicable law",["These terms are governed by Spanish law. For the resolution of any dispute, the parties submit to the courts of the owner's domicile, unless the law provides otherwise."]),
 ],
},
"privacidad": {
 "es":[
  ("Responsable del tratamiento",[f"{_TITULAR} es responsable del tratamiento de los datos personales facilitados a través de este sitio web. Domicilio: {_DIR}. Contacto: <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Finalidad",["Los datos que nos facilitas a través del formulario de contacto se tratan con la finalidad de atender tu consulta o solicitud de información sobre nuestros servicios y, en su caso, elaborar un presupuesto."]),
  ("Legitimación",["La base legal es tu consentimiento, otorgado al enviar el formulario, conforme al Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD)."]),
  ("Conservación",["Conservaremos tus datos durante el tiempo necesario para atender tu solicitud y, posteriormente, durante los plazos legalmente exigibles."]),
  ("Destinatarios",["No se cederán datos a terceros salvo obligación legal. Los servidores de envío de formularios pueden tratar los datos como encargados del tratamiento bajo las debidas garantías."]),
  ("Derechos",[f"Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href='mailto:{_EMAIL}'>{_EMAIL}</a>. También puedes presentar una reclamación ante la Agencia Española de Protección de Datos (aepd.es)."]),
 ],
 "eu":[
  ("Tratamenduaren arduraduna",[f"{_TITULAR} da webgune honen bidez emandako datu pertsonalen tratamenduaren arduraduna. Helbidea: {_DIR}. Kontaktua: <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Helburua",["Harremanetarako formularioaren bidez ematen dizkiguzun datuak zure kontsulta edo informazio-eskaera erantzuteko helburuarekin tratatzen dira."]),
  ("Legitimazioa",["Oinarri legala zure baimena da, formularioa bidaltzean emana, 2016/679 (EB) Erregelamenduaren (RGPD) eta 3/2018 Lege Organikoaren (LOPDGDD) arabera."]),
  ("Kontserbazioa",["Zure datuak eskaera erantzuteko beharrezkoa den denboran gordeko ditugu."]),
  ("Hartzaileak",["Ez zaizkie datuak hirugarrenei lagako, lege-betebeharra denean izan ezik."]),
  ("Eskubideak",[f"Sarbide, zuzenketa, ezabatze, aurkaratze, mugatze eta eramangarritasun eskubideak balia ditzakezu <a href='mailto:{_EMAIL}'>{_EMAIL}</a> helbidera idatziz."]),
 ],
 "fr":[
  ("Responsable du traitement",[f"{_TITULAR} est responsable du traitement des données personnelles fournies via ce site. Adresse : {_DIR}. Contact : <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Finalité",["Les données que vous nous fournissez via le formulaire de contact sont traitées dans le but de répondre à votre demande d'information sur nos services et, le cas échéant, d'établir un devis."]),
  ("Base légale",["La base légale est votre consentement, donné lors de l'envoi du formulaire, conformément au Règlement (UE) 2016/679 (RGPD) et à la loi organique 3/2018 (LOPDGDD)."]),
  ("Conservation",["Nous conserverons vos données pendant le temps nécessaire pour traiter votre demande."]),
  ("Destinataires",["Aucune donnée ne sera cédée à des tiers, sauf obligation légale."]),
  ("Droits",[f"Vous pouvez exercer vos droits d'accès, de rectification, de suppression, d'opposition, de limitation et de portabilité en écrivant à <a href='mailto:{_EMAIL}'>{_EMAIL}</a>. Vous pouvez aussi déposer une réclamation auprès de l'Agence Espagnole de Protection des Données (aepd.es)."]),
 ],
 "en":[
  ("Data controller",[f"{_TITULAR} is the controller of the personal data provided through this website. Address: {_DIR}. Contact: <a href='mailto:{_EMAIL}'>{_EMAIL}</a>."]),
  ("Purpose",["The data you provide through the contact form is processed in order to handle your enquiry or request for information about our services and, where applicable, to prepare a quote."]),
  ("Legal basis",["The legal basis is your consent, given when you submit the form, in accordance with Regulation (EU) 2016/679 (GDPR) and Organic Law 3/2018 (LOPDGDD)."]),
  ("Retention",["We will keep your data for the time necessary to handle your request and, afterwards, for the legally required periods."]),
  ("Recipients",["No data will be transferred to third parties except by legal obligation. Form-delivery servers may process the data as processors under the appropriate safeguards."]),
  ("Your rights",[f"You can exercise your rights of access, rectification, erasure, objection, restriction and portability by writing to <a href='mailto:{_EMAIL}'>{_EMAIL}</a>. You may also file a complaint with the Spanish Data Protection Agency (aepd.es)."]),
 ],
},
"cookies": {
 "es":[
  ("¿Qué son las cookies?",["Una cookie es un pequeño archivo que se descarga en tu dispositivo al acceder a determinadas páginas web, y que permite almacenar y recuperar información sobre la navegación."]),
  ("Cookies que utilizamos",["Este sitio es estático y no utiliza cookies de seguimiento ni de publicidad propias. Únicamente puede emplearse almacenamiento local del navegador para recordar tu preferencia de idioma y mostrar la pantalla de bienvenida una sola vez por sesión."]),
  ("Servicios de terceros",["El mapa de localización se carga desde Google Maps, que puede instalar cookies propias. Puedes consultar su política en policies.google.com. El botón de WhatsApp abre la aplicación o el sitio de WhatsApp."]),
  ("Gestión de cookies",["Puedes configurar o eliminar las cookies y el almacenamiento local desde las opciones de tu navegador en cualquier momento."]),
 ],
 "eu":[
  ("Zer dira cookieak?",["Cookie bat fitxategi txiki bat da, web orri jakin batzuetara sartzean zure gailuan deskargatzen dena, eta nabigazioari buruzko informazioa gordetzeko aukera ematen duena."]),
  ("Erabiltzen ditugun cookieak",["Webgune hau estatikoa da eta ez du jarraipen edo publizitate cookierik erabiltzen. Nabigatzailearen biltegiratze lokala soilik erabil daiteke zure hizkuntza-lehentasuna gogoratzeko."]),
  ("Hirugarrenen zerbitzuak",["Kokapen-mapa Google Maps-etik kargatzen da, bere cookieak instala ditzakeena. WhatsApp botoiak aplikazioa irekitzen du."]),
  ("Cookien kudeaketa",["Cookieak eta biltegiratze lokala konfiguratu edo ezaba ditzakezu zure nabigatzailearen aukeretatik."]),
 ],
 "fr":[
  ("Que sont les cookies ?",["Un cookie est un petit fichier téléchargé sur votre appareil lors de l'accès à certaines pages web, qui permet de stocker et de récupérer des informations sur la navigation."]),
  ("Cookies que nous utilisons",["Ce site est statique et n'utilise pas de cookies de suivi ni de publicité propres. Seul le stockage local du navigateur peut être utilisé pour mémoriser votre préférence de langue."]),
  ("Services tiers",["La carte de localisation est chargée depuis Google Maps, qui peut installer ses propres cookies. Le bouton WhatsApp ouvre l'application WhatsApp."]),
  ("Gestion des cookies",["Vous pouvez configurer ou supprimer les cookies et le stockage local depuis les options de votre navigateur à tout moment."]),
 ],
 "en":[
  ("What are cookies?",["A cookie is a small file downloaded to your device when you access certain web pages, allowing information about your browsing to be stored and retrieved."]),
  ("Cookies we use",["This site is static and does not use its own tracking or advertising cookies. Only the browser's local storage may be used to remember your language preference and show the welcome screen once per session."]),
  ("Third-party services",["The location map is loaded from Google Maps, which may set its own cookies. You can review its policy at policies.google.com. The WhatsApp button opens the WhatsApp app or website."]),
  ("Managing cookies",["You can configure or delete cookies and local storage from your browser options at any time."]),
 ],
},
}

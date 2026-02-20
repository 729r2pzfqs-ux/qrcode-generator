#!/usr/bin/env python3
"""Generate educational articles for qrcodes.win in 11 languages."""

import os

LANGUAGES = ['en', 'es', 'de', 'fr', 'pt', 'zh', 'ja', 'ar', 'hi', 'ru', 'tr']

# Article 1: How QR Codes Work
HOW_QR_WORKS = {
    'en': {
        'title': 'How QR Codes Work | The Technology Explained Simply',
        'meta': 'Learn how QR codes work, from scanning to decoding. Understand the technology behind those square patterns and why they\'re so reliable.',
        'h1': 'How QR Codes Work',
        'subtitle': 'The fascinating technology behind those black and white squares',
        'intro': 'You scan them every day — at restaurants, on products, in ads. But have you ever wondered <strong>how QR codes actually work</strong>? Let\'s break down the technology in simple terms.',
        'what_title': 'What is a QR Code?',
        'what_text': 'QR stands for <strong>Quick Response</strong>. It\'s a type of 2D barcode invented in 1994 by a Japanese company called Denso Wave. Unlike traditional barcodes that only hold data horizontally, QR codes store information both horizontally and vertically — allowing them to hold much more data.',
        'what_capacity': 'A single QR code can store up to <strong>3,000 characters</strong> of text, compared to just 20-25 characters in a traditional barcode.',
        'anatomy_title': 'Anatomy of a QR Code',
        'anatomy_intro': 'Every QR code has these key components:',
        'anatomy_1_title': 'Finder Patterns (Big Squares)',
        'anatomy_1': 'The three large squares in the corners help scanners quickly locate and orient the QR code, even at an angle.',
        'anatomy_2_title': 'Alignment Pattern',
        'anatomy_2': 'The smaller square helps with accurate reading, especially on curved surfaces.',
        'anatomy_3_title': 'Timing Patterns',
        'anatomy_3': 'Alternating black and white modules that help determine the size of the data grid.',
        'anatomy_4_title': 'Data Area',
        'anatomy_4': 'The scrambled-looking pattern in the middle — this is where your actual information is encoded.',
        'anatomy_5_title': 'Quiet Zone',
        'anatomy_5': 'The white border around the code that helps scanners distinguish the QR code from its surroundings.',
        'how_scan_title': 'How Scanning Works',
        'how_scan_steps': [
            '<strong>Image Capture:</strong> Your phone\'s camera takes a picture of the QR code',
            '<strong>Pattern Detection:</strong> Software finds the three finder patterns to locate and orient the code',
            '<strong>Grid Mapping:</strong> The scanner creates a grid over the image, identifying each black/white module',
            '<strong>Data Extraction:</strong> Black modules = 1, white modules = 0 — creating binary data',
            '<strong>Error Correction:</strong> The scanner uses Reed-Solomon error correction to fix any damaged parts',
            '<strong>Decoding:</strong> Binary data is converted to readable text, URLs, or other formats'
        ],
        'error_title': 'Error Correction: Why Damaged QR Codes Still Work',
        'error_text': 'QR codes have built-in redundancy. Even if part of the code is damaged, scratched, or covered, it can still be read. There are four error correction levels:',
        'error_levels': [
            '<strong>L (Low):</strong> ~7% of code can be restored',
            '<strong>M (Medium):</strong> ~15% can be restored',
            '<strong>Q (Quartile):</strong> ~25% can be restored',
            '<strong>H (High):</strong> ~30% can be restored — this is why you can put logos in the center!'
        ],
        'types_title': 'What Can QR Codes Store?',
        'types': ['Website URLs', 'Plain text', 'Contact information (vCard)', 'WiFi network credentials', 'Phone numbers', 'Email addresses', 'GPS coordinates', 'Calendar events', 'App store links'],
        'static_dynamic_title': 'Static vs Dynamic QR Codes',
        'static_title': 'Static QR Codes',
        'static_text': 'The data is encoded directly in the pattern. Once created, it cannot be changed. Free to create, works forever.',
        'dynamic_title': 'Dynamic QR Codes',
        'dynamic_text': 'The code points to a redirect URL. You can change the destination anytime, track scans, and gather analytics. Requires a paid service.',
        'why_popular_title': 'Why QR Codes Became So Popular',
        'why_popular': [
            '<strong>Contactless:</strong> COVID-19 accelerated adoption for touchless menus and payments',
            '<strong>Smartphone cameras:</strong> No app needed — built into iOS and Android since 2017',
            '<strong>Free to create:</strong> Anyone can generate QR codes instantly',
            '<strong>Versatile:</strong> Works for URLs, text, WiFi, contacts, and more',
            '<strong>Reliable:</strong> Error correction means they work even when partially damaged'
        ],
        'fun_facts_title': 'Fun Facts',
        'fun_facts': [
            'The largest QR code ever made was 2.1 km² (created in a Chinese wheat field)',
            'QR codes were originally invented to track car parts in manufacturing',
            'The patent for QR codes is owned by Denso Wave, but they don\'t exercise it — keeping the technology free',
            'A QR code must have a minimum "quiet zone" of 4 modules around it to scan properly'
        ],
        'cta_title': 'Create Your Own QR Code',
        'cta_text': 'Now that you know how they work, create your own QR code for free — no signup required.',
        'cta_button': 'Create QR Code →',
        'back': '← Back',
        'lang_name': 'English',
    },
    'de': {
        'title': 'Wie QR-Codes funktionieren | Die Technologie einfach erklärt',
        'meta': 'Erfahren Sie, wie QR-Codes funktionieren, vom Scannen bis zur Dekodierung. Verstehen Sie die Technologie hinter diesen quadratischen Mustern.',
        'h1': 'Wie QR-Codes funktionieren',
        'subtitle': 'Die faszinierende Technologie hinter den schwarz-weißen Quadraten',
        'intro': 'Sie scannen sie jeden Tag — in Restaurants, auf Produkten, in Werbung. Aber haben Sie sich jemals gefragt, <strong>wie QR-Codes tatsächlich funktionieren</strong>? Lassen Sie uns die Technologie einfach erklären.',
        'what_title': 'Was ist ein QR-Code?',
        'what_text': 'QR steht für <strong>Quick Response</strong> (Schnelle Antwort). Es ist eine Art 2D-Barcode, der 1994 von der japanischen Firma Denso Wave erfunden wurde. Anders als traditionelle Barcodes, die Daten nur horizontal speichern, speichern QR-Codes Informationen horizontal und vertikal — was ihnen ermöglicht, viel mehr Daten zu speichern.',
        'what_capacity': 'Ein einzelner QR-Code kann bis zu <strong>3.000 Zeichen</strong> Text speichern, verglichen mit nur 20-25 Zeichen bei einem traditionellen Barcode.',
        'anatomy_title': 'Anatomie eines QR-Codes',
        'anatomy_intro': 'Jeder QR-Code hat diese Hauptkomponenten:',
        'anatomy_1_title': 'Positionsmarkierungen (Große Quadrate)',
        'anatomy_1': 'Die drei großen Quadrate in den Ecken helfen Scannern, den QR-Code schnell zu finden und auszurichten.',
        'anatomy_2_title': 'Ausrichtungsmuster',
        'anatomy_2': 'Das kleinere Quadrat hilft beim genauen Lesen, besonders auf gekrümmten Oberflächen.',
        'anatomy_3_title': 'Timing-Muster',
        'anatomy_3': 'Abwechselnde schwarze und weiße Module, die die Größe des Datenrasters bestimmen.',
        'anatomy_4_title': 'Datenbereich',
        'anatomy_4': 'Das verschlüsselt aussehende Muster in der Mitte — hier sind Ihre tatsächlichen Informationen kodiert.',
        'anatomy_5_title': 'Ruhezone',
        'anatomy_5': 'Der weiße Rand um den Code, der Scannern hilft, den QR-Code von seiner Umgebung zu unterscheiden.',
        'how_scan_title': 'Wie das Scannen funktioniert',
        'how_scan_steps': [
            '<strong>Bildaufnahme:</strong> Die Kamera Ihres Handys macht ein Foto des QR-Codes',
            '<strong>Mustererkennung:</strong> Software findet die drei Positionsmarkierungen zur Lokalisierung',
            '<strong>Rasterzuordnung:</strong> Der Scanner erstellt ein Raster über das Bild',
            '<strong>Datenextraktion:</strong> Schwarze Module = 1, weiße Module = 0 — erzeugt Binärdaten',
            '<strong>Fehlerkorrektur:</strong> Der Scanner verwendet Reed-Solomon-Fehlerkorrektur',
            '<strong>Dekodierung:</strong> Binärdaten werden in lesbaren Text oder URLs umgewandelt'
        ],
        'error_title': 'Fehlerkorrektur: Warum beschädigte QR-Codes noch funktionieren',
        'error_text': 'QR-Codes haben eingebaute Redundanz. Selbst wenn ein Teil des Codes beschädigt oder verdeckt ist, kann er noch gelesen werden. Es gibt vier Fehlerkorrekturstufen:',
        'error_levels': [
            '<strong>L (Niedrig):</strong> ~7% des Codes können wiederhergestellt werden',
            '<strong>M (Mittel):</strong> ~15% können wiederhergestellt werden',
            '<strong>Q (Quartil):</strong> ~25% können wiederhergestellt werden',
            '<strong>H (Hoch):</strong> ~30% können wiederhergestellt werden — deshalb können Sie Logos in die Mitte setzen!'
        ],
        'types_title': 'Was können QR-Codes speichern?',
        'types': ['Website-URLs', 'Einfacher Text', 'Kontaktinformationen (vCard)', 'WLAN-Zugangsdaten', 'Telefonnummern', 'E-Mail-Adressen', 'GPS-Koordinaten', 'Kalendertermine', 'App-Store-Links'],
        'static_dynamic_title': 'Statische vs Dynamische QR-Codes',
        'static_title': 'Statische QR-Codes',
        'static_text': 'Die Daten sind direkt im Muster kodiert. Einmal erstellt, können sie nicht geändert werden. Kostenlos zu erstellen, funktioniert für immer.',
        'dynamic_title': 'Dynamische QR-Codes',
        'dynamic_text': 'Der Code verweist auf eine Weiterleitungs-URL. Sie können das Ziel jederzeit ändern und Scans verfolgen. Erfordert einen kostenpflichtigen Dienst.',
        'why_popular_title': 'Warum QR-Codes so beliebt wurden',
        'why_popular': [
            '<strong>Kontaktlos:</strong> COVID-19 beschleunigte die Nutzung für berührungslose Menüs und Zahlungen',
            '<strong>Smartphone-Kameras:</strong> Keine App nötig — seit 2017 in iOS und Android integriert',
            '<strong>Kostenlos:</strong> Jeder kann QR-Codes sofort erstellen',
            '<strong>Vielseitig:</strong> Funktioniert für URLs, Text, WLAN, Kontakte und mehr',
            '<strong>Zuverlässig:</strong> Fehlerkorrektur bedeutet, dass sie auch beschädigt funktionieren'
        ],
        'fun_facts_title': 'Interessante Fakten',
        'fun_facts': [
            'Der größte QR-Code war 2,1 km² (in einem chinesischen Weizenfeld erstellt)',
            'QR-Codes wurden ursprünglich erfunden, um Autoteile in der Fertigung zu verfolgen',
            'Das Patent für QR-Codes gehört Denso Wave, aber sie nutzen es nicht — die Technologie bleibt kostenlos',
            'Ein QR-Code braucht mindestens 4 Module "Ruhezone" um ihn herum'
        ],
        'cta_title': 'Erstellen Sie Ihren eigenen QR-Code',
        'cta_text': 'Jetzt, da Sie wissen, wie sie funktionieren, erstellen Sie kostenlos Ihren eigenen QR-Code.',
        'cta_button': 'QR-Code erstellen →',
        'back': '← Zurück',
        'lang_name': 'Deutsch',
    },
    'es': {
        'title': 'Cómo Funcionan los Códigos QR | La Tecnología Explicada',
        'meta': 'Aprende cómo funcionan los códigos QR, desde el escaneo hasta la decodificación. Entiende la tecnología detrás de esos patrones cuadrados.',
        'h1': 'Cómo Funcionan los Códigos QR',
        'subtitle': 'La fascinante tecnología detrás de esos cuadrados blancos y negros',
        'intro': 'Los escaneas todos los días — en restaurantes, productos, anuncios. ¿Pero alguna vez te preguntaste <strong>cómo funcionan realmente los códigos QR</strong>? Vamos a explicar la tecnología de forma simple.',
        'what_title': '¿Qué es un Código QR?',
        'what_text': 'QR significa <strong>Quick Response</strong> (Respuesta Rápida). Es un tipo de código de barras 2D inventado en 1994 por una empresa japonesa llamada Denso Wave. A diferencia de los códigos de barras tradicionales que solo almacenan datos horizontalmente, los códigos QR almacenan información horizontal y verticalmente — permitiéndoles almacenar mucha más información.',
        'what_capacity': 'Un solo código QR puede almacenar hasta <strong>3,000 caracteres</strong> de texto, comparado con solo 20-25 caracteres en un código de barras tradicional.',
        'anatomy_title': 'Anatomía de un Código QR',
        'anatomy_intro': 'Cada código QR tiene estos componentes clave:',
        'anatomy_1_title': 'Patrones de Posición (Cuadrados Grandes)',
        'anatomy_1': 'Los tres cuadrados grandes en las esquinas ayudan a los escáneres a localizar y orientar rápidamente el código QR.',
        'anatomy_2_title': 'Patrón de Alineación',
        'anatomy_2': 'El cuadrado más pequeño ayuda con la lectura precisa, especialmente en superficies curvas.',
        'anatomy_3_title': 'Patrones de Tiempo',
        'anatomy_3': 'Módulos alternos blancos y negros que determinan el tamaño de la cuadrícula de datos.',
        'anatomy_4_title': 'Área de Datos',
        'anatomy_4': 'El patrón revuelto en el medio — aquí es donde tu información real está codificada.',
        'anatomy_5_title': 'Zona Silenciosa',
        'anatomy_5': 'El borde blanco alrededor del código que ayuda a los escáneres a distinguir el código QR de su entorno.',
        'how_scan_title': 'Cómo Funciona el Escaneo',
        'how_scan_steps': [
            '<strong>Captura de Imagen:</strong> La cámara de tu teléfono toma una foto del código QR',
            '<strong>Detección de Patrones:</strong> El software encuentra los tres patrones de posición',
            '<strong>Mapeo de Cuadrícula:</strong> El escáner crea una cuadrícula sobre la imagen',
            '<strong>Extracción de Datos:</strong> Módulos negros = 1, módulos blancos = 0 — creando datos binarios',
            '<strong>Corrección de Errores:</strong> El escáner usa corrección de errores Reed-Solomon',
            '<strong>Decodificación:</strong> Los datos binarios se convierten en texto o URLs legibles'
        ],
        'error_title': 'Corrección de Errores: Por Qué los Códigos QR Dañados Aún Funcionan',
        'error_text': 'Los códigos QR tienen redundancia incorporada. Incluso si parte del código está dañado o cubierto, aún puede leerse. Hay cuatro niveles de corrección de errores:',
        'error_levels': [
            '<strong>L (Bajo):</strong> ~7% del código puede restaurarse',
            '<strong>M (Medio):</strong> ~15% puede restaurarse',
            '<strong>Q (Cuartil):</strong> ~25% puede restaurarse',
            '<strong>H (Alto):</strong> ~30% puede restaurarse — ¡por eso puedes poner logos en el centro!'
        ],
        'types_title': '¿Qué Pueden Almacenar los Códigos QR?',
        'types': ['URLs de sitios web', 'Texto simple', 'Información de contacto (vCard)', 'Credenciales WiFi', 'Números de teléfono', 'Direcciones de email', 'Coordenadas GPS', 'Eventos de calendario', 'Enlaces a tiendas de apps'],
        'static_dynamic_title': 'Códigos QR Estáticos vs Dinámicos',
        'static_title': 'Códigos QR Estáticos',
        'static_text': 'Los datos están codificados directamente en el patrón. Una vez creados, no pueden cambiarse. Gratis de crear, funcionan para siempre.',
        'dynamic_title': 'Códigos QR Dinámicos',
        'dynamic_text': 'El código apunta a una URL de redirección. Puedes cambiar el destino en cualquier momento y rastrear escaneos. Requiere un servicio de pago.',
        'why_popular_title': 'Por Qué los Códigos QR Se Volvieron Tan Populares',
        'why_popular': [
            '<strong>Sin contacto:</strong> COVID-19 aceleró la adopción para menús y pagos sin contacto',
            '<strong>Cámaras de smartphone:</strong> No se necesita app — integrado en iOS y Android desde 2017',
            '<strong>Gratis:</strong> Cualquiera puede generar códigos QR instantáneamente',
            '<strong>Versátil:</strong> Funciona para URLs, texto, WiFi, contactos y más',
            '<strong>Confiable:</strong> La corrección de errores significa que funcionan incluso dañados'
        ],
        'fun_facts_title': 'Datos Curiosos',
        'fun_facts': [
            'El código QR más grande jamás hecho fue de 2.1 km² (creado en un campo de trigo chino)',
            'Los códigos QR fueron inventados originalmente para rastrear partes de autos en manufactura',
            'La patente de los códigos QR es de Denso Wave, pero no la ejercen — manteniendo la tecnología gratis',
            'Un código QR necesita mínimo 4 módulos de "zona silenciosa" alrededor'
        ],
        'cta_title': 'Crea Tu Propio Código QR',
        'cta_text': 'Ahora que sabes cómo funcionan, crea tu propio código QR gratis.',
        'cta_button': 'Crear Código QR →',
        'back': '← Volver',
        'lang_name': 'Español',
    },
    'fr': {
        'title': 'Comment Fonctionnent les QR Codes | La Technologie Expliquée',
        'meta': 'Découvrez comment fonctionnent les QR codes, du scan au décodage. Comprenez la technologie derrière ces motifs carrés.',
        'h1': 'Comment Fonctionnent les QR Codes',
        'subtitle': 'La technologie fascinante derrière ces carrés noirs et blancs',
        'intro': 'Vous les scannez tous les jours — dans les restaurants, sur les produits, dans les publicités. Mais vous êtes-vous déjà demandé <strong>comment fonctionnent vraiment les QR codes</strong>? Expliquons la technologie simplement.',
        'what_title': 'Qu\'est-ce qu\'un QR Code?',
        'what_text': 'QR signifie <strong>Quick Response</strong> (Réponse Rapide). C\'est un type de code-barres 2D inventé en 1994 par une société japonaise appelée Denso Wave. Contrairement aux codes-barres traditionnels qui ne stockent des données qu\'horizontalement, les QR codes stockent les informations horizontalement et verticalement — leur permettant de contenir beaucoup plus de données.',
        'what_capacity': 'Un seul QR code peut stocker jusqu\'à <strong>3 000 caractères</strong> de texte, contre seulement 20-25 caractères pour un code-barres traditionnel.',
        'anatomy_title': 'Anatomie d\'un QR Code',
        'anatomy_intro': 'Chaque QR code possède ces composants clés:',
        'anatomy_1_title': 'Motifs de Position (Grands Carrés)',
        'anatomy_1': 'Les trois grands carrés dans les coins aident les scanners à localiser et orienter rapidement le QR code.',
        'anatomy_2_title': 'Motif d\'Alignement',
        'anatomy_2': 'Le petit carré aide à une lecture précise, surtout sur les surfaces courbes.',
        'anatomy_3_title': 'Motifs de Synchronisation',
        'anatomy_3': 'Modules alternés noirs et blancs qui déterminent la taille de la grille de données.',
        'anatomy_4_title': 'Zone de Données',
        'anatomy_4': 'Le motif brouillé au milieu — c\'est là que vos informations sont encodées.',
        'anatomy_5_title': 'Zone de Silence',
        'anatomy_5': 'La bordure blanche autour du code qui aide les scanners à distinguer le QR code de son environnement.',
        'how_scan_title': 'Comment Fonctionne le Scan',
        'how_scan_steps': [
            '<strong>Capture d\'Image:</strong> L\'appareil photo de votre téléphone prend une photo du QR code',
            '<strong>Détection de Motifs:</strong> Le logiciel trouve les trois motifs de position',
            '<strong>Mappage de Grille:</strong> Le scanner crée une grille sur l\'image',
            '<strong>Extraction de Données:</strong> Modules noirs = 1, modules blancs = 0 — créant des données binaires',
            '<strong>Correction d\'Erreurs:</strong> Le scanner utilise la correction d\'erreurs Reed-Solomon',
            '<strong>Décodage:</strong> Les données binaires sont converties en texte ou URLs lisibles'
        ],
        'error_title': 'Correction d\'Erreurs: Pourquoi les QR Codes Endommagés Fonctionnent Encore',
        'error_text': 'Les QR codes ont une redondance intégrée. Même si une partie du code est endommagée ou couverte, il peut encore être lu. Il y a quatre niveaux de correction d\'erreurs:',
        'error_levels': [
            '<strong>L (Bas):</strong> ~7% du code peut être restauré',
            '<strong>M (Moyen):</strong> ~15% peut être restauré',
            '<strong>Q (Quartile):</strong> ~25% peut être restauré',
            '<strong>H (Haut):</strong> ~30% peut être restauré — c\'est pourquoi vous pouvez mettre des logos au centre!'
        ],
        'types_title': 'Que Peuvent Stocker les QR Codes?',
        'types': ['URLs de sites web', 'Texte simple', 'Informations de contact (vCard)', 'Identifiants WiFi', 'Numéros de téléphone', 'Adresses email', 'Coordonnées GPS', 'Événements calendrier', 'Liens App Store'],
        'static_dynamic_title': 'QR Codes Statiques vs Dynamiques',
        'static_title': 'QR Codes Statiques',
        'static_text': 'Les données sont encodées directement dans le motif. Une fois créés, ils ne peuvent pas être modifiés. Gratuits à créer, fonctionnent pour toujours.',
        'dynamic_title': 'QR Codes Dynamiques',
        'dynamic_text': 'Le code pointe vers une URL de redirection. Vous pouvez changer la destination à tout moment et suivre les scans. Nécessite un service payant.',
        'why_popular_title': 'Pourquoi les QR Codes Sont Devenus Si Populaires',
        'why_popular': [
            '<strong>Sans contact:</strong> Le COVID-19 a accéléré l\'adoption pour les menus et paiements sans contact',
            '<strong>Caméras smartphone:</strong> Pas d\'app nécessaire — intégré dans iOS et Android depuis 2017',
            '<strong>Gratuit:</strong> Tout le monde peut générer des QR codes instantanément',
            '<strong>Polyvalent:</strong> Fonctionne pour URLs, texte, WiFi, contacts et plus',
            '<strong>Fiable:</strong> La correction d\'erreurs signifie qu\'ils fonctionnent même endommagés'
        ],
        'fun_facts_title': 'Faits Amusants',
        'fun_facts': [
            'Le plus grand QR code jamais fait mesurait 2,1 km² (créé dans un champ de blé chinois)',
            'Les QR codes ont été inventés à l\'origine pour suivre les pièces automobiles',
            'Le brevet des QR codes appartient à Denso Wave, mais ils ne l\'exercent pas — gardant la technologie gratuite',
            'Un QR code doit avoir minimum 4 modules de "zone de silence" autour de lui'
        ],
        'cta_title': 'Créez Votre Propre QR Code',
        'cta_text': 'Maintenant que vous savez comment ils fonctionnent, créez gratuitement votre propre QR code.',
        'cta_button': 'Créer un QR Code →',
        'back': '← Retour',
        'lang_name': 'Français',
    },
    'pt': {
        'title': 'Como os QR Codes Funcionam | A Tecnologia Explicada',
        'meta': 'Aprenda como os QR codes funcionam, do escaneamento à decodificação. Entenda a tecnologia por trás desses padrões quadrados.',
        'h1': 'Como os QR Codes Funcionam',
        'subtitle': 'A fascinante tecnologia por trás desses quadrados pretos e brancos',
        'intro': 'Você os escaneia todos os dias — em restaurantes, produtos, anúncios. Mas você já se perguntou <strong>como os QR codes realmente funcionam</strong>? Vamos explicar a tecnologia de forma simples.',
        'what_title': 'O que é um QR Code?',
        'what_text': 'QR significa <strong>Quick Response</strong> (Resposta Rápida). É um tipo de código de barras 2D inventado em 1994 por uma empresa japonesa chamada Denso Wave. Diferente dos códigos de barras tradicionais que só armazenam dados horizontalmente, os QR codes armazenam informações horizontal e verticalmente — permitindo armazenar muito mais dados.',
        'what_capacity': 'Um único QR code pode armazenar até <strong>3.000 caracteres</strong> de texto, comparado com apenas 20-25 caracteres em um código de barras tradicional.',
        'anatomy_title': 'Anatomia de um QR Code',
        'anatomy_intro': 'Todo QR code tem estes componentes principais:',
        'anatomy_1_title': 'Padrões de Posição (Quadrados Grandes)',
        'anatomy_1': 'Os três quadrados grandes nos cantos ajudam os scanners a localizar e orientar rapidamente o QR code.',
        'anatomy_2_title': 'Padrão de Alinhamento',
        'anatomy_2': 'O quadrado menor ajuda na leitura precisa, especialmente em superfícies curvas.',
        'anatomy_3_title': 'Padrões de Tempo',
        'anatomy_3': 'Módulos alternados pretos e brancos que determinam o tamanho da grade de dados.',
        'anatomy_4_title': 'Área de Dados',
        'anatomy_4': 'O padrão embaralhado no meio — é aqui que suas informações reais estão codificadas.',
        'anatomy_5_title': 'Zona Silenciosa',
        'anatomy_5': 'A borda branca ao redor do código que ajuda os scanners a distinguir o QR code do ambiente.',
        'how_scan_title': 'Como o Escaneamento Funciona',
        'how_scan_steps': [
            '<strong>Captura de Imagem:</strong> A câmera do seu celular tira uma foto do QR code',
            '<strong>Detecção de Padrões:</strong> O software encontra os três padrões de posição',
            '<strong>Mapeamento de Grade:</strong> O scanner cria uma grade sobre a imagem',
            '<strong>Extração de Dados:</strong> Módulos pretos = 1, módulos brancos = 0 — criando dados binários',
            '<strong>Correção de Erros:</strong> O scanner usa correção de erros Reed-Solomon',
            '<strong>Decodificação:</strong> Dados binários são convertidos em texto ou URLs legíveis'
        ],
        'error_title': 'Correção de Erros: Por Que QR Codes Danificados Ainda Funcionam',
        'error_text': 'QR codes têm redundância embutida. Mesmo se parte do código estiver danificada ou coberta, ainda pode ser lido. Há quatro níveis de correção de erros:',
        'error_levels': [
            '<strong>L (Baixo):</strong> ~7% do código pode ser restaurado',
            '<strong>M (Médio):</strong> ~15% pode ser restaurado',
            '<strong>Q (Quartil):</strong> ~25% pode ser restaurado',
            '<strong>H (Alto):</strong> ~30% pode ser restaurado — por isso você pode colocar logos no centro!'
        ],
        'types_title': 'O Que os QR Codes Podem Armazenar?',
        'types': ['URLs de sites', 'Texto simples', 'Informações de contato (vCard)', 'Credenciais WiFi', 'Números de telefone', 'Endereços de email', 'Coordenadas GPS', 'Eventos de calendário', 'Links de lojas de apps'],
        'static_dynamic_title': 'QR Codes Estáticos vs Dinâmicos',
        'static_title': 'QR Codes Estáticos',
        'static_text': 'Os dados são codificados diretamente no padrão. Uma vez criados, não podem ser alterados. Grátis para criar, funcionam para sempre.',
        'dynamic_title': 'QR Codes Dinâmicos',
        'dynamic_text': 'O código aponta para uma URL de redirecionamento. Você pode mudar o destino a qualquer momento e rastrear escaneamentos. Requer um serviço pago.',
        'why_popular_title': 'Por Que os QR Codes Se Tornaram Tão Populares',
        'why_popular': [
            '<strong>Sem contato:</strong> COVID-19 acelerou a adoção para menus e pagamentos sem contato',
            '<strong>Câmeras de smartphone:</strong> Sem necessidade de app — integrado no iOS e Android desde 2017',
            '<strong>Grátis:</strong> Qualquer um pode gerar QR codes instantaneamente',
            '<strong>Versátil:</strong> Funciona para URLs, texto, WiFi, contatos e mais',
            '<strong>Confiável:</strong> Correção de erros significa que funcionam mesmo danificados'
        ],
        'fun_facts_title': 'Curiosidades',
        'fun_facts': [
            'O maior QR code já feito tinha 2,1 km² (criado em um campo de trigo chinês)',
            'QR codes foram originalmente inventados para rastrear peças de carros na manufatura',
            'A patente dos QR codes é da Denso Wave, mas eles não a exercem — mantendo a tecnologia grátis',
            'Um QR code precisa de no mínimo 4 módulos de "zona silenciosa" ao redor'
        ],
        'cta_title': 'Crie Seu Próprio QR Code',
        'cta_text': 'Agora que você sabe como funcionam, crie seu próprio QR code gratuitamente.',
        'cta_button': 'Criar QR Code →',
        'back': '← Voltar',
        'lang_name': 'Português',
    },
    'zh': {
        'title': '二维码如何工作 | 技术原理简单解释',
        'meta': '了解二维码如何工作，从扫描到解码。理解这些方形图案背后的技术以及它们为何如此可靠。',
        'h1': '二维码如何工作',
        'subtitle': '黑白方块背后的迷人技术',
        'intro': '你每天都在扫描它们——在餐厅、产品上、广告中。但你有没有想过<strong>二维码究竟是如何工作的</strong>？让我们用简单的术语来解释这项技术。',
        'what_title': '什么是二维码？',
        'what_text': 'QR代表<strong>Quick Response</strong>（快速响应）。它是一种二维条码，由日本公司Denso Wave于1994年发明。与只能水平存储数据的传统条码不同，二维码可以水平和垂直存储信息——使它们能够存储更多数据。',
        'what_capacity': '一个二维码可以存储多达<strong>3,000个字符</strong>的文本，而传统条码只能存储20-25个字符。',
        'anatomy_title': '二维码的结构',
        'anatomy_intro': '每个二维码都有这些关键组件：',
        'anatomy_1_title': '定位图案（大方块）',
        'anatomy_1': '角落的三个大方块帮助扫描器快速定位和确定二维码的方向。',
        'anatomy_2_title': '对齐图案',
        'anatomy_2': '较小的方块有助于精确读取，特别是在曲面上。',
        'anatomy_3_title': '定时图案',
        'anatomy_3': '交替的黑白模块，用于确定数据网格的大小。',
        'anatomy_4_title': '数据区',
        'anatomy_4': '中间看起来杂乱的图案——这是你的实际信息编码的地方。',
        'anatomy_5_title': '静区',
        'anatomy_5': '代码周围的白色边框，帮助扫描器将二维码与周围环境区分开。',
        'how_scan_title': '扫描如何工作',
        'how_scan_steps': [
            '<strong>图像捕获：</strong>手机摄像头拍摄二维码照片',
            '<strong>图案检测：</strong>软件找到三个定位图案来定位代码',
            '<strong>网格映射：</strong>扫描器在图像上创建网格',
            '<strong>数据提取：</strong>黑色模块=1，白色模块=0——创建二进制数据',
            '<strong>纠错：</strong>扫描器使用Reed-Solomon纠错',
            '<strong>解码：</strong>二进制数据转换为可读文本或URL'
        ],
        'error_title': '纠错：为什么损坏的二维码仍然有效',
        'error_text': '二维码具有内置冗余。即使部分代码损坏或被遮盖，仍然可以读取。有四个纠错级别：',
        'error_levels': [
            '<strong>L（低）：</strong>约7%的代码可以恢复',
            '<strong>M（中）：</strong>约15%可以恢复',
            '<strong>Q（四分位）：</strong>约25%可以恢复',
            '<strong>H（高）：</strong>约30%可以恢复——这就是为什么你可以在中间放logo！'
        ],
        'types_title': '二维码可以存储什么？',
        'types': ['网站URL', '纯文本', '联系信息（vCard）', 'WiFi凭证', '电话号码', '电子邮件地址', 'GPS坐标', '日历事件', '应用商店链接'],
        'static_dynamic_title': '静态与动态二维码',
        'static_title': '静态二维码',
        'static_text': '数据直接编码在图案中。一旦创建，无法更改。免费创建，永久有效。',
        'dynamic_title': '动态二维码',
        'dynamic_text': '代码指向重定向URL。你可以随时更改目标并跟踪扫描。需要付费服务。',
        'why_popular_title': '为什么二维码如此流行',
        'why_popular': [
            '<strong>无接触：</strong>COVID-19加速了无接触菜单和支付的采用',
            '<strong>智能手机摄像头：</strong>无需应用——自2017年起内置于iOS和Android',
            '<strong>免费：</strong>任何人都可以即时生成二维码',
            '<strong>多功能：</strong>适用于URL、文本、WiFi、联系人等',
            '<strong>可靠：</strong>纠错意味着即使损坏也能工作'
        ],
        'fun_facts_title': '有趣的事实',
        'fun_facts': [
            '有史以来最大的二维码是2.1平方公里（在中国麦田中创建）',
            '二维码最初是为了在制造中追踪汽车零件而发明的',
            '二维码专利属于Denso Wave，但他们不行使——保持技术免费',
            '二维码周围必须至少有4个模块的"静区"'
        ],
        'cta_title': '创建你自己的二维码',
        'cta_text': '现在你知道它们是如何工作的了，免费创建你自己的二维码。',
        'cta_button': '创建二维码 →',
        'back': '← 返回',
        'lang_name': '中文',
    },
    'ja': {
        'title': 'QRコードの仕組み | 技術をわかりやすく解説',
        'meta': 'QRコードがどのように機能するか、スキャンからデコードまでを学びましょう。あの四角いパターンの背後にある技術を理解しましょう。',
        'h1': 'QRコードの仕組み',
        'subtitle': '白黒の四角の背後にある魅力的な技術',
        'intro': 'あなたは毎日それをスキャンしています — レストラン、製品、広告で。でも<strong>QRコードが実際にどのように機能するか</strong>考えたことはありますか？技術をシンプルに解説します。',
        'what_title': 'QRコードとは？',
        'what_text': 'QRは<strong>Quick Response</strong>（クイックレスポンス）の略です。1994年に日本の会社デンソーウェーブによって発明された2次元バーコードの一種です。データを水平方向にのみ保存する従来のバーコードとは異なり、QRコードは水平と垂直の両方に情報を保存できます — より多くのデータを保存できます。',
        'what_capacity': '1つのQRコードは最大<strong>3,000文字</strong>のテキストを保存できます。従来のバーコードの20-25文字と比較してください。',
        'anatomy_title': 'QRコードの構造',
        'anatomy_intro': 'すべてのQRコードにはこれらの主要なコンポーネントがあります：',
        'anatomy_1_title': '位置検出パターン（大きな四角）',
        'anatomy_1': '角にある3つの大きな四角は、スキャナーがQRコードを素早く見つけて向きを決めるのに役立ちます。',
        'anatomy_2_title': 'アライメントパターン',
        'anatomy_2': '小さな四角は、特に曲面での正確な読み取りに役立ちます。',
        'anatomy_3_title': 'タイミングパターン',
        'anatomy_3': 'データグリッドのサイズを決定する白黒交互のモジュール。',
        'anatomy_4_title': 'データ領域',
        'anatomy_4': '中央のスクランブルに見えるパターン — ここに実際の情報がエンコードされています。',
        'anatomy_5_title': 'クワイエットゾーン',
        'anatomy_5': 'コード周囲の白い境界線で、スキャナーがQRコードを周囲から区別するのに役立ちます。',
        'how_scan_title': 'スキャンの仕組み',
        'how_scan_steps': [
            '<strong>画像キャプチャ：</strong>スマホのカメラがQRコードの写真を撮影',
            '<strong>パターン検出：</strong>ソフトウェアが3つの位置検出パターンを見つける',
            '<strong>グリッドマッピング：</strong>スキャナーが画像上にグリッドを作成',
            '<strong>データ抽出：</strong>黒いモジュール=1、白いモジュール=0 — バイナリデータを作成',
            '<strong>エラー訂正：</strong>スキャナーがリードソロモン誤り訂正を使用',
            '<strong>デコード：</strong>バイナリデータが読み取り可能なテキストやURLに変換'
        ],
        'error_title': 'エラー訂正：損傷したQRコードがまだ機能する理由',
        'error_text': 'QRコードには冗長性が組み込まれています。コードの一部が損傷したり覆われていても、読み取ることができます。4つのエラー訂正レベルがあります：',
        'error_levels': [
            '<strong>L（低）：</strong>コードの約7%を復元可能',
            '<strong>M（中）：</strong>約15%を復元可能',
            '<strong>Q（クォータイル）：</strong>約25%を復元可能',
            '<strong>H（高）：</strong>約30%を復元可能 — だから中央にロゴを入れられます！'
        ],
        'types_title': 'QRコードに保存できるもの',
        'types': ['ウェブサイトURL', 'プレーンテキスト', '連絡先情報（vCard）', 'WiFi認証情報', '電話番号', 'メールアドレス', 'GPS座標', 'カレンダーイベント', 'アプリストアリンク'],
        'static_dynamic_title': '静的QRコード vs 動的QRコード',
        'static_title': '静的QRコード',
        'static_text': 'データはパターンに直接エンコードされます。作成後は変更できません。無料で作成、永久に機能。',
        'dynamic_title': '動的QRコード',
        'dynamic_text': 'コードはリダイレクトURLを指します。いつでも宛先を変更でき、スキャンを追跡できます。有料サービスが必要。',
        'why_popular_title': 'QRコードが人気になった理由',
        'why_popular': [
            '<strong>非接触：</strong>COVID-19が非接触メニューや決済の採用を加速',
            '<strong>スマホカメラ：</strong>アプリ不要 — 2017年からiOSとAndroidに内蔵',
            '<strong>無料：</strong>誰でも即座にQRコードを生成できる',
            '<strong>多用途：</strong>URL、テキスト、WiFi、連絡先などに対応',
            '<strong>信頼性：</strong>エラー訂正により損傷しても機能'
        ],
        'fun_facts_title': '豆知識',
        'fun_facts': [
            '史上最大のQRコードは2.1km²（中国の麦畑に作成）',
            'QRコードは元々、製造業で自動車部品を追跡するために発明された',
            'QRコードの特許はデンソーウェーブが所有しているが、行使していない — 技術を無料に保っている',
            'QRコードは周囲に最低4モジュールの「クワイエットゾーン」が必要'
        ],
        'cta_title': '自分のQRコードを作成',
        'cta_text': '仕組みがわかったところで、無料で自分のQRコードを作成しましょう。',
        'cta_button': 'QRコードを作成 →',
        'back': '← 戻る',
        'lang_name': '日本語',
    },
    'ar': {
        'title': 'كيف تعمل رموز QR | التقنية موضحة ببساطة',
        'meta': 'تعلم كيف تعمل رموز QR، من المسح إلى فك التشفير. افهم التقنية وراء تلك الأنماط المربعة.',
        'h1': 'كيف تعمل رموز QR',
        'subtitle': 'التقنية الرائعة وراء تلك المربعات السوداء والبيضاء',
        'intro': 'أنت تمسحها كل يوم — في المطاعم، على المنتجات، في الإعلانات. لكن هل تساءلت يوماً <strong>كيف تعمل رموز QR فعلاً</strong>؟ دعنا نشرح التقنية بعبارات بسيطة.',
        'what_title': 'ما هو رمز QR؟',
        'what_text': 'QR تعني <strong>Quick Response</strong> (استجابة سريعة). إنه نوع من الباركود ثنائي الأبعاد اخترعته شركة يابانية تسمى Denso Wave في عام 1994. على عكس الباركود التقليدي الذي يخزن البيانات أفقياً فقط، تخزن رموز QR المعلومات أفقياً وعمودياً — مما يسمح لها بتخزين المزيد من البيانات.',
        'what_capacity': 'يمكن لرمز QR واحد تخزين ما يصل إلى <strong>3,000 حرف</strong> من النص، مقارنة بـ 20-25 حرفاً فقط في الباركود التقليدي.',
        'anatomy_title': 'تشريح رمز QR',
        'anatomy_intro': 'كل رمز QR يحتوي على هذه المكونات الرئيسية:',
        'anatomy_1_title': 'أنماط الموقع (المربعات الكبيرة)',
        'anatomy_1': 'المربعات الثلاثة الكبيرة في الزوايا تساعد الماسحات على تحديد موقع رمز QR وتوجيهه بسرعة.',
        'anatomy_2_title': 'نمط المحاذاة',
        'anatomy_2': 'المربع الأصغر يساعد في القراءة الدقيقة، خاصة على الأسطح المنحنية.',
        'anatomy_3_title': 'أنماط التوقيت',
        'anatomy_3': 'وحدات سوداء وبيضاء متناوبة تحدد حجم شبكة البيانات.',
        'anatomy_4_title': 'منطقة البيانات',
        'anatomy_4': 'النمط المشوش في المنتصف — هنا يتم ترميز معلوماتك الفعلية.',
        'anatomy_5_title': 'المنطقة الهادئة',
        'anatomy_5': 'الحدود البيضاء حول الرمز التي تساعد الماسحات على تمييز رمز QR عن محيطه.',
        'how_scan_title': 'كيف يعمل المسح',
        'how_scan_steps': [
            '<strong>التقاط الصورة:</strong> كاميرا هاتفك تلتقط صورة لرمز QR',
            '<strong>كشف الأنماط:</strong> البرنامج يجد أنماط الموقع الثلاثة',
            '<strong>رسم الشبكة:</strong> الماسح ينشئ شبكة فوق الصورة',
            '<strong>استخراج البيانات:</strong> الوحدات السوداء = 1، الوحدات البيضاء = 0 — إنشاء بيانات ثنائية',
            '<strong>تصحيح الأخطاء:</strong> الماسح يستخدم تصحيح أخطاء Reed-Solomon',
            '<strong>فك التشفير:</strong> البيانات الثنائية تتحول إلى نص أو روابط قابلة للقراءة'
        ],
        'error_title': 'تصحيح الأخطاء: لماذا تعمل رموز QR التالفة',
        'error_text': 'رموز QR لديها تكرار مدمج. حتى لو كان جزء من الرمز تالفاً أو مغطى، يمكن قراءته. هناك أربعة مستويات لتصحيح الأخطاء:',
        'error_levels': [
            '<strong>L (منخفض):</strong> يمكن استعادة ~7% من الرمز',
            '<strong>M (متوسط):</strong> يمكن استعادة ~15%',
            '<strong>Q (ربعي):</strong> يمكن استعادة ~25%',
            '<strong>H (عالي):</strong> يمكن استعادة ~30% — لهذا يمكنك وضع الشعارات في المنتصف!'
        ],
        'types_title': 'ماذا يمكن أن تخزن رموز QR؟',
        'types': ['روابط المواقع', 'نص عادي', 'معلومات الاتصال (vCard)', 'بيانات WiFi', 'أرقام الهاتف', 'عناوين البريد الإلكتروني', 'إحداثيات GPS', 'أحداث التقويم', 'روابط متجر التطبيقات'],
        'static_dynamic_title': 'رموز QR الثابتة مقابل الديناميكية',
        'static_title': 'رموز QR الثابتة',
        'static_text': 'البيانات مشفرة مباشرة في النمط. بمجرد إنشائها، لا يمكن تغييرها. مجانية الإنشاء، تعمل للأبد.',
        'dynamic_title': 'رموز QR الديناميكية',
        'dynamic_text': 'الرمز يشير إلى رابط إعادة توجيه. يمكنك تغيير الوجهة في أي وقت وتتبع المسح. يتطلب خدمة مدفوعة.',
        'why_popular_title': 'لماذا أصبحت رموز QR شائعة جداً',
        'why_popular': [
            '<strong>بدون تلامس:</strong> كوفيد-19 سرّع اعتماد القوائم والمدفوعات اللاتلامسية',
            '<strong>كاميرات الهواتف:</strong> لا حاجة لتطبيق — مدمج في iOS وأندرويد منذ 2017',
            '<strong>مجاني:</strong> أي شخص يمكنه إنشاء رموز QR فوراً',
            '<strong>متعدد الاستخدامات:</strong> يعمل للروابط والنصوص وWiFi وجهات الاتصال والمزيد',
            '<strong>موثوق:</strong> تصحيح الأخطاء يعني أنها تعمل حتى عند التلف'
        ],
        'fun_facts_title': 'حقائق ممتعة',
        'fun_facts': [
            'أكبر رمز QR على الإطلاق كان 2.1 كم² (أُنشئ في حقل قمح صيني)',
            'اخترعت رموز QR أصلاً لتتبع قطع السيارات في التصنيع',
            'براءة اختراع رموز QR مملوكة لـ Denso Wave، لكنهم لا يمارسونها — للحفاظ على التقنية مجانية',
            'يجب أن يكون لرمز QR منطقة هادئة لا تقل عن 4 وحدات حوله'
        ],
        'cta_title': 'أنشئ رمز QR الخاص بك',
        'cta_text': 'الآن بعد أن تعرف كيف تعمل، أنشئ رمز QR الخاص بك مجاناً.',
        'cta_button': 'إنشاء رمز QR ←',
        'back': 'رجوع ←',
        'lang_name': 'العربية',
    },
    'hi': {
        'title': 'QR कोड कैसे काम करते हैं | तकनीक सरल भाषा में',
        'meta': 'जानें QR कोड कैसे काम करते हैं, स्कैनिंग से डिकोडिंग तक। उन चौकोर पैटर्न के पीछे की तकनीक को समझें।',
        'h1': 'QR कोड कैसे काम करते हैं',
        'subtitle': 'उन काले और सफेद वर्गों के पीछे की आकर्षक तकनीक',
        'intro': 'आप हर दिन इन्हें स्कैन करते हैं — रेस्तरां में, उत्पादों पर, विज्ञापनों में। लेकिन क्या आपने कभी सोचा है कि <strong>QR कोड वास्तव में कैसे काम करते हैं</strong>? आइए तकनीक को सरल शब्दों में समझें।',
        'what_title': 'QR कोड क्या है?',
        'what_text': 'QR का मतलब <strong>Quick Response</strong> (त्वरित प्रतिक्रिया) है। यह एक 2D बारकोड है जिसका आविष्कार 1994 में जापानी कंपनी Denso Wave ने किया था। पारंपरिक बारकोड जो केवल क्षैतिज रूप से डेटा संग्रहीत करते हैं, उनके विपरीत QR कोड क्षैतिज और लंबवत दोनों तरह से जानकारी संग्रहीत करते हैं।',
        'what_capacity': 'एक QR कोड में <strong>3,000 अक्षर</strong> तक का टेक्स्ट संग्रहीत किया जा सकता है, जबकि पारंपरिक बारकोड में केवल 20-25 अक्षर।',
        'anatomy_title': 'QR कोड की संरचना',
        'anatomy_intro': 'हर QR कोड में ये मुख्य घटक होते हैं:',
        'anatomy_1_title': 'फाइंडर पैटर्न (बड़े वर्ग)',
        'anatomy_1': 'कोनों में तीन बड़े वर्ग स्कैनर को QR कोड को जल्दी से खोजने और उन्मुख करने में मदद करते हैं।',
        'anatomy_2_title': 'एलाइनमेंट पैटर्न',
        'anatomy_2': 'छोटा वर्ग सटीक पढ़ने में मदद करता है, विशेष रूप से घुमावदार सतहों पर।',
        'anatomy_3_title': 'टाइमिंग पैटर्न',
        'anatomy_3': 'वैकल्पिक काले और सफेद मॉड्यूल जो डेटा ग्रिड का आकार निर्धारित करते हैं।',
        'anatomy_4_title': 'डेटा क्षेत्र',
        'anatomy_4': 'बीच में अव्यवस्थित दिखने वाला पैटर्न — यहीं आपकी वास्तविक जानकारी एनकोड होती है।',
        'anatomy_5_title': 'क्वाइट जोन',
        'anatomy_5': 'कोड के चारों ओर सफेद बॉर्डर जो स्कैनर को QR कोड को उसके परिवेश से अलग करने में मदद करता है।',
        'how_scan_title': 'स्कैनिंग कैसे काम करती है',
        'how_scan_steps': [
            '<strong>इमेज कैप्चर:</strong> आपके फोन का कैमरा QR कोड की फोटो लेता है',
            '<strong>पैटर्न डिटेक्शन:</strong> सॉफ्टवेयर तीन फाइंडर पैटर्न खोजता है',
            '<strong>ग्रिड मैपिंग:</strong> स्कैनर इमेज पर ग्रिड बनाता है',
            '<strong>डेटा एक्सट्रैक्शन:</strong> काले मॉड्यूल = 1, सफेद मॉड्यूल = 0 — बाइनरी डेटा बनाता है',
            '<strong>एरर करेक्शन:</strong> स्कैनर Reed-Solomon एरर करेक्शन का उपयोग करता है',
            '<strong>डिकोडिंग:</strong> बाइनरी डेटा पढ़ने योग्य टेक्स्ट या URL में बदल जाता है'
        ],
        'error_title': 'एरर करेक्शन: क्षतिग्रस्त QR कोड अभी भी क्यों काम करते हैं',
        'error_text': 'QR कोड में बिल्ट-इन रिडंडेंसी होती है। भले ही कोड का कुछ हिस्सा क्षतिग्रस्त या ढका हो, फिर भी इसे पढ़ा जा सकता है। चार एरर करेक्शन स्तर हैं:',
        'error_levels': [
            '<strong>L (कम):</strong> कोड का ~7% पुनर्स्थापित किया जा सकता है',
            '<strong>M (मध्यम):</strong> ~15% पुनर्स्थापित किया जा सकता है',
            '<strong>Q (क्वार्टाइल):</strong> ~25% पुनर्स्थापित किया जा सकता है',
            '<strong>H (उच्च):</strong> ~30% पुनर्स्थापित किया जा सकता है — इसीलिए आप बीच में लोगो डाल सकते हैं!'
        ],
        'types_title': 'QR कोड में क्या संग्रहीत किया जा सकता है?',
        'types': ['वेबसाइट URL', 'सादा टेक्स्ट', 'संपर्क जानकारी (vCard)', 'WiFi क्रेडेंशियल', 'फोन नंबर', 'ईमेल पते', 'GPS निर्देशांक', 'कैलेंडर इवेंट', 'ऐप स्टोर लिंक'],
        'static_dynamic_title': 'स्टैटिक बनाम डायनामिक QR कोड',
        'static_title': 'स्टैटिक QR कोड',
        'static_text': 'डेटा सीधे पैटर्न में एनकोड होता है। एक बार बनाने के बाद, बदला नहीं जा सकता। मुफ्त में बनाएं, हमेशा काम करता है।',
        'dynamic_title': 'डायनामिक QR कोड',
        'dynamic_text': 'कोड रीडायरेक्ट URL की ओर इंगित करता है। आप कभी भी गंतव्य बदल सकते हैं और स्कैन ट्रैक कर सकते हैं। पेड सर्विस की जरूरत।',
        'why_popular_title': 'QR कोड इतने लोकप्रिय क्यों हुए',
        'why_popular': [
            '<strong>संपर्क रहित:</strong> COVID-19 ने टचलेस मेन्यू और भुगतान को तेज किया',
            '<strong>स्मार्टफोन कैमरे:</strong> कोई ऐप नहीं चाहिए — 2017 से iOS और Android में बिल्ट-इन',
            '<strong>मुफ्त:</strong> कोई भी तुरंत QR कोड बना सकता है',
            '<strong>बहुमुखी:</strong> URL, टेक्स्ट, WiFi, संपर्क और अधिक के लिए काम करता है',
            '<strong>विश्वसनीय:</strong> एरर करेक्शन का मतलब है कि क्षतिग्रस्त होने पर भी काम करते हैं'
        ],
        'fun_facts_title': 'रोचक तथ्य',
        'fun_facts': [
            'अब तक का सबसे बड़ा QR कोड 2.1 km² था (चीनी गेहूं के खेत में बनाया गया)',
            'QR कोड मूल रूप से विनिर्माण में कार के पुर्जों को ट्रैक करने के लिए आविष्कार किए गए थे',
            'QR कोड का पेटेंट Denso Wave के पास है, लेकिन वे इसे लागू नहीं करते — तकनीक मुफ्त रखते हैं',
            'QR कोड के चारों ओर कम से कम 4 मॉड्यूल का "क्वाइट जोन" होना चाहिए'
        ],
        'cta_title': 'अपना खुद का QR कोड बनाएं',
        'cta_text': 'अब जब आप जानते हैं कि वे कैसे काम करते हैं, मुफ्त में अपना QR कोड बनाएं।',
        'cta_button': 'QR कोड बनाएं →',
        'back': '← वापस',
        'lang_name': 'हिन्दी',
    },
    'ru': {
        'title': 'Как работают QR-коды | Технология простыми словами',
        'meta': 'Узнайте, как работают QR-коды, от сканирования до декодирования. Поймите технологию за этими квадратными узорами.',
        'h1': 'Как работают QR-коды',
        'subtitle': 'Увлекательная технология за чёрно-белыми квадратами',
        'intro': 'Вы сканируете их каждый день — в ресторанах, на товарах, в рекламе. Но задумывались ли вы, <strong>как QR-коды на самом деле работают</strong>? Давайте разберём технологию простым языком.',
        'what_title': 'Что такое QR-код?',
        'what_text': 'QR означает <strong>Quick Response</strong> (Быстрый Ответ). Это тип 2D штрих-кода, изобретённый в 1994 году японской компанией Denso Wave. В отличие от традиционных штрих-кодов, хранящих данные только горизонтально, QR-коды хранят информацию горизонтально и вертикально — позволяя хранить гораздо больше данных.',
        'what_capacity': 'Один QR-код может хранить до <strong>3000 символов</strong> текста, по сравнению с 20-25 символами в традиционном штрих-коде.',
        'anatomy_title': 'Анатомия QR-кода',
        'anatomy_intro': 'Каждый QR-код имеет эти ключевые компоненты:',
        'anatomy_1_title': 'Поисковые паттерны (Большие квадраты)',
        'anatomy_1': 'Три больших квадрата в углах помогают сканерам быстро находить и ориентировать QR-код.',
        'anatomy_2_title': 'Паттерн выравнивания',
        'anatomy_2': 'Меньший квадрат помогает точному чтению, особенно на изогнутых поверхностях.',
        'anatomy_3_title': 'Тайминг-паттерны',
        'anatomy_3': 'Чередующиеся чёрные и белые модули, определяющие размер сетки данных.',
        'anatomy_4_title': 'Область данных',
        'anatomy_4': 'Запутанный на вид узор в центре — здесь закодирована ваша информация.',
        'anatomy_5_title': 'Тихая зона',
        'anatomy_5': 'Белая граница вокруг кода, помогающая сканерам отличить QR-код от окружения.',
        'how_scan_title': 'Как работает сканирование',
        'how_scan_steps': [
            '<strong>Захват изображения:</strong> Камера телефона фотографирует QR-код',
            '<strong>Обнаружение паттернов:</strong> ПО находит три поисковых паттерна',
            '<strong>Построение сетки:</strong> Сканер создаёт сетку поверх изображения',
            '<strong>Извлечение данных:</strong> Чёрные модули = 1, белые = 0 — создаётся двоичные данные',
            '<strong>Коррекция ошибок:</strong> Сканер использует коррекцию ошибок Рида-Соломона',
            '<strong>Декодирование:</strong> Двоичные данные преобразуются в читаемый текст или URL'
        ],
        'error_title': 'Коррекция ошибок: Почему повреждённые QR-коды работают',
        'error_text': 'QR-коды имеют встроенную избыточность. Даже если часть кода повреждена или закрыта, его можно прочитать. Есть четыре уровня коррекции ошибок:',
        'error_levels': [
            '<strong>L (Низкий):</strong> ~7% кода можно восстановить',
            '<strong>M (Средний):</strong> ~15% можно восстановить',
            '<strong>Q (Квартиль):</strong> ~25% можно восстановить',
            '<strong>H (Высокий):</strong> ~30% можно восстановить — поэтому можно помещать логотипы в центр!'
        ],
        'types_title': 'Что могут хранить QR-коды?',
        'types': ['URL сайтов', 'Простой текст', 'Контактная информация (vCard)', 'Данные WiFi', 'Номера телефонов', 'Email-адреса', 'GPS-координаты', 'События календаря', 'Ссылки на магазины приложений'],
        'static_dynamic_title': 'Статические vs Динамические QR-коды',
        'static_title': 'Статические QR-коды',
        'static_text': 'Данные закодированы прямо в паттерне. После создания нельзя изменить. Бесплатно создавать, работают вечно.',
        'dynamic_title': 'Динамические QR-коды',
        'dynamic_text': 'Код указывает на URL перенаправления. Можно менять назначение когда угодно и отслеживать сканирования. Требуется платный сервис.',
        'why_popular_title': 'Почему QR-коды стали такими популярными',
        'why_popular': [
            '<strong>Бесконтактность:</strong> COVID-19 ускорил внедрение бесконтактных меню и платежей',
            '<strong>Камеры смартфонов:</strong> Приложение не нужно — встроено в iOS и Android с 2017',
            '<strong>Бесплатно:</strong> Любой может мгновенно создать QR-код',
            '<strong>Универсальность:</strong> Работает для URL, текста, WiFi, контактов и др.',
            '<strong>Надёжность:</strong> Коррекция ошибок позволяет работать даже при повреждении'
        ],
        'fun_facts_title': 'Интересные факты',
        'fun_facts': [
            'Самый большой QR-код составлял 2,1 км² (создан на китайском пшеничном поле)',
            'QR-коды изначально изобретены для отслеживания автозапчастей на производстве',
            'Патент на QR-коды принадлежит Denso Wave, но они не реализуют его — технология остаётся бесплатной',
            'QR-код должен иметь минимум 4 модуля «тихой зоны» вокруг'
        ],
        'cta_title': 'Создайте свой QR-код',
        'cta_text': 'Теперь, когда вы знаете, как они работают, создайте свой QR-код бесплатно.',
        'cta_button': 'Создать QR-код →',
        'back': '← Назад',
        'lang_name': 'Русский',
    },
    'tr': {
        'title': 'QR Kodları Nasıl Çalışır | Teknoloji Basitçe Açıklandı',
        'meta': 'QR kodların nasıl çalıştığını, taramadan kod çözmeye kadar öğrenin. Kare desenlerin arkasındaki teknolojiyi anlayın.',
        'h1': 'QR Kodları Nasıl Çalışır',
        'subtitle': 'Siyah beyaz karelerin arkasındaki büyüleyici teknoloji',
        'intro': 'Her gün onları tarıyorsunuz — restoranlarda, ürünlerde, reklamlarda. Ama hiç <strong>QR kodların gerçekte nasıl çalıştığını</strong> merak ettiniz mi? Teknolojiyi basit terimlerle açıklayalım.',
        'what_title': 'QR Kod Nedir?',
        'what_text': 'QR, <strong>Quick Response</strong> (Hızlı Yanıt) anlamına gelir. 1994 yılında Denso Wave adlı bir Japon şirketi tarafından icat edilen bir 2D barkod türüdür. Verileri yalnızca yatay olarak depolayan geleneksel barkodların aksine, QR kodlar bilgileri hem yatay hem de dikey olarak depolar — çok daha fazla veri depolamalarını sağlar.',
        'what_capacity': 'Tek bir QR kod, geleneksel barkodun 20-25 karakterine kıyasla <strong>3.000 karaktere</strong> kadar metin depolayabilir.',
        'anatomy_title': 'QR Kodun Anatomisi',
        'anatomy_intro': 'Her QR kodun bu temel bileşenleri vardır:',
        'anatomy_1_title': 'Konum Desenleri (Büyük Kareler)',
        'anatomy_1': 'Köşelerdeki üç büyük kare, tarayıcıların QR kodu hızla bulmasına ve yönlendirmesine yardımcı olur.',
        'anatomy_2_title': 'Hizalama Deseni',
        'anatomy_2': 'Küçük kare, özellikle eğri yüzeylerde doğru okumaya yardımcı olur.',
        'anatomy_3_title': 'Zamanlama Desenleri',
        'anatomy_3': 'Veri ızgarasının boyutunu belirleyen siyah ve beyaz değişen modüller.',
        'anatomy_4_title': 'Veri Alanı',
        'anatomy_4': 'Ortadaki karışık görünümlü desen — gerçek bilgilerinizin kodlandığı yer burası.',
        'anatomy_5_title': 'Sessiz Bölge',
        'anatomy_5': 'Kodun etrafındaki beyaz kenarlık, tarayıcıların QR kodu çevresinden ayırt etmesine yardımcı olur.',
        'how_scan_title': 'Tarama Nasıl Çalışır',
        'how_scan_steps': [
            '<strong>Görüntü Yakalama:</strong> Telefonunuzun kamerası QR kodun fotoğrafını çeker',
            '<strong>Desen Algılama:</strong> Yazılım üç konum desenini bulur',
            '<strong>Izgara Eşleme:</strong> Tarayıcı görüntü üzerine bir ızgara oluşturur',
            '<strong>Veri Çıkarma:</strong> Siyah modüller = 1, beyaz modüller = 0 — ikili veri oluşturur',
            '<strong>Hata Düzeltme:</strong> Tarayıcı Reed-Solomon hata düzeltmesini kullanır',
            '<strong>Kod Çözme:</strong> İkili veriler okunabilir metin veya URL\'lere dönüştürülür'
        ],
        'error_title': 'Hata Düzeltme: Hasarlı QR Kodlar Neden Hala Çalışır',
        'error_text': 'QR kodlarda yerleşik yedeklilik vardır. Kodun bir kısmı hasar görse veya kapatılsa bile yine okunabilir. Dört hata düzeltme seviyesi vardır:',
        'error_levels': [
            '<strong>L (Düşük):</strong> Kodun ~%7\'si geri yüklenebilir',
            '<strong>M (Orta):</strong> ~%15 geri yüklenebilir',
            '<strong>Q (Çeyrek):</strong> ~%25 geri yüklenebilir',
            '<strong>H (Yüksek):</strong> ~%30 geri yüklenebilir — bu yüzden ortaya logo koyabilirsiniz!'
        ],
        'types_title': 'QR Kodlar Ne Depolayabilir?',
        'types': ['Web sitesi URL\'leri', 'Düz metin', 'İletişim bilgileri (vCard)', 'WiFi kimlik bilgileri', 'Telefon numaraları', 'E-posta adresleri', 'GPS koordinatları', 'Takvim etkinlikleri', 'Uygulama mağazası bağlantıları'],
        'static_dynamic_title': 'Statik vs Dinamik QR Kodlar',
        'static_title': 'Statik QR Kodlar',
        'static_text': 'Veriler doğrudan desene kodlanır. Oluşturulduktan sonra değiştirilemez. Ücretsiz oluşturulur, sonsuza kadar çalışır.',
        'dynamic_title': 'Dinamik QR Kodlar',
        'dynamic_text': 'Kod bir yönlendirme URL\'sine işaret eder. Hedefi istediğiniz zaman değiştirebilir ve taramaları izleyebilirsiniz. Ücretli hizmet gerektirir.',
        'why_popular_title': 'QR Kodlar Neden Bu Kadar Popüler Oldu',
        'why_popular': [
            '<strong>Temassız:</strong> COVID-19, temassız menüler ve ödemeler için benimsemeyi hızlandırdı',
            '<strong>Akıllı telefon kameraları:</strong> Uygulama gerekmez — 2017\'den beri iOS ve Android\'de yerleşik',
            '<strong>Ücretsiz:</strong> Herkes anında QR kod oluşturabilir',
            '<strong>Çok yönlü:</strong> URL\'ler, metin, WiFi, kişiler ve daha fazlası için çalışır',
            '<strong>Güvenilir:</strong> Hata düzeltme, hasarlı olsalar bile çalışacakları anlamına gelir'
        ],
        'fun_facts_title': 'İlginç Bilgiler',
        'fun_facts': [
            'Şimdiye kadar yapılan en büyük QR kod 2,1 km² idi (Çin buğday tarlasında oluşturuldu)',
            'QR kodlar başlangıçta üretimde araba parçalarını izlemek için icat edildi',
            'QR kod patenti Denso Wave\'e aittir, ancak uygulamıyorlar — teknolojiyi ücretsiz tutuyorlar',
            'Bir QR kodun etrafında en az 4 modül "sessiz bölge" olmalıdır'
        ],
        'cta_title': 'Kendi QR Kodunuzu Oluşturun',
        'cta_text': 'Artık nasıl çalıştıklarını bildiğinize göre, ücretsiz kendi QR kodunuzu oluşturun.',
        'cta_button': 'QR Kodu Oluştur →',
        'back': '← Geri',
        'lang_name': 'Türkçe',
    },
}

# Article 2: Are QR Codes Safe?
QR_SAFE = {
    'en': {
        'title': 'Are QR Codes Safe? Security Risks & How to Stay Protected',
        'meta': 'Are QR codes safe to scan? Learn about QR code security risks, common scams, and how to protect yourself from malicious codes.',
        'h1': 'Are QR Codes Safe?',
        'subtitle': 'Understanding the risks and how to protect yourself',
        'intro': 'QR codes are everywhere — but are they safe? The short answer: <strong>QR codes themselves are safe, but what they link to might not be</strong>. Let\'s break down the risks and how to stay protected.',
        'tech_safe_title': 'The Technology Itself is Safe',
        'tech_safe_text': 'A QR code is just a visual way to store data — like text or a URL. The code itself can\'t install malware or hack your phone. It\'s simply a data format, like a barcode.',
        'tech_safe_analogy': 'Think of a QR code like an envelope with an address. The envelope itself is harmless — but the destination it points to is what matters.',
        'risks_title': 'The Real Risks',
        'risk1_title': '1. Phishing Attacks',
        'risk1': 'A malicious QR code could link to a fake website that looks like your bank, email, or social media — designed to steal your login credentials.',
        'risk2_title': '2. Malicious Downloads',
        'risk2': 'Some QR codes might link to websites that try to download malware, especially if you\'re on an outdated phone or browser.',
        'risk3_title': '3. QR Code Swapping',
        'risk3': 'Criminals can place fake QR code stickers over legitimate ones — like on parking meters or restaurant menus — redirecting you to scam sites.',
        'risk4_title': '4. Data Collection',
        'risk4': 'Some QR codes link to tracking URLs that collect your location, device info, or browsing habits without clear disclosure.',
        'real_scams_title': 'Real-World QR Code Scams',
        'scam1': '<strong>Parking meter scams:</strong> Fake QR codes placed on meters lead to payment sites that steal credit card info',
        'scam2': '<strong>Package delivery scams:</strong> Fake "missed delivery" notices with QR codes leading to phishing sites',
        'scam3': '<strong>Crypto scams:</strong> QR codes promising free Bitcoin that actually steal wallet credentials',
        'scam4': '<strong>COVID-19 scams:</strong> Fake vaccination or test result QR codes linked to data-harvesting sites',
        'protect_title': 'How to Stay Safe',
        'protect1_title': 'Preview Before You Click',
        'protect1': 'Most phones show you the URL before opening it. Always check the domain — is it the real company\'s website?',
        'protect2_title': 'Check for Tampering',
        'protect2': 'If a QR code looks like a sticker placed over something else, be suspicious. Legitimate businesses print QR codes directly.',
        'protect3_title': 'Use a QR Scanner with Preview',
        'protect3': 'Some scanner apps show you the link and ask for confirmation before opening. The built-in camera app on iPhone and Android does this.',
        'protect4_title': 'Keep Your Phone Updated',
        'protect4': 'Updates patch security vulnerabilities. An updated phone is much harder to compromise even if you visit a malicious site.',
        'protect5_title': 'Trust Your Instincts',
        'protect5': 'Random QR codes on street poles? Unsolicited QR codes in emails? If it seems sketchy, don\'t scan it.',
        'red_flags_title': '🚩 Red Flags to Watch For',
        'red_flags': [
            'QR code stickers placed over existing codes',
            'QR codes on random flyers or posters with no clear source',
            'Being asked for sensitive info (passwords, SSN, credit cards) after scanning',
            'URLs that look slightly "off" (g00gle.com instead of google.com)',
            'Pressure to act quickly ("Scan now or lose your account!")'
        ],
        'safe_uses_title': 'When QR Codes Are Generally Safe',
        'safe_uses': [
            '✅ Restaurant menus (at the table, not on random stickers)',
            '✅ Product packaging from brands you trust',
            '✅ Official apps and websites of known companies',
            '✅ Event tickets from official ticketing platforms',
            '✅ Two-factor authentication setup',
            '✅ WiFi sharing in homes and offices you trust'
        ],
        'bottom_line_title': 'The Bottom Line',
        'bottom_line': 'QR codes are as safe as the person or company that created them. Treat scanning a QR code like clicking a link — would you click a random link from a stranger? Apply the same caution to QR codes.',
        'cta_title': 'Create Safe QR Codes',
        'cta_text': 'When you create QR codes with us, what you see is what you get — no tracking, no redirects, no funny business.',
        'cta_button': 'Create QR Code →',
        'back': '← Back',
        'lang_name': 'English',
    },
    'de': {
        'title': 'Sind QR-Codes sicher? Sicherheitsrisiken & Schutzmaßnahmen',
        'meta': 'Sind QR-Codes sicher zum Scannen? Erfahren Sie mehr über QR-Code-Sicherheitsrisiken, häufige Betrugsmaschen und wie Sie sich schützen.',
        'h1': 'Sind QR-Codes sicher?',
        'subtitle': 'Die Risiken verstehen und sich schützen',
        'intro': 'QR-Codes sind überall — aber sind sie sicher? Die kurze Antwort: <strong>QR-Codes selbst sind sicher, aber das, wohin sie führen, möglicherweise nicht</strong>. Lassen Sie uns die Risiken und Schutzmaßnahmen aufschlüsseln.',
        'tech_safe_title': 'Die Technologie selbst ist sicher',
        'tech_safe_text': 'Ein QR-Code ist nur eine visuelle Art, Daten zu speichern — wie Text oder eine URL. Der Code selbst kann keine Malware installieren oder Ihr Telefon hacken. Es ist einfach ein Datenformat, wie ein Barcode.',
        'tech_safe_analogy': 'Denken Sie an einen QR-Code wie an einen Briefumschlag mit einer Adresse. Der Umschlag selbst ist harmlos — aber das Ziel, auf das er zeigt, ist entscheidend.',
        'risks_title': 'Die echten Risiken',
        'risk1_title': '1. Phishing-Angriffe',
        'risk1': 'Ein bösartiger QR-Code könnte zu einer gefälschten Website führen, die wie Ihre Bank oder E-Mail aussieht — entwickelt, um Ihre Anmeldedaten zu stehlen.',
        'risk2_title': '2. Schädliche Downloads',
        'risk2': 'Einige QR-Codes können zu Websites führen, die versuchen, Malware herunterzuladen, besonders auf veralteten Geräten.',
        'risk3_title': '3. QR-Code-Austausch',
        'risk3': 'Kriminelle können gefälschte QR-Code-Aufkleber über legitime kleben — wie an Parkuhren oder Restaurantmenüs.',
        'risk4_title': '4. Datensammlung',
        'risk4': 'Einige QR-Codes führen zu Tracking-URLs, die Ihren Standort und Geräteinformationen ohne klare Offenlegung sammeln.',
        'real_scams_title': 'Echte QR-Code-Betrugsmaschen',
        'scam1': '<strong>Parkuhr-Betrug:</strong> Gefälschte QR-Codes an Parkuhren führen zu Zahlungsseiten, die Kreditkartendaten stehlen',
        'scam2': '<strong>Paket-Betrug:</strong> Gefälschte "Verpasste Lieferung"-Benachrichtigungen mit QR-Codes zu Phishing-Seiten',
        'scam3': '<strong>Krypto-Betrug:</strong> QR-Codes, die kostenloses Bitcoin versprechen, aber Wallet-Daten stehlen',
        'scam4': '<strong>COVID-19-Betrug:</strong> Gefälschte Impf- oder Testergebnis-QR-Codes zu datensammelnden Seiten',
        'protect_title': 'So bleiben Sie sicher',
        'protect1_title': 'Vorschau vor dem Klicken',
        'protect1': 'Die meisten Telefone zeigen Ihnen die URL vor dem Öffnen. Überprüfen Sie immer die Domain.',
        'protect2_title': 'Auf Manipulation prüfen',
        'protect2': 'Wenn ein QR-Code wie ein Aufkleber über etwas anderem aussieht, seien Sie misstrauisch.',
        'protect3_title': 'Scanner mit Vorschau verwenden',
        'protect3': 'Einige Scanner-Apps zeigen den Link und bitten um Bestätigung. Die eingebaute Kamera-App auf iPhone und Android macht das.',
        'protect4_title': 'Telefon aktuell halten',
        'protect4': 'Updates schließen Sicherheitslücken. Ein aktualisiertes Telefon ist viel schwerer zu kompromittieren.',
        'protect5_title': 'Vertrauen Sie Ihrem Instinkt',
        'protect5': 'Zufällige QR-Codes an Laternenpfählen? Unaufgeforderte QR-Codes in E-Mails? Wenn es verdächtig erscheint, scannen Sie nicht.',
        'red_flags_title': '🚩 Warnsignale',
        'red_flags': [
            'QR-Code-Aufkleber über bestehenden Codes',
            'QR-Codes auf zufälligen Flyern ohne klare Quelle',
            'Anfrage nach sensiblen Daten nach dem Scannen',
            'URLs, die leicht "falsch" aussehen',
            'Druck, schnell zu handeln'
        ],
        'safe_uses_title': 'Wann QR-Codes generell sicher sind',
        'safe_uses': [
            '✅ Restaurant-Menüs (am Tisch, nicht auf zufälligen Aufklebern)',
            '✅ Produktverpackungen von vertrauenswürdigen Marken',
            '✅ Offizielle Apps und Websites bekannter Unternehmen',
            '✅ Event-Tickets von offiziellen Ticketing-Plattformen',
            '✅ Zwei-Faktor-Authentifizierung-Einrichtung',
            '✅ WLAN-Sharing in vertrauenswürdigen Umgebungen'
        ],
        'bottom_line_title': 'Das Fazit',
        'bottom_line': 'QR-Codes sind so sicher wie die Person oder Firma, die sie erstellt hat. Behandeln Sie das Scannen eines QR-Codes wie das Klicken auf einen Link.',
        'cta_title': 'Sichere QR-Codes erstellen',
        'cta_text': 'Wenn Sie QR-Codes bei uns erstellen, bekommen Sie was Sie sehen — kein Tracking, keine Weiterleitungen.',
        'cta_button': 'QR-Code erstellen →',
        'back': '← Zurück',
        'lang_name': 'Deutsch',
    },
    'es': {
        'title': '¿Son Seguros los Códigos QR? Riesgos de Seguridad y Protección',
        'meta': '¿Son seguros los códigos QR para escanear? Conoce los riesgos de seguridad, estafas comunes y cómo protegerte de códigos maliciosos.',
        'h1': '¿Son Seguros los Códigos QR?',
        'subtitle': 'Entendiendo los riesgos y cómo protegerte',
        'intro': 'Los códigos QR están en todas partes — ¿pero son seguros? La respuesta corta: <strong>los códigos QR en sí son seguros, pero a lo que enlazan podría no serlo</strong>. Analicemos los riesgos y cómo mantenerte protegido.',
        'tech_safe_title': 'La tecnología en sí es segura',
        'tech_safe_text': 'Un código QR es solo una forma visual de almacenar datos — como texto o una URL. El código en sí no puede instalar malware ni hackear tu teléfono. Es simplemente un formato de datos, como un código de barras.',
        'tech_safe_analogy': 'Piensa en un código QR como un sobre con una dirección. El sobre en sí es inofensivo — pero el destino al que apunta es lo que importa.',
        'risks_title': 'Los riesgos reales',
        'risk1_title': '1. Ataques de Phishing',
        'risk1': 'Un código QR malicioso podría enlazar a un sitio web falso que parece tu banco o email — diseñado para robar tus credenciales.',
        'risk2_title': '2. Descargas Maliciosas',
        'risk2': 'Algunos códigos QR podrían enlazar a sitios que intentan descargar malware, especialmente en dispositivos desactualizados.',
        'risk3_title': '3. Intercambio de QR',
        'risk3': 'Los criminales pueden poner pegatinas de códigos QR falsos sobre los legítimos — como en parquímetros o menús de restaurantes.',
        'risk4_title': '4. Recolección de Datos',
        'risk4': 'Algunos códigos QR enlazan a URLs de rastreo que recolectan tu ubicación e información del dispositivo sin revelación clara.',
        'real_scams_title': 'Estafas Reales con Códigos QR',
        'scam1': '<strong>Estafas en parquímetros:</strong> Códigos QR falsos llevan a sitios de pago que roban datos de tarjetas',
        'scam2': '<strong>Estafas de paquetes:</strong> Avisos falsos de "entrega perdida" con QR que llevan a sitios de phishing',
        'scam3': '<strong>Estafas cripto:</strong> Códigos QR prometiendo Bitcoin gratis que roban credenciales de billetera',
        'scam4': '<strong>Estafas COVID-19:</strong> QR falsos de vacunación o resultados de pruebas que llevan a sitios que roban datos',
        'protect_title': 'Cómo Mantenerte Seguro',
        'protect1_title': 'Vista previa antes de hacer clic',
        'protect1': 'La mayoría de teléfonos muestran la URL antes de abrirla. Siempre verifica el dominio.',
        'protect2_title': 'Busca manipulación',
        'protect2': 'Si un código QR parece una pegatina sobre algo más, desconfía.',
        'protect3_title': 'Usa un escáner con vista previa',
        'protect3': 'Algunas apps de escáner muestran el enlace y piden confirmación. La app de cámara integrada en iPhone y Android hace esto.',
        'protect4_title': 'Mantén tu teléfono actualizado',
        'protect4': 'Las actualizaciones parchean vulnerabilidades de seguridad. Un teléfono actualizado es mucho más difícil de comprometer.',
        'protect5_title': 'Confía en tus instintos',
        'protect5': '¿Códigos QR aleatorios en postes? ¿Códigos QR no solicitados en emails? Si parece sospechoso, no lo escanees.',
        'red_flags_title': '🚩 Señales de Alerta',
        'red_flags': [
            'Pegatinas de código QR sobre códigos existentes',
            'Códigos QR en volantes aleatorios sin fuente clara',
            'Solicitud de información sensible después de escanear',
            'URLs que lucen ligeramente "mal"',
            'Presión para actuar rápido'
        ],
        'safe_uses_title': 'Cuándo los Códigos QR Son Generalmente Seguros',
        'safe_uses': [
            '✅ Menús de restaurantes (en la mesa, no en pegatinas aleatorias)',
            '✅ Empaques de productos de marcas de confianza',
            '✅ Apps y sitios web oficiales de empresas conocidas',
            '✅ Entradas de eventos de plataformas oficiales',
            '✅ Configuración de autenticación de dos factores',
            '✅ Compartir WiFi en hogares y oficinas de confianza'
        ],
        'bottom_line_title': 'En Resumen',
        'bottom_line': 'Los códigos QR son tan seguros como la persona o empresa que los creó. Trata escanear un código QR como hacer clic en un enlace.',
        'cta_title': 'Crea Códigos QR Seguros',
        'cta_text': 'Cuando creas códigos QR con nosotros, lo que ves es lo que obtienes — sin rastreo, sin redirecciones.',
        'cta_button': 'Crear Código QR →',
        'back': '← Volver',
        'lang_name': 'Español',
    },
    'fr': {
        'title': 'Les QR Codes Sont-ils Sûrs? Risques de Sécurité & Protection',
        'meta': 'Les QR codes sont-ils sûrs à scanner? Découvrez les risques de sécurité, les arnaques courantes et comment vous protéger des codes malveillants.',
        'h1': 'Les QR Codes Sont-ils Sûrs?',
        'subtitle': 'Comprendre les risques et comment se protéger',
        'intro': 'Les QR codes sont partout — mais sont-ils sûrs? La réponse courte: <strong>les QR codes eux-mêmes sont sûrs, mais ce vers quoi ils pointent pourrait ne pas l\'être</strong>. Analysons les risques et comment rester protégé.',
        'tech_safe_title': 'La technologie elle-même est sûre',
        'tech_safe_text': 'Un QR code est juste une façon visuelle de stocker des données — comme du texte ou une URL. Le code lui-même ne peut pas installer de malware ou pirater votre téléphone. C\'est simplement un format de données, comme un code-barres.',
        'tech_safe_analogy': 'Pensez à un QR code comme une enveloppe avec une adresse. L\'enveloppe elle-même est inoffensive — mais la destination vers laquelle elle pointe est ce qui compte.',
        'risks_title': 'Les vrais risques',
        'risk1_title': '1. Attaques de Phishing',
        'risk1': 'Un QR code malveillant pourrait renvoyer vers un faux site web qui ressemble à votre banque ou email — conçu pour voler vos identifiants.',
        'risk2_title': '2. Téléchargements Malveillants',
        'risk2': 'Certains QR codes pourraient renvoyer vers des sites qui tentent de télécharger des malwares, surtout sur des appareils non mis à jour.',
        'risk3_title': '3. Échange de QR Code',
        'risk3': 'Les criminels peuvent placer de faux autocollants QR code sur les légitimes — comme sur les parcmètres ou menus de restaurant.',
        'risk4_title': '4. Collecte de Données',
        'risk4': 'Certains QR codes renvoient vers des URLs de suivi qui collectent votre localisation et infos appareil sans divulgation claire.',
        'real_scams_title': 'Arnaques Réelles aux QR Codes',
        'scam1': '<strong>Arnaques aux parcmètres:</strong> Faux QR codes menant à des sites de paiement volant les infos de carte',
        'scam2': '<strong>Arnaques livraison:</strong> Faux avis de "livraison manquée" avec QR codes vers des sites de phishing',
        'scam3': '<strong>Arnaques crypto:</strong> QR codes promettant du Bitcoin gratuit qui volent les identifiants de portefeuille',
        'scam4': '<strong>Arnaques COVID-19:</strong> Faux QR codes de vaccination ou résultats de tests vers des sites collectant des données',
        'protect_title': 'Comment Rester en Sécurité',
        'protect1_title': 'Prévisualiser avant de cliquer',
        'protect1': 'La plupart des téléphones montrent l\'URL avant de l\'ouvrir. Vérifiez toujours le domaine.',
        'protect2_title': 'Vérifier les manipulations',
        'protect2': 'Si un QR code ressemble à un autocollant placé sur autre chose, méfiez-vous.',
        'protect3_title': 'Utiliser un scanner avec prévisualisation',
        'protect3': 'Certaines apps de scan montrent le lien et demandent confirmation. L\'app appareil photo intégrée sur iPhone et Android fait cela.',
        'protect4_title': 'Garder votre téléphone à jour',
        'protect4': 'Les mises à jour corrigent les failles de sécurité. Un téléphone à jour est beaucoup plus difficile à compromettre.',
        'protect5_title': 'Faites confiance à votre instinct',
        'protect5': 'QR codes aléatoires sur des poteaux? QR codes non sollicités dans les emails? Si ça semble louche, ne scannez pas.',
        'red_flags_title': '🚩 Signaux d\'Alerte',
        'red_flags': [
            'Autocollants QR code placés sur des codes existants',
            'QR codes sur des flyers aléatoires sans source claire',
            'Demande d\'infos sensibles après le scan',
            'URLs qui semblent légèrement "fausses"',
            'Pression pour agir vite'
        ],
        'safe_uses_title': 'Quand les QR Codes Sont Généralement Sûrs',
        'safe_uses': [
            '✅ Menus de restaurants (à table, pas sur des autocollants aléatoires)',
            '✅ Emballages de produits de marques de confiance',
            '✅ Apps et sites officiels d\'entreprises connues',
            '✅ Billets d\'événements de plateformes officielles',
            '✅ Configuration d\'authentification à deux facteurs',
            '✅ Partage WiFi dans des environnements de confiance'
        ],
        'bottom_line_title': 'En Résumé',
        'bottom_line': 'Les QR codes sont aussi sûrs que la personne ou l\'entreprise qui les a créés. Traitez le scan d\'un QR code comme cliquer sur un lien.',
        'cta_title': 'Créez des QR Codes Sûrs',
        'cta_text': 'Quand vous créez des QR codes chez nous, ce que vous voyez est ce que vous obtenez — pas de suivi, pas de redirections.',
        'cta_button': 'Créer un QR Code →',
        'back': '← Retour',
        'lang_name': 'Français',
    },
    'pt': {
        'title': 'QR Codes São Seguros? Riscos de Segurança e Proteção',
        'meta': 'QR codes são seguros para escanear? Conheça os riscos de segurança, golpes comuns e como se proteger de códigos maliciosos.',
        'h1': 'QR Codes São Seguros?',
        'subtitle': 'Entendendo os riscos e como se proteger',
        'intro': 'QR codes estão em toda parte — mas são seguros? A resposta curta: <strong>QR codes em si são seguros, mas para onde eles direcionam pode não ser</strong>. Vamos analisar os riscos e como se manter protegido.',
        'tech_safe_title': 'A tecnologia em si é segura',
        'tech_safe_text': 'Um QR code é apenas uma forma visual de armazenar dados — como texto ou uma URL. O código em si não pode instalar malware ou hackear seu telefone. É simplesmente um formato de dados, como um código de barras.',
        'tech_safe_analogy': 'Pense em um QR code como um envelope com um endereço. O envelope em si é inofensivo — mas o destino para onde ele aponta é o que importa.',
        'risks_title': 'Os riscos reais',
        'risk1_title': '1. Ataques de Phishing',
        'risk1': 'Um QR code malicioso pode direcionar para um site falso que parece seu banco ou email — projetado para roubar suas credenciais.',
        'risk2_title': '2. Downloads Maliciosos',
        'risk2': 'Alguns QR codes podem direcionar para sites que tentam baixar malware, especialmente em dispositivos desatualizados.',
        'risk3_title': '3. Troca de QR Code',
        'risk3': 'Criminosos podem colocar adesivos de QR codes falsos sobre os legítimos — como em parquímetros ou cardápios de restaurantes.',
        'risk4_title': '4. Coleta de Dados',
        'risk4': 'Alguns QR codes direcionam para URLs de rastreamento que coletam sua localização e informações do dispositivo sem divulgação clara.',
        'real_scams_title': 'Golpes Reais com QR Codes',
        'scam1': '<strong>Golpes em parquímetros:</strong> QR codes falsos levam a sites de pagamento que roubam dados de cartão',
        'scam2': '<strong>Golpes de entrega:</strong> Avisos falsos de "entrega perdida" com QR codes para sites de phishing',
        'scam3': '<strong>Golpes cripto:</strong> QR codes prometendo Bitcoin grátis que roubam credenciais de carteira',
        'scam4': '<strong>Golpes COVID-19:</strong> QR codes falsos de vacinação ou resultados de testes para sites que coletam dados',
        'protect_title': 'Como Se Manter Seguro',
        'protect1_title': 'Visualize antes de clicar',
        'protect1': 'A maioria dos telefones mostra a URL antes de abrir. Sempre verifique o domínio.',
        'protect2_title': 'Verifique manipulação',
        'protect2': 'Se um QR code parece um adesivo colocado sobre algo, desconfie.',
        'protect3_title': 'Use um scanner com visualização',
        'protect3': 'Alguns apps de scanner mostram o link e pedem confirmação. O app de câmera nativo no iPhone e Android faz isso.',
        'protect4_title': 'Mantenha seu telefone atualizado',
        'protect4': 'Atualizações corrigem vulnerabilidades de segurança. Um telefone atualizado é muito mais difícil de comprometer.',
        'protect5_title': 'Confie em seus instintos',
        'protect5': 'QR codes aleatórios em postes? QR codes não solicitados em emails? Se parece suspeito, não escaneie.',
        'red_flags_title': '🚩 Sinais de Alerta',
        'red_flags': [
            'Adesivos de QR code sobre códigos existentes',
            'QR codes em panfletos aleatórios sem fonte clara',
            'Pedido de informações sensíveis após escanear',
            'URLs que parecem ligeiramente "erradas"',
            'Pressão para agir rápido'
        ],
        'safe_uses_title': 'Quando QR Codes São Geralmente Seguros',
        'safe_uses': [
            '✅ Cardápios de restaurantes (na mesa, não em adesivos aleatórios)',
            '✅ Embalagens de produtos de marcas confiáveis',
            '✅ Apps e sites oficiais de empresas conhecidas',
            '✅ Ingressos de eventos de plataformas oficiais',
            '✅ Configuração de autenticação de dois fatores',
            '✅ Compartilhamento de WiFi em ambientes confiáveis'
        ],
        'bottom_line_title': 'Resumindo',
        'bottom_line': 'QR codes são tão seguros quanto a pessoa ou empresa que os criou. Trate escanear um QR code como clicar em um link.',
        'cta_title': 'Crie QR Codes Seguros',
        'cta_text': 'Quando você cria QR codes conosco, o que você vê é o que você obtém — sem rastreamento, sem redirecionamentos.',
        'cta_button': 'Criar QR Code →',
        'back': '← Voltar',
        'lang_name': 'Português',
    },
    'zh': {
        'title': '二维码安全吗？安全风险与防护措施',
        'meta': '扫描二维码安全吗？了解二维码安全风险、常见骗局以及如何保护自己免受恶意代码的侵害。',
        'h1': '二维码安全吗？',
        'subtitle': '了解风险以及如何保护自己',
        'intro': '二维码无处不在——但它们安全吗？简短的回答：<strong>二维码本身是安全的，但它们链接到的内容可能不安全</strong>。让我们分析风险和如何保持安全。',
        'tech_safe_title': '技术本身是安全的',
        'tech_safe_text': '二维码只是一种可视化存储数据的方式——如文本或URL。代码本身不能安装恶意软件或入侵您的手机。它只是一种数据格式，就像条形码一样。',
        'tech_safe_analogy': '把二维码想象成一个有地址的信封。信封本身是无害的——但它指向的目的地才是关键。',
        'risks_title': '真正的风险',
        'risk1_title': '1. 钓鱼攻击',
        'risk1': '恶意二维码可能链接到看起来像您银行或邮箱的假网站——旨在窃取您的登录凭证。',
        'risk2_title': '2. 恶意下载',
        'risk2': '某些二维码可能链接到试图下载恶意软件的网站，特别是在过时的设备上。',
        'risk3_title': '3. 二维码替换',
        'risk3': '犯罪分子可以将假的二维码贴纸贴在合法的上面——如停车计时器或餐厅菜单上。',
        'risk4_title': '4. 数据收集',
        'risk4': '某些二维码链接到跟踪URL，在没有明确披露的情况下收集您的位置和设备信息。',
        'real_scams_title': '真实的二维码骗局',
        'scam1': '<strong>停车计时器骗局：</strong>假二维码导向窃取信用卡信息的支付网站',
        'scam2': '<strong>包裹递送骗局：</strong>带有二维码的假"错过递送"通知导向钓鱼网站',
        'scam3': '<strong>加密货币骗局：</strong>承诺免费比特币的二维码实际上窃取钱包凭证',
        'scam4': '<strong>COVID-19骗局：</strong>假疫苗接种或测试结果二维码链接到数据收集网站',
        'protect_title': '如何保持安全',
        'protect1_title': '点击前预览',
        'protect1': '大多数手机在打开前会显示URL。始终检查域名。',
        'protect2_title': '检查是否被篡改',
        'protect2': '如果二维码看起来像贴在其他东西上的贴纸，要警惕。',
        'protect3_title': '使用带预览的扫描器',
        'protect3': '某些扫描器应用会显示链接并要求确认。iPhone和Android上的内置相机应用会这样做。',
        'protect4_title': '保持手机更新',
        'protect4': '更新可修补安全漏洞。更新的手机更难被攻击。',
        'protect5_title': '相信你的直觉',
        'protect5': '路灯杆上的随机二维码？邮件中未经请求的二维码？如果看起来可疑，就不要扫描。',
        'red_flags_title': '🚩 危险信号',
        'red_flags': [
            '贴在现有代码上的二维码贴纸',
            '没有明确来源的随机传单上的二维码',
            '扫描后要求敏感信息',
            '看起来有点"不对劲"的URL',
            '催促快速行动的压力'
        ],
        'safe_uses_title': '二维码通常安全的情况',
        'safe_uses': [
            '✅ 餐厅菜单（在桌上，不是随机贴纸上）',
            '✅ 您信任的品牌的产品包装',
            '✅ 知名公司的官方应用和网站',
            '✅ 官方票务平台的活动门票',
            '✅ 双因素认证设置',
            '✅ 您信任的家庭和办公室的WiFi共享'
        ],
        'bottom_line_title': '总结',
        'bottom_line': '二维码的安全程度取决于创建它的人或公司。像点击链接一样对待扫描二维码。',
        'cta_title': '创建安全的二维码',
        'cta_text': '当您用我们创建二维码时，所见即所得——没有跟踪，没有重定向。',
        'cta_button': '创建二维码 →',
        'back': '← 返回',
        'lang_name': '中文',
    },
    'ja': {
        'title': 'QRコードは安全？セキュリティリスクと対策',
        'meta': 'QRコードをスキャンするのは安全ですか？QRコードのセキュリティリスク、一般的な詐欺、悪意のあるコードから身を守る方法について学びましょう。',
        'h1': 'QRコードは安全？',
        'subtitle': 'リスクを理解し、身を守る方法',
        'intro': 'QRコードはどこにでもあります — でも安全なのでしょうか？短い答え：<strong>QRコード自体は安全ですが、リンク先は安全でない可能性があります</strong>。リスクと対策を解説します。',
        'tech_safe_title': '技術自体は安全',
        'tech_safe_text': 'QRコードはデータを視覚的に保存する方法に過ぎません — テキストやURLのように。コード自体はマルウェアをインストールしたり、スマホをハッキングすることはできません。バーコードのような単なるデータ形式です。',
        'tech_safe_analogy': 'QRコードは住所が書かれた封筒のようなものです。封筒自体は無害ですが、それが指す目的地が重要です。',
        'risks_title': '本当のリスク',
        'risk1_title': '1. フィッシング攻撃',
        'risk1': '悪意のあるQRコードは、銀行やメールに見せかけた偽サイトにリンクし、ログイン情報を盗む可能性があります。',
        'risk2_title': '2. 悪意のあるダウンロード',
        'risk2': '一部のQRコードは、特に古いデバイスでマルウェアをダウンロードしようとするサイトにリンクする可能性があります。',
        'risk3_title': '3. QRコードの入れ替え',
        'risk3': '犯罪者は、駐車メーターやレストランのメニューなど、正規のQRコードの上に偽のステッカーを貼ることがあります。',
        'risk4_title': '4. データ収集',
        'risk4': '一部のQRコードは、明確な開示なしに位置情報やデバイス情報を収集するトラッキングURLにリンクします。',
        'real_scams_title': '実際のQRコード詐欺',
        'scam1': '<strong>駐車メーター詐欺：</strong>偽のQRコードがクレジットカード情報を盗む支払いサイトに誘導',
        'scam2': '<strong>配達詐欺：</strong>フィッシングサイトにつながるQRコード付きの偽の「不在配達」通知',
        'scam3': '<strong>暗号通貨詐欺：</strong>無料のビットコインを約束するQRコードが実際にはウォレット認証情報を盗む',
        'scam4': '<strong>COVID-19詐欺：</strong>データ収集サイトにリンクする偽のワクチン接種や検査結果のQRコード',
        'protect_title': '安全を保つ方法',
        'protect1_title': 'クリック前にプレビュー',
        'protect1': 'ほとんどのスマホは開く前にURLを表示します。常にドメインを確認してください。',
        'protect2_title': '改ざんをチェック',
        'protect2': 'QRコードが何かの上に貼られたステッカーのように見えたら、警戒してください。',
        'protect3_title': 'プレビュー機能付きスキャナーを使用',
        'protect3': '一部のスキャナーアプリはリンクを表示し、確認を求めます。iPhoneとAndroidの内蔵カメラアプリはこれを行います。',
        'protect4_title': 'スマホを最新に保つ',
        'protect4': 'アップデートはセキュリティ脆弱性を修正します。最新のスマホは攻撃されにくくなります。',
        'protect5_title': '直感を信じる',
        'protect5': '電柱のランダムなQRコード？メールの未承諾QRコード？怪しいと思ったら、スキャンしないでください。',
        'red_flags_title': '🚩 危険信号',
        'red_flags': [
            '既存のコードの上に貼られたQRコードステッカー',
            '出所不明のランダムなチラシのQRコード',
            'スキャン後に機密情報を求められる',
            '少し「おかしい」URL',
            '急いで行動するよう圧力'
        ],
        'safe_uses_title': 'QRコードが一般的に安全な場合',
        'safe_uses': [
            '✅ レストランメニュー（テーブルで、ランダムなステッカーではなく）',
            '✅ 信頼できるブランドの製品パッケージ',
            '✅ 有名企業の公式アプリとウェブサイト',
            '✅ 公式チケットプラットフォームからのイベントチケット',
            '✅ 二要素認証の設定',
            '✅ 信頼できる家庭やオフィスでのWiFi共有'
        ],
        'bottom_line_title': '結論',
        'bottom_line': 'QRコードは、それを作成した人や会社と同じくらい安全です。QRコードのスキャンをリンクのクリックと同じように扱ってください。',
        'cta_title': '安全なQRコードを作成',
        'cta_text': '私たちでQRコードを作成すると、見たままのものが得られます — トラッキングなし、リダイレクトなし。',
        'cta_button': 'QRコードを作成 →',
        'back': '← 戻る',
        'lang_name': '日本語',
    },
    'ar': {
        'title': 'هل رموز QR آمنة؟ مخاطر الأمان وكيفية الحماية',
        'meta': 'هل رموز QR آمنة للمسح؟ تعرف على مخاطر أمان رموز QR والاحتيالات الشائعة وكيفية حماية نفسك من الرموز الضارة.',
        'h1': 'هل رموز QR آمنة؟',
        'subtitle': 'فهم المخاطر وكيفية حماية نفسك',
        'intro': 'رموز QR في كل مكان — لكن هل هي آمنة؟ الإجابة القصيرة: <strong>رموز QR نفسها آمنة، لكن ما ترتبط به قد لا يكون كذلك</strong>. دعنا نحلل المخاطر وكيفية البقاء محمياً.',
        'tech_safe_title': 'التقنية نفسها آمنة',
        'tech_safe_text': 'رمز QR هو مجرد طريقة بصرية لتخزين البيانات — مثل النص أو URL. الرمز نفسه لا يمكنه تثبيت برامج ضارة أو اختراق هاتفك. إنه ببساطة صيغة بيانات، مثل الباركود.',
        'tech_safe_analogy': 'فكر في رمز QR كظرف بعنوان. الظرف نفسه غير ضار — لكن الوجهة التي يشير إليها هي المهمة.',
        'risks_title': 'المخاطر الحقيقية',
        'risk1_title': '1. هجمات التصيد',
        'risk1': 'رمز QR ضار قد يرتبط بموقع مزيف يبدو مثل بنكك أو بريدك — مصمم لسرقة بيانات الدخول.',
        'risk2_title': '2. التنزيلات الضارة',
        'risk2': 'بعض رموز QR قد ترتبط بمواقع تحاول تنزيل برامج ضارة، خاصة على الأجهزة القديمة.',
        'risk3_title': '3. استبدال رمز QR',
        'risk3': 'المجرمون يمكنهم وضع ملصقات رموز QR مزيفة فوق الشرعية — مثل على عدادات الوقوف أو قوائم المطاعم.',
        'risk4_title': '4. جمع البيانات',
        'risk4': 'بعض رموز QR ترتبط بروابط تتبع تجمع موقعك ومعلومات جهازك دون إفصاح واضح.',
        'real_scams_title': 'احتيالات رموز QR الحقيقية',
        'scam1': '<strong>احتيال عدادات الوقوف:</strong> رموز QR مزيفة تؤدي إلى مواقع دفع تسرق معلومات البطاقة',
        'scam2': '<strong>احتيال التوصيل:</strong> إشعارات "تسليم فائت" مزيفة مع رموز QR تؤدي إلى مواقع تصيد',
        'scam3': '<strong>احتيال العملات المشفرة:</strong> رموز QR تعد ببيتكوين مجاني تسرق بيانات المحفظة',
        'scam4': '<strong>احتيال COVID-19:</strong> رموز QR مزيفة للتطعيم أو نتائج الفحص ترتبط بمواقع جمع البيانات',
        'protect_title': 'كيف تبقى آمناً',
        'protect1_title': 'معاينة قبل النقر',
        'protect1': 'معظم الهواتف تظهر لك URL قبل فتحه. تحقق دائماً من النطاق.',
        'protect2_title': 'تحقق من التلاعب',
        'protect2': 'إذا بدا رمز QR كملصق موضوع فوق شيء آخر، كن حذراً.',
        'protect3_title': 'استخدم ماسح مع معاينة',
        'protect3': 'بعض تطبيقات المسح تظهر الرابط وتطلب التأكيد. تطبيق الكاميرا المدمج في iPhone وAndroid يفعل ذلك.',
        'protect4_title': 'حافظ على تحديث هاتفك',
        'protect4': 'التحديثات تصلح الثغرات الأمنية. الهاتف المحدث أصعب في الاختراق.',
        'protect5_title': 'ثق بحدسك',
        'protect5': 'رموز QR عشوائية على أعمدة الشارع؟ رموز QR غير مطلوبة في الإيميلات؟ إذا بدت مشبوهة، لا تمسحها.',
        'red_flags_title': '🚩 علامات التحذير',
        'red_flags': [
            'ملصقات رموز QR موضوعة فوق رموز موجودة',
            'رموز QR على منشورات عشوائية بدون مصدر واضح',
            'طلب معلومات حساسة بعد المسح',
            'روابط تبدو "خاطئة" قليلاً',
            'ضغط للتصرف بسرعة'
        ],
        'safe_uses_title': 'متى تكون رموز QR آمنة عموماً',
        'safe_uses': [
            '✅ قوائم المطاعم (على الطاولة، ليس على ملصقات عشوائية)',
            '✅ تغليف منتجات من علامات تجارية موثوقة',
            '✅ تطبيقات ومواقع رسمية لشركات معروفة',
            '✅ تذاكر الفعاليات من منصات التذاكر الرسمية',
            '✅ إعداد المصادقة الثنائية',
            '✅ مشاركة WiFi في المنازل والمكاتب الموثوقة'
        ],
        'bottom_line_title': 'الخلاصة',
        'bottom_line': 'رموز QR آمنة بقدر الشخص أو الشركة التي أنشأتها. تعامل مع مسح رمز QR كالنقر على رابط.',
        'cta_title': 'أنشئ رموز QR آمنة',
        'cta_text': 'عندما تنشئ رموز QR معنا، ما تراه هو ما تحصل عليه — بدون تتبع، بدون إعادات توجيه.',
        'cta_button': 'إنشاء رمز QR ←',
        'back': 'رجوع ←',
        'lang_name': 'العربية',
    },
    'hi': {
        'title': 'क्या QR कोड सुरक्षित हैं? सुरक्षा जोखिम और बचाव',
        'meta': 'क्या QR कोड स्कैन करना सुरक्षित है? QR कोड सुरक्षा जोखिमों, सामान्य घोटालों और खुद को दुर्भावनापूर्ण कोड से कैसे बचाएं, यह जानें।',
        'h1': 'क्या QR कोड सुरक्षित हैं?',
        'subtitle': 'जोखिमों को समझना और खुद को कैसे बचाएं',
        'intro': 'QR कोड हर जगह हैं — लेकिन क्या वे सुरक्षित हैं? संक्षिप्त उत्तर: <strong>QR कोड स्वयं सुरक्षित हैं, लेकिन वे जिससे लिंक करते हैं वह नहीं हो सकता</strong>। आइए जोखिमों और सुरक्षित रहने के तरीकों को समझें।',
        'tech_safe_title': 'तकनीक स्वयं सुरक्षित है',
        'tech_safe_text': 'QR कोड डेटा संग्रहीत करने का सिर्फ एक दृश्य तरीका है — जैसे टेक्स्ट या URL। कोड स्वयं मैलवेयर इंस्टॉल नहीं कर सकता या आपके फोन को हैक नहीं कर सकता। यह बारकोड की तरह बस एक डेटा प्रारूप है।',
        'tech_safe_analogy': 'QR कोड को एक पते वाले लिफाफे की तरह सोचें। लिफाफा स्वयं हानिरहित है — लेकिन जिस गंतव्य को यह इंगित करता है वह मायने रखता है।',
        'risks_title': 'वास्तविक जोखिम',
        'risk1_title': '1. फ़िशिंग हमले',
        'risk1': 'एक दुर्भावनापूर्ण QR कोड आपके बैंक या ईमेल जैसी दिखने वाली नकली वेबसाइट से लिंक कर सकता है — आपके लॉगिन क्रेडेंशियल चुराने के लिए डिज़ाइन किया गया।',
        'risk2_title': '2. दुर्भावनापूर्ण डाउनलोड',
        'risk2': 'कुछ QR कोड उन वेबसाइटों से लिंक हो सकते हैं जो मैलवेयर डाउनलोड करने का प्रयास करती हैं, विशेष रूप से पुराने उपकरणों पर।',
        'risk3_title': '3. QR कोड स्वैपिंग',
        'risk3': 'अपराधी वैध QR कोड के ऊपर नकली QR कोड स्टिकर लगा सकते हैं — जैसे पार्किंग मीटर या रेस्तरां मेन्यू पर।',
        'risk4_title': '4. डेटा संग्रह',
        'risk4': 'कुछ QR कोड ट्रैकिंग URL से लिंक करते हैं जो बिना स्पष्ट खुलासे के आपका स्थान और डिवाइस जानकारी एकत्र करते हैं।',
        'real_scams_title': 'वास्तविक QR कोड घोटाले',
        'scam1': '<strong>पार्किंग मीटर घोटाले:</strong> नकली QR कोड क्रेडिट कार्ड जानकारी चुराने वाली भुगतान साइटों पर ले जाते हैं',
        'scam2': '<strong>पैकेज डिलीवरी घोटाले:</strong> फ़िशिंग साइटों पर जाने वाले QR कोड के साथ नकली "मिस्ड डिलीवरी" नोटिस',
        'scam3': '<strong>क्रिप्टो घोटाले:</strong> मुफ्त बिटकॉइन का वादा करने वाले QR कोड जो वास्तव में वॉलेट क्रेडेंशियल चुराते हैं',
        'scam4': '<strong>COVID-19 घोटाले:</strong> डेटा-संग्रह साइटों से जुड़े नकली टीकाकरण या परीक्षण परिणाम QR कोड',
        'protect_title': 'सुरक्षित कैसे रहें',
        'protect1_title': 'क्लिक करने से पहले प्रीव्यू करें',
        'protect1': 'अधिकांश फोन खोलने से पहले URL दिखाते हैं। हमेशा डोमेन जांचें।',
        'protect2_title': 'छेड़छाड़ की जांच करें',
        'protect2': 'यदि QR कोड किसी अन्य चीज़ पर चिपकाया गया स्टिकर जैसा दिखता है, तो सतर्क रहें।',
        'protect3_title': 'प्रीव्यू वाले स्कैनर का उपयोग करें',
        'protect3': 'कुछ स्कैनर ऐप्स लिंक दिखाते हैं और खोलने से पहले पुष्टि मांगते हैं। iPhone और Android पर बिल्ट-इन कैमरा ऐप यह करता है।',
        'protect4_title': 'अपना फोन अपडेट रखें',
        'protect4': 'अपडेट सुरक्षा कमजोरियों को ठीक करते हैं। अपडेटेड फोन को समझौता करना बहुत कठिन है।',
        'protect5_title': 'अपनी सहज बुद्धि पर भरोसा करें',
        'protect5': 'सड़क के खंभों पर यादृच्छिक QR कोड? ईमेल में अनचाहे QR कोड? यदि यह संदिग्ध लगता है, तो स्कैन न करें।',
        'red_flags_title': '🚩 चेतावनी के संकेत',
        'red_flags': [
            'मौजूदा कोड पर चिपकाए गए QR कोड स्टिकर',
            'बिना स्पष्ट स्रोत के यादृच्छिक फ्लायर्स पर QR कोड',
            'स्कैन करने के बाद संवेदनशील जानकारी मांगना',
            'URL जो थोड़े "गलत" दिखते हैं',
            'जल्दी कार्य करने का दबाव'
        ],
        'safe_uses_title': 'जब QR कोड आमतौर पर सुरक्षित होते हैं',
        'safe_uses': [
            '✅ रेस्तरां मेन्यू (टेबल पर, यादृच्छिक स्टिकर पर नहीं)',
            '✅ विश्वसनीय ब्रांडों की उत्पाद पैकेजिंग',
            '✅ ज्ञात कंपनियों के आधिकारिक ऐप्स और वेबसाइटें',
            '✅ आधिकारिक टिकटिंग प्लेटफॉर्म से इवेंट टिकट',
            '✅ दो-कारक प्रमाणीकरण सेटअप',
            '✅ विश्वसनीय घरों और कार्यालयों में WiFi शेयरिंग'
        ],
        'bottom_line_title': 'सारांश',
        'bottom_line': 'QR कोड उतने ही सुरक्षित हैं जितना उन्हें बनाने वाला व्यक्ति या कंपनी। QR कोड स्कैन करने को लिंक पर क्लिक करने जैसा मानें।',
        'cta_title': 'सुरक्षित QR कोड बनाएं',
        'cta_text': 'जब आप हमारे साथ QR कोड बनाते हैं, तो जो आप देखते हैं वही आपको मिलता है — कोई ट्रैकिंग नहीं, कोई रीडायरेक्ट नहीं।',
        'cta_button': 'QR कोड बनाएं →',
        'back': '← वापस',
        'lang_name': 'हिन्दी',
    },
    'ru': {
        'title': 'Безопасны ли QR-коды? Риски безопасности и защита',
        'meta': 'Безопасно ли сканировать QR-коды? Узнайте о рисках безопасности QR-кодов, распространённых мошенничествах и как защититься от вредоносных кодов.',
        'h1': 'Безопасны ли QR-коды?',
        'subtitle': 'Понимание рисков и способы защиты',
        'intro': 'QR-коды повсюду — но безопасны ли они? Короткий ответ: <strong>сами QR-коды безопасны, но то, на что они ссылаются, может быть опасным</strong>. Разберём риски и способы защиты.',
        'tech_safe_title': 'Сама технология безопасна',
        'tech_safe_text': 'QR-код — это просто визуальный способ хранения данных — текста или URL. Сам код не может установить вредоносное ПО или взломать ваш телефон. Это просто формат данных, как штрих-код.',
        'tech_safe_analogy': 'Представьте QR-код как конверт с адресом. Сам конверт безвреден — но пункт назначения имеет значение.',
        'risks_title': 'Реальные риски',
        'risk1_title': '1. Фишинговые атаки',
        'risk1': 'Вредоносный QR-код может вести на поддельный сайт, похожий на ваш банк или почту — созданный для кражи учётных данных.',
        'risk2_title': '2. Вредоносные загрузки',
        'risk2': 'Некоторые QR-коды могут вести на сайты, пытающиеся загрузить вредоносное ПО, особенно на устаревших устройствах.',
        'risk3_title': '3. Подмена QR-кода',
        'risk3': 'Преступники могут наклеивать поддельные QR-коды поверх настоящих — на паркоматах или меню ресторанов.',
        'risk4_title': '4. Сбор данных',
        'risk4': 'Некоторые QR-коды ведут на URL-адреса отслеживания, собирающие ваше местоположение и данные устройства без явного уведомления.',
        'real_scams_title': 'Реальные мошенничества с QR-кодами',
        'scam1': '<strong>Мошенничество на паркоматах:</strong> Поддельные QR-коды ведут на платёжные сайты, крадущие данные карт',
        'scam2': '<strong>Мошенничество с доставкой:</strong> Поддельные уведомления о "пропущенной доставке" с QR-кодами на фишинговые сайты',
        'scam3': '<strong>Крипто-мошенничество:</strong> QR-коды, обещающие бесплатный биткоин, крадут данные кошелька',
        'scam4': '<strong>COVID-19 мошенничество:</strong> Поддельные QR-коды вакцинации или результатов тестов, ведущие на сайты сбора данных',
        'protect_title': 'Как оставаться в безопасности',
        'protect1_title': 'Просматривайте перед кликом',
        'protect1': 'Большинство телефонов показывают URL перед открытием. Всегда проверяйте домен.',
        'protect2_title': 'Проверяйте на подделку',
        'protect2': 'Если QR-код выглядит как наклейка поверх чего-то, будьте осторожны.',
        'protect3_title': 'Используйте сканер с предпросмотром',
        'protect3': 'Некоторые приложения-сканеры показывают ссылку и просят подтверждение. Встроенное приложение камеры на iPhone и Android делает это.',
        'protect4_title': 'Обновляйте телефон',
        'protect4': 'Обновления исправляют уязвимости. Обновлённый телефон намного сложнее взломать.',
        'protect5_title': 'Доверяйте интуиции',
        'protect5': 'Случайные QR-коды на столбах? Непрошенные QR-коды в письмах? Если выглядит подозрительно — не сканируйте.',
        'red_flags_title': '🚩 Тревожные сигналы',
        'red_flags': [
            'Наклейки QR-кодов поверх существующих кодов',
            'QR-коды на случайных листовках без ясного источника',
            'Запрос конфиденциальной информации после сканирования',
            'URL, которые выглядят слегка "неправильно"',
            'Давление действовать быстро'
        ],
        'safe_uses_title': 'Когда QR-коды обычно безопасны',
        'safe_uses': [
            '✅ Меню ресторанов (на столе, не на случайных наклейках)',
            '✅ Упаковка продуктов от проверенных брендов',
            '✅ Официальные приложения и сайты известных компаний',
            '✅ Билеты на мероприятия от официальных платформ',
            '✅ Настройка двухфакторной аутентификации',
            '✅ Обмен WiFi в доверенных местах'
        ],
        'bottom_line_title': 'Итог',
        'bottom_line': 'QR-коды так же безопасны, как человек или компания, создавшие их. Относитесь к сканированию QR-кода как к клику по ссылке.',
        'cta_title': 'Создавайте безопасные QR-коды',
        'cta_text': 'Когда вы создаёте QR-коды у нас, вы получаете то, что видите — без отслеживания, без перенаправлений.',
        'cta_button': 'Создать QR-код →',
        'back': '← Назад',
        'lang_name': 'Русский',
    },
    'tr': {
        'title': 'QR Kodları Güvenli mi? Güvenlik Riskleri ve Korunma',
        'meta': 'QR kodları taramak güvenli mi? QR kod güvenlik riskleri, yaygın dolandırıcılıklar ve kötü amaçlı kodlardan nasıl korunacağınızı öğrenin.',
        'h1': 'QR Kodları Güvenli mi?',
        'subtitle': 'Riskleri anlamak ve kendinizi korumak',
        'intro': 'QR kodlar her yerde — ama güvenli mi? Kısa cevap: <strong>QR kodların kendisi güvenlidir, ancak bağlandıkları şey olmayabilir</strong>. Riskleri ve nasıl korunacağınızı inceleyelim.',
        'tech_safe_title': 'Teknolojinin kendisi güvenli',
        'tech_safe_text': 'QR kod sadece veri depolamanın görsel bir yoludur — metin veya URL gibi. Kodun kendisi kötü amaçlı yazılım yükleyemez veya telefonunuzu hackleyemez. Barkod gibi sadece bir veri formatıdır.',
        'tech_safe_analogy': 'QR kodu adres yazılı bir zarf gibi düşünün. Zarfın kendisi zararsızdır — ancak işaret ettiği hedef önemlidir.',
        'risks_title': 'Gerçek riskler',
        'risk1_title': '1. Kimlik Avı Saldırıları',
        'risk1': 'Kötü amaçlı bir QR kod, bankanıza veya e-postanıza benzeyen sahte bir web sitesine yönlendirebilir — giriş bilgilerinizi çalmak için tasarlanmış.',
        'risk2_title': '2. Kötü Amaçlı İndirmeler',
        'risk2': 'Bazı QR kodlar, özellikle eski cihazlarda kötü amaçlı yazılım indirmeye çalışan sitelere bağlanabilir.',
        'risk3_title': '3. QR Kod Değiştirme',
        'risk3': 'Suçlular sahte QR kod etiketlerini meşru olanların üzerine yapıştırabilir — park sayaçları veya restoran menüleri gibi.',
        'risk4_title': '4. Veri Toplama',
        'risk4': 'Bazı QR kodlar, açık bir bildirim olmadan konumunuzu ve cihaz bilgilerinizi toplayan izleme URL\'lerine bağlanır.',
        'real_scams_title': 'Gerçek QR Kod Dolandırıcılıkları',
        'scam1': '<strong>Park sayacı dolandırıcılığı:</strong> Sahte QR kodlar kredi kartı bilgilerini çalan ödeme sitelerine yönlendiriyor',
        'scam2': '<strong>Kargo dolandırıcılığı:</strong> Kimlik avı sitelerine yönlendiren QR kodlu sahte "kaçırılan teslimat" bildirimleri',
        'scam3': '<strong>Kripto dolandırıcılığı:</strong> Ücretsiz Bitcoin vaat eden QR kodlar aslında cüzdan bilgilerini çalıyor',
        'scam4': '<strong>COVID-19 dolandırıcılığı:</strong> Veri toplama sitelerine bağlanan sahte aşı veya test sonucu QR kodları',
        'protect_title': 'Nasıl Güvende Kalınır',
        'protect1_title': 'Tıklamadan önce önizleyin',
        'protect1': 'Çoğu telefon açmadan önce URL\'yi gösterir. Her zaman alan adını kontrol edin.',
        'protect2_title': 'Kurcalamayı kontrol edin',
        'protect2': 'Bir QR kod başka bir şeyin üzerine yapıştırılmış bir etiket gibi görünüyorsa, şüphelenin.',
        'protect3_title': 'Önizlemeli tarayıcı kullanın',
        'protect3': 'Bazı tarayıcı uygulamaları linki gösterir ve onay ister. iPhone ve Android\'deki yerleşik kamera uygulaması bunu yapar.',
        'protect4_title': 'Telefonunuzu güncel tutun',
        'protect4': 'Güncellemeler güvenlik açıklarını düzeltir. Güncel bir telefonu tehlikeye atmak çok daha zordur.',
        'protect5_title': 'İçgüdülerinize güvenin',
        'protect5': 'Sokak direklerinde rastgele QR kodlar? E-postalarda istenmeyen QR kodlar? Şüpheli görünüyorsa, taramayın.',
        'red_flags_title': '🚩 Uyarı İşaretleri',
        'red_flags': [
            'Mevcut kodların üzerine yapıştırılmış QR kod etiketleri',
            'Açık kaynağı olmayan rastgele el ilanlarındaki QR kodlar',
            'Taradıktan sonra hassas bilgi istenmesi',
            'Biraz "yanlış" görünen URL\'ler',
            'Hızlı hareket etme baskısı'
        ],
        'safe_uses_title': 'QR Kodların Genellikle Güvenli Olduğu Durumlar',
        'safe_uses': [
            '✅ Restoran menüleri (masada, rastgele etiketlerde değil)',
            '✅ Güvendiğiniz markaların ürün ambalajları',
            '✅ Bilinen şirketlerin resmi uygulamaları ve web siteleri',
            '✅ Resmi biletleme platformlarından etkinlik biletleri',
            '✅ İki faktörlü kimlik doğrulama kurulumu',
            '✅ Güvendiğiniz evlerde ve ofislerde WiFi paylaşımı'
        ],
        'bottom_line_title': 'Sonuç',
        'bottom_line': 'QR kodlar, onları oluşturan kişi veya şirket kadar güvenlidir. QR kod taramayı bir linke tıklamak gibi değerlendirin.',
        'cta_title': 'Güvenli QR Kodlar Oluşturun',
        'cta_text': 'Bizimle QR kod oluşturduğunuzda, gördüğünüz şey aldığınız şeydir — izleme yok, yönlendirme yok.',
        'cta_button': 'QR Kodu Oluştur →',
        'back': '← Geri',
        'lang_name': 'Türkçe',
    },
}


def generate_how_qr_works(t, lang):
    """Generate How QR Codes Work article."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    base_path = '../' if lang == 'en' else '../../'
    
    steps_html = ''.join([f'<li class="flex gap-3 items-start"><span class="bg-indigo-100 text-indigo-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0 mt-0.5">{i+1}</span><span>{s}</span></li>' for i, s in enumerate(t['how_scan_steps'])])
    error_html = ''.join([f'<li>{e}</li>' for e in t['error_levels']])
    types_html = ''.join([f'<li>{typ}</li>' for typ in t['types']])
    why_html = ''.join([f'<li>{w}</li>' for w in t['why_popular']])
    facts_html = ''.join([f'<li>{f}</li>' for f in t['fun_facts']])
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    <link rel="canonical" href="https://qrcodes.win/blog/{'' if lang == 'en' else lang + '/'}how-qr-codes-work/">
    <link rel="icon" href="{base_path}favicon.svg" type="image/svg+xml">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{t['h1']}","description":"{t['meta']}","author":{{"@type":"Organization","name":"QRCodes.win"}},"publisher":{{"@type":"Organization","name":"QRCodes.win"}},"datePublished":"2026-02-20"}}
    </script>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #4F46E5; }}
        .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #6366f1; }}
        .prose p {{ margin-bottom: 1rem; color: #374151; line-height: 1.7; }}
        .prose ul, .prose ol {{ margin-left: 1.5rem; margin-bottom: 1rem; color: #374151; }}
        .prose ul {{ list-style: disc; }}
        .prose ol {{ list-style: decimal; }}
        .prose li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body class="text-gray-900">
    <header class="py-6 px-4">
        <div class="max-w-3xl mx-auto flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-2 text-white">
                <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center text-xl">📱</div>
                <span class="text-xl font-bold">QRCodes.win</span>
            </a>
            <a href="{base_path}" class="text-white/80 hover:text-white text-sm">{t['back']}</a>
        </div>
    </header>

    <main class="px-4 pb-16">
        <article class="max-w-3xl mx-auto">
            <div class="text-center mb-8 text-white">
                <h1 class="text-3xl md:text-4xl font-bold mb-2">{t['h1']}</h1>
                <p class="text-white/70">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-10 prose">
                <p class="text-lg">{t['intro']}</p>

                <h2>{t['what_title']}</h2>
                <p>{t['what_text']}</p>
                <p class="bg-indigo-50 p-4 rounded-xl border-l-4 border-indigo-500">{t['what_capacity']}</p>

                <h2>{t['anatomy_title']}</h2>
                <p>{t['anatomy_intro']}</p>
                <div class="space-y-3 my-4">
                    <div class="p-3 bg-gray-50 rounded-lg"><strong class="text-indigo-600">{t['anatomy_1_title']}:</strong> {t['anatomy_1']}</div>
                    <div class="p-3 bg-gray-50 rounded-lg"><strong class="text-indigo-600">{t['anatomy_2_title']}:</strong> {t['anatomy_2']}</div>
                    <div class="p-3 bg-gray-50 rounded-lg"><strong class="text-indigo-600">{t['anatomy_3_title']}:</strong> {t['anatomy_3']}</div>
                    <div class="p-3 bg-gray-50 rounded-lg"><strong class="text-indigo-600">{t['anatomy_4_title']}:</strong> {t['anatomy_4']}</div>
                    <div class="p-3 bg-gray-50 rounded-lg"><strong class="text-indigo-600">{t['anatomy_5_title']}:</strong> {t['anatomy_5']}</div>
                </div>

                <h2>{t['how_scan_title']}</h2>
                <ol class="space-y-2 list-none ml-0">{steps_html}</ol>

                <h2>{t['error_title']}</h2>
                <p>{t['error_text']}</p>
                <ul>{error_html}</ul>

                <h2>{t['types_title']}</h2>
                <ul class="grid grid-cols-2 gap-2">{types_html}</ul>

                <h2>{t['static_dynamic_title']}</h2>
                <div class="grid md:grid-cols-2 gap-4 my-4">
                    <div class="p-4 bg-green-50 rounded-xl border border-green-200">
                        <h3 class="text-green-700 mt-0">{t['static_title']}</h3>
                        <p class="text-green-800 text-sm mb-0">{t['static_text']}</p>
                    </div>
                    <div class="p-4 bg-blue-50 rounded-xl border border-blue-200">
                        <h3 class="text-blue-700 mt-0">{t['dynamic_title']}</h3>
                        <p class="text-blue-800 text-sm mb-0">{t['dynamic_text']}</p>
                    </div>
                </div>

                <h2>{t['why_popular_title']}</h2>
                <ul>{why_html}</ul>

                <h2>{t['fun_facts_title']}</h2>
                <ul class="bg-amber-50 p-4 rounded-xl">{facts_html}</ul>

                <div class="mt-8 p-6 bg-indigo-100 rounded-xl text-center">
                    <h3 class="text-indigo-800 mt-0">{t['cta_title']}</h3>
                    <p class="text-indigo-700">{t['cta_text']}</p>
                    <a href="{base_path}" class="inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-6 py-3 rounded-xl mt-2">{t['cta_button']}</a>
                </div>
            </div>
        </article>
    </main>
</body>
</html>'''


def generate_qr_safe(t, lang):
    """Generate Are QR Codes Safe article."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    base_path = '../' if lang == 'en' else '../../'
    
    red_flags_html = ''.join([f'<li>{f}</li>' for f in t['red_flags']])
    safe_uses_html = ''.join([f'<li>{u}</li>' for u in t['safe_uses']])
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    <link rel="canonical" href="https://qrcodes.win/blog/{'' if lang == 'en' else lang + '/'}qr-code-safety/">
    <link rel="icon" href="{base_path}favicon.svg" type="image/svg+xml">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{t['h1']}","description":"{t['meta']}","author":{{"@type":"Organization","name":"QRCodes.win"}},"publisher":{{"@type":"Organization","name":"QRCodes.win"}},"datePublished":"2026-02-20"}}
    </script>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #dc2626; }}
        .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #b91c1c; }}
        .prose p {{ margin-bottom: 1rem; color: #374151; line-height: 1.7; }}
        .prose ul {{ list-style: disc; margin-left: 1.5rem; margin-bottom: 1rem; color: #374151; }}
        .prose li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body class="text-gray-900">
    <header class="py-6 px-4">
        <div class="max-w-3xl mx-auto flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-2 text-white">
                <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center text-xl">🔒</div>
                <span class="text-xl font-bold">QRCodes.win</span>
            </a>
            <a href="{base_path}" class="text-white/80 hover:text-white text-sm">{t['back']}</a>
        </div>
    </header>

    <main class="px-4 pb-16">
        <article class="max-w-3xl mx-auto">
            <div class="text-center mb-8 text-white">
                <h1 class="text-3xl md:text-4xl font-bold mb-2">{t['h1']}</h1>
                <p class="text-white/70">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-10 prose">
                <p class="text-lg">{t['intro']}</p>

                <h2>✅ {t['tech_safe_title']}</h2>
                <p>{t['tech_safe_text']}</p>
                <p class="bg-green-50 p-4 rounded-xl border-l-4 border-green-500 italic">{t['tech_safe_analogy']}</p>

                <h2>⚠️ {t['risks_title']}</h2>
                <div class="space-y-4">
                    <div class="p-4 bg-red-50 rounded-xl border-l-4 border-red-400">
                        <h3 class="mt-0 text-red-700">{t['risk1_title']}</h3>
                        <p class="mb-0 text-red-800">{t['risk1']}</p>
                    </div>
                    <div class="p-4 bg-red-50 rounded-xl border-l-4 border-red-400">
                        <h3 class="mt-0 text-red-700">{t['risk2_title']}</h3>
                        <p class="mb-0 text-red-800">{t['risk2']}</p>
                    </div>
                    <div class="p-4 bg-red-50 rounded-xl border-l-4 border-red-400">
                        <h3 class="mt-0 text-red-700">{t['risk3_title']}</h3>
                        <p class="mb-0 text-red-800">{t['risk3']}</p>
                    </div>
                    <div class="p-4 bg-red-50 rounded-xl border-l-4 border-red-400">
                        <h3 class="mt-0 text-red-700">{t['risk4_title']}</h3>
                        <p class="mb-0 text-red-800">{t['risk4']}</p>
                    </div>
                </div>

                <h2>🚨 {t['real_scams_title']}</h2>
                <ul>
                    <li>{t['scam1']}</li>
                    <li>{t['scam2']}</li>
                    <li>{t['scam3']}</li>
                    <li>{t['scam4']}</li>
                </ul>

                <h2>🛡️ {t['protect_title']}</h2>
                <div class="space-y-3">
                    <div class="p-3 bg-blue-50 rounded-lg"><strong class="text-blue-700">{t['protect1_title']}:</strong> {t['protect1']}</div>
                    <div class="p-3 bg-blue-50 rounded-lg"><strong class="text-blue-700">{t['protect2_title']}:</strong> {t['protect2']}</div>
                    <div class="p-3 bg-blue-50 rounded-lg"><strong class="text-blue-700">{t['protect3_title']}:</strong> {t['protect3']}</div>
                    <div class="p-3 bg-blue-50 rounded-lg"><strong class="text-blue-700">{t['protect4_title']}:</strong> {t['protect4']}</div>
                    <div class="p-3 bg-blue-50 rounded-lg"><strong class="text-blue-700">{t['protect5_title']}:</strong> {t['protect5']}</div>
                </div>

                <h2>{t['red_flags_title']}</h2>
                <ul class="bg-amber-50 p-4 rounded-xl">{red_flags_html}</ul>

                <h2>{t['safe_uses_title']}</h2>
                <ul class="bg-green-50 p-4 rounded-xl">{safe_uses_html}</ul>

                <h2>📋 {t['bottom_line_title']}</h2>
                <p class="bg-gray-100 p-4 rounded-xl font-medium">{t['bottom_line']}</p>

                <div class="mt-8 p-6 bg-red-100 rounded-xl text-center">
                    <h3 class="text-red-800 mt-0">{t['cta_title']}</h3>
                    <p class="text-red-700">{t['cta_text']}</p>
                    <a href="{base_path}" class="inline-block bg-red-600 hover:bg-red-700 text-white font-semibold px-6 py-3 rounded-xl mt-2">{t['cta_button']}</a>
                </div>
            </div>
        </article>
    </main>
</body>
</html>'''


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate How QR Codes Work articles
    print("Generating 'How QR Codes Work' articles...")
    for lang in LANGUAGES:
        t = HOW_QR_WORKS.get(lang, HOW_QR_WORKS['en'])
        
        if lang == 'en':
            out_dir = os.path.join(base_dir, 'blog', 'how-qr-codes-work')
        else:
            out_dir = os.path.join(base_dir, 'blog', lang, 'how-qr-codes-work')
        
        os.makedirs(out_dir, exist_ok=True)
        html = generate_how_qr_works(t, lang)
        
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {lang}")
    
    # Generate Are QR Codes Safe articles
    print("\nGenerating 'Are QR Codes Safe?' articles...")
    for lang in LANGUAGES:
        t = QR_SAFE.get(lang, QR_SAFE['en'])
        
        if lang == 'en':
            out_dir = os.path.join(base_dir, 'blog', 'qr-code-safety')
        else:
            out_dir = os.path.join(base_dir, 'blog', lang, 'qr-code-safety')
        
        os.makedirs(out_dir, exist_ok=True)
        html = generate_qr_safe(t, lang)
        
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {lang}")
    
    print(f"\n🎉 Generated 22 article pages (2 articles × 11 languages)!")


if __name__ == '__main__':
    main()

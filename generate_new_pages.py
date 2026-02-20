#!/usr/bin/env python3
"""Generate Google Review and PDF QR code pages for qrcodes.win in 11 languages."""

import os

LANGUAGES = ['en', 'es', 'de', 'fr', 'pt', 'zh', 'ja', 'ar', 'hi', 'ru', 'tr']

# Translations for Google Review QR page
GOOGLE_REVIEW = {
    'en': {
        'title': 'Google Review QR Code Generator | Get More Reviews',
        'meta': 'Create a QR code that links directly to your Google Reviews page. Make it easy for customers to leave 5-star reviews. Free, instant, no signup.',
        'h1': 'Google Review QR Code',
        'subtitle': 'Get more 5-star reviews with one scan',
        'label_url': 'Google Review Link',
        'placeholder': 'Paste your Google review link here',
        'help_text': 'Get your link from Google Business Profile → "Ask for reviews"',
        'btn_generate': 'Generate QR Code',
        'btn_download': 'Download QR Code',
        'how_title': 'How to Get Your Google Review Link',
        'step1': 'Go to your <strong>Google Business Profile</strong>',
        'step2': 'Click <strong>"Get more reviews"</strong> or <strong>"Ask for reviews"</strong>',
        'step3': 'Copy the review link provided',
        'step4': 'Paste it above and generate your QR code',
        'why_title': 'Why Use a Google Review QR Code?',
        'why1_title': 'More Reviews',
        'why1': 'Customers are 3x more likely to leave a review when it\'s easy',
        'why2_title': 'Better SEO',
        'why2': 'More Google reviews = higher local search rankings',
        'why3_title': 'Build Trust',
        'why3': 'Reviews are the #1 factor customers check before buying',
        'why4_title': 'Easy to Share',
        'why4': 'Print on receipts, cards, signs, tables, menus',
        'uses_title': 'Where to Display Your QR Code',
        'uses': ['Checkout counter or register', 'Receipts and invoices', 'Business cards', 'Table tents (restaurants)', 'Product packaging', 'Email signatures', 'Thank you cards'],
        'faq1_q': 'What is a Google Review QR code?',
        'faq1_a': 'It\'s a QR code that, when scanned, takes customers directly to your Google review page. They can leave a review in seconds without searching for your business.',
        'faq2_q': 'How do I find my Google review link?',
        'faq2_a': 'Log into Google Business Profile, click "Get more reviews" or "Share review form". Copy the provided link. If you don\'t see it, search "Google Place ID finder" and construct the link.',
        'faq3_q': 'Is this free?',
        'faq3_a': 'Yes, 100% free. No signup, no limits, no watermarks. Generate as many QR codes as you need.',
        'back': '← All QR Types',
        'lang_name': 'English',
    },
    'de': {
        'title': 'Google Bewertung QR-Code Generator | Mehr Bewertungen erhalten',
        'meta': 'Erstellen Sie einen QR-Code, der direkt zu Ihrer Google-Bewertungsseite führt. Machen Sie es Kunden leicht, 5-Sterne-Bewertungen zu hinterlassen. Kostenlos und sofort.',
        'h1': 'Google Bewertung QR-Code',
        'subtitle': 'Erhalten Sie mehr 5-Sterne-Bewertungen mit einem Scan',
        'label_url': 'Google Bewertungs-Link',
        'placeholder': 'Fügen Sie Ihren Google-Bewertungslink hier ein',
        'help_text': 'Link aus Google Unternehmensprofil → "Nach Bewertungen fragen"',
        'btn_generate': 'QR-Code erstellen',
        'btn_download': 'QR-Code herunterladen',
        'how_title': 'So erhalten Sie Ihren Google-Bewertungslink',
        'step1': 'Gehen Sie zu Ihrem <strong>Google Unternehmensprofil</strong>',
        'step2': 'Klicken Sie auf <strong>"Mehr Bewertungen erhalten"</strong>',
        'step3': 'Kopieren Sie den bereitgestellten Link',
        'step4': 'Fügen Sie ihn oben ein und erstellen Sie Ihren QR-Code',
        'why_title': 'Warum einen Google Bewertung QR-Code verwenden?',
        'why1_title': 'Mehr Bewertungen',
        'why1': 'Kunden hinterlassen 3x häufiger eine Bewertung, wenn es einfach ist',
        'why2_title': 'Besseres SEO',
        'why2': 'Mehr Google-Bewertungen = höhere lokale Suchrankings',
        'why3_title': 'Vertrauen aufbauen',
        'why3': 'Bewertungen sind der #1 Faktor, den Kunden vor dem Kauf prüfen',
        'why4_title': 'Einfach zu teilen',
        'why4': 'Drucken auf Quittungen, Karten, Schildern, Tischen, Menüs',
        'uses_title': 'Wo Sie Ihren QR-Code anzeigen können',
        'uses': ['Kasse oder Tresen', 'Quittungen und Rechnungen', 'Visitenkarten', 'Tischaufsteller (Restaurants)', 'Produktverpackungen', 'E-Mail-Signaturen', 'Dankeskarten'],
        'faq1_q': 'Was ist ein Google Bewertung QR-Code?',
        'faq1_a': 'Ein QR-Code, der Kunden direkt zu Ihrer Google-Bewertungsseite führt. Sie können in Sekunden eine Bewertung hinterlassen.',
        'faq2_q': 'Wie finde ich meinen Google-Bewertungslink?',
        'faq2_a': 'Melden Sie sich bei Google Unternehmensprofil an, klicken Sie auf "Mehr Bewertungen erhalten". Kopieren Sie den Link.',
        'faq3_q': 'Ist das kostenlos?',
        'faq3_a': 'Ja, 100% kostenlos. Keine Anmeldung, keine Limits, keine Wasserzeichen.',
        'back': '← Alle QR-Typen',
        'lang_name': 'Deutsch',
    },
    'es': {
        'title': 'Generador de Código QR para Reseñas de Google | Obtén Más Reseñas',
        'meta': 'Crea un código QR que enlace directamente a tu página de reseñas de Google. Facilita que los clientes dejen reseñas de 5 estrellas. Gratis e instantáneo.',
        'h1': 'Código QR para Reseñas de Google',
        'subtitle': 'Obtén más reseñas de 5 estrellas con un escaneo',
        'label_url': 'Enlace de Reseña de Google',
        'placeholder': 'Pega tu enlace de reseña de Google aquí',
        'help_text': 'Obtén el enlace desde Perfil de Empresa de Google → "Pedir reseñas"',
        'btn_generate': 'Generar Código QR',
        'btn_download': 'Descargar Código QR',
        'how_title': 'Cómo Obtener tu Enlace de Reseña de Google',
        'step1': 'Ve a tu <strong>Perfil de Empresa de Google</strong>',
        'step2': 'Haz clic en <strong>"Obtener más reseñas"</strong>',
        'step3': 'Copia el enlace proporcionado',
        'step4': 'Pégalo arriba y genera tu código QR',
        'why_title': '¿Por Qué Usar un Código QR de Reseña de Google?',
        'why1_title': 'Más Reseñas',
        'why1': 'Los clientes tienen 3x más probabilidades de dejar una reseña cuando es fácil',
        'why2_title': 'Mejor SEO',
        'why2': 'Más reseñas de Google = mejores rankings en búsquedas locales',
        'why3_title': 'Construir Confianza',
        'why3': 'Las reseñas son el factor #1 que los clientes verifican antes de comprar',
        'why4_title': 'Fácil de Compartir',
        'why4': 'Imprime en recibos, tarjetas, letreros, mesas, menús',
        'uses_title': 'Dónde Mostrar tu Código QR',
        'uses': ['Mostrador de caja', 'Recibos y facturas', 'Tarjetas de presentación', 'Caballetes de mesa (restaurantes)', 'Empaque de productos', 'Firmas de correo', 'Tarjetas de agradecimiento'],
        'faq1_q': '¿Qué es un código QR de reseña de Google?',
        'faq1_a': 'Es un código QR que lleva a los clientes directamente a tu página de reseñas de Google. Pueden dejar una reseña en segundos.',
        'faq2_q': '¿Cómo encuentro mi enlace de reseña de Google?',
        'faq2_a': 'Inicia sesión en Perfil de Empresa de Google, haz clic en "Obtener más reseñas". Copia el enlace.',
        'faq3_q': '¿Es gratis?',
        'faq3_a': 'Sí, 100% gratis. Sin registro, sin límites, sin marcas de agua.',
        'back': '← Todos los tipos de QR',
        'lang_name': 'Español',
    },
    'fr': {
        'title': 'Générateur de QR Code Avis Google | Obtenez Plus d\'Avis',
        'meta': 'Créez un QR code qui renvoie directement vers votre page d\'avis Google. Facilitez les avis 5 étoiles pour vos clients. Gratuit et instantané.',
        'h1': 'QR Code Avis Google',
        'subtitle': 'Obtenez plus d\'avis 5 étoiles en un scan',
        'label_url': 'Lien Avis Google',
        'placeholder': 'Collez votre lien d\'avis Google ici',
        'help_text': 'Obtenez le lien depuis Fiche Google → "Demander des avis"',
        'btn_generate': 'Générer le QR Code',
        'btn_download': 'Télécharger le QR Code',
        'how_title': 'Comment Obtenir Votre Lien Avis Google',
        'step1': 'Allez sur votre <strong>Fiche d\'établissement Google</strong>',
        'step2': 'Cliquez sur <strong>"Obtenir plus d\'avis"</strong>',
        'step3': 'Copiez le lien fourni',
        'step4': 'Collez-le ci-dessus et générez votre QR code',
        'why_title': 'Pourquoi Utiliser un QR Code Avis Google?',
        'why1_title': 'Plus d\'Avis',
        'why1': 'Les clients ont 3x plus de chances de laisser un avis quand c\'est facile',
        'why2_title': 'Meilleur SEO',
        'why2': 'Plus d\'avis Google = meilleur classement local',
        'why3_title': 'Construire la Confiance',
        'why3': 'Les avis sont le facteur #1 vérifié par les clients avant d\'acheter',
        'why4_title': 'Facile à Partager',
        'why4': 'Imprimez sur reçus, cartes, panneaux, tables, menus',
        'uses_title': 'Où Afficher Votre QR Code',
        'uses': ['Comptoir de caisse', 'Reçus et factures', 'Cartes de visite', 'Chevalets de table (restaurants)', 'Emballages produits', 'Signatures email', 'Cartes de remerciement'],
        'faq1_q': 'Qu\'est-ce qu\'un QR code avis Google?',
        'faq1_a': 'C\'est un QR code qui amène les clients directement sur votre page d\'avis Google. Ils peuvent laisser un avis en quelques secondes.',
        'faq2_q': 'Comment trouver mon lien avis Google?',
        'faq2_a': 'Connectez-vous à Fiche Google, cliquez sur "Obtenir plus d\'avis". Copiez le lien.',
        'faq3_q': 'Est-ce gratuit?',
        'faq3_a': 'Oui, 100% gratuit. Sans inscription, sans limites, sans filigrane.',
        'back': '← Tous les types de QR',
        'lang_name': 'Français',
    },
    'pt': {
        'title': 'Gerador de QR Code para Avaliação Google | Obtenha Mais Avaliações',
        'meta': 'Crie um QR code que leva diretamente à sua página de avaliações do Google. Facilite avaliações de 5 estrelas para seus clientes. Grátis e instantâneo.',
        'h1': 'QR Code Avaliação Google',
        'subtitle': 'Obtenha mais avaliações de 5 estrelas com um scan',
        'label_url': 'Link de Avaliação Google',
        'placeholder': 'Cole seu link de avaliação do Google aqui',
        'help_text': 'Obtenha o link do Perfil da Empresa Google → "Pedir avaliações"',
        'btn_generate': 'Gerar QR Code',
        'btn_download': 'Baixar QR Code',
        'how_title': 'Como Obter Seu Link de Avaliação Google',
        'step1': 'Acesse seu <strong>Perfil da Empresa Google</strong>',
        'step2': 'Clique em <strong>"Obter mais avaliações"</strong>',
        'step3': 'Copie o link fornecido',
        'step4': 'Cole acima e gere seu QR code',
        'why_title': 'Por Que Usar um QR Code de Avaliação Google?',
        'why1_title': 'Mais Avaliações',
        'why1': 'Clientes têm 3x mais chances de avaliar quando é fácil',
        'why2_title': 'Melhor SEO',
        'why2': 'Mais avaliações Google = melhor ranking nas buscas locais',
        'why3_title': 'Construir Confiança',
        'why3': 'Avaliações são o fator #1 que clientes verificam antes de comprar',
        'why4_title': 'Fácil de Compartilhar',
        'why4': 'Imprima em recibos, cartões, placas, mesas, cardápios',
        'uses_title': 'Onde Exibir Seu QR Code',
        'uses': ['Balcão de caixa', 'Recibos e faturas', 'Cartões de visita', 'Displays de mesa (restaurantes)', 'Embalagens', 'Assinaturas de email', 'Cartões de agradecimento'],
        'faq1_q': 'O que é um QR code de avaliação Google?',
        'faq1_a': 'É um QR code que leva clientes diretamente à sua página de avaliações Google. Eles podem avaliar em segundos.',
        'faq2_q': 'Como encontro meu link de avaliação Google?',
        'faq2_a': 'Entre no Perfil da Empresa Google, clique em "Obter mais avaliações". Copie o link.',
        'faq3_q': 'É grátis?',
        'faq3_a': 'Sim, 100% grátis. Sem cadastro, sem limites, sem marca d\'água.',
        'back': '← Todos os tipos de QR',
        'lang_name': 'Português',
    },
    'zh': {
        'title': 'Google评价二维码生成器 | 获取更多评价',
        'meta': '创建直接链接到您的Google评价页面的二维码。让客户轻松留下5星评价。免费即时生成。',
        'h1': 'Google评价二维码',
        'subtitle': '一次扫描获取更多5星评价',
        'label_url': 'Google评价链接',
        'placeholder': '在此粘贴您的Google评价链接',
        'help_text': '从Google商家资料 → "请求评价"获取链接',
        'btn_generate': '生成二维码',
        'btn_download': '下载二维码',
        'how_title': '如何获取您的Google评价链接',
        'step1': '前往您的<strong>Google商家资料</strong>',
        'step2': '点击<strong>"获取更多评价"</strong>',
        'step3': '复制提供的链接',
        'step4': '粘贴到上方并生成您的二维码',
        'why_title': '为什么使用Google评价二维码？',
        'why1_title': '更多评价',
        'why1': '当操作简单时，客户留下评价的可能性增加3倍',
        'why2_title': '更好的SEO',
        'why2': '更多Google评价 = 更高的本地搜索排名',
        'why3_title': '建立信任',
        'why3': '评价是客户购买前检查的第一要素',
        'why4_title': '易于分享',
        'why4': '打印在收据、卡片、标牌、桌面、菜单上',
        'uses_title': '在哪里展示您的二维码',
        'uses': ['收银台', '收据和发票', '名片', '桌牌（餐厅）', '产品包装', '电子邮件签名', '感谢卡'],
        'faq1_q': '什么是Google评价二维码？',
        'faq1_a': '这是一个二维码，扫描后直接将客户带到您的Google评价页面。他们可以在几秒钟内留下评价。',
        'faq2_q': '如何找到我的Google评价链接？',
        'faq2_a': '登录Google商家资料，点击"获取更多评价"。复制链接。',
        'faq3_q': '这是免费的吗？',
        'faq3_a': '是的，100%免费。无需注册，无限制，无水印。',
        'back': '← 所有二维码类型',
        'lang_name': '中文',
    },
    'ja': {
        'title': 'Googleレビュー QRコード作成 | もっとレビューを獲得',
        'meta': 'Googleレビューページに直接リンクするQRコードを作成。お客様が簡単に5つ星レビューを残せます。無料で即座に作成。',
        'h1': 'Googleレビュー QRコード',
        'subtitle': 'ワンスキャンで5つ星レビューをもっと獲得',
        'label_url': 'Googleレビューリンク',
        'placeholder': 'Googleレビューリンクをここに貼り付け',
        'help_text': 'Googleビジネスプロフィール → 「レビューをリクエスト」からリンクを取得',
        'btn_generate': 'QRコードを生成',
        'btn_download': 'QRコードをダウンロード',
        'how_title': 'Googleレビューリンクの取得方法',
        'step1': '<strong>Googleビジネスプロフィール</strong>にアクセス',
        'step2': '<strong>「レビューを増やす」</strong>をクリック',
        'step3': '表示されたリンクをコピー',
        'step4': '上に貼り付けてQRコードを生成',
        'why_title': 'なぜGoogleレビューQRコードを使うのか？',
        'why1_title': 'より多くのレビュー',
        'why1': '簡単だとお客様がレビューを残す確率が3倍に',
        'why2_title': 'より良いSEO',
        'why2': 'Googleレビューが増える = ローカル検索順位が上昇',
        'why3_title': '信頼を構築',
        'why3': 'レビューは購入前にお客様が最も確認する要素',
        'why4_title': '共有が簡単',
        'why4': 'レシート、カード、看板、テーブル、メニューに印刷',
        'uses_title': 'QRコードの表示場所',
        'uses': ['レジカウンター', '領収書・請求書', '名刺', 'テーブルスタンド（飲食店）', '商品パッケージ', 'メール署名', 'お礼状'],
        'faq1_q': 'GoogleレビューQRコードとは？',
        'faq1_a': 'スキャンするとお客様をGoogleレビューページに直接案内するQRコードです。数秒でレビューを残せます。',
        'faq2_q': 'Googleレビューリンクの見つけ方は？',
        'faq2_a': 'Googleビジネスプロフィールにログインし、「レビューを増やす」をクリック。リンクをコピーしてください。',
        'faq3_q': '無料ですか？',
        'faq3_a': 'はい、100%無料です。登録不要、制限なし、透かしなし。',
        'back': '← すべてのQRタイプ',
        'lang_name': '日本語',
    },
    'ar': {
        'title': 'مولد رمز QR لتقييمات جوجل | احصل على المزيد من التقييمات',
        'meta': 'أنشئ رمز QR يرتبط مباشرة بصفحة تقييمات جوجل الخاصة بك. اجعل من السهل على العملاء ترك تقييمات 5 نجوم. مجاني وفوري.',
        'h1': 'رمز QR لتقييمات جوجل',
        'subtitle': 'احصل على المزيد من تقييمات 5 نجوم بمسح واحد',
        'label_url': 'رابط تقييم جوجل',
        'placeholder': 'الصق رابط تقييم جوجل هنا',
        'help_text': 'احصل على الرابط من ملف نشاط جوجل التجاري ← "طلب تقييمات"',
        'btn_generate': 'إنشاء رمز QR',
        'btn_download': 'تحميل رمز QR',
        'how_title': 'كيفية الحصول على رابط تقييم جوجل',
        'step1': 'اذهب إلى <strong>ملف نشاط جوجل التجاري</strong>',
        'step2': 'انقر على <strong>"الحصول على المزيد من التقييمات"</strong>',
        'step3': 'انسخ الرابط المقدم',
        'step4': 'الصقه أعلاه وأنشئ رمز QR الخاص بك',
        'why_title': 'لماذا تستخدم رمز QR لتقييمات جوجل؟',
        'why1_title': 'المزيد من التقييمات',
        'why1': 'العملاء أكثر احتمالاً بـ3 مرات لترك تقييم عندما يكون سهلاً',
        'why2_title': 'تحسين محركات البحث',
        'why2': 'المزيد من تقييمات جوجل = ترتيب أعلى في البحث المحلي',
        'why3_title': 'بناء الثقة',
        'why3': 'التقييمات هي العامل الأول الذي يتحقق منه العملاء قبل الشراء',
        'why4_title': 'سهل المشاركة',
        'why4': 'اطبع على الإيصالات والبطاقات واللافتات والطاولات والقوائم',
        'uses_title': 'أين تعرض رمز QR الخاص بك',
        'uses': ['منضدة الكاشير', 'الإيصالات والفواتير', 'بطاقات العمل', 'حوامل الطاولة (المطاعم)', 'تغليف المنتجات', 'توقيعات البريد الإلكتروني', 'بطاقات الشكر'],
        'faq1_q': 'ما هو رمز QR لتقييم جوجل؟',
        'faq1_a': 'رمز QR ينقل العملاء مباشرة إلى صفحة تقييمات جوجل الخاصة بك. يمكنهم ترك تقييم في ثوانٍ.',
        'faq2_q': 'كيف أجد رابط تقييم جوجل الخاص بي؟',
        'faq2_a': 'سجل الدخول إلى ملف نشاط جوجل التجاري، انقر على "الحصول على المزيد من التقييمات". انسخ الرابط.',
        'faq3_q': 'هل هذا مجاني؟',
        'faq3_a': 'نعم، مجاني 100%. بدون تسجيل، بدون حدود، بدون علامات مائية.',
        'back': '← جميع أنواع QR',
        'lang_name': 'العربية',
    },
    'hi': {
        'title': 'Google रिव्यू QR कोड जेनरेटर | अधिक रिव्यू प्राप्त करें',
        'meta': 'एक QR कोड बनाएं जो सीधे आपके Google रिव्यू पेज से लिंक हो। ग्राहकों के लिए 5-स्टार रिव्यू देना आसान बनाएं। मुफ्त और तुरंत।',
        'h1': 'Google रिव्यू QR कोड',
        'subtitle': 'एक स्कैन से अधिक 5-स्टार रिव्यू प्राप्त करें',
        'label_url': 'Google रिव्यू लिंक',
        'placeholder': 'अपना Google रिव्यू लिंक यहां पेस्ट करें',
        'help_text': 'Google Business Profile से लिंक प्राप्त करें → "रिव्यू मांगें"',
        'btn_generate': 'QR कोड बनाएं',
        'btn_download': 'QR कोड डाउनलोड करें',
        'how_title': 'अपना Google रिव्यू लिंक कैसे प्राप्त करें',
        'step1': 'अपने <strong>Google Business Profile</strong> पर जाएं',
        'step2': '<strong>"अधिक रिव्यू प्राप्त करें"</strong> पर क्लिक करें',
        'step3': 'दिए गए लिंक को कॉपी करें',
        'step4': 'ऊपर पेस्ट करें और अपना QR कोड बनाएं',
        'why_title': 'Google रिव्यू QR कोड क्यों उपयोग करें?',
        'why1_title': 'अधिक रिव्यू',
        'why1': 'जब आसान होता है तो ग्राहकों के रिव्यू देने की संभावना 3 गुना बढ़ जाती है',
        'why2_title': 'बेहतर SEO',
        'why2': 'अधिक Google रिव्यू = उच्च स्थानीय खोज रैंकिंग',
        'why3_title': 'विश्वास बनाएं',
        'why3': 'रिव्यू ग्राहकों द्वारा खरीदने से पहले जांचा जाने वाला #1 कारक है',
        'why4_title': 'साझा करना आसान',
        'why4': 'रसीदों, कार्डों, साइनों, टेबलों, मेन्यू पर प्रिंट करें',
        'uses_title': 'अपना QR कोड कहां प्रदर्शित करें',
        'uses': ['चेकआउट काउंटर', 'रसीदें और बिल', 'बिजनेस कार्ड', 'टेबल स्टैंड (रेस्तरां)', 'उत्पाद पैकेजिंग', 'ईमेल हस्ताक्षर', 'धन्यवाद कार्ड'],
        'faq1_q': 'Google रिव्यू QR कोड क्या है?',
        'faq1_a': 'यह एक QR कोड है जो स्कैन करने पर ग्राहकों को सीधे आपके Google रिव्यू पेज पर ले जाता है। वे सेकंडों में रिव्यू दे सकते हैं।',
        'faq2_q': 'मैं अपना Google रिव्यू लिंक कैसे खोजूं?',
        'faq2_a': 'Google Business Profile में लॉगिन करें, "अधिक रिव्यू प्राप्त करें" पर क्लिक करें। लिंक कॉपी करें।',
        'faq3_q': 'क्या यह मुफ्त है?',
        'faq3_a': 'हां, 100% मुफ्त। कोई साइनअप नहीं, कोई सीमा नहीं, कोई वॉटरमार्क नहीं।',
        'back': '← सभी QR प्रकार',
        'lang_name': 'हिन्दी',
    },
    'ru': {
        'title': 'Генератор QR-кода для отзывов Google | Получите больше отзывов',
        'meta': 'Создайте QR-код со ссылкой на страницу отзывов Google. Упростите клиентам возможность оставить 5-звездочный отзыв. Бесплатно и мгновенно.',
        'h1': 'QR-код для отзывов Google',
        'subtitle': 'Получите больше 5-звездочных отзывов одним сканированием',
        'label_url': 'Ссылка на отзыв Google',
        'placeholder': 'Вставьте ссылку на отзыв Google здесь',
        'help_text': 'Получите ссылку из Google Бизнес Профиля → "Запросить отзывы"',
        'btn_generate': 'Создать QR-код',
        'btn_download': 'Скачать QR-код',
        'how_title': 'Как получить ссылку для отзыва Google',
        'step1': 'Перейдите в <strong>Google Бизнес Профиль</strong>',
        'step2': 'Нажмите <strong>"Получить больше отзывов"</strong>',
        'step3': 'Скопируйте предоставленную ссылку',
        'step4': 'Вставьте выше и создайте QR-код',
        'why_title': 'Зачем использовать QR-код для отзывов Google?',
        'why1_title': 'Больше отзывов',
        'why1': 'Клиенты в 3 раза чаще оставляют отзыв, когда это легко',
        'why2_title': 'Лучшее SEO',
        'why2': 'Больше отзывов Google = выше позиции в локальном поиске',
        'why3_title': 'Построение доверия',
        'why3': 'Отзывы — фактор №1, который проверяют клиенты перед покупкой',
        'why4_title': 'Легко делиться',
        'why4': 'Печатайте на чеках, визитках, вывесках, столах, меню',
        'uses_title': 'Где разместить QR-код',
        'uses': ['Касса', 'Чеки и счета', 'Визитные карточки', 'Настольные подставки (рестораны)', 'Упаковка продукции', 'Подписи в email', 'Благодарственные открытки'],
        'faq1_q': 'Что такое QR-код для отзыва Google?',
        'faq1_a': 'Это QR-код, который при сканировании ведёт клиентов прямо на страницу отзывов Google. Они могут оставить отзыв за секунды.',
        'faq2_q': 'Как найти ссылку на отзыв Google?',
        'faq2_a': 'Войдите в Google Бизнес Профиль, нажмите "Получить больше отзывов". Скопируйте ссылку.',
        'faq3_q': 'Это бесплатно?',
        'faq3_a': 'Да, 100% бесплатно. Без регистрации, без ограничений, без водяных знаков.',
        'back': '← Все типы QR',
        'lang_name': 'Русский',
    },
    'tr': {
        'title': 'Google Yorum QR Kodu Oluşturucu | Daha Fazla Yorum Alın',
        'meta': 'Google yorumlar sayfanıza doğrudan bağlanan bir QR kodu oluşturun. Müşterilerin 5 yıldızlı yorum bırakmasını kolaylaştırın. Ücretsiz ve anında.',
        'h1': 'Google Yorum QR Kodu',
        'subtitle': 'Tek tarama ile daha fazla 5 yıldızlı yorum alın',
        'label_url': 'Google Yorum Linki',
        'placeholder': 'Google yorum linkinizi buraya yapıştırın',
        'help_text': 'Linki Google İşletme Profilinden alın → "Yorum İste"',
        'btn_generate': 'QR Kodu Oluştur',
        'btn_download': 'QR Kodu İndir',
        'how_title': 'Google Yorum Linkinizi Nasıl Alırsınız',
        'step1': '<strong>Google İşletme Profilinize</strong> gidin',
        'step2': '<strong>"Daha fazla yorum al"</strong>\'a tıklayın',
        'step3': 'Verilen linki kopyalayın',
        'step4': 'Yukarıya yapıştırın ve QR kodunuzu oluşturun',
        'why_title': 'Neden Google Yorum QR Kodu Kullanmalı?',
        'why1_title': 'Daha Fazla Yorum',
        'why1': 'Kolay olduğunda müşterilerin yorum bırakma olasılığı 3 kat artar',
        'why2_title': 'Daha İyi SEO',
        'why2': 'Daha fazla Google yorumu = daha yüksek yerel arama sıralaması',
        'why3_title': 'Güven Oluşturun',
        'why3': 'Yorumlar, müşterilerin satın almadan önce kontrol ettiği #1 faktör',
        'why4_title': 'Paylaşması Kolay',
        'why4': 'Fişlere, kartlara, tabelaların, masalara, menülere yazdırın',
        'uses_title': 'QR Kodunuzu Nerede Göstermelisiniz',
        'uses': ['Kasa tezgahı', 'Fişler ve faturalar', 'Kartvizitler', 'Masa standları (restoranlar)', 'Ürün ambalajları', 'E-posta imzaları', 'Teşekkür kartları'],
        'faq1_q': 'Google yorum QR kodu nedir?',
        'faq1_a': 'Tarandığında müşterileri doğrudan Google yorum sayfanıza götüren bir QR kodudur. Saniyeler içinde yorum bırakabilirler.',
        'faq2_q': 'Google yorum linkimi nasıl bulurum?',
        'faq2_a': 'Google İşletme Profiline giriş yapın, "Daha fazla yorum al"a tıklayın. Linki kopyalayın.',
        'faq3_q': 'Bu ücretsiz mi?',
        'faq3_a': 'Evet, %100 ücretsiz. Kayıt yok, limit yok, filigran yok.',
        'back': '← Tüm QR Tipleri',
        'lang_name': 'Türkçe',
    },
}

# PDF QR translations
PDF_QR = {
    'en': {
        'title': 'PDF QR Code Generator | Link to PDF Documents',
        'meta': 'Create a QR code that links to your PDF file. Perfect for menus, brochures, manuals, and documents. Free, instant, no signup required.',
        'h1': 'PDF QR Code Generator',
        'subtitle': 'Share any PDF document with a simple scan',
        'label_url': 'PDF Link (URL)',
        'placeholder': 'https://example.com/document.pdf',
        'help_text': 'Your PDF must be hosted online (Google Drive, Dropbox, your website)',
        'btn_generate': 'Generate QR Code',
        'btn_download': 'Download QR Code',
        'how_title': 'How to Create a PDF QR Code',
        'step1': 'Upload your PDF to cloud storage (Google Drive, Dropbox) or your website',
        'step2': 'Get the <strong>public/shareable link</strong> to your PDF',
        'step3': 'Paste the link above',
        'step4': 'Generate and download your QR code',
        'tip_title': '💡 Pro Tip: Google Drive',
        'tip': 'For Google Drive: Right-click your PDF → "Get link" → Change to "Anyone with the link" → Copy link',
        'why_title': 'Why Use a PDF QR Code?',
        'why1_title': 'Paperless',
        'why1': 'Share documents without printing — eco-friendly and cost-effective',
        'why2_title': 'Always Updated',
        'why2': 'Update your PDF anytime — the QR code stays the same',
        'why3_title': 'Track Views',
        'why3': 'Use bit.ly or similar to track how many people access your PDF',
        'why4_title': 'Works Everywhere',
        'why4': 'Any smartphone can scan and view PDFs instantly',
        'uses_title': 'Popular Uses for PDF QR Codes',
        'uses': ['Restaurant menus', 'Product manuals & instructions', 'Event programs', 'Real estate flyers', 'Business brochures', 'Educational materials', 'Price lists & catalogs'],
        'faq1_q': 'Where should I host my PDF?',
        'faq1_a': 'Google Drive (free), Dropbox, OneDrive, or your own website all work. Make sure the link is publicly accessible (anyone with link can view).',
        'faq2_q': 'Can I update the PDF later?',
        'faq2_a': 'Yes! If you replace the file at the same URL, the QR code will show the new version. With Google Drive, just upload a new version of the same file.',
        'faq3_q': 'Is there a file size limit?',
        'faq3_a': 'The QR code just links to your PDF — there\'s no limit. However, smaller PDFs (under 10MB) load faster on mobile devices.',
        'back': '← All QR Types',
        'lang_name': 'English',
    },
    'de': {
        'title': 'PDF QR-Code Generator | Link zu PDF-Dokumenten',
        'meta': 'Erstellen Sie einen QR-Code, der zu Ihrer PDF-Datei verlinkt. Perfekt für Menüs, Broschüren, Handbücher und Dokumente. Kostenlos und sofort.',
        'h1': 'PDF QR-Code Generator',
        'subtitle': 'Teilen Sie jedes PDF-Dokument mit einem einfachen Scan',
        'label_url': 'PDF-Link (URL)',
        'placeholder': 'https://beispiel.de/dokument.pdf',
        'help_text': 'Ihre PDF muss online gehostet sein (Google Drive, Dropbox, Ihre Website)',
        'btn_generate': 'QR-Code erstellen',
        'btn_download': 'QR-Code herunterladen',
        'how_title': 'So erstellen Sie einen PDF QR-Code',
        'step1': 'Laden Sie Ihre PDF in Cloud-Speicher (Google Drive, Dropbox) oder auf Ihre Website hoch',
        'step2': 'Holen Sie sich den <strong>öffentlichen/teilbaren Link</strong> zu Ihrer PDF',
        'step3': 'Fügen Sie den Link oben ein',
        'step4': 'Erstellen und laden Sie Ihren QR-Code herunter',
        'tip_title': '💡 Profi-Tipp: Google Drive',
        'tip': 'Für Google Drive: Rechtsklick auf PDF → "Link abrufen" → Ändern zu "Jeder mit dem Link" → Link kopieren',
        'why_title': 'Warum einen PDF QR-Code verwenden?',
        'why1_title': 'Papierlos',
        'why1': 'Dokumente teilen ohne Drucken — umweltfreundlich und kostengünstig',
        'why2_title': 'Immer Aktuell',
        'why2': 'Aktualisieren Sie Ihre PDF jederzeit — der QR-Code bleibt gleich',
        'why3_title': 'Aufrufe Verfolgen',
        'why3': 'Verwenden Sie bit.ly oder ähnliches, um Zugriffe zu verfolgen',
        'why4_title': 'Funktioniert Überall',
        'why4': 'Jedes Smartphone kann scannen und PDFs sofort anzeigen',
        'uses_title': 'Beliebte Verwendungen für PDF QR-Codes',
        'uses': ['Restaurant-Menüs', 'Produkthandbücher & Anleitungen', 'Veranstaltungsprogramme', 'Immobilien-Flyer', 'Geschäftsbroschüren', 'Bildungsmaterialien', 'Preislisten & Kataloge'],
        'faq1_q': 'Wo sollte ich meine PDF hosten?',
        'faq1_a': 'Google Drive (kostenlos), Dropbox, OneDrive oder Ihre eigene Website funktionieren alle. Stellen Sie sicher, dass der Link öffentlich zugänglich ist.',
        'faq2_q': 'Kann ich die PDF später aktualisieren?',
        'faq2_a': 'Ja! Wenn Sie die Datei unter derselben URL ersetzen, zeigt der QR-Code die neue Version. Bei Google Drive laden Sie einfach eine neue Version der gleichen Datei hoch.',
        'faq3_q': 'Gibt es ein Dateigrößenlimit?',
        'faq3_a': 'Der QR-Code verlinkt nur zu Ihrer PDF — es gibt kein Limit. Kleinere PDFs (unter 10MB) laden jedoch schneller auf Mobilgeräten.',
        'back': '← Alle QR-Typen',
        'lang_name': 'Deutsch',
    },
    'es': {
        'title': 'Generador de QR para PDF | Enlace a Documentos PDF',
        'meta': 'Crea un código QR que enlaza a tu archivo PDF. Perfecto para menús, folletos, manuales y documentos. Gratis e instantáneo.',
        'h1': 'Generador de QR para PDF',
        'subtitle': 'Comparte cualquier documento PDF con un simple escaneo',
        'label_url': 'Enlace PDF (URL)',
        'placeholder': 'https://ejemplo.com/documento.pdf',
        'help_text': 'Tu PDF debe estar alojado en línea (Google Drive, Dropbox, tu sitio web)',
        'btn_generate': 'Generar Código QR',
        'btn_download': 'Descargar Código QR',
        'how_title': 'Cómo Crear un Código QR para PDF',
        'step1': 'Sube tu PDF a almacenamiento en la nube (Google Drive, Dropbox) o tu sitio web',
        'step2': 'Obtén el <strong>enlace público/compartible</strong> de tu PDF',
        'step3': 'Pega el enlace arriba',
        'step4': 'Genera y descarga tu código QR',
        'tip_title': '💡 Consejo Pro: Google Drive',
        'tip': 'Para Google Drive: Clic derecho en PDF → "Obtener enlace" → Cambiar a "Cualquiera con el enlace" → Copiar enlace',
        'why_title': '¿Por Qué Usar un Código QR para PDF?',
        'why1_title': 'Sin Papel',
        'why1': 'Comparte documentos sin imprimir — ecológico y económico',
        'why2_title': 'Siempre Actualizado',
        'why2': 'Actualiza tu PDF cuando quieras — el código QR permanece igual',
        'why3_title': 'Rastrea Vistas',
        'why3': 'Usa bit.ly o similar para rastrear cuántas personas acceden a tu PDF',
        'why4_title': 'Funciona en Todos Lados',
        'why4': 'Cualquier smartphone puede escanear y ver PDFs instantáneamente',
        'uses_title': 'Usos Populares para Códigos QR de PDF',
        'uses': ['Menús de restaurantes', 'Manuales e instrucciones', 'Programas de eventos', 'Folletos inmobiliarios', 'Folletos de negocios', 'Materiales educativos', 'Listas de precios y catálogos'],
        'faq1_q': '¿Dónde debo alojar mi PDF?',
        'faq1_a': 'Google Drive (gratis), Dropbox, OneDrive o tu propio sitio web funcionan. Asegúrate de que el enlace sea de acceso público.',
        'faq2_q': '¿Puedo actualizar el PDF después?',
        'faq2_a': '¡Sí! Si reemplazas el archivo en la misma URL, el código QR mostrará la nueva versión. Con Google Drive, solo sube una nueva versión del mismo archivo.',
        'faq3_q': '¿Hay límite de tamaño de archivo?',
        'faq3_a': 'El código QR solo enlaza a tu PDF — no hay límite. Sin embargo, PDFs más pequeños (menos de 10MB) cargan más rápido en dispositivos móviles.',
        'back': '← Todos los tipos de QR',
        'lang_name': 'Español',
    },
    'fr': {
        'title': 'Générateur QR Code PDF | Lien vers Documents PDF',
        'meta': 'Créez un QR code qui renvoie vers votre fichier PDF. Parfait pour menus, brochures, manuels et documents. Gratuit et instantané.',
        'h1': 'Générateur QR Code PDF',
        'subtitle': 'Partagez n\'importe quel document PDF d\'un simple scan',
        'label_url': 'Lien PDF (URL)',
        'placeholder': 'https://exemple.com/document.pdf',
        'help_text': 'Votre PDF doit être hébergé en ligne (Google Drive, Dropbox, votre site)',
        'btn_generate': 'Générer le QR Code',
        'btn_download': 'Télécharger le QR Code',
        'how_title': 'Comment Créer un QR Code PDF',
        'step1': 'Téléchargez votre PDF sur un stockage cloud (Google Drive, Dropbox) ou votre site',
        'step2': 'Obtenez le <strong>lien public/partageable</strong> de votre PDF',
        'step3': 'Collez le lien ci-dessus',
        'step4': 'Générez et téléchargez votre QR code',
        'tip_title': '💡 Astuce Pro: Google Drive',
        'tip': 'Pour Google Drive: Clic droit sur PDF → "Obtenir le lien" → Changer pour "Tous ceux qui ont le lien" → Copier',
        'why_title': 'Pourquoi Utiliser un QR Code PDF?',
        'why1_title': 'Sans Papier',
        'why1': 'Partagez des documents sans imprimer — écologique et économique',
        'why2_title': 'Toujours à Jour',
        'why2': 'Mettez à jour votre PDF quand vous voulez — le QR code reste le même',
        'why3_title': 'Suivez les Vues',
        'why3': 'Utilisez bit.ly ou similaire pour suivre combien de personnes accèdent à votre PDF',
        'why4_title': 'Fonctionne Partout',
        'why4': 'Tout smartphone peut scanner et voir les PDFs instantanément',
        'uses_title': 'Utilisations Populaires des QR Codes PDF',
        'uses': ['Menus de restaurants', 'Manuels et instructions produits', 'Programmes d\'événements', 'Flyers immobiliers', 'Brochures d\'entreprise', 'Matériels éducatifs', 'Listes de prix et catalogues'],
        'faq1_q': 'Où héberger mon PDF?',
        'faq1_a': 'Google Drive (gratuit), Dropbox, OneDrive ou votre propre site fonctionnent tous. Assurez-vous que le lien est accessible publiquement.',
        'faq2_q': 'Puis-je mettre à jour le PDF plus tard?',
        'faq2_a': 'Oui! Si vous remplacez le fichier à la même URL, le QR code affichera la nouvelle version. Avec Google Drive, téléchargez simplement une nouvelle version du même fichier.',
        'faq3_q': 'Y a-t-il une limite de taille?',
        'faq3_a': 'Le QR code ne fait que lier vers votre PDF — pas de limite. Cependant, les PDFs plus petits (moins de 10Mo) se chargent plus vite sur mobile.',
        'back': '← Tous les types de QR',
        'lang_name': 'Français',
    },
    'pt': {
        'title': 'Gerador de QR Code para PDF | Link para Documentos PDF',
        'meta': 'Crie um QR code que linka para seu arquivo PDF. Perfeito para cardápios, folhetos, manuais e documentos. Grátis e instantâneo.',
        'h1': 'Gerador de QR Code para PDF',
        'subtitle': 'Compartilhe qualquer documento PDF com um simples scan',
        'label_url': 'Link do PDF (URL)',
        'placeholder': 'https://exemplo.com/documento.pdf',
        'help_text': 'Seu PDF deve estar hospedado online (Google Drive, Dropbox, seu site)',
        'btn_generate': 'Gerar QR Code',
        'btn_download': 'Baixar QR Code',
        'how_title': 'Como Criar um QR Code para PDF',
        'step1': 'Faça upload do seu PDF para armazenamento em nuvem (Google Drive, Dropbox) ou seu site',
        'step2': 'Obtenha o <strong>link público/compartilhável</strong> do seu PDF',
        'step3': 'Cole o link acima',
        'step4': 'Gere e baixe seu QR code',
        'tip_title': '💡 Dica Pro: Google Drive',
        'tip': 'Para Google Drive: Clique direito no PDF → "Obter link" → Mudar para "Qualquer pessoa com o link" → Copiar',
        'why_title': 'Por Que Usar um QR Code para PDF?',
        'why1_title': 'Sem Papel',
        'why1': 'Compartilhe documentos sem imprimir — ecológico e econômico',
        'why2_title': 'Sempre Atualizado',
        'why2': 'Atualize seu PDF quando quiser — o QR code permanece o mesmo',
        'why3_title': 'Rastreie Visualizações',
        'why3': 'Use bit.ly ou similar para rastrear quantas pessoas acessam seu PDF',
        'why4_title': 'Funciona em Todo Lugar',
        'why4': 'Qualquer smartphone pode escanear e ver PDFs instantaneamente',
        'uses_title': 'Usos Populares para QR Codes de PDF',
        'uses': ['Cardápios de restaurantes', 'Manuais e instruções', 'Programas de eventos', 'Folhetos imobiliários', 'Folhetos empresariais', 'Materiais educacionais', 'Listas de preços e catálogos'],
        'faq1_q': 'Onde devo hospedar meu PDF?',
        'faq1_a': 'Google Drive (grátis), Dropbox, OneDrive ou seu próprio site funcionam. Certifique-se de que o link seja acessível publicamente.',
        'faq2_q': 'Posso atualizar o PDF depois?',
        'faq2_a': 'Sim! Se você substituir o arquivo na mesma URL, o QR code mostrará a nova versão. Com Google Drive, basta fazer upload de uma nova versão do mesmo arquivo.',
        'faq3_q': 'Há limite de tamanho de arquivo?',
        'faq3_a': 'O QR code apenas linka para seu PDF — não há limite. Porém, PDFs menores (menos de 10MB) carregam mais rápido em dispositivos móveis.',
        'back': '← Todos os tipos de QR',
        'lang_name': 'Português',
    },
    'zh': {
        'title': 'PDF二维码生成器 | 链接到PDF文档',
        'meta': '创建链接到PDF文件的二维码。非常适合菜单、宣传册、手册和文档。免费即时生成。',
        'h1': 'PDF二维码生成器',
        'subtitle': '一次扫描分享任何PDF文档',
        'label_url': 'PDF链接 (URL)',
        'placeholder': 'https://example.com/document.pdf',
        'help_text': '您的PDF必须托管在线上（Google Drive、Dropbox、您的网站）',
        'btn_generate': '生成二维码',
        'btn_download': '下载二维码',
        'how_title': '如何创建PDF二维码',
        'step1': '将PDF上传到云存储（Google Drive、Dropbox）或您的网站',
        'step2': '获取PDF的<strong>公开/可分享链接</strong>',
        'step3': '将链接粘贴到上方',
        'step4': '生成并下载您的二维码',
        'tip_title': '💡 专业提示：Google Drive',
        'tip': 'Google Drive操作：右键点击PDF → "获取链接" → 更改为"知道链接的任何人" → 复制链接',
        'why_title': '为什么使用PDF二维码？',
        'why1_title': '无纸化',
        'why1': '无需打印即可分享文档 - 环保且经济',
        'why2_title': '始终更新',
        'why2': '随时更新PDF - 二维码保持不变',
        'why3_title': '追踪查看',
        'why3': '使用bit.ly或类似工具追踪多少人访问您的PDF',
        'why4_title': '随处可用',
        'why4': '任何智能手机都可以扫描并即时查看PDF',
        'uses_title': 'PDF二维码的常见用途',
        'uses': ['餐厅菜单', '产品手册和说明', '活动节目单', '房地产传单', '商业宣传册', '教育材料', '价格表和目录'],
        'faq1_q': '我应该在哪里托管PDF？',
        'faq1_a': 'Google Drive（免费）、Dropbox、OneDrive或您自己的网站都可以。确保链接是公开可访问的。',
        'faq2_q': '以后可以更新PDF吗？',
        'faq2_a': '可以！如果您在同一URL替换文件，二维码将显示新版本。使用Google Drive，只需上传同一文件的新版本。',
        'faq3_q': '文件大小有限制吗？',
        'faq3_a': '二维码只是链接到您的PDF - 没有限制。但是，较小的PDF（10MB以下）在移动设备上加载更快。',
        'back': '← 所有二维码类型',
        'lang_name': '中文',
    },
    'ja': {
        'title': 'PDF QRコード作成 | PDFドキュメントへのリンク',
        'meta': 'PDFファイルにリンクするQRコードを作成。メニュー、パンフレット、マニュアル、ドキュメントに最適。無料で即座に作成。',
        'h1': 'PDF QRコード作成',
        'subtitle': 'シンプルなスキャンでPDFドキュメントを共有',
        'label_url': 'PDFリンク (URL)',
        'placeholder': 'https://example.com/document.pdf',
        'help_text': 'PDFはオンラインでホストされている必要があります（Google Drive、Dropbox、ウェブサイト）',
        'btn_generate': 'QRコードを生成',
        'btn_download': 'QRコードをダウンロード',
        'how_title': 'PDF QRコードの作成方法',
        'step1': 'PDFをクラウドストレージ（Google Drive、Dropbox）またはウェブサイトにアップロード',
        'step2': 'PDFの<strong>公開/共有リンク</strong>を取得',
        'step3': '上のリンクを貼り付け',
        'step4': 'QRコードを生成してダウンロード',
        'tip_title': '💡 プロのヒント：Google Drive',
        'tip': 'Google Driveの場合：PDFを右クリック → "リンクを取得" → "リンクを知っている全員"に変更 → リンクをコピー',
        'why_title': 'なぜPDF QRコードを使うのか？',
        'why1_title': 'ペーパーレス',
        'why1': '印刷せずにドキュメントを共有 - エコで経済的',
        'why2_title': '常に最新',
        'why2': 'いつでもPDFを更新 - QRコードは同じまま',
        'why3_title': '閲覧追跡',
        'why3': 'bit.lyなどを使って何人がPDFにアクセスしたか追跡',
        'why4_title': 'どこでも動作',
        'why4': 'どのスマートフォンでもスキャンしてPDFを即座に表示',
        'uses_title': 'PDF QRコードの一般的な用途',
        'uses': ['レストランメニュー', '製品マニュアル・取扱説明書', 'イベントプログラム', '不動産チラシ', 'ビジネスパンフレット', '教育資料', '価格表・カタログ'],
        'faq1_q': 'PDFはどこにホストすべき？',
        'faq1_a': 'Google Drive（無料）、Dropbox、OneDrive、または自分のウェブサイトが使えます。リンクが公開アクセス可能であることを確認してください。',
        'faq2_q': '後でPDFを更新できますか？',
        'faq2_a': 'はい！同じURLでファイルを置き換えると、QRコードは新しいバージョンを表示します。Google Driveでは、同じファイルの新バージョンをアップロードするだけです。',
        'faq3_q': 'ファイルサイズに制限はありますか？',
        'faq3_a': 'QRコードはPDFにリンクするだけなので制限はありません。ただし、小さいPDF（10MB以下）はモバイルデバイスで速く読み込めます。',
        'back': '← すべてのQRタイプ',
        'lang_name': '日本語',
    },
    'ar': {
        'title': 'مولد رمز QR لملفات PDF | رابط لمستندات PDF',
        'meta': 'أنشئ رمز QR يرتبط بملف PDF الخاص بك. مثالي للقوائم والكتيبات والأدلة والمستندات. مجاني وفوري.',
        'h1': 'مولد رمز QR لملفات PDF',
        'subtitle': 'شارك أي مستند PDF بمسح بسيط',
        'label_url': 'رابط PDF (URL)',
        'placeholder': 'https://example.com/document.pdf',
        'help_text': 'يجب أن يكون PDF مستضافاً على الإنترنت (Google Drive، Dropbox، موقعك)',
        'btn_generate': 'إنشاء رمز QR',
        'btn_download': 'تحميل رمز QR',
        'how_title': 'كيفية إنشاء رمز QR لملف PDF',
        'step1': 'ارفع PDF إلى التخزين السحابي (Google Drive، Dropbox) أو موقعك',
        'step2': 'احصل على <strong>الرابط العام/القابل للمشاركة</strong> لملف PDF',
        'step3': 'الصق الرابط أعلاه',
        'step4': 'أنشئ وحمّل رمز QR الخاص بك',
        'tip_title': '💡 نصيحة احترافية: Google Drive',
        'tip': 'لـ Google Drive: انقر بزر الماوس الأيمن على PDF ← "الحصول على رابط" ← تغيير إلى "أي شخص لديه الرابط" ← نسخ',
        'why_title': 'لماذا تستخدم رمز QR لملفات PDF؟',
        'why1_title': 'بدون ورق',
        'why1': 'شارك المستندات بدون طباعة - صديق للبيئة واقتصادي',
        'why2_title': 'محدث دائماً',
        'why2': 'حدّث PDF في أي وقت - رمز QR يبقى كما هو',
        'why3_title': 'تتبع المشاهدات',
        'why3': 'استخدم bit.ly أو ما شابه لتتبع عدد الأشخاص الذين يصلون إلى PDF',
        'why4_title': 'يعمل في كل مكان',
        'why4': 'أي هاتف ذكي يمكنه المسح وعرض PDF فوراً',
        'uses_title': 'الاستخدامات الشائعة لرموز QR لملفات PDF',
        'uses': ['قوائم المطاعم', 'أدلة المنتجات والتعليمات', 'برامج الفعاليات', 'منشورات العقارات', 'كتيبات الأعمال', 'المواد التعليمية', 'قوائم الأسعار والكتالوجات'],
        'faq1_q': 'أين يجب أن أستضيف PDF؟',
        'faq1_a': 'Google Drive (مجاني)، Dropbox، OneDrive، أو موقعك الخاص كلها تعمل. تأكد من أن الرابط متاح للجمهور.',
        'faq2_q': 'هل يمكنني تحديث PDF لاحقاً؟',
        'faq2_a': 'نعم! إذا استبدلت الملف في نفس URL، سيعرض رمز QR النسخة الجديدة. مع Google Drive، فقط ارفع نسخة جديدة من نفس الملف.',
        'faq3_q': 'هل هناك حد لحجم الملف؟',
        'faq3_a': 'رمز QR يرتبط فقط بـ PDF - لا يوجد حد. لكن ملفات PDF الأصغر (أقل من 10 ميجا) تُحمّل أسرع على الأجهزة المحمولة.',
        'back': '← جميع أنواع QR',
        'lang_name': 'العربية',
    },
    'hi': {
        'title': 'PDF QR कोड जेनरेटर | PDF दस्तावेज़ों का लिंक',
        'meta': 'अपनी PDF फ़ाइल से लिंक करने वाला QR कोड बनाएं। मेन्यू, ब्रोशर, मैनुअल और दस्तावेज़ों के लिए बिल्कुल सही। मुफ्त और तुरंत।',
        'h1': 'PDF QR कोड जेनरेटर',
        'subtitle': 'एक साधारण स्कैन से कोई भी PDF दस्तावेज़ साझा करें',
        'label_url': 'PDF लिंक (URL)',
        'placeholder': 'https://example.com/document.pdf',
        'help_text': 'आपकी PDF ऑनलाइन होस्ट होनी चाहिए (Google Drive, Dropbox, आपकी वेबसाइट)',
        'btn_generate': 'QR कोड बनाएं',
        'btn_download': 'QR कोड डाउनलोड करें',
        'how_title': 'PDF QR कोड कैसे बनाएं',
        'step1': 'अपनी PDF को क्लाउड स्टोरेज (Google Drive, Dropbox) या अपनी वेबसाइट पर अपलोड करें',
        'step2': 'अपनी PDF का <strong>सार्वजनिक/साझा करने योग्य लिंक</strong> प्राप्त करें',
        'step3': 'ऊपर लिंक पेस्ट करें',
        'step4': 'अपना QR कोड बनाएं और डाउनलोड करें',
        'tip_title': '💡 प्रो टिप: Google Drive',
        'tip': 'Google Drive के लिए: PDF पर राइट-क्लिक करें → "लिंक प्राप्त करें" → "लिंक वाला कोई भी व्यक्ति" में बदलें → कॉपी करें',
        'why_title': 'PDF QR कोड क्यों उपयोग करें?',
        'why1_title': 'पेपरलेस',
        'why1': 'बिना प्रिंट किए दस्तावेज़ साझा करें - पर्यावरण के अनुकूल और किफायती',
        'why2_title': 'हमेशा अपडेट',
        'why2': 'कभी भी अपनी PDF अपडेट करें - QR कोड वही रहता है',
        'why3_title': 'व्यूज ट्रैक करें',
        'why3': 'bit.ly या समान का उपयोग करके ट्रैक करें कि कितने लोग आपकी PDF देखते हैं',
        'why4_title': 'हर जगह काम करता है',
        'why4': 'कोई भी स्मार्टफोन स्कैन कर सकता है और तुरंत PDF देख सकता है',
        'uses_title': 'PDF QR कोड के लोकप्रिय उपयोग',
        'uses': ['रेस्तरां मेन्यू', 'उत्पाद मैनुअल और निर्देश', 'इवेंट प्रोग्राम', 'रियल एस्टेट फ्लायर', 'बिज़नेस ब्रोशर', 'शैक्षिक सामग्री', 'मूल्य सूची और कैटलॉग'],
        'faq1_q': 'मुझे अपनी PDF कहां होस्ट करनी चाहिए?',
        'faq1_a': 'Google Drive (मुफ्त), Dropbox, OneDrive, या आपकी अपनी वेबसाइट सभी काम करती हैं। सुनिश्चित करें कि लिंक सार्वजनिक रूप से सुलभ है।',
        'faq2_q': 'क्या मैं बाद में PDF अपडेट कर सकता हूं?',
        'faq2_a': 'हां! यदि आप उसी URL पर फ़ाइल बदलते हैं, तो QR कोड नया संस्करण दिखाएगा। Google Drive के साथ, बस उसी फ़ाइल का नया संस्करण अपलोड करें।',
        'faq3_q': 'क्या फ़ाइल आकार की सीमा है?',
        'faq3_a': 'QR कोड बस आपकी PDF से लिंक करता है - कोई सीमा नहीं है। हालांकि, छोटी PDFs (10MB से कम) मोबाइल पर तेज़ी से लोड होती हैं।',
        'back': '← सभी QR प्रकार',
        'lang_name': 'हिन्दी',
    },
    'ru': {
        'title': 'Генератор QR-кода для PDF | Ссылка на PDF-документы',
        'meta': 'Создайте QR-код со ссылкой на ваш PDF-файл. Идеально для меню, брошюр, инструкций и документов. Бесплатно и мгновенно.',
        'h1': 'Генератор QR-кода для PDF',
        'subtitle': 'Делитесь любым PDF-документом простым сканированием',
        'label_url': 'Ссылка на PDF (URL)',
        'placeholder': 'https://example.com/document.pdf',
        'help_text': 'Ваш PDF должен быть размещён онлайн (Google Drive, Dropbox, ваш сайт)',
        'btn_generate': 'Создать QR-код',
        'btn_download': 'Скачать QR-код',
        'how_title': 'Как создать QR-код для PDF',
        'step1': 'Загрузите PDF в облачное хранилище (Google Drive, Dropbox) или на свой сайт',
        'step2': 'Получите <strong>публичную/общедоступную ссылку</strong> на PDF',
        'step3': 'Вставьте ссылку выше',
        'step4': 'Создайте и скачайте QR-код',
        'tip_title': '💡 Совет профи: Google Drive',
        'tip': 'Для Google Drive: ПКМ на PDF → "Получить ссылку" → Изменить на "Все, у кого есть ссылка" → Копировать',
        'why_title': 'Зачем использовать QR-код для PDF?',
        'why1_title': 'Без бумаги',
        'why1': 'Делитесь документами без печати — экологично и экономно',
        'why2_title': 'Всегда актуально',
        'why2': 'Обновляйте PDF когда угодно — QR-код остаётся прежним',
        'why3_title': 'Отслеживание просмотров',
        'why3': 'Используйте bit.ly или подобное для отслеживания количества просмотров PDF',
        'why4_title': 'Работает везде',
        'why4': 'Любой смартфон может отсканировать и мгновенно просмотреть PDF',
        'uses_title': 'Популярные применения QR-кодов для PDF',
        'uses': ['Меню ресторанов', 'Инструкции и руководства', 'Программы мероприятий', 'Листовки недвижимости', 'Бизнес-брошюры', 'Учебные материалы', 'Прайс-листы и каталоги'],
        'faq1_q': 'Где разместить PDF?',
        'faq1_a': 'Google Drive (бесплатно), Dropbox, OneDrive или собственный сайт — всё подходит. Убедитесь, что ссылка общедоступна.',
        'faq2_q': 'Можно обновить PDF позже?',
        'faq2_a': 'Да! Если заменить файл по той же ссылке, QR-код покажет новую версию. В Google Drive просто загрузите новую версию того же файла.',
        'faq3_q': 'Есть ограничение размера файла?',
        'faq3_a': 'QR-код только ссылается на PDF — ограничений нет. Однако меньшие PDF (до 10МБ) быстрее загружаются на мобильных.',
        'back': '← Все типы QR',
        'lang_name': 'Русский',
    },
    'tr': {
        'title': 'PDF QR Kodu Oluşturucu | PDF Belgelerine Link',
        'meta': 'PDF dosyanıza bağlanan bir QR kodu oluşturun. Menüler, broşürler, kılavuzlar ve belgeler için mükemmel. Ücretsiz ve anında.',
        'h1': 'PDF QR Kodu Oluşturucu',
        'subtitle': 'Basit bir tarama ile herhangi bir PDF belgesini paylaşın',
        'label_url': 'PDF Linki (URL)',
        'placeholder': 'https://ornek.com/belge.pdf',
        'help_text': 'PDF\'iniz çevrimiçi barındırılmalı (Google Drive, Dropbox, web siteniz)',
        'btn_generate': 'QR Kodu Oluştur',
        'btn_download': 'QR Kodu İndir',
        'how_title': 'PDF QR Kodu Nasıl Oluşturulur',
        'step1': 'PDF\'inizi bulut depolamaya (Google Drive, Dropbox) veya web sitenize yükleyin',
        'step2': 'PDF\'inizin <strong>herkese açık/paylaşılabilir linkini</strong> alın',
        'step3': 'Linki yukarıya yapıştırın',
        'step4': 'QR kodunuzu oluşturun ve indirin',
        'tip_title': '💡 Pro İpucu: Google Drive',
        'tip': 'Google Drive için: PDF\'e sağ tıklayın → "Link al" → "Linki bilen herkes" olarak değiştirin → Kopyalayın',
        'why_title': 'Neden PDF QR Kodu Kullanmalı?',
        'why1_title': 'Kağıtsız',
        'why1': 'Belgeleri yazdırmadan paylaşın — çevre dostu ve ekonomik',
        'why2_title': 'Her Zaman Güncel',
        'why2': 'PDF\'inizi istediğiniz zaman güncelleyin — QR kodu aynı kalır',
        'why3_title': 'Görüntülemeleri İzleyin',
        'why3': 'Kaç kişinin PDF\'inize eriştiğini izlemek için bit.ly veya benzerini kullanın',
        'why4_title': 'Her Yerde Çalışır',
        'why4': 'Herhangi bir akıllı telefon tarayabilir ve PDF\'leri anında görüntüleyebilir',
        'uses_title': 'PDF QR Kodlarının Popüler Kullanımları',
        'uses': ['Restoran menüleri', 'Ürün kılavuzları ve talimatlar', 'Etkinlik programları', 'Emlak ilanları', 'İş broşürleri', 'Eğitim materyalleri', 'Fiyat listeleri ve kataloglar'],
        'faq1_q': 'PDF\'imi nerede barındırmalıyım?',
        'faq1_a': 'Google Drive (ücretsiz), Dropbox, OneDrive veya kendi web siteniz hepsi çalışır. Linkin herkese açık olduğundan emin olun.',
        'faq2_q': 'PDF\'i daha sonra güncelleyebilir miyim?',
        'faq2_a': 'Evet! Aynı URL\'de dosyayı değiştirirseniz, QR kodu yeni sürümü gösterecektir. Google Drive ile aynı dosyanın yeni sürümünü yükleyin.',
        'faq3_q': 'Dosya boyutu sınırı var mı?',
        'faq3_a': 'QR kodu sadece PDF\'inize bağlanır — sınır yok. Ancak daha küçük PDF\'ler (10MB altı) mobil cihazlarda daha hızlı yüklenir.',
        'back': '← Tüm QR Tipleri',
        'lang_name': 'Türkçe',
    },
}


def get_lang_selector_options(page_type, current_lang, base_path):
    """Generate language selector options."""
    options = []
    for lang in LANGUAGES:
        if page_type == 'google-review':
            page = 'google-review'
        else:
            page = 'pdf'
        
        if lang == 'en':
            url = f"{base_path}{page}/"
        else:
            url = f"{base_path}{lang}/{page}/"
        
        selected = ' selected' if lang == current_lang else ''
        lang_name = GOOGLE_REVIEW.get(lang, {}).get('lang_name', lang)
        options.append(f'<option value="{url}"{selected} class="text-gray-800">{lang_name}</option>')
    return '\n'.join(options)


def generate_google_review_page(t, lang):
    """Generate Google Review QR page HTML."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    base_path = '../' if lang == 'en' else '../../'
    lang_options = get_lang_selector_options('google-review', lang, base_path)
    uses_list = ''.join([f'<li>{use}</li>' for use in t['uses']])
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    
    <link rel="canonical" href="https://qrcodes.win/{'' if lang == 'en' else lang + '/'}google-review/">
    <link rel="icon" href="{base_path}favicon.svg" type="image/svg+xml">
    
    <meta property="og:title" content="{t['h1']}">
    <meta property="og:description" content="{t['meta']}">
    <meta property="og:type" content="website">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebPage","name":"{t['h1']}","description":"{t['meta']}","url":"https://qrcodes.win/{'' if lang == 'en' else lang + '/'}google-review/","mainEntity":{{"@type":"SoftwareApplication","name":"Google Review QR Code Generator","applicationCategory":"UtilitiesApplication","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {{"@type":"Question","name":"{t['faq1_q']}","acceptedAnswer":{{"@type":"Answer","text":"{t['faq1_a']}"}}}},
        {{"@type":"Question","name":"{t['faq2_q']}","acceptedAnswer":{{"@type":"Answer","text":"{t['faq2_a']}"}}}},
        {{"@type":"Question","name":"{t['faq3_q']}","acceptedAnswer":{{"@type":"Answer","text":"{t['faq3_a']}"}}}}
    ]}}
    </script>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="{base_path}qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }}
        .input-field {{ border: 2px solid #e5e7eb; }}
        .input-field:focus {{ border-color: #4F46E5; outline: none; box-shadow: 0 0 0 3px rgba(79,70,229,0.1); }}
    </style>
</head>
<body class="text-gray-900">
    <header class="py-6 px-4">
        <div class="max-w-4xl mx-auto flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-2 text-white">
                <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center">
                    <i data-lucide="qr-code" class="w-6 h-6"></i>
                </div>
                <span class="text-xl font-bold">QRCodes.win</span>
            </a>
            <a href="{base_path}" class="text-white/80 hover:text-white text-sm">{t['back']}</a>
            <select onchange="window.location.href=this.value" class="bg-white/20 text-white text-sm rounded-lg px-3 py-2 outline-none cursor-pointer border border-white/30">
                {lang_options}
            </select>
        </div>
    </header>

    <main class="px-4 pb-16">
        <div class="max-w-4xl mx-auto">
            <div class="text-center mb-8">
                <h1 class="text-3xl md:text-4xl font-bold text-white mb-2">⭐ {t['h1']}</h1>
                <p class="text-white/80">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 shadow-2xl mb-8">
                <div class="grid md:grid-cols-2 gap-8">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">{t['label_url']}</label>
                        <input type="url" id="reviewUrl" placeholder="{t['placeholder']}" class="input-field w-full px-4 py-3 rounded-xl text-lg">
                        <p class="text-sm text-gray-500 mt-2">{t['help_text']}</p>
                        
                        <button onclick="generateQR()" class="w-full mt-4 bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold py-3 px-6 rounded-xl hover:opacity-90 transition">
                            {t['btn_generate']}
                        </button>
                    </div>
                    
                    <div class="flex flex-col items-center justify-center">
                        <div id="qrcode" class="bg-white p-4 rounded-xl shadow-lg"></div>
                        <button id="downloadBtn" onclick="downloadQR()" class="mt-4 bg-gray-900 text-white font-medium py-2 px-6 rounded-lg hover:bg-gray-800 transition hidden">
                            {t['btn_download']}
                        </button>
                    </div>
                </div>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 mb-8">
                <h2 class="text-xl font-bold mb-4">{t['how_title']}</h2>
                <ol class="space-y-3 text-gray-700">
                    <li class="flex gap-3"><span class="bg-indigo-100 text-indigo-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">1</span>{t['step1']}</li>
                    <li class="flex gap-3"><span class="bg-indigo-100 text-indigo-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">2</span>{t['step2']}</li>
                    <li class="flex gap-3"><span class="bg-indigo-100 text-indigo-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">3</span>{t['step3']}</li>
                    <li class="flex gap-3"><span class="bg-indigo-100 text-indigo-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">4</span>{t['step4']}</li>
                </ol>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 mb-8">
                <h2 class="text-xl font-bold mb-6">{t['why_title']}</h2>
                <div class="grid md:grid-cols-2 gap-4">
                    <div class="p-4 bg-green-50 rounded-xl"><h3 class="font-semibold text-green-800">📈 {t['why1_title']}</h3><p class="text-green-700 text-sm mt-1">{t['why1']}</p></div>
                    <div class="p-4 bg-blue-50 rounded-xl"><h3 class="font-semibold text-blue-800">🔍 {t['why2_title']}</h3><p class="text-blue-700 text-sm mt-1">{t['why2']}</p></div>
                    <div class="p-4 bg-purple-50 rounded-xl"><h3 class="font-semibold text-purple-800">🤝 {t['why3_title']}</h3><p class="text-purple-700 text-sm mt-1">{t['why3']}</p></div>
                    <div class="p-4 bg-amber-50 rounded-xl"><h3 class="font-semibold text-amber-800">📤 {t['why4_title']}</h3><p class="text-amber-700 text-sm mt-1">{t['why4']}</p></div>
                </div>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 mb-8">
                <h2 class="text-xl font-bold mb-4">{t['uses_title']}</h2>
                <ul class="grid md:grid-cols-2 gap-2 text-gray-700">
                    {uses_list}
                </ul>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8">
                <h2 class="text-xl font-bold mb-4">FAQ</h2>
                <div class="space-y-4">
                    <div><h3 class="font-semibold text-indigo-700">{t['faq1_q']}</h3><p class="text-gray-600 mt-1">{t['faq1_a']}</p></div>
                    <div><h3 class="font-semibold text-indigo-700">{t['faq2_q']}</h3><p class="text-gray-600 mt-1">{t['faq2_a']}</p></div>
                    <div><h3 class="font-semibold text-indigo-700">{t['faq3_q']}</h3><p class="text-gray-600 mt-1">{t['faq3_a']}</p></div>
                </div>
            </div>
        </div>
    </main>

    <footer class="py-8 px-4 border-t border-white/10">
        <div class="max-w-4xl mx-auto text-center text-white/60 text-sm">
            <p>© 2026 QRCodes.win — Free QR Code Generator</p>
        </div>
    </footer>

    <script>
        let qr = null;
        function generateQR() {{
            const url = document.getElementById('reviewUrl').value.trim();
            if (!url) return alert('Please enter a URL');
            
            const container = document.getElementById('qrcode');
            container.innerHTML = '';
            
            qr = new QRCode(container, {{
                text: url,
                width: 200,
                height: 200,
                colorDark: '#000000',
                colorLight: '#ffffff',
                correctLevel: QRCode.CorrectLevel.H
            }});
            
            document.getElementById('downloadBtn').classList.remove('hidden');
        }}
        
        function downloadQR() {{
            const canvas = document.querySelector('#qrcode canvas');
            if (canvas) {{
                const link = document.createElement('a');
                link.download = 'google-review-qr.png';
                link.href = canvas.toDataURL('image/png');
                link.click();
            }}
        }}
        
        lucide.createIcons();
    </script>
</body>
</html>'''


def generate_pdf_page(t, lang):
    """Generate PDF QR page HTML."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    base_path = '../' if lang == 'en' else '../../'
    lang_options = get_lang_selector_options('pdf', lang, base_path)
    uses_list = ''.join([f'<li>{use}</li>' for use in t['uses']])
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    
    <link rel="canonical" href="https://qrcodes.win/{'' if lang == 'en' else lang + '/'}pdf/">
    <link rel="icon" href="{base_path}favicon.svg" type="image/svg+xml">
    
    <meta property="og:title" content="{t['h1']}">
    <meta property="og:description" content="{t['meta']}">
    <meta property="og:type" content="website">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebPage","name":"{t['h1']}","description":"{t['meta']}","url":"https://qrcodes.win/{'' if lang == 'en' else lang + '/'}pdf/","mainEntity":{{"@type":"SoftwareApplication","name":"PDF QR Code Generator","applicationCategory":"UtilitiesApplication","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {{"@type":"Question","name":"{t['faq1_q']}","acceptedAnswer":{{"@type":"Answer","text":"{t['faq1_a']}"}}}},
        {{"@type":"Question","name":"{t['faq2_q']}","acceptedAnswer":{{"@type":"Answer","text":"{t['faq2_a']}"}}}},
        {{"@type":"Question","name":"{t['faq3_q']}","acceptedAnswer":{{"@type":"Answer","text":"{t['faq3_a']}"}}}}
    ]}}
    </script>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="{base_path}qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }}
        .input-field {{ border: 2px solid #e5e7eb; }}
        .input-field:focus {{ border-color: #dc2626; outline: none; box-shadow: 0 0 0 3px rgba(220,38,38,0.1); }}
    </style>
</head>
<body class="text-gray-900">
    <header class="py-6 px-4">
        <div class="max-w-4xl mx-auto flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-2 text-white">
                <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center">
                    <i data-lucide="qr-code" class="w-6 h-6"></i>
                </div>
                <span class="text-xl font-bold">QRCodes.win</span>
            </a>
            <a href="{base_path}" class="text-white/80 hover:text-white text-sm">{t['back']}</a>
            <select onchange="window.location.href=this.value" class="bg-white/20 text-white text-sm rounded-lg px-3 py-2 outline-none cursor-pointer border border-white/30">
                {lang_options}
            </select>
        </div>
    </header>

    <main class="px-4 pb-16">
        <div class="max-w-4xl mx-auto">
            <div class="text-center mb-8">
                <h1 class="text-3xl md:text-4xl font-bold text-white mb-2">📄 {t['h1']}</h1>
                <p class="text-white/80">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 shadow-2xl mb-8">
                <div class="grid md:grid-cols-2 gap-8">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">{t['label_url']}</label>
                        <input type="url" id="pdfUrl" placeholder="{t['placeholder']}" class="input-field w-full px-4 py-3 rounded-xl text-lg">
                        <p class="text-sm text-gray-500 mt-2">{t['help_text']}</p>
                        
                        <button onclick="generateQR()" class="w-full mt-4 bg-gradient-to-r from-red-600 to-orange-600 text-white font-semibold py-3 px-6 rounded-xl hover:opacity-90 transition">
                            {t['btn_generate']}
                        </button>
                    </div>
                    
                    <div class="flex flex-col items-center justify-center">
                        <div id="qrcode" class="bg-white p-4 rounded-xl shadow-lg"></div>
                        <button id="downloadBtn" onclick="downloadQR()" class="mt-4 bg-gray-900 text-white font-medium py-2 px-6 rounded-lg hover:bg-gray-800 transition hidden">
                            {t['btn_download']}
                        </button>
                    </div>
                </div>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 mb-8">
                <h2 class="text-xl font-bold mb-4">{t['how_title']}</h2>
                <ol class="space-y-3 text-gray-700">
                    <li class="flex gap-3"><span class="bg-red-100 text-red-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">1</span>{t['step1']}</li>
                    <li class="flex gap-3"><span class="bg-red-100 text-red-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">2</span>{t['step2']}</li>
                    <li class="flex gap-3"><span class="bg-red-100 text-red-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">3</span>{t['step3']}</li>
                    <li class="flex gap-3"><span class="bg-red-100 text-red-700 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">4</span>{t['step4']}</li>
                </ol>
                <div class="mt-4 p-4 bg-amber-50 rounded-xl border border-amber-200">
                    <p class="font-semibold text-amber-800">{t['tip_title']}</p>
                    <p class="text-amber-700 text-sm mt-1">{t['tip']}</p>
                </div>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 mb-8">
                <h2 class="text-xl font-bold mb-6">{t['why_title']}</h2>
                <div class="grid md:grid-cols-2 gap-4">
                    <div class="p-4 bg-green-50 rounded-xl"><h3 class="font-semibold text-green-800">🌱 {t['why1_title']}</h3><p class="text-green-700 text-sm mt-1">{t['why1']}</p></div>
                    <div class="p-4 bg-blue-50 rounded-xl"><h3 class="font-semibold text-blue-800">🔄 {t['why2_title']}</h3><p class="text-blue-700 text-sm mt-1">{t['why2']}</p></div>
                    <div class="p-4 bg-purple-50 rounded-xl"><h3 class="font-semibold text-purple-800">📊 {t['why3_title']}</h3><p class="text-purple-700 text-sm mt-1">{t['why3']}</p></div>
                    <div class="p-4 bg-amber-50 rounded-xl"><h3 class="font-semibold text-amber-800">📱 {t['why4_title']}</h3><p class="text-amber-700 text-sm mt-1">{t['why4']}</p></div>
                </div>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8 mb-8">
                <h2 class="text-xl font-bold mb-4">{t['uses_title']}</h2>
                <ul class="grid md:grid-cols-2 gap-2 text-gray-700">
                    {uses_list}
                </ul>
            </div>

            <div class="glass rounded-2xl p-6 md:p-8">
                <h2 class="text-xl font-bold mb-4">FAQ</h2>
                <div class="space-y-4">
                    <div><h3 class="font-semibold text-red-700">{t['faq1_q']}</h3><p class="text-gray-600 mt-1">{t['faq1_a']}</p></div>
                    <div><h3 class="font-semibold text-red-700">{t['faq2_q']}</h3><p class="text-gray-600 mt-1">{t['faq2_a']}</p></div>
                    <div><h3 class="font-semibold text-red-700">{t['faq3_q']}</h3><p class="text-gray-600 mt-1">{t['faq3_a']}</p></div>
                </div>
            </div>
        </div>
    </main>

    <footer class="py-8 px-4 border-t border-white/10">
        <div class="max-w-4xl mx-auto text-center text-white/60 text-sm">
            <p>© 2026 QRCodes.win — Free QR Code Generator</p>
        </div>
    </footer>

    <script>
        let qr = null;
        function generateQR() {{
            const url = document.getElementById('pdfUrl').value.trim();
            if (!url) return alert('Please enter a PDF URL');
            
            const container = document.getElementById('qrcode');
            container.innerHTML = '';
            
            qr = new QRCode(container, {{
                text: url,
                width: 200,
                height: 200,
                colorDark: '#000000',
                colorLight: '#ffffff',
                correctLevel: QRCode.CorrectLevel.H
            }});
            
            document.getElementById('downloadBtn').classList.remove('hidden');
        }}
        
        function downloadQR() {{
            const canvas = document.querySelector('#qrcode canvas');
            if (canvas) {{
                const link = document.createElement('a');
                link.download = 'pdf-qr-code.png';
                link.href = canvas.toDataURL('image/png');
                link.click();
            }}
        }}
        
        lucide.createIcons();
    </script>
</body>
</html>'''


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate Google Review pages
    print("Generating Google Review QR pages...")
    for lang in LANGUAGES:
        t = GOOGLE_REVIEW.get(lang, GOOGLE_REVIEW['en'])
        
        if lang == 'en':
            out_dir = os.path.join(base_dir, 'google-review')
        else:
            out_dir = os.path.join(base_dir, lang, 'google-review')
        
        os.makedirs(out_dir, exist_ok=True)
        html = generate_google_review_page(t, lang)
        
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {lang}")
    
    # Generate PDF pages
    print("\nGenerating PDF QR pages...")
    for lang in LANGUAGES:
        t = PDF_QR.get(lang, PDF_QR['en'])
        
        if lang == 'en':
            out_dir = os.path.join(base_dir, 'pdf')
        else:
            out_dir = os.path.join(base_dir, lang, 'pdf')
        
        os.makedirs(out_dir, exist_ok=True)
        html = generate_pdf_page(t, lang)
        
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {lang}")
    
    print(f"\n🎉 Generated 22 pages (2 types × 11 languages)!")


if __name__ == '__main__':
    main()

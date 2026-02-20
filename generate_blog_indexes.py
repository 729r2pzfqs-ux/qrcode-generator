#!/usr/bin/env python3
"""Generate blog index pages for all languages."""
import os

LANGS = {
    'de': {'title': 'QR-Code Blog', 'subtitle': 'Tipps, Anleitungen und Best Practices', 'back': '← QR-Generator', 'new': 'NEU',
           'art1': 'Wie QR-Codes funktionieren: Die Technologie erklärt', 'art1_desc': 'Haben Sie sich jemals gefragt, wie diese schwarz-weißen Quadrate funktionieren? Erfahren Sie mehr über Positionsmarkierungen, Fehlerkorrektur und mehr.',
           'art2': 'Sind QR-Codes sicher? Sicherheitsrisiken & Schutz', 'art2_desc': 'QR-Codes sind überall, aber sind sie sicher? Erfahren Sie mehr über Phishing-Risiken und wie Sie sich schützen können.'},
    'es': {'title': 'Blog de Códigos QR', 'subtitle': 'Consejos, guías y mejores prácticas', 'back': '← Generador QR', 'new': 'NUEVO',
           'art1': 'Cómo Funcionan los Códigos QR: La Tecnología Explicada', 'art1_desc': '¿Alguna vez te preguntaste cómo funcionan esos cuadrados blancos y negros? Aprende sobre patrones de posición, corrección de errores y más.',
           'art2': '¿Son Seguros los Códigos QR? Riesgos y Protección', 'art2_desc': 'Los códigos QR están en todas partes, ¿pero son seguros? Conoce los riesgos de phishing y cómo protegerte.'},
    'fr': {'title': 'Blog QR Code', 'subtitle': 'Conseils, guides et bonnes pratiques', 'back': '← Générateur QR', 'new': 'NOUVEAU',
           'art1': 'Comment Fonctionnent les QR Codes: La Technologie Expliquée', 'art1_desc': 'Vous êtes-vous déjà demandé comment fonctionnent ces carrés noirs et blancs? Découvrez les motifs de position, la correction d\'erreurs et plus.',
           'art2': 'Les QR Codes Sont-ils Sûrs? Risques et Protection', 'art2_desc': 'Les QR codes sont partout, mais sont-ils sûrs? Découvrez les risques de phishing et comment vous protéger.'},
    'pt': {'title': 'Blog de QR Codes', 'subtitle': 'Dicas, guias e melhores práticas', 'back': '← Gerador QR', 'new': 'NOVO',
           'art1': 'Como os QR Codes Funcionam: A Tecnologia Explicada', 'art1_desc': 'Já se perguntou como esses quadrados pretos e brancos funcionam? Aprenda sobre padrões de posição, correção de erros e mais.',
           'art2': 'QR Codes São Seguros? Riscos e Proteção', 'art2_desc': 'QR codes estão em toda parte, mas são seguros? Conheça os riscos de phishing e como se proteger.'},
    'zh': {'title': 'QR码博客', 'subtitle': '技巧、指南和最佳实践', 'back': '← QR生成器', 'new': '新',
           'art1': '二维码如何工作：技术解析', 'art1_desc': '想知道那些黑白方块是如何工作的吗？了解定位图案、纠错等技术。',
           'art2': '二维码安全吗？风险与防护', 'art2_desc': '二维码无处不在，但它们安全吗？了解钓鱼风险以及如何保护自己。'},
    'ja': {'title': 'QRコードブログ', 'subtitle': 'ヒント、ガイド、ベストプラクティス', 'back': '← QRジェネレーター', 'new': '新着',
           'art1': 'QRコードの仕組み：技術解説', 'art1_desc': 'あの白黒の四角がどのように機能するか考えたことはありますか？位置検出パターン、エラー訂正などについて学びましょう。',
           'art2': 'QRコードは安全？リスクと対策', 'art2_desc': 'QRコードはどこにでもありますが、安全ですか？フィッシングリスクと身を守る方法を学びましょう。'},
    'ar': {'title': 'مدونة رموز QR', 'subtitle': 'نصائح وإرشادات وأفضل الممارسات', 'back': 'مولد QR ←', 'new': 'جديد',
           'art1': 'كيف تعمل رموز QR: شرح التقنية', 'art1_desc': 'هل تساءلت يومًا كيف تعمل تلك المربعات السوداء والبيضاء؟ تعرف على أنماط الموقع وتصحيح الأخطاء والمزيد.',
           'art2': 'هل رموز QR آمنة؟ المخاطر والحماية', 'art2_desc': 'رموز QR في كل مكان، لكن هل هي آمنة؟ تعرف على مخاطر التصيد وكيفية حماية نفسك.'},
    'hi': {'title': 'QR कोड ब्लॉग', 'subtitle': 'टिप्स, गाइड और बेस्ट प्रैक्टिस', 'back': '← QR जेनरेटर', 'new': 'नया',
           'art1': 'QR कोड कैसे काम करते हैं: तकनीक की व्याख्या', 'art1_desc': 'क्या आपने कभी सोचा है कि वे काले और सफेद वर्ग कैसे काम करते हैं? पोजीशन पैटर्न, एरर करेक्शन और बहुत कुछ जानें।',
           'art2': 'क्या QR कोड सुरक्षित हैं? जोखिम और सुरक्षा', 'art2_desc': 'QR कोड हर जगह हैं, लेकिन क्या वे सुरक्षित हैं? फिशिंग जोखिमों और खुद को कैसे बचाएं यह जानें।'},
    'ru': {'title': 'Блог о QR-кодах', 'subtitle': 'Советы, руководства и лучшие практики', 'back': '← QR-генератор', 'new': 'НОВОЕ',
           'art1': 'Как работают QR-коды: технология простыми словами', 'art1_desc': 'Задумывались ли вы, как работают эти чёрно-белые квадраты? Узнайте о поисковых паттернах, коррекции ошибок и многом другом.',
           'art2': 'Безопасны ли QR-коды? Риски и защита', 'art2_desc': 'QR-коды повсюду, но безопасны ли они? Узнайте о рисках фишинга и как защитить себя.'},
    'tr': {'title': 'QR Kod Blogu', 'subtitle': 'İpuçları, rehberler ve en iyi uygulamalar', 'back': '← QR Oluşturucu', 'new': 'YENİ',
           'art1': 'QR Kodları Nasıl Çalışır: Teknoloji Açıklandı', 'art1_desc': 'O siyah beyaz karelerin nasıl çalıştığını hiç merak ettiniz mi? Konum desenleri, hata düzeltme ve daha fazlasını öğrenin.',
           'art2': 'QR Kodları Güvenli mi? Riskler ve Korunma', 'art2_desc': 'QR kodlar her yerde, ama güvenli mi? Kimlik avı riskleri ve kendinizi nasıl koruyacağınızı öğrenin.'},
}

def gen_index(lang, t):
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['subtitle']}">
    <link rel="canonical" href="https://qrcodes.win/blog/{lang}/">
    <link rel="icon" href="../../favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }}
    </style>
</head>
<body class="text-gray-900">
    <header class="py-6 px-4">
        <div class="max-w-4xl mx-auto flex items-center justify-between">
            <a href="../../{lang}/" class="flex items-center gap-2 text-white">
                <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center">
                    <i data-lucide="qr-code" class="w-6 h-6"></i>
                </div>
                <span class="text-xl font-bold">QRCodes.win</span>
            </a>
            <a href="../../{lang}/" class="text-white/80 hover:text-white text-sm">{t['back']}</a>
        </div>
    </header>

    <main class="px-4 pb-12">
        <div class="max-w-4xl mx-auto">
            <div class="text-center text-white mb-10">
                <h1 class="text-3xl md:text-5xl font-bold mb-4">{t['title']}</h1>
                <p class="text-white/80 text-lg">{t['subtitle']}</p>
            </div>

            <div class="space-y-6">
                <a href="how-qr-codes-work/" class="glass rounded-2xl p-6 shadow-xl block hover:shadow-2xl transition-shadow">
                    <div class="flex items-start gap-4">
                        <div class="w-16 h-16 bg-blue-100 rounded-xl flex items-center justify-center flex-shrink-0">
                            <i data-lucide="cpu" class="w-8 h-8 text-blue-600"></i>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="bg-blue-600 text-white text-xs px-2 py-0.5 rounded-full">{t['new']}</span>
                            </div>
                            <h2 class="text-xl font-bold mb-2">{t['art1']}</h2>
                            <p class="text-gray-600 mb-3">{t['art1_desc']}</p>
                            <span class="text-indigo-600 font-medium text-sm">→</span>
                        </div>
                    </div>
                </a>

                <a href="qr-code-safety/" class="glass rounded-2xl p-6 shadow-xl block hover:shadow-2xl transition-shadow">
                    <div class="flex items-start gap-4">
                        <div class="w-16 h-16 bg-red-100 rounded-xl flex items-center justify-center flex-shrink-0">
                            <i data-lucide="shield-check" class="w-8 h-8 text-red-600"></i>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="bg-red-600 text-white text-xs px-2 py-0.5 rounded-full">{t['new']}</span>
                            </div>
                            <h2 class="text-xl font-bold mb-2">{t['art2']}</h2>
                            <p class="text-gray-600 mb-3">{t['art2_desc']}</p>
                            <span class="text-indigo-600 font-medium text-sm">→</span>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </main>

    <footer class="py-8 px-4 text-center text-white/60 text-sm">
        <p>© 2026 QRCodes.win</p>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>'''

base = os.path.dirname(os.path.abspath(__file__))
for lang, t in LANGS.items():
    out_dir = os.path.join(base, 'blog', lang)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(gen_index(lang, t))
    print(f"✅ {lang}")

print(f"\n🎉 Created 10 translated blog indexes!")

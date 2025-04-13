# 🛡️ Phishing URL Tespit Aracı (CLI Tool)

URL'leri analiz ederek **phishing (oltalama) saldırılarını tespit** etmeye yardımcı olan hafif, hızlı ve açık kaynaklı bir komut satırı aracıdır. Python ile geliştirilmiştir ve çeşitli URL göstergeleri kullanılarak risk puanlaması yapar.

---

## 🚀 Özellikler

- 🔍 IP adresi kullanımı kontrolü
- 🔐 HTTPS ve SSL sertifikası denetimi
- 🔗 URL uzunluğu, `@`, `-`, `/` karakter analizi
- 🌍 Şüpheli TLD uzantıları kontrolü (.tk, .ga, .cf vs.)
- 📌 Phishing odaklı anahtar kelime arama (`login`, `secure`, `account`, `paypal`, vb.)
- 🧠 Typosquatting tespiti (örn. `g00gle`, `faceb00k`)
- 📊 Puanlama sistemi ile yorumlama: Güvenli / Riskli / Şüpheli

---

## 🧪 Örnek Kullanım

```bash
$ python phishing_detector.py https://secure-login.paypa1.com

## Çıktı:

{
    "URL": "https://secure-login.paypa1.com",
    "Durum": "🚨 ŞÜPHELİ!",
    "Toplam Risk Skoru": 9,
    "Nedenler": [
        "'paypa1' şüpheli domain benzerliği",
        "'login' kelimesi içeriyor",
        "Alan adında '-' karakteri var",
        "Şüpheli TLD uzantısı (.com değilse)",
        "SSL sertifikası alınamıyor"
    ]
}

📁 Proje Klasör Yapısı:

phishing-url-detector/
│
├── phishing_detector.py       # CLI uygulaması
├── indicators.py              # URL analiz göstergeleri
├── requirements.txt           # Bağımlılıklar (opsiyonel)
├── .gitignore                 # Gereksiz dosyaları dışlama
├── LICENSE                    # MIT lisansı
└── README.md                  # Bu dosya

🔧 Kurulum

Python 3.7+ sürümünün sisteminizde yüklü olduğundan emin olun:
git clone https://github.com/omeredebal/phishing_detector.git
cd phishing_detector
pip install -r requirements.txt

📌 Kullanım:

python phishing_detector.py <URL>

Örnek:
python phishing_detector.py https://example.com

🧠 Genişletilebilirlik:
Proje yapısı modüler olacak şekilde hazırlandı.
Yeni analiz göstergeleri eklemek için indicators.py dosyasına yeni fonksiyonlar yazabilir, phishing_detector.py dosyasına entegre edebilirsiniz.

⚖️ Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Özgürce kullanabilir, geliştirebilir ve paylaşabilirsiniz.

✨ Katkı Sağla
Katkılara açığız! Yeni tespit metotları, False Positive filtreleri ya da arayüz geliştirmeleri için pull request gönderebilirsiniz.

🙌 Geliştirici
Ömer Edebalı
👨‍💻 Yazılım Mühendisliği 3. sınıf öğrencisi | Siber Güvenlik Uzmanı Adayı
📫 LinkedIn Profilim: https://www.linkedin.com/in/omeredebal/

⭐ Destek Olmak İstersen
Projeyi faydalı bulduysan, GitHub üzerinde ⭐ vermeyi unutma!

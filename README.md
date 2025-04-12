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

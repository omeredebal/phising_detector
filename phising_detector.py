import json
import sys
from urllib.parse import urlparse

# URL'yi analiz etme ve risk değerlendirmesi yapma
def analyze_url(url):
    # URL'yi çözümle
    parsed = urlparse(url)
    
    # Risk analizini yapacak göstergeler (example)
    result = {
        "URL": url,
        "Durum": "🚨 ŞÜPHELİ!",
        "Toplam Risk Skoru": 0,
        "Nedenler": []
    }

    # HTTPS kontrolü
    if parsed.scheme != "https":
        result["Nedenler"].append("HTTPS kullanılmıyor")
        result["Toplam Risk Skoru"] += 5
    
    # Alan adında '-' karakteri olup olmadığını kontrol et
    if "-" in parsed.netloc:
        result["Nedenler"].append("Alan adında '-' karakteri var")
        result["Toplam Risk Skoru"] += 2
    
    # 'bank' kelimesinin URL içinde olup olmadığını kontrol et
    if "bank" in parsed.netloc:
        result["Nedenler"].append("'bank' kelimesi içeriyor")
        result["Toplam Risk Skoru"] += 1

    # 'login' kelimesinin URL içinde olup olmadığını kontrol et
    if "login" in parsed.netloc:
        result["Nedenler"].append("'login' kelimesi içeriyor")
        result["Toplam Risk Skoru"] += 1

    # 'secure' kelimesinin URL içinde olup olmadığını kontrol et
    if "secure" in parsed.netloc:
        result["Nedenler"].append("'secure' kelimesi içeriyor")
        result["Toplam Risk Skoru"] += 1

    # 'update' kelimesinin URL içinde olup olmadığını kontrol et
    if "update" in parsed.netloc:
        result["Nedenler"].append("'update' kelimesi içeriyor")
        result["Toplam Risk Skoru"] += 1

    # Eğer risk skoru 5 veya daha yüksekse, ŞÜPHELİ!
    if result["Toplam Risk Skoru"] > 0:
        result["Durum"] = "🚨 ŞÜPHELİ!"
    else:
        result["Durum"] = "✅ Güvenli görünüyor."
    
    # JSON çıktısını düzgün bir şekilde yazdırma (Türkçe karakterlerle)
    return json.dumps(result, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        result = analyze_url(url)
        print(result)
    else:
        print("Lütfen bir URL girin.")

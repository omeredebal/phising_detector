import sys
import json
from indicators import (
    check_ip_address,
    check_https,
    check_url_length,
    check_at_symbol,
    check_hyphen_in_domain,
    check_many_slashes,
    check_complex_domain,
    check_suspicious_tlds,
    check_keywords,
    check_typosquatting,
    check_ssl_certificate
)

def analyze_url(url):
    score = 0
    reasons = []

    # URL'i analiz et
    if not url.startswith("http"):
        url = "http://" + url  # https veya http olmadığında, http ile başlat

    parsed = urlparse(url)
    domain = parsed.netloc

    results = []

    # Göstergeleri kontrol et
    check_ip_address(url, domain, results)
    check_https(url, domain, results)
    check_url_length(url, domain, results)
    check_at_symbol(url, domain, results)
    check_hyphen_in_domain(url, domain, results)
    check_many_slashes(url, domain, results)
    check_complex_domain(url, domain, results)
    check_suspicious_tlds(url, domain, results)
    check_keywords(url, domain, results)
    check_typosquatting(url, domain, results)
    
    if url.startswith("https://"):
        check_ssl_certificate(domain, results)

    # Sonuçları işle
    for reason, point in results:
        score += point
        reasons.append(reason)

    # Risk puanına göre sonuca karar ver
    if score >= 7:
        verdict = "🚨 ŞÜPHELİ!"
    elif score >= 4:
        verdict = "⚠️ Riskli"
    else:
        verdict = "✅ Güvenli görünüyor."

    # Çıktı olarak JSON formatında döndür
    result = {
        "URL": url,
        "Durum": verdict,
        "Toplam Risk Skoru": score,
        "Nedenler": reasons
    }
    
    return json.dumps(result, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python phishing_detector.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = analyze_url(url)
    print(result)

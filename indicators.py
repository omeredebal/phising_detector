import re
from urllib.parse import urlparse
import ssl
import socket

def check_ip_address(url, domain, results):
    if re.match(r"(\d{1,3}\.){3}\d{1,3}", domain):
        results.append(("IP adresi içeriyor", 3))

def check_https(url, domain, results):
    if not url.startswith("https://"):
        results.append(("HTTPS kullanılmıyor", 2))

def check_url_length(url, domain, results):
    if len(url) > 75:
        results.append(("URL çok uzun", 1))

def check_at_symbol(url, domain, results):
    if '@' in url:
        results.append(("@ karakteri içeriyor", 1))

def check_hyphen_in_domain(url, domain, results):
    if '-' in domain:
        results.append(("Alan adında '-' karakteri var", 1))

def check_many_slashes(url, domain, results):
    if url.count('/') > 5:
        results.append(("Çok fazla '/' karakteri içeriyor", 1))

def check_complex_domain(url, domain, results):
    if domain.count('.') > 3:
        results.append(("Alan adı yapısı karmaşık (çok fazla nokta)", 1))

def check_suspicious_tlds(url, domain, results):
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
    for tld in suspicious_tlds:
        if domain.endswith(tld):
            results.append((f"Şüpheli TLD uzantısı ({tld})", 2))

def check_keywords(url, domain, results):
    suspicious_keywords = ["paypal", "bank", "login", "secure", "account", "update"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            results.append((f"'{keyword}' kelimesi içeriyor", 2))

def check_typosquatting(url, domain, results):
    typos = ['paypa1', 'faceb00k', 'g00gle', 'micros0ft']
    for typo in typos:
        if typo in domain:
            results.append((f"'{typo}' şüpheli domain benzerliği", 2))

def check_ssl_certificate(domain, results):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain
        )
        conn.settimeout(3)
        conn.connect((domain, 443))
    except Exception:
        results.append(("SSL sertifikası geçersiz veya alınamıyor", 2))

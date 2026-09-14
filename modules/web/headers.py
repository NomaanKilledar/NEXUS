import requests

from modules.reports.logger import log_event


SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps control which resources a page can load.",
    "X-Frame-Options": "Helps prevent clickjacking.",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing.",
    "Referrer-Policy": "Controls referrer information sent by the browser.",
    "Permissions-Policy": "Controls access to browser features.",
    "Strict-Transport-Security": "Forces browsers to use HTTPS.",
}


def analyze_headers(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True,
            headers={
                "User-Agent": "NEXUS-Security-Analyzer/1.0"
            },
        )

    except requests.RequestException as exc:
        print(f"\nRequest failed: {exc}")
        return

    print("\n========== WEB SECURITY HEADERS ==========\n")
    print(f"URL: {response.url}")
    print(f"Status: {response.status_code}\n")

    print("Security Header Analysis")
    print("-" * 60)

    for header, description in SECURITY_HEADERS.items():
        value = response.headers.get(header)

        if value:
            print(f"[+] {header}")
            print(f"    {value}")
        else:
            print(f"[-] {header}")
            print(f"    Missing — {description}")

        print()

    print("==========================================\n")


def show_header_analyzer():
    print("\n========== HEADER SECURITY ANALYZER ==========\n")

    url = input("Website URL: ").strip()

    if not url:
        print("URL cannot be empty.")
        return

    log_event(f"Security Header Analyzer | URL: {url}")

    analyze_headers(url)
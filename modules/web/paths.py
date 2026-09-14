import requests

from modules.reports.logger import log_event


COMMON_PATHS = [
    "/admin",
    "/login",
    "/robots.txt",
    "/sitemap.xml",
    "/.well-known/",
    "/backup",
    "/backup.zip",
    "/test",
    "/dev",
    "/api",
]


def check_path(base_url, path):
    url = base_url.rstrip("/") + path

    try:
        response = requests.get(
            url,
            timeout=5,
            allow_redirects=False,
            headers={
                "User-Agent": "NEXUS-Security-Analyzer/1.0"
            },
        )

        return response.status_code

    except requests.RequestException:
        return None


def show_path_checker():
    print("\n========== WEB PATH CHECKER ==========\n")

    url = input("Website URL: ").strip()

    if not url:
        print("URL cannot be empty.")
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    log_event(
        f"Directory/Path Checker | URL: {url}"
    )

    print(f"\nChecking common paths on: {url}")
    print("-" * 55)

    found = 0

    for path in COMMON_PATHS:
        status = check_path(url, path)

        if status is None:
            print(f"[!] {path:<20} Request failed")
            continue

        if status in (200, 204, 301, 302, 307, 308):
            print(f"[+] {path:<20} HTTP {status}")
            found += 1

        elif status in (401, 403):
            print(f"[?] {path:<20} HTTP {status} Protected")

        else:
            print(f"[-] {path:<20} HTTP {status}")

    print("\n" + "-" * 55)
    print(f"Interesting paths: {found}")

    print("\n=====================================\n")
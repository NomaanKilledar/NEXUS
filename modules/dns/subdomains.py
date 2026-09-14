import socket


COMMON_SUBDOMAINS = [
    "www",
    "mail",
    "ftp",
    "api",
    "dev",
    "test",
    "staging",
    "admin",
    "portal",
    "blog",
    "shop",
    "app",
    "vpn",
    "cdn",
    "status",
]


def resolve_subdomain(subdomain, domain):
    hostname = f"{subdomain}.{domain}"

    try:
        addresses = socket.gethostbyname_ex(hostname)[2]
        return hostname, addresses

    except (socket.gaierror, socket.herror):
        return None


def show_subdomain_enumerator():
    print("\n========== SUBDOMAIN ENUMERATOR ==========\n")

    domain = input("Domain: ").strip()

    if not domain:
        print("Domain cannot be empty.")
        return

    domain = domain.replace("https://", "")
    domain = domain.replace("http://", "")
    domain = domain.split("/")[0]

    print(f"\nChecking common subdomains for: {domain}")
    print("-" * 50)

    found = 0

    for subdomain in COMMON_SUBDOMAINS:
        result = resolve_subdomain(subdomain, domain)

        if result:
            hostname, addresses = result

            print(f"[+] {hostname}")
            for address in addresses:
                print(f"    IP: {address}")

            found += 1

    print("\n" + "-" * 50)

    if found:
        print(f"Found {found} resolving subdomain(s).")
    else:
        print("No common subdomains found.")

    print("\n==========================================\n")
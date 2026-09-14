from modules.reports.logger import log_event
import ipaddress
import requests


def lookup_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        return None

    try:
        response = requests.get(
            f"https://ipwho.is/{ip_address}",
            timeout=5
        )
        response.raise_for_status()

        data = response.json()

        if not data.get("success", False):
            return None

        connection = data.get("connection", {})

        return {
            "IP": data.get("ip", ip_address),
            "Country": data.get("country", "Unknown"),
            "Region": data.get("region", "Unknown"),
            "City": data.get("city", "Unknown"),
            "ISP": connection.get("isp", "Unknown"),
            "Organization": connection.get("org", "Unknown"),
            "ASN": connection.get("asn", "Unknown"),
        }

    except (requests.RequestException, ValueError):
        return None


def show_ip_lookup():
    print("\n========== IP LOOKUP ==========\n")

    ip_address = input("IP address: ").strip()
    log_event(f"IP Lookup | IP: {ip_address}")

    if not ip_address:
        print("IP address cannot be empty.")
        return

    print("\nLooking up...\n")

    result = lookup_ip(ip_address)

    if result is None:
        print("IP lookup failed or the IP address is invalid.")
        return

    print("--------------------------------")
    for key, value in result.items():
        print(f"{key:<15}: {value}")
    print("--------------------------------")

    print("\n================================\n")
from modules.reports.logger import log_event
import subprocess
import re


def get_arp_table():
    try:
        result = subprocess.run(
            ["arp", "-a"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            return []

        devices = []

        for line in result.stdout.splitlines():
            match = re.search(
                r"(\d+\.\d+\.\d+\.\d+)\s+"
                r"([0-9a-fA-F-]{17})\s+"
                r"(\w+)",
                line
            )

            if match:
                ip_address = match.group(1)
                mac_address = match.group(2)
                entry_type = match.group(3)

                devices.append({
                    "IP": ip_address,
                    "MAC": mac_address,
                    "Type": entry_type,
                })

        return devices

    except (subprocess.SubprocessError, OSError):
        return []


def show_arp_scanner():
    print("\n========== ARP SCANNER ==========\n")

    log_event("ARP Scanner | Local ARP table scan")

    print("Reading local ARP table...\n")

    devices = get_arp_table()

    if not devices:
        print("No ARP entries found.")
        print("Try communicating with devices on your local network first.")
        print("\n=================================\n")
        return

    print(f"{'IP Address':<18}{'MAC Address':<20}{'Type'}")
    print("-" * 55)

    for device in devices:
        print(
            f"{device['IP']:<18}"
            f"{device['MAC']:<20}"
            f"{device['Type']}"
        )

    print(f"\nDevices found: {len(devices)}")
    print("\n=================================\n")
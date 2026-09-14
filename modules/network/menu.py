from modules.network.info import show_network_info
from modules.network.ip_lookup import show_ip_lookup
from modules.network.arp_scanner import show_arp_scanner
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def network_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== NETWORK =========={Colors.RESET}")
        print("[1] Network Information")
        print("[2] IP Lookup")
        print("[3] ARP Scanner")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}NETWORK > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used Network Information")
            show_network_info()
            pause()

        elif choice == "2":
            log_event("Used IP Lookup")
            show_ip_lookup()
            pause()

        elif choice == "3":
            log_event("Used ARP Scanner")
            show_arp_scanner()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
from utils.banner import show_banner
from utils.colors import Colors
from utils.input import pause

from modules.network.menu import network_menu
from modules.dns.menu import dns_menu
from modules.web.menu import web_menu
from modules.ports.menu import ports_menu
from modules.hashing.menu import hashing_menu
from modules.integrity.menu import integrity_menu
from modules.system.menu import system_menu
from modules.reports.menu import reports_menu
from modules.reports.logger import log_event


def main_menu():
    while True:
        show_banner()

        print(f"{Colors.CYAN}")
        print("┌──────────────────────────────────────────┐")
        print("│              NEXUS MODULES               │")
        print("├──────────────────────────────────────────┤")
        print("│ [1] Network                              │")
        print("│ [2] DNS                                  │")
        print("│ [3] Web                                  │")
        print("│ [4] Ports & Services                     │")
        print("│ [5] Hashing                              │")
        print("│ [6] File Integrity                       │")
        print("│ [7] System                               │")
        print("│ [8] Reports                              │")
        print("│ [0] Exit                                 │")
        print("└──────────────────────────────────────────┘")
        print(Colors.RESET)

        choice = input(
            f"{Colors.GREEN}NEXUS > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Opened Network module")
            network_menu()

        elif choice == "2":
            log_event("Opened DNS module")
            dns_menu()

        elif choice == "3":
            log_event("Opened Web Security module")
            web_menu()

        elif choice == "4":
            log_event("Opened Ports & Services module")
            ports_menu()

        elif choice == "5":
            log_event("Opened Hashing module")
            hashing_menu()

        elif choice == "6":
            log_event("Opened File Integrity module")
            integrity_menu()

        elif choice == "7":
            log_event("Opened System module")
            system_menu()

        elif choice == "8":
            log_event("Opened Reports module")
            reports_menu()

        elif choice == "0":
            log_event("Exited NEXUS")
            print("Exiting NEXUS...")
            break

        else:
            print(f"\n{Colors.RED}Invalid option.{Colors.RESET}")
            pause()


if __name__ == "__main__":
    main_menu()
from modules.ports.tcp import show_tcp_scanner
from modules.ports.udp import show_udp_scanner
from modules.ports.banner import show_banner_grabber
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def ports_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== PORTS & SERVICES =========={Colors.RESET}")

        print("[1] TCP Port Scanner")
        print("[2] UDP Port Scanner")
        print("[3] Banner Grabber")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}PORTS > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used TCP Port Scanner")
            show_tcp_scanner()
            pause()

        elif choice == "2":
            log_event("Used UDP Port Scanner")
            show_udp_scanner()
            pause()

        elif choice == "3":
            log_event("Used Banner Grabber")
            show_banner_grabber()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
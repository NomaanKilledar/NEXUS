from modules.integrity.checksum import show_checksum_calculator
from modules.integrity.monitor import show_integrity_monitor
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def integrity_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== FILE INTEGRITY =========={Colors.RESET}")

        print("[1] File Checksum Calculator")
        print("[2] Integrity Monitor")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}INTEGRITY > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used File Checksum Calculator")
            show_checksum_calculator()
            pause()

        elif choice == "2":
            log_event("Used Integrity Monitor")
            show_integrity_monitor()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
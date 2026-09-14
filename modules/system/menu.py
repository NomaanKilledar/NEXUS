from modules.system.info import show_system_info
from modules.system.connections import show_active_connections
from modules.system.privileges import show_privilege_checker
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def system_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== SYSTEM =========={Colors.RESET}")

        print("[1] System Information")
        print("[2] Active Connections")
        print("[3] Privilege Checker")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}SYSTEM > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used System Information")
            show_system_info()
            pause()

        elif choice == "2":
            log_event("Used Active Connections")
            show_active_connections()
            pause()

        elif choice == "3":
            log_event("Used Privilege Checker")
            show_privilege_checker()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
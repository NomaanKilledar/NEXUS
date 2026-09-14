from modules.web.headers import show_header_analyzer
from modules.web.tls import show_tls_checker
from modules.web.paths import show_path_checker
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def web_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== WEB SECURITY =========={Colors.RESET}")

        print("[1] Security Header Analyzer")
        print("[2] SSL / TLS Checker")
        print("[3] Directory / Path Checker")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}WEB > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used Security Header Analyzer")
            show_header_analyzer()
            pause()

        elif choice == "2":
            log_event("Used SSL / TLS Checker")
            show_tls_checker()
            pause()

        elif choice == "3":
            log_event("Used Directory / Path Checker")
            show_path_checker()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
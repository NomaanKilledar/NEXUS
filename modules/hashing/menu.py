from modules.hashing.generator import show_hash_generator
from modules.hashing.identifier import show_hash_identifier
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def hashing_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== HASHING =========={Colors.RESET}")

        print("[1] Hash Generator")
        print("[2] Hash Identifier")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}HASHING > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used Hash Generator")
            show_hash_generator()
            pause()

        elif choice == "2":
            log_event("Used Hash Identifier")
            show_hash_identifier()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
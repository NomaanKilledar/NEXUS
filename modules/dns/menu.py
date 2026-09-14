from modules.dns.records import show_dns_records
from modules.dns.reverse import show_reverse_dns
from modules.dns.subdomains import show_subdomain_enumerator
from modules.reports.logger import log_event

from utils.colors import Colors
from utils.input import pause


def dns_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== DNS =========={Colors.RESET}")

        print("[1] DNS Record Finder")
        print("[2] Reverse DNS Lookup")
        print("[3] Subdomain Enumerator")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}DNS > {Colors.RESET}"
        ).strip()

        if choice == "1":
            log_event("Used DNS Record Finder")
            show_dns_records()
            pause()

        elif choice == "2":
            log_event("Used Reverse DNS Lookup")
            show_reverse_dns()
            pause()

        elif choice == "3":
            log_event("Used Subdomain Enumerator")
            show_subdomain_enumerator()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
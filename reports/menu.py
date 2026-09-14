from modules.reports.logger import show_session_logs
from utils.colors import Colors
from utils.input import pause


def reports_menu():
    while True:
        print("\033[2J\033[H", end="")

        print(f"{Colors.CYAN}========== REPORTS =========={Colors.RESET}")

        print("[1] Session Logs Viewer")
        print("[0] Back")

        choice = input(
            f"\n{Colors.GREEN}REPORTS > {Colors.RESET}"
        ).strip()

        if choice == "1":
            show_session_logs()
            pause()

        elif choice == "0":
            break

        else:
            print(f"{Colors.RED}Invalid option.{Colors.RESET}")
            pause()
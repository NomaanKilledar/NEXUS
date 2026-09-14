from utils.colors import Colors


def success(message):
    print(f"{Colors.GREEN}[+] {message}{Colors.RESET}")


def error(message):
    print(f"{Colors.RED}[!] {message}{Colors.RESET}")


def warning(message):
    print(f"{Colors.YELLOW}[*] {message}{Colors.RESET}")


def info(message):
    print(f"{Colors.CYAN}[i] {message}{Colors.RESET}")


def separator():
    print(f"{Colors.BLUE}" + "-" * 60 + f"{Colors.RESET}")


def title(message):
    separator()
    print(f"{Colors.CYAN}{message}{Colors.RESET}")
    separator()
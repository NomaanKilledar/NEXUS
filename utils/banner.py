from utils.colors import Colors


def show_banner():
    print("\033[2J\033[H", end="")

    print(f"""{Colors.CYAN}
███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
██║╚██╗██║██╔══╝   ██╔██╗ ╚██╗ ██╔╝╚════██║
██║ ╚████║███████╗██╔╝ ██╗ ╚████╔╝ ███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
{Colors.RESET}""")

    print(f"{Colors.WHITE}Network & Endpoint Security Utility Suite")
    print(f"{Colors.YELLOW}Authorized security testing and local analysis only.{Colors.RESET}")
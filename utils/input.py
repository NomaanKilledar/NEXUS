from utils.colors import Colors


def ask(prompt):
    return input(f"{Colors.GREEN}{prompt}{Colors.RESET}").strip()


def pause():
    input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")


def ask_int(prompt, minimum=None, maximum=None):
    while True:
        value = ask(prompt)

        try:
            number = int(value)
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number.{Colors.RESET}")
            continue

        if minimum is not None and number < minimum:
            print(f"{Colors.RED}Minimum value is {minimum}.{Colors.RESET}")
            continue

        if maximum is not None and number > maximum:
            print(f"{Colors.RED}Maximum value is {maximum}.{Colors.RESET}")
            continue

        return number
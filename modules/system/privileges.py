import ctypes
import getpass
import os
import platform

from modules.reports.logger import log_event


def is_admin():
    if platform.system() == "Windows":
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except (AttributeError, OSError):
            return False

    return os.geteuid() == 0


def show_privilege_checker():
    print("\n========== PRIVILEGE CHECKER ==========\n")

    username = getpass.getuser()
    admin = is_admin()

    log_event(
        f"Privilege Checker | User: {username} | "
        f"Administrator: {admin}"
    )

    print(f"Username       : {username}")
    print(f"Administrator  : {'YES' if admin else 'NO'}")

    if admin:
        print("\n[!] NEXUS is running with elevated privileges.")
    else:
        print("\n[+] NEXUS is running with standard privileges.")

    print("\n=======================================\n")
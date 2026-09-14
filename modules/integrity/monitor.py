import hashlib
import os

from modules.reports.logger import log_event


def calculate_sha256(filepath):
    hasher = hashlib.sha256()

    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(1024 * 1024)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()


def show_integrity_monitor():
    print("\n========== INTEGRITY MONITOR ==========\n")

    filepath = input("File path: ").strip().strip('"')

    if not filepath:
        print("File path cannot be empty.")
        return

    if not os.path.isfile(filepath):
        print("File does not exist.")
        return

    log_event(
        f"Integrity Monitor | File: {filepath}"
    )

    try:
        original_hash = calculate_sha256(filepath)

        print(f"File: {filepath}")
        print(f"SHA256: {original_hash}")

        print("\nMonitoring file...")
        print("Press Ctrl+C to stop.\n")

        while True:
            if not os.path.exists(filepath):
                print("[!] File no longer exists.")
                break

            current_hash = calculate_sha256(filepath)

            if current_hash != original_hash:
                print("\n[!] FILE CHANGED")
                print(f"Original SHA256: {original_hash}")
                print(f"Current SHA256 : {current_hash}")

                log_event(
                    f"Integrity Monitor | CHANGE DETECTED | "
                    f"File: {filepath}"
                )

                original_hash = current_hash

            else:
                print("[+] No change detected.")

            input("\nPress Enter to check again, or Ctrl+C to stop...")

    except KeyboardInterrupt:
        print("\n\nIntegrity monitoring stopped.")

    except OSError as exc:
        print(f"\nCould not monitor file: {exc}")

    print("\n=======================================\n")
import hashlib
import os

from modules.reports.logger import log_event


SUPPORTED_ALGORITHMS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha512",
}


def calculate_checksum(filepath, algorithm):
    hasher = hashlib.new(algorithm)

    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(1024 * 1024)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()


def show_checksum_calculator():
    print("\n========== FILE CHECKSUM CALCULATOR ==========\n")

    filepath = input("File path: ").strip().strip('"')

    if not filepath:
        print("File path cannot be empty.")
        return

    if not os.path.isfile(filepath):
        print("File does not exist.")
        return

    print("\n[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[4] SHA512")

    choice = input("\nAlgorithm > ").strip()

    if choice not in SUPPORTED_ALGORITHMS:
        print("Invalid algorithm.")
        return

    algorithm = SUPPORTED_ALGORITHMS[choice]

    log_event(
        f"File Checksum Calculator | File: {filepath} | "
        f"Algorithm: {algorithm}"
    )

    try:
        checksum = calculate_checksum(filepath, algorithm)

    except OSError as exc:
        print(f"\nCould not read file: {exc}")
        return

    print("\n----------------------------------------")
    print(f"File      : {filepath}")
    print(f"Algorithm : {algorithm.upper()}")
    print(f"Checksum  : {checksum}")
    print("----------------------------------------\n")
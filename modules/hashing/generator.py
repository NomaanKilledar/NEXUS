import hashlib

from modules.reports.logger import log_event


SUPPORTED_ALGORITHMS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha512",
}


def generate_hash(text, algorithm):
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()


def show_hash_generator():
    print("\n========== HASH GENERATOR ==========\n")

    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[4] SHA512")

    choice = input("\nAlgorithm > ").strip()

    if choice not in SUPPORTED_ALGORITHMS:
        print("Invalid algorithm.")
        return

    text = input("Text to hash: ")

    algorithm = SUPPORTED_ALGORITHMS[choice]

    log_event(
        f"Hash Generator | Algorithm: {algorithm}"
    )

    result = generate_hash(text, algorithm)

    print("\n----------------------------------------")
    print(f"Algorithm : {algorithm.upper()}")
    print(f"Hash      : {result}")
    print("----------------------------------------\n")
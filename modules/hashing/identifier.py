from modules.reports.logger import log_event


HASH_LENGTHS = {
    32: "MD5",
    40: "SHA1",
    64: "SHA256",
    128: "SHA512",
}


def identify_hash(hash_value):
    hash_value = hash_value.strip()

    if not hash_value:
        return []

    if not all(character in "0123456789abcdefABCDEF" for character in hash_value):
        return []

    algorithm = HASH_LENGTHS.get(len(hash_value))

    if algorithm:
        return [algorithm]

    return []


def show_hash_identifier():
    print("\n========== HASH IDENTIFIER ==========\n")

    hash_value = input("Hash: ").strip()

    if not hash_value:
        print("Hash cannot be empty.")
        return

    log_event(
        f"Hash Identifier | Length: {len(hash_value)}"
    )

    matches = identify_hash(hash_value)

    if matches:
        print("\nPossible hash type(s):")

        for algorithm in matches:
            print(f"[+] {algorithm}")

    else:
        print("\n[-] Could not identify the hash.")

    print("\n=====================================\n")
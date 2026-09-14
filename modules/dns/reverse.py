import socket


def reverse_dns_lookup(ip_address):
    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip_address)

        return {
            "Hostname": hostname,
            "Aliases": aliases,
            "Addresses": addresses,
        }

    except (socket.herror, socket.gaierror):
        return None


def show_reverse_dns():
    print("\n========== REVERSE DNS LOOKUP ==========\n")

    ip_address = input("IP address: ").strip()

    if not ip_address:
        print("IP address cannot be empty.")
        return

    try:
        socket.inet_aton(ip_address)
    except socket.error:
        print("Invalid IPv4 address.")
        return

    print("\nLooking up...\n")

    result = reverse_dns_lookup(ip_address)

    if result is None:
        print("No reverse DNS hostname found.")
    else:
        print(f"Hostname : {result['Hostname']}")

        if result["Aliases"]:
            print(f"Aliases  : {', '.join(result['Aliases'])}")
        else:
            print("Aliases  : None")

        if result["Addresses"]:
            print(f"Addresses: {', '.join(result['Addresses'])}")

    print("\n========================================\n")
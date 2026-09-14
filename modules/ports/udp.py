import socket

from modules.reports.logger import log_event


def scan_udp_port(host, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)

    try:
        sock.sendto(b"", (host, port))

        try:
            data, _ = sock.recvfrom(1024)
            return "OPEN"

        except socket.timeout:
            return "OPEN|FILTERED"

    except socket.error:
        return "CLOSED"

    finally:
        sock.close()


def show_udp_scanner():
    print("\n========== UDP PORT SCANNER ==========\n")

    host = input("Target host/IP: ").strip()

    if not host:
        print("Target cannot be empty.")
        return

    try:
        start_port = int(input("Start port: ").strip())
        end_port = int(input("End port: ").strip())
    except ValueError:
        print("Ports must be valid numbers.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range.")
        return

    log_event(
        f"UDP Port Scanner | Target: {host} | "
        f"Ports: {start_port}-{end_port}"
    )

    print(f"\nScanning {host}:{start_port}-{end_port}")
    print("-" * 55)

    interesting_ports = []

    for port in range(start_port, end_port + 1):
        result = scan_udp_port(host, port)

        if result == "OPEN":
            print(f"[+] Port {port:<5} OPEN")
            interesting_ports.append(port)

        elif result == "OPEN|FILTERED":
            print(f"[?] Port {port:<5} OPEN/FILTERED")
            interesting_ports.append(port)

    print("\n" + "-" * 55)
    print(f"Interesting UDP ports: {len(interesting_ports)}")

    print("\n=====================================\n")
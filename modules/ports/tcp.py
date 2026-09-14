import socket

from modules.reports.logger import log_event


def scan_tcp_port(host, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((host, port))
        return result == 0

    except socket.error:
        return False

    finally:
        sock.close()


def show_tcp_scanner():
    print("\n========== TCP PORT SCANNER ==========\n")

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
        f"TCP Port Scanner | Target: {host} | "
        f"Ports: {start_port}-{end_port}"
    )

    print(f"\nScanning {host}:{start_port}-{end_port}")
    print("-" * 55)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_tcp_port(host, port):
            print(f"[+] Port {port:<5} OPEN")
            open_ports.append(port)

    print("\n" + "-" * 55)
    print(f"Open TCP ports: {len(open_ports)}")

    print("\n=====================================\n")
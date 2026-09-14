import socket

from modules.reports.logger import log_event


def grab_banner(host, port, timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))

        try:
            sock.sendall(b"\r\n")
        except socket.error:
            pass

        data = sock.recv(1024)

        if not data:
            return "No banner received."

        return data.decode("utf-8", errors="replace").strip()

    except socket.timeout:
        return "Connection timed out."

    except socket.error as exc:
        return f"Connection failed: {exc}"

    finally:
        sock.close()


def show_banner_grabber():
    print("\n========== BANNER GRABBER ==========\n")

    host = input("Target host/IP: ").strip()

    if not host:
        print("Target cannot be empty.")
        return

    try:
        port = int(input("Port: ").strip())
    except ValueError:
        print("Port must be a valid number.")
        return

    if port < 1 or port > 65535:
        print("Invalid port.")
        return

    log_event(
        f"Banner Grabber | Target: {host} | Port: {port}"
    )

    print(f"\nConnecting to {host}:{port}")
    print("-" * 55)

    banner = grab_banner(host, port)

    print(f"Banner: {banner}")

    print("\n===================================\n")
from modules.reports.logger import log_event
import socket
import platform


def get_network_info():
    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        local_ip = "Unavailable"

    try:
        fqdn = socket.getfqdn()
    except socket.gaierror:
        fqdn = "Unavailable"

    return {
        "Hostname": hostname,
        "FQDN": fqdn,
        "Local IP": local_ip,
        "Platform": platform.system(),
    }


def show_network_info():
    print("\n========== NETWORK INFORMATION ==========\n")

    log_event("Network Information | Local system network details")

    info = get_network_info()

    for key, value in info.items():
        print(f"{key:<15}: {value}")

    print("\n==========================================\n")
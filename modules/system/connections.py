import psutil

from modules.reports.logger import log_event


def show_active_connections():
    print("\n========== ACTIVE CONNECTIONS ==========\n")

    log_event("Active Connections | Local network connections")

    try:
        connections = psutil.net_connections(kind="inet")
    except psutil.Error as exc:
        print(f"Could not retrieve connections: {exc}")
        return

    if not connections:
        print("No active network connections found.")
        print("\n========================================\n")
        return

    print(
        f"{'PROTO':<7}"
        f"{'LOCAL ADDRESS':<24}"
        f"{'REMOTE ADDRESS':<24}"
        f"{'STATUS':<15}"
        f"{'PID':<8}"
    )

    print("-" * 80)

    for connection in connections:
        protocol = "TCP" if connection.type == 1 else "UDP"

        local = (
            f"{connection.laddr.ip}:{connection.laddr.port}"
            if connection.laddr
            else "-"
        )

        remote = (
            f"{connection.raddr.ip}:{connection.raddr.port}"
            if connection.raddr
            else "-"
        )

        status = connection.status or "-"

        pid = str(connection.pid) if connection.pid else "-"

        print(
            f"{protocol:<7}"
            f"{local:<24}"
            f"{remote:<24}"
            f"{status:<15}"
            f"{pid:<8}"
        )

    print("\n========================================\n")
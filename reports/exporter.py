import json
import os

from modules.reports.logger import read_session_logs


REPORTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "reports")
)


def export_report():
    print("\n========== REPORT EXPORT ==========\n")

    logs = read_session_logs()

    if logs == "No session logs found.":
        print("No session logs available to export.")
        print("\n===================================\n")
        return

    print("[1] Export as TXT")
    print("[2] Export as JSON")
    print("[3] Export as Markdown")
    print("[0] Back")

    choice = input("\nFormat > ").strip()

    os.makedirs(REPORTS_DIR, exist_ok=True)

    if choice == "1":
        filepath = os.path.join(REPORTS_DIR, "nexus_report.txt")

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(logs)

    elif choice == "2":
        filepath = os.path.join(REPORTS_DIR, "nexus_report.json")

        entries = [
            line for line in logs.splitlines()
            if line.strip()
        ]

        data = {
            "tool": "NEXUS",
            "report_type": "session_logs",
            "entries": entries,
        }

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    elif choice == "3":
        filepath = os.path.join(REPORTS_DIR, "nexus_report.md")

        with open(filepath, "w", encoding="utf-8") as file:
            file.write("# NEXUS Session Report\n\n")

            for line in logs.splitlines():
                if line.strip():
                    file.write(f"- {line}\n")

    elif choice == "0":
        return

    else:
        print("Invalid option.")
        return

    print(f"\n[+] Report exported successfully:")
    print(filepath)

    print("\n===================================\n")
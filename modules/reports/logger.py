import os
from datetime import datetime


REPORTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "reports")
)

LOG_FILE = os.path.join(REPORTS_DIR, "nexus_session.log")


def ensure_reports_directory():
    os.makedirs(REPORTS_DIR, exist_ok=True)


def log_event(message):
    ensure_reports_directory()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def read_session_logs():
    ensure_reports_directory()

    if not os.path.exists(LOG_FILE):
        return "No session logs found."

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    return content if content else "No session logs found."


def show_session_logs():
    print("\n========== SESSION LOGS ==========\n")

    logs = read_session_logs()

    print(logs)

    print("\n==================================\n")
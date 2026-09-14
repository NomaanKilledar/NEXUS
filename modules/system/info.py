import os
import platform
import socket
import psutil

from modules.reports.logger import log_event


def show_system_info():
    print("\n========== SYSTEM INFORMATION ==========\n")

    log_event("System Information | Local system details")

    print(f"OS              : {platform.system()}")
    print(f"OS Version      : {platform.version()}")
    print(f"Architecture    : {platform.machine()}")
    print(f"Hostname        : {socket.gethostname()}")
    print(f"Processor       : {platform.processor()}")
    print(f"Python Version  : {platform.python_version()}")

    print("\nCPU")
    print("-" * 40)
    print(f"Physical Cores  : {psutil.cpu_count(logical=False)}")
    print(f"Logical Cores   : {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage       : {psutil.cpu_percent(interval=1)}%")

    memory = psutil.virtual_memory()

    print("\nMemory")
    print("-" * 40)
    print(f"Total           : {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available       : {memory.available / (1024 ** 3):.2f} GB")
    print(f"Usage           : {memory.percent}%")

    disk = psutil.disk_usage(os.path.abspath(os.sep))

    print("\nDisk")
    print("-" * 40)
    print(f"Total           : {disk.total / (1024 ** 3):.2f} GB")
    print(f"Free            : {disk.free / (1024 ** 3):.2f} GB")
    print(f"Usage           : {disk.percent}%")

    print("\n========================================\n")
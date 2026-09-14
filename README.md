# NEXUS

### Network & Endpoint Security Utility Suite

NEXUS is a Python-based interactive CLI toolkit for **authorized security testing, system inspection, and local security analysis**.

It provides a single terminal interface for working with network information, DNS records, web security checks, ports and services, hashing, file integrity, system information, and session reports.

> **Authorized security testing and local analysis only.**
>
> Only use NEXUS on systems, networks, files, and domains that you own or have explicit permission to test.

---

## Features

### Network

* Local network information
* IP lookup
* Local ARP scanning
* Network analysis utilities

### DNS

* DNS record lookup
* Reverse DNS lookup
* Subdomain analysis

### Web

* HTTP security header analysis
* SSL/TLS inspection
* Common path availability checker

### Ports & Services

* TCP port scanning
* UDP port scanning
* Basic service/banner inspection

### Hashing

* MD5 generation
* SHA1 generation
* SHA256 generation
* SHA512 generation
* Basic hash identification

### File Integrity

* File checksum calculation
* SHA256 integrity monitoring
* File change detection

### System

* System information
* Active network connections
* Privilege/admin status

### Reports

* Session activity logging
* Session log viewer
* TXT report export
* JSON report export
* Markdown report export

---

## Project Structure

```text
NEXUS/
├── main.py
├── config.json
├── requirements.txt
├── README.md
│
├── modules/
│   ├── network/
│   ├── dns/
│   ├── web/
│   ├── ports/
│   ├── hashing/
│   ├── integrity/
│   ├── system/
│   └── reports/
│
├── utils/
│   ├── banner.py
│   ├── colors.py
│   ├── input.py
│   └── output.py
│
├── reports/
└── tests/
```

---

## Requirements

* Python 3.10+
* Windows, Linux, or macOS
* Internet connection for features that query external hosts/domains
* Appropriate permissions for certain local system/network operations

Dependencies:

```text
dnspython
requests
psutil
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/NomaanKilledar/NEXUS.git
cd NEXUS
```

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

---

## Running NEXUS

Start the application with:

```bash
python main.py
```

The main menu provides:

```text
[1] Network
[2] DNS
[3] Web
[4] Ports & Services
[5] Hashing
[6] File Integrity
[7] System
[8] Reports
[0] Exit
```

---

## Logging & Reports

NEXUS records session activity in:

```text
reports/nexus_session.log
```

Generated report files are stored in the same `reports/` directory.

Runtime reports and logs are excluded from Git using `.gitignore`.

---

## Security & Responsible Use

NEXUS is designed for legitimate security analysis and learning.

Do not use it to:

* Scan systems without authorization
* Access networks you do not own or have permission to test
* Attempt unauthorized access
* Collect information from private systems without permission
* Disrupt or damage systems or services

For testing, use your own computer, lab environment, or systems where you have explicit authorization.

---

## Development

The project is structured into independent modules so new security-analysis features can be added without changing the entire application.

Compile-check the project:

```bash
python -m compileall -q .
```

Run the application:

```bash
python main.py
```

---

## License

This project is currently provided for educational and authorized security-analysis purposes.

A formal open-source license can be added later if required.

---

## Author

**Nomaan Killedar**

GitHub:
https://github.com/NomaanKilledar

Project:
https://github.com/NomaanKilledar/NEXUS

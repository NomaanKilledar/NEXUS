import socket
import ssl

from modules.reports.logger import log_event


def check_tls(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port), timeout=5) as sock:
        with context.wrap_socket(
            sock,
            server_hostname=hostname
        ) as tls_sock:

            certificate = tls_sock.getpeercert()

            issuer = dict(
                x[0] for x in certificate.get("issuer", [])
            )

            subject = dict(
                x[0] for x in certificate.get("subject", [])
            )

            not_before = certificate.get("notBefore")
            not_after = certificate.get("notAfter")

            return {
                "Hostname": hostname,
                "TLS Version": tls_sock.version(),
                "Cipher": tls_sock.cipher()[0],
                "Certificate Subject": subject.get(
                    "commonName",
                    "Unknown"
                ),
                "Certificate Issuer": issuer.get(
                    "commonName",
                    "Unknown"
                ),
                "Valid From": not_before or "Unknown",
                "Valid Until": not_after or "Unknown",
            }


def show_tls_checker():
    print("\n========== SSL / TLS CHECKER ==========\n")

    hostname = input("Hostname: ").strip()

    if hostname.startswith("https://"):
        hostname = hostname[8:]

    elif hostname.startswith("http://"):
        hostname = hostname[7:]

    hostname = hostname.split("/")[0].split(":")[0]

    if not hostname:
        print("Hostname cannot be empty.")
        return

    log_event(
        f"SSL/TLS Checker | Hostname: {hostname}"
    )

    try:
        result = check_tls(hostname)

        for key, value in result.items():
            print(f"{key:<22}: {value}")

    except socket.gaierror:
        print("\nCould not resolve hostname.")

    except ssl.SSLCertVerificationError:
        print("\nTLS certificate verification failed.")

    except (socket.timeout, TimeoutError):
        print("\nConnection timed out.")

    except OSError as exc:
        print(f"\nTLS connection failed: {exc}")

    print("\n=======================================\n")
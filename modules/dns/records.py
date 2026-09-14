import dns.resolver


RECORD_TYPES = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
    "SOA",
]


def lookup_records(domain, record_type):
    record_type = record_type.upper()

    if record_type not in RECORD_TYPES:
        raise ValueError("Unsupported DNS record type.")

    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 5

    answers = resolver.resolve(domain, record_type)

    return [str(answer) for answer in answers]


def show_dns_records():
    print("\n========== DNS RECORD FINDER ==========\n")

    domain = input("Domain: ").strip()

    if not domain:
        print("Domain cannot be empty.")
        return

    print("\nAvailable record types:")
    print(", ".join(RECORD_TYPES))

    record_type = input("\nRecord type: ").strip().upper()

    try:
        records = lookup_records(domain, record_type)

        print(f"\n{record_type} records for {domain}:")
        print("-" * 50)

        for record in records:
            print(record)

    except dns.resolver.NXDOMAIN:
        print("\nDomain does not exist.")

    except dns.resolver.NoAnswer:
        print(f"\nNo {record_type} record found.")

    except dns.resolver.NoNameservers:
        print("\nNo usable DNS nameserver was found.")

    except dns.exception.Timeout:
        print("\nDNS request timed out.")

    except Exception as exc:
        print(f"\nDNS lookup failed: {exc}")

    print("\n=======================================\n")
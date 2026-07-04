import dns.resolver


def enumerate_dns(domain):

    dns_results = {}

    record_types = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME"
    ]

    for record in record_types:

        dns_results[record] = []

        try:

            answers = dns.resolver.resolve(
                domain,
                record
            )

            for answer in answers:

                dns_results[record].append(
                    str(answer)
                )

        except Exception:
            pass

    return dns_results

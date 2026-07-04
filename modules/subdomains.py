import socket

from config import COMMON_SUBDOMAINS


def enumerate_subdomains(domain):

    results = []

    for sub in COMMON_SUBDOMAINS:

        hostname = f"{sub}.{domain}"

        try:

            ip = socket.gethostbyname(hostname)

            results.append({

                "subdomain": hostname,

                "ip": ip

            })

        except socket.gaierror:

            continue

    return results
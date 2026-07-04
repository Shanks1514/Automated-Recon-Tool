import socket
from urllib.parse import urlparse


def validate_url(target):

    target = target.strip()

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    return target


def extract_domain(url):

    parsed = urlparse(url)

    return parsed.netloc


def resolve_ip(domain):

    try:
        return socket.gethostbyname(domain)

    except socket.gaierror:
        return None


def print_banner():

    print("=" * 70)
    print("        Automated Recon Tool")
    print("=" * 70)

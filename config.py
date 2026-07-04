"""
Configuration file for Automated Recon Tool
"""

# Common ports for scanning
COMMON_PORTS = [
    21,
    22,
    25,
    53,
    80,
    110,
    143,
    443,
    445,
    3306,
    3389,
    5432,
    8080,
    8443
]

# Common subdomains
COMMON_SUBDOMAINS = [
    "www",
    "mail",
    "ftp",
    "api",
    "dev",
    "test",
    "admin",
    "staging",
    "blog",
    "cdn",
    "vpn"
]

# DNS Record Types
DNS_RECORDS = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME"
]

# Request timeout
REQUEST_TIMEOUT = 5

# Socket timeout
SOCKET_TIMEOUT = 2

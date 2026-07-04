import ssl
import socket
from datetime import datetime


def analyze_ssl(domain):

    ssl_info = {}

    try:

        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

                ssl_info["subject"] = dict(
                    x[0] for x in cert["subject"]
                )

                ssl_info["issuer"] = dict(
                    x[0] for x in cert["issuer"]
                )

                ssl_info["version"] = ssock.version()

                ssl_info["serial"] = cert.get(
                    "serialNumber",
                    "Unknown"
                )

                ssl_info["valid_from"] = cert["notBefore"]

                ssl_info["valid_until"] = cert["notAfter"]

                expiry = datetime.strptime(
                    cert["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                remaining = (
                    expiry - datetime.utcnow()
                ).days

                ssl_info["days_remaining"] = remaining

                ssl_info["status"] = (
                    "Valid"
                    if remaining > 0
                    else "Expired"
                )

    except Exception as e:

        ssl_info["error"] = str(e)

    return ssl_info
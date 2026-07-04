import socket

from config import (
    COMMON_PORTS,
    SOCKET_TIMEOUT
)


def scan_ports(ip):

    results = []

    for port in COMMON_PORTS:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(SOCKET_TIMEOUT)

        try:

            result = sock.connect_ex(
                (ip, port)
            )

            if result == 0:

                try:

                    service = socket.getservbyport(
                        port
                    )

                except:

                    service = "Unknown"

                results.append({

                    "port": port,

                    "service": service

                })

        finally:

            sock.close()

    return results
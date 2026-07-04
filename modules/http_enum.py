import time
import requests

from config import REQUEST_TIMEOUT


def http_information(target):

    info = {}

    try:

        start = time.time()

        response = requests.get(
            target,
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True,
            verify=True
        )

        elapsed = time.time() - start

        info["response"] = response
        info["status"] = response.status_code
        info["server"] = response.headers.get(
            "Server",
            "Unknown"
        )
        info["cookies"] = len(response.cookies)
        info["headers"] = dict(response.headers)
        info["url"] = response.url
        info["redirects"] = len(response.history)
        info["time"] = round(elapsed, 3)

    except Exception as e:

        info["error"] = str(e)

    return info
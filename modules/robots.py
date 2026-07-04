import requests

from config import REQUEST_TIMEOUT


def analyze_robots(target):

    robots_info = {}

    robots_url = target.rstrip("/") + "/robots.txt"

    try:

        response = requests.get(
            robots_url,
            timeout=REQUEST_TIMEOUT
        )

        robots_info["url"] = robots_url
        robots_info["status"] = response.status_code

        if response.status_code == 200:

            disallow = []
            allow = []
            sitemaps = []

            for line in response.text.splitlines():

                line = line.strip()

                if line.lower().startswith("disallow:"):
                    disallow.append(
                        line.split(":", 1)[1].strip()
                    )

                elif line.lower().startswith("allow:"):
                    allow.append(
                        line.split(":", 1)[1].strip()
                    )

                elif line.lower().startswith("sitemap:"):
                    sitemaps.append(
                        line.split(":", 1)[1].strip()
                    )

            robots_info["disallow"] = disallow
            robots_info["allow"] = allow
            robots_info["sitemaps"] = sitemaps

        else:

            robots_info["error"] = "robots.txt not found"

    except Exception as e:

        robots_info["error"] = str(e)

    return robots_info
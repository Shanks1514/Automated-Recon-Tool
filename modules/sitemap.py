import requests
import xml.etree.ElementTree as ET

from config import REQUEST_TIMEOUT


def analyze_sitemap(target):

    sitemap_info = {}

    sitemap_url = target.rstrip("/") + "/sitemap.xml"

    try:

        response = requests.get(
            sitemap_url,
            timeout=REQUEST_TIMEOUT
        )

        sitemap_info["url"] = sitemap_url
        sitemap_info["status"] = response.status_code

        if response.status_code == 200:

            urls = []

            root = ET.fromstring(response.content)

            namespace = {
                "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
            }

            for loc in root.findall(".//sm:loc", namespace):

                urls.append(loc.text)

            sitemap_info["urls"] = urls

        else:

            sitemap_info["error"] = "sitemap.xml not found"

    except Exception as e:

        sitemap_info["error"] = str(e)

    return sitemap_info
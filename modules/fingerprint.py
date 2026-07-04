from bs4 import BeautifulSoup


def detect_technologies(response):

    technologies = []

    headers = response.headers
    html = response.text.lower()

    server = headers.get("Server", "").lower()

    if "apache" in server:
        technologies.append("Apache")

    if "nginx" in server:
        technologies.append("Nginx")

    if "iis" in server:
        technologies.append("Microsoft IIS")

    if "litespeed" in server:
        technologies.append("LiteSpeed")

    if "cloudflare" in server:
        technologies.append("Cloudflare")

    powered = headers.get("X-Powered-By", "").lower()

    if "php" in powered:
        technologies.append("PHP")

    if "asp.net" in powered:
        technologies.append("ASP.NET")

    soup = BeautifulSoup(response.text, "html.parser")

    generator = soup.find("meta", attrs={"name": "generator"})

    if generator:

        content = generator.get("content", "").lower()

        if "wordpress" in content:
            technologies.append("WordPress")

        if "joomla" in content:
            technologies.append("Joomla")

        if "drupal" in content:
            technologies.append("Drupal")

    checks = {

        "wp-content": "WordPress",
        "django": "Django",
        "flask": "Flask",
        "laravel": "Laravel",
        "react": "React",
        "vue": "Vue.js",
        "bootstrap": "Bootstrap",
        "express": "Express.js"

    }

    for keyword, tech in checks.items():

        if keyword in html and tech not in technologies:

            technologies.append(tech)

    return sorted(technologies)
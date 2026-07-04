SECURITY_HEADERS = {

    "Content-Security-Policy":
        "Prevents XSS attacks",

    "Strict-Transport-Security":
        "Forces HTTPS",

    "X-Frame-Options":
        "Prevents Clickjacking",

    "X-Content-Type-Options":
        "Prevents MIME Sniffing",

    "Referrer-Policy":
        "Protects Referrer Information",

    "Permissions-Policy":
        "Restricts Browser Features",

    "Cross-Origin-Opener-Policy":
        "Isolation Protection",

    "Cross-Origin-Resource-Policy":
        "Cross-Origin Protection"

}


def analyze_headers(response):

    results = {

        "present": [],

        "missing": []

    }

    headers = response.headers

    for header, purpose in SECURITY_HEADERS.items():

        if header in headers:

            results["present"].append(

                (header, headers[header])

            )

        else:

            results["missing"].append(

                (header, purpose)

            )

    return results
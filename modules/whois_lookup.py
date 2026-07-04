import whois


def get_whois(domain):

    whois_data = {}

    try:

        w = whois.whois(domain)

        whois_data["Registrar"] = w.registrar

        whois_data["Creation Date"] = str(w.creation_date)

        whois_data["Expiration Date"] = str(w.expiration_date)

        whois_data["Organization"] = w.org

        whois_data["Country"] = w.country

        whois_data["Name Servers"] = w.name_servers

    except Exception as e:

        whois_data["Error"] = str(e)

    return whois_data

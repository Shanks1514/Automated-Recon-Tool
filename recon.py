from modules.utils import (
    validate_url,
    extract_domain,
    resolve_ip,
    print_banner
)
import time
from modules.dns_lookup import enumerate_dns

from modules.whois_lookup import get_whois
from modules.ports import scan_ports
from modules.http_enum import http_information
from modules.fingerprint import detect_technologies
from modules.headers import analyze_headers
from modules.robots import analyze_robots
from modules.sitemap import analyze_sitemap
from modules.sslcheck import analyze_ssl
from modules.subdomains import enumerate_subdomains
from modules.report import (
    generate_json,
    generate_html
)
from modules.logger import log
def main():
    start_time = time.time()
    print_banner()

    target = input("\nEnter Target URL: ").strip()

    target = validate_url(target)

    domain = extract_domain(target)

    ip = resolve_ip(domain)
    log(f"Started scan for {target}")
    report = {}

    report["target"] = target
    report["domain"] = domain
    report["ip"] = ip
    print("\nTarget Information")
    print("-" * 40)

    print(f"Target URL : {target}")
    print(f"Domain     : {domain}")
    print(f"IP Address : {ip}")

    print("\nDNS Enumeration")
    print("-" * 40)

    dns_records = enumerate_dns(domain)
    report["dns"] = dns_records

    log("DNS Enumeration completed")
    for record_type, records in dns_records.items():

        print(f"\n{record_type} Records")

        if records:

            for record in records:

                print(f"  {record}")

        else:

            print("  None Found")


    # ----------------------------
    # WHOIS Section
    # ----------------------------

    print("\nWHOIS Information")
    print("-" * 40)

    whois_info = get_whois(domain)
    whois_info = get_whois(domain)
    report["whois"] = whois_info

    log("WHOIS Lookup completed")
    for key, value in whois_info.items():

        print(f"{key}: {value}")

    print("\nPort Scan")
    print("-" * 40)
    print(f"Domain: {domain}")
    print(f"IP: {ip}")
    open_ports = scan_ports(ip)
    report["ports"] = open_ports

    log("Port Scan completed")
    if open_ports:

        for port in open_ports:

            print(
                f"{port['port']}/tcp\tOPEN\t{port['service']}"
            )

    else:

        print("No common open ports detected.")

    print("\nHTTP Enumeration")
    print("-" * 40)

    http_info = http_information(target)
    report["http"] = http_info

    log("HTTP Enumeration completed")
    if "error" in http_info:

        print(http_info["error"])

    else:

        print(f"Final URL      : {http_info['url']}")
        print(f"Status Code    : {http_info['status']}")
        print(f"Server         : {http_info['server']}")
        print(f"Response Time  : {http_info['time']} sec")
        print(f"Redirects      : {http_info['redirects']}")
        print(f"Cookies        : {http_info['cookies']}")
        

    print("\nTechnology Fingerprinting")
    print("-" * 40)

    if "response" in http_info:

        technologies = detect_technologies(
            http_info["response"]
        )
        report["technologies"] = technologies

        log("Technology Fingerprinting completed")  
        if technologies:

            for tech in technologies:

                print(f"Detected: {tech}")

        else:

            print("No technologies identified.")

    print("\nSecurity Header Analysis")
    print("-" * 40)

    header_results = analyze_headers(
        http_info["response"]
    )
    report["headers"] = header_results

    log("Security Header Analysis completed")
    print("\nPresent Headers")

    if header_results["present"]:

        for header, value in header_results["present"]:

            print(f"✔ {header}")

    else:

        print("None")


    print("\nMissing Headers")

    if header_results["missing"]:

        for header, purpose in header_results["missing"]:

            print(f"✖ {header}")
            print(f"   Purpose: {purpose}")

    else:

        print("No missing security headers.")
    total = len(header_results["present"]) + len(header_results["missing"])

    score = int(
        (len(header_results["present"]) / total) * 100
    )

    print("\nSecurity Score")
    print("-" * 40)

    print(f"{score}/100")

    print("\nrobots.txt Analysis")
    print("-" * 40)

    robots = analyze_robots(target)
    report["robots"] = robots

    log("robots.txt Analysis completed")
    if "error" in robots:

        print(robots["error"])

    else:

        print(f"URL: {robots['url']}")
        print(f"Status Code: {robots['status']}")

        print("\nDisallow Entries:")

        if robots["disallow"]:

            for entry in robots["disallow"]:

                print(f"  {entry}")

        else:

            print("  None")

        print("\nAllow Entries:")

        if robots["allow"]:

            for entry in robots["allow"]:

                print(f"  {entry}")

        else:

            print("  None")

        print("\nSitemaps:")

        if robots["sitemaps"]:

            for sitemap in robots["sitemaps"]:

                print(f"  {sitemap}")

        else:

            print("  None")

    print("\nSitemap Analysis")
    print("-" * 40)

    sitemap = analyze_sitemap(target)
    report["sitemap"] = sitemap

    log("Sitemap Analysis completed")
    if "error" in sitemap:

        print(sitemap["error"])

    else:

        print(f"URL: {sitemap['url']}")
        print(f"Status Code: {sitemap['status']}")

        print(f"\nURLs Found: {len(sitemap['urls'])}")

        for url in sitemap["urls"][:10]:

            print(f"  {url}")

        if len(sitemap["urls"]) > 10:

            print(f"...and {len(sitemap['urls'])-10} more URLs")

    print("\nSSL/TLS Analysis")
    print("-" * 40)

    ssl_data = analyze_ssl(domain)
    report["ssl"] = ssl_data

    log("SSL Analysis completed")
    if "error" in ssl_data:

        print(ssl_data["error"])

    else:

        print(f"Version          : {ssl_data['version']}")
        print(f"Subject          : {ssl_data['subject']}")
        print(f"Issuer           : {ssl_data['issuer']}")
        print(f"Serial Number    : {ssl_data['serial']}")
        print(f"Valid From       : {ssl_data['valid_from']}")
        print(f"Valid Until      : {ssl_data['valid_until']}")
        print(f"Days Remaining   : {ssl_data['days_remaining']}")
        print(f"Certificate      : {ssl_data['status']}")

    print("\nSubdomain Enumeration")
    print("-" * 40)

    subdomains = enumerate_subdomains(domain)
    report["subdomains"] = subdomains
    log("Subdomain Enumeration completed")
    if subdomains:

        for sub in subdomains:

            print(
                f"{sub['subdomain']}  -->  {sub['ip']}"
            )

    else:

        print("No common subdomains found.")
    duration = round(
    time.time() - start_time,
    2
)
    print("\nGenerating Reports...")
    print("-" * 40)

    json_report = generate_json(report)

    html_report = generate_html(report)
    log("Reports generated successfully")
    print("\n" + "=" * 60)
    print("SCAN COMPLETED")
    print("=" * 60)

    print(f"Target              : {target}")
    print(f"IP Address          : {ip}")

    print()

    print(f"Technologies Found  : {len(technologies)}")
    print(f"Open Ports          : {len(open_ports)}")
    print(f"Subdomains Found    : {len(subdomains)}")

    print()

    print(f"Headers Present     : {len(header_results['present'])}")
    print(f"Headers Missing     : {len(header_results['missing'])}")

    print()

    print(f"robots.txt          : {'Found' if 'error' not in robots else 'Not Found'}")
    print(f"sitemap.xml         : {'Found' if 'error' not in sitemap else 'Not Found'}")

    print()

    print(f"Scan Duration       : {duration} seconds")

    print()

    print("Reports")

    print(f"JSON : {json_report}")
    print(f"HTML : {html_report}")

    print("=" * 60)
if __name__ == "__main__":
    main()
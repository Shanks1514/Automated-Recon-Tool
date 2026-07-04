import json
import os
from datetime import datetime


def generate_json(report):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/report.json"

    report_copy = report.copy()

    # Remove response object (not JSON serializable)
    if "http" in report_copy:

        report_copy["http"] = report_copy["http"].copy()

        report_copy["http"].pop("response", None)

    report_copy["generated"] = str(datetime.now())

    with open(filename, "w") as file:

        json.dump(
            report_copy,
            file,
            indent=4,
            default=str
        )

    return filename


def generate_html(report):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/report.html"

    html = f"""

<!DOCTYPE html>

<html>

<head>

<title>Recon Report</title>

<style>

body {{
    font-family: Arial;
    background: #f4f4f4;
    padding:40px;
}}

table {{
    border-collapse: collapse;
    width:100%;
    margin-bottom:30px;
}}

th,td {{
    border:1px solid #ccc;
    padding:10px;
}}

th {{
    background:#222;
    color:white;
}}

h1 {{
    color:#333;
}}

</style>

</head>

<body>

<h1>Automated Recon Tool Report</h1>

<p><strong>Generated:</strong> {datetime.now()}</p>

<table>

<tr>
<th>Target</th>
<td>{report['target']}</td>
</tr>

<tr>
<th>Domain</th>
<td>{report['domain']}</td>
</tr>

<tr>
<th>IP Address</th>
<td>{report['ip']}</td>
</tr>

</table>

<h2>Technologies</h2>

<ul>

"""

    for tech in report.get("technologies", []):

        html += f"<li>{tech}</li>"

    html += "</ul>"

    html += """

<h2>Open Ports</h2>

<table>

<tr>

<th>Port</th>

<th>Service</th>

</tr>

"""

    for port in report.get("ports", []):

        html += f"""

<tr>

<td>{port['port']}</td>

<td>{port['service']}</td>

</tr>

"""

    html += "</table>"

    html += """

<h2>Subdomains</h2>

<table>

<tr>

<th>Subdomain</th>

<th>IP</th>

</tr>

"""

    for sub in report.get("subdomains", []):

        html += f"""

<tr>

<td>{sub['subdomain']}</td>

<td>{sub['ip']}</td>

</tr>

"""

    html += """

</table>

</body>

</html>

"""

    with open(filename, "w") as file:

        file.write(html)

    return filename
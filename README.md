# Automated-Recon-Tool
A modular Python-based reconnaissance framework designed to automate information gathering during authorized penetration testing and security assessments. The tool streamlines reconnaissance by collecting network, DNS, HTTP, SSL/TLS, and web application information, while generating professional JSON and HTML reports.

> ⚠️ **Disclaimer:** This tool is intended for educational purposes and authorized security testing only. Always obtain proper permission before scanning any systems.

---

## 🚀 Features

### 🌐 Information Gathering
- URL Validation
- Domain Extraction
- IP Address Resolution
- DNS Enumeration
  - A Records
  - AAAA Records
  - MX Records
  - NS Records
  - TXT Records
  - CNAME Records
- WHOIS Lookup

### 🔍 Network Reconnaissance
- TCP Port Scanning
- Service Detection

### 🌍 Web Reconnaissance
- HTTP Enumeration
- Technology Fingerprinting
- Security Header Analysis
- robots.txt Analysis
- sitemap.xml Analysis
- SSL/TLS Certificate Validation
- Subdomain Enumeration

### 📊 Reporting
- JSON Report Generation
- HTML Report Generation
- Scan Summary
- Scan Duration

---

## 🛠 Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Socket
- SSL
- JSON
- HTML
- XML
- Colorama

---

## 📁 Project Structure

```
Automated-Recon-Tool/
│
├── modules/
│   ├── dns.py
│   ├── fingerprint.py
│   ├── headers.py
│   ├── http_enum.py
│   ├── ports.py
│   ├── report.py
│   ├── robots.py
│   ├── sitemap.py
│   ├── sslcheck.py
│   ├── subdomains.py
│   └── whois_lookup.py
│
├── reports/
│
├── recon.py
├── config.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Automated-Recon-Tool.git

cd Automated-Recon-Tool
```

Create a virtual environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```cmd
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the tool

```bash
python recon.py
```

Enter the target URL when prompted

Example:

```text
https://example.com
```

---

## 📄 Reports

The tool automatically generates:

```
reports/report.json
reports/report.html
```

These reports include:

- Target Information
- DNS Records
- WHOIS Information
- Open Ports
- HTTP Enumeration
- Technology Fingerprinting
- Security Header Analysis
- SSL/TLS Details
- robots.txt Analysis
- sitemap.xml Analysis
- Subdomain Enumeration

---

## 📸 Example Output

```
SCAN COMPLETED

Target              : https://example.com
IP Address          : 104.xx.xx.xx

Technologies Found  : 1
Open Ports          : 4
Subdomains Found    : 1

Reports

JSON : reports/report.json
HTML : reports/report.html
```

---

## 🎯 Skills Demonstrated

- Python Programming
- Network Programming
- DNS Enumeration
- HTTP Protocol Analysis
- SSL/TLS Validation
- Port Scanning
- Information Gathering
- Reconnaissance Automation
- Web Security
- Report Generation
- Modular Software Development

---

## 🔮 Future Improvements

- Multithreaded Port Scanning
- Advanced Subdomain Enumeration
- Screenshot Capture
- Directory Enumeration
- API Integration
- Export to PDF
- Interactive HTML Dashboard

---

## 📜 License

This project is developed for educational and authorized security assessment purposes only.

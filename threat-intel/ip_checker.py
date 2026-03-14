# ============================================================
# ThreatWatch-SOC-Lab | Threat Intelligence Script
# Author: Mohammed Shakir
# Last Updated: March 2026
# ============================================================
# This script queries the AbuseIPDB API to enrich suspicious
# IPs detected in Splunk. Instead of manually checking each
# IP on a website, this automates the whole process.
#
# In my lab I used this after Splunk flagged brute force
# attempts — fed the source IP here to get instant context.
# ============================================================

import requests
from datetime import datetime

def check_ip(ip):
    """
    Queries AbuseIPDB for threat intel on a suspicious IP.
    Returns abuse score, country, total reports and severity.
    """
    
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": "YOUR_API_KEY_HERE",  # Replace with your AbuseIPDB API key
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()["data"]

        score = data["abuseConfidenceScore"]
        severity = "HIGH" if score > 50 else "MEDIUM" if score > 20 else "LOW"

        print(f"\n{'='*45}")
        print(f"   THREAT INTELLIGENCE REPORT")
        print(f"{'='*45}")
        print(f"  IP Address    : {ip}")
        print(f"  Abuse Score   : {score}%")
        print(f"  Total Reports : {data['totalReports']}")
        print(f"  Country       : {data['countryCode']}")
        print(f"  ISP           : {data['isp']}")
        print(f"  Severity      : {severity}")
        print(f"  Checked At    : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'='*45}\n")

        return score, severity

    except Exception as e:
        print(f"[ERROR] Could not fetch threat intel: {e}")
        return 0, "UNKNOWN"


def generate_report(ip, score, severity, event_type):
    """
    Auto-generates a structured incident report.
    Saves to a .txt file for documentation.
    """

    report = f"""
========================================
         INCIDENT REPORT
========================================
Date/Time    : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Analyst      : Mohammed Shakir
========================================
INCIDENT DETAILS
----------------------------------------
Event Type   : {event_type}
Source IP    : {ip}
Detected By  : Splunk SIEM
Abuse Score  : {score}%
Severity     : {severity}
========================================
MITRE ATT&CK MAPPING
----------------------------------------
Technique    : T1110 - Brute Force
Tactic       : Credential Access
========================================
ACTION TAKEN
----------------------------------------
- IP flagged in Splunk SIEM alert
- Threat intel enriched via AbuseIPDB
- Incident report generated and logged
========================================
"""

    filename = f"incident_{ip}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(filename, "w") as f:
        f.write(report)

    print(report)
    print(f"[+] Report saved: {filename}")


# ============================================================
# Example usage — run after Splunk flags a suspicious IP
# ============================================================
if __name__ == "__main__":
    suspicious_ip = "192.168.148.130"  # Replace with actual flagged IP
    score, severity = check_ip(suspicious_ip)
    generate_report(suspicious_ip, score, severity, "Brute Force Attack")

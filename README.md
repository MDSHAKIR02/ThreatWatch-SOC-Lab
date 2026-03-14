# 🛡️ ThreatWatch-SOC-Lab

![SOC Lab](https://img.shields.io/badge/SOC-Home%20Lab-blue?style=for-the-badge)
![Splunk](https://img.shields.io/badge/Splunk-SIEM-brightgreen?style=for-the-badge)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Automation-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> A hands-on SOC home lab simulating real-world cyberattacks, threat detection, and incident response — built from scratch using enterprise-grade tools.

---

## 📖 About This Project

I first started experimenting with security tools like Nmap, Metasploit, and Aircrack-ng about 8-9 months ago. Life got busy, practice stopped, and honestly — I forgot most of it.

Then I decided to build something real instead of just following tutorials. This lab is that attempt.

It wasn't smooth. Metasploitable wouldn't get a Host-Only IP, Splunk threw 404 errors, Hydra couldn't reach the target — I hit every wall possible. But fixing each issue taught me more than any course would have.

By the end I understood:
- How Windows event logs actually work
- How a SIEM ingests and searches logs in real-time
- How brute force attacks look from the defender side
- How threat intel enrichment fits into a real SOC workflow
- How to write Python scripts that automate analyst tasks

This is a fresher's lab — not an enterprise deployment. But every alert, every detection, every incident report here is real and working.

---

## 🏗️ Lab Architecture
```
┌─────────────────────────────────────────┐
│         HOST-ONLY NETWORK               │
│          192.168.148.0/24               │
│                                         │
│  ┌──────────┐     ┌──────────────────┐  │
│  │   Kali   │────▶│   Windows 10     │  │
│  │ Attacker │     │  Splunk SIEM     │  │
│  │.148.130  │     │    .148.131      │  │
│  └──────────┘     └──────────────────┘  │
│       │                                 │
│       ▼                                 │
│  ┌──────────────┐                       │
│  │Metasploitable│                       │
│  │    Victim    │                       │
│  │  .148.132    │                       │
│  └──────────────┘                       │
└─────────────────────────────────────────┘
```

---

## 🔧 Tools & Technologies

| Tool | Purpose |
|------|---------|
| Splunk Enterprise | SIEM — log ingestion, correlation, alerting |
| Kali Linux 2025.2 | Attack simulation |
| Metasploitable 2 | Vulnerable target machine |
| Windows 10 | Target + Splunk host |
| Python 3 | Threat intel automation |
| Nmap | Network reconnaissance |
| Hydra | Brute force simulation |
| AbuseIPDB API | Threat intelligence enrichment |

---

## ⚔️ Attack Scenarios Simulated

### 1. Brute Force Attack — RDP
- **Tool:** Hydra
- **Target:** Windows 10 (192.168.148.131:3389)
- **MITRE ATT&CK:** T1110 — Brute Force
- **Tactic:** Credential Access
- **Result:** 1,720+ events captured in Splunk ✅

### 2. Network Reconnaissance
- **Tool:** Nmap SYN Scan
- **Target:** Full lab network
- **MITRE ATT&CK:** T1046 — Network Service Discovery
- **Tactic:** Discovery
- **Result:** Live hosts and ports identified ✅

---

## 🔍 Detection & Response Workflow
```
Attack Launched from Kali
        ↓
Windows Generates Event Logs
        ↓
Splunk SIEM Ingests Logs in Real-Time
        ↓
SPL Query Detects EventCode 4625
        ↓
Real-Time Alert Fires — "Brute Force Detection"
        ↓
Python Enriches Source IP via AbuseIPDB API
        ↓
Incident Report Auto-Generated with MITRE Mapping
```

---

## 📊 Splunk SPL Detection Rules
```spl
# Brute Force Detection — EventCode 4625
index=main EventCode=4625
| stats count by src_ip, user
| where count > 5

# Suspicious Process Detection — EventCode 4688
index=main EventCode=4688
| search CommandLine="*nmap*" OR "*mimikatz*"
```

---

## 🐍 Python Threat Intel Script
```python
def check_ip(ip):
    # Queries AbuseIPDB API
    # Returns: abuse score, country, total reports
    # Generates severity: HIGH / MEDIUM / LOW
    # Auto-saves incident report to .txt file
```

---

## 📄 Sample Incident Report
```
========================================
         INCIDENT REPORT
========================================
Date/Time    : 2026-03-14 11:59:13
Analyst      : Mohammed Shakir
========================================
Event Type   : Brute Force Attack
Source IP    : 192.168.148.130
Detected By  : Splunk SIEM
Abuse Score  : 87%
Severity     : HIGH
========================================
MITRE ATT&CK MAPPING
Technique    : T1110 - Brute Force
Tactic       : Credential Access
========================================
ACTION TAKEN
- IP flagged in Splunk SIEM
- Threat Intel checked via AbuseIPDB
- Incident logged for review
========================================
```

---

## 🧠 Skills Demonstrated

| Skill | Details |
|-------|---------|
| SIEM Operations | Splunk log ingestion, SPL queries, real-time alerting |
| Threat Detection | EventCode analysis, brute force detection |
| Threat Intelligence | AbuseIPDB API integration, IP enrichment |
| Incident Response | Structured incident reports, MITRE ATT&CK mapping |
| Scripting | Python automation for SOC workflows |
| Network Security | Nmap scanning, network traffic analysis |

---

## 📁 Repository Structure
```
ThreatWatch-SOC-Lab/
├── splunk-queries/
│   └── detection_rules.spl
├── threat-intel/
│   └── ip_checker.py
├── incident-reports/
│   └── sample_incident_report.txt
├── screenshots/
│   └── splunk_alert.png
│   └── event_detection.png
└── README.md
```

---

## 👤 Author

**Mohammed Shakir**
Aspiring SOC Analyst | B.Tech EEE 2026 | Cybersecurity Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mohammed%20Shakir-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/mohammed-shakir-cyber)

---

> *"Built this lab because I believe the best way to learn defense is to understand offense."*

---

⭐ *If this helped you build your own SOC lab, consider giving it a star!*

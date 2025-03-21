# Widowmaker 🕷️

**Widowmaker** is an automated vulnerability discovery framework aimed at empowering ethical hackers, bug bounty hunters, and OSINT analysts. It combines enumeration, scanning, reconnaissance, and reporting into one streamlined toolkit that evolves with the needs of offensive security professionals.


> 📢 **!!! IMPORTANT Note:** Widowmaker is in its **early development phase**. Many core features are under active construction, and stability is not guaranteed. Although I am actively practicing security, ***I am by no means an **"expert**"***. I build these tools to study and practice development and automations and they are for educational purposes only. <--- 😴

---

## 💡 Project Goal

To create an extensible, modular, and script-driven framework that automates the repetitive and time-consuming parts of bug bounty hunting, including:
- Asset discovery
- Vulnerability enumeration
- OSINT collection
- Report-ready data formatting

---

## ✅ Current Features

### 🔍 Enumeration ✅
- Subdomain discovery using external APIs
- Passive and active DNS lookups
- Wordlist-based fuzzing for directories and parameters

### 🔓 Vulnerability Scanning ✅
- Automated recon + vulnerability detection pipeline
- CVE checking for known technologies and software
- Basic HTTP service scanning

### 🌐 OSINT Collection ❌
- Basic passive intel gathering using public sources
- Metadata extraction from websites
- Tech stack identification

### 🛠️ Automation ❌
- Daily scanning schedule using cron or Task Scheduler
- Modular structure for plugging in tools/scripts
- Results stored in organized JSON/Markdown reports

---

## 🗺️ Roadmap

### 🔧 In Progress
- Refactor scanning modules into independent classes
- Add logging system + simple CLI dashboard
- Implement parallel scanning with asyncio or threading

### 🚀 Planned Features
- Integrated Slack/Discord/webhook notifications
- Built-in web dashboard for real-time monitoring
- AI-powered recon suggestion engine (targets + wordlists)
- Credential leak checking (pastebin, breach dbs, etc.)
- Mobile-friendly OSINT reporting for field ops
- GitHub/Bitbucket repo scraping and secrets detection
- Automatic scope validation against HackerOne/BB programs

---

## 📂 Project Structure (WIP)
widowmaker 
├── modules/ # Pluggable scanners and recon tools 
├── results/ # Created dirs and results in txt format after scan. Adding multiple domains will create seperate folders for each 
├── reports/ # Generated reports and templates 
├── main.py # Main controller script 
├── domains.txt # List of domains to poke
├── README.md # This file you are reading now, good job

---

## 🤝 Contributing

We're still laying the foundation, but contributors are welcome! If you have a tool, script, or API you want to integrate — open an issue or submit a PR.

---

## 📣 Disclaimer

> Widowmaker is built for **ethical** and **legal** security testing only. The developers do not support or condone unauthorized access, data leaks, or malicious activity. 

---

## 🧑‍💻 Author

GitHub: [github.com/brav0kado](https://github.com/brav0kado)

---
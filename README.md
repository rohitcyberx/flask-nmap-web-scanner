# Flask Nmap Web Scanner 🛡️

A simple Flask-based web interface for running **Nmap** scans on systems you own.  
Built as a learning project for network reconnaissance, cybercrime investigation basics, and Flask.

> ⚠️ **Educational use only.**  
> Scan **only** devices and networks you own or have written permission to test.

---

## 🔍 What it does

- Takes an IP address or domain from a web form
- Runs a safe, limited Nmap scan in the background
- Shows the raw Nmap output in the browser
- Handles invalid input and timeouts

This is similar to a small internal tool that a cybercrime unit / SOC analyst might use for **quick enumeration**.

---

## 🧱 Tech Stack

- Python 3
- Flask
- Nmap (CLI)
- HTML (Jinja2 templates)

---

## 📂 Project structure

```text
flask_nmap_scanner/
├── app.py             # Flask application
└── templates/
    ├── index.html     # Form to enter target
    └── result.html    # Page to show Nmap output

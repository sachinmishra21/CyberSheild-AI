# CyberShield-AI 🛡️

An AI-powered cybersecurity awareness tool that detects phishing emails/messages, checks URLs for safety, and tests password strength. It uses a **local LLM (Mistral via Ollama)**, so no data leaves your machine and no API key is needed.

## Features

- **Phishing detection**: paste an email, message, or URL and get a threat level (Safe / Suspicious / Dangerous)
- **URL checker**: flags suspicious links using rule-based checks
- **Password strength checker**: rates passwords and suggests improvements
- **Risk score**: a percentage-based risk score with the reasons behind it
- **AI recommendation**: Mistral explains the threat and advises what to do
- **PDF report**: every scan is saved as a timestamped "AI Cybersecurity Awareness Report" in the `reports/` folder

## Tech Stack

- Python 3
- Ollama + Mistral (local LLM)
- ReportLab / FPDF-style PDF generation (see `requirements.txt`)

## Project Structure

```
cyber security/
├── app.py               # Main entry point (menu-driven CLI)
├── analyzer.py          # Combines checks and AI analysis
├── detector.py          # Phishing / threat detection logic
├── url_checker.py       # URL safety checks
├── password_checker.py  # Password strength checker
├── report.py            # PDF report generation
├── utils.py             # Helper functions
├── samples/             # Sample test inputs
├── reports/             # Generated PDF reports (git-ignored)
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama and download the model

Download Ollama from [ollama.com](https://ollama.com), then run:

```bash
ollama pull mistral
ollama list        # should show mistral:latest
```

> ⚠️ If you see `AI Error: model 'mistral' not found (404)`, the model has not been downloaded yet. Run `ollama pull mistral` and try again.

## Usage

Make sure Ollama is running, then:

```bash
python app.py
```

Choose an option from the menu, paste the email / message / URL (or password), and the tool will show:

```
========== RESULT ==========
Threat : Dangerous
Risk   : 85 %
Reason : Suspicious link and urgent language

AI Recommendation
...
[+] Report Saved Inside reports Folder
```

The PDF report is saved in the `reports/` folder.

## Troubleshooting

| Problem | Fix |
|---|---|
| `model 'mistral' not found (404)` | Run `ollama pull mistral` |
| Connection error to Ollama | Start Ollama (`ollama serve`) |
| `ModuleNotFoundError` | Activate venv and run `pip install -r requirements.txt` |

## Disclaimer

This project is for **educational and awareness purposes**. It is not a replacement for professional security tools. Always verify suspicious links and emails through official channels.

## Author

**Sachin Mishra**
B.Tech AI & ML, Buddha Institute of Technology, Gorakhpur
Built during an AI internship at EISystems Services.

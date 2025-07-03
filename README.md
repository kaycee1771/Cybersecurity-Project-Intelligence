# 🧠 Cybersecurity Project Intelligence Dashboard (CPID)

The **Cybersecurity Project Intelligence Dashboard (CPID)** is a backend-only meta-tracker for cybersecurity project pipelines. It monitors project health, detects anomalies, and forecasts risks based on real-time data.

Think of it as the **“SIEM of Project Management”** for agile cybersecurity teams.

---

## 🚀 Features

- 📥 Log-based data collection (Jira/Trello/GitHub – simulated)
- 📊 Metrics engine (velocity, contributor stats, risk scores)
- 🚨 Anomaly detection (e.g. sudden velocity drops, churn)
- 🔮 Forecasting engine for future milestone outcomes
- 📝 Audit & compliance logging with hash tracing

---

## 🏗️ System Architecture

```
        Raw Logs
          ↓
+------------------+
| Collector        |
| (Phase 1)        |
+------------------+
          ↓
+------------------+
| Metrics Engine   |
| (Phase 2)        |
+------------------+
          ↓
+------------------+
| Anomaly Engine   |
| (Phase 3)        |
+------------------+
          ↓
+------------------+
| Forecast Engine  |
| (Phase 4)        |
+------------------+
          ↓
+------------------+
| Audit Logger     |
| (Phase 5)        |
+------------------+
```

---

## ▶️ How to Run

```bash
# Clone & enter the repo
git clone https://github.com/<your-username>/cpid.git
cd cpid

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run all phases
python run_all.py
```

---

## 📁 Folder Structure

```
cpid/
├── data/              # Raw + normalized logs
├── engine/            # Phase modules: collector, metrics, anomaly, forecast
├── logs/              # Audit logs
├── metrics/           # Output results
├── utils/             # Logger, configs
├── run_all.py         # Orchestration script
├── run_phase*.py      # Individual phase runners
├── requirements.txt
└── README.md
```

---

## 📈 Sample Outputs

- `metrics/project_scores.json` → Velocity, risk, contributors
- `metrics/anomaly_flags.json` → Flags for suspicious behavior
- `metrics/forecast.json` → Predicted project success/failure
- `logs/project_audit.log` → Audit trail (timestamped, hashed)

---

## 🧩 Future Enhancements

- 🌐 API endpoints (Flask/FastAPI)
- 📊 Web dashboard frontend (React/Vue)
- 🧠 ML model auto-tuning using `river`
- 🔗 Blockchain-ready audit logging

---

## 🧑‍💻 Author

Built by Kelechi Okpala, 2025  
Cybersecurity + AI-Driven Infrastructure Enthusiast  

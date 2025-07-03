# Cybersecurity Project Intelligence Dashboard (CPID)

> **Real-time risk scoring and audit intelligence for cybersecurity projects.**  
> Imagine GitHub + ISO27001 compliance + AI anomaly detection — fully automated.

---

## Overview

**CPID** is a smart pipeline that ingests development activity (e.g., GitHub logs), calculates behavioral metrics, detects anomalies using both statistical and ML models, forecasts risk trends, and auto-generates audit & ISMS reports for compliance visibility.

### Why It Matters

- Prevent security debt by catching risky behaviors early
- Predict future compliance drifts using real data
- Auto-generate logs for ISO 27001/NIS2 readiness
- ML-powered anomaly detection (via River)

---

## Features

| Phase | Description |
|-------|-------------|
| **Phase 1** | Log ingestion + GitHub normalization |
| **Phase 2** | Risk metric calculation (velocity, volatility, reliability) |
| **Phase 3** | Anomaly detection (Z-score + River ML model auto-tuning) |
| **Phase 4** | Risk forecasting using historical metrics |
| **Phase 5** | Audit report generation (JSON + human-readable log) |
| **Phase 6** | ISMS Control Mapping (ISO27001, NIS2) |

---

## Project Structure

```
CPID/
├── core/                    # Phase scripts (invoked by CLI)
├── engine/                  # Logic modules (metrics, normalizer, ML, etc.)
├── models/                  # Saved River ML model
├── metrics/                 # Output: scores, anomalies, forecasts
├── logs/                    # Generated audit logs
├── data/normalized/         # Parsed GitHub logs
├── utils/                   # Logging utilities
├── cpid.py                  # Main CLI runner
```

---

## Usage

Run the full pipeline:

```bash
python cpid.py run all
```

Run a specific phase:

```bash
python cpid.py run phase3
```

---

## Intelligence Stack

- Metric Engine: Velocity, change size, contributor reliability
- Hybrid Anomaly Detection:
  - Statistical Z-Score
  - ML-based classifier (River: Logistic Regression + StandardScaler)
- Forecasting: Project risk trends (future sprints)
- Audit Logger: Merges anomaly & forecast into readable and machine-readable audit logs
- ISMS Map: Projects flagged to ISO27001 controls (A.12, A.17, etc.)

---

## Sample Output

- `metrics/project_scores.json`
- `metrics/anomaly_flags.json`
- `metrics/forecast.json`
- `logs/project_audit.log`
- `metrics/isms_map.json`

---

## Future Work

- GitHub Actions CI/CD to audit all commits
- Slack/Email anomaly alerts
- Web dashboard
- GitHub App with webhook push triggers

---

## License

MIT License

---

## Maintainer

**Kelechi Okpala** – Helsinki, Finland  
Cybersecurity Student & Enthusiast
[GitHub @kaycee1771](https://github.com/kaycee1771)

---

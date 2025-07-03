import json
import os
from datetime import datetime

ANOMALY_FILE = "metrics/anomaly_flags.json"
FORECAST_FILE = "metrics/forecast.json"
LOG_FILE = "logs/project_audit.log"
JSON_REPORT_FILE = "metrics/audit_report.json"

def load_json(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def classify_risk(anomaly_score, flags):
    if anomaly_score == 0:
        return "OK"
    elif "low_reliability" in flags:
        return "HIGH"
    elif len(flags) > 1:
        return "MODERATE"
    else:
        return "LOW"

def run():
    print("Phase 5: Audit & Compliance Logger")
    os.makedirs("logs", exist_ok=True)

    anomalies = load_json(ANOMALY_FILE)
    forecast_list = load_json(FORECAST_FILE)

    forecasts = {f.get("project_id", "unknown"): f for f in forecast_list}

    report = {}
    lines = [f"Project Audit Log — {datetime.utcnow().isoformat()}Z\n"]

    for entry in anomalies:
        pid = entry.get("project_id", "unknown")
        milestone = entry["milestone"]
        risk_level = classify_risk(entry["anomaly_score"], entry["flags"])
        forecast = forecasts.get(pid, {})
        risk_trend = forecast.get("risk_trend", "unknown")

        lines.append(f"{pid} [{milestone}]")
        lines.append(f"  - Anomaly Score: {entry['anomaly_score']}")
        lines.append(f"  - Flags: {entry['flags']}")
        lines.append(f"  - ML Prediction: {entry['ml_predicted_anomaly']}")
        lines.append(f"  - Risk Level: {risk_level}")
        lines.append(f"  - Forecasted Trend: {risk_trend}")
        lines.append("")

        report[pid] = {
            "milestone": milestone,
            "anomaly_score": entry["anomaly_score"],
            "flags": entry["flags"],
            "ml_predicted_anomaly": entry["ml_predicted_anomaly"],
            "risk_level": risk_level,
            "forecast_trend": risk_trend
        }

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    with open(JSON_REPORT_FILE, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Audit report written to {LOG_FILE}")
    print(f"Structured JSON report saved to {JSON_REPORT_FILE}")
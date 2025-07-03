import json
import os

AUDIT_FILE = "metrics/audit_report.json"
OUTPUT_FILE = "metrics/isms_map.json"

def load_json(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def map_controls(entry):
    flags = entry.get("flags", [])
    trend = entry.get("forecast_trend", "unknown")
    risk = entry.get("risk_level", "OK")
    ml_flag = entry.get("ml_predicted_anomaly", 0)

    control_status = {}

    control_status["A.14.2.2 – Secure Development Policy"] = (
        "RISK" if any(f in flags for f in ["high_volatility", "low_reliability"]) else "OK"
    )

    control_status["A.12.6.1 – Technical Vulnerability Management"] = (
        "RISK" if "high_velocity" in flags or risk == "HIGH" else "OK"
    )

    control_status["A.9.4.1 – Information Access Control"] = (
        "RISK" if "low_velocity" in flags else "OK"
    )

    control_status["A.17.2.1 – Availability of Information Processing Facilities"] = (
        "RISK" if trend == "degrading" else "OK"
    )

    control_status["A.18.2.3 – Technical Compliance Checking"] = (
        "RISK" if ml_flag == 1 else "OK"
    )

    return control_status

def run():
    print("Phase 6: ISMS Control Mapping")

    audit = load_json(AUDIT_FILE)
    isms_map = {}

    for project_id, entry in audit.items():
        isms_map[project_id] = map_controls(entry)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(isms_map, f, indent=2)

    print(f"ISMS control map generated: {OUTPUT_FILE}")

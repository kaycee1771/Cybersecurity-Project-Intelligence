import json
import os
from utils.logger import log_event
from engine.anomaly_detector import detect_anomalies

INPUT_FILE = "metrics/project_scores.json"
OUTPUT_FILE = "metrics/anomaly_flags.json"

def run():
    print("Phase 3: Anomaly Detection")

    print("Loading project metrics...")
    with open(INPUT_FILE) as f:
        scores = json.load(f)

    print("Running anomaly detection...")
    anomalies = detect_anomalies()

    os.makedirs("metrics", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(anomalies, f, indent=2)

    print(f"{len(anomalies)} anomalies detected.")
    print(f"Saved to {OUTPUT_FILE}")

    log_event("anomaly_detection", "Detected anomalies in project metrics.", anomalies)

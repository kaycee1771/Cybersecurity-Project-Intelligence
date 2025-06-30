import os
import json

RAW_DIR = "data/raw_logs"

def collect_raw_logs():
    logs = []
    for fname in os.listdir(RAW_DIR):
        if fname.endswith(".json"):
            with open(os.path.join(RAW_DIR, fname)) as f:
                try:
                    logs += json.load(f)
                except Exception as e:
                    print(f"Error loading {fname}: {e}")
    return logs

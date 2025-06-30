import json
from utils.logger import log_event
from collections import defaultdict
from engine.simulator import forecast_project
import os

INPUT_FILE = "metrics/project_scores.json"
OUTPUT_FILE = "metrics/forecast.json"

def run_phase4():
    print("📥 Loading project metrics...")
    with open(INPUT_FILE) as f:
        scores = json.load(f)

    print("🔮 Generating forecasts...")
    grouped = defaultdict(list)
    for entry in scores:
        grouped[entry["project_id"]].append(entry)

    results = []
    for project_id, history in grouped.items():
        history = sorted(history, key=lambda x: x["milestone"])
        if len(history) >= 2:
            result = forecast_project(history)
            results.append(result)
        else:
            print(f"⚠️  Not enough history to forecast: {project_id}")

    os.makedirs("metrics", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ Forecasts saved to {OUTPUT_FILE}")
    
    log_event("forecast", "Generated risk forecast for upcoming milestones.", results)

if __name__ == "__main__":
    run_phase4()
    
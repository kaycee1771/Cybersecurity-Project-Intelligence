import json
import os
from collections import defaultdict
from utils.logger import log_event
from engine.metrics_engine import compute_velocity, compute_avg_change, compute_contributor_stats
from engine.risk_scoring import score_reliability, score_risk

INPUT_FILE = "data/normalized/github_normalized.json"
OUTPUT_FILE = "metrics/project_scores.json"

def run():
    print("Phase 2: Metrics Engine")
    print("Loading normalized logs...")

    with open(INPUT_FILE) as f:
        logs = json.load(f)

    grouped = defaultdict(list)
    for log in logs:
        key = (log["project_id"], log["milestone"])
        grouped[key].append(log)

    results = []
    for (project_id, milestone), entries in grouped.items():
        print(f"Processing: {project_id} / {milestone}")
        velocity = compute_velocity(entries)
        avg_change = compute_avg_change(entries)
        contributor_stats = compute_contributor_stats(entries)
        reliability = score_reliability(contributor_stats)
        risk_score = score_risk(velocity, reliability, avg_change)

        results.append({
            "project_id": project_id,
            "milestone": milestone,
            "velocity": float(velocity),
            "avg_change_size": float(avg_change),
            "contributors": contributor_stats,
            "reliability_score": float(reliability),
            "risk_score": float(risk_score)
        })

    os.makedirs("metrics", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"All project scores saved to {OUTPUT_FILE}")
    log_event("metrics", "Calculated metrics for all projects.", results)

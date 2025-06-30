from datetime import datetime
import json
import os

NORMALIZED_DIR = "data/normalized"

def normalize_github(commits):
    normalized = []
    for commit in commits:
        normalized.append({
            "project_id": "cybersec-core",
            "timestamp": commit["timestamp"],
            "source": "github",
            "milestone": "sprint-5",  
            "ticket_id": commit["commit_id"],
            "status": "committed",
            "contributor": commit["committer"],
            "change_size": commit["lines_changed"],
            "risk_tag": "none" if "fix" in commit["message"].lower() else "review"
        })
    return normalized

def save_normalized(data, filename):
    os.makedirs(NORMALIZED_DIR, exist_ok=True)
    with open(os.path.join(NORMALIZED_DIR, filename), "w") as f:
        json.dump(data, f, indent=2)

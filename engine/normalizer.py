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
            "milestone": commit["milestone"], 
            "ticket_id": commit["commit_id"],
            "status": "committed",
            "contributor": commit["committer"], 
            "change_size": commit.get("lines_changed", commit.get("lines_added", 0) + commit.get("lines_deleted", 0)),
            "risk_tag": "none" if "fix" in commit.get("message", "").lower() else "review"
        })
    return normalized

'''def normalize_github(logs):
    return [
        {
            "project_id": log["project_id"],
            "milestone": log["milestone"],
            "author": log.get("author", "unknown"),
            "committer": log.get("committer", log.get("author", "unknown")),
            "change_size": log.get("lines_changed", log.get("lines_added", 0) + log.get("lines_deleted", 0)),
            "timestamp": log["timestamp"]
        }
        for log in logs
    ]'''

def save_normalized(data, filename):
    os.makedirs(NORMALIZED_DIR, exist_ok=True)
    with open(os.path.join(NORMALIZED_DIR, filename), "w") as f:
        json.dump(data, f, indent=2)

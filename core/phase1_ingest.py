from engine.collector import collect_raw_logs
from engine.normalizer import normalize_github, save_normalized

def run():
    print("Phase 1: Log Ingestion")

    print("Collecting raw logs...")
    logs = collect_raw_logs()
    print(f"Collected {len(logs)} raw records.")

    github_logs = [log for log in logs if "commit_id" in log]

    print("Normalizing GitHub logs...")
    normalized_logs = normalize_github(github_logs)
    print(f"Normalized {len(normalized_logs)} records.")

    print("Saving normalized data...")
    save_normalized(normalized_logs, "github_normalized.json")
    print("Done! Normalized data saved to data/normalized/github_normalized.json")

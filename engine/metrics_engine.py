import json
from collections import defaultdict
from datetime import datetime
from dateutil.parser import parse as parse_date

def compute_velocity(entries):
    timestamps = [parse_date(entry["timestamp"]) for entry in entries]
    if not timestamps:
        return 0
    start = min(timestamps)
    end = max(timestamps)
    days = max((end - start).days, 1)  
    return round(len(entries) / days, 2)

def compute_avg_change(entries):
    if not entries:
        return 0
    total = sum(entry.get("change_size", 0) for entry in entries)
    return round(total / len(entries), 2)

def compute_contributor_stats(entries):
    stats = defaultdict(lambda: {"commits": 0, "total_change": 0})
    for entry in entries:
        contributor = entry["contributor"]
        stats[contributor]["commits"] += 1
        stats[contributor]["total_change"] += entry.get("change_size", 0)

    # Convert to avg change
    for user in stats:
        commits = stats[user]["commits"]
        stats[user]["avg_change"] = round(stats[user]["total_change"] / commits, 2)
        del stats[user]["total_change"]
    return dict(stats)
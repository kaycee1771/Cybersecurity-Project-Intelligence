import os
import json
from datetime import datetime
import hashlib

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "project_audit.log")

def compute_hash(data):
    """Generate a SHA256 hash of a JSON-serializable object."""
    data_string = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(data_string).hexdigest()

def log_event(operation, summary, payload=None):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.utcnow().isoformat()
    hash_digest = compute_hash(payload) if payload else "N/A"

    log_entry = f"[{timestamp}] OPERATION={operation}\\nSUMMARY={summary}\\nHASH={hash_digest}\\n\\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
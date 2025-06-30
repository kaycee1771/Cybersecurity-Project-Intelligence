import json
import numpy as np

def detect_anomalies(entries, threshold=2.0):
    """
    Detect anomalies based on Z-score deviation from the mean.
    Flags: low_velocity, high_volatility, low_reliability
    """
    velocities = np.array([e["velocity"] for e in entries])
    changes = np.array([e["avg_change_size"] for e in entries])
    reliabilities = np.array([e["reliability_score"] for e in entries])

    mean_vel, std_vel = np.mean(velocities), np.std(velocities)
    mean_chg, std_chg = np.mean(changes), np.std(changes)
    mean_rel, std_rel = np.mean(reliabilities), np.std(reliabilities)

    anomalies = []

    for e in entries:
        flags = []

        # Velocity anomaly
        if abs(e["velocity"] - mean_vel) > threshold * std_vel:
            flags.append("low_velocity" if e["velocity"] < mean_vel else "high_velocity")

        # Change size anomaly
        if abs(e["avg_change_size"] - mean_chg) > threshold * std_chg:
            flags.append("high_volatility")

        # Reliability anomaly
        if abs(e["reliability_score"] - mean_rel) > threshold * std_rel:
            flags.append("low_reliability")

        if flags:
            anomaly_score = round(len(flags) / 3, 2)
            anomalies.append({
                "project_id": e["project_id"],
                "milestone": e["milestone"],
                "flags": flags,
                "anomaly_score": anomaly_score
            })

    return anomalies
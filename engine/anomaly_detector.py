import json
import os
import pickle
import numpy as np
from river import linear_model, preprocessing, metrics

INPUT_FILE = "metrics/project_scores.json"
OUTPUT_FILE = "metrics/anomaly_flags.json"
MODEL_FILE = "models/river_model.pkl"

def detect_anomalies(threshold=2.0):
    # Project metrics
    if not os.path.exists(INPUT_FILE):
        print(f"Missing input: {INPUT_FILE}")
        return []

    with open(INPUT_FILE, "r") as f:
        raw_data = json.load(f)

    # Clean + cast entries
    entries = []
    for m in raw_data:
        try:
            entries.append({
                "project_id": m.get("project_id", "unknown"),
                "milestone": m.get("milestone", "unknown"),
                "velocity": float(m.get("velocity", 0)),
                "avg_change_size": float(m.get("avg_change_size", 0)),
                "reliability_score": float(m.get("reliability_score", 0))
            })
        except (ValueError, TypeError):
            continue

    if not entries:
        print("No valid numeric entries to process.")
        return []

    # Z-score statistics
    velocities = np.array([e["velocity"] for e in entries])
    changes = np.array([e["avg_change_size"] for e in entries])
    reliabilities = np.array([e["reliability_score"] for e in entries])

    mean_vel, std_vel = np.mean(velocities), np.std(velocities)
    mean_chg, std_chg = np.mean(changes), np.std(changes)
    mean_rel, std_rel = np.mean(reliabilities), np.std(reliabilities)

    # River model
    if os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, "rb") as f:
            model = pickle.load(f)
    else:
        model = preprocessing.StandardScaler() | linear_model.LogisticRegression()

    accuracy = metrics.Accuracy()
    output = []

    for e in entries:
        flags = []

        # Z-score based flags
        if std_vel > 0 and abs(e["velocity"] - mean_vel) > threshold * std_vel:
            flags.append("low_velocity" if e["velocity"] < mean_vel else "high_velocity")

        if std_chg > 0 and abs(e["avg_change_size"] - mean_chg) > threshold * std_chg:
            flags.append("high_volatility")

        if std_rel > 0 and abs(e["reliability_score"] - mean_rel) > threshold * std_rel:
            flags.append("low_reliability")

        anomaly_score = round(len(flags) / 3, 2) if flags else 0

        # ML prediction
        x = {
            "velocity": e["velocity"],
            "avg_change_size": e["avg_change_size"],
            "reliability_score": e["reliability_score"]
        }

        y = int(anomaly_score > 0)
        y_pred = model.predict_one(x) or 0
        model.learn_one(x, y)
        accuracy.update(y, y_pred)

        output.append({
            "project_id": e["project_id"],
            "milestone": e["milestone"],
            "flags": flags,
            "anomaly_score": anomaly_score,
            "ml_predicted_anomaly": int(y_pred),
            "ml_confidence_features": x
        })

    # Save output
    os.makedirs("metrics", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    os.makedirs("models", exist_ok=True)
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    print(f"Combined anomaly detection complete. Accuracy: {accuracy.get():.2f}")
    print(f"Results saved to {OUTPUT_FILE}")
    return output

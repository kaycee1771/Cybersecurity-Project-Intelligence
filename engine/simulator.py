import json
from collections import defaultdict
import numpy as np

def linear_forecast(values):
    """
    Forecast the next value using a simple linear extrapolation.
    values: list of float (time-ordered)
    """
    if len(values) < 2:
        return values[-1] if values else 0
    x = np.arange(len(values))
    y = np.array(values)
    coeffs = np.polyfit(x, y, 1)
    slope, intercept = coeffs
    forecast = slope * (len(values)) + intercept
    return round(forecast, 2), slope

def monte_carlo_simulation(values, std_dev, iterations=1000):
    sims = []
    for _ in range(iterations):
        simulated = [v + np.random.normal(0, std_dev) for v in values]
        forecast, _ = linear_forecast(simulated)
        sims.append(forecast)
    avg_forecast = np.mean(sims)
    std_forecast = np.std(sims)
    return round(avg_forecast, 2), round(std_forecast, 2)
    
def forecast_project(project_history):
    project_id = project_history[0]["project_id"]
    milestones = [entry["milestone"] for entry in project_history]
    velocities = [entry["velocity"] for entry in project_history]
    risks = [entry["risk_score"] for entry in project_history]

    pred_velocity, vel_slope = linear_forecast(velocities)
    pred_risk, risk_slope = linear_forecast(risks)

    forecast_label = "on_track"
    if pred_risk > 0.6 or pred_velocity < 1.5:
        forecast_label = "at_risk"

    confidence = round(1.0 - abs(risk_slope + vel_slope) / 10, 2)
    confidence = max(0.0, min(1.0, confidence))

    return {
        "project_id": project_id,
        "next_milestone": f"sprint-{int(milestones[-1].split('-')[-1]) + 1}",
        "predicted_velocity": pred_velocity,
        "predicted_risk_score": pred_risk,
        "forecast": forecast_label,
        "confidence": confidence
    }
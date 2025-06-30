def score_reliability(contributor_stats):
   
    counts = [v["commits"] for v in contributor_stats.values()]
    if len(counts) <= 1:
        return 1.0
    mean = sum(counts) / len(counts)
    variance = sum((x - mean) ** 2 for x in counts) / len(counts)
    reliability = max(0.0, min(1.0, 1.0 - variance / 10))  # Normalize
    return round(reliability, 2)

def score_risk(velocity, reliability, avg_change):
    ALPHA = 0.4
    BETA = 0.3
    GAMMA = 0.3

    
    velocity_drop = max(0, (3 - velocity) / 3)
    contributor_risk = 1 - reliability
    volatility_score = max(0, min(1, abs(avg_change - 100) / 100))  

    risk = ALPHA * velocity_drop + BETA * contributor_risk + GAMMA * volatility_score
    return round(risk, 2)
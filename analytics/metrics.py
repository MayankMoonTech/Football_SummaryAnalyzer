def calculate_metrics(df):

    # Filter events
    passes = df[df["event_type"] == "pass"]
    shots = df[df["event_type"] == "shot"]
    tackles = df[df["event_type"] == "tackle"]

    # Avoid division by zero
    if len(passes) > 0:
        pass_accuracy = len(passes[passes["result"] == "success"]) / len(passes)
    else:
        pass_accuracy = 0

    metrics = {
        "total_passes": len(passes),
        "shots": len(shots),
        "tackles": len(tackles),
        "pass_accuracy": round(pass_accuracy, 2)
    }

    return metrics
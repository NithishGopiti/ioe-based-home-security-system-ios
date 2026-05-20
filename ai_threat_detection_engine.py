import numpy as np

def detect_threat(sensor_event):

    anomaly_score = sensor_event["anomaly_score"]

    if anomaly_score > 80:
        return {
            "threat_detected": True,
            "severity": "CRITICAL"
        }

    if anomaly_score > 50:
        return {
            "threat_detected": True,
            "severity": "MEDIUM"
        }

    return {
        "threat_detected": False,
        "severity": "LOW"
    }

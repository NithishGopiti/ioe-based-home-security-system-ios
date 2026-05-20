def validate_sensor_payload(payload):

    required_fields = [
        "sensor_id",
        "sensor_type",
        "event_type",
        "anomaly_score",
        "device_location"
    ]

    for field in required_fields:

        if field not in payload:
            return False

    if payload["anomaly_score"] < 0:
        return False

    return True

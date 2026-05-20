def validate_sensor_health(sensor_metrics):

    if sensor_metrics["packet_loss"] > 40:
        return False

    return True

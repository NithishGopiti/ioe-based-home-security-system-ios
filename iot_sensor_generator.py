from faker import Faker
from datetime import datetime

import random
import json
import uuid

fake = Faker()

SENSOR_TYPES = [
    "MOTION",
    "TEMPERATURE",
    "DOOR",
    "WINDOW",
    "SMOKE",
    "CAMERA"
]

EVENTS = [
    "NORMAL",
    "INTRUSION",
    "ALERT",
    "MOVEMENT"
]

def generate_sensor_event():

    return {
        "sensor_id": str(uuid.uuid4()),
        "sensor_type": random.choice(SENSOR_TYPES),
        "event_type": random.choice(EVENTS),
        "anomaly_score": round(random.uniform(0, 100), 2),
        "device_location": fake.city(),
        "created_at": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":

    for _ in range(10):
        print(json.dumps(generate_sensor_event()))

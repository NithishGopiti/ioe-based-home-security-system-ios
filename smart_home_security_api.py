from fastapi import FastAPI

from ai_threat_detection_engine import detect_threat

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "smart_security_platform_running"
    }

@app.post("/detect-threat")
def detect(sensor_event: dict):

    return detect_threat(sensor_event)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()

class SensorEvent(Base):

    __tablename__ = "sensor_events"

    id = Column(Integer, primary_key=True)

    sensor_id = Column(String(120))
    sensor_type = Column(String(120))

    event_type = Column(String(120))
    anomaly_score = Column(Float)

    device_location = Column(String(120))

    created_at = Column(DateTime)

class SecurityAlert(Base):

    __tablename__ = "security_alerts"

    id = Column(Integer, primary_key=True)

    alert_type = Column(String(120))
    severity = Column(String(50))
    response_status = Column(String(50))

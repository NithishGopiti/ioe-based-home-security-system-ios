from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from security_platform_settings import security_settings

DATABASE_URL = (
    f"mysql+pymysql://{security_settings.MYSQL_USER}:"
    f"{security_settings.MYSQL_PASSWORD}@"
    f"{security_settings.MYSQL_HOST}:"
    f"{security_settings.MYSQL_PORT}/"
    f"{security_settings.MYSQL_DATABASE}"
)

security_engine = create_engine(
    DATABASE_URL,
    pool_size=30,
    max_overflow=60,
    pool_pre_ping=True,
    pool_recycle=3600
)

SecuritySession = sessionmaker(
    bind=security_engine,
    autocommit=False,
    autoflush=False
)

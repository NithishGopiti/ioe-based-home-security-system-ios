from security_database_connection import security_engine
from security_models import Base

def initialize_security_tables():
    Base.metadata.create_all(bind=security_engine)

if __name__ == "__main__":
    initialize_security_tables()

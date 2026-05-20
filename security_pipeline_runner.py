import subprocess

services = [
    ["python", "initialize_security_tables.py"],
    ["uvicorn", "smart_home_security_api:app", "--host", "0.0.0.0", "--port", "8050"]
]

for service in services:
    subprocess.Popen(service)

input()

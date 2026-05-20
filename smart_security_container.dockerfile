FROM python:3.11

WORKDIR /smart_security_platform

COPY . .

RUN pip install -r security_platform_requirements.txt

CMD ["python", "security_pipeline_runner.py"]

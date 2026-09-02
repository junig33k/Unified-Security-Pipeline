FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser || useradd -u 1000 appuser && chown -R 1000:1000 /app
USER appuser

ENTRYPOINT ["python", "orchestrator.py"]

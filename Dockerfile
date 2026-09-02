FROM python:3.11-slim

WORKDIR /app

RUN useradd -u 1000 -ms /bin/bash appuser && chown -R appuser:appuser /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

ENTRYPOINT ["python", "orchestrator.py"]

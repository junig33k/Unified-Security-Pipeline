FROM python:3.11-slim

WORKDIR /app

RUN useradd -u 1000 -ms /bin/bash appuser && chown -R appuser:appuser /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip "setuptools>=79.0.2" "wheel>=0.46.3" && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

ENTRYPOINT ["python", "orchestrator.py"]

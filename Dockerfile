FROM python:3.12-slim

# Isolation : utilisateur non-root (ID 1000)
RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY . /app
RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["python", "orchestrator.py"]

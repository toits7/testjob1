FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

ARG HTTP_SERVER_PORT

ENV HTTP_SERVER_PORT=${HTTP_SERVER_PORT}

RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN mkdir -p /app && chown -R appuser:appuser /app

USER appuser

WORKDIR /app

COPY --chown=appuser:appuser backend/main.py .

EXPOSE ${HTTP_SERVER_PORT}

CMD ["python", "main.py"]
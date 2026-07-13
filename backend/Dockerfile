ARG HTTP_SERVER_PORT

FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/main.py .

COPY .env .

EXPOSE ${HTTP_SERVER_PORT}

CMD ["python", "main.py"]
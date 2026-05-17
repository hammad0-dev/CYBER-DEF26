FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /input/logs
RUN mkdir -p /output

# Copy logs file into container
COPY input/logs/logs.csv /input/logs/logs.csv

CMD ["python", "inference.py"]

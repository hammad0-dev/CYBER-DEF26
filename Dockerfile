# Use official Python image
FROM python:3.10-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN mkdir -p /input/logs
RUN mkdir -p /output

# Run inference script
CMD ["python", "inference.py"]
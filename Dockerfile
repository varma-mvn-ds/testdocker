FROM docker.io/python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .


CMD ["python3", "app.py"]

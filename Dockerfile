FROM python:3.10-slim-buster

# Ku shub agabka muhiimka u ah in lagu dhiso maktabadaha Python
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Halkan waxaan ku cusbooneysiineynaa pip ka hor intaanan ku shubin requirements
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

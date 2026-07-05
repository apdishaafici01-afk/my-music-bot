FROM python:3.10-slim

# Ku rakib FFmpeg iyo maktabadaha nidaamka ee loo baahan yahay
RUN apt-get update && apt-get install -y ffmpeg gcc python3-dev && apt-get clean

WORKDIR /app

# Ku koobiyeey feylasha requirements-ka oo rakib
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ku koobiyeey code-ka bot-ka oo dhan
COPY . .

# Amarka kiciya bot-ka
CMD ["python", "bot.py"]


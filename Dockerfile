FROM python:3.10-slim

# 1. Ku rakib FFmpeg iyo aaladaha dhismaha nidaamka
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    python3-dev \
    glib-2.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Cusboonaysii pip oo si toos ah u rakib maktabadaha iyadoo aan la isticmaalin requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyrogram==2.0.106 pytgcalls==2.1.0 yt-dlp

# 3. Ku koobiyeey code-ka bot-ka oo dhan
COPY . .

CMD ["python", "bot.py"]

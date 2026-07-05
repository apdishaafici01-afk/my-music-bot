FROM python:3.10-slim

# Ku rakib FFmpeg iyo aaladaha dhismaha nidaamka
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    python3-dev \
    glib-2.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Si toos ah u rakib nooca shaqaynaya ee dev-ka ah ee leh tgcalls-ka saxda ah
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyrogram==2.0.106 yt-dlp && \
    pip install --no-cache-dir pytgcalls==3.0.0.dev24

# Ku koobiyeey code-ka bot-ka oo dhan
COPY . .

CMD ["python", "bot.py"]

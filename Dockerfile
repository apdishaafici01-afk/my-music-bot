FROM python:3.10-slim

# Ku rakib FFmpeg iyo aaladaha dhismaha (build-essential) ee loogu talagalay pytgcalls
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    python3-dev \
    glib-2.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Ku koobiyeey oo rakib requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Ku koobiyeey code-ka bot-ka oo dhan
COPY . .

CMD ["python", "bot.py"]

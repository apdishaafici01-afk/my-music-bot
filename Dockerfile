FROM python:3.10-slim

# Khadkan wuxuu Kinesis ku qasbayaa inay iska ilowdo xogtaas hore
ENV BUST_CACHE=1

RUN pip install --no-cache-dir pyrogram==2.0.106 tgcrypto

WORKDIR /app
COPY . .

# Halkan waxaan si toos ah ugu sheegaynaa in nidaamku akhriyo koodhkaaga
CMD ["python", "bot.py"]


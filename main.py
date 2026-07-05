import asyncio
import os
from pyrogram import Client, filters

# Xogta deegaanka rasmiga ah
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Huraay! Hadda si toos ah ayaan u shaqaynayaa, waana kuu jawaabay!")

async def main():
    print("🚀 Bot-ku wuxuu ka bilaabanayaa Kinesis...")
    await app.start()
    print("✅ Bot-kii wuxuu ku xirmay Telegram!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    

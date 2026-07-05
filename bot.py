import asyncio
import os
from pyrogram import Client, filters
from pytgcalls import GroupCallClient

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Nooca dev24 wuxuu isticmaalaa GroupCallClient
call_py = GroupCallClient(app)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("👋 Sannad Wacan! Bot-kii si guul leh ayuu u shaqaynayaa.")

async def main():
    await app.start()
    print("🚀 Bot-kii si guul leh ayuu u shaqaynayaa 24/7...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    

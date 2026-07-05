from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "🎵 Music Bot is online!\n\nUse /play after the music plugin is added."
    )

if __name__ == "__main__":
    print("Music Bot Started...")
    app.run()

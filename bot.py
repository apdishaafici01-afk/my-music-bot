import asyncio
import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import ChatUpdate

# Xogta sirta ah ee laga soo akhrinayo Kinesis environment variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if len(message.command) < 2:
        await message.reply_text("❌ Isku qor sidan: `/play [Link]`")
        return
    audio_url = message.command[1]
    await message.reply_text("🔄 Waxaan isku dayayaa inaan ku biiro Call-ka...")
    try:
        # Habka saxda ah ee v3 loogu biiro call-ka
        from pytgcalls.types import MediaStream
        await call_py.play(message.chat.id, MediaStream(audio_url))
        await message.reply_text("🎶 Hadda si guul leh ayaan ugu soo biiray Call-ka, heestiina waa shidantahay!")
    except Exception as e:
        await message.reply_text(f"❌ Cilad: {str(e)}")

@app.on_message(filters.command("stop") & filters.group)
async def stop_music(client, message):
    try:
        await call_py.leave(message.chat.id)
        await message.reply_text("⏹️ Bot-ku wuxuu ka baxay Call-ka.")
    except Exception as e:
        await message.reply_text(f"❌ Cilad: {str(e)}")

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("👋 Sannad Wacan! Waxaan ahay Bot-ka Muusigga ee Group-yada. Igu dar group-kaaga si aan idiinku shido heeso!")

async def main():
    await app.start()
    await call_py.start()
    print("🚀 Bot-kii si guul leh ayuu u shaqaynayaa 24/7...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    

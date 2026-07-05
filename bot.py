import asyncio
import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

# Waxaan xogta ka soo qaadanaynaa gudaha Railway (Environment Variables)
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if len(message.command) < 2:
        await message.reply_text("❌ Isku qor sidan: `/play [Link-ga Muusigga]`")
        return
    audio_url = message.command[1]
    chat_id = message.chat.id
    await message.reply_text("🔄 Waxaan isku dayayaa inaan ku biiro Call-ka...")
    try:
        await call_py.join_group_call(chat_id, AudioPiped(audio_url))
        await message.reply_text("🎶 Hadda si guul leh ayaan ugu soo biiray Call-ka!")
    except Exception as e:
        await message.reply_text(f"❌ Cilad: {str(e)}")

@app.on_message(filters.command("stop") & filters.group)
async def stop_music(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏹️ Bot-ku wuxuu ka baxay Call-ka.")
    except Exception as e:
        await message.reply_text(f"❌ Cilad: {str(e)}")

async def main():
    await app.start()
    await call_py.start()
    print("🚀 Bot-kii wuxuu u shaqaynayaa si toos ah...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
  

import asyncio
import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING_SESSION = os.getenv("STRING_SESSION")

bot = Client(
    name="MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

user = Client(
    name="UserBot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

call = PyTgCalls(user)

@bot.on_message(filters.command("start") & filters.private)
async def start_private(client, message):
    await message.reply_text(
        f"Haye {message.from_user.mention}!\n\n"
        "Waxaan ahay Music Bot Voice Chat ah. 🎧\n"
        "Ku dar group-kaaga ka dibna isticmaal amarka `/play`."
    )

@bot.on_message(filters.command("play") & filters.group)
async def play_audio(client, message):
    test_audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    chat_id = message.chat.id
    
    await message.reply_text("🔄 **Fadlan sug... Waxaan ku biirayaa Voice Chat-ka...**")

    try:
        await call.play(
            chat_id,
            AudioPiped(test_audio_url)
        )
        await message.reply_text("▶️ **Bot-ku wuxuu si guul leh u dhex galay Voice Chat-ka, muusikadii tijaabaduna waa ay daarantaa!**")
    except Exception as e:
        await message.reply_text(f"❌ **Aniga iyo Call-ka ma is heli weynay:**\n`{str(e)}`")

async def main():
    await bot.start()
    await user.start()
    await call.start()
    print("---------------------------------------")
    print("🔥 BOT-KII WAA ONLINE (BOT.PY) ! 🔥")
    print("---------------------------------------")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    

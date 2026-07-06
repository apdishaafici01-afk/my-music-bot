from pyrogram import Client, filters
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp, os

os.makedirs("downloads", exist_ok=True)

async def download_audio(query):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        if query.startswith("http"):
            info = ydl.extract_info(query, download=True)
        else:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)["entries"][0]
        return ydl.prepare_filename(info), info["title"]

@Client.on_message(filters.command("play") & filters.group)
async def play_cmd(client, message):
    if len(message.command) < 2:
        await message.reply_text("Fadlan qor magaca ama link-ka: /play <hees>")
        return

    query = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    msg = await message.reply_text("🔍 Soo dejinaya heesta...")

    try:
        file_path, title = await download_audio(query)
    except Exception as e:
        await msg.edit_text(f"⚠️ Qalad soo dejinta: {e}")
        return

    try:
        await client.call_py.join_group_call(chat_id, AudioPiped(file_path))
        await msg.edit_text(f"▶️ Hadda la Ciyaarayaa: {title} 🎶")
    except Exception as e:
        await msg.edit_text(f"⚠️ Kama biiri karo VC: {e}\n\nHubi assistant-ku group-ka ku jiro oo VC furan yahay.")

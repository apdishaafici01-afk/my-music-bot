from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import yt_dlp

waiting_for_song = {}  # user_id -> True

@Client.on_callback_query(filters.regex("search_song"))
async def ask_song(client, callback_query):
    user_id = callback_query.from_user.id
    waiting_for_song[user_id] = True
    await callback_query.message.reply_text("🔍 Codso Magaca Heesta, Codka ama Link-ka:")
    await callback_query.answer()

@Client.on_message(filters.private & filters.text & ~filters.command(["start", "play", "pause", "skip", "stop"]))
async def handle_song_query(client, message):
    user_id = message.from_user.id
    if not waiting_for_song.get(user_id):
        return

    waiting_for_song[user_id] = False
    query = message.text
    msg = await message.reply_text(f"🔍 Radinaya: {query} ...")

    ydl_opts = {"format": "bestaudio", "noplaylist": True, "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch5:{query}", download=False)
        results = info["entries"]

    buttons = []
    for entry in results:
        title = entry["title"][:40]
        buttons.append([InlineKeyboardButton(f"🎵 {title}", callback_data=f"play_{entry['id']}")])

    await msg.edit_text("Hesta aad Rabto Dooro 🎵:", reply_markup=InlineKeyboardMarkup(buttons))

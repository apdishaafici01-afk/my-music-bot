from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user_name = message.from_user.first_name
    bot_username = client.me.username

    text = f"Hi {user_name}, Add Your Group or Search Song? 🔥"

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "➕ Add Your Group",
            url=f"https://t.me/{bot_username}?startgroup=true&admin=manage_video_chats+delete_messages+invite_users"
        )],
        [InlineKeyboardButton("🔍 Search Song", callback_data="search_song")]
    ])

    await message.reply_text(text, reply_markup=buttons)

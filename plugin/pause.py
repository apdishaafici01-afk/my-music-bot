from pyrogram import Client, filters

@Client.on_message(filters.command("pause") & filters.group)
async def pause_cmd(client, message):
    try:
        await client.call_py.pause_stream(message.chat.id)
        await message.reply_text("⏸ Hesta waa la joojiyay.")
    except Exception as e:
        await message.reply_text(f"⚠️ Qalad: {e}")

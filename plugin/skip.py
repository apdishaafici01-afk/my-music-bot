from pyrogram import Client, filters

@Client.on_message(filters.command("skip") & filters.group)
async def skip_cmd(client, message):
    try:
        await client.call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏭ Waa la gudbay. Qor /play hees kale.")
    except Exception as e:
        await message.reply_text(f"⚠️ Qalad: {e}")

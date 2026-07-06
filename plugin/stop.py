from pyrogram import Client, filters

@Client.on_message(filters.command("stop") & filters.group)
async def stop_cmd(client, message):
    try:
        await client.call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏹ Dhammaan waa la joojiyay, Bot-ku VC-ga wuu ka baxay.")
    except Exception as e:
        await message.reply_text(f"⚠️ Qalad: {e}")

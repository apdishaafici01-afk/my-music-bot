from pyrogram import Client
from pytgcalls import PyTgCalls
import config

app = Client(
    "music_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

call_py = PyTgCalls(app)

if __name__ == "__main__":
    print("Bot is starting...")
    app.start()
    call_py.start()
    print("Bot started successfully!")
    from pyrogram import idle
    idle()

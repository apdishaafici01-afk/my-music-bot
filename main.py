from pyrogram import Client, idle
from pytgcalls import PyTgCalls
import config

# Bot-ka (wuxuu maamulaa commands sida /play /skip)
app = Client(
    "music_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Userbot-ka (kani ayaa runtii ku biiraya Voice Chat-ka)
assistant = Client(
    "assistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION_STRING
)

call_py = PyTgCalls(assistant)

if __name__ == "__main__":
    print("Starting bot...")
    app.start()
    print("Starting assistant...")
    assistant.start()
    call_py.start()
    print("Bot iyo Assistant labaduba way shaqeynayaan!")
    idle()

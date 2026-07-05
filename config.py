import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

STRING_SESSION = os.getenv("STRING_SESSION", "")
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split() if x]

BOT_NAME = os.getenv("BOT_NAME", "Music Bot")
